# Roadmap

**Status:** v1.0
**Last updated:** 2026-04-28

## v1 (10-14 weeks)

The phase plan from `PRD.md` §9.3, with concrete deliverables per phase.

### Phase 1: Foundations and ingestion spike (week 1-2)

- Repo skeleton (already in place)
- Per-agent shims (in place)
- `verify-setup.py`
- Atlassian Remote MCP Server validation spike (5-page test ingest)
- Port the user's existing Confluence ingestion skill into the repo with frontmatter and layout adapted to AGENTS.md
- `.env.example`, `.gitignore`, `config/second-brain.example.yml` (in place)

Exit: `verify-setup.py` passes against Atlassian Cloud Enterprise; one small Confluence space ingested end-to-end via API path.

### Phase 2: Wiki layer and compile workflow (week 3-4)

- `wiki/` directory layout with `.gitkeep` placeholders
- `compile.prompt.md` (in place; verify integration with `obsidian-markdown` skill)
- `wiki/index.md` and `wiki/log.md` formats
- Quarantine folder behavior
- Post-ingest manifest UX
- Frontmatter schema validation
- Lint scaffold (structural checks 1-7)

Exit: a 100-page Confluence ingest produces a coherent wiki layer with index, log, and zero structural lint errors.

### Phase 3: Query and agent chain skeleton (week 5-6)

- `query.prompt.md` exercises (in place)
- Agent prompts (in place; refine based on early use)
- `start-project.prompt.md` orchestration (in place)
- Project lifecycle: status field, draft → review transitions
- Cross-project dependency rules in lint
- First end-to-end project run (a small internal initiative)

Exit: one project completed via the agent chain; CEO operator confirms the workflow is usable.

### Phase 4: Alignment and vendor truth (week 7-8)

- `align-cite` (production)
- `align-vendor-truth` (production)
- `align-closure` (production)
- `align-conformance` and `align-coverage` (best-effort tier)
- `defuddle` skill integration for vendor doc fetch
- `revalidate-vendor-docs` prompt
- TTL behavior verified end-to-end

Exit: align-cite passes on a project's full artifact set; align-vendor-truth catches a planted contradiction.

### Phase 5: Publish, archive, and Bases integration (week 9-10)

- `publish.prompt.md`, `prepare-for-confluence.prompt.md`, `publish-to-confluence.prompt.md` (in place; refine Markdown-to-storage-format conversion)
- `archive.prompt.md` and `unarchive.prompt.md`
- `obsidian-bases` skill integration; `wiki/views/` Base files for live navigation

Exit: one project published to Confluence successfully; Bases views render in Obsidian.

### Phase 6: Persona templates, exemplar, polish (week 11-12)

- `templates/personas/ceo/` fully populated
- Engineer, Architect, PM, Director, VP stubs (READMEs)
- `docs/style/exemplar-published-doc.md` cleaned and finalized
- README, setup-kit, adoption-checklist polished
- End-to-end pilot with a real project

Exit: a new clone of the repo can be set up and the first project run within 30 minutes of starting.

### Phase 7: Buffer (week 13-14)

- ADF macro coverage long tail
- Lint quality tuning
- Documentation polish
- Pilot feedback incorporated

Exit: v1 release.

## v1.x (post-v1, prioritized)

- Jira ingestion (using `atlassian-requirements-to-jira` agent pattern from `build-inputs/`)
- Pre-ingestion of vendor docs via vendor MCPs (AWS, Snowflake)
- SharePoint and OneNote ingestion
- Population of Engineer, Architect, PM, Director, VP persona templates
- `align-conformance` and `align-coverage` at production quality (with labeled standards or rule-based extraction)
- Atlassian Remote MCP Server as the primary path (if validated and preferred)
- Custom chat-participant extension for `/second-brain` slash command
- Workflow automations (in `build-inputs/workflows/`): scheduled Confluence sync, vendor doc revalidation
- `obsidian-cli` skill adoption for live-update workflows
- Embeddings / hybrid retrieval if wiki passes ~500 articles

## v2 candidates

- Multi-user / shared wiki with merge protocols
- Confluence write-back (edits to existing pages, not just new)
- Mobile or web UI
- Code-as-source (ingest a repo as a knowledge source)
- Cross-tenant federation (read from multiple Atlassian Cloud tenants)
