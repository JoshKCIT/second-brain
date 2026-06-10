# DRAFT ADR: PH-2026-06-09-004 - Architect Reviewer Stage

## Status

Draft

## Context

Advisory conformance review before finalize reduces misalignment with in-scope standards. Complements PH-004 advisory align-cite per stage.

## Decision

Add `.github/prompts/workspace-architect-reviewer-agent.prompt.md` — **report-only** conformance pass against scoped `wiki/workspace-standards/**`. Writes to `reports/` or stage `research/` only; does not mutate publish-bound artifacts without CEO approval.

Optional chain stage `architect-review` after architecture or before finalize.

## Intent

- **In scope:** Advisory report shape; routing-map row.
- **Out of scope:** Blocking publish without CEO override path; replacing `workspace-align-conformance`.

## Approval

- Pending PIC; depends on PH-2026-06-09-001, PH-004 ✓
