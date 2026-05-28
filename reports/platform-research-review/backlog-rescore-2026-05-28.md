# Platform Backlog Rescore — 2026-05-28

## Executive Judgment

PIC-001 through PIC-023 closed **21 RC experiments/adoptions** plus **6 PH hygiene items**. The active RC implementation lane is **sufficient for v1 pilot**. Remaining work should shift from **stack-lift** to **validation-first**: consolidate docs (PH-007), fold doc-reinforcement claims, then implement RCs only when a **workspace trigger** exists (ingest batch, review artifact, persona project).

## Source

- Inputs: `wiki/platform-research/claim-register.md`, `wiki/platform-research/implementation-backlog.md`, PIC-001–023 decision history
- Date: 2026-05-28
- Processing limitations: lift scores are planning estimates; 61 pending RCs triaged by governance band and duplicate analysis.

## Claim Summary

Scanned **61 unimplemented** adopt/experiment RCs (excluding reject/monitor/defer/already-accepted). **3** were in the old active queue (RC-050, RC-055, RC-149). **~20** adopt claims are **verified_no_change**. **~25** **parked**.

| Phase | Mode | Count | Examples |
|---|---|---:|---|
| A — Consolidation | Implement now | 1 | PH-007 |
| B — Doc reinforcement | Fold-in | 3 | RC-105, RC-115, RC-113 |
| C — Workspace-triggered | Queue on pilot | 9 | RC-149, RC-114, RC-050 |
| D — Blocked | Wait | 1 | RC-012 |
| E — Park | No queue | ~25 | RC-118–121, RC-135/136 |
| F — Verified baseline | No cycle | ~20 | RC-016, RC-090, RC-137 |

## Rescore policy (2026-05-28)

| Phase | Mode | Selection rule |
|---|---|---|
| **A — Consolidation** | Implement | PH-007 only until accepted |
| **B — Doc reinforcement** | Fold-in (no PIC) | RC-105, RC-115, RC-113 |
| **C — Workspace-triggered** | Queue RC | Implement when ingest / review / persona project exists |
| **D — Blocked** | Wait | RC-012 until failure traces |
| **E — Park** | No queue | Duplicate, generic-band, or superseded by accepted RCs |
| **F — Verified baseline** | No cycle | Adopt claims already in current design |

**New priority formula emphasis** (same math, different weights in practice):

```text
priority_score =
  (stack_lift * 3) + (platform_lift * 2) + (validation_clarity * 2)
  + (implementability * 2) + (evidence_strength * 1)
  - (canonical_risk * 2) - (experiment_uncertainty * 1)
  - (validation_debt_penalty * 2)   # NEW: penalize new RC if ≥8 accepted experiments lack pilot
```

`validation_debt_penalty = 1` for all new RC PICs until first workspace project completes one stage gate.

## Highest-Value Claims

| Claim ID | Rescored priority | Why |
|---|---:|---|
| PH-2026-05-27-007 | 22 | Consolidates experiment registry; reduces AGENTS bloat without new features |
| RC-2026-05-27-105 + RC-115 | 18 | Doc fold strengthens closure at publish — high governance, low lift |
| RC-2026-05-27-149 | 16 | Compile hygiene after first ingest; depends on RC-146 ✓ |

## Highest-Risk Claims

| Claim ID | Risk if implemented now |
|---|---|
| RC-2026-05-27-050 | Verbatim excerpts before any artifact hits `review` — no validation signal |
| RC-2026-05-27-055 | Identity packs are generic-band PKM; not governance core |
| RC-2026-05-27-135/136 | Duplicate agent-hub routing already covered by RC-162 + RC-165 |
| RC-2026-05-27-012 | Harness mutation without failure traces — advisory process untested |

## Recommended Next Actions

