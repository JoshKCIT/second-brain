# Platform Implementation Backlog

This queue turns reviewed claims into **one change at a time**: implement → validate → user review → accept or rollback → re-score → next item.

Priority uses **stack lift**, not raw transcript impact alone. A claim with a lower impact score but high unblocking value can rank above a stronger standalone experiment.

**Stack-aware rescoring (2026-05-27):** Policy-tier claims bundle in one cycle (RC-122+157). Foundation claims RC-018 and RC-058 precede dependent experiments. Verified-no-change and doc-reinforcement claims removed from active queue.

## Active policy

| Rule | Value |
|---|---|
| Selection method | Highest `priority_score` among `queued` items with satisfied dependencies |
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
```

## Stack tiers

| Tier | Role | Next items |
|---|---|---|
| 0 — Accepted | Foundation complete | RC-014, RC-010, RC-001/002, RC-015, RC-003 ✓ |
| 1 — Policy | Query discipline | RC-122 + RC-157 ✓ |
| 2 — Scaffolding | Retrieval + agent rules | RC-018 ✓, RC-161 ✓ |
| 3 — Session | Handoff ergonomics | RC-058 ✓, RC-130 ✓ |
| 3b — Hygiene | Agent chain gaps | PH-001 ✓, **PH-003** (next) |
| 4 — Experiments | After 1–3 | RC-163→164, RC-116→117, RC-162, RC-165, RC-167 |
| 5 — Compile lane | Raw inbox | RC-146 → RC-148 → RC-149 |

Template: `templates/platform-research/implementation-backlog.md`. Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`.

## Queue

| Rank | Claim ID | Decision | priority_score | Status | Depends on | Draft ADR |
|---:|---|---|---:|---|---|---|
| 1 | RC-2026-05-27-014 | adopt | 38 | accepted | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-014-platform-research-artifacts.md` |
| 2 | RC-2026-05-27-010 | adopt | 35 | accepted | RC-014 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-010-trust-loop-workflow-pattern.md` |
| 3 | RC-2026-05-27-001 | adopt | 31 | accepted | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-001-page-index-retrieval.md` |
| 4 | RC-2026-05-27-002 | adopt | 29 | accepted | RC-001 ✓ | (bundle with RC-001) |
| 5 | RC-2026-05-27-015 | experiment | 24 | accepted | RC-014 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-015-lightweight-intent-records.md` |
| 6 | RC-2026-05-27-003 | experiment | 22 | accepted | RC-010 ✓, RC-014 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-003-controlled-gap-research.md` |
| 7 | RC-2026-05-27-012 | experiment | 20 | blocked | RC-010 ✓, RC-014 ✓, failure data | `docs/platform-decision-records/DRAFT-RC-2026-05-27-012-advisory-harness-failure-review.md` |
| 8 | RC-2026-05-27-122 + RC-157 | adopt | 28 | accepted | RC-001 ✓, RC-002 ✓ | RC-122 + RC-157 (bundled) |
| 9 | RC-2026-05-27-018 | adopt | 27 | accepted | RC-001 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-018-retrieval-contract-first.md` |
| 10 | RC-2026-05-27-161 | adopt | 24 | accepted | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-161-hierarchical-instruction-stacking.md` |
| 11 | RC-2026-05-27-058 | experiment | 23 | accepted | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md` |
| 12 | RC-2026-05-27-130 | experiment | 22 | accepted | RC-058 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-130-project-stage-scaffold.md` |
| 12a | PH-2026-05-27-001 | hygiene | 26 | accepted | RC-058 ✓, RC-130 ✓ | `templates/workspace/project-meta.yml.md` |
| 12b | PH-2026-05-27-002 | hygiene | 25 | accepted | RC-161 ✓, PIC-011 | finalize delegation in start-project |
| 12c | PH-2026-05-27-003 | hygiene | 21 | queued | RC-058 ✓, RC-130 ✓ | inter-stage output contract in handoff |
| 13 | RC-2026-05-27-163 | experiment | 21 | queued | RC-058 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-163-disposable-session-orientation.md` |
| 14 | RC-2026-05-27-167 | experiment | 20 | queued | RC-058 ✓, RC-130 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-167-project-subfolder-rule-stacking.md` |
| 14a | PH-2026-05-27-004 | hygiene | 19 | queued | RC-122 ✓ | advisory align-cite per stage |
| 14b | PH-2026-05-27-005 | hygiene | 18 | queued | PH-001 ✓ | reopen stage protocol |
| 15 | RC-2026-05-27-164 | experiment | 19 | queued | RC-163 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-164-session-audit-skill.md` |
| 16 | RC-2026-05-27-162 | experiment | 18 | queued | RC-018 ✓, RC-161 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-162-routing-map-agents-shim.md` |
| 16a | PH-2026-05-27-006 | hygiene | 16 | queued | RC-162 | platform escalation row in routing map |
| 17 | RC-2026-05-27-165 | experiment | 17 | queued | RC-018 ✓, RC-161 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-165-lean-root-pointer-resources.md` |
| 18 | RC-2026-05-27-116 | experiment | 20 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-116-thinking-artifact-mode-separation.md` |
| 19 | RC-2026-05-27-117 | experiment | 18 | queued | RC-116 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-117-thinking-partner-subagent.md` |
| 20 | RC-2026-05-27-146 | experiment | 18 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-146-raw-inbox-staging.md` |
| 21 | RC-2026-05-27-148 | experiment | 16 | queued | RC-146 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-148-topic-entity-compile.md` |
| 22 | RC-2026-05-27-149 | experiment | 14 | queued | RC-146 | — |
| 23 | RC-2026-05-27-050 | experiment | 15 | queued | RC-122 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-050-verbatim-cite-excerpts.md` |
| 24 | RC-2026-05-27-055 | experiment | 15 | queued | RC-122 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-055-identity-packs-compile.md` |

