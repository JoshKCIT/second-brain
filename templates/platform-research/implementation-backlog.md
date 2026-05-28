# Platform Implementation Backlog

One-change-at-a-time queue for approved platform claims.

## Active policy

| Rule | Value |
|---|---|
| Selection method | Highest `priority_score` among `queued` items with satisfied dependencies |
| One item per cycle | Yes |
| User approval required before canonical edits | Yes |
| Rollback required on rejection | Yes |

## Priority formula

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

## Queue

| Rank | Claim ID | Decision | priority_score | Status | Depends on | Draft ADR |
|---:|---|---|---:|---|---|---|
|  |  |  |  | queued |  |  |

Status values: `queued`, `blocked`, `in_progress`, `user_review`, `accepted`, `rolled_back`, `verified_no_change`, `deferred`.

## Current cycle

```yaml
cycle_id: PIC-YYYY-MM-DD-001
selected_claim:
status:
blocked_by:
validation_commands:
  - python -m unittest discover -s tests
  - python scripts/lint-platform-research.py --root .
rollback_plan: ""
next_action: ""
```

## Decision history

| Date | Claim ID | Action | Notes |
|---|---|---|---|
