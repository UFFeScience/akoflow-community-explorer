# Community Explorer worker rules

- GitHub issues are the authoritative queue. Resume work in progress, then
  prioritize candidates with independent scientific branches and meaningful
  visual and downloadable outputs. Favor qualified work from Brazilian research
  groups among similarly suitable candidates.
- Never implement a candidate still blocked on license, data, method, or a missing
  acceptance criterion. Resolve the evidence or label and comment the blocker.
- Keep scientific build and execution isolated from Hub credentials and the host
  Docker socket. Network access is allowed only in a separately declared input or
  image preparation step.
- Run the selected reference scenario through the AkôFlow daemon. A local helper
  run is a preflight, not execution evidence.
- Treat clean-machine importability as a publication gate for every workflow.
  Published activities must resolve their executable from an AkôFlow portable
  build recipe (`source.type: build`), not from a host-only image tag or digest.
- Keep every Dockerfile `COPY` or `ADD` source inside the registered, versioned
  build context. Reject absolute paths, parent traversal (`../`), host mounts,
  generated files absent from the context, and undeclared network downloads.
  Pin the base image by digest and record both recipe and context digests.
- Test portability from an unmaterialized state: import the public YAML, confirm
  preflight requests the missing build, let AkôFlow reconstruct the image, and
  rerun the full reference scenario through the daemon. Anonymous verification
  must confirm that the public YAML embeds the build origin, context archive,
  and digests needed to repeat that reconstruction on another machine.
- Apply the same portability audit and daemon rerun to legacy publications.
  A previously successful local run does not waive this gate.
- Do not claim parallel speedup without a matching one-slot run. Always prove
  overlap among independent scientific activities from measured timestamps.
- Publish only validated results to Community Explorer project
  `44e9e6b5-454b-43b9-bf73-240be5e31aab`. Confirm this ID immediately before any
  write, and restrict writes to publications created for this queue.
- Publication retries must be idempotent. Search by the issue's persistent
  publication key before creating a publication or version.
- A disconnected or approval-pending Hub blocks publication only. Record that
  blocker once and continue all safe queue work that does not require Hub access;
  never end a worker pass solely to wait for interactive authorization.
- Close an issue only after anonymous verification of the public page, import YAML,
  recorded completed run, embedded result figure, result-bearing animation,
  measured DAG and/or timeline, result links, authorship, citation,
  licenses, and agreement between displayed results and the reference run.
- Preserve unrelated work and credentials. Never print secrets or place them in
  source, logs, images, results, or issue comments.
