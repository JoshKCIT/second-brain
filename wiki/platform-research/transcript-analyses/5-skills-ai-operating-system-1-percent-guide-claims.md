# Claims Analysis: 5-skills-ai-operating-system-1-percent-guide

## Source

- Transcript: `raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt`
- Processing limitations: vendor tutorial (Claude plugins, Relay, Railway MCP); personal/business life-OS focus; heavy autonomous scheduled-task framing; closure-compile brief applied.

## Executive Judgment

This transcript is **useful for routing and filesystem patterns** but **risky on autonomous mutation**. Reinforces `AGENTS.md` as the agent navigation map and local-folder-first retrieval. Rejects scheduled operators that merge/delete strategy content and weekly optimizers that reorganize the vault without approval. Team sync and cloud MCP vault are deferred to multi-user / infrastructure phases.

## Discussion Blocks

| Block | Timestamp (approx) | Topic |
|---|---|---|
| 1 | 00:00–00:04 | Value of memory layer; Obsidian as folder overlay |
| 2 | 00:04–00:07 | OS setup skill: folder templates, CLAUDE.md population |
| 3 | 00:07–00:14 | CLAUDE.md routing; Karpathy nested-CLAUDE.md pattern |
| 4 | 00:14–00:19 | OS operator: scheduled ingest from Slack/meetings; auto-update/delete |
| 5 | 00:19–00:22 | OS optimizer: token audit, merge dupes, reorganize structure |
| 6 | 00:22–00:28 | Team OS + Relay permissions; OS MCP + Railway for cloud routines |
| 7 | 00:24–00:25 | Local folder vs Notion/Drive+MCP tradeoffs |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-082 | `architecture_proposal` | adopt | Top-level agent instruction file (`AGENTS.md` / shims) is the vault navigation map read each session. |
| RC-2026-05-27-083 | `workflow_proposal` | experiment | Nested per-scope instruction files improve agent routing without bloating the root map. |
| RC-2026-05-27-084 | `workflow_proposal` | reject | Scheduled OS operator autonomously updates/deletes strategy and context files from connectors. |
| RC-2026-05-27-085 | `workflow_proposal` | reject | Weekly optimizer autonomously merges, deletes, and reorganizes vault structure without approval. |
| RC-2026-05-27-086 | `architecture_proposal` | defer | MCP-exposed remote vault required for cloud routines when laptop is closed. |
| RC-2026-05-27-087 | `principle_claim` | adopt | Local filesystem access beats cloud Notion/Drive+MCP for agent retrieval accuracy and cost. |
| RC-2026-05-27-088 | `product_requirement` | defer | Real-time team folder sync with per-folder read/write permissions as v1 requirement. |

## Grounding Notes

- **RC-082, RC-087:** Already in `AGENTS.md` (filesystem-first, index-guided query, shims). Reinforcement under closure-compile lens (authoring-time orientation).
- **RC-083:** Karpathy nested-instruction pattern cited; Second Brain has stage paths and `config/second-brain.yml` scoping but not per-wiki-subtree routing files.
- **RC-084, RC-085:** Conflicts with approval-gated mutations, immutable `raw/`, and rejected patterns RC-059 / RP-001 (autonomous canonical mutation).
- **RC-086:** Infrastructure dependency; no v1 closure gain.
- **RC-088:** Aligns with RC-005 defer (multi-user); Relay/Obsidian plugins are vendor-specific.

## Closure–compile lens (2026-05-27)

Favors **compile-time routing** (082, 083, 087). Rejects **publish-time erosion** via unsupervised vault writes (084, 085). Team/cloud items are not closure blockers for v1 solo compiler.

## Recommended Next Actions

- Record RC-084/085 in `rejected-ideas.md`.
- Track RC-083 in `open-hypotheses.md` if nested routing pilot is approved.
- No canonical edits from this transcript.
