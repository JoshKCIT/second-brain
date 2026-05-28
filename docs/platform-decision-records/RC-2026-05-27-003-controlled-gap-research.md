# ADR: RC-2026-05-27-003 - Controlled Platform Gap Research

## Status

Accepted (experiment)

## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-005
- Notes: User approved via continue; gap-review workflow applied.

## Source Claim

- Claim ID: RC-2026-05-27-003
- Source transcript: `raw/platform-transcripts/second-brain-self-learning-ideas.txt`
- Speaker: unknown
- Timestamp: 00:00:30-00:01:00
- Claim type: workflow_proposal

## Context

The transcript proposes a self-learning loop that finds gaps and researches external sources. The safe Second Brain variant is a controlled platform research loop that produces candidate sources and hypotheses, not direct canonical edits.

## Decision

Run this as an experiment. A gap-review loop may update platform research artifacts and draft ADRs, but it must not modify protected files or workspace knowledge.

## Intent

- **Intended outcome:** Repeatable platform discovery that surfaces candidate sources and hypotheses without automatic canonical mutation.
- **In scope:** Monthly manual gap reviews, open-hypotheses updates, gap-review reports, draft ADRs for user approval.
- **Out of scope:** Auto-ingest of transcripts, workspace compile/query changes, direct edits to PRD/roadmap/AGENTS.md.

## Safety and non-goals

- **Safety posture:** Fail closed on protected paths; check `rejected-ideas.md` before proposing rediscovered unsafe patterns.
- **Non-goals:** Self-learning auto-update of canonical docs; generic market research without platform scope.

## Regulatory posture

- **Legal/regulatory claims:** none
- **Notes:** Not a compliance workflow.

## Rationale

The experiment could improve platform learning while preserving source authority, user approval, and lane separation.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 1 | Adds review gates around proactive research. |
| Closure | 0 | Neutral until ideas become project work. |
| Grounding | 1 | Encourages source candidates to be evaluated. |
| Vendor truth | 0 | Neutral unless vendor claims are reviewed. |
| Inspectability | 2 | Outputs are explicit hypotheses and reports. |
| Maintainability | 0 | Manageable if monthly and manual. |
| Differentiation | 1 | Strengthens platform co-evolution. |
| Enterprise fit | 1 | Avoids uncontrolled source ingestion. |
| Human review leverage | 2 | Surfaces decisions for user review. |

## Alternatives Considered

1. Do nothing.
2. Let the agent automatically update canonical docs.
3. Only run transcript review when the user provides sources.
4. Run a controlled, candidate-source-only gap review.

## Consequences

### Positive

- Gives platform improvement a repeatable discovery loop.
- Keeps uncertain ideas in `open-hypotheses.md`.
- Avoids rediscovering known rejected ideas.

### Negative / Risks

- Can create noise if run too often.
- Can drift into generic market research if not scoped.

### Safeguards

- No writes outside `wiki/platform-research/**`, `reports/platform-research-review/**`, and draft ADRs.
- Every output must name its evidence quality and validation method.

## Validation Plan

Run one monthly cycle. Success means at least one useful source candidate or hypothesis is accepted by the user, with no protected-file mutation.

## Files Proposed for Future Change

```text
.github/prompts/platform-research-review/gap-review.prompt.md
.github/prompts/platform-research-review.prompt.md
.cursor/agents/platform-research-reviewer.md
docs/platform-intelligence/platform-research-review-setup.md
templates/platform-research/gap-review-report.md
config/platform-research-review.example.yml
```
