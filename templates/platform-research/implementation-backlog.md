# Platform Implementation Backlog

One-change-at-a-time queue for approved platform claims. **Stack-aware:** use `stack_lift` and hard/soft dependencies; bundle policy-tier claims in one cycle when they ship together (see RC-001+002, RC-122+157).

## Active policy

| Rule | Value |
|---|---|
| Selection method | Highest `priority_score` among `queued` items with satisfied dependencies |
| One item per cycle | Yes (bundled claims count as one cycle when policy-tier) |
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

## Stack tiers (planning)

| Tier | Role | Examples |
|---|---|---|
| 0 — Accepted foundation | Unblocks all later work | RC-014, RC-010, RC-001, RC-002, RC-015, RC-003 |
| 1 — Policy bundle | Query/retrieval discipline | RC-122 + RC-157 (one cycle) |
| 2 — Compile scaffolding | Agent orientation contracts | RC-018, RC-161 |
| 3 — Session ergonomics | Multi-day project resume | RC-058 → RC-130 |
| 4 — Experiments | After tiers 1–3 satisfied | RC-163→164, RC-116→117, RC-162, RC-165, RC-167 |
| 5 — Compile lane | Raw inbox pilots | RC-146 → RC-148 → RC-149 |
| — verified_no_change | Already in design; no cycle | RC-004, RC-006, RC-147, RC-160, RC-111 |
| — doc reinforcement | Fold into other ADRs, not standalone | RC-105+115 |
| — blocked / deferred | Wait on data or user | RC-012, RC-007, RC-008 |

Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`

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
| 8 | RC-2026-05-27-122 + RC-157 | adopt | 28 | in_progress | RC-001 ✓, RC-002 ✓ | RC-122 + RC-157 ADRs (bundled policy cycle) |
| 9 | RC-2026-05-27-018 | adopt | 27 | queued | RC-001 ✓ | `docs/platform-decision-records/DRAFT-RC-2026-05-27-018-retrieval-contract-first.md` |
| 10 | RC-2026-05-27-161 | adopt | 24 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-161-hierarchical-instruction-stacking.md` |
| 11 | RC-2026-05-27-058 | experiment | 23 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-058-project-session-handoff.md` |
| 12 | RC-2026-05-27-130 | experiment | 22 | queued | RC-058 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-130-project-stage-scaffold.md` |
| 13 | RC-2026-05-27-163 | experiment | 21 | queued | RC-058 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-163-disposable-session-orientation.md` |
| 14 | RC-2026-05-27-167 | experiment | 20 | queued | RC-058, RC-130 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-167-project-subfolder-rule-stacking.md` |
| 15 | RC-2026-05-27-164 | experiment | 19 | queued | RC-163 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-164-session-audit-skill.md` |
| 16 | RC-2026-05-27-162 | experiment | 18 | queued | RC-018, RC-161 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-162-routing-map-agents-shim.md` |
| 17 | RC-2026-05-27-165 | experiment | 17 | queued | RC-018, RC-161 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-165-lean-root-pointer-resources.md` |
| 18 | RC-2026-05-27-116 | experiment | 20 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-116-thinking-artifact-mode-separation.md` |
| 19 | RC-2026-05-27-117 | experiment | 18 | queued | RC-116 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-117-thinking-partner-subagent.md` |
| 20 | RC-2026-05-27-146 | experiment | 18 | queued | — | `docs/platform-decision-records/DRAFT-RC-2026-05-27-146-raw-inbox-staging.md` |
| 21 | RC-2026-05-27-148 | experiment | 16 | queued | RC-146 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-148-topic-entity-compile.md` |
| 22 | RC-2026-05-27-149 | experiment | 14 | queued | RC-146 | — |
| 23 | RC-2026-05-27-050 | experiment | 15 | queued | RC-122 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-050-verbatim-cite-excerpts.md` |
| 24 | RC-2026-05-27-055 | experiment | 15 | queued | RC-122 | `docs/platform-decision-records/DRAFT-RC-2026-05-27-055-identity-packs-compile.md` |

Status values: `queued`, `blocked`, `in_progress`, `user_review`, `accepted`, `rolled_back`, `verified_no_change`, `deferred`.

## Verified baseline (no backlog work)

| Claim ID | Decision | Status | Notes |
|---|---|---|---|
| RC-2026-05-27-004 | adopt | verified_no_change | Filesystem-first substrate |
| RC-2026-05-27-006 | adopt | verified_no_change | Durable stage artifacts |
| RC-2026-05-27-111 | adopt | verified_no_change | Hybrid LLM + deterministic checks (align-*, lint) |
| RC-2026-05-27-147 | adopt | verified_no_change | AGENTS.md ingest routing |
| RC-2026-05-27-160 | adopt | verified_no_change | Karpathy compiler model in AGENTS.md |

## Doc reinforcement (bundle into other cycles, not standalone)

| Claim ID | Fold into |
|---|---|
| RC-2026-05-27-105, RC-115 | Finalize/publish prompts (understanding/accountability checkpoints) |
| RC-2026-05-27-113 | Onboarding / second-brain prompt (tools-over-models framing) |

## Deferred (not in active queue)

| Claim ID | Decision | Status | Re-enter when |
|---|---|---|---|
| RC-2026-05-27-005 | defer | deferred | v2/multi-user scope approved |
| RC-2026-05-27-011 | defer | deferred | v1 pilot usage exists |
| RC-2026-05-27-007 | experiment | deferred | Obsidian graph insufficient |
| RC-2026-05-27-008 | experiment | deferred | With RC-007 if needed |

## Current cycle

```yaml
cycle_id: PIC-YYYY-MM-DD-NNN
selected_claim: RC-2026-05-27-122
bundled_claims:
  - RC-2026-05-27-157
status: in_progress | user_review | accepted | rolled_back
blocked_by: none
validation_commands:
  - python -m unittest discover -s tests
  - python scripts/lint-platform-research.py --root .
rollback_plan: "Revert prompt/shim/AGENTS.md edits from this cycle; restore prior workspace-query response shape."
next_action: ""
```

## Decision history

| Date | Claim ID | Action | Notes |
|---|---|---|---|
|  |  |  |  |

## See also

- Claim register: `wiki/platform-research/claim-register.md`
- Stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`
- Process ADR: `docs/platform-decision-records/DRAFT-RC-implementation-priority-loop.md`
