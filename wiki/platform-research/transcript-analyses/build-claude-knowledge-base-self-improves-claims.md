# Claims Analysis: build-claude-knowledge-base-self-improves

## Source

- Transcript: `raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt`
- Processing limitations: Karpathy-pattern tutorial in Claude Cowork; health-check automation shown with approval bypass options; Karpathy corpus scale anecdote unvalidated for enterprise use.

## Executive Judgment

This transcript is **the closest Karpathy compiler tutorial** in the batch and aligns strongly with Second Brain's architecture. Valuable compile/closure ideas: raw/wiki/outputs loop, ingested registry, index-first query, monthly health check mirroring lint dimensions, anti-AI writing rules at compile. **Reject** unsafe self-improvement paths: auto-saving Q&A to wiki without review, health checks that web-fill gaps without approval. Reinforces no-RAG-at-moderate-scale policy already in architecture rationale.

## Discussion Blocks

| Block | Timestamp (approx) | Topic |
|---|---|---|
| 1 | 00:00–00:03 | Karpathy pattern: raw/wiki/outputs + CLAUDE.md; no Obsidian required |
| 2 | 00:03–00:08 | Schema design, ingestion registry, changelog as memory |
| 3 | 00:08–00:16 | Raw dump; AI compiles wiki; writing style guide |
| 4 | 00:16–00:22 | Index-first query; outputs folder for Q&A artifacts |
| 5 | 00:22–00:28 | Feedback loop: save answers back; gap analysis |
| 6 | 00:24–00:32 | Monthly health check skill; contradictions, orphans, stale, unsourced |
| 7 | 00:32–00:35 | Scheduled auto-action; compounding over 100 days |

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-035 | `architecture_proposal` | adopt | Karpathy raw/wiki/outputs + schema file without Obsidian matches Second Brain's compiler model. |
| RC-2026-05-27-036 | `workflow_proposal` | experiment | outputs/ folder for query artifacts that feed back into compile loop (parallel to workspace-qa). |
| RC-2026-05-27-037 | `evaluation_proposal` | experiment | Monthly health check auditing contradictions, orphans, unsourced claims, and stale wiki articles extends publish closure. |
| RC-2026-05-27-038 | `architecture_proposal` | experiment | Ingested registry / changelog tracks last-processed raw files for incremental compile. |
| RC-2026-05-27-039 | `architecture_proposal` | adopt | Moderate corpora (~100 articles / ~400k words) do not require vector RAG when index-guided retrieval is used. |
| RC-2026-05-27-040 | `workflow_proposal` | reject | Liked Q&A answers should auto-save back to wiki/raw without human review for self-improvement. |
| RC-2026-05-27-041 | `workflow_proposal` | reject | Health check should auto-fill wiki gaps via web search without approval gates. |
| RC-2026-05-27-042 | `workflow_proposal` | experiment | Anti-AI writing style rules applied at wiki compile improve published artifact prose quality. |

## Grounding Notes

- **RC-035:** Direct match to `docs/architecture-rationale.md` §1 and `AGENTS.md` layers; outputs/ is extra vs Second Brain's workspace-qa pattern.
- **RC-036:** Partially supported by `wiki/workspace-qa/` filing; needs explicit compile feedback loop design.
- **RC-037:** Overlaps workspace-lint dimensions; 90-day stale check aligns with vendor TTL thinking.
- **RC-038:** Partially supported by `wiki/log.md` and raw immutability; incremental compile memory not formalized.
- **RC-039:** Reinforces RC-001 and architecture rationale defer-embeddings policy.
- **RC-040:** Matches rejected pattern RP-2026-05-27-001 (auto-update canonical without approval).
- **RC-041:** Bypasses vendor-truth fetch-on-demand and approval gates.
- **RC-042:** Aligns with body-prose-clean and exemplar quality bar; not yet a compile-step requirement.

## Re-review (closure–compile lens, 2026-05-27)

Adopt claims reinforce existing compiler architecture. Experiments target **lint/compile hygiene** and **QA feedback loop**. Reject autonomous self-mutation paths.

## Recommended Next Actions

- Prototype RC-037 as platform wiki lint extension before scheduled automation.
- Route RC-036 through workspace-qa + compile, not direct wiki mutation.
- Do not implement RC-040/041; record in rejected-ideas.md.
