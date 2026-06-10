# Task-type routing map (RC-162)

Orientation-only table for Tier-2 shims. **Does not auto-load content** or bypass read-before-write (RC-122), retrieval contracts (RC-018), or align-cite.

Canonical copy lives in `AGENTS.md` § Routing map. Update this template when prompts or paths change.

## How to use

1. Classify the user task → **lane** (`workspace` or `platform`).
2. Find the matching row → invoke **prompt/skill** and read **first paths**.
3. Mutations require explicit user approval unless the operation is read-only query.

## Routing table

| Task type | Lane | Invoke | Read first | Write scope (approval-gated) |
|---|---|---|---|---|
| Onboard / configure scope | workspace | `second-brain` | `config/second-brain.yml`, `wiki/index.md` | `config/second-brain.yml` |
| Start or resume project | workspace | `workspace-start-project` | `wiki/index.md`, `wiki/workspace-projects/{slug}/meta.yml`, **`templates/workspace/chain-profiles/`**, stage `handoff.md`, **`templates/workspace/draft-tier-map.md`** | `wiki/workspace-projects/{slug}/**` |
| VP / PM / Architect / Engineer stage | workspace | `workspace-{vp,pm,architect,engineer}-agent` | `meta.yml`, stage artifact, `handoff.md`, `orientation.md` | Active stage artifact + draft-tier scaffolds |
| Technical Writer stage (optional) | workspace | `workspace-technical-writer-agent` | Upstream approved artifacts, `docs/style/exemplar-published-doc.md`, `05-technical-writing/handoff.md` | In-place prose polish on stage artifacts; `05-technical-writing/**` scaffolds |
| Architect Reviewer stage (optional) | workspace | `workspace-architect-reviewer-agent` | `meta.yml`, retrieval contract, in-scope `wiki/workspace-standards/**`, project artifacts | `reports/workspace-architect-reviewer-*.md` only; optional `03-architecture/research/` notes |
| Thinking-partner exploration | workspace | `workspace-thinking-partner` | Stage `handoff.md`, upstream artifacts, `orientation.md` | `thinking-notes/**` only |
| Session end preference capture | workspace | `session-audit` skill / `workspace-session-audit` | Stage `handoff.md`, `orientation.md` | `handoff.md`, `orientation.md` only |
| Ingest Confluence | workspace | `workspace-ingest-confluence` | `config/second-brain.yml`, scoped spaces | `raw/workspace-confluence/**`; compile after RC-146 approval |
| Ingest vendor doc | workspace | `workspace-ingest-vendor-doc` | `raw/workspace-external/{vendor}/` TTL | `raw/workspace-external/**`, `raw/workspace-inbox/**` |
| Compile raw → wiki | workspace | `workspace-compile` | `wiki/index.md`, target `raw/**`, retrieval contract if multi-standard | `wiki/**`, `wiki/log.md` — **explicit batch approval required (RC-146)** |
| Query / Q&A | workspace | `workspace-query` | `wiki/index.md` then scoped articles | Optional `wiki/workspace-qa/**` with `--file-back` |
| Align cite / closure / vendor truth | workspace | `workspace-align-*` | Target artifact + cited sources | Reports under `reports/` only |
| Publish / archive | workspace | `workspace-publish`, `workspace-archive` | Active project artifact set | `wiki/workspace-projects/**`, `confluence-review/**` |
| Workspace health | workspace | `workspace-lint` | `wiki/index.md`, `scripts/lint-workspace.py` | `reports/workspace-lint-*.md` |
| Pointer resource depth | workspace | read on task match | `templates/workspace/pointer-resources/README.md` | Optional reads only (RC-165) |
| Stack orientation (experiments + draft-tier) | workspace | read on task match | `templates/workspace/experiment-registry.md`, `templates/workspace/draft-tier-map.md` | Reference only (PH-007) |
| **Platform escalation (PH-006)** | **platform** | **`platform-transcript-librarian`** or **`platform-research-review`** | **`wiki/platform-research/transcript-register.md`, claim register** | **`wiki/platform-research/**`, `reports/platform-research-review/**`, `docs/platform-decision-records/DRAFT-*` only — **never** workspace standards/projects/PRD/`AGENTS.md` without approval |
| Import transcript | platform | `platform-transcript-librarian` | `wiki/platform-research/transcript-register.md` | `raw/platform-transcripts/**` after H1 approval |
| Research review / claims | platform | `platform-research-review` | Transcript, `wiki/platform-research/claim-register.md` | Platform research artifacts only |
| Platform implementation (PIC) | platform | **`platform-implement-backlog`** | `wiki/platform-research/implementation-backlog.md`, draft ADR | Per approved ADR; **agent runs** `promote-platform-adr.py` on accept (PH-008) |

## Platform escalation (PH-006)

When a **workspace** session surfaces Second Brain product ideas, transcripts, or architecture proposals:

1. **Stop** workspace-lane canonical edits to protected files.
2. Switch to **platform** lane per row above.
3. Route through research review; user approves ADR before stack-lift implementation.

Protected without explicit approval: `wiki/workspace-standards/**`, `wiki/workspace-recommendations/**`, `wiki/workspace-projects/**` (for platform claims), `PRD.md`, `product-brief.md`, `docs/roadmap.md`, `docs/architecture-rationale.md`, `AGENTS.md`.

## Cross-links

- RC-018 retrieval contract: `templates/workspace/retrieval-contract-checklist.md`
- PH-007 experiment registry: `templates/workspace/experiment-registry.md`
- PH-007 draft-tier map: `templates/workspace/draft-tier-map.md`
- RC-135 agent hub (future compile index): `docs/platform-decision-records/DRAFT-RC-2026-05-27-135-agent-hub-compile-artifacts.md`
- Lane vocabulary: `AGENTS.md` § Lane vocabulary

## Maintenance

When adding or renaming a prompt under `.github/prompts/`, update this table and `AGENTS.md` § Routing map in the same change set.

## See also

- ADR: `docs/platform-decision-records/RC-2026-05-27-162-routing-map-agents-shim.md`
- Instruction stack: `templates/workspace/instruction-stack-header.md`
