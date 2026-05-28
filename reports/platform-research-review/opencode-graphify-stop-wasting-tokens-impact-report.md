# Research Impact Report: OpenCode + Graphify

## Executive Judgment

**Re-reviewed 2026-05-27** under `docs/platform-intelligence/closure-compile-review-brief.md`. The transcript supports **compile-time assembly** for **publish closure**, not v1 expansion into IDE codebase chat. Adopt the boundary rejection for full code-graph indexing (**009a**); experiment with a **safer orientation map** (**009**) alongside RC-008.

## Source

- Transcript: `raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt`
- Date: unknown
- Participants: unknown speaker
- Processing limitations: tutorial and sponsored content; product claims are unvalidated.
- Review lens: closure–compile (2026-05-27 re-review)

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 0 |
| Experiment | 1 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-009 | experiment | Safer variant: disposable cross-source orientation for drafting publishable sets; strengthens compile without replacing align-cite. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-009a | reject | Full mixed code/docs graph indexing duplicates generic IDE assistants and weakens v1 focus. |

## Claim Register Entries

- `RC-2026-05-27-009` (experiment, safer variant)
- `RC-2026-05-27-009a` (reject as stated)

## Recommended Next Actions

### Immediate Changes

- None to canonical docs without ADR.

### Experiments

- Pair RC-009 safer variant with RC-008 session orientation experiment.
- Success metric: fewer orientation reads, no regression on align-cite pass rate or publish closure.

### ADRs to Draft

- Optional: extend RC-008 ADR to include cross-source orientation scope (wiki + project + vendor cache).

### Claims to Reject

- RC-2026-05-27-009a as stated (repo-wide code graph for v1).

### Claims Requiring External Validation

- Graphify/OpenCode product capabilities if experiment proceeds.

## Trust Loop Summary

Fail-closed guardrails applied: vendor and benchmark claims `unvalidated`; orientation map must remain advisory and regenerated from Markdown sources.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-009 | experiment | Approve via implementation backlog / open-hypotheses; reject via backlog rollback. |
| RC-2026-05-27-009a | reject | Reopen only with explicit code-as-source v2 ADR. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
