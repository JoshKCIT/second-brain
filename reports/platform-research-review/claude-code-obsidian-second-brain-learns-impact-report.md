# Research Impact Report: Claude Code + Obsidian — Build a Second Brain That Actually Learns

## Executive Judgment

This transcript contains **substantial compile-closure material** disguised as an Obsidian tutorial. The speaker operationalizes the same raw/wiki/schema compiler Second Brain already uses, with useful additions: hot-cache orientation, wiki lint cadence, raw-triggered recompile, and index-over-chunk retrieval. One governance risk (hot cache as authority) is rejected. Pinecone-at-scale is monitor-only.

## Source

- Transcript: `raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt`
- Date: unknown
- Participants: unknown (tutorial presenter)
- Processing limitations: personal Paperclip use case; token/scale anecdotes unvalidated; Obsidian plugin marketing present.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 2 |
| Experiment | 4 |
| Defer | 0 |
| Reject | 1 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-016 | adopt | Confirms three-layer compiler substrate already in AGENTS.md and architecture rationale. |
| RC-2026-05-27-017 | adopt | Index/catalog + wikilink navigation reinforces RC-001/002 compile-time grounding before publish. |
| RC-2026-05-27-019 | experiment | Wiki lint for contradictions/stale/orphans directly supports publish closure maintenance. |
| RC-2026-05-27-018 | experiment | Hot-cache orientation as safer variant of RC-008/009; speeds compile, not publish verification. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-023 | reject | Treating hot cache as authoritative would bypass align-cite and inlined rules at publish. |
| RC-2026-05-27-022 | monitor | Premature vector adoption based on unvalidated ~100-source threshold. |

## Claim Register Entries

- RC-2026-05-27-016 through RC-2026-05-27-023

## Recommended Next Actions

### Immediate changes

- None to canonical docs in this pass.

### Experiments

- Merge RC-018 with RC-008/009 session-orientation backlog.
- Prototype RC-019 wiki lint as workspace-lint extension.
- Pilot RC-020 targeted recompile on raw ingest.

### ADRs to draft

- Optional: bundle RC-019 with workspace-lint ADR if experiment succeeds.

### Claims to reject

- RC-2026-05-27-023 (hot cache replaces verification).

### Claims requiring external validation

- RC-022 Pinecone threshold; Karpathy corpus scale anecdote.

## Trust Loop Summary

All claims marked with `validation_status` in claim register. Market/scale claims (RC-022) remain `unvalidated`; no adopt decision on unvalidated external claims. RC-016/017 validated against current design. RC-023 fail-closed reject prevents orientation artifact from replacing citation verification.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-016, 017 | adopt | Reinforcement only; approve via backlog if canonical doc update desired; reject via rollback. |
| RC-2026-05-27-018–021 | experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback. |
| RC-2026-05-27-022 | monitor | Re-review when holdout eval for hybrid retrieval exists. |
| RC-2026-05-27-023 | reject | Re-review 2026-08-27; submit safer variant as new claim if needed. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
