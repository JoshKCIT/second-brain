# DRAFT ADR: RC-2026-06-09-007 - Falsifiable Platform Change Manifest

## Status

Draft

## Source Claim

- Claim ID: RC-2026-06-09-007
- Source transcript: `raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt`
- Speaker: unknown
- Timestamp: 00:05:00-00:05:30
- Claim type: evaluation_proposal

## Context

A-H-E pairs each harness edit with a self-declared prediction verified in the next evaluation round; failed edits roll back. Second Brain PIC cycles already accept/rollback backlog items but lack a standard manifest schema tying each change to a falsifiable expected outcome.

## Decision

Experiment: require PIC backlog items and platform ADRs to include a change manifest with predicted outcome, verification command, and rollback steps before implementation begins.

## Intent

- **Intended outcome:** Make platform improvements falsifiable like align-cite/closure checks.
- **In scope:** `implementation-backlog.md` schema; PIC cycle validation template.
- **Out of scope:** Autonomous commit loops; wiki/content auto-mutation.

## Safety and non-goals

- **Safety posture:** Verification runs before accept; failed prediction triggers rollback.
- **Non-goals:** Unattended multi-round evolution without CEO gate.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Extends Karpathy RC-090 verifiability and existing PIC accept/rollback without weakening human approval gates.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | +2 | Explicit verification before accept |
| Closure | +1 | Better regression detection |
| Grounding | +1 | Predictions tied to tests/lint |
| Vendor truth | 0 | Neutral |
| Inspectability | +2 | Manifest is auditable artifact |
| Maintainability | +1 | Standard PIC template |
| Differentiation | +1 | Governance-quality improvement |
| Enterprise fit | +1 | Audit trail |
| Human review leverage | +1 | CEO reviews prediction before accept |

## Alternatives Considered

1. Continue PIC without manifest fields.
2. Full A-H-E autonomous verify-and-rollback loop.
3. Lightweight manifest on PIC items only.

## Consequences

### Positive

- Clearer accept/reject criteria for platform changes.
- Easier rollback when predictions fail.

### Negative / Risks

- Template overhead for small fixes.

### Safeguards

- Manifest required only for `experiment` and `adopt` PIC items.
- No auto-accept on predicted success.

## Validation Plan

Apply manifest template to next three PIC cycles; measure whether rollback reasons are clearer and whether failed predictions are caught before accept.

## Files Proposed for Future Change

```text
wiki/platform-research/implementation-backlog.md
templates/platform-research/
.github/prompts/platform-implement-backlog.prompt.md
```
