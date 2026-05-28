# Closure-Compile Review Brief

**Status:** Active (2026-05-27 re-review wave)  
**Applies to:** All `/platform-research-review` and `/platform-transcript-librarian` runs until superseded.

## User thesis

Transcripts about second brains, graphs, RAG, Obsidian, and token efficiency are primarily about **how to architect the compiler** so that:

1. **Authoring-time** — agents pull scattered organizational knowledge together (index, structure, optional orientation map) while drafting.
2. **Publish-time** — the **published artifact set** is junior-engineer-executable: steps in body prose, internal rules **inlined**, Confluence/vendor URLs in **See Also** for verification only.

Question-askers get links to source of truth; executors do not click through dozens of pages to complete work.

## Score claims on this axis

| Question | If yes |
|----------|--------|
| Does it improve **closure** (self-contained published sets)? | Favor adopt/experiment |
| Does it improve **compile-time grounding** (find right standard/section before write)? | Favor adopt/experiment |
| Does it strengthen **align-cite** / inspectable retrieval? | Favor adopt/experiment |
| Is it only **generic chat/search/IDE codebase assistant** with no governance gain? | Reject or monitor |

## Do not auto-reject because

- It mentions graphs, vectors, Obsidian, or token savings.
- It sounds like Graphify, Pinecone, or Claude Code tutorials.

## Safer variants (required when surface form sounds generic)

| Rejected-as-stated pattern | Safer variant |
|---------------------------|---------------|
| Index the codebase | Authoring-time map over **wiki + raw Confluence/vendor + project artifacts** to draft publishable docs |
| Mixed code/docs graph | Regenerable **orientation report** from Markdown sources; disposable; not canonical |
| RAG / vectors | Structure-aware or index-guided retrieval with **citation verification**; hybrid only with eval |
| Hot cache / session file | Optional **session orientation** artifact; must not replace align-cite or inline rules at publish |

## Canonical alignment

- `AGENTS.md` — closure rule, internal inline + See Also pattern, page-index retrieval (RC-001/002)
- `docs/architecture-rationale.md` — disposable projections, no premature embeddings
- `product-brief.md` — governance-and-closure band (not generic enterprise search)

## Re-review actions (2026-05-27)

- **RC-2026-05-27-009** moved from `reject` to `experiment` under safer variant (authoring-time cross-source orientation for publish closure).
- Prior batch analyses updated with `## Re-review (closure-compile lens)` sections.
- New queued transcripts reviewed under this brief; claim IDs continue from RC-2026-05-27-016.
