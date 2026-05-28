# Research Impact Report: Build AI Second Brain Knowledge Base (Step-by-Step)

## Executive Judgment

This tutorial **validates the Karpathy/Second Brain raw→wiki compiler shape** but implements it as a **personal chat OS** (journal, CRM, hourly auto-ingest). Valuable as evidence that the three-layer model is teachable; **not** a v1 product direction. Two small hygiene experiments (processed folder, raw backlinks) are worth piloting alongside RC-050.

## Source

- Transcript: `raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt`
- Date: unknown (Matt Wolf channel tutorial)
- Participants: Matt Wolf (speaker)
- Processing limitations: Codex/OpenAI tooling; Karpathy GitHub wiki reference; sponsor segment (Hostinger/OpenClaw).

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 2 |
| Experiment | 2 |
| Defer | 0 |
| Reject | 4 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-097 | adopt | raw/wiki/AGENTS/index/log matches canonical architecture. |
| RC-2026-05-27-098 | adopt | Explicit process/ingest approval aligns with approval-gated mutations. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-101 | reject | Auto-wiki-from-query erodes human review and pollutes workspace knowledge. |
| RC-2026-05-27-100 | reject | Hourly unattended raw→wiki violates fail-closed ingest policy. |

## Claim Register Entries

RC-2026-05-27-097 through RC-2026-05-27-104 — full YAML in `wiki/platform-research/claim-register.md`.

## Recommended Next Actions

### Immediate changes

- None.

### Experiments

- RC-2026-05-27-102: Document `raw/processed/` convention in compile prompt after user-approved pilot.
- RC-2026-05-27-103: Merge with RC-050 cite/link pilot in compile workflow.

### ADRs to draft

- None unless RC-102/103 promoted after pilot.

### Claims to reject

- RC-2026-05-27-099, 100, 101, 104 — `rejected-ideas.md`.

### Claims requiring external validation

- None.

## Trust Loop Summary

Karpathy wiki GitHub reference treated as pattern validation, not vendor truth. Consumer-content ingest rejected for enterprise authority/domain requirements. Experiment claims require user-approved compile prompt changes only.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-097, 098 | adopt | Approve draft ADR via implementation backlog; reject via backlog rollback. |
| RC-2026-05-27-102, 103 | experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback. |
| RC-2026-05-27-099–101, 104 | reject | Re-review 2026-08-27 per rejected-ideas.md. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
