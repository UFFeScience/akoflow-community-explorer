# Community Explorer worker rules

- GitHub issues are the authoritative queue. Work on the oldest open actionable
  issue before researching or creating another candidate.
- Never implement a candidate still blocked on license, data, method, or a missing
  acceptance criterion. Resolve the evidence or label and comment the blocker.
- Keep scientific build and execution isolated from Hub credentials and the host
  Docker socket. Network access is allowed only in a separately declared input or
  image preparation step.
- Run the selected reference scenario through the AkôFlow daemon. A local helper
  run is a preflight, not execution evidence.
- Do not claim parallel speedup without a matching one-slot run. Always prove
  overlap among independent scientific activities from measured timestamps.
- Publish only validated results to Community Explorer project
  `44e9e6b5-454b-43b9-bf73-240be5e31aab`. Confirm this ID immediately before any
  write, and restrict writes to publications created for this queue.
- Publication retries must be idempotent. Search by the issue's persistent
  publication key before creating a publication or version.
- Close an issue only after anonymous verification of the public page, import YAML,
  recorded completed run, gallery/animation, result links, authorship, citation,
  licenses, and agreement between displayed results and the reference run.
- Preserve unrelated work and credentials. Never print secrets or place them in
  source, logs, images, results, or issue comments.