## Verified baseline (no backlog work)

| Claim ID | Decision | Status | Notes |
|---|---|---|---|
| RC-2026-05-27-004 | adopt | verified_no_change | Filesystem-first substrate already implemented |
| RC-2026-05-27-006 | adopt | verified_no_change | Durable stage artifacts already implemented |
| RC-2026-05-27-111 | adopt | verified_no_change | align-*, lint deterministic checks |
| RC-2026-05-27-147 | adopt | verified_no_change | AGENTS.md ingest routing |
| RC-2026-05-27-160 | adopt | verified_no_change | Karpathy compiler model in AGENTS.md |

## Doc reinforcement (not standalone cycles)

| Claim ID | Fold into |
|---|---|
| RC-2026-05-27-105, RC-115 | Finalize/publish prompts |
| RC-2026-05-27-113 | Onboarding prompt |

## Agent chain hygiene queue (PH-*)

From `reports/platform-research-review/agent-chain-hygiene-2026-05-27.md`. Not transcript claims; platform maintenance discovered during RC-161/058 review.

| ID | Title | Status | Notes |
|---|---|---|---|
| PH-2026-05-27-001 | meta.yml stage state machine | accepted | PIC-012; template + prompt transitions |
| PH-2026-05-27-002 | start-project finalize alignment | accepted | PIC-011 delegated finalize to engineer prompt |
| PH-2026-05-27-003 | inter-stage output contract | accepted | PIC-013; handoff locked/forwarded sections; inter-stage contract template |
| PH-2026-05-27-004 | advisory align-cite per stage | queued | optional before CEO gates |
| PH-2026-05-27-005 | reopen stage protocol | accepted | PIC-014; invalidated_stages + artifact flags; orchestrator reopen checklist |
| PH-2026-05-27-006 | platform escalation routing | queued | bundle with RC-162 |

## Deferred (not in active queue)

| Claim ID | Decision | Status | Re-enter when |
|---|---|---|---|
| RC-2026-05-27-005 | defer | deferred | v2/multi-user scope is approved |
| RC-2026-05-27-011 | defer | deferred | v1 pilot usage exists |
| RC-2026-05-27-007 | experiment | deferred | Obsidian graph is sufficient for now |
| RC-2026-05-27-008 | experiment | deferred | Depends on RC-007 |

## Current cycle

```yaml
cycle_id: —
selected_claim: —
status: idle
blocked_by: none
next_action: "PH-005 accepted (PIC-014). Next: PH-004 (advisory align-cite per stage, priority 19) or PH-006 (platform escalation routing, priority 16) or RC-116 (thinking mode, priority 20)."
```

## Previous cycles (closed)

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
6. On **accept**: mark `accepted`, update decision history, re-score queue.
7. On **reject**: rollback, mark `rolled_back`, capture reason, re-score queue.
8. Repeat.

Process ADR: `docs/platform-decision-records/DRAFT-RC-implementation-priority-loop.md`

## Decision history

| Date | Claim ID | Action | Notes |
|---|---|---|---|
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
- Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`
- Template: `templates/platform-research/implementation-backlog.md`
