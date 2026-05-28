# DRAFT ADR: RC-2026-05-27-111 - Hybrid LLM Deterministic Pipeline

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-111
- Source transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
- Speaker: Dr Vivian Balakrishnan
- Timestamp: 00:16:00-00:16:30
- Claim type: architecture_proposal

## Context

Keynote warns against routing every step through LLMs when deterministic and rule-based systems are cheaper, inspectable, and more reliable. Second Brain already runs `align-cite`, `align-closure`, and lint scripts, but the **ordering and fail-closed requirement** are implicit in prompts rather than documented as a hybrid pipeline contract.

## Decision

Document and enforce a **hybrid pipeline contract**: LLM stages may draft and synthesize; deterministic stages must pass before publish. Required gate order for workspace publish path: `align-cite` → `align-closure` → `workspace-lint` (or equivalent scripts), with explicit user override logged.

## Intent

- **Intended outcome:** No publish without deterministic verification; LLM output never substitutes for align reports.
- **In scope:** Publish/finalize prompt text, implementation backlog item, operator checklist.
- **Out of scope:** Neurosymbolic research stacks; replacing align with model self-check.

## Safety and non-goals

- **Safety posture:** Fail closed—publish blocked on align/lint violations unless user explicitly waives with audit log entry.
- **Non-goals:** LLM-only validation; embedding similarity as citation support.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Total score +14; validated against `AGENTS.md` align and lint operations. External keynote reinforces anti-hammer pattern without changing storage architecture.

## Impact Scores

governance +2, closure +2, grounding +2, inspectability +2, enterprise_fit +2 — total +14.

## Alternatives Considered

- LLM self-critique only before publish — rejected (weak inspectability).
- Skip lint for speed — rejected (closure risk).

## Consequences

### Positive

- Clear operator expectations; auditable publish path.

### Negative / Risks

- Slower publish if lint noise is high.

### Safeguards

- Advisory-only conformance/coverage align; production blockers limited to cite + closure + structural lint.

## Validation Plan

Run one pilot project through documented gate order; compare violation catch rate vs ad hoc publish.

## Files Proposed for Future Change

- `.github/prompts/workspace-publish.prompt.md`
- `.github/prompts/finalize.prompt.md`
- `AGENTS.md` (user-approved only)
