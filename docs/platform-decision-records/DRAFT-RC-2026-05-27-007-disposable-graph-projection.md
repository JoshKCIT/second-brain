# DRAFT ADR: RC-2026-05-27-007 - Disposable Graph Projection

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-007
- Source transcript: `raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt`
- Speaker: Matt
- Timestamp: 00:10:30-00:25:30
- Claim type: architecture_proposal

## Context

Several transcripts suggest knowledge graphs for agent orientation and relationship discovery. Second Brain already uses Markdown, wikilinks, and Obsidian/Bases. A graph projection may help if it is generated from canonical Markdown and can be deleted and rebuilt.

## Decision

Experiment with a disposable graph projection only after core workspace lint stabilizes. The graph must never become source truth.

## Rationale

This keeps the useful inspectability benefit while avoiding premature graph infrastructure.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 1 | Can expose relationships for review. |
| Closure | 0 | Indirect benefit only. |
| Grounding | 1 | Generated from existing sources. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 2 | Relationship map may make context easier to audit. |
| Maintainability | -1 | Adds tooling surface. |
| Differentiation | 1 | Helps governed knowledge review. |
| Enterprise fit | 0 | Neutral in local-only form. |
| Human review leverage | 1 | Helps reviewers find connections. |

## Alternatives Considered

1. Do nothing.
2. Adopt a graph database as canonical storage.
3. Use Obsidian graph only.
4. Generate a disposable graph report from Markdown.

## Consequences

### Positive

- Improves relationship visibility.
- Preserves Markdown as the source of truth.

### Negative / Risks

- Adds a maintenance burden.
- Could duplicate Obsidian/Bases.

### Safeguards

- Regenerate from Markdown only.
- Do not require it for workspace operations.
- Treat stale graph reports as invalid.

## Validation Plan

Generate a graph from wikilinks and frontmatter on a sample wiki. Compare whether reviewers find more broken links, missing backlinks, or cross-topic dependencies than with Obsidian/Bases alone.

## Files Proposed for Future Change

```text
scripts/
wiki/workspace-views/
docs/platform-intelligence/
```
