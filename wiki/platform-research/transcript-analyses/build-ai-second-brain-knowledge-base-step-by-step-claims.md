# Claims Analysis: build-ai-second-brain-knowledge-base-step-by-step

## Source

- Transcript: `raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt`
- Processing limitations: YouTube tutorial; Karpathy LLM-wiki clone in Codex; personal journal/CRM/chat focus; Hostinger sponsor segment; closure-compile brief applied.

## Executive Judgment

The **raw/wiki/AGENTS/index/log skeleton** strongly validates Second Brain's three-layer model. Most surface features (journal, CRM, hourly auto-ingest, query-driven wiki growth) are **generic personal assistant scope** and conflict with approval-gated compile and governance band. Two hygiene experiments (processed subfolder, raw back-links) merit small pilots.

## Discussion Blocks

| Block | Timestamp (approx) | Topic |
|---|---|---|
| 1 | 00:00–00:03 | Wiki + CRM + journal pillars; Obsidian center |
| 2 | 00:03–00:06 | Web clipper → raw; AI summarize/extract entities |
| 3 | 00:08–00:12 | Karpathy wiki architecture via Codex; raw/wiki/agents |
| 4 | 00:14–00:19 | Manual process command; query updates wiki |
| 5 | 00:19–00:24 | raw/processed move; cross-link sources; journal/CRM rules |
| 6 | 00:28–00:31 | Hourly Codex automation + GitHub push |
| 7 | 00:06–00:08 | OpenClaw/Hostinger sponsor (out of scope) |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-097 | `architecture_proposal` | adopt | Separating immutable `raw/`, curated `wiki/`, and `AGENTS.md` matches the documentation-compiler three-layer model. |
| RC-2026-05-27-098 | `workflow_proposal` | adopt | Compile from raw to wiki should run on explicit user-approved ingest/process, not implicit chat side effects. |
| RC-2026-05-27-099 | `product_requirement` | reject | Journal + CRM chat layers should be core Second Brain v1 product requirements. |
| RC-2026-05-27-100 | `workflow_proposal` | reject | Hourly automation should process `raw/` into `wiki/` without per-batch human approval. |
| RC-2026-05-27-101 | `workflow_proposal` | reject | Every workspace query should auto-create or update wiki articles without review. |
| RC-2026-05-27-102 | `workflow_proposal` | experiment | After successful compile, move sources to `raw/processed/` for ingest hygiene. |
| RC-2026-05-27-103 | `workflow_proposal` | experiment | Require bidirectional links from wiki articles to immutable raw sources to reduce orphans. |
| RC-2026-05-27-104 | `architecture_proposal` | reject | Consumer YouTube/web-clip dumps without authority/domain tagging should be the default enterprise substrate. |

## Grounding Notes

- **RC-097, RC-098:** Direct match to `AGENTS.md` architecture and approval-gated ingest/compile.
- **RC-099:** Generic personal OS; RC-063 rejected CRM-in-Obsidian pattern.
- **RC-100, RC-101:** Match RC-040 (auto Q&A wiki), RC-051 (passive indexing), RP-001.
- **RC-102:** Hygiene only; does not weaken immutability if raw/processed remains append-only archive.
- **RC-103:** Overlaps RC-050 verbatim-cite experiment; safer as link discipline in compile prompt.
- **RC-104:** Missing authority/domain tags; not Confluence/vendor grounded.

## Closure–compile lens (2026-05-27)

Tutorial **confirms compile model** but optimizes for **chat convenience** over **publish closure**. Reject auto-wiki-from-query patterns that would pollute workspace standards path.

## Recommended Next Actions

- Record RC-099–101, 104 in `rejected-ideas.md`.
- Track RC-102/103 in `open-hypotheses.md` with RC-050 pilot.