1. Accept and implement **PH-007** (PIC-024) — stack consolidation.
2. Fold **RC-105/115/113** into finalize/publish/onboarding prompts (no PIC unless bundled).
3. **Pause new RC PICs** until first workspace project or ingest pilot.
4. Unpark Phase C items in trigger order when pilot evidence exists.
5. Re-score quarterly; unpark parked claims only with new evidence.

## Phase detail — A (next implement)

| Rank | ID | Score | Trigger | Notes |
|---:|---|---:|---|---|
| 1 | PH-007 | 22 | None | Experiment registry + draft-tier map; AGENTS pointer refactor |

## Phase detail — B (doc reinforcement)

| ID | Fold into | Score | Notes |
|---|---|---:|---|
| RC-105, RC-115 | finalize + publish prompts | 18 | Accountability comprehension attestation |
| RC-113 | `second-brain` onboarding | 12 | Tools-over-models framing |
| RC-090, RC-091, RC-093 | Already partial | — | align-cite, CEO gates, PH-003; document in registry |

## Phase C — Workspace-triggered queue

Implement **only when trigger fires**:

| Rank | ID | Rescored score | Trigger | Depends | ADR |
|---:|---|---:|---|---|---|
| 1 | RC-149 | 16 | First Confluence/vendor ingest batch | RC-146 ✓ | Draft needed |
| 2 | RC-114 | 15 | After first ingest+compile pilot | RC-146 ✓ | Draft needed |
| 3 | RC-050 | 14 | First artifact at `review` | RC-122 ✓ | Yes |
| 4 | RC-105 | 14 | Same as doc fold (or bundle with finalize PIC) | — | Yes |
| 5 | RC-094 | 13 | First fresh-clone setup pain | RC-161 ✓ | Yes |
| 6 | RC-139 | 12 | Multi-source ingest (internal + vendor) | RC-146 ✓ | Yes |
| 7 | RC-140 | 11 | Meeting notes ingest requested | RC-146 ✓ | Yes |
| 8 | RC-055 | 10 | Client/persona voice project | RC-122 ✓ | Yes |
| 9 | RC-103 | 10 | After RC-148 compile pilot | RC-148 ✓ | — |
| 10 | RC-102 | 9 | Orphan noise after ingest pilot | RC-146 ✓ | — |

## Phase D — Blocked

| ID | Score | Blocker |
|---|---:|---|
| RC-012 | 8 | ≥3 real harness/lint/publish failure traces |

## Phase E — Park (per-claim rescore)

See `reports/platform-research-review/parked-rescore-2026-05-28.md` for full table. Top unpark candidates if triggers fire: RC-032 (10), RC-079/019/107 (9).

## Phase F — Verified baseline expansion

Move to `verified_no_change` (no PIC):

| ID | Rationale |
|---|---|
| RC-016, RC-035, RC-097 | Three-layer raw/wiki/AGENTS substrate |
| RC-017, RC-039 | Page-index / moderate corpus — RC-001 ✓ |
| RC-066, RC-068, RC-069, RC-071, RC-075, RC-078 | Skills/prompts/specialist chain — implemented |
| RC-082, RC-087, RC-089 | AGENTS navigation, filesystem-first |
| RC-090, RC-091, RC-092, RC-093 | align-cite, CEO gates, agentic engineering |
| RC-098 | User-triggered compile — RC-146 ✓ |
| RC-137 | Skills library — `.github/skills/` |
| RC-158 | Open repo/vault — operational not schema |

## Accepted experiments — validation debt

These need **pilot validation**, not new RC implementation:

RC-116, RC-117, RC-163, RC-164, RC-167, RC-146, RC-148 (+ active hypotheses H-021–H-027, H-026).

## Protected Files Not Modified

This rescore updated `wiki/platform-research/implementation-backlog.md` queue sections and this report only. No canonical workspace standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md behavior, or raw files were modified.

## See Also

- `wiki/platform-research/implementation-backlog.md`
- `wiki/platform-research/claim-register.md`
