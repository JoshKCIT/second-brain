# Final Recommendations - Platform Transcript Review - 2026-05-27

## Executive Judgment

Adopt the ideas that reinforce Second Brain's existing governance model: structure-aware retrieval, trust-loop mechanics, and traceable platform research artifacts. Run experiments only where the idea remains advisory and approval-gated. Reject ideas that make the system opaque, generic, or too autonomous.

## Source

- Transcripts: all current platform transcripts listed in the plan.
- Date: 2026-05-27
- Participants: multiple external speakers; names known only where stated in the transcripts.
- Processing limitations: external market, vendor, paper, legal, and benchmark claims are unvalidated until checked against primary sources.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 6 |
| Experiment | 5 |
| Defer | 2 |
| Reject | 2 |
| Monitor | 0 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-001 | adopt | Keeps retrieval structured and inspectable. |
| RC-2026-05-27-010 | adopt | Adds reusable trust-loop mechanics. |
| RC-2026-05-27-014 | adopt | Makes platform research traceable and reviewable. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-009 | reject | Generic codebase-assistant scope creep. |
| RC-2026-05-27-013 | reject | Opaque autonomous reasoning loop. |

## Ideas Already Implemented In Second Brain

- Local, filesystem-first Markdown knowledge base visible to coding agents.
- Durable stage artifacts to reduce context loss across sessions.
- Index-guided retrieval with embeddings deferred until scale justifies them.
- Citation verification and closure checks as production-quality gates.
- Platform/workspace lane separation so research does not become canonical workspace knowledge.

## Ideas To Adopt

- Codify page-index retrieval as the v1 retrieval default and make future retrievers pass a citation-precision and inspectability bar.
- Treat similarity, graph proximity, or model confidence as insufficient for source support unless `workspace-align-cite` verifies the claim.
- Add trust-loop language to future workflow designs: audit trail, confidence state, fail-closed handling, and easy correction.
- Formalize platform research artifacts as structured claim-plus-evidence packages with preserved negative knowledge.

## Experiments To Run

- Monthly platform gap-review loop that proposes sources and hypotheses but does not modify canonical docs.
- Disposable Markdown-derived graph report for reviewer navigation and agent orientation.
- Session-start graph summary experiment with measured read count, correctness, and elapsed time.
- Advisory harness-failure review that converts failure traces into draft ADRs, not automatic prompt changes.
- Lightweight intent/safety records in draft platform ADRs.

## Ideas To Reject

See the full historical register: `wiki/platform-research/rejected-ideas.md` (next re-review: **2026-08-27**).

- **RC-2026-05-27-009** — Adding mixed code/docs/media graph indexing to v1.
- **RC-2026-05-27-013** — Replacing text-based review loops with opaque latent-space recursive agents.
- **RP-2026-05-27-001** — Allowing self-learning automation to directly update `AGENTS.md`, PRD, roadmap, architecture rationale, workspace standards, workspace recommendations, or raw mirrors.
- **RP-2026-05-27-002** — Treating social transcript benchmark or vendor claims as verified without primary-source validation.

## Claims Needing External Validation

- Page-index benchmark accuracy claims.
- GitKB product capability and sparse-sync claims.
- Graphify token-saving and graph-quality claims.
- Stanford meta-harness paper and benchmark claims.
- Texas AI governance implications and NIST risk-management references.
- Recursive latent-agent performance claims.

## Recommended Next Actions

- Review the prioritized implementation queue: `wiki/platform-research/implementation-backlog.md`
- Read the stack analysis: `reports/platform-research-review/claim-stack-analysis-2026-05-27.md`
- Approve or revise draft ADRs before any canonical doc changes.
- Run one implementation cycle at a time using `docs/platform-decision-records/RC-implementation-priority-loop.md`.
- Keep external product, benchmark, legal, and paper claims marked unvalidated until primary-source checks are performed.

## Draft ADRs Created

- `docs/platform-decision-records/RC-2026-05-27-001-page-index-retrieval.md`
- `docs/platform-decision-records/RC-2026-05-27-003-controlled-gap-research.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-007-disposable-graph-projection.md`
- `docs/platform-decision-records/RC-2026-05-27-010-trust-loop-workflow-pattern.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-012-advisory-harness-failure-review.md`
- `docs/platform-decision-records/RC-2026-05-27-014-platform-research-artifacts.md`
- `docs/platform-decision-records/RC-2026-05-27-015-lightweight-intent-records.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-008-session-graph-orientation.md`
- `docs/platform-decision-records/RC-implementation-priority-loop.md`

## Protected Files Intentionally Not Modified

- `AGENTS.md`
- `PRD.md`
- `product-brief.md`
- `docs/roadmap.md`
- `docs/architecture-rationale.md`
- `wiki/workspace-standards/**`
- `wiki/workspace-recommendations/**`
- `raw/**`

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, workspace knowledge, or raw files were modified based on transcript evidence.
