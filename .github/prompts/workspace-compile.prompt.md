---
description: Compile newly ingested raw/ pages into the wiki layer. Creates or updates concept, standard, recommendation, and connection articles. Updates index.md and log.md.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-compile

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are integrating newly ingested raw/ pages into the wiki layer. Each raw page becomes one or more wiki articles (concepts, standards, recommendations, informational, or connections), the index is updated, and the log records the action.

## Compile approval gate (RC-146)

**Stop before any wiki write** until the user explicitly approves the compile batch.

1. List every raw path you intend to compile (from user input, `--all` orphan scan, or ingest handoff).
2. Summarize count, paths (max 10 shown; "... and N more" if larger), and expected wiki targets from `wiki/index.md`.
3. Ask: **"Compile these {N} raw pages to wiki? (y/n)"**
4. If **no** or unclear: exit without wiki mutations; suggest `workspace-lint` orphan report for inbox review.
5. If **yes**: proceed with retrieval contract and per-page workflow below.

Never auto-compile on ingest completion, cron, or "small batch" heuristics. Log approved paths in the compile log entry.

Inbox convention: `templates/workspace/raw-inbox-staging.md`. Orphan raw pages in lint are **expected** until approved compile.

## Retrieval contract (RC-018)

Before reading raw pages for a batch, draft a lightweight **retrieval contract** using `templates/workspace/retrieval-contract-checklist.md`:

1. State batch purpose and in-scope sources (from raw frontmatter and `config/second-brain.yml`).
2. List wiki articles you expect to consult via `wiki/index.md` (page-index; RC-001).
3. Tag authority and domain per knowledge type you will extract.
4. Note vendor freshness requirements before citing `raw/workspace-external/`.
5. Record the contract in the compile log entry (YAML block or bullet summary).

Do not select vector/graph/hybrid retrieval—use page-index and section anchors unless an approved eval says otherwise. The contract is orientation, not canonical wiki content.

## Topic / entity compile (RC-148)

After batch approval, follow `templates/workspace/topic-entity-compile.md` for structured cross-link synthesis:

| Phase | Output |
|---|---|
| 1 — Topics | Create/update `wiki/workspace-concepts/` (or standards/recommendations per authority) |
| 2 — Entities | Named things as concepts with `aliases`; merge duplicates |
| 3 — Connections | `wiki/workspace-connections/` only when raw explicitly supports 2+ topic relationship |
| 4 — Verify | Index update; offer advisory align-cite on new/changed concept and connection articles |

**Safeguards:** No connection without raw excerpt in `## Evidence`. No wikilink to a concept that is not in `sources` or `connects` with section anchor. Reject invented cross-links—log skipped candidates in compile log.

## Inputs

- A list of raw/ page paths to compile, OR a `--all` flag to compile every raw page that does not yet have a corresponding wiki article (orphan ingestion check)
- The current state of `wiki/index.md` and existing wiki articles

## Per-page workflow

For each raw page:

1. **Read raw page** including its frontmatter (`source_url`, `authority`, `domain`, etc.)
2. **Read wiki/index.md** to know existing knowledge state
3. **Identify knowledge content** in the page (facts, rules, decisions, patterns, definitions). Each is a candidate for a wiki article.
4. **For each knowledge item, decide:**
   - **Update existing article?** If a `wiki/workspace-concepts/`, `wiki/workspace-standards/`, etc. article already covers this topic, UPDATE it: add the raw page to its `sources` frontmatter, integrate any new information, refresh `updated` date.
   - **Create new article?** If no existing article covers it, CREATE one in the appropriate directory based on `authority`:
     - `authority: standard` → `wiki/workspace-standards/{team}/{slug}.md`
     - `authority: recommendation` → `wiki/workspace-recommendations/{team}/{slug}.md`
     - `authority: informational` → `wiki/workspace-informational/{slug}.md` or `wiki/workspace-concepts/{slug}.md`
