# PRD: Second Brain

**Status:** Draft v1.0
**Owner:** Josh
**Last updated:** 2026-04-28
**Source brief:** `product-brief.md` v0.3

This PRD specifies what Second Brain v1 builds, who it serves, what it must do, how success is measured, and what it explicitly will not do. Every requirement here traces back to a statement in the product brief.

---

## 1. Product overview

### 1.1 Document title and version

- PRD: Second Brain
- Version: v1.0

### 1.2 Product summary

Second Brain is a personal, LLM-maintained knowledge base and documentation production system that runs inside VS Code with GitHub Copilot. It ingests organizational documentation from Confluence (and on-demand vendor documentation from public sources) into a local Markdown wiki, and orchestrates a chain of specialized LLM agents to produce new project documentation that is grounded in canonical sources and executable by a junior engineer using only the published artifact set.

**Scope positioning.** Second Brain does not compete with Rovo, Glean, Microsoft Copilot for M365, Notion AI, or Sourcegraph Cody on generic enterprise search, Q&A, multi-step agents, IDE-integrated codebase chat, or basic page templates. Those tools have substantially closed those capabilities since early 2025. Second Brain targets the governance-and-closure band that none of them productize: claim-domain authority and vendor truth arbitration, jr-engineer-executable closure, multi-page stage-gated technical-doc generation with Confluence-storage-format output, mandatory section-level citation discipline, inspectable retrieval as policy, and project artifact lifecycle with cross-project dependency rules. See `product-brief.md` §1.2 for the capability table and §8.1 Risk 7 for the scope-discipline filter applied to feature proposals.

The system is designed for a CEO operator who declares a project's high-level intent and reviews artifacts produced by VP, PM, Architect, and Engineer agents in sequence. The wiki layer compounds over time: each completed project's published documents become referenceable knowledge for future projects.

The deliverable is a clonable GitHub repository. Users adopt by cloning, configuring `.env` with Atlassian Cloud credentials, and invoking the `/second-brain` onboarding prompt in Copilot chat. The repo ships with a canonical operating spec (`AGENTS.md`), per-agent shim files for major coding agents (Copilot, Claude Code, Cursor, Windsurf), reusable prompts, agent-skill definitions, default Obsidian configuration, and persona templates.

---

## 2. Goals

### 2.1 Business goals

- Standardize how engineering project documentation is produced across teams, with explicit grounding in canonical sources
- Reduce the time between a project being assigned and a usable documentation set existing
- Produce documentation that is auditable: every claim traces to a Confluence page section or vendor URL
- Catch documentation drift between internal claims and vendor capabilities before publication
- Provide a reusable, agent-agnostic foundation that other roles in the organization can adopt over time

### 2.2 User goals

- Declare a new project's intent and let the agent chain produce a complete artifact set with minimal review burden
- Trust that any document marked `published` is executable by a junior engineer without follow-up
- Pull canonical standards from multiple teams' Confluence spaces into the personal wiki and have them tagged by authority and domain
- Author derivative documentation that automatically aligns with those canonical standards
- Verify that vendor-related claims reflect current vendor documentation, not stale internal interpretation
- Move completed projects' artifacts into the wiki as referenceable knowledge for future projects
- Archive completed or deprecated work without losing audit trail

### 2.3 Non-goals

- Not a Confluence replacement. Second Brain reads from Confluence and creates new pages; it does not edit existing pages.
- Not a real-time collaboration tool. Single-user local in v1.
- Not a chat product or general-purpose assistant. Verbs are scoped.
- Not a replacement for Obsidian. Obsidian is the canonical reader; Second Brain produces Obsidian-compatible files.
- Not multi-tenant. Each user runs their own instance.
- No telemetry, analytics, or phone-home behavior in v1.

---

## 3. User personas

### 3.1 Key user types

- **CEO (primary, populated in v1):** declares project intent, reviews artifacts between agent stages, edits drafts, approves publish operations
- **Engineer, Architect, Product Manager, Director, VP (secondary, stubs in v1; populated in v1.x):** alternative operator personas using the same system with persona-specific templates

### 3.2 Basic persona details

