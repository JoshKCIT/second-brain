# ADR: RC-2026-05-27-014 - Platform Research Artifacts

## Status

Accepted

## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-001
- Notes: User approved ADR and implementation pass.

## Source Claim

- Claim ID: RC-2026-05-27-014
- Source transcript: `raw/platform-transcripts/Robot_girlfriends_recursive_AI_agents_full_AI_research_Happy_Horse_-_AI_NEWS.txt`
- Speaker: unknown
- Timestamp: 00:21:30-00:24:30
- Claim type: workflow_proposal

## Context

The transcript describes agent-native research artifacts that preserve claims, experiments, failed attempts, logs, and raw evidence. Second Brain's platform research lane already moves in this direction with claim records, reports, hypotheses, rejected ideas, and draft ADRs.

## Decision

Adopt platform research artifacts as structured claim-plus-evidence packages. Preserve failed ideas and evidence quality instead of only final recommendations.

## Rationale

This strengthens inspectability and keeps transcript-derived ideas from becoming canonical knowledge without review.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 2 | Makes product decisions evidence-backed. |
| Closure | 1 | Keeps next actions explicit. |
| Grounding | 2 | Preserves source excerpts and validation status. |
| Vendor truth | 0 | Neutral unless vendor claims appear. |
| Inspectability | 2 | Shows decisions, rejected ideas, and uncertainty. |
| Maintainability | 0 | More files, but structured. |
| Differentiation | 1 | Reinforces governed platform evolution. |
| Enterprise fit | 1 | Audit-friendly. |
| Human review leverage | 2 | Lets user approve/reject focused decisions. |

## Alternatives Considered

1. Do nothing.
2. Summarize transcripts only.
3. Convert transcript claims directly into canonical docs.
4. Preserve structured research artifacts and draft ADRs.

## Consequences

### Positive

- Prevents noisy transcript claims from polluting canonical docs.
- Preserves negative knowledge.
- Gives future agents durable decision context.

### Negative / Risks

- Reports can sprawl if every transcript produces too many claims.

### Safeguards

- Keep claims atomic.
- Keep decision rationale and validation state required.
- Lint platform research artifacts.

## Validation Plan

Run `python scripts/lint-platform-research.py --root .` and user-review the final recommendation package. Success means the user can identify adopt, experiment, defer, and reject decisions without reading every transcript.

## Files Proposed for Future Change

```text
.github/prompts/platform-research-review.prompt.md
.cursor/agents/platform-research-reviewer.md
templates/platform-research/
scripts/lint-platform-research.py
```
