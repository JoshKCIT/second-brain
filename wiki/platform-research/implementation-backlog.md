# Platform Implementation Backlog

This queue turns reviewed claims into **one change at a time**: implement → validate → user review → accept or rollback → re-score → next item.

Priority uses **stack lift**, not raw transcript impact alone. A claim with a lower impact score but high unblocking value can rank above a stronger standalone experiment.

**Stack-aware rescoring (2026-05-27):** Policy-tier claims bundle in one cycle (RC-122+157). Foundation claims RC-018 and RC-058 precede dependent experiments. Verified-no-change and doc-reinforcement claims removed from active queue.

**Resync (2026-05-28):** PH-003/PH-005 main-queue status aligned with PIC-013/014; dependency checkmarks updated after RC-163/RC-116 acceptance.

**Full rescore (2026-05-28):** PIC-001–023 closed 21 RC cycles. Policy shifts to **validation-first**: PH-007 consolidation next; new RC PICs paused until workspace trigger (ingest, review artifact, persona project). Report: `reports/platform-research-review/backlog-rescore-2026-05-28.md`.

## Active policy

| Rule | Value |
|---|---|
| Selection method | Highest `priority_score` among `queued` items with satisfied dependencies |
| Phase gate | PH-007 ✓; **PH-2026-06-09 wave** queued (CEO 2026-06-09); general RC PIC pause unless workspace trigger |
| Validation debt | ≥8 accepted experiments lack pilot — apply `validation_debt_penalty` to new RCs |
| One item per cycle | Yes (bundled when policy-tier) |
| User approval required before canonical edits | Yes |
| Rollback required on rejection | Yes |
| Re-score after each cycle | Yes |

## Priority formula

```text
priority_score =
  (stack_lift * 3)
  + (platform_lift * 2)
  + (validation_clarity * 2)
  + (implementability * 2)
  + (evidence_strength * 1)
  - (canonical_risk * 2)
  - (experiment_uncertainty * 1)
  - (validation_debt_penalty * 2)   # 1 while pilot validation debt open
```

## Stack tiers

| Tier | Role | Status |
|---|---|---|
| 0 — Accepted | Foundation complete | RC-014, RC-010, RC-001/002, RC-015, RC-003 ✓ |
| 1 — Policy | Query discipline | RC-122 + RC-157 ✓ |
| 2 — Scaffolding | Retrieval + agent rules | RC-018 ✓, RC-161 ✓ |
| 3 — Session | Handoff ergonomics | RC-058 ✓, RC-130 ✓ |
| 3b — Hygiene | Agent chain gaps | PH-001 ✓ … PH-006 ✓ |
| 4 — Experiments | Pilot validation pending | RC-163, RC-116, RC-167, RC-164, RC-162, RC-117, RC-165 ✓ |
| 5 — Compile lane | Raw inbox | RC-146 ✓, RC-148 ✓ |
| **6 — Consolidation** | **Complete** | **PH-007 ✓** |
| 7 — Workspace-triggered | RC queue on pilot | RC-149, RC-114, RC-050, … |
| 8 — Park | Superseded / low band | See Parked table |
| **9 — Chain profiles** | **Specialist stages + project-type chains** | **PH-001 ✓, PH-002 ✓; PH-003–007 queued** |

