# Research Impact Report: I Built a Second Brain With Codex in 15 Minutes (Matt Wolfe)

## Executive Judgment

Matt Wolfe's Codex + Obsidian demo is **high-signal validation** for Second Brain's Karpathy compiler shape and **high-signal rejection** for consumer PKM automation. The transcript confirms that teachable **raw inbox → AGENTS.md-routed compile → citation-grounded query** workflows resonate with practitioners—but the showcased **Chrome clipper dumps, nightly auto-compile, Slack briefs, Gmail auto-response, journal/CRM layers, and personal topics/entities vault** are generic-band patterns that weaken governance, authority tagging, and junior-engineer closure. Extract **four adopt reinforcements**, **three compile hygiene experiments**, **one monitor**, and **seven rejects**.

## Source

- Transcript: `raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt`
- Date: unknown (podcast episode; Codex Chrome plugin referenced as "this week" at recording)
- Participants: Matt Wolfe (Future Tools), host (marketing podcast)
- Processing limitations: Personal PKM demo; Codex plugin/integration claims unvalidated against OpenAI docs; Karpathy GitHub bootstrap referenced but not verified in-repo; no enterprise Confluence corpus shown.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 4 |
| Experiment | 3 |
| Defer | 0 |
| Reject | 7 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-160 | adopt | Karpathy LLM-wiki pattern independently validates raw→curated compile + query model already in `AGENTS.md`. |
| RC-2026-05-27-147 | adopt | `AGENTS.md` ingest sub-prompt routing is the teachable surface practitioners copy from Karpathy tutorials. |
| RC-2026-05-27-157 | adopt | Matt's strategy query with explicit wiki source list mirrors citation-grounded `workspace-query` policy. |
| RC-2026-05-27-146 | experiment | Raw inbox staging with approval-gated compile is the safe variant of Matt's clipper→raw workflow. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-151 | reject | Nightly unattended raw→wiki mutation bypasses approval gates and audit trail. |
| RC-2026-05-27-150 | reject | Chrome clipper without authority/domain tags pollutes workspace knowledge (RC-104 pattern). |
| RC-2026-05-27-153 | reject | Proactive Slack briefs act on curated wiki without human review checkpoints. |

## Claim Register Entries

RC-2026-05-27-146 through RC-2026-05-27-160 — full YAML in `wiki/platform-research/claim-register.md`.

## Recommended Next Actions

### Immediate changes

- None without user ADR approval.

### Experiments

- RC-2026-05-27-146: Document raw inbox staging + explicit compile approval in workspace-ingest prompt pilot.
- RC-2026-05-27-148: Pilot topic/entity compile from immutable raw with mandatory Sources sections.
- RC-2026-05-27-149: Add duplicate source URL check to compile prompt; measure redundant raw entries.

### ADRs to draft

- `docs/platform-decision-records/DRAFT-RC-2026-05-27-146-raw-inbox-staging.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-148-topic-entity-compile.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-157-citation-grounded-query.md`

### Claims to reject

- RC-2026-05-27-150, 151, 152, 153, 154, 156, 159 — recorded in `rejected-ideas.md`.

### Claims requiring external validation

- RC-2026-05-27-155: Sitemap-watcher competitive intel — monitor until vendor-truth fetch workflow exists for watched URLs.

## Trust Loop Summary

Karpathy tweet/GitHub references treated as pattern validation, not vendor truth. Codex plugin capabilities (Gmail, Slack, Chrome) marked unvalidated. Consumer clip ingest rejected fail-closed for workspace lane. Experiment claims require user-approved compile prompt changes only; no autonomous wiki writes.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-147, 157, 158, 160 | adopt | Approve draft ADR via implementation backlog; reject via backlog rollback. |
| RC-2026-05-27-146, 148, 149 | experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback. |
| RC-2026-05-27-150–154, 156, 159 | reject | Re-review 2026-08-27 per rejected-ideas.md; submit safer variant as new claim. |
| RC-2026-05-27-155 | monitor | Re-review when vendor-truth cache covers watched competitive sources. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
