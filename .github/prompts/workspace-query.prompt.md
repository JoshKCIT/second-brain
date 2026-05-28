---
description: Index-guided query against the wiki. Reads index.md and Base views, identifies relevant articles, synthesizes an answer with citations. Optional file-back saves the answer as a wiki/workspace-qa/ article.
mode: agent
---

# /workspace-query

You are answering a user question by reading the wiki layer (no embeddings, no vector search). **Page-index retrieval:** read `wiki/index.md` first, identify relevant articles, read them in full, synthesize. For long structured sources, navigate by hierarchy and section anchors—not similarity chunking alone.

**Citation ≠ retrieval:** Retrieved context is not citation support. Do not treat semantic similarity or retrieval confidence as verified evidence. Answers must cite section-anchored sources; project artifacts require `align-cite` before publish.

Policy ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-001-page-index-retrieval.md`

## Inputs

- The user's question (natural language)
- Optional `--file-back` flag: persist the answer as a `wiki/workspace-qa/` article
- Optional `--project {slug}` flag: scope retrieval to the project's in-scope sources only
- Optional `--include-archives` flag: include archived content (default: excluded)

## Workflow

### Step 1: Read the index

Read `wiki/index.md` and any embedded Base views. The index is the catalog of every wiki article.

### Step 2: Identify candidate articles

Based on the question, identify 3-10 articles whose titles, summaries, or tags suggest relevance. Prefer articles in:

- `wiki/workspace-standards/` (highest authority)
- `wiki/workspace-recommendations/`
- `wiki/workspace-concepts/`
- `wiki/workspace-connections/` (cross-cutting)
- `wiki/workspace-qa/` (prior answers)

### Step 3: Filter by scope (if applicable)

If `--project` is set, filter to articles whose sources are in the project's `in_scope_spaces` (per `wiki/workspace-projects/{slug}/meta.yml`).

If `--include-archives` is not set, exclude any article with `archived: true` in frontmatter or under `wiki/workspace-archives/`.

### Step 4: Read full articles

Read each candidate article in full. Extract relevant content.

### Step 5: Synthesize

Compose an answer that:

- Directly addresses the question
- Cites every fact-bearing claim to its wiki source (using section anchors where possible) or to a raw/workspace-external/ vendor cache
- Uses the authority+domain rule for conflicts: vendor truth for vendor claims; internal standards for internal architecture
- If a vendor capability is cited but no cached vendor doc exists in `raw/workspace-external/`, offer to ingest it via `/workspace-ingest-vendor-doc` before continuing

### Step 6: Coverage transparency

If you cannot fully answer:

- Report what you consulted: "I read X, Y, Z."
- Report what you could not find: "None addressed the specific question of W."
- Report scope limitations: "Pages on W you may have ingested are not in the current project's scope."
- Do not fabricate.

### Step 7: File-back (if requested)

If `--file-back` is set, save the answer as `wiki/workspace-qa/{slug}.md`:

```markdown
---
title: "Q: {original question}"
type: qa
question: "{exact question}"
consulted:
  - "{wiki path 1}"
  - "{wiki path 2}"
project: {slug if --project was set}
filed: {ISO date}
status: published
---

# Q: {original question}

## Answer

{synthesized answer with citations}

## Sources Consulted

- [{article title}]({path}) — relevant because...

## Follow-Up Questions

- [Open questions raised]
```

Update `wiki/index.md` to list the new qa article. Append to `wiki/log.md`.

### Step 8: Append to log

```
## [{ISO timestamp}] query | "{question}"
- Consulted: {N articles}
- Project scope: {slug or none}
- Filed back: {wiki path or no}
```

## On no relevant articles found

If after reading the index, no articles seem relevant:

- Report this honestly
- Suggest possible reasons (topic not yet ingested, scope too narrow, terminology mismatch)
- Offer remediation: ingest a relevant Confluence space, broaden project scope, or ask a follow-up question

Do not fabricate an answer from general knowledge if the wiki has no support for the claim.
