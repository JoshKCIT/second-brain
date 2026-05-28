# Research Impact Report: Remio.ai Review vs Alter AI

## Executive Judgment

This transcript is **competitor noise with one inspectability win**. Remio’s passive indexing and “fully developed second brain” positioning are misaligned with Second Brain’s governed documentation compiler. The actionable idea is optional **verbatim citation excerpts** in alignment reports—not copying Remio’s background capture model.

## Source

- Transcript: `raw/platform-transcripts/Remio.ai_Review_-_The_Ultimate_AI_Second_Brain_That_is_So_Much_More_vs._Alter_AI.txt`
- Date: unknown (speaker references weekend posting)
- Participants: unknown reviewer (YouTube-style product walkthrough)
- Processing limitations: AppSumo user review; no vendor doc validation; feature guesses on credits/recording tiers.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 0 |
| Experiment | 2 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-050 | experiment | Verbatim excerpts + anchors strengthen align-cite and human review without changing canonical wiki content. |
| RC-2026-05-27-052 | experiment | Safer variant: compile-time taxonomy suggestions with approval—supports wiki organization at authoring time. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-051 | reject | Silent indexing of all files and browsing history bypasses ingest approval, scope config, and audit trail. |
| RC-2026-05-27-053 | monitor | Treating Remio/Alter as the definition of “second brain” invites scope creep into generic personal-assistant territory. |

## Claim Register Entries

- `RC-2026-05-27-050`
- `RC-2026-05-27-051`
- `RC-2026-05-27-052`
- `RC-2026-05-27-053`

Full YAML: `wiki/platform-research/claim-register.md`

## Recommended Next Actions

### Immediate Changes

- None to canonical docs in this pass.

### Experiments

- Extend `align-cite` output with optional verbatim excerpt blocks (RC-036).
- Pilot compile-time collection/tag suggestions requiring explicit approval (RC-038).

### ADRs to Draft

- `docs/platform-decision-records/DRAFT-RC-2026-05-27-050-verbatim-cite-excerpts.md`

### Claims to Reject

- RC-2026-05-27-051 (background indexing) — recorded in `rejected-ideas.md`.

### Claims Requiring External Validation

- RC-2026-05-27-053 (market positioning) — monitor until product-brief competitive table is refreshed.

## Trust Loop Summary

Fail-closed: no `adopt` on unvalidated Remio/Alter capability claims. RC-036 and RC-038 marked `validated_against_design` where they extend existing align/compile patterns. RC-039 remains `unvalidated` market intelligence.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-050 | experiment | Approve experiment ADR; track in `open-hypotheses.md`; reject via backlog rollback. |
| RC-2026-05-27-051 | reject | Re-review 2026-08-27; submit safer variant as new claim if needed. |
| RC-2026-05-27-052 | experiment | Approve experiment ADR; reject via backlog rollback. |
| RC-2026-05-27-053 | monitor | Re-review when competitive landscape review is scheduled. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
