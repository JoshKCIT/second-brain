# Pointer resources (RC-165)

On-demand reference files for **Tier-2 IDE shims** and retrieval contracts. Keeps default session load lean while preserving fail-closed governance in every shim.

## Convention

| Tier | Default load | Pointer load |
|---|---|---|
| Tier 1 (`AGENTS.md`) | Canonical schema; full operation detail stays here | Shims link here for schema; do not duplicate article formats |
| Tier 2 (shims) | Architecture, routing, 15 compact critical rules, verb names | Expanded rule text, verb descriptions, examples |
| Tier 3 (project) | `meta.yml`, stage scaffolds | `templates/workspace/*` per task |

**Rule:** Governance invariants (approval gates, align-cite, closure, lane boundaries, fail closed) **never** move to optional-only pointers. Optional pointers add depth only.

## Pointer catalog

| File | Load when | Mandatory for |
|---|---|---|
| `mandatory-default-load.md` | Auditing shims; onboarding maintainers | Shim authors |
| `critical-rules-expanded.md` | Rule interpretation disputes; onboarding | Optional |
| `verb-invocation-detail.md` | First use of an unfamiliar verb; onboarding | Optional |
| `article-formats-reference.md` | Authoring new wiki article types | Compile, project agents |
| `operation-deep-dives.md` | Multi-step ingest/compile/publish runs | Ingest, compile, publish |
| `topic-entity-compile.md` | Structured topic/connection synthesis from raw | Compile batches (RC-148) |

## Shim targets

Keep each Tier-2 shim under **~100 lines** (soft limit; lint advisory). Current shims:

- `.cursor/rules/agents.mdc`
- `CLAUDE.md`
- `.github/copilot-instructions.md`

When adding platform features, update **one-line pointers** in shims and put extended prose in this directory.

## Retrieval contract integration (RC-018)

When drafting a retrieval contract, tag pointer reads:

```yaml
mandatory_read:
  - AGENTS.md
  - wiki/index.md
optional_read:
  - templates/workspace/pointer-resources/verb-invocation-detail.md
```

See `templates/workspace/retrieval-contract-checklist.md` § Pointer bundle fields.

## See also

- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-165-lean-root-pointer-resources.md`
- Instruction stack: `templates/workspace/instruction-stack-header.md` (RC-161)
- Routing: `templates/workspace/routing-map.md` (RC-162)
