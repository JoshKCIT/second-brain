# CLAUDE.md - Second Brain Operating Instructions

Claude Code reads both this file and `AGENTS.md` at the repository root. `AGENTS.md` is canonical; the content here is operationally sufficient if you only read this file, but you should read `AGENTS.md` for the complete schema, article formats, operation details, and lint check inventory.

## What this repo is

Three layers:

1. `raw/` — immutable source mirror (Confluence pages, vendor docs)
2. `wiki/` — LLM-curated knowledge layer organized by article type and authority
3. `AGENTS.md` — canonical operating spec

Agent chain for new projects: CEO → VP Agent → PM Agent → Architect Agent (if technical) → Engineer Agent → finalize. CEO reviews between stages.

Operations: ingest, compile, query, research-review, align (5 levels), publish, archive, lint.

## Critical rules

1. Filesystem-first. Markdown and JSON only.
2. Citation-grounded. Every claim has a source link.
3. Authority + domain tagged sources. Vendor claims cite vendor sources; internal claims cite internal sources.
4. Approval-gated mutations. Ingest, sync, archive, remove, publish require explicit user approval.
5. Scoped retrieval per project from `config/second-brain.yml`.
6. Multi-step orchestration with persistent state. Agents hand off through `wiki/projects/{slug}/0X-{stage}/`.
7. The LLM owns the wiki layer. Direct human edits set `manually_edited: true`.
8. Vendor truth fetched, cached, validated (90-day default TTL).
9. Project deliverable closure: jr-engineer-executable from the published artifact set alone.
10. Body-prose-clean at review and published. Wikilinks allowed at `draft`. Navigation goes in `## See Also` or frontmatter at higher statuses.
11. Three-state lifecycle: `in-progress` → `published` → `archived`. No cross in-progress dependencies.
12. Vendor citation: parenthetical attribution + See Also link. Internal standards: inline relevant rules + Confluence URL in See Also.
13. Safety: fail closed, explicit tool allowlists, append-only audit in `wiki/log.md`, no secrets in vault or logs.
14. No telemetry.

## How operations are invoked

Prompt files in `.github/prompts/`:

- `start-project` (orchestrates the agent chain)
- `second-brain` (onboarding)
- `ingest-confluence`, `ingest-vendor-doc`, `compile`, `query`, `research-review`
- `align-cite`, `align-conformance`, `align-coverage`, `align-vendor-truth`, `align-closure`
- `publish`, `archive`, `unarchive`, `lint`

## Skills available

`.github/skills/`:

- `obsidian-markdown/` — Obsidian Flavored Markdown (use when authoring wiki content)
- `obsidian-bases/` — `.base` files for live navigation views
- `defuddle/` — clean Markdown extraction from web pages (use when ingesting vendor docs)
- `research-review/` — transcript-to-claim review with grounding, skeptical scoring, and draft ADR routing

## Authoring quality bar

`docs/style/exemplar-published-doc.md` is the quality target. Self-contained, term definitions before use, decision rules in tables, concrete worked examples, platform notes, quick reference where useful.

## Where to read more

`AGENTS.md` at repo root.
