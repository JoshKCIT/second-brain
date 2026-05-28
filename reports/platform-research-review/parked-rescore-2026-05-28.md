# Parked Claims Rescore — 2026-05-28

## Executive Judgment

The initial rescore (2026-05-28) bucketed **28 parked RCs** into five coarse groups. This pass **scores each claim individually** against the governance band (`product-brief.md` §1.2), post-PH-007 stack state, and the implementation priority formula. Result: **6 permanent park**, **8 monitor**, **3 doc reinforcement**, **6 unpark-on-trigger**, **3 workspace-triggered** (merge with Phase C), **2 reject/supersede to verified**, plus **4 deferred** rescored separately.

No parked claim outranks Phase C workspace-triggered items (RC-149 score 16) unless a specific trigger fires. Highest parked **unpark candidate** is **RC-032** (expert validation, score 10) and **RC-079** (decision log snippets, score 9).

## Source

- Inputs: `wiki/platform-research/claim-register.md`, `wiki/platform-research/implementation-backlog.md`, `reports/platform-research-review/backlog-rescore-2026-05-28.md`, `product-brief.md` §1.2
- Date: 2026-05-28
- Context: PH-007 accepted (PIC-024); validation-first policy active

## Claim Summary

| Disposition | Count | Score range | Meaning |
|---|---|---:|---|
| `permanent_park` | 11 | 0–4 | Superseded, duplicate, or generic-band; no PIC unless scope changes |
| `monitor` | 8 | 4–6 | Watch for pilot pain; no queue slot |
| `doc_reinforcement` | 3 | 6–9 | Fold into existing prompts; no standalone PIC |
| `unpark_watch` | 6 | 7–9 | Re-enter queue when trigger fires |
| `workspace_triggered` | 3 | 6–8 | Same triggers as Phase C; merge with existing rows |
| `reject_candidate` | 0 | — | Synced 2026-05-28 (RC-021, RC-118, RC-119) |
| `deferred` (unchanged) | 4 | 1–3 | RC-005/007/008/011 — out of v1 band |

## Scoring method

Same formula as active queue; `validation_debt_penalty = 1` applied to all unpark candidates.

```text
priority_score =
  (stack_lift * 3) + (platform_lift * 2) + (validation_clarity * 2)
  + (implementability * 2) + (evidence_strength * 1)
  - (canonical_risk * 2) - (experiment_uncertainty * 1)
  - (validation_debt_penalty * 2)
```

Parked claims use **governance-weighted** dimension estimates (0–5), not raw transcript `total_score`.

## Per-claim rescore (parked)

| ID | Decision | Transcript score | Rescore | Disposition | Unpark trigger / notes |
|---|---|---:|---:|---|---|
| RC-021 | reject | 6 | **2** | rejected | RC-148 topic/entity compile (2026-05-28) |
| RC-118 | reject | 10 | **2** | rejected | RC-130 daily-progress (2026-05-28) |
| RC-119 | reject | 10 | **2** | rejected | RC-130 research + handoff (2026-05-28) |
| RC-120 | experiment | 3 | **3** | permanent_park | RC-018 retrieval contract; repo-root start unnecessary |
| RC-121 | experiment | 6 | **5** | monitor | User regularly imports external chat transcripts |
| RC-166 | experiment | 9 | **4** | workspace_triggered | Bundle with RC-055 persona project; pointer not pack |
| RC-135 | experiment | 7 | **3** | permanent_park | RC-162 routing + PH-007 registry; agent hub redundant |
| RC-136 | experiment | 7 | **2** | permanent_park | Stage agent chain + routing map sufficient |
| RC-083 | experiment | 5 | **2** | permanent_park | RC-162 + RC-165 pointers supersede nested ROUTING |
| RC-138 | experiment | 6 | **6** | doc_reinforcement | Fold path/schema note into routing-map cross-links |
| RC-019 | experiment | 11 | **9** | unpark_watch | Biweekly `workspace-lint` cadence pain at publish |
| RC-037 | experiment | 12 | **8** | unpark_watch | Merge with RC-019; monthly health report template |
| RC-142 | experiment | 7 | **7** | unpark_watch | CEO requests disposable orientation pulse from log+lint |
| RC-029 | experiment | 9 | **8** | workspace_triggered | First ingest batch; materials vs notes frontmatter |
| RC-030 | experiment | 8 | **7** | unpark_watch | Multi-project capture metadata needed |
| RC-042 | experiment | 7 | **2** | permanent_park | Generic prose/style band; not governance |
| RC-070 | experiment | 6 | **5** | monitor | v1.x CI align+lint; after pilot automation request |
| RC-107 | experiment | 6 | **9** | doc_reinforcement | Fold governed tool-assembly into `second-brain` onboarding |
| RC-112 | experiment | 7 | **3** | permanent_park | Edge deploy out of v1 scope |
| RC-141 | experiment | 5 | **6** | monitor | Scoped query misses; config tag vocabulary pilot |
| RC-020 | experiment | 8 | **6** | monitor | Incremental recompile on raw drop; overlaps RC-146 |
| RC-024 | experiment | 8 | **4** | permanent_park | Stage agents + thinking-partner cover scoped subtasks |
| RC-031 | experiment | 8 | **3** | permanent_park | orientation + thinking-notes cover disposable maps |
| RC-036 | experiment | 7 | **6** | monitor | `query --file-back` insufficient for outputs loop |
| RC-038 | experiment | 8 | **8** | unpark_watch | Merge RC-102 family; after first ingest pilot |
| RC-067 | experiment | 7 | **5** | monitor | RC-018 + routing-map; path hints if compile mis-scopes |
| RC-079 | experiment | 8 | **9** | unpark_watch | First publish/align event; decision snippets in log |
| RC-032 | adopt | 12 | **10** | unpark_watch | Domain research compile; expert validation gate |

