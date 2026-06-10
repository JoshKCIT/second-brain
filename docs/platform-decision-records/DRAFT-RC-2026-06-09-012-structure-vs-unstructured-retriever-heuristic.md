# DRAFT ADR: RC-2026-06-09-012 - Structure vs Unstructured Retriever Heuristic

## Status

Draft

## Source Claim

- Claim ID: RC-2026-06-09-012
- Source transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
- Speaker: unknown
- Timestamp: 00:04:00-00:05:30
- Claim type: architecture_proposal

## Context

Graphify (transcript evidence) uses deterministic structure graphs without embeddings for wired codebases; GraphRAG-style systems use embeddings for unstructured document corpora. Second Brain already defaults to page-index retrieval (RC-001) and holdout-gates any future vector/hybrid/graph retriever. The architecture-rationale future retriever gate lacks an explicit decision table for when structure-aware vs embedding retrievers apply.

## Decision

Document a retriever-selection heuristic in platform intelligence (not PRD mutation in this draft):

- **Structure-aware (page-index, hierarchy, explicit cross-links, deterministic AST/graph reports):** wired corpora with inspectable hierarchy—compiled wiki, Confluence-derived Markdown, code repos when code-as-source is explicitly in scope.
- **Embedding GraphRAG (holdout-gated only):** large unstructured cross-document corpora where explicit structure is weak (e.g., policy PDFs across thousands of files with no stable hierarchy).

v1 default remains page-index. No embeddings adoption from this ADR alone.

## Intent

- **Intended outcome:** Give implementers and reviewers a scope filter so Graphify-style tooling is not misapplied to unstructured policy search, and embedding RAG is not misapplied where hierarchy and citations already suffice.
- **In scope:** Decision table in `docs/platform-intelligence/` or architecture-rationale addendum on PIC accept.
- **Out of scope:** Installing Graphify; enabling embeddings in v1; replacing align-cite.

## Safety and non-goals

- **Safety posture:** Fail closed—retrieved orientation is not citation support (RC-002).
- **Non-goals:** Repo-wide IDE indexing; vendor tool bundling; autonomous retriever switching without holdout evaluation.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Aligns transcript evidence with existing RC-001/002 policy. Prevents scope creep into generic IDE assistants (RC-009a rejection) while preserving a path for holdout-gated unstructured retrieval if wiki scale demands it.

## Impact Scores

governance +1, closure +1, grounding +1, inspectability +1, differentiation +1, enterprise_fit +1; total +7

## Alternatives Considered

1. **Adopt Graphify for all retrieval** — rejected (IDE scope, weak governance).
2. **Ignore transcript** — loses useful decision heuristic already implied in architecture-rationale.
3. **Enable embeddings now** — violates RC-001 holdout gate.

## Consequences

### Positive

- Clearer product boundary when evaluating Graphify, GraphRAG, and page-index proposals.
- Supports skeptical review of generic "add RAG" suggestions.

### Negative / Risks

- Heuristic may be misread as mandate to add graph infrastructure in v1.

### Safeguards

- Pair table with explicit "v1 default = page-index" callout.
- Require holdout evaluation before any embedding retriever ships.

## Validation Plan

- Apply heuristic to next three platform research reviews mentioning graphs or RAG; record whether proposal is accepted, rejected, or deferred consistently.

## Files Proposed for Future Change

- `docs/product/architecture-rationale.md` (retriever decision table section)
- `docs/platform-intelligence/retriever-selection-heuristic.md` (new, informational)
