---
description: Compile newly ingested raw/ pages into the wiki layer. Creates or updates concept, standard, recommendation, and connection articles. Updates index.md and log.md.
mode: agent
---

# /compile

You are integrating newly ingested raw/ pages into the wiki layer. Each raw page becomes one or more wiki articles (concepts, standards, recommendations, informational, or connections), the index is updated, and the log records the action.

## Inputs

- A list of raw/ page paths to compile, OR a `--all` flag to compile every raw page that does not yet have a corresponding wiki article (orphan ingestion check)
- The current state of `wiki/index.md` and existing wiki articles

## Per-page workflow

For each raw page:

1. **Read raw page** including its frontmatter (`source_url`, `authority`, `domain`, etc.)
2. **Read wiki/index.md** to know existing knowledge state
3. **Identify knowledge content** in the page (facts, rules, decisions, patterns, definitions). Each is a candidate for a wiki article.
4. **For each knowledge item, decide:**
   - **Update existing article?** If a `wiki/concepts/`, `wiki/standards/`, etc. article already covers this topic, UPDATE it: add the raw page to its `sources` frontmatter, integrate any new information, refresh `updated` date.
   - **Create new article?** If no existing article covers it, CREATE one in the appropriate directory based on `authority`:
     - `authority: standard` → `wiki/standards/{team}/{slug}.md`
     - `authority: recommendation` → `wiki/recommendations/{team}/{slug}.md`
     - `authority: informational` → `wiki/informational/{slug}.md` or `wiki/concepts/{slug}.md`
5. **Detect connections.** If the page reveals a non-obvious link between 2+ existing concepts, create a `wiki/connections/{slug}.md` article.
6. **Use the obsidian-markdown skill** (`.github/skills/obsidian-markdown/`) for output format compliance.
7. **Update wiki/index.md** with new or modified entries.
8. **Append to wiki/log.md.**

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
  - "raw/confluence/{space-key}/pages/{page-id}--{slug}.md"
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

- [{source page title}]({source_url}) — section reference
```

## Connection article

```markdown
---
title: "Connection: X and Y"
type: connection
connects:
  - "concepts/concept-x"
  - "concepts/concept-y"
sources:
  - {raw paths}
status: published
created: {ISO date}
updated: {ISO date}
---

# Connection: X and Y

## The Connection
[What links them]

## Key Insight
[The non-obvious relationship]

## Evidence
[Examples]

## See Also
- [[concepts/concept-x]]
- [[concepts/concept-y]]
```

## Update wiki/index.md

After creating or updating articles, ensure `wiki/index.md` reflects current state. The index is the LLM's primary retrieval mechanism for queries; without an entry, an article is effectively invisible.

Index format follows AGENTS.md spec (overview + embedded Base views + catalog tables).

## Append to wiki/log.md

```
## [{ISO timestamp}] compile | {raw page or batch}
- Source: {raw paths, max 5}
- Articles created: {list, max 5}
- Articles updated: {list, max 5}
- Index updated: yes
```

## State tracking

Track per-raw-page compile state in `state.json` (gitignored):

```json
{
  "raw/confluence/SPACE/pages/123--page.md": {
    "content_hash": "...",
    "compiled_at": "...",
    "wiki_articles": ["wiki/concepts/...", "wiki/standards/..."]
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
