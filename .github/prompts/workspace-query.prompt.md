---
description: Index-guided query against the wiki. Reads index.md and Base views, identifies relevant articles, synthesizes an answer with citations. Optional file-back saves the answer as a wiki/workspace-qa/ article.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-query

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are answering a user question by reading the wiki layer (no embeddings, no vector search). **Page-index retrieval:** read `wiki/index.md` first, identify relevant articles, read them in full, synthesize. For long structured sources, navigate by hierarchy and section anchors—not similarity chunking alone.

**Citation ≠ retrieval:** Retrieved context is not citation support. Do not treat semantic similarity or retrieval confidence as verified evidence. Answers must cite section-anchored sources; project artifacts require `align-cite` before publish.

**Read-before-write (RC-122):** Complete index navigation and full article reads before synthesizing. Do not answer from parametric knowledge when scoped wiki sources exist.

**Citation-grounded query (RC-157):** Every response includes a **Sources consulted** section listing wiki paths, `raw/` paths, and vendor cache paths actually read (paths must exist on disk). Place it before the answer body.

Policy ADRs: `docs/platform-decision-records/RC-2026-05-27-001-page-index-retrieval.md`, `DRAFT-RC-2026-05-27-122-read-before-write-retrieval.md`, `DRAFT-RC-2026-05-27-157-citation-grounded-query.md`

## Inputs

- The user's question (natural language)
- Optional `--file-back` flag: persist the answer as a `wiki/workspace-qa/` article
- Optional `--project {slug}` flag: scope retrieval to the project's in-scope sources only
- Optional `--include-archives` flag: include archived content (default: excluded)

## Workflow

If `--project` is set, draft a brief retrieval contract per `templates/workspace/retrieval-contract-checklist.md` (purpose, scoped sources from `meta.yml`, expected wiki paths) before Step 2 when the question spans multiple standards or domains.

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

### Step 5: List sources consulted

Before synthesizing, emit **Sources consulted** as a bullet list of paths actually read (deduplicated):

- Wiki: `wiki/workspace-standards/...`, `wiki/workspace-concepts/...`, etc.
- Raw: `raw/workspace-confluence/...`, `raw/workspace-external/...` when read for vendor truth
- Do not list articles you identified from the index but did not read in full

Each path must exist on disk. If none apply after honest search, state that explicitly.

### Step 6: Synthesize

Compose an answer that:

- Directly addresses the question
- Cites every fact-bearing claim to its wiki source (using section anchors where possible) or to a raw/workspace-external/ vendor cache
- Uses the authority+domain rule for conflicts: vendor truth for vendor claims; internal standards for internal architecture
- If a vendor capability is cited but no cached vendor doc exists in `raw/workspace-external/`, offer to ingest it via `/workspace-ingest-vendor-doc` before continuing

### Step 7: Coverage transparency

If you cannot fully answer:

- Report what you consulted: "I read X, Y, Z."
- Report what you could not find: "None addressed the specific question of W."
- Report scope limitations: "Pages on W you may have ingested are not in the current project's scope."
- Do not fabricate.

### Step 8: File-back (if requested)

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

### Step 9: Append to log

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

## Response format (required)

Every query response (with or without `--file-back`):

```markdown
## Sources consulted

- `wiki/...` — read in full
- `raw/...` — if applicable

## Answer

{synthesis with section-anchored citations}
```

If coverage is partial, add `## Coverage gaps` after the answer.
