# CLAUDE.md - Second Brain Operating Instructions

Claude Code reads both this file and `AGENTS.md` at the repository root. `AGENTS.md` is canonical; the content here is operationally sufficient if you only read this file, but you should read `AGENTS.md` for the complete schema, article formats, operation details, and lint check inventory.

## What this repo is

Three layers:

1. `raw/` — immutable source mirror (Confluence pages, vendor docs)
2. `wiki/` — LLM-curated knowledge layer organized by article type and authority
3. `AGENTS.md` — canonical operating spec

Workspace agent chain for new projects: CEO → VP Agent → PM Agent → Architect Agent (if technical) → Engineer Agent → finalize. CEO reviews between stages.

Operations are lane-labeled: `workspace-*` for everyday project/documentation work, and `platform-*` for improving Second Brain itself.

## Routing map (RC-162)

Classify task → invoke prompt → read first paths. Full table: `AGENTS.md` § Routing map. **PH-006:** mid-project Second Brain ideas → platform lane (`platform-transcript-librarian` / `platform-research-review`); do not mutate protected workspace/PRD files without approval.

## Instruction stack (RC-161)

This file is **Tier 2** (IDE shim). It inherits `AGENTS.md` (Tier 1) and adds Claude Code invocation only. Do not restate full root governance—see `AGENTS.md` § Instruction stacking.

## Pointer resources (RC-165)

Extended rule text and verb/operation detail: `templates/workspace/pointer-resources/`. Governance invariants below remain in default load.

## Critical rules

1. Filesystem-first. Markdown and JSON only.
2. Citation-grounded. Every claim has a source link.
3. Read-before-write (RC-122). Read scoped index and sources before artifact edits; record consulted paths in frontmatter `sources`.
4. Authority + domain tagged sources. Vendor claims cite vendor sources; internal claims cite internal sources.
5. Approval-gated mutations. Ingest, sync, archive, remove, publish require explicit user approval.
6. Scoped retrieval per project from `config/second-brain.yml`.
7. Multi-step orchestration with persistent state. Agents hand off through `wiki/workspace-projects/{slug}/0X-{stage}/`.
8. The LLM owns the wiki layer. Direct human edits set `manually_edited: true`.
9. Vendor truth fetched, cached, validated (90-day default TTL).
10. Project deliverable closure: jr-engineer-executable from the published artifact set alone.
11. Body-prose-clean at review and published. Wikilinks allowed at `draft`. Navigation goes in `## See Also` or frontmatter at higher statuses.
12. Three-state lifecycle: `in-progress` → `published` → `archived`. No cross in-progress dependencies.
13. Vendor citation: parenthetical attribution + See Also link. Internal standards: inline relevant rules + Confluence URL in See Also.
14. Safety: fail closed, explicit tool allowlists, append-only audit in `wiki/log.md`, no secrets in vault or logs.
15. No telemetry.

## How operations are invoked

Prompt files in `.github/prompts/`:

- `workspace-start-project` (orchestrates the workspace agent chain)
- `second-brain` (onboarding)
- `workspace-ingest-confluence`, `workspace-ingest-vendor-doc`, `workspace-compile`, `workspace-query`, `workspace-session-audit`, `workspace-thinking-partner`
- `platform-transcript-librarian`, `platform-research-review`, **`platform-implement-backlog`**
- `workspace-align-cite`, `workspace-align-conformance`, `workspace-align-coverage`, `workspace-align-vendor-truth`, `workspace-align-closure`
- `workspace-publish`, `workspace-archive`, `workspace-unarchive`, `workspace-lint`

Verb detail: `templates/workspace/pointer-resources/verb-invocation-detail.md`

## Skills available

`.github/skills/`:

- `obsidian-markdown/` — Obsidian Flavored Markdown (use when authoring wiki content)
- `obsidian-bases/` — `.base` files for live navigation views
- `defuddle/` — clean Markdown extraction from web pages (use when ingesting vendor docs)
- `platform-transcript-librarian` — transcript import, register sync, review queue with human checkpoints
- `platform-research-review/` — transcript-to-claim review with grounding, skeptical scoring, and draft ADR routing
- `platform-implement-backlog/` — one PIC cycle at a time; agent runs `promote-platform-adr.py` on accept (PH-008)
- `session-audit/` — end-of-session orientation/handoff proposals with CEO approval (RC-164)

## Authoring quality bar

`docs/style/exemplar-published-doc.md` is the quality target. Self-contained, term definitions before use, decision rules in tables, concrete worked examples, platform notes, quick reference where useful.

## Where to read more

`AGENTS.md` at repo root.