## Deferred rescore (related, not parked)

| ID | Decision | Transcript score | Rescore | Disposition | Re-enter when |
|---|---|---:|---:|---|---|
| RC-005 | defer | 2 | **1** | deferred | v2 multi-user scope approved |
| RC-007 | experiment | 5 | **1** | deferred | CEO unparks graph branch (Obsidian insufficient) |
| RC-008 | experiment | 2 | **1** | deferred | RC-007 accepted |
| RC-011 | defer | 1 | **3** | monitor | v1 pilot usage; local digest from `wiki/log.md` only |

## Highest-Value Claims

| ID | Rescore | Why unpark matters |
|---|---:|---|
| RC-032 | 10 | Governance: expert validation before domain research → compile |
| RC-079 | 9 | Audit trail at publish; aligns with trust-loop |
| RC-019 | 9 | Scheduled lint catches closure drift before publish |
| RC-107 | 9 | Doc fold only; onboarding tool-assembly clarity |

## Highest-Risk Claims

| ID | Risk if unparked prematurely |
|---|---|
| RC-135/136 | Rebuilds agent hub/registry duplicate; context bloat returns |
| RC-021 | Redundant wikilink pass weakens RC-148 Sources discipline |
| RC-042 | Style rules dilute governance-band focus |
| RC-070 | CI automation before pilot invites unsupervised wiki writes |

## Recommended Next Actions

1. ~~**Reject candidates:** RC-021, RC-118, RC-119 → sync to `rejected-ideas.md` on next register maintenance (superseded by RC-148 / RC-130).~~ **Done 2026-05-28.**
2. **Doc reinforcement (no PIC):** RC-107 → onboarding; RC-138 → routing-map cross-link; bundle RC-107 with RC-113 fold.
3. **Do not unpark** duplicate/superseded cluster (RC-083, RC-135, RC-136, RC-024, RC-031) without new evidence.
4. **Watch list:** RC-121, RC-141, RC-067, RC-020, RC-036, RC-070 — promote to unpark_watch when pilot logs pain.
5. **Trigger-linked unpark:** RC-029/038 with ingest; RC-079 with first publish; RC-019/037 with lint cadence pain; RC-032 when domain research compile requested.

## Unpark priority (if triggers fire)

Rank among parked/unpark_watch only — still below Phase C unless CEO explicit unpark:

| Rank | ID | Rescore | Trigger |
|---:|---|---:|---|
| 1 | RC-032 | 10 | Domain research compile with expert gate |
| 2 | RC-079 | 9 | First successful publish/align cycle |
| 3 | RC-019 | 9 | Scheduled lint cadence requested |
| 4 | RC-107 | 9 | Doc fold (immediate, no PIC) |
| 5 | RC-029 | 8 | First ingest batch |
| 6 | RC-038 | 8 | Ingest + orphan/processed noise |
| 7 | RC-037 | 8 | Monthly health report (bundle RC-019) |
| 8 | RC-030 | 7 | Multi-project capture metadata |
| 9 | RC-142 | 7 | CEO orientation pulse request |

## Protected Files Not Modified

This rescore updates backlog parked tables and this report only.

## See Also

- Active queue rescore: `reports/platform-research-review/backlog-rescore-2026-05-28.md`
- Backlog: `wiki/platform-research/implementation-backlog.md`
- Claim register: `wiki/platform-research/claim-register.md`
