# Research Impact Report: Pinecone Just Demoted Vector Search — Here's the Knowledge Layer

## Executive Judgment

This transcript contains **strong product-improving material** for Second Brain's compiler architecture. It is not a call to adopt Pinecone or multi-database stacks; it validates structure-aware retrieval, governed bundles, and contract-first design while warning against context-maximization and unvalidated session memory. Vendor consolidation claims are useful market signal only.

## Source

- Transcript: `raw/platform-transcripts/Pinecone_Just_Demoted_Vector_Search._Here_s_the_Knowledge_Layer.txt`
- Date: unknown
- Participants: unknown (infrastructure analyst / builder)
- Processing limitations: benchmark and spend figures unvalidated; Substack references not ingested.

## Claim Summary

| Decision | Count |
|---|---:|
| Adopt | 3 |
| Experiment | 2 |
| Defer | 0 |
| Reject | 0 |
| Monitor | 1 |

## Highest-Value Claims

| Claim ID | Decision | Rationale |
|---|---|---|
| RC-2026-05-27-018 | adopt | Contract-first design (what the agent receives, in what shape, from which authority) matches governance-and-closure and prevents database-first scope creep. |
| RC-2026-05-27-016 | adopt | Reinforces RC-001: retrieval unit must match work—sections for long docs, not similarity chunks alone. |
| RC-2026-05-27-019 | adopt | "Appropriate context" not "maximum context" supports inline rules at publish and index-guided compile. |

## Highest-Risk Claims

| Claim ID | Decision | Risk |
|---|---|---|
| RC-2026-05-27-020 | experiment | Treating prior agent summaries as confirmed memory without human validation could bypass align-cite and erode grounding. |
| RC-2026-05-27-021 | monitor | Adopting Pinecone/Page Index benchmark claims without validation would violate vendor-truth discipline. |

## Claim Register Entries

- `RC-2026-05-27-016` through `RC-2026-05-27-021` — see `wiki/platform-research/claim-register.md`

## Recommended Next Actions

### Immediate changes

- None to canonical docs in this pass.

### Experiments

- RC-017: Pair bundle checklist with RC-009 orientation map; measure compile citation precision.
- RC-020: Document fail-closed rule for session orientation artifacts (disposable, not canonical).

### ADRs to draft

- `docs/platform-decision-records/RC-2026-05-27-018-retrieval-contract-first.md`

### Claims to reject

- None.

### Claims requiring external validation

- RC-021: Pinecone 85% rediscovery stat, Page Index 98.7% Finance Bench, SAP €1B+ figures, Chroma context-rot paper.

## Trust Loop Summary

Vendor and benchmark claims marked `unvalidated`. No `adopt` decisions on unvalidated market claims. RC-020 flagged for explicit human validation before any session-memory write path.

## Correction Routes

| Claim ID | Decision | Correction route |
|---|---|---|
| RC-016, RC-018, RC-019 | adopt | Approve draft ADR via implementation backlog; reject via backlog rollback. |
| RC-017, RC-020 | experiment | Track in `open-hypotheses.md`; approve experiment ADR before implementation. |
| RC-021 | monitor | Re-score when primary vendor docs or benchmarks are cached under `raw/workspace-external/`. |

## Protected Files Not Modified

Confirmed: no canonical standards, PRD, product brief, roadmap, architecture rationale, AGENTS.md, or raw files were modified based on this transcript.
