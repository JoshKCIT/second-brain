---
description: Push project artifact(s) to Confluence as new pages via the user's API path (or Atlassian Remote MCP Server alternative).
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-publish-to-confluence

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are pushing one or more project artifacts to Confluence as new pages. Uses the user's API-based publish code (primary) or the Atlassian Remote MCP Server (alternative, if validated in build week 1).

## Inputs

- Path to one artifact, OR a project slug
- Target Confluence space key (ask the user; prefer the project's primary space if defined in `meta.yml`)
- Optional parent page (where to nest the new pages; ask the user)

## Pre-flight

- Verify Atlassian credentials in `.env`
- Verify target space exists and the user has create permissions (test with a dry-run API call: GET space, GET space children)
- Confirm the artifact(s) are at status `review` (or higher); refuse to publish drafts unless overridden

## Workflow

### Step 1: Convert Markdown to Confluence storage format

For each artifact:

1. Convert Markdown body to Confluence storage format (XHTML with macros). Use the user's existing converter code (built into the API skill) or invoke the MCP server if it handles conversion.
2. Resolve internal wikilinks: at `published` status these should already be in `## See Also` only (per closure rule); convert to Confluence link macros
3. Resolve cited Confluence URLs in See Also: keep as standard hyperlinks
4. Resolve embedded images: upload as Confluence attachments first, then reference in the body

### Step 2: Confirm with the user

Show a preview:

```
About to publish {N} pages to Confluence:
- Space: {space-key}
- Parent: {parent page or root}
- Pages:
  - {page title 1} (from {artifact path})
  - ...

Proceed? (y/n)
```

Wait for explicit y. Do not proceed on n or anything else.

### Step 3: Publish

For each artifact:

1. POST to `/wiki/api/v2/pages` with title, space ID, parent ID, body
2. On success: capture the new page URL
3. On failure: log the failure, do not block other pages

### Step 4: Update artifact frontmatter

For each successfully published artifact, add to its frontmatter:

```yaml
published_to_confluence:
  page_id: {new page ID}
  page_url: {new page URL}
  published_at: {ISO timestamp}
  published_by: {user email from .env}
```

### Step 5: Update meta.yml

Update `wiki/workspace-projects/{slug}/meta.yml`:

```yaml
status: published
published_at: {ISO timestamp}
confluence_pages:
  - title: {title}
    url: {URL}
  - ...
```

### Step 6: Append to log

```
## [{ISO timestamp}] publish-to-confluence | {slug or artifact}
- Target space: {space-key}
- Parent: {parent or root}
- Pages published: {count}
- Failures: {count or zero}
- URLs: {list}
```

## On API errors

- 401 / 403: stop; surface auth failure
- 409 conflict (page title exists): ask the user whether to update existing or rename
- 429 rate limit: backoff and retry
- 5xx: backoff and retry; if persistent, stop and surface

## Confluence storage format conversion

The conversion is non-trivial. Choices for the build:

- **Option A:** use a maintained library (e.g., a port of mistune with a Confluence renderer)
- **Option B:** custom converter that handles the subset of Markdown we use (frontmatter stripped, headings, paragraphs, lists, tables, code blocks, links, basic emphasis)
- **Option C:** delegate to the Atlassian Remote MCP Server if its publish action handles conversion internally

The build-week decision is captured in `docs/architecture-rationale.md` and any build-time addendum.

## MCP path (alternative)

If the Atlassian Remote MCP Server validates in build week 1 and the user prefers it:

- Replace the API call in Step 3 with the MCP `confluence.create_page` tool
- The rest of the workflow (frontmatter update, log append) is identical
- AGENTS.md documents the choice and how to switch between paths
