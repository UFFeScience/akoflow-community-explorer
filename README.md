# AkôFlow Community Explorer

Operational queue for small, reproducible scientific workflows implemented and
published in the AkôFlow Community Explorer.

The repository is issue-first: research is captured in an issue before code is
written. The same issue then tracks implementation, daemon execution, validation,
Hub publication, and anonymous public verification.

## What belongs here

Each candidate issue must identify:

- the paper, authors, persistent identifier, code, data, and licenses;
- the exact result to reproduce (figure, table, map, curve, or metric);
- whether the scope is a full reproduction, a paper slice, or a method adaptation;
- the pinned inputs, parameters, versions, seeds, and expected CPU resources;
- an acceptance criterion and tolerance fixed before implementation;
- the scientific activities, their dependencies, parallel branches, aggregation,
  and expected artifacts;
- why the candidate adds a new scientific question or method to the catalog;
- provenance, redistribution constraints, limitations, risks, and open questions;
- a proposed README/gallery plan, including a scientific figure and measured DAG
  or timeline evidence.

Prefer candidates with at least two independent scientific activities that can run
in parallel: ensembles, geographic tiles, parameter sweeps, independent
simulations, or method/scenario comparisons. Generating PNG and GIF files in
parallel does not by itself qualify a workflow as scientifically parallel.

## Issue states

- `research`: evidence is still being collected.
- `qualified`: inputs, licenses, novelty, DAG, and acceptance criteria are clear.
- `needs-data`: blocked on a usable or redistributable dataset.
- `needs-method`: the paper does not yet provide enough detail for reproduction.
- `duplicate`: better represented as a profile or version of an existing workflow.
- `ready-for-implementation`: reviewed and suitable for a separate implementation
  task.
- `implementing`: source, image, DAG, and validation are being built.
- `executing`: the reference scenario is running through the AkôFlow daemon.
- `publishing`: the validated reference run is being attached to a Hub version.
- `published`: the public page, gallery, imports, and result links were verified
  without an authenticated session.
- `blocked`: the next action requires external data, permission, credentials, or
  another state change; the issue must say exactly what is missing.

An issue is closed only after it has the `published` label and a final comment with
the public URL, run ID, workflow version, image digest, validation result, measured
parallel overlap, and artifact checksums. Failed or incomplete candidates remain
open with a precise blocker; duplicates may be closed after linking the canonical
workflow/version.

## Hourly worker

`automation/run-hourly.sh` starts one Codex worker in this workspace. The user-level
`akoflow-community-explorer.timer` runs hourly and never overlaps an active worker.
Each invocation reads the live GitHub issues, resumes the oldest actionable issue,
and leaves durable evidence in the issue and repository. See
`automation/worker-prompt.md` for the execution and publication gates.

## Propose a workflow

Open a **Scientific workflow candidate** issue and complete every applicable
section. Link primary sources whenever possible and clearly distinguish facts from
inferences or implementation ideas.
