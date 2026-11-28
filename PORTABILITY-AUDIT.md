# Community Explorer portability audit

Scope: publications with receipts for production project
`44e9e6b5-454b-43b9-bf73-240be5e31aab`.

The isolated overlay runs below completed after import from the published
URIs. Their daemon validation reports all passed.

| Run | Completed activities |
| --- | ---: |
| `oceanbench-hub-v3-clean-overlay` | 13 |
| `caco2-hub-v2-clean-overlay` | 19 |
| `turing-hub-v2-clean-overlay` | 9 |
| `hodgkin-hub-v2-clean-overlay` | 15 |
| `weatherbench-hub-v2-clean-overlay` | 10 |
| `sir-hub-v2-clean-overlay` | 12 |
| `wright-fisher-hub-v2-clean-overlay` | 28 |
| `stardist-hub-v2-clean-overlay` | 12 |
| `mfc-hub-v2-clean-overlay` | 12 |
| `bioclip-hub-v2-clean-overlay` | 12 |
| `community-prodes-hub-v1-clean` | 4 |
| `community-sisdr-hub-v1-clean` | 3 |
| `community-monash-hub-v1-clean` | 7 |
| `community-gap-bfs-hub-v1-clean` | 3 |
| `community-sobol-hub-v1-clean` | 130 |
| `community-inpe-deter-hub-v1-clean` | 74 |
| `community-ngspice-rlc-hub-v1-clean` | 130 |

Scrambled Sobol v1 was imported anonymously from
`akoflow::o/akoflow/community-explorer-issue-107-sobol-ensemble:latest` into
the isolated overlay daemon. The public YAML contains a build source and
archived context on all 130 activities, with recipe digest
`sha256:aefd17db428025e2f6396a252e070dd121277c126a40f185b0b68ae69783b540`
and context digest
`sha256:d0603330f08aa3146bcd5740960985eefc840e554cba042a616bc02792f25bbc`.
Run `community-sobol-hub-v1-clean` completed 130/130 activities in 159.019
seconds. Its validator passed 128 replicas, 1,408 estimates, 11 prefixes and
11 animation frames. The estimates CSV, convergence CSV, PNG and GIF SHA-256
digests match the recorded four-slot reference exactly.

INPE DETER v1 was imported anonymously from
`akoflow://hub/publications/5c1296ca-9f5d-4ccb-aecd-b163b03e0d25/versions/1`
into the isolated overlay daemon. All 74 activities embed the compact build
origin and archived context, with recipe digest
`sha256:64e8b11b3ea9b6a7069eb785359ae1ef1157304dae1493b3150c836f0627ec64`
and context digest
`sha256:478fc6930a97aac997b4fab184ab8f6db9e151a8ad4a68cf99281d7b61e149e9`.
Run `community-inpe-deter-hub-v1-clean` reconstructed the image and completed
74/74 activities. Its validator passed 72 monthly partitions, 334,054 alert
records, 2,491 reference groups, and 72 animation frames. The two result CSVs,
map, and animation match the portable reference SHA-256 values exactly.

