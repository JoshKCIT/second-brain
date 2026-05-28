# Retrieval contract checklist (RC-018)

Define **what context the agent needs** before choosing storage, index, or retrieval mechanics. Storage follows the contract; page-index navigation (RC-001) executes it.

Use this checklist at the start of `/workspace-compile` batches and when authoring multi-standard project artifacts. **Optional** for single-source Q&A. **Required** before moving project artifacts to `review` when they depend on two or more in-scope standards or source domains.

## Contract fields

| Field | Required | Notes |
|---|---|---|
| Artifact / task | yes | e.g. `compile batch`, `02-pm-prd/product-requirements.md` |
| Bundle purpose | yes | One sentence: what decision or output this context supports |
| In-scope sources | yes | Confluence spaces, vendor caches, wiki paths from `config/second-brain.yml` / `meta.yml` |
| Required wiki articles | if known | 3–10 paths from `wiki/index.md` catalog navigation |
| Required raw paths | if known | Immutable sources to read before synthesis |
| Authority per field | yes | `standard` / `recommendation` / `informational`; domain tag per claim type |
| Freshness rules | vendor only | TTL from `config/second-brain.yml`; flag stale before cite |
| Permissions / scope | yes | Project slug, `--project` scope, excluded archives |
| Out of scope | yes | Explicit exclusions to prevent full-vault reads |
| Storage/index choice | after contract | Default: page-index + section anchors; no new vector/graph without eval |
| Mandatory read (pointers) | yes | `AGENTS.md` + task-required paths; see `templates/workspace/pointer-resources/mandatory-default-load.md` |
| Optional read (pointers) | if task match | e.g. `verb-invocation-detail.md`, `operation-deep-dives.md` (RC-165) |

## Pointer bundle fields (RC-165)

```yaml
mandatory_read:
  - AGENTS.md
  - wiki/index.md
optional_read:
  - templates/workspace/pointer-resources/verb-invocation-detail.md
  - templates/workspace/pointer-resources/operation-deep-dives.md
```

Optional pointers do not substitute for `mandatory_read` or `align-cite`.

## Fail-closed gates

Block publish (or flag in compile log) when:

- A bundle field lacks authority or domain for a fact-bearing claim
- Vendor capability cited without a fresh `raw/workspace-external/` cache
- Retrieval scope exceeds `meta.yml` / config without explicit user waiver

Retrieval lists and contracts do **not** substitute for `align-cite` at publish.

## Example (project PM stage)

```yaml
artifact: wiki/workspace-projects/{slug}/02-pm-prd/product-requirements.md
purpose: Requirements grounded in Architecture and Security standards for {feature}
in_scope_spaces: [ARCH, SECURITY]
required_wiki:
  - wiki/workspace-standards/architecture/microservice-sizing.md
  - wiki/workspace-standards/security/encryption-at-rest.md
required_raw: []
authority: internal standard for architecture/security claims; vendor:aws if S3 cited
freshness: revalidate aws encryption doc if past TTL
out_of_scope: platform-transcripts, archived projects
storage: page-index via wiki/index.md; section-tree reads only
```

## See also

- ADR: `docs/platform-decision-records/RC-2026-05-27-018-retrieval-contract-first.md`
- Read-before-write: RC-122
- Page-index policy: RC-001, RC-002
