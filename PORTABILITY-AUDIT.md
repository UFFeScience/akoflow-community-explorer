# Community Explorer portability audit

Scope: publications with receipts for production project
`44e9e6b5-454b-43b9-bf73-240be5e31aab`.

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

Current production-project total: 9 publications, 9 passed, 0 pending. Receipts
for other projects or receipts without a project identifier are excluded from
this production audit.
