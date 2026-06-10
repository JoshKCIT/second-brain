# ADR: PH-2026-06-09-003 - Technical Writer Stage

## Status

Accepted (PIC-2026-06-09-028, 2026-06-09)

## Approval

- Approved: 2026-06-09
- Cycle: PIC-2026-06-09-028
- Notes: workspace-technical-writer-agent prompt; optional technical-writing stage; not in default profile v1.

## Context

Profiles need a publish-shaped prose stage between engineering specs and finalize. Overlaps with finalize; this stage owns exemplar style, body-prose-clean prep, and See Also population per `docs/style/exemplar-published-doc.md`.

## Decision

Add `.github/prompts/workspace-technical-writer-agent.prompt.md` and optional chain stage `technical-writing` in profiles that include it (not required in default profile v1).

**Input contract:** Approved upstream stage artifacts + in-scope standards (retrieval contract).  
**Output contract:** Draft-tier edits to stage artifact or dedicated `technical-spec.md` per profile; `authored_by_agent: technical-writer`.

## Intent

- **In scope:** Prompt, routing-map row, profile optional stage slot.
- **Out of scope:** Autonomous publish; bypassing CEO gate.

## Safety and non-goals

- **Safety posture:** Does not set `review` status or run finalize; citations preserved.
- **Non-goals:** Autonomous publish; replacing Engineer finalize.

## Implementation Notes

- Prompt: `.github/prompts/workspace-technical-writer-agent.prompt.md`
- Template: `templates/workspace/technical-writer-stage.md`
- Routing: `templates/workspace/routing-map.md`
- Optional `current_stage: technical-writing` in `meta.yml` for profiles that include this stage.

## Approval

- Pending PIC-2026-06-09-028; depends on PH-2026-06-09-001 ✓