- **CEO operator (Josh).** Hands-on operator. Runs Copilot prompts, reviews artifacts, edits prose. Tone of templates and prompts is direct, terse, technical. Doc types include strategy memos, board materials, project briefs, executive briefings, decision rationales.
- **Agent roles (not user personas).** VP, PM, Architect, Engineer agents are workflow stages invoked by the system, not separate users. Each has a defined role definition, input contract, output contract, source-of-truth scope, and human checkpoint.
  - **VP Agent:** works with CEO to produce `product-brief.md` for a new project
  - **PM Agent:** uses VP output to produce `product-requirements.md`
  - **Architect Agent (when technical):** produces `architectural-approaches.md` evaluating candidate options
  - **Engineer Agent:** produces implementation specifics; runs the finalize step

### 3.3 Role-based access

N/A. Second Brain is single-user local in v1. Each user runs their own instance with their own Confluence credentials. Access to source content is governed by the user's existing Confluence permissions (the API token cannot read what the user cannot read). There are no in-product roles, accounts, or sharing primitives.

---

## 4. Functional requirements

### 4.1 Setup and configuration (Priority: High)

- Clone-and-run installation: user clones the GitHub repo, copies `.env.example` to `.env`, fills credentials, runs `verify-setup.py`
- `verify-setup.py` validates `.env` completeness, tests Confluence API connectivity, creates required runtime directories (`raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/`), initializes empty `wiki/index.md` and `wiki/log.md`
- Per-agent shim files in conventional locations (`.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`) reference `AGENTS.md` and are operationally sufficient on their own
- `.gitignore` excludes runtime content (`raw/*`, `wiki/*`, `confluence-review/`, `quarantine/`, `reports/`, `config/second-brain.yml`, `.env`)

### 4.2 Onboarding (Priority: High)

- `/second-brain` prompt (invoked from Copilot chat) walks the user through: default in-scope Confluence spaces with authority and domain mappings, naming conventions, first project setup
- Conversation produces `config/second-brain.yml` with user's choices
- Conversation creates an initial `wiki/workspace-projects/{first-slug}/` skeleton

### 4.3 Project lifecycle (Priority: High)

- `start-project` prompt orchestrates the agent chain: CEO declares intent → VP Agent → PM Agent → Architect Agent (if technical) → Engineer Agent → Engineer-led finalize step
- Each agent reads the prior agent's output and produces its own artifact in `wiki/workspace-projects/{slug}/0X-{stage}/`
- CEO reviews and edits between stages; explicit approval required to invoke the next agent
- Three lifecycle states: `in-progress` (sub-states `draft`, `review`), `published`, `archived`
- Status field in frontmatter; lint enforces stage-appropriate rules
- Archive operation moves the project's directory to `wiki/workspace-archives/projects/{slug}/`; opt-in to include in search and reference; `unarchive` reverses
- Cross-project dependency rule: an `in-progress` project cannot reference another `in-progress` or `archived` project. Resolution is finish, archive, or restate.

### 4.4 Confluence ingestion (Priority: High)

- User provides a space key, page ID, page URL, or list of these
- Ingestion uses the user's existing API-based skill (REST API v2; ADF body format) ported into the repo with file format adapted to Second Brain frontmatter
- Per-page output: `raw/workspace-confluence/{space-key}/pages/{page-id}--{slug}.md` with frontmatter (`source_url`, `space_key`, `page_id`, `title`, `ancestors`, `version`, `last_modified`, `labels`, `ingested_at`, `content_hash`, `domain`, `authority`)
- Attachments captured under `raw/workspace-confluence/{space-key}/attachments/`
- Compile stage runs synchronously: each ingested page is integrated into the wiki layer (concept extraction, standards classification, index update)
- Quarantine for conversion failures: `quarantine/{date}/{page-id}/` with raw payload and error report; does not block the rest of the run
- Post-ingest manifest: agent prints page count, success count, quarantined count with reasons, wiki articles created or updated, index status, optional smoke-test query
- Atlassian Remote MCP Server documented as an alternative path; build-week-1 spike validates whether it is viable on the user's tenant
- Confluence sync: weekly default cadence; reminder after 7 days; user-invoked sync command runs incremental ingestion

### 4.5 Vendor doc ingestion (Priority: High)

