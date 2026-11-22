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

Read AGENTS.md and inspect current GitHub issues and local/external state before
acting. Resume the oldest open actionable issue. If an issue is still research,
resolve its qualification gaps first. Do not write implementation code until code
and data licenses, exact result, inputs, acceptance tolerance, novelty, and a
scientifically parallel DAG are established.

Use `main` as the continuous integration branch in both the Community Explorer
and implementation repositories. Before editing, verify the worktree is clean,
switch to `main`, and fast-forward it from `origin/main`. Commit validated
Community Explorer changes directly to `main` and push them before finishing the
run. Do not leave queue state or automation changes on a topic branch. For an
implementation, work from the current implementation `main`, validate it, and
integrate it back into `main` during the same run; do not accumulate completed
implementation branches or open pull requests.

For a qualified issue, implement the smallest faithful CPU/Docker workflow, pin
versions/seeds/inputs, build in an isolated environment, preflight, execute the
reference scenario through the AkôFlow daemon with at least two slots, validate
files and science, and prove activity overlap from measured timestamps. Generate
an English README, scientific figure, measured DAG/timeline image, and an animation
when the result has a useful evolving dimension. Record image digest, run ID,
workflow version, environment, measured timings, checksums, and limitations.

Publish idempotently only to the confirmed Community Explorer project. Keep Hub
credentials outside scientific build/execution. Verify the public page anonymously,
including authors/citation, importable YAML, completed recorded run, gallery,
animation, downloads, and result consistency. Comment durable evidence on the
issue, apply lifecycle labels, and close only after every public check passes.
An unavailable, disconnected, or approval-pending Hub blocks only publication.
Record the exact publication blocker once, then continue qualification,
implementation, daemon execution, or new-candidate research that does not require
Hub access. Do not end a run merely to wait for interactive Hub authorization.

If no issue is actionable, research one new non-duplicate paper candidate in the
rotating scientific domains described by the repository template and open a fully
evidenced issue. Never invent completion or performance claims. Finish with a
concise summary of authoritative changes and the next unresolved action.
