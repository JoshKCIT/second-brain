# Claims Analysis: second-brain-self-learning-ideas

## Source

- Transcript: `raw/platform-transcripts/second-brain-self-learning-ideas.txt`
- Processing limitations: short promotional transcript; examples are not implementation evidence.

## Executive Judgment

This transcript contains one useful experiment candidate and one already-supported architectural point. The useful idea is a controlled gap-research loop, but only if it routes discoveries through platform research review and draft ADRs. The dangerous variant would let external research directly update canonical platform docs.

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-003 | `workflow_proposal` | experiment | Run a controlled gap-research loop to identify missing platform knowledge and candidate sources. |
| RC-2026-05-27-004 | `architecture_proposal` | adopt | Use a local file-backed knowledge base visible to the coding agent. |

## Grounding Notes

- `AGENTS.md` already treats transcripts as product-intelligence evidence, not canonical knowledge.
- The filesystem-first substrate is already central to Second Brain.
- A self-learning loop must be fail-closed and approval-gated to avoid source contamination.

## Re-review (closure–compile lens, 2026-05-27)

RC-003 **experiment** unchanged: gap research feeds **compile quality** for publish sets via platform review—not auto-canonical edits.

## Recommended Next Actions

- Add a platform research hypothesis for a monthly gap-review cadence.
- Do not allow the gap loop to write `AGENTS.md`, `PRD.md`, or workspace wiki files directly.