- Triggered on demand: when an agent is about to cite a vendor capability, it offers to fetch the relevant vendor doc
- User opts in per claim
- Fetch uses `defuddle` to extract clean Markdown
- Output: `raw/workspace-external/{vendor}/{topic}/{slug}.md` with frontmatter (`source_url`, `vendor`, `topic`, `fetched_at`, `revalidate_after`, `domain` (e.g., `vendor:aws`), `authority`)
- TTL defaults: 90 days (`vendor_revalidation.default_ttl_days`); per-vendor overrides supported; hard max 365 days
- Within TTL: cache treated as fresh; cited with `(cached YYYY-MM-DD)` annotation in agent output
- Past TTL but under hard max: agent flags stale and offers refetch before citing
- Past hard max: agent always prompts; cannot cite without refresh
- `revalidate-vendor-docs` command enumerates stale items and offers batch refresh

### 4.6 Wiki layer and indexing (Priority: High)

- Deterministic on-disk layout under `wiki/`:
  - `index.md` (master catalog; Obsidian home page; embeds Base views)
  - `log.md` (append-only chronological build log)
  - `standards/`, `recommendations/`, `informational/` (organized by authority level)
  - `concepts/` (atomic knowledge articles)
  - `connections/` (cross-cutting insights linking 2+ concepts)
  - `qa/` (filed query answers)
  - `projects/{slug}/` (project-specific artifact sets)
  - `archives/` (completed and deprecated content)
  - `views/` (Obsidian Base files for live navigation)
- Every wiki article carries YAML frontmatter (title, type, authority, domain, sources, status, created, updated)
- Compile stage uses `obsidian-markdown` skill to ensure valid Obsidian Flavored Markdown output
- Base views in `wiki/workspace-views/`: standards-by-team, recommendations-by-team, active-projects, recent-activity, stale-vendor-docs, lint-flagged
- Atomic publish: a compile run that fails partway leaves the index and articles unchanged

### 4.7 Query (Priority: High)

- Index-guided retrieval: agent reads `wiki/index.md` and Base views first, identifies relevant articles, reads them in full, synthesizes answer
- Embeddings deferred (revisit only if wiki passes ~500 articles)
- Citations to source pages and section anchors required in the answer
- Optional `--file-back`: persists the answer as a `wiki/workspace-qa/` article and updates `index.md` and `log.md`
- Project-scoped queries: when invoked from inside a project context, retrieval is filtered to in-scope sources for that project

### 4.8 Documentation generation via agent chain (Priority: High)

- `start-project` prompt orchestrates the chain
- Each agent prompt is in `.github/prompts/{vp,pm,architect,engineer}-agent.prompt.md` with explicit role, input contract, output contract, source-of-truth scope, and finalize-handoff instructions
- Generated artifacts include inline citations to source pages and vendor URLs
- Body prose at `draft` stage allows wikilinks; finalize step rewrites to body-prose-clean for `review`
- Each artifact's frontmatter includes status, sources consulted, domain, authority (where applicable)
- Writing-quality target: every authored artifact aims to match the exemplar in `docs/style/exemplar-published-doc.md`

### 4.9 Alignment checks (Priority: High)

Five distinct align operations:

| Command | Purpose | Quality tier in v1 |
|---|---|---|
| `align-cite` | Verify every cited claim resolves to a source containing the cited content | Production |
| `align-conformance` | Verify draft's structure, terminology, and decisions match each in-scope standard's conventions | Best-effort (advisory) |
| `align-coverage` | Verify draft addresses every relevant requirement from in-scope standards (gap analysis) | Best-effort (advisory) |
| `align-vendor-truth` | Verify vendor-domain claims cite vendor sources, not stale internal claims | Production |
| `align-closure` | Verify the active authored set is jr-engineer-executable using only itself; no body wikilinks at review/published; cross-project rules respected | Production |

`align-cite` and `align-closure` run automatically before publish (review or Confluence). Others on demand or before formal external review.

### 4.10 Lint (Priority: High)

Seven structural checks plus engineering additions:

1. Broken links
2. Orphan pages (no inbound links from other articles in the same set)
3. Orphan sources (raw/ pages not yet compiled)
4. Stale articles (source raw/ page changed since article was last compiled)
5. Missing backlinks
6. Sparse articles (under 200 words)
7. Contradictions (LLM-judged, advisory)

Engineering additions:
- Deprecated standards detection
- Conflicts between teams' requirements
- Missing alignment to published standards (within in-scope sources)
- Incomplete ingestion (page in `raw/` without wiki article)
- Stale vendor docs (past TTL or hard max)
- Status-aware closure violations
- Cross-project dependency violations

Lint reports written to `reports/workspace-lint-{date}.md` with severity (error, warning, suggestion).

