# Draft-tier map (PH-007)

CEO and agent cheat sheet: **where to write** during an active project. Everything in this map except the stage artifact is **draft-tier** — excluded from finalize, align-closure publish set, and publish.

Path pattern: `wiki/workspace-projects/{slug}/{stage-dir}/…`

## Quick reference

| Intent | Write to | Canonical? | Promoted how |
|---|---|---|---|
| Resume / locks / forwarded decisions | `{stage}/handoff.md` | No | PH-003 forward at CEO gate |
| Session preferences / scratch notes | `{stage}/orientation.md` | No | Never without compile + approval + align-cite |
| Interview / exploration (thinking-partner) | `{stage}/thinking-notes/` | No | Verify in stage artifact + sources |
| Reading notes with sources | `{stage}/research/` | No | Merge into stage artifact at gate |
| Chat / transcript fragments | `{stage}/chats/` | No | Merge or discard; never publish as-is |
| Daily catch-up log | `{stage}/daily-progress/` | No | Inform handoff; never publish |
| Parallel workstream (CEO-approved) | `{stage}/subprojects/{workstream}/` | No | Tier-3 scaffold; `publish_scope: exclude` |
| Retrieval scope for multi-standard work | `{stage}/retrieval-contract.md` | No | Consulted at draft; excluded from publish |
| **Publish-bound deliverable** | `{stage}/{artifact}.md` | Yes (when published) | Finalize → align-cite + align-closure |

## Distinctions

**`handoff.md` (RC-058, PH-003)** — structured restart state: `starting_context`, `next_steps`, open decisions, **Locked decisions**, **Forwarded open decisions**. Read on resume; update at session end after CEO confirms.

**`orientation.md` (RC-163)** — disposable session context: preferences, “remember this”, active scratch. `not_canonical: true`. Distinct from handoff; never wiki-promoted without compile.

**`thinking-notes/` (RC-117)** — thinking-partner output only. Pairs with `agent_mode: thinking` (RC-116). Never publish-shaped.

**Stage artifact** — the deliverable for that stage (`product-brief.md`, `product-requirements.md`, etc.). Only files promoted to `review` / `published` by finalize.

## Exclusion reminder

Finalize and publish **exclude**: `handoff.md`, `orientation.md`, `retrieval-contract.md`, `README.md`, `STAGE-SCAFFOLD.md`, and all files under `research/`, `chats/`, `daily-progress/`, `thinking-notes/`, `subprojects/`.

## Agent mode (RC-116)

| `agent_mode` | Artifact body | Notes go to |
|---|---|---|
| `artifact` (default) | Publish-shaped draft allowed | `research/` or artifact |
| `thinking` | No publish-shaped output | `orientation.md` or `research/` |

Finalize blocks `review` while any artifact remains in `thinking` mode.

## CEO checkpoint (project create)

When starting a project, confirm you know where to write:

1. Locks and forwards → `handoff.md`
2. Session scratch → `orientation.md`
3. Exploration → `thinking-notes/` or thinking-partner prompt
4. Deliverable → stage artifact only

## See also

- Experiment details: `templates/workspace/experiment-registry.md`
- Stage scaffold layout: `templates/workspace/project-stage-scaffold/README.md`
- ADR: `docs/platform-decision-records/PH-2026-05-27-007-stack-consolidation.md`
