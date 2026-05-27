---
description: Ingest Confluence pages via the user's existing API-based skill. Per-page output to raw/workspace-confluence/{space-key}/pages/, synchronous compile to wiki/, post-ingest manifest with quarantine for failures.
mode: agent
---

# /workspace-ingest-confluence

You are ingesting Confluence pages into the user's Second Brain. The user provides a space key, page ID, page URL, or list of these. Output lands in `raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md`. The wiki layer is compiled synchronously.

## Inputs

The user provides one of:
- A Confluence space key (ingest the space's pages)
- A page URL (ingest single page; ask whether to include children)
- A page ID (same)
- A list of any of the above

## Pre-flight

- Verify Atlassian credentials in `.env`
- Verify the source-domain mapping for this space exists in `config/second-brain.yml`. If not, ask the user to configure authority and domain for the new space before proceeding.
- Verify `raw/workspace-confluence/{space-key}/` exists; create if not.

## Ingest pipeline (per page)

1. **Fetch.** Use the API path documented in `AGENTS.md` (REST API v2 with `body-format=atlas_doc_format`). Pull the page body, attachments metadata, and labels.
2. **Convert.** Convert ADF to Markdown. Use the `obsidian-markdown` skill (`.github/skills/obsidian-markdown/`) to ensure output matches Obsidian Flavored Markdown conventions.
3. **Frontmatter.** Add YAML frontmatter:

```yaml
---
source_url: {Confluence URL with section anchor}
space_key: {SPACE}
page_id: {NUMERIC}
title: {Page title}
ancestors: [list of ancestor page titles]
version: {version number}
last_modified: {ISO timestamp}
labels: [list]
ingested_at: {ISO timestamp}
content_hash: {SHA-256 of body content}
authority: {from config: standard|recommendation|informational}
domain: {from config: internal|vendor:X|industry:Y}
---
```

4. **Write to raw.** `raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md`.
5. **On conversion failure:** write the raw payload (ADF JSON) and error to `quarantine/{date}/{page-id}/source.json` and `quarantine/{date}/{page-id}/error.md`. Do not block the rest of the run.

## Compile (synchronous)

After the raw page lands, invoke `workspace-compile.prompt.md` to integrate it into the wiki layer. Compile is part of ingest; do not return until both raw and wiki are updated.

## Post-ingest manifest

Print to the user:

```
Ingested {N} pages from {space-key}:
- Compiled into wiki: {count}
  - New articles: {count}
  - Updated articles: {count}
- Quarantined: {count}
  - {page-id}: {error reason}
- Index updated: yes/no
- Run smoke-test query? (y/n)
```

If the user opts for a smoke test, run `workspace-query.prompt.md` against a few canned queries derived from the new content's titles or labels.

## Append to log

```
## [{ISO timestamp}] ingest-confluence | {space-key}
- Pages fetched: {N}
- Compiled: {count}
- Quarantined: {count}
- Wiki articles created: {list, max 5; "..." if more}
- Wiki articles updated: {list, max 5; "..." if more}
```

## Sync mode

If invoked with `--sync` flag (or the user asks for sync), compare incoming pages against existing raw/ entries by `version` and `content_hash`. Skip unchanged pages. For changed pages, run the ingest pipeline as above; the compile stage will update the corresponding wiki article rather than create a new one.

The weekly sync reminder fires after 7 days since the last sync (per `config/second-brain.yml` `confluence_sync.default_cadence`); when it fires, prompt the user to run sync.

## On API errors

- 429 rate limit: backoff and retry with exponential delay
- 401 / 403: stop; surface auth failure; recommend running setup verification
- 404 page not found: skip the page, log the failure, continue
- 5xx: backoff and retry; if persistent, stop and surface
