# Platform Research Batch Synthesis — Re-review (closure–compile) — 2026-05-27

## Executive Judgment

Re-review under `docs/platform-intelligence/closure-compile-review-brief.md` confirms the batch supports **governance-and-closure** positioning. The main correction: **RC-2026-05-27-009** is no longer a blanket v1 reject—it splits into an **experiment** (authoring-time cross-source orientation for publishable sets) and **009a reject** (full IDE-style code graph indexing). Graph/token/RAG themes are **compile-for-publish** mechanics, not generic product scope.

## Source

- Brief: `docs/platform-intelligence/closure-compile-review-brief.md`
- Re-review date: 2026-05-27
- Wave 2: thirteen transcripts reviewed under closure–compile lens (parallel research-review runs)

## Claim Summary

| Decision | Approx. wave-2 count |
|----------|---------------------:|
| Adopt | 15+ |
| Experiment | 25+ |
| Defer | 2+ |
| Reject | 15+ |
| Monitor | 5+ |

Exact totals: reconcile `wiki/platform-research/claim-register.md` (IDs RC-016–042, RC-066–081; parallel runs used overlapping ranges—see note below).

## Highest-Value Claims

| Theme | Examples |
|-------|----------|
| Compile → publish closure | RC-054 (raw→wiki compiler), RC-018 (retrieval contract-first), RC-037 (wiki health lint) |
| Trust + citations | RC-010 (unchanged), RC-028, RC-032 |
| Agent layering | RC-066 (instructions/agents/skills), RC-075 (skills before autonomy) |

## Highest-Risk Claims

| Theme | Examples |
|-------|----------|
| Auto-mutation without approval | RC-030, RC-041, RC-059 |
| Passive / background indexing | RC-051 |
| IDE substrate / YOLO | RC-077, RC-073, RC-035 |

## Recommended Next Actions

- Approve draft ADRs for top adopt/experiment claims via implementation backlog (one at a time).
- Process **3 remaining queued** transcripts (see register).
- Optional: claim-register deduplication pass after parallel ID collision (016–042 vs 066–081).

## Scope

- **Re-reviewed:** eight transcripts with existing analyses (closure–compile lens appended; OpenCode+Graphify fully revised).
- **Wave 2:** thirteen new files reviewed; **3 additional** files queued after sync (user drop).

## Claim decision changes

| Claim ID | Prior | Updated |
|----------|-------|---------|
| RC-2026-05-27-009 | reject | **experiment** (safer variant) |
| RC-2026-05-27-009a | — | **reject** (as stated: v1 code graph) |

All other RC-001–015 decisions unchanged on re-review.

## Highest-value themes (unchanged + reinforced)

- Page-index retrieval + citation≠similarity (RC-001, RC-002)
- Trust loop for platform workflows (RC-010)
- Platform research artifact package (RC-014)
- Persistent Markdown + disposable orientation (RC-006, RC-007, RC-008, RC-009 experiment)

## Protected Files Not Modified

No canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw mirrors were modified in this re-review pass.
