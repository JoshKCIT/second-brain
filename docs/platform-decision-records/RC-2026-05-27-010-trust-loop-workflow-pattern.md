# ADR: RC-2026-05-27-010 - Trust Loop Workflow Pattern

## Status

Accepted

## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-002
- Notes: User approved via continue; implementation pass applied.

## Source Claim

- Claim ID: RC-2026-05-27-010
- Source transcript: `raw/platform-transcripts/Why_2026_Is_the_Year_to_Build_a_Second_Brain_And_Why_You_NEED_One.txt`
- Speaker: unknown
- Timestamp: 00:09:00-00:21:30
- Claim type: workflow_proposal

## Context

The transcript describes reliable AI workflows as small loops with capture, schema, audit trail, confidence guardrails, proactive surfacing, and correction. Second Brain already has many of these parts, but the pattern should be explicit for future workflows.

## Decision

Adopt a trust-loop pattern for future platform and workspace workflow designs: audit every decision, record confidence or validation state, fail closed on uncertainty, and provide a clear correction route.

## Rationale

Trust mechanisms protect governance and human review leverage. They are more important than raw automation capability.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 2 | Makes workflow state auditable. |
| Closure | 1 | Reduces hidden assumptions. |
| Grounding | 1 | Encourages validation state. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 2 | Decisions and corrections are visible. |
| Maintainability | 1 | Uses consistent patterns. |
| Differentiation | 1 | Reinforces governed workflow niche. |
| Enterprise fit | 1 | Better auditability. |
| Human review leverage | 2 | Humans review meaningful exceptions. |

## Alternatives Considered

1. Do nothing.
2. Add more automation without trust mechanisms.
3. Require manual review for every step.
4. Adopt trust loops with fail-closed exceptions.

## Consequences

### Positive

- Improves reliability and user trust.
- Makes platform research outputs easier to correct.
- Creates a reusable pattern for future prompts and scripts.

### Negative / Risks

- Adds small metadata burden to workflows.

### Safeguards

- Keep outputs concise.
- Use trust state only where it affects downstream decisions.

## Validation Plan

Apply the pattern to platform research review artifacts first. Review whether claim records, reports, and ADRs expose enough evidence and correction paths for the user to approve or reject recommendations quickly.

## Files Proposed for Future Change

```text
.github/prompts/platform-research-review.prompt.md
templates/platform-research/
scripts/lint-platform-research.py
```
