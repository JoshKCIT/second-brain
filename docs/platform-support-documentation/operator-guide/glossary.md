---
title: "Glossary"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "templates/workspace/routing-map.md"
  - "templates/workspace/pointer-resources/verb-invocation-detail.md"
---

# Glossary

Terms used across Second Brain support documentation. Definitions here are operator-oriented; [AGENTS.md](../../../AGENTS.md) is authoritative for agent behavior.

## Term table

| Term | Definition |
|------|------------|
| **Agent chain** | Orchestrated VP → PM → Architect → Engineer stages for a workspace project |
| **align-cite** | Operation verifying citations in an artifact match on-disk sources |
| **align-closure** | Operation checking publish-set rules: wikilinks, cross-project deps, TODOs |
| **Approval gate** | Explicit CEO consent before a mutation (compile, stage, publish) |
| **Authority** | Source level: standard, recommendation, or informational |
| **CEO gate** | Review point between project stages before next agent runs |
| **Compile** | Approval-gated raw → wiki transformation |
| **Closure rule** | Published set must be jr-engineer-executable without wiki link hunting |
| **Compiler analogy** | raw = source; agent = compiler; wiki = executable knowledge |
| **Domain** | Claim scope: internal, vendor:{name}, industry:{name} |
| **Draft tier** | Non-publish scaffolds: handoff, orientation, thinking-notes |
| **Fail closed** | Agent stops and asks rather than guessing on sensitive writes |
| **File-back** | Optional query output saved to `wiki/workspace-qa/` |
| **Handoff** | Stage `handoff.md` carrying locked and open decisions |
| **Inbox** | Raw staging before compile (`workspace-inbox`, RSS items) |
| **Inventory** | Machine scan of prompts/scripts for support doc sync |
| **Jr-engineer-executable** | Junior engineer can execute from published artifact set alone |
| **Lane** | workspace-* (daily docs) vs platform-* (improve Second Brain) |
| **Locked decision** | CEO-confirmed upstream fact downstream must not reopen |
| **meta.yml** | Project stage state: current_stage, stage_gate, last_completed |
| **Page-index retrieval** | Query navigates catalog and structure, not embeddings alone |
| **PIC** | Platform implementation cycle — one approved ADR change at a time |
| **Prompt / verb** | Slash command mapping to `.github/prompts/*.prompt.md` |
| **Quarantine** | Failed ingest conversions stored for review |
| **Raw** | Immutable source layer under `raw/` |
| **RC-146** | Explicit compile batch approval before wiki writes |
| **RC-151** | No unattended wiki compile |
| **Retrieval contract** | Documented source bundle before multi-standard authoring |
| **RSS register** | Review queue index at `raw/workspace-rss-feed/rss-register.md` |
| **Stage gate** | meta.yml signal awaiting_ceo_review when draft stage completes |
| **Tier 1 / 2 / 3** | Instruction stack: AGENTS.md → prompts/shims → project files |
| **Vendor truth** | Vendor claims must cite vendor-domain raw sources |
| **Wiki** | LLM-curated knowledge under `wiki/` |
| **Wikilink** | Obsidian-style double-bracket link — forbidden in body at review/published |

## See Also

- [how-second-brain-works.md](../user-guide/how-second-brain-works.md)
- [concepts-for-operators.md](concepts-for-operators.md)
- [verb-reference.md](verb-reference.md)

## Sources consulted

- AGENTS.md, routing-map.md, verb-invocation-detail.md
