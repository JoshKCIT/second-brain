# Research Impact Report: The AI-Native Shift — Second Brain for AI (George B. Thomas)

## Executive Judgment

This transcript **strongly validates Second Brain’s compiler architecture** (immutable raw, curated wiki, append-only log, identity-aware compile) while surfacing **two governance hazards**: autonomous nightly wiki mutation and a personal CRM command center. Under the closure-compile brief, prioritize identity packs, session handoffs, and human-readable draft review—reject SaaS-aggregator UX.

## Source

- Transcript: `raw/platform-transcripts/The_AI-Native_Shift_-_Second_Brain_for_AI_with_George_B._Thomas.txt`
- Date: unknown (references May 2026 journal dates in demo)
- Participants: George B. Thomas (practitioner), Chris (interviewer)
- Processing limitations: live demo of custom Obsidian plugin; tool stack specific to speaker; promotional training mentions.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 2 |
| Experiment | 5 |
| Defer | 0 |
| Reject | 2 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-054 | adopt | Direct architectural confirmation of raw → wiki compile—core compiler metaphor. |
| RC-2026-05-27-057 | adopt | Append-only journal matches `wiki/log.md` and audit trail requirements. |
| RC-2026-05-27-055 | experiment | Identity-before-generation reduces guessing and improves publish closure for voice-aligned artifacts. |
| RC-2026-05-27-058 | experiment | Save-context handoffs support multi-session project chains without cross in-progress wiki dependencies. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-059 | reject | Autonomous nightly link/structure mutation bypasses approval gates and obscures provenance. |
| RC-2026-05-27-063 | reject | Email/calendar/CRM command center duplicates generic M365 assistant scope; weakens differentiation. |

## Claim Register Entries

- `RC-2026-05-27-054` through `RC-2026-05-27-063`

Full YAML: `wiki/platform-research/claim-register.md`

## Recommended Next Actions

### Immediate Changes

- None to canonical docs without user-approved ADR implementation pass.

### Experiments

- Identity pack template under `templates/personas/` wired into workspace agent prompts (RC-041, RC-048).
- Stage-level `handoff.md` or frontmatter `restart_context` per project (RC-044).
- Rich HTML preview branch for `review` status artifacts (RC-042).
- Optional local-model tier for compile subtasks with holdout eval (RC-046).
- Platform transcript web-clipper intake template (RC-047).

### ADRs to Draft

- `docs/platform-decision-records/DRAFT-RC-2026-05-27-055-identity-packs-compile.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md`

### Claims to Reject

- RC-2026-05-27-059, RC-2026-05-27-063 — recorded in `rejected-ideas.md`.

### Claims Requiring External Validation

- RC-2026-05-27-060 (local model quality for wiki compile) — requires holdout before production compile path.

## Trust Loop Summary

RC-040 and RC-043: `supported_by_current_design` / `validated_against_design`. Experiments include explicit validation plans and fail-closed approval gates. Rejected claims document safer variants (lint-only reconciliation vs autonomous dream; scoped compile orientation vs CRM dashboard).

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-054, RC-2026-05-27-057 | adopt | Reinforcement only; no backlog change unless docs gap found. |
| RC-2026-05-27-055, RC-056, RC-058, RC-060, RC-061, RC-062 | experiment | Approve experiment ADR; track in `open-hypotheses.md`; rollback via backlog. |
| RC-2026-05-27-059, RC-2026-05-27-063 | reject | Re-review 2026-08-27 per `rejected-ideas.md`. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