5. **Detect connections (RC-148).** If the page reveals a non-obvious link between 2+ topics/entities **with explicit raw support**, create or update `wiki/workspace-connections/{slug}.md`. Skip connections lacking a quotable excerpt—log as `connections_skipped: [{reason}]`.
6. **Use the obsidian-markdown skill** (`.github/skills/obsidian-markdown/`) for output format compliance.
7. **Update wiki/index.md** with new or modified entries (concepts and connections tables).
8. **Append to wiki/log.md.**
9. **Post-batch (RC-148):** Summarize topics created/updated and connections created/updated. Offer advisory align-cite on new concept and connection paths.

## Article structure (concept / standard / recommendation / informational)

```markdown
---
title: "{Title}"
type: concept | standard | recommendation | informational
authority: {from raw page}
domain: {from raw page}
team: {if applicable}
aliases: []
tags: []
sources:
  - "raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md"
status: published
created: {ISO date}
updated: {ISO date}
---

# {Title}

[2-4 sentence core explanation]

## Key Points

- [Self-contained bullets]

## Details

[Encyclopedia-style paragraphs]

## See Also

- [Related concept]({path}) — relationship

## Sources

- [[raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}]] (Section {n}.{heading}) — {one-line excerpt or paraphrase tied to this article}
```

Every concept must include `## Sources` with at least one raw path anchor. Wikilinks in `## See Also` must not assert relationships unsupported by compiled sources.

## Connection article (RC-148)

```markdown
---
title: "Connection: X and Y"
type: connection
connects:
  - "workspace-concepts/concept-x"
  - "workspace-concepts/concept-y"
sources:
  - "raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md"
status: published
created: {ISO date}
updated: {ISO date}
---

# Connection: X and Y

## The Connection

[What links them — one paragraph]

## Key Insight

[The non-obvious relationship]

## Evidence

[Quote or paraphrase from raw with section anchor — **required**; connection invalid without this]

## Sources

- [[raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}#section]] — excerpt supporting the link

## See Also

- [[workspace-concepts/concept-x]]
- [[workspace-concepts/concept-y]]
```

Both `connects` endpoints must exist in wiki or be created in the same batch. Do not publish connection articles without Evidence tied to raw.

## Update wiki/index.md

After creating or updating articles, ensure `wiki/index.md` reflects current state. The index is the LLM's primary retrieval mechanism for queries; without an entry, an article is effectively invisible.

Index format follows AGENTS.md spec (overview + embedded Base views + catalog tables).

## Append to wiki/log.md

```
## [{ISO timestamp}] compile | {raw page or batch}
- Retrieval contract: {one-line purpose; link or inline YAML summary}
- Source: {raw paths, max 5}
- Topics created: {count} | Topics updated: {count}
- Connections created: {count} | Connections updated: {count}
- Connections skipped (no raw support): {count or list}
- Articles created: {list, max 5}
- Articles updated: {list, max 5}
- Advisory align-cite offered: yes | no
- Index updated: yes
```

## State tracking

Track per-raw-page compile state in `state.json` (gitignored):

```json
{
  "raw/workspace-confluence/SPACE/pages/123--page.md": {
    "content_hash": "...",
    "compiled_at": "...",
    "wiki_articles": ["wiki/workspace-concepts/...", "wiki/workspace-standards/..."]
  }
}
```

Use this for incremental compile: if `content_hash` matches the raw frontmatter, skip; otherwise re-compile.

## Conflict handling

If during compile you find that a new raw page contradicts an existing wiki article:

- Apply the authority+domain rule: the source authoritative for the claim's domain wins
- If the new page is authoritative and the existing article is wrong: update the wiki article and flag the change in log
- If the existing article is authoritative and the new page is wrong: do not propagate the new claim into wiki; flag in log as "raw page contradicts authoritative wiki standard"
- If unclear: surface to the user for resolution

## On compile failure

If compile fails for a specific raw page (LLM error, malformed input, etc.):

- Append to log
- Do not block other pages in the batch
- Surface failed pages to the user at end with retry option
