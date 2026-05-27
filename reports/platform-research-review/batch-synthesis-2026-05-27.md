# Platform Research Batch Synthesis - 2026-05-27

## Executive Judgment

The batch supports Second Brain's current governance-and-closure positioning. The strongest recommendations are to preserve structure-aware retrieval, strengthen trust-loop mechanics, and formalize platform research artifacts. The main rejections are opaque recursive agents and v1 graph/codebase indexing that would dilute scope.

## Source

- Transcripts: all current files under `raw/platform-transcripts/` listed in the plan.
- Date: 2026-05-27
- Participants: multiple external speakers; names known only where stated in the transcripts.
- Processing limitations: external product, benchmark, paper, and legal claims are unvalidated unless explicitly marked otherwise.

## Scope

This synthesis covers the eight transcripts listed in the platform transcript review plan. The transcripts were treated as product-intelligence evidence only; no canonical platform docs, workspace standards, workspace recommendations, PRD, roadmap, architecture rationale, AGENTS.md, or raw source mirrors were directly modified.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 6 |
| Experiment | 5 |
| Defer | 2 |
| Reject | 2 |
| Monitor | 0 |
| Total | 15 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-001 | adopt | Preserves structure-aware retrieval as the v1 default. |
| RC-2026-05-27-010 | adopt | Adds an explicit trust-loop pattern for future workflows. |
| RC-2026-05-27-014 | adopt | Formalizes platform research as traceable claim-plus-evidence artifacts. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-009 | reject | Would push v1 into generic codebase assistant scope. |
| RC-2026-05-27-013 | reject | Opaque latent collaboration conflicts with inspectability. |
| RC-2026-05-27-005 | defer | Distributed sync would add v2-level complexity to v1. |

## Cluster Summary

| Cluster | Claims | Judgment |
|---|---|---|
| Retrieval strategy | RC-2026-05-27-001, RC-2026-05-27-002 | Adopt. The batch reinforces v1's structure-aware, inspectable, no-vector-default approach. |
| Memory and self-learning | RC-2026-05-27-003, RC-2026-05-27-004, RC-2026-05-27-006 | Adopt current filesystem memory; experiment with controlled gap review only. |
| Graph and knowledge representation | RC-2026-05-27-005, RC-2026-05-27-007, RC-2026-05-27-008, RC-2026-05-27-009 | Defer distributed sync, experiment with disposable graph reports, reject v1 mixed code/docs graph indexing. |
| Trust, UX, and workflow integrity | RC-2026-05-27-010, RC-2026-05-27-011 | Adopt trust-loop mechanisms; defer proactive digests until real pilot data exists. |
| Evaluation and harness improvement | RC-2026-05-27-012 | Experiment with advisory failure-trace reviews, not autonomous prompt mutation. |
| Agent recursion/autonomy | RC-2026-05-27-013 | Reject opaque latent/recursive agent loops as stated. |
| Platform research artifacts | RC-2026-05-27-014 | Adopt structured claim-plus-evidence artifacts. |
| Governance and regulatory readiness | RC-2026-05-27-015 | Experiment with lightweight intent/safety records in platform ADRs. |

## Already Supported Ideas

- Filesystem-first, Obsidian-readable, agent-visible Markdown storage is already core to Second Brain.
- Durable stage artifacts already address session amnesia and context loss.
- Index-guided retrieval and citation verification already address the "similarity is not support" failure mode.
- Platform transcripts are already separated from canonical workspace knowledge by the `platform-*` lane.

## Adopt

- Preserve page-index / structure-aware retrieval as the v1 default and require future retrieval additions to beat it on citation precision and inspectability.
- Treat retrieved context as candidate evidence only; keep `workspace-align-cite` as the source-support gate.
- Preserve filesystem-first durable memory as a core platform constraint.
- Adopt trust-loop language for future workflows: audit trail, confidence state, fail-closed handling, and easy correction.
- Formalize platform research outputs as claim-plus-evidence artifacts that preserve rejected ideas and failed paths.

## Experiments

- Controlled platform gap-review loop that produces source candidates and hypotheses only.
- Disposable graph projection from Markdown/wikilinks/frontmatter.
- Session-start graph summary for agent orientation.
- Advisory harness-failure review that proposes prompt/workflow changes without editing protected files.
- Lightweight intent/safety sections in draft platform ADRs.

## Defer

- Distributed sparse-sync knowledge protocol is a v2/multi-user question, not v1.
- Daily and weekly proactive digests should wait until real v1 pilot usage exists.

## Reject

- Mixed code/docs/media graph indexing as a v1 feature because it drifts into generic IDE assistant territory.
- Recursive latent-space multi-agent collaboration as a replacement for text-review loops because it is not inspectable.
- Any "self-learning" loop that directly mutates canonical docs.
- Any use of transcript vendor/product claims as verified facts without primary-source validation.

## Contradictions and Duplicates

- The Graphify/OpenCode transcripts duplicate the GitKB graph-projection theme. The safe common denominator is a disposable graph report generated from canonical Markdown, not a graph database as source truth.
- The "no vector database" transcript and graph transcripts pull in opposite directions. The resolution is to preserve v1 page-index retrieval and only experiment with graph summaries as review/orientation aids.
- The self-learning transcript conflicts with protected-file governance if interpreted literally. The safe interpretation routes all learning through platform research artifacts and draft ADRs.

## Recommended Next Actions

1. Draft ADRs for page-index retrieval, controlled platform gap review, disposable graph orientation, workflow trust loops, platform research artifacts, and advisory harness-failure review.
2. Keep all experiment candidates in `wiki/platform-research/open-hypotheses.md`.
3. Keep rejected recurring ideas in `wiki/platform-research/rejected-ideas.md`.
4. Validate all external product, legal, benchmark, and vendor claims against primary sources before any future canonical citation.

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, workspace knowledge, or raw files were modified based on transcript evidence.
