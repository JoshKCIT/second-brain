# GitHub Copilot Instructions for Second Brain

You are operating in a Second Brain repository: a personal LLM-maintained knowledge base and documentation production system. Read `AGENTS.md` at the repository root for the canonical operating spec. This file is the Copilot-specific shim (Tier 2) and is operationally sufficient on its own.

## What this repo is

Three layers: `raw/` (immutable source), `wiki/` (LLM-curated), `AGENTS.md` (schema).

Workspace agent chain: CEO → VP → PM → Architect (if technical) → Engineer → finalize. CEO reviews between stages.

Operations are lane-labeled: `workspace-*` for everyday work, `platform-*` for improving Second Brain itself. Classify the task before touching files.

## Routing map (RC-162)

See `AGENTS.md` § Routing map and `templates/workspace/routing-map.md`. **PH-006:** product/transcript ideas during workspace work → platform lane; no protected-file edits without research review + approval.

## Instruction stack (RC-161)

This file is **Tier 2**. It inherits `AGENTS.md` (Tier 1) and adds Copilot invocation only. Do not restate full root governance—see `AGENTS.md` § Instruction stacking.

## Pointer resources (RC-165)

Extended rule text, verb descriptions, and operation walkthroughs live under `templates/workspace/pointer-resources/`. Read on task match; governance invariants below stay in default load.

## Critical rules

1. Filesystem-first; Markdown and JSON only
2. Citation-grounded; every claim has a source link
3. Read-before-write (RC-122); record consulted paths in frontmatter `sources`
4. Authority + domain tagged sources; domain-authoritative source wins conflicts
5. Approval-gated mutations; ingest/sync/archive/publish require explicit user approval
6. Scoped retrieval per project from `config/second-brain.yml`
7. Multi-step orchestration; hand off through `wiki/workspace-projects/{slug}/0X-{stage}/`
8. The LLM owns `wiki/`; direct human edits set `manually_edited: true`
9. Vendor truth fetched, cached, validated (90-day default TTL; 365 hard max)
10. Project closure: jr-engineer-executable from published artifact set alone
11. Body-prose-clean at review and published; wikilinks allowed at draft only
12. Three-state lifecycle: in-progress → published → archived; no cross in-progress dependencies
13. Vendor citation: parenthetical + See Also link; internal standards: inline rules + Confluence URL
14. Safety: fail closed, explicit allowlists, append-only audit, no secrets in artifacts
15. No telemetry

Expanded explanations: `templates/workspace/pointer-resources/critical-rules-expanded.md`

## How to invoke verbs

Prompt files in `.github/prompts/`:

`workspace-start-project`, `second-brain`, `workspace-ingest-confluence`, `workspace-ingest-vendor-doc`, `workspace-compile`, `workspace-query`, `workspace-session-audit`, `workspace-thinking-partner`, `platform-transcript-librarian`, `platform-research-review`, **`platform-implement-backlog`**, `workspace-align-cite`, `workspace-align-conformance`, `workspace-align-coverage`, `workspace-align-vendor-truth`, `workspace-align-closure`, `workspace-publish`, `workspace-archive`, `workspace-unarchive`, `workspace-lint`

Verb descriptions: `templates/workspace/pointer-resources/verb-invocation-detail.md`

## Skills available

`.github/skills/`: `obsidian-markdown/`, `obsidian-bases/`, `defuddle/`, `platform-transcript-librarian`, `platform-research-review/`, `platform-implement-backlog/`, `session-audit/`

## Authoring quality bar

Match `docs/style/exemplar-published-doc.md`. Article format pointer: `templates/workspace/pointer-resources/article-formats-reference.md`

## Where to read more

`AGENTS.md` at repo root. Operation deep-dives: `templates/workspace/pointer-resources/operation-deep-dives.md`