ngspice RLC v1 was imported anonymously from
`akoflow://hub/publications/0e03851e-c5f1-42f4-84be-ac7d2ab1a52b/versions/1`
into the isolated overlay daemon. All 130 activities carry archived build
contexts with recipe digest
`sha256:be529b3fb56fdadec5c513d0a1a27b8022da4a010da8f3394bd9dfbe65250093`
and context digest
`sha256:e40b0c90574fea219ae57e028bb292ec56df24ac7df2904fb79611a6337fca55`.
Run `community-ngspice-rlc-hub-v1-clean` completed 130/130 activities and
validated 128 batches, 4,096 circuits, 1,056,768 samples, and five animation
frames. Its two CSVs, PNG and GIF match the recorded reference hashes. Isolated
recovery run `community-ngspice-rlc-retry-kill-isolated` retried four
interrupted batches as attempt 2 and reproduced those hashes. The interrupted
batch produced a single registered output. Two other retried blocks lost their
compressed output registrations because the retry reproduced bytes already
present in its workspace. [AkôFlow issue #565](https://github.com/UFFeScience/akoflow/issues/565)
tracks the recovery discrepancy. It did not affect the clean public URI run.

BioCLIP v2 is public and imported from its public Hub page in the isolated
daemon with all 12 activities. Each activity carries a portable build source.
The original portable reference completed all activities and passed validation.
Its capture exceeded the Hub YAML size limit, so v2 was published as a
workflow-only revision. The compact recipe downloads the identical classifier
from a pinned public commit and verifies its SHA-256 digest. The isolated run
`bioclip-hub-v2-clean-overlay` completed all 12 activities from the public v2
revision and passed all seven validation checks. Its validator SHA-256 is
`ce246762397e95414b73e5bef798eeb5922d51660fa6d96d3fbee46bb851f451`.
The clean run completed in 2,952.159 seconds with 5,785.670 compute-seconds
and 12.136 transfer-seconds. Its `predictions.csv` and result figure are
byte-identical to the validated reference (`334fd145...7f018` and
`7d19307a...2b39c`). The four measured inference overlaps were 738.300,
669.637, 619.317, and 661.889 seconds. These timestamps prove activity
overlap; no parallel speedup is claimed because there is no matching one-slot
control.

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
31-entry cohort reached 30 portable public revisions before the BioCLIP
replacement recorded above.
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
activities and reported `overall_pass: true`.
Newman–Ziff v2, Brachistochrone v2, Debye v2, and Black–Scholes v1 imported
from their public URIs and reported image builds required on all 20, seven,
seven, and eight activities. Their isolated runs were submitted as
`newman-hub-v2-clean-uri`, `brachistochrone-hub-v2-clean-uri`,
`debye-hub-v2-clean-uri`, and `black-scholes-hub-v1-clean-uri`. Lorenz's reference run
`community-lorenz-portable-run-v2` was submitted after preflight confirmed
that all eight activities required a build. Hodgkin–Huxley reference run
`community-hodgkin-huxley-portable-run-v3` was submitted after fifteen
activities reported a required build. Its first run completed preparation
and timed out while starting the parallel branches. The two-slot reference
run `community-hodgkin-huxley-portable-run-v3-two-slot` passed preflight
and was accepted with the same workflow and scientific parameters. It
completed all 15 activities and passed validation. Public Hodgkin–Huxley
v2 includes 15 archived contexts. Isolated run `hodgkin-hub-v2-clean-uri`
was submitted from the URI.

The hourly queue has also added the [Planck blackbody spectrum audit](https://hub.akoflow.com/o/akoflow/issue-53-planck-blackbody-radiation-audit) outside the original 31-entry cohort. Its public v1 YAML includes eight archived build contexts and its recorded public result is completed. [Issue #53](https://github.com/UFFeScience/akoflow-community-explorer/issues/53) records the isolated clean run evidence. The hourly queue also published the [Kepler equal-area audit](https://hub.akoflow.com/o/akoflow/community-explorer-issue-54-kepler-equal-area-v1). [Issue #54](https://github.com/UFFeScience/akoflow-community-explorer/issues/54) records an eight-activity isolated URI run with matching validation and checksums.

An anonymous refresh before BioCLIP v2 checked the 31 original publications
plus Planck and Kepler. Every activity in 32 of the 33 revisions checked
resolved to an embedded build context. BioCLIP v1 had 0/12 activities
with embedded context. An archive audit
verified the 32 embedded context and Dockerfile SHA-256 digests, checked
that archived paths are relative with regular files or directories, and
confirmed that each Dockerfile's local `COPY` and `ADD` inputs are present.
The audit uses the repository's base-image pin validation.

The same audit verified each publication's project, version, and build
sources. The following legacy revision was later superseded.

| Publication | Public version | Activities with archived build context |
| --- | ---: | ---: |
| [bioclip-rare-species-evaluation](https://hub.akoflow.com/o/akoflow/bioclip-rare-species-evaluation) | 1 | 0/12 |

First reference runs for Turing–Schnakenberg and Wright–Fisher completed
their prepare activities before executable preparation timed out on the parallel
branches. Both reproduced images are now present in the daemon's image store.
The daemon accepted Turing–Schnakenberg recovery job
`0a04acd43037d42728853dfe3481d05b` in continue mode, reusing its prepare
activity, but the retry also timed out starting local containers. Lorenz completed five activities before local container startup
timed out. A later recovery preview allowed continuation without reusable
activities. The daemon accepted recovery job `8cc3769f9aa74b10eb5fbd6ed84c5499`.
That retry also hit startup deadlines. A new reference run
`community-lorenz-portable-run-v2-two-slot` passed preflight and was submitted
with two local slots and the same scientific parameters. It completed
8/8 activities and passed scientific validation. Lorenz v2 is public with
eight embedded build contexts. `lorenz-hub-v2-clean-uri` was submitted
after all eight activities required reconstruction on URI import.
Turing–Schnakenberg also passed preflight with two local slots and was
submitted as `community-turing-portable-run-v2-two-slot`. It completed
all nine activities and passed validation. Public v2 includes nine archived
contexts. Isolated run `turing-hub-v2-clean-uri` was submitted from the URI.
WeatherBench 2 and Caco-2 first runs failed before completing an activity.
The daemon accepted WeatherBench 2 recovery job
`37903585255d8ccf514ed00898b49f53` and Caco-2 recovery job
`114bee0b19b33ac20543aa540caef99b`. Both continue from their original
execution records. Caco-2 had no reusable activities.
WeatherBench 2 recovery completed ten activities and passed validation.
The publication preview rejected that run with `source_unavailable` because
its immutable planning context was unavailable. The daemon accepted the new
reference run `community-weatherbench2-score-portable-reference-v2` after
a passing preflight. It passed validation but publication still returned
`source_unavailable`. The portable plan context measured 36,760,714 bytes,
above the publication source snapshot limit of 24 MiB. The compact recipe
downloads the same pinned public inputs during the build and checks all
hashes. Both NetCDF files matched byte-for-byte. Its archive is 4,826
bytes and the expanded plan context is 93,722 bytes. Reference run
`community-weatherbench2-score-compact-run-v3` completed 10/10 activities
and passed validation. Public WeatherBench 2 v2 has 10 embedded contexts.
Isolated run `weatherbench-hub-v2-clean-uri` was submitted from the URI.

The SIR threshold reference run `community-sir-threshold-sweep-portable-run-v3`
was submitted after all twelve activities requested image reconstruction.
Turing–Schnakenberg run `community-turing-portable-run-v2` was submitted
after all nine activities requested image reconstruction. Wright–Fisher run
`community-wright-fisher-portable-run-v2` was submitted after all 28
activities requested an image build. Its two-slot reference run
`community-wright-fisher-portable-run-v2-two-slot` passed preflight and
was accepted and completed all 28 activities with scientific validation
passing. Public Wright–Fisher v2 embeds all 28 build contexts. Isolated
run `wright-fisher-hub-v2-clean-uri` was submitted from its public URI.
The StarDist portable definition and
schedule are registered. Its first preflight timed out on artifact
compatibility. The daemon accepted `community-stardist-portable-run-v2`;
the runner now requires a passing preflight before future submissions.
The reference run completed all 12 activities and passed validation. Its
public v2 YAML embeds a build context for each activity. Run
`stardist-hub-v2-clean-uri` was submitted after a successful URI import
and twelve checks confirmed that an image build was required.
MFC Sod reference run `community-mfc-sod-portable-run-v3` was submitted
with a passing preflight and required builds on all 12 activities. Its
execution-time prerequisite check timed out before an activity started.
The daemon accepted recovery job `91c40a95e59234fdb882aeeaa00a7af7`.
The recovered reference run completed all 12 activities and validation
passed. Public MFC Sod v2 contains 12 archived contexts, and isolated test
`mfc-hub-v2-clean-uri` was submitted from its URI.
SIR's first run also stopped after its prepare activity, while preparing
executables for the parallel branches. Its two-slot reference run
`community-sir-threshold-sweep-portable-run-v3-two-slot` passed preflight
and was submitted with the same scientific settings. It completed all
12 activities and passed scientific validation. Public SIR v2 includes
12 archived contexts. Isolated run `sir-hub-v2-clean-uri` was submitted
from the public URI.
WeatherBench 2's portable workflow, runner, and schedule are on the examples
main branch. The archived context validated with nine entries. Production
registration returned HTTP 503 before dispatch while persisting its request
audit. The revised workflow and schedule were absent on follow-up, and no
reference run was submitted on the first attempt. The follow-up registration
and preflight passed, and the daemon accepted
`community-weatherbench2-score-portable-run-v2`. The Caco-2 baseline's
portable workflow, plan, and runner are on the examples main branch. The
archived build context validated with three entries. The first submission
attempt returned HTTP 503 registering its plan and stopped before launching a
run. The runner now requires a passing execution preflight. The retry passed
preflight and the daemon accepted `community-caco2-portable-run-v2`. Its
recovery finished 19/19 activities and passed validation. Public Caco-2 v2
has 19 embedded contexts and the isolated daemon imported it. A second
isolated installation using `overlay2` started with zero images and a fresh
BuildKit store. The public URI imported there, all 19 activities required
reconstruction, and its two-slot run `caco2-hub-v2-clean-overlay` was
submitted. The earlier shared daemon and its active runs were left running.
BioCLIP's archived build context validated with four entries. Its preflight
passed and the daemon accepted `community-bioclip-portable-run-v2`.
Execution-time prerequisites timed out before it started an activity.
The revised two-slot plan passed preflight with all twelve assignments
preserved. Four unreferenced Docker image caches from completed URI checks were
removed from the isolated test daemon, leaving their run records and
validation files available. Free host storage increased by about 16 GB
during cleanup. The daemon then accepted
`community-bioclip-portable-run-v2-two-slot` with a passing preflight.
The reference run has completed five activities and is executing two inference
branches. The BioCLIP README currently cites
`community-bioclip-rare-species-run-v4` and its four-slot measurements. Refresh
the recorded measurements, checksums, and linked gallery from the new validated
capture before publishing the portable revision.

Twenty-one revisions completed after URI import in the isolated installation
and passed their scientific validators. The run IDs were
`volterra-hub-v2-clean-uri`, `buffon-hub-v2-clean-uri`,
`chsh-hub-v2-clean-uri`, `pdebench-hub-v2-clean-uri`,
`ising-hub-v2-clean-uri`, `shannon-hub-v2-clean-uri`,
`well-hub-v2-clean-uri-retry`, `bateman-hub-v2-clean-uri`,
`rrlyrae-hub-v2-clean-uri-retry`, `robertson-hub-v2-clean-uri`,
`foucault-hub-v2-clean-uri`, `rabi-hub-v2-clean-uri`,
`cooley-hub-v2-clean-uri`, `henon-hub-v2-clean-uri`, and
`airy-hub-v2-clean-uri`, `jarzynski-hub-v2-clean-uri-retry`,
`brachistochrone-hub-v2-clean-uri`, `debye-hub-v2-clean-uri`,
`black-scholes-hub-v1-clean-uri`, `newman-hub-v2-clean-uri`, and
`lorenz-hub-v2-clean-overlay`. Foucault completed 9/9 activities and its
validator reported `passed: true`.
Rabi, Hénon, and Airy diffraction v2 imported from the Hub and reported
required builds for all eight, eight, and seven activities, respectively.
Their isolated runs are `rabi-hub-v2-clean-uri`, `henon-hub-v2-clean-uri`,
and `airy-hub-v2-clean-uri`. Jarzynski and Cooley–Tukey v2 also
imported from the Hub and reported required builds on all 22 and eight
activities. Rabi and Cooley–Tukey each completed eight activities and passed
scientific validation, as did Hénon (8/8) and Airy diffraction (7/7).
Jarzynski run `jarzynski-hub-v2-clean-uri` failed
during container startup after the prepare activity completed. The other
branches were cancelled after the local runtime deadline expired. The
isolated retry `jarzynski-hub-v2-clean-uri-retry` completed successfully
and reported `overall_pass: true`.
OceanBench v2 recovered some input files but failed twice on transient DNS
errors during the public data fetch. OceanBench reference run
`community-oceanbench-glonet-run-v4` uses bounded backoff for public downloads
and retains the pinned manifest and object checksums. BuildKit record
`l9jd82b8rjh9pd6aqe9i6gwxr` completed the download, verification and Docker
image export with manifest
`sha256:f5d830ecbcca7b5077264884d6abf3d91c8e1a21d7abebc254391a11cf8178b1`.
The reference run completed four activities before local container startup
timed out. The daemon accepted recovery job `12f3ec8f9096b138491090d6e88af2c4`
in continue mode, with four reusable activities and no pending cleanup.
Recovery completed all 13 activities and `validation.json` reported
`passed: true`. OceanBench v3 is public with 13 embedded build contexts.
Its public URI imported into the isolated daemon, where preflight required
reconstruction for all 13 activities and run `oceanbench-hub-v3-clean-uri`
was submitted.

The current URI test uses the existing isolated Docker daemon with its
`vfs` store. A disposable Docker 29 daemon on this host successfully
initialized an `overlay2` store, which can share image layers across
containers in future clean installations. The probe used its own storage
and completed without changing the active validation daemon.
The hourly worker later restarted the shared validation daemon while
URI tests were active. The worker prompt now directs it to check active
executions, keep shared tests running, and use a separate validation
instance when the shared one is busy. Nine execution jobs in that isolated
daemon reached terminal failure after their queue leases expired, despite
the execution API retaining the running state. The replacement Lorenz test
`lorenz-hub-v2-clean-overlay` was imported from the published URI and
submitted on the separate overlay-backed daemon. It completed 8/8
activities and passed validation. After confirming the original OceanBench
job had reached terminal failure and no containers referenced its image,
the scratch Docker image was removed from the old validation daemon. Free
storage increased by about 27 GB during cleanup. The new run
`oceanbench-hub-v3-clean-overlay` imported the v3 public URI into the
overlay-backed daemon and preflight required reconstruction for all 13
activities. Turing–Schnakenberg and Hodgkin–Huxley were imported again
from their public v2 URIs and submitted as `turing-hub-v2-clean-overlay`
and `hodgkin-hub-v2-clean-overlay`. Preflight reported build requirements
for all nine and 15 activities on the separate daemon. WeatherBench 2 and SIR
also imported from their public v2 URIs into the overlay-backed instance.
Preflight passed with 10 and 12 required image builds, respectively. The
runs `weatherbench-hub-v2-clean-overlay` and
`sir-hub-v2-clean-overlay` were submitted and accepted by that daemon. Wright–Fisher, StarDist, and MFC Sod
also imported into the overlay-backed daemon and passed execution preflight.
Their 28, 12, and 12 activities require reconstruction from the public
recipe. The daemon accepted runs `wright-fisher-hub-v2-clean-overlay`,
`stardist-hub-v2-clean-overlay`, and `mfc-hub-v2-clean-overlay`.

Portable image preparation is serialized by the daemon. Its
[reproduction code](https://github.com/UFFeScience/akoflow/blob/3f2067b6e3e180cd0bd27d8c122f4abf2588d8d0/internal/application/build/portable.go#L236-L285)
locks before the image cache lookup and holds that lock throughout the build.
As a result, the long OceanBench build can delay preparation for other
activities on the same instance, even if their images are already cached.
The queue worker now schedules long builds accordingly.

The daemon timestamps show overlapping scientific branches in the portable
reference runs for OceanBench (35.952 s), Turing–Schnakenberg (7.222 s),
Hodgkin–Huxley (1.350 s), Wright–Fisher (0.888 s), and SIR (0.247 s).
The two-slot Lorenz v2 capture passed scientific validation with no measured
branch overlap. The Lorenz README documents overlap separately for its
original v1 run. None of these portability checks measures speedup.

The anonymous gallery audit checked all 21 portable public publications.
Seventeen already served a figure and an animation. Foucault, Cooley–Tukey,
Airy diffraction, and Hénon had repository-relative media paths in their Hub
READMEs. The paths now use 17 publicly verified image URLs pinned to examples
commit `ac00512ccd40322d79d536565b4ede01c659a1c6`. Their public pages render
figures and expose animations without signing in. The other ten public
publications also served at least one figure and one animation via the
URLs listed in their Hub READMEs. This verifies media access for all 31
publications in the original cohort.

| Workflow | Completed activities | Public revision |
| --- | ---: | --- |
| Shannon BSC | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/shannon-bsc-capacity-audit) |
| Buffon needle | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/buffon-needle-pi-audit) |
| The Well radiative layer | 13/13 | [v2](https://hub.akoflow.com/o/akoflow/the-well-radiative-mixing-layer) |
| OceanBench GLONet | 13/13 | [v3](https://hub.akoflow.com/o/akoflow/oceanbench-glonet-metric-reproduction) |
| CHSH singlet correlation | 9/9 | [v2](https://hub.akoflow.com/o/akoflow/chsh-singlet-correlation-audit) |
| PDEBench advection | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/pdebench-advection-checkpoint-audit) |
| Ising–Yang magnetization | 12/12 | [v2](https://hub.akoflow.com/o/akoflow/yang-ising-magnetization-curve) |
| RR Lyrae period recovery | 10/10 | [v2](https://hub.akoflow.com/o/akoflow/sparse-multiband-rrlyrae-period-recovery) |
| Bateman decay chain | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/bateman-decay-chain-equilibrium-audit) |
| Robertson stiff solver | 7/7 | [v2](https://hub.akoflow.com/o/akoflow/robertson-stiff-solver-agreement) |
| StarDist equivariance | 12/12 | [v2](https://hub.akoflow.com/o/akoflow/stardist-equivariance-sweep) |
| Lorenz bounded sensitivity | 8/8 | [v2](https://hub.akoflow.com/o/akoflow/lorenz-bounded-sensitivity-ensemble) |
| Turing–Schnakenberg | 9/9 | [v2](https://hub.akoflow.com/o/akoflow/turing-schnakenberg-pattern-selection) |
| Hodgkin–Huxley | 15/15 | [v2](https://hub.akoflow.com/o/akoflow/hodgkin-huxley-excitation-boundary) |
| SIR threshold and final size | 12/12 | [v2](https://hub.akoflow.com/o/akoflow/sir-threshold-final-size-sweep) |
| Wright–Fisher fixation | 28/28 | [v2](https://hub.akoflow.com/o/akoflow/kimura-wright-fisher-fixation) |
| MFC Sod refinement | 12/12 | [v2](https://hub.akoflow.com/o/akoflow/mfc-sod-shock-tube-refinement) |
| WeatherBench 2 | 10/10 | [v2](https://hub.akoflow.com/o/akoflow/weatherbench2-era5-score-audit) |
| Caco-2 scaffold split | 19/19 | [v2](https://hub.akoflow.com/o/akoflow/caco2-scaffold-split-baselines) |

Volterra's portable revision reported “Build required” on all seven activities
and completed 7/7 in daemon run `community-volterra-predator-prey-run-v2`.
The corrected revision is public as Volterra version 2. Import via
`akoflow://hub/publications/36509a08-f4f3-43d3-9a20-ffe47116fb16/versions/2`
returned seven build sources and seven archived contexts on the existing
daemon. The URI also imported into an isolated AkôFlow database with an empty
Docker image store and a fresh BuildKit instance. All seven activities
reported that the image needed to be built. AkôFlow rebuilt the image and
completed 7/7 activities in `volterra-hub-v2-clean-uri` against the imported
definition. The final `validation.json` reported `passed: true`. The version-scoped
retirement below subsequently removed v1 from public access.

Keep one public, verified portable version per workflow. Verify the replacement
through anonymous Hub import and execution before retiring the legacy version.
The daemon's publication deletion endpoint removes the entire publication, so
it must never be used to retire v1 from a publication that also holds the
verified replacement. Anonymous checks confirmed that both Volterra and BioCLIP
served v1 and v2 YAML before the retirement. [Hub version retirement](https://github.com/UFFeScience/akoflow-hub/issues/102) records the rollout and verification.

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

## Public version retirement

The anonymous project inventory contained 40 publications. The
[retirement candidates](PORTABILITY-RETIREMENT-CANDIDATES.json) record the 31
older versions of 30 publications, their current replacement YAML hashes, and
the corresponding clean daemon runs. All 30 clean run statuses were
`completed` and every downloaded replacement matched the version hash from
the Hub. This inventory is a snapshot. Re-read the active versions and confirm
the verified replacement before applying any retirement.

BioCLIP v2 uses
`akoflow://hub/publications/8e98e0af-1904-46bf-8365-b438d4334852/versions/2`.
The Hénon map publication has ID `68796b3b-104b-4a2a-876c-9770bfe81492`.

Run [the retirement driver](automation/retire_portable_versions.py) to recheck
the inventory against the current Hub. The default only reads public versions.
Once the version-scoped daemon route and Hub handler are deployed, use
`--apply` through the Project's authorized daemon connection. An optional
`--slug` limits the operation to one publication. The driver verifies the
replacement before each use and checks that the old YAML is unavailable after
retirement.

## Current public definitions

An anonymous inspection of the [40 latest public definitions](PORTABILITY-PUBLIC-AUDIT.json)
verified 709 activities. Each activity resolves to an embedded build recipe.
Both the recipe and archived context match their declared SHA-256 digests.
Local Dockerfile inputs are present inside the archive, archive paths are safe,
and the base images are pinned. Each downloaded YAML matches its published
version hash. The inspection checks the package itself. The daemon execution
evidence is recorded in the clean-run sections above.


On 2026-11-28 the version-scoped Hub API
[retired 31 older versions](PORTABILITY-RETIREMENT-RESULTS.json) across
30 publications. After each retirement the old YAML returned 404 or 410 and
the replacement retained its verified SHA-256. A final anonymous project
inventory returned **40 public workflows with one public version each**.

The [public media audit](PORTABILITY-PUBLIC-MEDIA.json) retrieved the README
images anonymously for all 40 workflows and verified at least one valid
static figure and one animation containing multiple frames per publication.

Rainfall infiltration v1 was imported anonymously using
`akoflow://hub/publications/a8d814ff-23eb-4a60-9b72-1646baadfb36/versions/1`.
Its isolated execution started with an empty Docker image store, reconstructed
the portable recipe, and finished 514/514 activities. Validation covered 512
batches and 131,072 soil columns. The CSV, PNG and eight-frame GIF matched the
recorded reference exactly. [Clean-run evidence](https://github.com/UFFeScience/akoflow-examples/blob/877aad2ba162b8bd2ffd51bbb27687200e37ef7e/hydrology/rainfall-infiltration-ensemble/evidence/reference/clean-hub-run.json).

## Synthetic IDW audit v1

The [public IDW workflow](https://hub.akoflow.com/o/akoflow/community-explorer-issue-395-synthetic-idw-audit?version=1)
is available at
`akoflow://hub/publications/7e05a7d2-c41e-45db-88d0-c5492099ba77/versions/1`.
Its [recorded reference execution](https://hub.akoflow.com/o/akoflow/community-explorer-issue-395-synthetic-idw-audit/results/1/executions/cc8e993b-918c-4a17-b337-51a5e20bace5/runs/community-synthetic-idw-run-4-v1/workflow)
is accessible anonymously and contains the 1,033-activity four-slot run.
The URI imported into an isolated daemon with empty workflow and image
stores. All 1,033 activities resolve to the same archived build recipe.
The YAML, Dockerfile and 785-byte context passed SHA-256 verification.
The daemon rebuilt its image and began producing matching prediction
blocks. Full clean-run completion and aggregate checksum verification
are pending. [Import and reconstruction evidence](https://github.com/UFFeScience/akoflow-examples/blob/5a3a304/geospatial/synthetic-idw-audit/evidence/reference/public-uri-import.json).
