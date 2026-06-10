# ADR: RC-2026-05-27-001 - Page-Index Retrieval Default

## Status

Accepted

## Approval

- Approved: 2026-05-27
- Cycle: PIC-2026-05-27-003
- Bundled claim: RC-2026-05-27-002 (citation ≠ similarity)
- Notes: User approved via continue; implementation pass applied.

## Source Claim

- Claim ID: RC-2026-05-27-001
- Source transcript: `raw/platform-transcripts/second-brain-no-vector-database.txt`
- Speaker: unknown
- Timestamp: 00:00:00-00:01:00
- Claim type: architecture_proposal

## Context

Second Brain v1 already favors index-guided retrieval and defers embeddings until the wiki exceeds roughly 500 articles. The transcript reinforces that structured documents should be navigated by their hierarchy and section context, not only by similarity.

## Decision

Adopt the constrained decision that page-index / structure-aware retrieval remains the v1 default. Any future vector, hybrid, graph, or rerank retriever must prove it improves citation precision and inspectability without weakening closure.

## Rationale

This strengthens Second Brain's governance-and-closure niche. It keeps retrieval evidence inspectable and aligns with the existing requirement that citation support be verified separately from retrieval.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 1 | Keeps retrieval policy explicit. |
| Closure | 1 | Helps generated artifacts point to exact sections. |
| Grounding | 2 | Supports source-structure preservation. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 2 | Navigation trail is visible. |
| Maintainability | 1 | Avoids premature vector infrastructure. |
| Differentiation | 1 | Reinforces a gap competitors do not enforce. |
| Enterprise fit | 1 | Works with local files and source permissions. |
| Human review leverage | 1 | Lets reviewers inspect retrieval decisions. |

## Alternatives Considered

1. Do nothing.
2. Adopt vector retrieval immediately.
3. Use only graph traversal.
4. Keep page-index retrieval as default and benchmark alternatives later.

## Consequences

### Positive

- Preserves the current v1 architecture.
- Makes future retrieval additions evidence-gated.
- Avoids confusing retrieval confidence with citation support.

### Negative / Risks

- Index-guided retrieval may miss cross-cutting concepts if index entries are weak.
- The policy may need revisiting when the wiki grows.

### Safeguards

- Keep `workspace-align-cite` as a publish blocker.
- Define a holdout retrieval/citation evaluation before adopting any new retriever.

## Validation Plan

Use a representative holdout of long Confluence pages. Compare page-index navigation against any candidate retriever on citation precision, reviewer inspectability, and time to supported answer.

## Files Proposed for Future Change

```text
docs/product/architecture-rationale.md
AGENTS.md
PRD.md
```
