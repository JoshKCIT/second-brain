# DRAFT ADR: RC-2026-05-27-012 - Advisory Harness Failure Review

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-012
- Source transcript: `raw/platform-transcripts/Researcher_at_Stanford_released_a_new_paper_for_an_automated_ai_agent_harmess_ai_tech_fyp.txt`
- Speaker: unknown
- Timestamp: 00:00:00-00:01:30
- Claim type: evaluation_proposal

## Context

The transcript argues that the agent harness matters as much as the model and that failure traces can guide improvements. Second Brain should learn from failures, but must not auto-mutate prompts, rules, or protected files.

## Decision

Run advisory harness-failure reviews as an experiment after enough real failures exist. The review may produce reports and draft ADRs only.

## Rationale

This preserves evidence-driven improvement while keeping platform governance and approval gates intact.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 1 | Routes failures through review. |
| Closure | 1 | Can improve jr-executable outputs. |
| Grounding | 1 | Uses real failure traces. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 2 | Makes harness issues visible. |
| Maintainability | 1 | Avoids ad hoc prompt edits. |
| Differentiation | 1 | Improves governance quality. |
| Enterprise fit | 1 | Audit-friendly. |
| Human review leverage | 2 | Gives the user concrete improvements to approve. |

## Alternatives Considered

1. Do nothing.
2. Let agents rewrite prompts automatically.
3. Manually tune prompts without failure data.
4. Produce advisory failure-review reports.

## Consequences

### Positive

- Converts failures into structured improvement proposals.
- Avoids unreviewed prompt drift.

### Negative / Risks

- Requires enough failure data to be useful.
- Can become process overhead if run too often.

### Safeguards

- No protected-file writes.
- Require explicit user approval before prompt/rule changes.
- Include test evidence in every recommendation.

## Validation Plan

After multiple real lint/test/publish failures, run a failure-review report. Success means at least one proposed change is accepted and improves a subsequent run.

## Files Proposed for Future Change

```text
.github/prompts/
.cursor/rules/
AGENTS.md
```
