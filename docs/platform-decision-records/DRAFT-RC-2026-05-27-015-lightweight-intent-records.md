# DRAFT ADR: RC-2026-05-27-015 - Lightweight Intent Records

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-015
- Source transcript: `raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt`
- Speaker: Steve
- Timestamp: 00:31:30-00:55:30
- Claim type: risk_claim

## Context

The legal segment emphasized records of intended use, risk management, and auditability. The legal specifics are unvalidated and should not become requirements, but Second Brain can cheaply improve auditability by making intent explicit in platform ADRs.

## Decision

Experiment with lightweight intent/safety sections in platform ADRs. Do not add heavy compliance machinery or legal claims to canonical docs without separate validation.

## Rationale

Intent records fit the existing ADR and log pattern. They improve enterprise readiness without changing the local-first v1 architecture.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 2 | Captures intent and safety posture. |
| Closure | 0 | Neutral. |
| Grounding | 1 | Forces source/validation clarity. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 2 | Makes rationale auditable. |
| Maintainability | 0 | Small added template burden. |
| Differentiation | 1 | Supports governed platform evolution. |
| Enterprise fit | 2 | Better readiness for review. |
| Human review leverage | 1 | Helps the user approve or reject changes. |

## Alternatives Considered

1. Do nothing.
2. Add a full compliance framework now.
3. Add lightweight intent/safety sections to draft ADRs only.

## Consequences

### Positive

- Improves auditability.
- Keeps legal claims out of canonical requirements until validated.

### Negative / Risks

- Could invite unnecessary process if overused.

### Safeguards

- Mark legal/regulatory statements unvalidated unless checked against primary sources.
- Keep the fields brief and decision-focused.

## Validation Plan

Use the fields on the next three platform ADRs and assess whether they improve review clarity. If they add noise, remove them.

## Files Proposed for Future Change

```text
docs/platform-decision-records/DRAFT-template-research-claim.md
templates/platform-research/
```
