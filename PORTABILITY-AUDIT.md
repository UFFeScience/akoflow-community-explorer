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
| Brachistochrone audit | legacy OCI; local `COPY` sources are bounded | pending migration |
| Foucault precession | legacy OCI; local `COPY` sources are bounded | pending migration |
| Hénon map audit | legacy OCI; local `COPY` sources are bounded | pending migration |
| Airy diffraction | legacy OCI; local `COPY` sources are bounded | pending migration |
| Rabi oscillations | legacy OCI; `COPY` sources are bounded; base image is not digest-pinned | pending migration and base pin |
| Cooley–Tukey FFT | legacy OCI; local `COPY` sources are bounded | pending migration |
| Debye heat capacity | legacy OCI; local `COPY` sources are bounded | pending migration |

Current production-project total: 9 publications, 2 passed, 7 pending. Receipts
for other projects or receipts without a project identifier are excluded from
this production audit.
