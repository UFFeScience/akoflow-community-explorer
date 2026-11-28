Work continuously on the AkôFlow Community Explorer operational queue.

Repository: UFFeScience/akoflow-community-explorer
Workspace: /home/ovvesley/Workspace/akoflow-community-explorer
Implementation source conventions: /home/ovvesley/Workspace/akoflow-examples
AkôFlow daemon source/runtime: /home/ovvesley/Workspace/akoflow
Production project ID: 44e9e6b5-454b-43b9-bf73-240be5e31aab

The account can access Docker non-interactively with `sudo -n docker` and can
start the official daemon with `sudo -n docker compose up -d` from the AkôFlow
repository. Do not label an issue blocked merely because the unprivileged
Docker socket probe fails; verify this sudo path and the daemon preflight API.
Before using a validation daemon, check its active executions and who owns the
instance. Leave shared or unrelated active executions running. A slow build or
an API observation timeout alone is insufficient grounds to restart a daemon.
Use a separate clean instance for validation if the existing instance is busy,
with independent storage and a distinct endpoint. Prefer layer-sharing storage
when supported and check free disk space before starting a large image build.
The daemon serializes portable image preparation, including cache lookups.
Let a long recipe build finish before sending unrelated validation runs to that
same daemon, or use an independent instance if the host has capacity.
Read `.automation/active-campaigns.md` if present for host-local worktree,
daemon, and evidence locations. Verify its pointers against the live API,
process state, and repository before acting. Keep the handoff current when you
launch, relocate, or finish a campaign. Keep credentials out of the handoff.
Before submitting a benchmark, look for that issue's active runs and profiling
processes across the primary and validation daemons on this host. Resume the
existing campaign on its original endpoint. Use another daemon for a clean
import check after the timed campaign, without duplicating its measurements.
When two timed campaigns would use the same physical CPUs, check all active
campaigns on that host before launching another. Separate AkôFlow containers
and databases alone do not imply separate CPUs. If concurrent measurements
already occurred, preserve the runs, record their overlap from live run
timestamps, and identify that load in the comparison.

Read AGENTS.md and inspect current GitHub issues and local/external state before
acting. Resume existing work and rank actionable candidates by independent
scientific branches, useful visual outputs, and downloadable result artifacts.
Include Brazilian papers, datasets, and institutions in candidate searches
and document the verified affiliation. If an issue is still research,
resolve its qualification gaps first. Do not write implementation code until code
and data licenses, exact result, inputs, acceptance tolerance, novelty, and a
scientifically parallel DAG are established.

During the legacy portability backfill, also read PORTABILITY-AUDIT.md each
pass and check the already submitted runs before starting new builds. The
BioCLIP v2 is already public with a compact recipe. Check for the latest
published revision and existing runs before retrying clean URI execution.
Record each confirmed backfill result in the audit.
Only retire an older version after its replacement passes the clean URI run,
and only through an operation scoped to that version.

Use `main` as the continuous integration branch in both the Community Explorer
and implementation repositories. Before editing, fetch `origin/main` and inspect
the local worktree and branch state. If the shared checkout is clean and can
fast-forward, work on its updated `main`. If it contains unrelated edits or local
commits, preserve them and use a separate worktree based on `origin/main`.
Push validated commits from that worktree to `main` without forcing. If the
remote advances, integrate the new remote commits in the separate worktree.
Commit validated Community Explorer changes directly to `main` and push them before finishing the
run. Do not leave queue state or automation changes on a topic branch. For an
implementation, work from the current implementation `main`, validate it, and
integrate it back into `main` during the same run; do not accumulate completed
implementation branches or open pull requests.

For a qualified issue, implement the smallest faithful CPU/Docker workflow, pin
versions/seeds/inputs, build in an isolated environment, preflight, execute the
reference scenario through the AkôFlow daemon with at least two slots, validate
files and science, and prove activity overlap from measured timestamps. Generate
an English README, at least one result-bearing scientific figure, a measured DAG
and/or timeline image, and a result-bearing animation. Treat animation as a
publication requirement whenever time, iteration, parameter sweep, convergence,
state transition, or another meaningful evolving dimension exists. If no honest
evolving view exists, document the concrete scientific reason in the issue and
README instead of manufacturing decorative motion. Record image digest, run ID,
workflow version, environment, measured timings, checksums, and limitations.
Every generated scientific figure, animation, and measured timeline/DAG used by
the publication must be committed to the implementation repository and embedded
directly in the README with an explanatory caption. Before publishing, verify the
exact committed raw URLs anonymously (HTTP 200, correct media signature, and more
than one frame for GIFs). Do not rely on untracked/ignored output files, mention a
gallery without rendering it in the README, or add a decorative placeholder.

Publish idempotently only to the confirmed Community Explorer project. Keep Hub
credentials outside scientific build/execution. Verify the public page anonymously,
including authors/citation, importable YAML, completed recorded run, gallery,
animation, downloads, and result consistency. Comment durable evidence on the
issue, apply lifecycle labels, and close only after every public check passes.
After verification, remove the completed candidate's temporary worktree if
clean, scratch datasets that can be fetched again, and candidate-specific
unused local images and build caches. Preserve source, committed galleries,
published artifacts, validation evidence, and resources referenced by active
runs or services. Check free disk space after cleanup and proceed to the next
actionable item if capacity permits.
An unavailable, disconnected, or approval-pending Hub blocks only publication.
Record the exact publication blocker once, then continue qualification,
implementation, daemon execution, or new-candidate research that does not require
Hub access. Do not end a run merely to wait for interactive Hub authorization.

If no issue is actionable, research one new paper candidate in the rotating
scientific domains described by the repository template. Before selecting or
opening it, perform a mandatory novelty gate against **all** GitHub issues (open
and closed), the implementation tree, and the public Community Explorer catalog.
Compare the scientific question, source paper, equations/method, inputs, DAG, and
claimed result semantically rather than relying only on title or search terms.
Record the searches and the closest catalog items in the new issue. A different
seed, scale, parameter range, or presentation of an already implemented question
is not a new candidate; treat it as a possible version/profile of the existing
publication and continue searching for a real catalog gap. Do not open or
implement a candidate until this gate passes. Never invent completion or
performance claims. Finish with a concise summary of authoritative changes and
the next unresolved action.
