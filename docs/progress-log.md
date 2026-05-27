# Progress Log

Append-only record of meaningful work sessions for this repo. Each entry follows the format:

```
## [YYYY-MM-DD] session | short title
- Changed:
- Open:
- Next:
```

Parseable with grep: `grep "^## \[" progress-log.md`.

---

## [2026-05-27] session | platform research review import

- Changed:
  - Promoted the draft platform-research-review kit into first-class project locations: prompt operation, Cursor agent and rule, GitHub skill, templates, product-intelligence docs, config example, and runtime placeholders.
  - Added platform-research-review semantics to `AGENTS.md` and per-agent shims: transcripts are product-intelligence evidence, not canonical knowledge.
  - Added ignore rules for live transcripts and generated platform-research-review outputs while preserving tracked templates and placeholders.

- Open:
  - Run the validation suite and confirm `draft-version/` has no remaining unique keep-worthy content before removal.

- Next:
  - Wire platform-research-review lint checks and tests, then delete `draft-version/` after validation.

---

## [2026-04-28] session | initial planning and core repo scaffolding

- Changed:
  - Worked through architecture decisions across multiple turns; produced product-brief v0.3 incorporating all locks (Karpathy + Cole pattern, GitHub repo distribution, AGENTS.md + per-agent shims, Confluence Enterprise Cloud as primary source, Obsidian as canonical reader, multi-agent workflow chain CEO → VP → PM → Architect → Engineer, three-state lifecycle, status-aware closure rule, body-prose-clean rule, vendor-truth handling with TTL, writing-style exemplar, etc.)
  - Created core planning docs: README.md, product-brief.md (v0.3), PRD.md, AGENTS.md, docs/architecture-rationale.md
  - Curated reference materials into `build-inputs/` (5 obsidian skills, 8 awesome-copilot skills, 2 agents, 5 instructions, 4 hooks, 2 plugins, 3 inspirations, 8 workflows)
  - Created shipped repo structure: `.github/{prompts,skills,agents,hooks}/`, `.cursor/rules/`, `docs/style/`, `config/`, `templates/personas/{ceo,engineer,architect,product-manager,director,vp}/`
  - Copied 3 obsidian skills into `.github/skills/`: obsidian-markdown, obsidian-bases, defuddle
  - Wrote per-agent shims: `.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`
  - Wrote agent chain prompts: `start-project`, `vp-agent`, `pm-agent`, `architect-agent`, `engineer-agent`
  - Wrote operational prompts: `second-brain` (onboarding), `ingest-confluence`, `ingest-vendor-doc`, `compile`, `query`, `align-cite`, `align-vendor-truth`, `align-closure`, `align-conformance`, `align-coverage`, `publish`, `prepare-for-confluence`, `publish-to-confluence`, `archive`, `unarchive`, `lint`
  - Wrote `.github/agents/workspace-adr-generator.agent.md`
  - Wrote `.env.example`, `.gitignore`, `config/second-brain.example.yml`
  - Wrote docs: roadmap.md, setup-kit.md, adoption-checklist.md, progress-log.md (this file)
  - Copied `writing-example.md` to `docs/style/exemplar-published-doc.md` (cleanup of export artifacts pending)

- Open:
  - The exemplar at `docs/style/exemplar-published-doc.md` has stray `**bold**` artifacts from the original export; needs a cleanup pass before final v1 release
  - The CEO persona template at `templates/personas/ceo/` is just a stub README in this batch; needs population (schema additions, example workflows, starter wiki content) per the Phase 6 milestone in roadmap
  - The other 5 persona templates (engineer, architect, product-manager, director, vp) are minimal stubs; v1.x population
  - Atlassian Remote MCP Server validation spike is queued for build week 1
  - Markdown-to-Confluence-storage-format conversion library choice is queued for Phase 5
  - The `ai-team-orchestration` plugin in `build-inputs/plugins/` was supposed to be removed (duplicate of the skill version) but had Windows readonly permissions; user can delete manually
  - Evidence (§1.2 of brief), why-now (§1.3), kill criteria (§7.3), build budget specifics still marked `[NEEDS INPUT]` in the brief

- Next:
  - Build week 1: foundations + Atlassian MCP spike + port the user's existing Confluence ingestion skill into the repo
  - Resolve the exemplar cleanup
  - Begin populating the CEO persona template
  - Track build progress per phase in this log

---
