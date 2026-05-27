# GitHub Copilot Instructions for Second Brain

You are operating in a Second Brain repository: a personal LLM-maintained knowledge base and documentation production system that runs in VS Code with GitHub Copilot. Read `AGENTS.md` at the repository root for the canonical operating spec. This file is the Copilot-specific shim and is operationally sufficient on its own.

## What this repo is

Three layers:

1. `raw/` — immutable source mirror (Confluence pages, vendor docs)
2. `wiki/` — LLM-curated knowledge layer organized by article type and authority
3. `AGENTS.md` — canonical schema you read

Agent chain (invoked when the user starts a project): CEO declares intent → VP Agent → PM Agent → Architect Agent (if technical) → Engineer Agent → finalize step. CEO reviews and edits between stages.

Operations: ingest (Confluence pages, vendor docs on demand), compile (raw → wiki), query (index-guided), research-review (transcripts to product-intelligence claims), align (cite, conformance, coverage, vendor-truth, closure), publish (review folder or Confluence), archive, lint.

## Critical rules

1. **Filesystem-first.** Every artifact is plain Markdown or JSON.
2. **Citation-grounded.** No claim without a source link.
3. **Authority + domain tagged sources.** Each source carries `authority` (`standard`/`recommendation`/`informational`) and `domain` (`internal`/`vendor:aws`/`industry:nist`/etc.). Vendor capability claims cite vendor sources; internal architecture claims cite internal sources. The source authoritative for the claim's domain wins.
4. **Approval-gated mutations.** Ingest, sync, archive, remove, publish all require explicit user approval after diff or preview.
5. **Scoped retrieval per project.** Default in-scope sources from `config/second-brain.yml`; projects layer additional scope.
6. **Multi-step orchestration with persistent state.** Iterative, resumable; agents hand off through the filesystem at `wiki/projects/{slug}/0X-{stage}/`.
7. **The LLM owns the wiki layer.** Humans read; you write. Direct human edits set `manually_edited: true` in frontmatter for lint visibility.
8. **Vendor truth: fetched, cached, time-validated.** Vendor docs cached on first use, revalidated per TTL (90 days default; 365 hard max).
9. **Project deliverable closure.** A published project's authored set must be jr-engineer-executable using only that set.
10. **Body-prose-clean at review and published.** Wikilinks in body prose are allowed at `draft` (agent collaboration). At `review` and `published`, body contains no internal `[[wikilinks]]`; navigation lives in `## See Also` or frontmatter.
11. **Three-state lifecycle.** Projects move through `in-progress` (sub-states `draft`, `review`) → `published` (curated, referenceable) → `archived` (excluded from default search and reference). In-progress projects cannot reference other in-progress or archived projects. Resolution: finish the dependency, archive it, or restate.
12. **Vendor citation:** parenthetical attribution + See Also link (e.g., "S3 supports SSE-KMS (per AWS docs)" with the URL in See Also). **Internal standards:** inline the relevant rules in body prose + provide Confluence URL in See Also (the reader may not have access to the linked page).
13. **Safety:** fail closed; explicit tool allowlists; require human approval for high-impact tools (publish to Confluence, archive); append-only audit in `wiki/log.md`; never write secrets to vault, index, or logs.
14. **No telemetry.** No phone-home, no analytics.

## How to invoke verbs

The user triggers operations by invoking prompt files in `.github/prompts/`:

- `/start-project` → orchestrates the agent chain for a new project
- `/second-brain` → onboarding; configures in-scope sources, authority and domain mappings
- `/ingest-confluence` → Confluence ingestion using the user's API-based skill
- `/ingest-vendor-doc` → on-demand vendor doc fetch via the `defuddle` skill
- `/compile` → compile new raw/ pages into wiki/ articles
- `/query` → index-guided query against the wiki
- `/research-review` → turn transcripts or meeting notes into grounded claim records, impact reports, and draft ADRs without directly mutating canonical docs
- `/align-cite`, `/align-conformance`, `/align-coverage`, `/align-vendor-truth`, `/align-closure` → verification checks
- `/publish` → branch dispatcher (review folder or Confluence)
- `/archive`, `/unarchive` → lifecycle transitions
- `/lint` → health check

## Skills available

Located in `.github/skills/`:

- `obsidian-markdown/` — produce valid Obsidian Flavored Markdown (wikilinks, callouts, frontmatter, embeds). Use when authoring any wiki article or project artifact.
- `obsidian-bases/` — create `.base` files for live navigation views in `wiki/views/`.
- `defuddle/` — extract clean Markdown from web pages. Use when ingesting vendor docs.
- `research-review/` — extract, ground, score, and adjudicate transcript-derived claims without treating them as canonical knowledge.

## Authoring quality bar

Match the quality target in `docs/style/exemplar-published-doc.md`. Self-contained, term definitions before use, decision rules and tables, concrete worked examples, platform notes, quick reference where useful. Body prose at review/published is clean of wikilinks.

## Where to read more

`AGENTS.md` at repo root for: complete article formats, frontmatter schemas, operation details, lint check inventory, authority/domain rules, project lifecycle, agent chain contracts.
