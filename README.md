# AkôFlow Community Explorer

Research backlog for small, reproducible scientific workflows that can later be
implemented and published in the AkôFlow Community Explorer.

This repository is intentionally issue-first. An issue is a researched proposal,
not evidence that a workflow has been implemented, executed, validated, or
published.

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

Implementation, daemon execution, Hub publication, and public verification are out
of scope for this repository's initial phase.

## Propose a workflow

Open a **Scientific workflow candidate** issue and complete every applicable
section. Link primary sources whenever possible and clearly distinguish facts from
inferences or implementation ideas.