Template: `templates/platform-research/implementation-backlog.md`. Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`.

## Queue

| Rank | Claim ID | Decision | priority_score | Status | Depends on | Draft ADR |
|---:|---|---|---:|---|---|---|
| 1 | RC-2026-05-27-014 | adopt | 38 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-014-platform-research-artifacts.md` |
| 2 | RC-2026-05-27-010 | adopt | 35 | accepted | RC-014 ✓ | `docs/platform-decision-records/RC-2026-05-27-010-trust-loop-workflow-pattern.md` |
| 3 | RC-2026-05-27-001 | adopt | 31 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-001-page-index-retrieval.md` |
| 4 | RC-2026-05-27-002 | adopt | 29 | accepted | RC-001 ✓ | (bundle with RC-001) |
| 5 | RC-2026-05-27-015 | experiment | 24 | accepted | RC-014 ✓ | `docs/platform-decision-records/RC-2026-05-27-015-lightweight-intent-records.md` |
| 6 | RC-2026-05-27-003 | experiment | 22 | accepted | RC-010 ✓, RC-014 ✓ | `docs/platform-decision-records/RC-2026-05-27-003-controlled-gap-research.md` |
| 7 | RC-2026-05-27-012 | experiment | 20 | blocked | RC-010 ✓, RC-014 ✓, failure data | `docs/platform-decision-records/DRAFT-RC-2026-05-27-012-advisory-harness-failure-review.md` |
| 8 | RC-2026-05-27-122 + RC-157 | adopt | 28 | accepted | RC-001 ✓, RC-002 ✓ | RC-122 + RC-157 (bundled) |
| 9 | RC-2026-05-27-018 | adopt | 27 | accepted | RC-001 ✓ | `docs/platform-decision-records/RC-2026-05-27-018-retrieval-contract-first.md` |
| 10 | RC-2026-05-27-161 | adopt | 24 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-161-hierarchical-instruction-stacking.md` |
| 11 | RC-2026-05-27-058 | experiment | 23 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-058-project-session-handoff.md` |
| 12 | RC-2026-05-27-130 | experiment | 22 | accepted | RC-058 ✓ | `docs/platform-decision-records/RC-2026-05-27-130-project-stage-scaffold.md` |
| 12a | PH-2026-05-27-001 | hygiene | 26 | accepted | RC-058 ✓, RC-130 ✓ | `templates/workspace/project-meta.yml.md` |
| 12b | PH-2026-05-27-002 | hygiene | 25 | accepted | RC-161 ✓, PIC-011 | finalize delegation in start-project |
| 12c | PH-2026-05-27-003 | hygiene | 21 | accepted | RC-058 ✓, RC-130 ✓ | `docs/platform-decision-records/PH-2026-05-27-003-inter-stage-output-contract.md` |
| 13 | RC-2026-05-27-163 | experiment | 21 | accepted | RC-058 ✓ | `docs/platform-decision-records/RC-2026-05-27-163-disposable-session-orientation.md` |
| 14 | RC-2026-05-27-167 | experiment | 20 | accepted | RC-058 ✓, RC-130 ✓ | `docs/platform-decision-records/RC-2026-05-27-167-project-subfolder-rule-stacking.md` |
| 14a | PH-2026-05-27-004 | hygiene | 19 | accepted | RC-122 ✓ | `docs/platform-decision-records/PH-2026-05-27-004-advisory-align-cite-per-stage.md` |
| 14b | PH-2026-05-27-005 | hygiene | 18 | accepted | PH-001 ✓ | `docs/platform-decision-records/PH-2026-05-27-005-reopen-stage-protocol.md` |
| 15 | RC-2026-05-27-164 | experiment | 19 | accepted | RC-163 ✓ | `docs/platform-decision-records/RC-2026-05-27-164-session-audit-skill.md` |
| 16 | RC-2026-05-27-162 | experiment | 18 | accepted | RC-018 ✓, RC-161 ✓ | `docs/platform-decision-records/RC-2026-05-27-162-routing-map-agents-shim.md` |
| 16a | PH-2026-05-27-006 | hygiene | 16 | accepted | RC-162 ✓ | platform escalation row in routing map |
| 17 | RC-2026-05-27-165 | experiment | 17 | accepted | RC-018 ✓, RC-161 ✓ | `docs/platform-decision-records/RC-2026-05-27-165-lean-root-pointer-resources.md` |
| 18 | RC-2026-05-27-116 | experiment | 20 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-116-thinking-artifact-mode-separation.md` |
| 19 | RC-2026-05-27-117 | experiment | 18 | accepted | RC-116 ✓ | `docs/platform-decision-records/RC-2026-05-27-117-thinking-partner-subagent.md` |
| 20 | RC-2026-05-27-146 | experiment | 18 | accepted | — | `docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md` |
| 21 | RC-2026-05-27-148 | experiment | 16 | accepted | RC-146 ✓ | `docs/platform-decision-records/RC-2026-05-27-148-topic-entity-compile.md` |
| 22 | RC-2026-05-27-149 | experiment | 16 | workspace_triggered | RC-146 ✓ | — |
| 23 | RC-2026-05-27-050 | experiment | 14 | workspace_triggered | RC-122 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-050-verbatim-cite-excerpts.md` |
| 24 | RC-2026-05-27-055 | experiment | 10 | workspace_triggered | RC-122 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-055-identity-packs-compile.md` |
| 25 | PH-2026-06-09-001 | hygiene | 22 | accepted | PH-001 ✓, RC-130 ✓ | `docs/platform-decision-records/PH-2026-06-09-001-chain-profile-schema.md` |
| 26 | PH-2026-06-09-002 | hygiene | 20 | accepted | PH-2026-06-09-001 ✓ | `docs/platform-decision-records/PH-2026-06-09-002-technical-doc-initiative-profile.md` |
| 27 | PH-2026-06-09-003 | experiment | 18 | accepted | PH-2026-06-09-001 ✓, RC-117 ✓ | `docs/platform-decision-records/PH-2026-06-09-003-technical-writer-stage.md` |
| 28 | PH-2026-06-09-004 | experiment | 17 | accepted | PH-2026-06-09-001 ✓, PH-004 ✓ | `docs/platform-decision-records/PH-2026-06-09-004-architect-reviewer-stage.md` |
| 29 | PH-2026-06-09-005 | experiment | 16 | queued | PH-2026-06-09-001 | `docs/platform-decision-records/DRAFT-PH-2026-06-09-005-qa-pre-publish-stage.md` |
| 30 | PH-2026-06-09-006 | experiment | 15 | workspace_triggered | PH-2026-06-09-001, RC-140 trigger | `docs/platform-decision-records/DRAFT-PH-2026-06-09-006-meeting-synthesis-profile.md` |
| 31 | PH-2026-06-09-007 | experiment | 14 | workspace_triggered | PH-2026-06-09-001, RC-148 ✓ | `docs/platform-decision-records/DRAFT-PH-2026-06-09-007-knowledge-hub-profile.md` |
| 32 | RC-2026-05-27-136 | experiment | 12 | unpark_watch | PH-2026-06-09-001 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-136-specialist-sub-agent-registry.md` |
| 33 | RC-2026-06-09-012 | adopt | 11 | queued | RC-001 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-06-09-012-structure-vs-unstructured-retriever-heuristic.md` |
| 34 | RC-2026-06-09-013 | experiment | 10 | queued | RC-009, RC-146 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-06-09-013-three-pass-compile-orientation-map.md` |

## Next selectable (rescore 2026-06-09)

**Phase A — implement now** (CEO-directed chain-profiles wave):

| Select rank | ID | Score | Status | Notes |
|---:|---|---:|---|---|
| 1 | PH-2026-06-09-005 | 16 | queued | **Next PIC** — QA pre-publish stage |

**Phase B — doc reinforcement** (fold into existing prompts; no PIC unless bundled):

| ID | Score | Fold into |
|---|---:|---|
| RC-105, RC-115 | 18 | finalize + publish prompts |
| RC-113 | 12 | `second-brain` onboarding |

**Phase C — workspace-triggered** (unpark when trigger fires; not selectable until then):

| Rank | Claim ID | Rescored | Trigger |
|---:|---|---:|---|
| 1 | RC-2026-05-27-149 | 16 | First Confluence/vendor ingest batch |
| 2 | RC-2026-05-27-114 | 15 | After first ingest+compile pilot |
| 3 | RC-2026-05-27-050 | 14 | First artifact at `review` |
| 4 | RC-2026-05-27-094 | 13 | Fresh-clone setup friction |
| 5 | RC-2026-05-27-139 | 12 | Multi-source ingest |
| 6 | RC-2026-05-27-140 | 11 | Meeting notes ingest |
| 7 | RC-2026-05-27-055 | 10 | Persona/voice project |
| 8 | RC-2026-05-27-103 | 10 | After RC-148 compile pilot |
| 9 | RC-2026-05-27-102 | 9 | Orphan noise after ingest |

**Blocked:** RC-012 (needs ≥3 failure traces).

**Paused:** New RC PICs until workspace trigger or explicit unpark of parked `unpark_watch` item.

**Parked rescore:** Per-claim scores in Parked table; report at `reports/platform-research-review/parked-rescore-2026-05-28.md`.

## Verified baseline (no backlog work)

| Claim ID | Decision | Status | Notes |
|---|---|---|---|
| RC-2026-05-27-004 | adopt | verified_no_change | Filesystem-first substrate |
| RC-2026-05-27-006 | adopt | verified_no_change | Durable stage artifacts |
| RC-2026-05-27-111 | adopt | verified_no_change | align-*, lint deterministic checks |
| RC-2026-05-27-147 | adopt | verified_no_change | AGENTS.md ingest routing |
| RC-2026-05-27-160 | adopt | verified_no_change | Karpathy compiler model in AGENTS.md |
| RC-2026-05-27-016, RC-035, RC-097 | adopt | verified_no_change | Three-layer raw/wiki/AGENTS |
| RC-2026-05-27-017, RC-039 | adopt | verified_no_change | Page-index / moderate corpus (RC-001 ✓) |
| RC-2026-05-27-066, RC-068, RC-069, RC-071, RC-075, RC-078 | adopt | verified_no_change | Skills/prompts/specialist chain |
| RC-2026-05-27-082, RC-087, RC-089 | adopt | verified_no_change | AGENTS navigation, filesystem-first |
| RC-2026-05-27-090, RC-091, RC-092, RC-093 | adopt | verified_no_change | align-cite, CEO gates, agentic engineering |
| RC-2026-05-27-098 | adopt | verified_no_change | User-triggered compile (RC-146 ✓) |
| RC-2026-05-27-137 | adopt | verified_no_change | Skills library `.github/skills/` |
| RC-2026-05-27-158 | adopt | verified_no_change | Open repo/vault — operational not schema |

## Doc reinforcement (not standalone cycles)

| Claim ID | Fold into | Rescored |
|---|---|---:|
| RC-2026-05-27-105, RC-115 | Finalize/publish prompts | 18 |
| RC-2026-05-27-113 | Onboarding prompt | 12 |
| RC-2026-05-27-107 | Onboarding prompt (parked rescore) | 9 |
| RC-2026-05-27-138 | routing-map cross-links (parked rescore) | 6 |

## Parked (rescore 2026-05-28, per-claim 2026-05-28)

Not in active queue unless **unpark trigger** fires or CEO explicit unpark. Full analysis: `reports/platform-research-review/parked-rescore-2026-05-28.md`.

### Summary by disposition

| Disposition | Count | Score range | Action |
|---|---|---:|---|
| `permanent_park` | 10 | 0–4 | No PIC; reject candidates noted |
| `monitor` | 8 | 4–6 | Watch pilot logs |
| `doc_reinforcement` | 3 | 6–9 | Fold into prompts |
| `unpark_watch` | 7 | 7–12 | Re-enter on trigger |
| `workspace_triggered` | 3 | 4–8 | Merge with Phase C |
| `reject_candidate` | 0 | 0–2 | Synced to rejected-ideas.md |

### Per-claim table

| ID | Rescore | Disposition | Unpark trigger |
|---|---:|---|---|
| RC-118 | 2 | **rejected** | Superseded by RC-130 daily-progress (2026-05-28) |
| RC-119 | 2 | **rejected** | Superseded by RC-130 research + handoff (2026-05-28) |
| RC-120 | 3 | permanent_park | — |
| RC-121 | 5 | monitor | Regular chat transcript imports |
| RC-021 | 2 | **rejected** | Superseded by RC-148 compile (2026-05-28) |
| RC-166 | 4 | workspace_triggered | Persona project (bundle RC-055) |
| RC-135 | 3 | permanent_park | — (PH-007 registry) |
| RC-136 | 12 | **unpark_watch** | PH-2026-06-09-001 accepted or CEO explicit unpark |
| RC-083 | 2 | permanent_park | — (RC-162/165) |
| RC-138 | 6 | doc_reinforcement | Fold into routing-map |
| RC-019 | 9 | unpark_watch | Biweekly lint cadence pain |
| RC-037 | 8 | unpark_watch | Monthly health report (bundle RC-019) |
| RC-142 | 7 | unpark_watch | CEO orientation pulse request |
| RC-029 | 8 | workspace_triggered | First ingest batch |
| RC-030 | 7 | unpark_watch | Multi-project capture metadata |
| RC-042 | 2 | permanent_park | — (style band) |
| RC-070 | 5 | monitor | v1.x CI automation request |
| RC-107 | 9 | doc_reinforcement | Fold into onboarding (with RC-113) |
| RC-112 | 3 | permanent_park | — (edge deploy) |
| RC-141 | 6 | monitor | Scoped query tag misses |
| RC-020 | 6 | monitor | Incremental recompile pain |
| RC-024 | 4 | permanent_park | — |
| RC-031 | 3 | permanent_park | — |
| RC-036 | 6 | monitor | outputs/ loop insufficient |
| RC-038 | 8 | unpark_watch | After ingest (RC-102 family) |
| RC-067 | 5 | monitor | Compile mis-scoping |
| RC-079 | 9 | unpark_watch | First publish/align event |
| RC-032 | 10 | unpark_watch | Domain research compile |

### Deferred (rescored, not parked)

| ID | Rescore | Disposition | Re-enter when |
|---|---:|---|---|
| RC-005 | 1 | deferred | v2 multi-user |
| RC-007 | 1 | deferred | CEO unparks graph branch |
| RC-008 | 1 | deferred | RC-007 |
| RC-011 | 3 | monitor | v1 pilot usage |

## Agent chain hygiene queue (PH-*)

From `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`. Not transcript claims; platform maintenance discovered during RC-161/058 review.

| ID | Title | Status | Notes |
|---|---|---|---|
| PH-2026-05-27-001 | meta.yml stage state machine | accepted | PIC-012; template + prompt transitions |
| PH-2026-05-27-002 | start-project finalize alignment | accepted | PIC-011 |
| PH-2026-05-27-003 | inter-stage output contract | accepted | PIC-013 |
| PH-2026-05-27-004 | advisory align-cite per stage | accepted | PIC-015 |
| PH-2026-05-27-005 | reopen stage protocol | accepted | PIC-014 |
| PH-2026-05-27-006 | platform escalation routing | accepted | PIC-020 bundled with RC-162 |
| PH-2026-05-27-007 | stack consolidation (registry + draft-tier map) | accepted | PIC-024; `templates/workspace/experiment-registry.md`, `draft-tier-map.md` |
| PH-2026-05-27-008 | ADR promotion on PIC accept (Option A) | accepted | PIC-025; batch promote 26 ADRs + `scripts/promote-platform-adr.py` |

## Chain profiles wave (CEO-directed 2026-06-09)

User request: multiple agent chains per project type (technical doc initiative, meeting synthesis, knowledge hub) and specialist stages (Technical Writer, Architect Reviewer, QA). **Out of scope:** email/Teams auto-responders (RC-153, RC-159, RC-108 rejected); autonomous platform optimizer (RC-085 rejected).

| ID | Title | Status | Depends on | Deliverable |
|---|---|---|---|---|
| PH-2026-06-09-001 | Chain profile schema | accepted | PH-001 ✓, RC-130 ✓ | PIC-026; promoted ADR |
| PH-2026-06-09-002 | Default `technical-doc-initiative` profile | accepted | PH-2026-06-09-001 ✓ | PIC-027; promoted ADR |
| PH-2026-06-09-003 | Technical Writer stage | accepted | PH-2026-06-09-001 ✓, RC-117 ✓ | PIC-028; promoted ADR |
| PH-2026-06-09-004 | Architect Reviewer stage | accepted | PH-2026-06-09-001 ✓, PH-004 ✓ | PIC-029; promoted ADR |
| PH-2026-06-09-005 | QA pre-publish stage | queued | PH-2026-06-09-001 | `workspace-qa-agent` (align-cite + align-closure + lint report) |
| PH-2026-06-09-006 | `meeting-synthesis` profile | workspace_triggered | PH-2026-06-09-001, RC-140 | Meeting capture → synthesis → publish path; trigger: first meeting ingest |
| PH-2026-06-09-007 | `knowledge-hub` profile | workspace_triggered | PH-2026-06-09-001, RC-148 ✓ | Hub scope → compile gates → structure; trigger: first hub project |

**Implementation order:** 001 → 002 → 003/004/005 (may parallelize) → 006/007 on trigger → RC-136 unpark optional.

**Bundled transcript items (same wave, lower rank):** RC-2026-06-09-012 (retriever heuristic), RC-2026-06-09-013 (three-pass orientation map).

**Related hypotheses:** H-2026-05-27-015 (RC-136), H-2026-05-27-018 (RC-140), H-2026-06-09-005 (chain profiles).

## Deferred (not in active queue)

| Claim ID | Decision | Status | Re-enter when |
|---|---|---|---|
| RC-2026-05-27-005 | defer | deferred | v2/multi-user scope is approved |
| RC-2026-05-27-011 | defer | deferred | v1 pilot usage exists |
| RC-2026-05-27-007 | experiment | deferred | Obsidian graph is sufficient for now |
| RC-2026-05-27-008 | experiment | deferred | Depends on RC-007 |

## Current cycle

```yaml
cycle_id: PIC-2026-06-09-029
selected_claim: PH-2026-06-09-004
status: accepted
accepted: 2026-06-09
blocked_by: none
next_action: "Select PH-2026-06-09-005 for next PIC (QA pre-publish stage)"
```

## Previous cycle

```yaml
cycle_id: PIC-2026-06-09-028
selected_claim: PH-2026-06-09-003
status: accepted
accepted: 2026-06-09
outcome: "Technical Writer stage; promoted PH-2026-06-09-003-technical-writer-stage.md"
```

## Previous cycle

```yaml
cycle_id: PIC-2026-06-09-026
selected_claim: PH-2026-06-09-001
status: accepted
accepted: 2026-06-09
outcome: "chain_profile schema; templates/workspace/chain-profiles/; start-project picker; promoted PH-2026-06-09-001-chain-profile-schema.md"
```

## Previous cycles (closed)

```yaml
cycle_id: PIC-2026-05-27-024
selected_claim: PH-2026-05-27-007
status: accepted
accepted: 2026-05-28
outcome: "experiment-registry.md + draft-tier-map.md; AGENTS agent-chain pointer refactor; routing-map + start-project + pointer-resources; lint check agents_agent_chain_budget."
```

```yaml
cycle_id: PIC-2026-05-27-023
selected_claim: RC-2026-05-27-148
status: accepted
accepted: 2026-05-28
outcome: "topic-entity-compile template; compile prompt phases; connection/concept lint (check 23); manifest + AGENTS updates."
```

```yaml
cycle_id: PIC-2026-05-27-022
selected_claim: RC-2026-05-27-165
status: accepted
accepted: 2026-05-28
outcome: "pointer-resources/ convention; shim trim (copilot 78→63 lines); retrieval contract mandatory/optional read; lint check 22 shim line budget."
```

```yaml
cycle_id: PIC-2026-05-27-021
selected_claim: RC-2026-05-27-117
bundled_claims:
  - RC-2026-05-27-146
