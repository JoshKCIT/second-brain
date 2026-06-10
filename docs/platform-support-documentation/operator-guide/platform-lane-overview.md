---
title: "Platform lane overview"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "templates/workspace/routing-map.md"
  - "wiki/platform-research/implementation-backlog.md"
  - ".github/prompts/platform-transcript-librarian.prompt.md"
---

# Platform lane overview

Short guide for **workspace operators** who encounter Second Brain product work. Daily documentation stays in **workspace** lane; **platform** lane improves Second Brain itself.

## When to escalate

Escalate (PH-006) when a session proposes:

- Changing `AGENTS.md`, PRD, roadmap, or architecture rationale from a transcript idea
- Promoting transcript claims into workspace standards or projects
- Implementing stack changes without an approved ADR

Do **not** escalate for normal workspace ingest, compile, projects, or query.

## Transcript flow

1. `/platform-transcript-librarian` — import transcript to `raw/platform-transcripts/` (human approval before raw write)
2. Sync register — `python scripts/sync-transcript-register.py --root .`
3. `/platform-research-review` — claim extraction, scoring, draft ADRs
4. CEO reviews impact report and draft ADR — approve or reject
5. Approved items queue in implementation backlog

Platform research writes `wiki/platform-research/**` and reports — not canonical workspace standards by default.

## PIC pointer

Approved platform changes deliver one at a time:

1. Load [implementation-backlog.md](../../../wiki/platform-research/implementation-backlog.md)
2. `/platform-implement-backlog` — smallest reversible change per ADR
3. Tests + lint pass → present diff
4. On accept: agent runs `promote-platform-adr.py`; backlog item marked accepted

Workspace operators rarely run PIC unless they maintain Second Brain itself.

## Boundaries

Platform lane outputs are **product intelligence**, not workspace standards:

| Artifact | Location | Canonical? |
|----------|----------|------------|
| Claim register | `wiki/platform-research/claim-register.md` | No — evidence for decisions |
| Draft ADR | `docs/platform-decision-records/DRAFT-*.md` | No until promoted |
| Accepted ADR | `docs/platform-decision-records/RC-*.md` | Yes after PIC accept |
| Workspace standard | `wiki/workspace-standards/**` | Yes — never from transcript alone |

When in doubt, ask: "Is this about my company's docs or about Second Brain the product?" Company docs → workspace. Product → platform.

## See Also

- [concepts-for-operators.md](concepts-for-operators.md)
- [ceo-approval-guide.md](ceo-approval-guide.md)
- [feature-catalog.md](feature-catalog.md) — Platform lane section

## Sources consulted

- AGENTS.md, routing-map.md, implementation-backlog.md, platform-transcript-librarian.prompt.md
