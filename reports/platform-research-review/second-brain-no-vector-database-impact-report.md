# Research Impact Report: second-brain-no-vector-database

## Executive Judgment

The transcript contains high-value reinforcement for Second Brain's current retrieval architecture. It does not introduce a new product direction so much as sharpen the reasoning: preserve document structure, make retrieval inspectable, and verify citations independently from retrieval.

## Source

- Transcript: `raw/platform-transcripts/second-brain-no-vector-database.txt`
- Date: unknown
- Participants: unknown speaker
- Processing limitations: short transcript; benchmark claims are unvalidated.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 2 |
| Experiment | 0 |
| Defer | 0 |
| Reject | 0 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-001 | adopt | Reinforces index-guided retrieval and gives a concrete eval frame for long structured documents. |
| RC-2026-05-27-002 | adopt | Supports the core distinction between retrieved context and verified citation support. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-001 | adopt | The "98.7% accuracy" claim is unvalidated and should not be cited as vendor/benchmark truth. |

## Claim Register Entries

- `RC-2026-05-27-001`
- `RC-2026-05-27-002`

## Recommended Next Actions

### Immediate Changes

- None to canonical docs in this pass.

### Experiments

- Add a future retrieval eval comparing section-tree navigation to any later vector/hybrid baseline.

### ADRs to Draft

- Draft page-index retrieval ADR using `RC-2026-05-27-001` and `RC-2026-05-27-002`.

### Claims to Reject

- None.

### Claims Requiring External Validation

- Validate any benchmark/accuracy claims before citing them externally.

## Trust Loop Summary

Fail-closed guardrails applied during review: vendor and benchmark claims marked `unvalidated`; no transcript claim promoted to canonical knowledge without draft ADR routing. See claim register `validation_status` and `correction_route` fields.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| See claim register | — | Approve via implementation backlog ADR review; reject via backlog rollback; reopen rejected claims per `rejected-ideas.md`. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