status: accepted
accepted: 2026-05-28
outcome: "Thinking-partner prompt+template; stage hooks; thinking-notes lint. Raw inbox staging; compile approval gate; orphan_sources advisory."
```

```yaml
cycle_id: PIC-2026-05-27-020
selected_claim: RC-2026-05-27-162
bundled_claims:
  - PH-2026-05-27-006
status: accepted
accepted: 2026-05-28
outcome: "Routing map in AGENTS + shims; templates/workspace/routing-map.md; PH-006 platform escalation row."
```

```yaml
cycle_id: PIC-2026-05-27-019
selected_claim: RC-2026-05-27-164
status: accepted
accepted: 2026-05-28
outcome: "session-audit skill; workspace-session-audit prompt; stage agent + finalize hooks; proposal-only writes."
```

```yaml
cycle_id: PIC-2026-05-27-018
selected_claim: RC-2026-05-27-167
status: accepted
accepted: 2026-05-28
outcome: "subprojects/{workstream}/ Tier-3 stack; publish_scope exclude; align-closure + finalize + lint."
```

```yaml
cycle_id: PIC-2026-05-27-017
selected_claim: RC-2026-05-27-116
status: accepted
accepted: 2026-05-27
outcome: "agent_mode thinking|artifact; meta.yml default; stage agent guards; finalize mode gate; lint check 18."
```

```yaml
cycle_id: PIC-2026-05-27-016
selected_claim: RC-2026-05-27-163
status: accepted
accepted: 2026-05-27
outcome: "orientation.md template; RC-163 read/write hooks; finalize exclusion; lint orientation integrity."
```

```yaml
cycle_id: PIC-2026-05-27-015
selected_claim: PH-2026-05-27-004
status: accepted
accepted: 2026-05-27
outcome: "Advisory align-cite --advisory mode; pre-gate offer in start-project; stage agent hooks; handoff advisory cite section."
```

```yaml
cycle_id: PIC-2026-05-27-014
selected_claim: PH-2026-05-27-005
status: accepted
accepted: 2026-05-27
outcome: "Reopen protocol; meta.yml invalidated_stages/reopen_reason; artifact invalidation flags; CEO reopen gate; finalize exclusions."
```

```yaml
cycle_id: PIC-2026-05-27-013
selected_claim: PH-2026-05-27-003
status: accepted
accepted: 2026-05-27
outcome: "Inter-stage contract; handoff locked/forwarded sections; start-project gate forwarding; agent read/honor hooks."
```

```yaml
cycle_id: PIC-2026-05-27-012
selected_claim: PH-2026-05-27-001
status: accepted
accepted: 2026-05-27
outcome: "meta.yml current_stage/stage_gate/last_completed; transition table; resumability-first; stage agent hooks."
```

```yaml
cycle_id: PIC-2026-05-27-011
selected_claim: RC-2026-05-27-130
status: accepted
accepted: 2026-05-27
outcome: "Per-stage research/chats/daily-progress scaffold; agent hooks; finalize/publish exclusions."
```

```yaml
cycle_id: PIC-2026-05-27-010
selected_claim: RC-2026-05-27-058
status: accepted
accepted: 2026-05-27
outcome: "Per-stage handoff.md template; agent read/write hooks; start-project resumability; finalize exclusions."
```

```yaml
cycle_id: PIC-2026-05-27-009
selected_claim: RC-2026-05-27-161
status: accepted
accepted: 2026-05-27
outcome: "Three-tier instruction stack in AGENTS.md; inheritance headers on 24 prompts; IDE shims; setup-kit; lint check 16."
```

```yaml
cycle_id: PIC-2026-05-27-008
selected_claim: RC-2026-05-27-018
status: accepted
accepted: 2026-05-27
outcome: "Retrieval contract checklist; compile/query/start-project/engineer prompt gates; AGENTS.md compile note."
```

```yaml
cycle_id: PIC-2026-05-27-007
selected_claim: RC-2026-05-27-122
bundled_claims:
  - RC-2026-05-27-157
