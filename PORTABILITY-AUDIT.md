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
`community-pdebench-advection-portable-run-v8`. Earlier OceanBench and
PDEBench attempts were cancelled after their network operations stopped
progressing. PDEBench's later build `community-pdebench-advection-portable-run-v7`
stalled during the DaRUS dataset download and failed in image preparation.
Version 8 restored the frozen 823,298,048-byte slice in verified 64 MiB ranges,
rebuilt image digest
`sha256:451b5a699d5eb16e2d364c732f9fcb1c488ae7dd9e8f02d47a70da62bf43a52e`,
and completed 7/7 activities. Its validator passed all required-file,
comparison, and rounding checks. FNO and U-Net inference overlapped from
`1795417547.912340` through `1795417574.536844` in daemon timestamps.

The anonymous latest-version YAML check initially found archived build contexts
in 11 of the 31 public entries. Four additional portable revisions have since
passed reference execution and anonymous YAML verification, bringing the
count to 15. CHSH, PDEBench, Ising–Yang, RR Lyrae, Bateman and Robertson v2 have since passed reference
execution, scientific validation and anonymous YAML verification. The original
31-entry cohort now has 21 portable public revisions and 10 pending updates.
RR Lyrae's first portable build failed resolving Docker Hub. Retry
`community-rrlyrae-portable-run-v2-retry1` rebuilt image digest
`sha256:70817d6a3e26df122d0989345412d3ffa9ec62faa2c2b2d13ee4a519f3567785`
and completed 10/10 activities. Its validator passed the period, input,
figure, and animation checks with absolute period error
`7.568748147634974e-05` days against the `0.001`-day tolerance. The six
periodogram branches overlap in measured daemon timestamps. The public v2
capture is associated with the separately validated reference run
`community-rrlyrae-portable-run-v2-retry`.
Bateman run `community-bateman-decay-portable-run-v2` completed 7/7
activities and reported `overall_pass: true`. Lorenz's reference run
`community-lorenz-portable-run-v2` was submitted after preflight confirmed
that all eight activities required a build. Hodgkin–Huxley reference run
`community-hodgkin-huxley-portable-run-v3` was submitted after fifteen
activities reported a required build.

The latest anonymous audit checked each publication's project, latest version,
and every activity's build source and embedded context. The following latest
public revisions still require replacement.

