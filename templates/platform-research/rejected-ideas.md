# Rejected Claims Register

This register preserves rejected claims and recurring rejection patterns so they are not rediscovered repeatedly.

Each rejected claim from `wiki/platform-research/claim-register.md` must have a matching record here with rationale, safer variant, and re-review date.

Sync after claim register updates:

```bash
python scripts/sync-rejected-register.py --root .
```

## Review cadence

| Rule | Value |
|---|---|
| Default re-review interval | Every 3 months |
| Next scheduled re-review | YYYY-MM-DD |

## Summary index

| ID | Idea (short) | Rejected | Next review | Status | Primary artifact |
|---|---|---|---|---|---|
|  |  |  |  | closed |  |

## Rejected claim records

Add one YAML block per rejected claim ID (`RC-*`).

```yaml
record_id: RC-YYYY-MM-DD-001
record_type: rejected_claim
source_transcript: raw/platform-transcripts/path/to/transcript.txt
claim_analysis: wiki/platform-research/transcript-analyses/{slug}-claims.md
impact_report: reports/platform-research-review/{slug}-impact-report.md
atomic_claim: ""
verbatim_excerpt: ""
decision: reject
decision_date: YYYY-MM-DD
next_review_after: YYYY-MM-DD
review_cadence: quarterly
total_score: 0
decision_rationale: ""
rejection_reason: ""
safer_variant: ""
reopen_conditions:
  - ""
owner: unassigned
status: closed
last_reviewed: YYYY-MM-DD
```

## Rejected recurring patterns

Add one YAML block per cross-transcript pattern (`RP-*`).

```yaml
record_id: RP-YYYY-MM-DD-001
record_type: rejected_pattern
first_seen: YYYY-MM-DD
related_claims:
  - RC-YYYY-MM-DD-001
decision: reject
decision_date: YYYY-MM-DD
next_review_after: YYYY-MM-DD
review_cadence: quarterly
pattern: ""
rejection_reason: ""
safer_variant: ""
reopen_conditions:
  - ""
owner: unassigned
status: closed
last_reviewed: YYYY-MM-DD
```

## Decision history

| Date | ID | Action | Notes |
|---|---|---|---|
|  |  | rejected |  |