status: accepted
accepted: 2026-05-27
outcome: "Read-before-write in agent shims and workspace prompts; citation-grounded query with Sources consulted block."
```

```yaml
cycle_id: PIC-2026-05-27-006
selected_claim: RC-2026-05-27-007
status: deferred_by_user
deferred: 2026-05-27
outcome: "User prefers Obsidian graph only; RC-008 deferred with RC-007."
```

```yaml
cycle_id: PIC-2026-05-27-005
selected_claim: RC-2026-05-27-003
status: accepted
accepted: 2026-05-27
outcome: "Controlled platform gap-review workflow adopted; H-001 experiment active."
```

```yaml
cycle_id: PIC-2026-05-27-004
selected_claim: RC-2026-05-27-015
status: accepted
accepted: 2026-05-27
outcome: "Lightweight intent/safety ADR template adopted."
```

```yaml
cycle_id: PIC-2026-05-27-003
selected_claim: RC-2026-05-27-001
bundled_claims:
  - RC-2026-05-27-002
status: accepted
accepted: 2026-05-27
outcome: "Page-index retrieval default and citation≠similarity policy adopted."
```

```yaml
cycle_id: PIC-2026-05-27-002
selected_claim: RC-2026-05-27-010
status: accepted
accepted: 2026-05-27
outcome: "Trust-loop pattern adopted."
```

```yaml
cycle_id: PIC-2026-05-27-001
selected_claim: RC-2026-05-27-014
status: accepted
accepted: 2026-05-27
outcome: "Platform research artifact package and implementation priority loop adopted."
```

## Recursive loop

1. Select top `queued` item with satisfied dependencies.
2. Confirm draft ADR approval with the user.
3. Implement the smallest reversible change set.
4. Run validation commands.
5. Present diff, test results, and rollback steps to the user.
6. On **accept**: mark `accepted`; update ADR Status + Approval; **`platform-implement-backlog` agent** runs `python scripts/promote-platform-adr.py --root . --claim-id {id} --pic-cycle {cycle}` (PH-008); update decision history; re-score queue.
7. On **reject**: rollback, mark `rolled_back`, capture reason, re-score queue.
8. Repeat.

Process ADR: `docs/platform-decision-records/RC-implementation-priority-loop.md`

## Decision history

| Date | Claim ID | Action | Notes |
|---|---|---|---|
| 2026-06-09 | PH-2026-06-09-004 | accepted | PIC-029; Architect Reviewer stage; promoted PH-2026-06-09-004-architect-reviewer-stage.md |
| 2026-05-28 | PH-2026-05-27-008 | accepted | PIC-025; Option A ADR promotion; 26 files renamed; 119 ref updates |
| 2026-05-28 | RC-021, RC-118, RC-119 | rejected | Parked rescore superseded; synced to rejected-ideas.md |
| 2026-05-28 | — | parked_rescored | 28 parked RCs individually scored; report parked-rescore-2026-05-28.md |
| 2026-05-28 | PH-2026-05-27-007 | accepted | PIC-024; stack consolidation |
| 2026-05-28 | — | backlog_rescored | Full rescore: validation-first policy; PH-007 next; RC-050/055/149 → workspace_triggered |
| 2026-05-28 | RC-2026-05-27-148 | accepted | PIC-023; topic/entity compile from raw |
| 2026-05-28 | RC-2026-05-27-165 | accepted | PIC-022; lean root pointer resources |
| 2026-05-28 | RC-2026-05-27-117, RC-146 | accepted | PIC-021; thinking-partner + raw inbox staging |
| 2026-05-28 | RC-2026-05-27-162, PH-006 | accepted | PIC-020; routing map + platform escalation |
| 2026-05-28 | RC-2026-05-27-164 | accepted | PIC-019; session audit skill |
| 2026-05-28 | RC-2026-05-27-167 | accepted | PIC-018; project sub-scaffold rule stacking |
| 2026-05-28 | — | backlog_resynced | PH-003/PH-005 queue drift fixed; RC-163/116 dep checkmarks; next-selectable table added |
| 2026-05-27 | RC-2026-05-27-116 | accepted | PIC-017; thinking vs artifact mode |
| 2026-05-27 | RC-2026-05-27-163 | accepted | PIC-016; disposable session orientation |
| 2026-05-27 | PH-2026-05-27-004 | accepted | PIC-015 closed; advisory align-cite per stage |
| 2026-05-27 | PH-2026-05-27-004 | implemented | PIC-015; advisory align-cite per stage |
| 2026-05-27 | PH-2026-05-27-001 | accepted | PIC-012 closed; meta.yml stage state machine |
| 2026-05-27 | PH-2026-05-27-001 | implemented | PIC-012; project-meta.yml template + prompt transitions |
| 2026-05-27 | PH-2026-05-27-002 | accepted | Finalize alignment closed with PIC-011 |
| 2026-05-27 | RC-2026-05-27-130 | accepted | PIC-011 closed; project stage scaffold |
| 2026-05-27 | — | backlog_rescored | Stack-aware tiers; RC-157 merged with RC-122; RC-018/058 promoted; verified_no_change for RC-111/147/160 |
| 2026-05-27 | — | hygiene_queue_added | PH-001–006 from agent-chain review; report at reports/platform-research-review/agent-chain-hygiene-2026-05-27.md |
| 2026-05-27 | RC-2026-05-27-130 | implemented | PIC-011; stage scaffold templates, agent hooks, finalize/publish exclusions |
| 2026-05-27 | RC-2026-05-27-058 | accepted | PIC-010 closed; project session handoff (experiment adopted) |
| 2026-05-27 | RC-2026-05-27-058 | implemented | PIC-010; handoff template, agent prompts, start-project resumability, finalize exclusions |
| 2026-05-27 | RC-2026-05-27-161 | accepted | PIC-009 closed; hierarchical instruction stacking |
| 2026-05-27 | RC-2026-05-27-161 | implemented | PIC-009; instruction stack in AGENTS.md, 24 prompts, shims, setup-kit, lint check 16 |
| 2026-05-27 | RC-2026-05-27-018 | accepted | PIC-008 closed; retrieval contract first |
| 2026-05-27 | RC-2026-05-27-018 | implemented | PIC-008; retrieval contract checklist + compile/query/start-project/engineer prompts + AGENTS.md |
| 2026-05-27 | RC-2026-05-27-122, RC-157 | accepted | PIC-007 closed; read-before-write + citation-grounded query |
| 2026-05-27 | RC-2026-05-27-122, RC-157 | implemented | Bundled policy cycle PIC-007 |
| 2026-05-27 | RC-2026-05-27-007 | deferred_by_user | Obsidian graph preferred |
| 2026-05-27 | RC-2026-05-27-003 | accepted | Gap-review workflow |
| 2026-05-27 | RC-2026-05-27-015 | accepted | Intent/safety ADR template |
| 2026-05-27 | RC-2026-05-27-001, RC-002 | accepted | Page-index retrieval policy |
| 2026-05-27 | RC-2026-05-27-010 | accepted | Trust-loop pattern |
| 2026-05-27 | RC-2026-05-27-014 | accepted | Platform research artifacts |

## See also

- Claim register: `wiki/platform-research/claim-register.md`
- Rescore report: `reports/platform-research-review/backlog-rescore-2026-05-28.md`
- Parked rescore: `reports/platform-research-review/parked-rescore-2026-05-28.md`
- Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`
- Template: `templates/platform-research/implementation-backlog.md`
