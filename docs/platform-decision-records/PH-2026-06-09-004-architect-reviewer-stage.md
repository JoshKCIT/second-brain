# ADR: PH-2026-06-09-004 - Architect Reviewer Stage

## Status

Accepted (PIC-2026-06-09-029, 2026-06-09)

## Context

Advisory conformance review before finalize reduces misalignment with in-scope standards. Complements PH-004 advisory align-cite per stage.

## Decision

Add `.github/prompts/workspace-architect-reviewer-agent.prompt.md` — **report-only** conformance pass against scoped `wiki/workspace-standards/**`. Writes to `reports/` or stage `research/` only; does not mutate publish-bound artifacts without CEO approval.

Optional chain stage `architect-review` after architecture or before finalize.

## Intent

- **In scope:** Advisory report shape; routing-map row.
- **Out of scope:** Blocking publish without CEO override path; replacing `workspace-align-conformance`.

## Safety and non-goals

- **Safety posture:** Report-only by default; no publish-bound edits without CEO approval.
- **Non-goals:** Blocking publish; replacing align-conformance verb.

## Implementation Notes

- Prompt: `.github/prompts/workspace-architect-reviewer-agent.prompt.md`
- Templates: `templates/workspace/architect-reviewer-stage.md`, `templates/workspace/architect-reviewer-report.md`
- Optional `current_stage: architect-review` in `meta.yml`.

## Approval

- Approved: 2026-06-09
- Cycle: PIC-2026-06-09-029
- Notes: workspace-architect-reviewer-agent prompt; optional architect-review stage; not in default profile v1.