| Publication | Public version | Activities with archived build context |
| --- | ---: | ---: |
| [caco2-scaffold-split-baselines](https://hub.akoflow.com/o/akoflow/caco2-scaffold-split-baselines) | 1 | 0/19 |
| [bioclip-rare-species-evaluation](https://hub.akoflow.com/o/akoflow/bioclip-rare-species-evaluation) | 1 | 0/12 |
| [lorenz-bounded-sensitivity-ensemble](https://hub.akoflow.com/o/akoflow/lorenz-bounded-sensitivity-ensemble) | 1 | 0/8 |
| [turing-schnakenberg-pattern-selection](https://hub.akoflow.com/o/akoflow/turing-schnakenberg-pattern-selection) | 1 | 0/9 |
| [kimura-wright-fisher-fixation](https://hub.akoflow.com/o/akoflow/kimura-wright-fisher-fixation) | 1 | 0/28 |
| [hodgkin-huxley-excitation-boundary](https://hub.akoflow.com/o/akoflow/hodgkin-huxley-excitation-boundary) | 1 | 0/15 |
| [sir-threshold-final-size-sweep](https://hub.akoflow.com/o/akoflow/sir-threshold-final-size-sweep) | 1 | 0/12 |
| [stardist-equivariance-sweep](https://hub.akoflow.com/o/akoflow/stardist-equivariance-sweep) | 1 | 0/12 |
| [mfc-sod-shock-tube-refinement](https://hub.akoflow.com/o/akoflow/mfc-sod-shock-tube-refinement) | 1 | 0/12 |
| [weatherbench2-era5-score-audit](https://hub.akoflow.com/o/akoflow/weatherbench2-era5-score-audit) | 1 | 0/10 |

The SIR threshold reference run `community-sir-threshold-sweep-portable-run-v3`
was submitted after all twelve activities requested image reconstruction.
Turing–Schnakenberg run `community-turing-portable-run-v2` was submitted
after all nine activities requested image reconstruction. Wright–Fisher run
`community-wright-fisher-portable-run-v2` was submitted after all 28
activities requested an image build. The StarDist portable definition and
schedule are registered. Its first preflight timed out on artifact
compatibility. The daemon accepted `community-stardist-portable-run-v2`;
the runner now requires a passing preflight before future submissions.
MFC Sod reference run `community-mfc-sod-portable-run-v3` was submitted
with a passing preflight and required builds on all 12 activities.
WeatherBench 2's portable workflow, runner, and schedule are on the examples
main branch. The archived context validated with nine entries. Production
registration returned HTTP 503 before dispatch while persisting its request
audit. The revised workflow and schedule were absent on follow-up, and no
reference run was submitted on the first attempt. The Caco-2 baseline's
portable workflow, plan, and runner are on the examples main branch. The
archived build context validated with three entries.

Eleven v2 revisions completed after URI import in the isolated installation
and passed their scientific validators. The run IDs were
`volterra-hub-v2-clean-uri`, `buffon-hub-v2-clean-uri`,
`chsh-hub-v2-clean-uri`, `pdebench-hub-v2-clean-uri`,
`ising-hub-v2-clean-uri`, `shannon-hub-v2-clean-uri`,
`well-hub-v2-clean-uri-retry`, `bateman-hub-v2-clean-uri`,
`rrlyrae-hub-v2-clean-uri-retry`, `robertson-hub-v2-clean-uri`, and
`foucault-hub-v2-clean-uri`. Foucault completed 9/9 activities and its
validator reported `passed: true`.
Rabi, Hénon, and Airy diffraction v2 imported from the Hub and reported
required builds for all eight, eight, and seven activities, respectively.
Their isolated runs are `rabi-hub-v2-clean-uri`, `henon-hub-v2-clean-uri`,
and `airy-hub-v2-clean-uri`. Jarzynski and Cooley–Tukey v2 also
imported from the Hub and reported required builds on all 22 and eight
activities. Their isolated runs are `jarzynski-hub-v2-clean-uri` and
`cooley-hub-v2-clean-uri`.
OceanBench v2 recovered some input files but failed twice on transient DNS
errors during the public data fetch. OceanBench reference run
`community-oceanbench-glonet-run-v4` uses bounded backoff for public downloads
and retains the pinned manifest and object checksums. BuildKit record
`l9jd82b8rjh9pd6aqe9i6gwxr` completed the download, verification and Docker
image export with manifest
`sha256:f5d830ecbcca7b5077264884d6abf3d91c8e1a21d7abebc254391a11cf8178b1`.
The reference workflow execution is pending completion.

| Workflow | Completed activities | Public revision |
| --- | ---: | --- |
| Shannon BSC | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/shannon-bsc-capacity-audit) |
| Buffon needle | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/buffon-needle-pi-audit) |
| The Well radiative layer | 13/13 | [v2](https://hub.akoflow.com/o/akoflow/the-well-radiative-mixing-layer) |
| OceanBench GLONet | 13/13 | [v2](https://hub.akoflow.com/o/akoflow/oceanbench-glonet-metric-reproduction) |
| CHSH singlet correlation | 9/9 | [v2](https://hub.akoflow.com/o/akoflow/chsh-singlet-correlation-audit) |
| PDEBench advection | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/pdebench-advection-checkpoint-audit) |
| Ising–Yang magnetization | 12/12 | [v2](https://hub.akoflow.com/o/akoflow/yang-ising-magnetization-curve) |
| RR Lyrae period recovery | 10/10 | [v2](https://hub.akoflow.com/o/akoflow/sparse-multiband-rrlyrae-period-recovery) |
| Bateman decay chain | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/bateman-decay-chain-equilibrium-audit) |
| Robertson stiff solver | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/robertson-stiff-solver-agreement) |

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