### 4.11 Publish (Priority: High)

- `publish` prompt asks: review or Confluence?
- **Review branch:** convert Markdown draft to vanilla HTML (browser-readable preview, not Confluence storage format); write to `confluence-review/{project-slug}/{doc-slug}-{timestamp}.html`; print full path; open the folder via OS-native opener (`explorer` Windows, `open` macOS, `xdg-open` Linux)
- **Confluence branch:** publish via the user's existing API-based code (primary) or Atlassian Remote MCP Server (alternative). Markdown converted to Confluence storage format or ADF.
- `align-cite` and `align-closure` run automatically before publish; violations block unless user explicitly overrides; overrides logged
- Publishing creates new Confluence pages; does not edit existing pages

### 4.12 Archive (Priority: Medium)

- `archive` prompt moves a completed or deprecated project's directory to `wiki/workspace-archives/projects/{slug}/` (or analogous for standards/recommendations)
- Frontmatter `archived: true` and `archived_at: timestamp` set on every file in the moved set
- Excluded from default search and reference; included only on explicit opt-in
- `unarchive` reverses the operation; logged in `wiki/log.md`

### 4.13 Run history and audit (Priority: Medium)

- Every ingestion, compile, query (with --file-back), align, publish, archive, and lint operation appended to `wiki/log.md` with ISO 8601 timestamp and structured prefix (`## [TIMESTAMP] operation | description`)
- Log is parseable with simple grep
- Per-run state tracked in `state.json` (gitignored): SHA-256 hashes of source files, last compile timestamps, query count, total cost (if budget tracking is added)

### 4.14 Configuration and secrets (Priority: High)

- Atlassian credentials in `.env` (`ATLASSIAN_SITE_URL`, `ATLASSIAN_EMAIL`, `ATLASSIAN_API_TOKEN`; or OAuth fields if the tenant requires)
- Anthropic key not required (LLM access is via Copilot agent mode)
- Vault path defaults to repo root; configurable
- Vendor TTL and Confluence sync cadence in `config/second-brain.yml`
- Secrets never written to vault, index, or run manifests

---

## 5. User experience

### 5.1 Entry points and first-time user flow

- First-time setup: clone the repo, copy `.env.example` to `.env`, fill Atlassian credentials, run `python scripts/verify-setup.py` to validate connectivity and create directories
- Open the repo in VS Code; ensure GitHub Copilot agent mode is enabled and points to a current Claude or GPT model
- In Copilot chat, invoke the `/second-brain` prompt (or open `.github/prompts/second-brain.prompt.md` and run it as a prompt file). The prompt walks the user through onboarding and creates the first project skeleton.
- Open the same folder in Obsidian as a vault; the bundled `.obsidian/` config opens to `wiki/index.md`

### 5.2 Core experience

- **Setup:** `verify-setup.py` runs, prints success summary
- **Onboard:** `/second-brain` walks the conversation, persists `config/second-brain.yml`, creates `wiki/workspace-projects/{first-slug}/`
- **Ingest a Confluence space:** the agent uses the API-based skill, ingests pages, compiles into wiki, prints manifest
- **Start a project:** CEO declares intent; agent chain produces VP brief → PM PRD → Architect doc (if technical) → Engineer specs; CEO reviews between stages
- **Query the wiki:** ask a question in Copilot chat; agent reads index, identifies relevant articles, synthesizes answer with citations
- **Generate vendor-truth check:** when an agent is about to cite a vendor capability, it offers to fetch the vendor doc; user opts in
- **Run align checks:** before review or publish, run `align-cite` and `align-closure` (automatic) plus optional deeper checks
- **Publish to review:** HTML output to `confluence-review/`, folder opens for inspection
- **Publish to Confluence:** API publishes new pages; user verifies in Confluence
- **Sync:** weekly reminder; user-invoked sync command refreshes in-scope spaces
- **Archive:** completed or deprecated content moves to `wiki/workspace-archives/`

### 5.3 Advanced features and edge cases

- Quarantine for failed Markdown conversions; user can inspect, fix the converter, and retry
- Cross-project dependency violations trigger a guided resolution prompt: finish dependency, archive dependency, or restate
- Stale vendor docs flagged in lint and at citation time; refetch is opt-in
- Status-aware lint avoids false alarms during draft authoring
- Override paths exist for closure and align gates at publish; overrides are logged for audit

