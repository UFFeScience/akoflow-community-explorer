#!/usr/bin/env python3
"""Register minimal portable build contexts and upgrade legacy workflow YAML.

The script intentionally archives only the Dockerfile and paths named by
Dockerfile COPY/ADD instructions. It refuses remote ADD sources, escaping
paths, unpinned base images, oversized contexts, and workflows whose command
shape cannot be upgraded without review.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import io
import json
import os
from pathlib import Path, PurePosixPath
import re
import shlex
import tarfile
import urllib.error
import urllib.request


MAX_COMPRESSED = 4 * 1024 * 1024
MAX_EXPANDED = 16 * 1024 * 1024
MAX_ENTRIES = 2048
BUILD_SOURCE = (
    "{source: {type: build, artifactBuildRef: %s}, "
    "delivery: {strategy: auto, targetFormat: oci}}"
)


def logical_lines(text: str) -> list[str]:
    lines: list[str] = []
    current = ""
    for raw in text.splitlines():
        stripped = raw.strip()
        current = f"{current} {stripped}".strip()
        if current.endswith("\\"):
            current = current[:-1].rstrip()
            continue
        lines.append(current)
        current = ""
    if current:
        lines.append(current)
    return lines


def docker_sources(dockerfile: str) -> list[str]:
    sources: list[str] = []
    for line in logical_lines(dockerfile):
        if not re.match(r"^(COPY|ADD)\s", line, re.I):
            continue
        tokens = shlex.split(line)
        operands = [token for token in tokens[1:] if not token.startswith("--")]
        if len(operands) < 2:
            raise ValueError(f"unsupported Dockerfile instruction: {line}")
        for source in operands[:-1]:
            if "://" in source:
                raise ValueError(f"remote ADD source is not portable: {source}")
            path = PurePosixPath(source)
            if path.is_absolute() or ".." in path.parts or any(ch in source for ch in "*?["):
                raise ValueError(f"unsafe or globbed build source: {source}")
            sources.append(source.rstrip("/"))
    return sorted(set(sources))


def validate_base_images(dockerfile: str) -> None:
    for line in logical_lines(dockerfile):
        if not line.upper().startswith("FROM "):
            continue
        image = line.split()[1]
        if image.lower() == "scratch" or image.startswith("$"):
            continue
        if "@sha256:" not in image:
            raise ValueError(f"base image is not pinned by digest: {image}")


def add_path(tar: tarfile.TarFile, root: Path, relative: str, entries: int, size: int) -> tuple[int, int]:
    path = root / relative
    if not path.exists():
        raise ValueError(f"COPY/ADD source does not exist: {relative}")
    paths = [path]
    if path.is_dir():
        paths.extend(sorted(p for p in path.rglob("*") if p.is_file() or p.is_symlink()))
    for item in paths:
        if item.is_dir():
            continue
        resolved = item.resolve()
        if root.resolve() not in resolved.parents and resolved != root.resolve():
            raise ValueError(f"build source escapes context: {item}")
        arcname = item.relative_to(root).as_posix()
        info = tar.gettarinfo(str(item), arcname=arcname)
        info.uid = info.gid = 0
        info.uname = info.gname = ""
        info.mtime = 0
        entries += 1
        size += info.size
        if entries > MAX_ENTRIES or size > MAX_EXPANDED:
            raise ValueError(f"context exceeds archive limits at {arcname}")
        if info.isfile():
            with item.open("rb") as handle:
                tar.addfile(info, handle)
        else:
            tar.addfile(info)
    return entries, size


def context_archive(root: Path, dockerfile_path: Path) -> tuple[bytes, dict[str, int]]:
    dockerfile = dockerfile_path.read_text()
    validate_base_images(dockerfile)
    sources = docker_sources(dockerfile)
    raw = io.BytesIO()
    entries = expanded = 0
    with tarfile.open(fileobj=raw, mode="w") as tar:
        for source in [dockerfile_path.relative_to(root).as_posix(), *sources]:
            entries, expanded = add_path(tar, root, source, entries, expanded)
    compressed = io.BytesIO()
    with gzip.GzipFile(fileobj=compressed, mode="wb", mtime=0) as stream:
        stream.write(raw.getvalue())
    archive = compressed.getvalue()
    if entries > MAX_ENTRIES:
        raise ValueError(f"context has {entries} entries; limit is {MAX_ENTRIES}")
    if expanded > MAX_EXPANDED:
        raise ValueError(f"context expands to {expanded} bytes; limit is {MAX_EXPANDED}")
    if len(archive) > MAX_COMPRESSED:
        raise ValueError(f"context compresses to {len(archive)} bytes; limit is {MAX_COMPRESSED}")
    return archive, {"entries": entries, "expandedBytes": expanded, "compressedBytes": len(archive)}


def register(api: str, token: str, archive: bytes) -> dict:
    body = json.dumps(
        {
            "contextArchive": base64.b64encode(archive).decode(),
            "recipePath": "docker/Dockerfile",
            "platform": "linux/amd64",
        }
    ).encode()
    request = urllib.request.Request(
        f"{api.rstrip('/')}/artifacts/recipe/",
        data=body,
        method="POST",
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.load(response)
    except urllib.error.HTTPError as error:
        raise RuntimeError(f"recipe registration failed ({error.code}): {error.read().decode()}") from error


def upgrade_workflow(path: Path, build_id: str) -> None:
    text = path.read_text()
    if "\n  image:" not in text:
        raise ValueError("workflow does not contain a legacy spec.image")
    text = re.sub(r"\n  image:[^\n]+", "", text, count=1)
    marker = "command: {entrypoint:"
    count = text.count(marker)
    if count == 0:
        raise ValueError("workflow has no supported inline activity commands")
    source = BUILD_SOURCE % build_id
    text = text.replace(marker, f"command: {{executable: &portable_image {source}, entrypoint:", 1)
    text = text.replace(marker, "command: {executable: *portable_image, entrypoint:")
    if " image:" in text or text.count("&portable_image") != 1 or text.count("*portable_image") != count - 1:
        raise ValueError("workflow upgrade invariant failed")
    path.write_text(text)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("workflows", nargs="+", type=Path)
    parser.add_argument("--api", default=os.environ.get("AKOFLOW_API_URL", "http://127.0.0.1:8080/akoflow-api"))
    parser.add_argument("--token", default=os.environ.get("AKOFLOW_API_TOKEN", "akoflow-development-token"))
    parser.add_argument("--manifest", type=Path)
    args = parser.parse_args()
    results: list[dict] = []
    failed = False
    for workflow in args.workflows:
        directory = workflow.parent
        label = directory.relative_to(args.root).as_posix()
        try:
            archive, metrics = context_archive(directory, directory / "docker/Dockerfile")
            response = register(args.api, args.token, archive)
            build_id = response["build"]["id"]
            upgrade_workflow(workflow, build_id)
            result = {"workflow": label, "status": "upgraded", "artifactBuildRef": build_id, **metrics}
        except Exception as error:  # report every workflow in one pass
            failed = True
            result = {"workflow": label, "status": "failed", "error": str(error)}
        results.append(result)
        print(json.dumps(result, sort_keys=True))
    if args.manifest:
        args.manifest.parent.mkdir(parents=True, exist_ok=True)
        args.manifest.write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
