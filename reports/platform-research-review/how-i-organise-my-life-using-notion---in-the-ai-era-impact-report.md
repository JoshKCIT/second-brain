# Research Impact Report: How I Organise My Life Using Notion — In the AI Era

## Executive Judgment

This transcript is a **Notion personal LifeOS product tour** with useful **agent orchestration metaphors** but the wrong substrate for Second Brain. Reject all Notion-SaaS, template-marketplace, credit-agent, and PACT life-dashboard claims. Extract five experiment-worthy patterns (agent hub compile bundle, sub-agent registry, internal/external taxonomy, meeting-notes lane, weekly disposable pulse) plus one adopt reinforcement (on-demand skills). Two Notion vendor superiority claims stay on monitor until primary-source validation.

## Source

- Transcript: `raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt`
- Date: unknown (2026-era Notion Agent features referenced)
- Participants: Simon (Better Creating); colleague Jakob (command center)
- Processing limitations: Sponsored Skillshare segment omitted from scoring; Notion Agent/skills/meeting-notes features not validated against current vendor docs; speaker sells Notion templates.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 1 |
| Experiment | 7 |
| Defer | 0 |
| Reject | 5 |
| Monitor | 2 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-137 | adopt | Reinforces existing `.github/skills/` + operation prompts pattern; on-demand SOPs reduce context bloat without weakening governance. |
| RC-2026-05-27-139 | experiment | Internal vs external knowledge split maps cleanly to `raw/workspace-confluence/` vs `raw/workspace-external/` authority lanes. |
| RC-2026-05-27-135 | experiment | Agent hub as compile artifact bundle (instructions + skills index + scoped KB pointers) improves agent orientation without Notion DBs. |
| RC-2026-05-27-140 | experiment | Dedicated meeting-notes capture lane preserves compile gates; platform transcripts already demonstrate the pattern. |
| RC-2026-05-27-142 | experiment | Weekly pulse as locked disposable report aligns with lint/digest experiments; explicitly not source truth. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-131 | reject | Notion LifeOS replaces filesystem immutability, citation traceability, and jr-engineer closure. |
| RC-2026-05-27-144 | reject | Auto task extraction from meeting notes bypasses approval-gated compile and align-cite. |
| RC-2026-05-27-133 | reject | Credit-based Notion agents as core runtime conflicts with fail-closed, approval-gated platform verbs. |
| RC-2026-05-27-138 | experiment | Schema map could become stale second canonical if not generated from `AGENTS.md` + index. |

## Claim Register Entries

Full YAML records: `wiki/platform-research/claim-register.md` (RC-2026-05-27-131 through RC-2026-05-27-145).

## Recommended Next Actions

### Immediate changes

- None to canonical docs in this pass.

### Experiments

- Agent hub compile bundle (RC-135); sub-agent registry (RC-136); path/schema orientation map (RC-138); internal/external taxonomy tags (RC-139); meeting-notes raw lane (RC-140); universal frontmatter tags (RC-141); weekly pulse report (RC-142).

### ADRs to draft

- `DRAFT-RC-2026-05-27-135-agent-hub-compile-artifacts.md`
- `DRAFT-RC-2026-05-27-136-specialist-sub-agent-registry.md`
- `DRAFT-RC-2026-05-27-139-internal-external-knowledge-taxonomy.md`
- `DRAFT-RC-2026-05-27-140-meeting-notes-capture-lane.md`
- `DRAFT-RC-2026-05-27-142-weekly-pulse-disposable-report.md`

### Claims to reject

- RC-131, RC-132, RC-133, RC-134, RC-144 — recorded in `rejected-ideas.md`.

### Claims requiring external validation

- RC-143 (Notion Personal Agent adoption lift); RC-145 (Notion meeting notes vs Granola/Plaud/Zoom).

## Trust Loop Summary

Notion vendor feature claims (RC-143, RC-145) marked `requires_external_validation: true`, `validation_status: unvalidated`; decisions capped at `monitor`. Substrate and automation rejections grounded against `AGENTS.md` (`validation_status: validated_against_design`). Fail-closed: no `adopt` on unvalidated Notion superiority claims. Experiment claims require user-approved ADRs before protected-file changes.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-2026-05-27-137 | adopt | Document in platform ADR or backlog; reject via backlog rollback. |
| RC-2026-05-27-135–142 | experiment | Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback. |
| RC-2026-05-27-131–134, RC-144 | reject | Re-review per rejected-ideas.md `next_review_after`; submit safer filesystem variant as new claim. |
| RC-2026-05-27-143, RC-145 | monitor | Re-open when Notion vendor docs cached under `raw/workspace-external/notion/`. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, `AGENTS.md`, or raw files were modified based on this transcript.
