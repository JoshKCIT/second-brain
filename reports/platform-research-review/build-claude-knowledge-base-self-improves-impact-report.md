# Research Impact Report: Build A Claude Knowledge Base That Self-Improves

## Executive Judgment

This transcript is **high-alignment Karpathy compiler content** with actionable compile/closure extensions: ingested registry, outputs feedback loop, monthly health check, writing-style compile rules. It strongly reinforces no-RAG-at-moderate-scale and index-first query. **Reject** autonomous self-improvement paths that mutate wiki without review or web-fill gaps without approval—both violate Second Brain trust loops.

## Source

- Transcript: `raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt`
- Date: unknown (references 2026 / Claude Cowork)
- Participants: unknown (Systems Made Better channel)
- Processing limitations: Cowork-specific tooling; scheduled auto-action shown; Karpathy scale anecdote unvalidated for enterprise Confluence.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 2 |
| Experiment | 4 |
| Defer | 0 |
| Reject | 2 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-035 | adopt | Karpathy raw/wiki/schema + outputs matches architecture rationale §1. |
| RC-2026-05-27-039 | adopt | Reinforces index-guided retrieval without embeddings for moderate corpora (RC-001). |
| RC-2026-05-27-037 | experiment | Health check dimensions mirror closure lint needs: contradictions, orphans, unsourced, stale. |
| RC-2026-05-27-038 | experiment | Ingested registry enables incremental compile—compile-time efficiency for publish pipeline. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-040 | reject | Auto-saving Q&A to wiki bypasses approval gates (RP-2026-05-27-001). |
| RC-2026-05-27-041 | reject | Web-search gap fill without approval bypasses vendor-truth and fail-closed policy. |

## Claim Register Entries

- RC-2026-05-27-035 through RC-2026-05-27-042

## Recommended Next Actions

### Immediate changes

- None to canonical docs.

### Experiments

- Prototype RC-037 as monthly platform wiki health check (report-only first).
- Design RC-036 outputs loop via workspace-qa filing + compile, not direct wiki mutation.
- Pilot RC-042 writing-style rules in workspace-compile for project artifacts.

### ADRs to draft

- Optional: RC-037 health-check experiment ADR if pilot passes.

### Claims to reject

- RC-2026-05-27-040, 041.

### Claims requiring external validation

- Karpathy ~400k-word / ~100-article scale claim (RC-039 context) unvalidated for 10k+ page Confluence scope.

## Trust Loop Summary

Self-improvement claims fail closed: RC-040/041 rejected per RP-2026-05-27-001 and vendor-truth gates. RC-037 experiment must start report-only (phase 1) with explicit user action for mutations—matching speaker's two-phase health check demo. RC-035/039 validated against current design.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-035, 039 | adopt | Reinforcement; canonical updates via backlog only. |
| RC-2026-05-27-036–038, 042 | experiment | Approve experiment ADR; track in open-hypotheses.md. |
| RC-2026-05-27-040–041 | reject | Re-review 2026-08-27; safer gated variants as new claims. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
