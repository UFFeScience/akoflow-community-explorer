# Community Explorer portability audit

Scope: publications with receipts for production project
`44e9e6b5-454b-43b9-bf73-240be5e31aab`.

The table below records the initial receipt-based audit. The expanded audit
covers all 31 workflow definitions in the Community Explorer namespace,
including publications without local receipts. All 31 definitions now select
build recipes in the local worktree. OceanBench, The Well, and PDEBench
download and verify pinned public inputs at image build time because the
datasets exceed the recipe archive limit. Their portable reference runs
are `community-oceanbench-glonet-run-v3`,
`community-well-radiative-layer-portable-run-v2`, and
`community-pdebench-advection-portable-run-v4`. Earlier OceanBench and
PDEBench attempts were cancelled after their network operations stopped
progressing. PDEBench's later build `community-pdebench-advection-portable-run-v7`
stalled during the DaRUS dataset download and failed in image preparation.
The worker submitted `community-pdebench-advection-portable-run-v8` with
smaller HTTP ranges after testing the frozen dataset download.

The anonymous latest-version YAML check initially found archived build contexts
in 11 of the 31 public entries. Four additional portable revisions have since
passed reference execution and anonymous YAML verification, bringing the
count to 15. CHSH v2 has since passed its nine-activity reference run,
scientific validation, and anonymous YAML verification, bringing the original
31-entry cohort to 16 portable public revisions and 15 pending updates.
RR Lyrae's portable reference run `community-rrlyrae-portable-run-v2` is
underway. Preflight confirmed image reconstruction on all ten activities.

OceanBench and Buffon v2 imported successfully from their public URIs into
the isolated installation. Preflight confirmed image reconstruction was
required for 13/13 and 8/8 activities, respectively. Runs
`oceanbench-hub-v2-clean-uri` and `buffon-hub-v2-clean-uri` are in progress.
Shannon BSC and The Well still await isolated URI execution.
CHSH v2 imported into the same isolated installation and reported a required
image build for 9/9 activities. Run `chsh-hub-v2-clean-uri` is in progress.

| Workflow | Completed activities | Public revision |
| --- | ---: | --- |
| Shannon BSC | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/shannon-bsc-capacity-audit) |
| Buffon needle | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/buffon-needle-pi-audit) |
| The Well radiative layer | 13/13 | [v2](https://hub.akoflow.com/o/akoflow/the-well-radiative-mixing-layer) |
| OceanBench GLONet | 13/13 | [v2](https://hub.akoflow.com/o/akoflow/oceanbench-glonet-metric-reproduction) |
| CHSH singlet correlation | 9/9 | [v2](https://hub.akoflow.com/o/akoflow/chsh-singlet-correlation-audit) |

Volterra's portable revision reported “Build required” on all seven activities
and completed 7/7 in daemon run `community-volterra-predator-prey-run-v2`.
The corrected revision is public as Volterra version 2. Import via
`akoflow://hub/publications/36509a08-f4f3-43d3-9a20-ffe47116fb16/versions/2`
returned seven build sources and seven archived contexts on the existing
daemon. The URI also imported into an isolated AkôFlow database with an empty
Docker image store and a fresh BuildKit instance. All seven activities
reported that the image needed to be built. AkôFlow rebuilt the image and
completed 7/7 activities in `volterra-hub-v2-clean-uri` against the imported
definition. The final `validation.json` reported `passed: true`. Version 1
remains public pending a version-scoped retirement operation.

Keep one public, verified portable version per workflow. Verify the replacement
through anonymous Hub import and execution before retiring the legacy version.
The daemon's publication deletion endpoint removes the entire publication, so
it must never be used to retire v1 from a publication that also holds the
verified replacement.

An item passes only after its public YAML contains an archived AkôFlow build
context, every Dockerfile `COPY`/`ADD` source is contained by that context, the
base image is pinned by digest, an unmaterialized preflight reports that a build
is required, and both image reconstruction and the full workflow finish through
the daemon.

| Workflow | Local image audit | Clean rebuild and rerun |
| --- | --- | --- |
| Newman–Ziff percolation | portable build context; all `COPY` sources contained | passed, public v2 |
| Jarzynski dragged trap | portable build context; all `COPY` sources contained | passed, public v2 |
| Brachistochrone audit | portable build context; all `COPY` sources contained | passed, public v2 |
| Foucault precession | portable build context; all `COPY` sources contained | passed, public v2 |
| Hénon map audit | portable build context; all `COPY` sources contained | passed, public v2 |
| Airy diffraction | portable build context; all `COPY` sources contained | passed, public v2 |
| Rabi oscillations | portable build context; all `COPY` sources contained; base digest pinned | passed, public v2 |
| Cooley–Tukey FFT | portable build context; all `COPY` sources contained | passed, public v2 |
| Debye heat capacity | portable build context; all `COPY` sources contained | passed, public v2 |

Initial receipt-based sample: 9 publications, all with successful reference
runs and portable public revisions. The expanded 31-workflow audit above
includes entries without local receipts.
