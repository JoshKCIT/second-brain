# Research Impact Report: Karpathy — Vibe Coding to Agentic Engineering

## Executive Judgment

**Highest product-improving transcript in this batch.** Karpathy articulates the same compiler, verifiability, and human-director principles Second Brain already encodes—useful as external validation and vocabulary for ADRs and onboarding. Reject one-shot “no intermediate artifacts” patterns; monitor sweeping software-3.0 obsolescence claims.

## Source

- Transcript: `raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt`
- Date: unknown (AI Ascent-style interview, ~2026)
- Participants: Andrej Karpathy (guest); hosts unknown
- Processing limitations: paradigm-level claims; model-version references (Opus 4.7) unvalidated.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 5 |
| Experiment | 1 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-090 | adopt | Verifiability explains why align-cite/closure should remain production gates. |
| RC-2026-05-27-092 | adopt | Agentic engineering = faster delivery without lowering publish quality bar. |
| RC-2026-05-27-089 | adopt | Document recompilation is the core Second Brain value prop. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-095 | reject | MenuGen-style one-shot outputs skip stage-gated, citation-grounded artifact sets. |

## Claim Register Entries

RC-2026-05-27-089 through RC-2026-05-27-096 — full YAML in `wiki/platform-research/claim-register.md`.

## Recommended Next Actions

### Immediate changes

- Quote RC-090/092 in next platform ADR or architecture-rationale user-approved pass (not from this review).

### Experiments

- RC-2026-05-27-094: Add agent-native setup skill blocks to `docs/setup-kit.md` pilot.

### ADRs to draft

- Optional: `DRAFT-RC-2026-05-27-094-agent-native-onboarding.md` if user approves experiment.

### Claims to reject

- RC-2026-05-27-095 — `rejected-ideas.md`.

### Claims requiring external validation

- RC-2026-05-27-096 — monitor; no roadmap action until primary-source check.

## Trust Loop Summary

No adopt decisions blocked on external validation. RC-096 marked `unvalidated` and `monitor`. Recompile/verifiability claims `validated_against_design` via `AGENTS.md` and closure-compile brief.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-089–093, 092 | adopt | Approve draft ADR via implementation backlog; reject via backlog rollback. |
| RC-2026-05-27-094 | experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback. |
| RC-2026-05-27-095 | reject | Re-review 2026-08-27 per rejected-ideas.md. |
| RC-2026-05-27-096 | monitor | Re-review when external validation is available. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
