# Research Impact Report: You've Been Using Git Wrong

## Executive Judgment

This transcript explains **why GitHub feels weird**, not how to rebuild Second Brain. The actionable thread is auditability: decision context should live beside artifact history. Patch-only collaboration is a reject for this product; team-scale GitHub vs git-native ownership stays on monitor for v2.

## Source

- Transcript: `raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt`
- Date: unknown
- Participants: unknown
- Processing limitations: General git collaboration essay; no Second Brain user pilot data.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 0 |
| Experiment | 1 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-079 | experiment | Improves inspectability and human review leverage for publish/align without leaving rationale in Slack-only threads. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-080 | reject | Patch/mail-list workflow fights jr-engineer closure and existing GitHub-based team habits for doc repos. |

## Claim Register Entries

- `RC-2026-05-27-079` through `RC-2026-05-27-081`

## Recommended Next Actions

### Immediate changes

- None.

### Experiments

- RC-037: structured decision append to `wiki/log.md` on publish/align (paired with trust loop).

### ADRs to draft

- Optional draft for RC-037 if experiment approved.

### Claims to reject

- RC-038 → `rejected-ideas.md`

### Claims requiring external validation

- RC-039 team-scale sync (ties to RC-005 defer queue).

## Trust Loop Summary

RC-037 supports audit stage of trust loop (capture decision → log → correct). No adopt on unvalidated team-collaboration claims.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-079 | experiment | Approve experiment ADR; track in `open-hypotheses.md`; reject via backlog rollback. |
| RC-2026-05-27-080 | reject | Re-review 2026-08-27. |
| RC-2026-05-27-081 | monitor | Revisit with RC-005 when multi-user scope opens. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, `AGENTS.md`, or raw files were modified based on this transcript.
