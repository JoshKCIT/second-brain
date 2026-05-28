# ADR: Platform Implementation Priority Loop

## Status

Accepted

## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-001
- Notes: User approved process ADR alongside RC-2026-05-27-014.

## Source Claim

- Claim ID: RC-2026-05-27-014 (primary), RC-2026-05-27-010 (supporting)
- Source transcript: platform research batch synthesis
- Claim type: workflow_proposal

## Context

Second Brain now has reviewed claims, draft ADRs, rejection history, and hypotheses. The missing piece is a **recursive implementation loop** that:

1. Picks the highest-lift claim whose dependencies are satisfied
2. Implements one change at a time
3. Validates automatically
4. Reviews with the user
5. Accepts or rolls back
6. Re-scores the backlog and continues

Without stack-aware prioritization, experiments can ship before the trust and artifact foundations that make them safe.

## Decision

Adopt a platform implementation priority loop with:

- A single backlog file: `wiki/platform-research/implementation-backlog.md`
- Stack-lift scoring in addition to transcript impact scores
- One claim per cycle
- Mandatory validation before user review
- Mandatory rollback on user rejection
- Re-scoring after every cycle

## Rationale

This turns platform research from a static report into a governed delivery pipeline. It preserves human approval, makes rollback explicit, and favors claims that unlock other claims.

## Priority model

Use `priority_score` from the backlog file:

```text
priority_score =
  (stack_lift * 3)
  + (platform_lift * 2)
  + (validation_clarity * 2)
  + (implementability * 2)
  + (evidence_strength * 1)
  - (canonical_risk * 2)
  - (experiment_uncertainty * 1)
```

Transcript `total_score` remains the evidence for **whether** to adopt/experiment/defer/reject. `priority_score` decides **when** to implement among approved items.

## Cycle workflow

```mermaid
flowchart TD
  A[Load implementation-backlog.md] --> B[Select top queued item with deps met]
  B --> C{User approved draft ADR?}
  C -->|No| D[Stop or revise ADR]
  C -->|Yes| E[Implement smallest reversible change]
  E --> F[Run validation commands]
  F --> G{Validation passed?}
  G -->|No| H[Fix or rollback]
  G -->|Yes| I[Present results to user]
  I --> J{User accepts?}
  J -->|Yes| K[Mark accepted; promote ADR (PH-008); re-score backlog]
  J -->|No| L[Rollback; mark rolled_back; re-score]
  K --> A
  L --> A
```

On accept (PH-008): update ADR Status/Approval; **`platform-implement-backlog` agent** runs `python scripts/promote-platform-adr.py --root . --claim-id {id} --pic-cycle {cycle}` (not the CEO).

## Validation gate (required every cycle)

```bash
python -m unittest discover -s tests
python scripts/lint-platform-research.py --root .
```

Add claim-specific checks when relevant (for example retrieval evals, graph prototype checks, or prompt-lint additions).

## Rollback rule

Every cycle must record:

- Git commit range or patch set
- Files touched
- Exact revert command or steps

If the user rejects the change, rollback before selecting the next backlog item.

## Consequences

### Positive

- Clear “what next” ordering
- Compounding gains from foundation-first delivery
- Safer experiments
- Auditable accept/reject history

### Negative / Risks

- Adds process overhead for small changes
- Priority scores are planning estimates until measured

### Safeguards

- One item per cycle
- No canonical edits without ADR approval
- Re-score after each accept/reject
- Keep rejected patterns in `wiki/platform-research/rejected-ideas.md`

## Validation Plan

Run one full cycle on RC-2026-05-27-014. Success means:

1. Backlog selection is unambiguous
2. Validation runs automatically
3. User can accept or reject with rollback
4. Backlog status and history update correctly

## Files Proposed for Future Change

```text
wiki/platform-research/implementation-backlog.md
.github/prompts/platform-research-review.prompt.md
.cursor/agents/platform-research-reviewer.md
config/platform-research-review.example.yml
AGENTS.md
```
