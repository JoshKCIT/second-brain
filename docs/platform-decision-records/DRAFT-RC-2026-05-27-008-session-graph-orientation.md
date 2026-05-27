# DRAFT ADR: RC-2026-05-27-008 - Session Graph Orientation

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-008
- Source transcript: `raw/platform-transcripts/Graphify_-_Instant_Knowledge_Graph_for_Claude_Code_Antigravity_FREE.txt`
- Speaker: unknown
- Timestamp: 00:00:30-00:04:30
- Claim type: architecture_proposal

## Context

Graphify-style tools propose reading a prebuilt graph summary at the start of each agent session to reduce repeated file reads. Second Brain already uses index-guided retrieval and durable Markdown artifacts. A session-start orientation summary may help agents without becoming canonical knowledge.

## Decision

Experiment with an optional, generated graph or index summary read at session start. The summary must remain advisory, refreshable, and non-authoritative.

## Rationale

If validated, this could reduce orientation cost for agents working on large wikis or repos. It must not replace source inspection, citation checks, or workspace retrieval policy.

## Impact Scores

| Axis | Score | Rationale |
|---|---:|---|
| Governance | 0 | Neutral unless treated as authoritative. |
| Closure | 1 | May improve first-pass context selection. |
| Grounding | 0 | Neutral; must not substitute for citations. |
| Vendor truth | 0 | Neutral. |
| Inspectability | 1 | Summary can expose what the agent saw first. |
| Maintainability | -1 | Adds sync/staleness concerns. |
| Differentiation | 0 | Neutral. |
| Enterprise fit | 0 | Neutral in local-only form. |
| Human review leverage | 1 | Helps reviewers audit orientation behavior. |

## Alternatives Considered

1. Do nothing.
2. Require agents to reread files every session.
3. Install a third-party graph tool as a hard dependency.
4. Generate an optional local orientation summary from Markdown/index data.

## Consequences

### Positive

- May reduce repeated orientation reads.
- Can complement index-guided retrieval rather than replace it.

### Negative / Risks

- Stale summaries can mislead agents.
- Token-savings claims from the transcript are unvalidated.

### Safeguards

- Mark the summary as advisory only.
- Regenerate from canonical Markdown/index on change.
- Do not wire workspace prompts to depend on it by default.

## Validation Plan

Run paired agent tasks with and without a generated orientation summary. Measure read count, elapsed time, answer correctness, and whether the agent still cites primary sources.

## Files Proposed for Future Change

```text
.github/prompts/
docs/platform-intelligence/
scripts/
```
