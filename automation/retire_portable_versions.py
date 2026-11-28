#!/usr/bin/env python3
"""Verify the public replacements and retire only the recorded older versions."""

import argparse
import hashlib
import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen
from uuid import UUID


HUB = "https://hub.akoflow.com"
PROJECT = "44e9e6b5-454b-43b9-bf73-240be5e31aab"
INVENTORY = Path(__file__).resolve().parents[1] / "PORTABILITY-RETIREMENT-CANDIDATES.json"


def request(url, method="GET", token=None):
    headers = {"Authorization": f"Bearer {token}"} if token else {}
    with urlopen(Request(url, method=method, headers=headers), timeout=30) as response:
        return response.read()


def checked_versions(entry):
    publication_id = str(UUID(entry["publicationId"]))
    endpoint = f"{HUB}/api/v1/publications/{publication_id}"
    publication = json.loads(request(endpoint))
    if publication["projectId"] != PROJECT or publication["visibility"] != "public":
        raise ValueError(f"{entry['slug']}: public project changed")
    if publication["slug"] != entry["slug"]:
        raise ValueError(f"{publication_id}: publication slug changed")
    versions = json.loads(request(f"{endpoint}/versions"))
    numbers = {version["number"] for version in versions}
    replacement = entry["replacementVersion"]
    if not numbers or max(numbers) != replacement:
        raise ValueError(f"{entry['slug']}: the recorded replacement is no longer current")
    digest = hashlib.sha256(request(f"{endpoint}/versions/{replacement}/yaml")).hexdigest()
    if digest != entry["replacementYAMLSHA256"]:
        raise ValueError(f"{entry['slug']}: the replacement YAML changed")
    return numbers


def retire(entry, version, daemon, token):
    identity = json.loads(request(f"{daemon}/hub/status/", token=token))
    if (not identity.get("connected") or identity.get("readOnly")
            or identity.get("hubUrl") != HUB
            or identity.get("identity", {}).get("projectId") != PROJECT):
        raise ValueError("Connect a writable daemon to the Community Explorer project")
    publication = str(UUID(entry["publicationId"]))
    replacement = entry["replacementVersion"]
    route = f"{daemon}/hub/publications/{publication}/versions/{version}/?replacement={replacement}"
    result = json.loads(request(route, method="DELETE", token=token))
    if result.get("retired") is not True or version in checked_versions(entry):
        raise ValueError(f"{entry['slug']}: retirement was not confirmed")
    check_unavailable(entry, version)


def check_unavailable(entry, version):
    publication = str(UUID(entry["publicationId"]))
    old_yaml = f"{HUB}/api/v1/publications/{publication}/versions/{version}/yaml"
    try:
        request(old_yaml)
    except HTTPError as error:
        if error.code not in (404, 410):
            raise
    else:
        raise ValueError(f"{entry['slug']}: retired v{version} remains anonymously downloadable")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", help="Limit the run to this publication slug")
    parser.add_argument("--apply", action="store_true", help="Retire the verified older versions")
    args = parser.parse_args()
    daemon = os.environ.get("AKOFLOW_API_URL", "http://127.0.0.1:8080/akoflow-api").rstrip("/")
    token = os.environ.get("AKOFLOW_API_TOKEN")
    if args.apply and not token:
        parser.error("--apply requires AKOFLOW_API_TOKEN")
    entries = json.loads(INVENTORY.read_bytes())
    entries = [entry for entry in entries if args.slug is None or entry["slug"] == args.slug]
    if not entries:
        parser.error("No matching publication in the retirement inventory")
    checked = pending = 0
    for entry in entries:
        if entry["cleanRunStatus"] != "completed" or not entry["archivedContextPresent"]:
            raise ValueError(f"{entry['slug']}: the inventory lacks clean-run evidence")
        replacement = entry["replacementVersion"]
        numbers = checked_versions(entry)
        for version in sorted(entry["publishedOlderVersions"]):
            if version < 1 or version >= replacement:
                raise ValueError(f"{entry['slug']}: invalid historical version")
            if version not in numbers:
                check_unavailable(entry, version)
                print(f"{entry['slug']} v{version} already absent")
                continue
            pending += 1
            if args.apply:
                retire(entry, version, daemon, token)
            action = "retired" if args.apply else "eligible to retire"
            print(f"{entry['slug']} v{version} {action}; v{replacement} verified")
        checked += 1
    action = "retired" if args.apply else "eligible"
    print(f"{checked} verified replacements; {pending} older versions {action}")


if __name__ == "__main__":
    main()
