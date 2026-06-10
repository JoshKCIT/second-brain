---
title: "Workflow: Compile and query"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "templates/workspace/routing-map.md"
  - ".github/prompts/workspace-compile.prompt.md"
  - ".github/prompts/workspace-query.prompt.md"
  - "docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md"
---

# Workflow: Compile and query

**Audience:** Operators who have raw material and want curated wiki knowledge or answers from the knowledge base.

**Purpose:** **Compile** transforms approved raw batches into wiki articles. **Query** navigates the wiki index to answer questions without mutating canonical knowledge (optional file-back to Q&A).

## Terms

| Term | Meaning |
|------|---------|
| **Compile** | LLM reads raw, updates/creates wiki articles, refreshes index and log |
| **RC-146** | Compile requires explicit CEO batch approval — no silent wiki writes |
| **Page-index retrieval** | Query reads `wiki/index.md` first, then full articles — not embedding-only search |
| **File-back** | Optional `--file-back` writes answer to `wiki/workspace-qa/` |

## When to compile vs query

| Goal | Use |
|------|-----|
| New or updated raw pages need wiki articles | `workspace-compile` |
| Ask a question against existing wiki | `workspace-query` |
| Verify citations before publish | `workspace-align-cite` (not query) |
| Refresh vendor TTL metadata | `workspace-revalidate-vendor-docs` |

## Compile batch

Typical compile steps:

1. Agent reads `wiki/index.md` and existing articles that may overlap
2. For each raw page in batch: update concept/standard articles or create new ones
3. Update connections when raw evidence links topics
4. Refresh `wiki/index.md`; append `wiki/log.md`
5. Offer advisory align-cite on new concept/connection articles

Multi-standard project authoring may require a retrieval contract first (RC-018) — compile for inbox/confluence is simpler.

## RC-146 gate

**No wiki write without explicit batch approval.**

The agent must:

1. List raw paths and proposed wiki targets
2. Ask: **"Compile these N items to wiki? (y/n)"**
3. Write `wiki/**` only on **y**

Applies to: Confluence compile, inbox staging, RSS promoted items, vendor compile batches.

RC-151 adds: no scheduled/unattended wiki compile — you must be in the loop.

```text
raw batch proposed  →  CEO y/n  →  wiki mutations + log append
```

## Query flow

1. Agent reads `wiki/index.md`
2. Identifies 3–10 relevant articles from catalog
3. Reads articles in full
4. Lists **Sources consulted** (paths on disk)
5. Synthesizes answer with section-anchored citations

Retrieval guides navigation; it does **not** substitute for `align-cite` at publish time.

## File-back

Optional: persist answer to `wiki/workspace-qa/{slug}.md` for compounding knowledge. Updates index and log. Useful for recurring organizational questions.

Invoke with file-back intent in conversation or per prompt flags when supported.

## Worked example

**Compile:**

1. You: `/workspace-compile` — "compile new ARCH raw pages from yesterday's ingest"
2. Agent: lists 8 raw paths → 6 wiki updates, 2 new concept articles
3. Agent: "Compile these 8 items to wiki? (y/n)"
4. You: **y**
5. Result: `wiki/index.md` updated; log entry with article links

**Query:**

1. You: `/workspace-query` — "What is our microservice sizing standard?"
2. Agent: reads index → `wiki/workspace-standards/architecture/microservice-sizing.md`
3. Agent: answer + Sources consulted list
4. Optional: file to `wiki/workspace-qa/microservice-sizing-explained.md`

## Approval checkpoints

| Operation | CEO approval |
|-----------|--------------|
| Compile batch | **Required y/n** |
| Query | Not required (read-only unless file-back) |
| File-back Q&A | Confirm if agent asks before wiki write |

## Common mistakes

- Running compile expecting it to run without confirmation — agent must stop for y/n
- Treating query sources list as publish-grade citation proof
- Compiling entire repo raw at once — prefer small reviewable batches
- Skipping index update after manual wiki edit — run lint or compile to reconcile

## See Also

- [workflow-ingest.md](workflow-ingest.md)
- [workflow-align-and-publish.md](workflow-align-and-publish.md)
- [operator-guide/concepts-for-operators.md](../operator-guide/concepts-for-operators.md)

## Sources consulted

- AGENTS.md, routing-map.md, workspace-compile.prompt.md, workspace-query.prompt.md, RC-146 ADR