### 5.4 UI/UX highlights

- Filesystem-first: every artifact inspectable in VS Code or Obsidian without the tool
- Obsidian compatibility: vault opens directly with frontmatter, wikilinks, Dataview, Bases support
- Conversational entry: `/second-brain` prompt is the primary user interface for onboarding and project work
- Auditability: every mutation traces to a `wiki/log.md` entry
- No silent operations: ingest, sync, publish, archive, remove all require explicit approval

---

## 6. Narrative

A CEO operator opens VS Code with the cloned `second-brain` repo as workspace and Obsidian as the vault reader. In Copilot chat, they invoke `/second-brain start-project` and describe the next initiative: replatforming the customer-data warehouse. The VP Agent works with the CEO to produce a one-page product-brief that names the project, its goals, and the constraints the CEO already knows. The CEO reviews and edits, then invokes the PM Agent. The PM Agent reads the brief, queries the wiki for in-scope standards from the Architecture, Audit, Security, and Snowflake teams, and produces a PRD with cited references. Each cited claim has a section-level link back to the original Confluence page; each vendor capability claim is annotated `(per Snowflake docs)` with a See Also link to the cached vendor doc. The CEO reviews; the PRD looks good but the Snowflake citation is from a cache that is 100 days old, beyond the 90-day TTL. The agent prompts to refetch; the user opts in; defuddle pulls the current Snowflake page; the citation refreshes. The Architect Agent proposes three architectural approaches with tradeoffs. The Engineer Agent fills in implementation specifics and runs the finalize step: body wikilinks rewritten to prose, navigation moved to See Also, status set to `review`. Lint runs `align-cite` and `align-closure` automatically; one violation surfaces (a reference to an in-progress project that does not exist yet). The agent prompts: finish that project, archive it, or restate. The CEO restates. Lint passes. The CEO runs `publish` and chooses review; the HTML preview opens; the prose is dense but jr-engineer-executable. The CEO publishes to Confluence; the agent uses the API to create new pages; the user verifies in Confluence. Two weeks later, a sync reminder fires; the user runs sync; the wiki refreshes; a new Architecture team standard is detected and integrated. The next project begins.

---

## 7. Success metrics

### 7.1 User-centric metrics

- **Adoption signal (binary, primary):** after a 4-week pilot, does the CEO operator prefer the Second Brain workflow to (Rovo + manual drafting) for at least two distinct project documentation tasks?
- **Junior-engineer executability:** a real jr engineer can execute one published project's work using only the artifact set, without follow-up questions to the CEO. Yes/No qualitative.
- **Time to first acceptable draft of a project's product-brief.md:** stopwatch on N=5 projects through the agent chain, baseline measured pre-build. Target: TBD.

### 7.2 Business metrics

- Number of projects published per month (tracked, no v1 target)
- Number of standards or recommendations referenced in published projects (tracked)
- Vendor-truth contradictions detected and corrected per month (tracked)

### 7.3 Technical metrics

- **Citation precision:** 30-claim labeled holdout; rate each cited claim 1 (supported) / 0 (not supported). Target ≥85%.
- **`align-vendor-truth` recall:** 20-claim labeled holdout where some claims contradict vendor truth; check the lint catches them. Target ≥90%.
- **`align-closure` precision:** 20-doc labeled holdout where some docs violate closure; check the lint catches them. Target ≥90%.
- **Ingestion success rate:** per ingest run, percent of pages reaching "ready" state (raw + wiki + index entry + structural lint passes). Target ≥95%.
- **Vendor doc cache hit rate:** per query session, percent of vendor lookups served from cache. Tracked, no v1 target.

---

## 8. Technical considerations

### 8.1 Integration points

- **Atlassian Cloud REST API v2** (Confluence + Jira; same tenant, single auth flow); fallback path if MCP lacks needed metadata
- **Atlassian Rovo MCP Server** (GA as of April 2026; exposes Rovo Search/fetch and product actions to AI clients via signed-in user permissions; first-choice data-layer path for build week 1; per `product-brief.md` §1.2, MCP is a connector not a governance engine; if it does not expose ADF body, version, last-modified, labels, ancestors with sufficient fidelity, fall back to the REST API path)
- **GitHub Copilot agent mode** (the LLM surface; reads `.github/copilot-instructions.md`, invokes prompts)
- **Per-agent shims** (`CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`) for cross-agent compatibility
- **Defuddle CLI** (vendor doc Markdown extraction)
- **Obsidian** (canonical reader; Bases plugin for live views; Dataview for dynamic tables)

