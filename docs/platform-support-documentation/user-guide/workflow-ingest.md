---
title: "Workflow: Ingest"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "templates/workspace/routing-map.md"
  - "templates/workspace/raw-inbox-staging.md"
  - "templates/workspace/rss-feed-lifecycle.md"
  - ".github/prompts/workspace-ingest-confluence.prompt.md"
  - ".github/prompts/workspace-ingest-vendor-doc.prompt.md"
  - ".github/prompts/workspace-ingest-rss.prompt.md"
---

# Workflow: Ingest

**Audience:** Operators and new users pulling external knowledge into Second Brain.

**Purpose:** Ingest moves source material into the immutable **raw** layer. Wiki updates happen only later via **compile** with explicit CEO approval (RC-146). This page covers Confluence, vendor docs, manual inbox clips, and RSS.

## Terms

| Term | Meaning |
|------|---------|
| **Raw** | Immutable evidence under `raw/` — not rewritten after ingest |
| **Inbox** | Staging paths (`raw/workspace-inbox/`, RSS items) awaiting triage or compile |
| **Compile** | Separate verb — raw → wiki; always approval-gated |
| **Authority / domain** | Tags on sources: who is authoritative and for what claim type |

## When to use which ingest

| Source | Invoke | Raw path |
|--------|--------|----------|
| Confluence space or pages | `workspace-ingest-confluence` | `raw/workspace-confluence/` |
| Vendor URL (AWS, etc.) | `workspace-ingest-vendor-doc` | `raw/workspace-external/{vendor}/` |
| Manual clip or export | inbox capture + compile | `raw/workspace-inbox/{date}/` |
| RSS feeds | `workspace-ingest-rss` | `raw/workspace-rss-feed/items/` |

## Confluence flow

```text
config/second-brain.yml  →  workspace-ingest-confluence  →  raw/workspace-confluence/
                                                          →  [CEO y/n] workspace-compile  →  wiki/
```

1. Confirm space is in-scope in `config/second-brain.yml` with authority and domain
2. Invoke `/workspace-ingest-confluence` with space key, URL, or page IDs
3. Agent fetches via Atlassian API, converts to Markdown, writes raw pages
4. Failures go to `quarantine/{date}/{page-id}/` — ingest continues
5. Agent presents compile batch — **you approve before wiki writes**

Large spaces: ingest in batches if rate-limited (429 responses).

## Vendor flow

1. Check TTL in `raw/workspace-external/` — stale caches prompt refetch (90-day default)
2. Invoke `/workspace-ingest-vendor-doc` with URL
3. Agent uses defuddle to clean HTML → Markdown in vendor path
4. Compile to wiki concepts via `/workspace-compile` with approval

Vendor capability claims at publish time must cite vendor-domain sources (`align-vendor-truth`).

## Inbox staging

Manual captures land in `raw/workspace-inbox/{YYYY-MM-DD}/{slug}.md` with frontmatter:

- `authority`, `domain`, `inbox_status: unprocessed`
- CEO confirms authority/domain before compile

See [templates/workspace/raw-inbox-staging.md](../../../templates/workspace/raw-inbox-staging.md).

## RSS flow

```text
config/rss-feeds.yml  →  ingest-rss  →  items/
                     →  triage-rss (deterministic)
                     →  workspace-triage-rss (borderline LLM, optional)
                     →  sync-rss-register  →  rss-register.md
                     →  workspace-review-rss  →  promote | archive | dismiss
                     →  promoted/ full article
                     →  workspace-compile (RC-146 y/n)  →  wiki/
```

RSS never auto-compiles to wiki. CEO reviews queue via `/workspace-review-rss`.

## Approval gates

| Step | Approval required? |
|------|-------------------|
| Fetch to raw | No (ingest may run) |
| Compile raw → wiki | **Yes — RC-146 explicit batch y/n** |
| RSS promote | **Yes — per item in review-rss** |
| Wiki write from RSS | **Yes — compile batch** |

## Worked example

**Scenario:** Ingest 15 pages from Architecture Confluence space.

1. You: `/workspace-ingest-confluence` — space key `ARCH`
2. Agent: fetches 15 pages → `raw/workspace-confluence/ARCH/pages/`; 1 quarantined
3. Agent: "Compile these 14 pages to wiki? (y/n)" with proposed article list
4. You: **y**
5. Agent: updates `wiki/workspace-concepts/`, `wiki/index.md`, appends `wiki/log.md`
6. You: open Obsidian → `wiki/index.md` shows new entries

If you answer **n**, raw remains; wiki unchanged.

## Approval checkpoints

| Checkpoint | Question you answer |
|------------|---------------------|
| Compile batch | "Compile these N pages to wiki? (y/n)" |
| RSS promote | promote / archive / dismiss per `item_id` |
| Inbox authority | Confirm authority/domain before compile |

## Common mistakes

- Assuming ingest automatically updates the wiki — it does not without compile approval
- Compiling platform transcripts into workspace wiki — wrong lane
- Skipping RSS review and expecting items in hub — only **promoted** paths compile
- Ingesting spaces not mapped in `config/second-brain.yml` — scope and authority unclear

## See Also

- [workflow-compile-and-query.md](workflow-compile-and-query.md)
- [templates/workspace/rss-feed-lifecycle.md](../../../templates/workspace/rss-feed-lifecycle.md)
- [operator-guide/ceo-approval-guide.md](../operator-guide/ceo-approval-guide.md)

## Sources consulted

- routing-map.md, raw-inbox-staging.md, rss-feed-lifecycle.md, workspace-ingest prompts