### 8.2 Data storage and privacy

- All knowledge artifacts on local filesystem under user-controlled paths
- `.env` for secrets; never written to vault or runtime artifacts
- No telemetry, no external logging in v1
- Confluence content access governed by user's API token; no ACL bypass
- Vendor doc cache retains content for the configured TTL (90 days default; 365 day hard max)
- Quarantine artifacts retained indefinitely for audit
- Generated drafts written to `wiki/workspace-projects/{slug}/`; user is responsible for what is shared

### 8.3 Scalability and performance

- Target scale v1: 50-500 wiki articles; index-only retrieval is sufficient (per Cole's claim)
- Embeddings deferred; revisit only if wiki passes ~500 articles
- Single-file SQLite index NOT used in v1 (no embeddings; navigation is via index.md and Base views)
- Confluence ingest rate-limited by tenant policy; respect 429s with backoff
- Vendor fetch rate is low (on-demand, opt-in per claim)

### 8.4 Potential challenges

- Confluence ADF macro coverage in Markdown conversion (the user's existing skill handles this; long tail will surface during ingest)
- Cross-team relevance noise at retrieval (mitigation: project scoping and authority weighting)
- Vendor truth fetch fragility (mitigation: TTL revalidation, manual refetch)
- Hallucinated citations (mitigation: `align-cite` as gating check)
- Multi-agent workflow state management (mitigation: filesystem checkpoints between stages)
- Atlassian Enterprise auth and IP allowlisting (mitigation: README documents enterprise considerations)

---

## 9. Milestones and sequencing

### 9.1 Project estimate

- **Large:** 10-14 weeks of solo build with LLM build agent inside Copilot

### 9.2 Team size and composition

- Solo engineer (Josh) + LLM build agent (Copilot agent mode)
- No designer, QA, or PM required for v1

### 9.3 Suggested phases

- **Phase 1 (week 1-2): Foundations + ingestion spike**
  - Repo skeleton, `.env` handling, `.gitignore`, `.github/` structure
  - Per-agent shims (Copilot, Claude Code, Cursor, Windsurf)
  - `verify-setup.py`
  - Atlassian Remote MCP Server spike (validates whether MCP path is viable as an alternative)
  - Port the user's existing Confluence ingestion skill into the repo with frontmatter and layout adapted

- **Phase 2 (week 3-4): Wiki layer + compile workflow**
  - `wiki/` directory layout
  - `workspace-compile.prompt.md` and the obsidian-markdown skill integration
  - `index.md` and `log.md` formats
  - Quarantine, post-ingest manifest
  - Frontmatter schema for raw/ and wiki/ articles
  - Lint scaffold (structural checks)

- **Phase 3 (week 5-6): Query + agent chain skeleton**
  - `workspace-query.prompt.md` (index-guided)
  - Agent prompt files: `vp-agent`, `pm-agent`, `architect-agent`, `engineer-agent`, `start-project`, `finalize`
  - Project lifecycle: status, in-progress vs published vs archived
  - Cross-project dependency rules in lint

- **Phase 4 (week 7-8): Alignment + vendor truth**
  - `align-cite` (production)
  - `align-vendor-truth` (production)
  - `align-closure` (production)
  - `align-conformance` and `align-coverage` (best-effort)
  - Vendor doc fetch with defuddle and TTL handling
  - `revalidate-vendor-docs` prompt

- **Phase 5 (week 9-10): Publish + archive + obsidian-bases integration**
  - `workspace-publish.prompt.md` with review and Confluence branches
  - `workspace-prepare-for-confluence.prompt.md` (Markdown to HTML)
  - `workspace-publish-to-confluence.prompt.md` (API publish; MCP alternative)
  - `archive` and `unarchive` prompts
  - obsidian-bases skill integration; `wiki/workspace-views/` Base files

- **Phase 6 (week 11-12): Persona templates + writing exemplar + polish**
  - CEO persona template fully populated
  - Engineer, Architect, PM, Director, VP stubs (READMEs)
  - `docs/style/exemplar-published-doc.md` written
  - Adoption checklist, setup-kit, README final
  - End-to-end pilot project run

- **Phase 7 (week 13-14): Buffer**
  - ADF macro coverage long tail
  - Lint quality tuning
  - Documentation polish
  - Pilot feedback

---

## 10. User stories

### 10.1 Initialize a Second Brain instance

- ID: US-001
- Description: As the CEO, I want to initialize a Second Brain instance so that I have a working repo and credentials before any ingestion.
- Acceptance criteria:
  - `python scripts/verify-setup.py` with valid `.env` validates Confluence connectivity
  - Required directories (`raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/`) are created
  - `wiki/index.md` and `wiki/log.md` are initialized
  - Failure produces a clear error with the missing or invalid setting named

### 10.2 Onboard via /second-brain prompt

- ID: US-002
- Description: As the CEO, I want a guided onboarding conversation in Copilot chat so that I configure default in-scope sources, authority and domain mappings, and my first project.
- Acceptance criteria:
  - Invoking the `second-brain` prompt walks through default in-scope spaces with authority and domain
  - Conversation persists `config/second-brain.yml`
  - Conversation creates `wiki/workspace-projects/{first-slug}/` skeleton

### 10.3 Ingest a Confluence space

- ID: US-003
- Description: As the CEO, I want to ingest a Confluence space so that its standards become referenceable in my wiki.
- Acceptance criteria:
  - User provides a space key, page ID, page URL, or list
  - Pages land in `raw/workspace-confluence/{space-key}/pages/...` with frontmatter
  - Wiki layer compiles synchronously
  - Quarantine catches conversion failures without blocking the run
  - Post-ingest manifest reports outcome

### 10.4 Sync a Confluence space

- ID: US-004
- Description: As the CEO, I want to sync ingested spaces so that my wiki reflects upstream changes.
- Acceptance criteria:
  - Weekly reminder fires after 7 days since last sync
  - User-invoked sync runs incremental ingestion (compares version and content_hash)
  - Modified pages updated, new pages added, pages deleted upstream marked archived

### 10.5 Ingest a vendor doc on demand

- ID: US-005
- Description: As the CEO, I want vendor docs fetched only when needed so that I do not pay to ingest entire vendor doc sites.
- Acceptance criteria:
  - When the agent is about to cite a vendor capability, it offers to fetch the relevant page
  - On opt-in, defuddle extracts clean Markdown
  - Page lands in `raw/workspace-external/{vendor}/{topic}/{slug}.md` with TTL frontmatter
  - Cached pages within TTL are reused without prompting

### 10.6 Revalidate vendor docs

- ID: US-006
- Description: As the CEO, I want to refresh stale vendor docs so that my citations reflect current vendor truth.
- Acceptance criteria:
  - `revalidate-vendor-docs` prompt enumerates docs past TTL or hard max
  - User can opt to refetch in batch or per item
  - Refreshed docs replace cached versions; previous version retained in `raw/workspace-external/{vendor}/{topic}/.history/` (optional)

### 10.7 Start a new project

- ID: US-007
- Description: As the CEO, I want to declare a new project intent and have agents produce the artifact set so that I do not draft from scratch.
- Acceptance criteria:
  - `start-project` orchestrates VP → PM → Architect (if technical) → Engineer
  - CEO reviews and edits between stages
  - Each agent's output written to `wiki/workspace-projects/{slug}/0X-{stage}/`
  - Status field set on every file; defaults to `draft`

### 10.8 Run finalize step

- ID: US-008
- Description: As the CEO, I want a finalize step that converts draft body wikilinks to clean prose so that documents are review-ready.
- Acceptance criteria:
  - Engineer agent (or finalize prompt) rewrites body to remove wikilinks
  - Navigation links moved to `See Also` section
  - Status updated to `review`
  - Lint runs and reports any remaining violations

### 10.9 Run align-cite

- ID: US-009
- Description: As the CEO, I want every cited claim to resolve to a source containing that claim so that I trust my published documents.
- Acceptance criteria:
  - `align-cite` walks every citation in the active set
  - Reports each violation with the document, claim, and (apparent) source
  - Runs automatically before publish

### 10.10 Run align-vendor-truth

- ID: US-010
- Description: As the CEO, I want vendor-domain claims to cite vendor sources so that I do not propagate stale internal claims.
- Acceptance criteria:
  - `align-vendor-truth` identifies vendor-domain claims (claims about AWS, Snowflake, etc.)
  - Verifies citation source is in the matching vendor domain
  - Flags violations with suggested vendor docs to fetch

### 10.11 Run align-closure

- ID: US-011
- Description: As the CEO, I want my project's authored set to be jr-engineer-executable so that handoff is smooth.
- Acceptance criteria:
  - `align-closure` enforces status-aware rules (no body wikilinks at review or published; navigation in See Also or frontmatter)
  - Flags cross-project dependency violations (in-progress → in-progress or archived)
  - Provides resolution options (finish dependency, archive, restate)
  - Runs automatically before publish

### 10.12 Publish to review folder

- ID: US-012
- Description: As the CEO, I want to preview a draft as HTML before pushing to Confluence so that I catch rendering issues.
- Acceptance criteria:
  - `publish` prompt asks "review or Confluence?"
  - On "review": Markdown converted to HTML, written to `confluence-review/{project-slug}/{doc-slug}-{timestamp}.html`
  - Full path printed
  - Folder opened via OS-native opener

### 10.13 Publish to Confluence

- ID: US-013
- Description: As the CEO, I want to push a finalized document to Confluence as new pages so that other teams can read it.
- Acceptance criteria:
  - `publish` prompt asks "review or Confluence?"
  - On "Confluence": agent uses the user's API code to create new pages
  - Pre-publish lint (`align-cite` and `align-closure`) runs automatically
  - Publish blocks on lint violations unless overridden; overrides logged

### 10.14 Query the wiki

- ID: US-014
- Description: As the CEO, I want to ask the wiki a question and get a synthesized answer with citations so that I do not need to read everything myself.
- Acceptance criteria:
  - Agent reads `wiki/index.md` and Base views, identifies relevant articles, reads them, synthesizes
  - Answer includes section-level citations
  - Optional `--file-back` persists as `wiki/workspace-qa/` article and updates index and log
  - Project-scoped query filters to in-scope sources

### 10.15 Archive a completed project

- ID: US-015
- Description: As the CEO, I want to archive a finished project so that it stays on disk but does not clutter active search.
- Acceptance criteria:
  - `archive` prompt moves project directory to `wiki/workspace-archives/projects/{slug}/`
  - Frontmatter `archived: true` and `archived_at` set on every file
  - Excluded from default search and reference; opt-in to include
  - `unarchive` reverses

### 10.16 Run lint

- ID: US-016
- Description: As the CEO, I want a periodic health check so that the wiki does not silently degrade.
- Acceptance criteria:
  - `lint` runs all seven structural checks plus engineering additions
  - Report written to `reports/workspace-lint-{date}.md` with severity per finding
  - Status-aware closure violations included

### 10.17 Resolve cross-project dependency

- ID: US-017
- Description: As the CEO, when a project depends on another in-progress project, I want guided resolution so that my project does not stall on tangled dependencies.
- Acceptance criteria:
  - Lint or align-closure detects the violation
  - Agent presents options: finish dependency, archive dependency, restate
  - User chooses; agent assists with the chosen path

### 10.18 Configure credentials and config

- ID: US-018
- Description: As the CEO, I want credentials in `.env` and operating defaults in `config/second-brain.yml` so that I do not hardcode secrets or settings.
- Acceptance criteria:
  - `.env.example` documents every required variable
  - `config/second-brain.example.yml` documents every operating default (vendor TTL, sync cadence, in-scope spaces)
  - Missing required variables produce a startup error naming the missing variable
  - Secrets never written to vault, index, or logs

### 10.19 Verify Atlassian Remote MCP Server (build week 1 spike)

- ID: US-019
- Description: As the engineer building Second Brain, I want to validate whether the Atlassian Remote MCP Server is a viable alternative to the API-based ingestion path so that the documented alternative actually works.
- Acceptance criteria:
  - In build week 1, run a 5-page test ingestion via the MCP server against the user's tenant
  - Document outcome (works cleanly, has gaps, fails)
  - If viable: document the MCP path in AGENTS.md as the alternative
  - If not viable: document why and remove from v1 scope (v1.x reconsideration)

### 10.20 Adopt the kit on a new machine

- ID: US-020
- Description: As an alternative operator (or the CEO on a new machine), I want a clear setup checklist so that I can adopt the kit quickly.
- Acceptance criteria:
  - `docs/setup-kit.md` documents the steps
  - `docs/adoption-checklist.md` provides a quick checklist
  - First-time setup completes in under 30 minutes assuming Atlassian credentials are available
