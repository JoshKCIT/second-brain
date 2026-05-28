# Second Brain

A personal, LLM-maintained knowledge base and documentation production system that runs inside VS Code with GitHub Copilot. Ingests organizational documentation from Confluence (and on-demand vendor docs from public sources) into a local Markdown wiki, and orchestrates a chain of specialized agents to produce new project documentation that is grounded in canonical sources and executable by a junior engineer.

## What problem this solves

You join a project at a large company. The relevant standards live across multiple teams' Confluence spaces (Architecture, Security, Audit, Snowflake, Data Modeling, etc.). New documentation must align with what those teams have published.

As of April 2026, generic AI tools cover much of the surrounding workflow. Atlassian Intelligence (Rovo) ships Search, Chat, Agents, Studio, Canvas, MCP server, and Rovo Dev in VS Code. Glean has multi-step agents with branches and memory. Microsoft Copilot for M365 has GA multi-step app actions and admin-designated authoritative SharePoint sites. Notion AI supports page templates via API/MCP. Sourcegraph Cody covers IDE-integrated codebase chat.

Second Brain does not compete with those on generic capabilities. It targets the **governance-and-closure** band that none of them productize:

- Source authority + domain tagging with claim-level conflict resolution (vendor-vs-internal arbitration)
- Vendor truth validation with TTL-cached vendor docs and revalidation
- Junior-engineer-executable closure rule (published artifact set must be self-sufficient)
- Multi-page stage-gated technical-doc generation with Confluence-storage-format output
- Mandatory section-level citation discipline across multi-page artifacts
- Inspectable retrieval enforced before generation as policy
- Project artifact lifecycle (in-progress / published / archived) with cross-project dependency rules

Second Brain produces new documentation by:

1. Pulling canonical content from in-scope sources (you configure the spaces and authority levels)
2. Tagging every source by authority (standard, recommendation, informational) and domain (internal, vendor:aws, etc.) so vendor capability claims are validated against vendor docs, not stale internal claims
3. Running a chain of specialized agents (VP, PM, Architect, Engineer) to produce a project artifact set
4. Enforcing a closure rule: published artifacts must be executable by a jr engineer using only the artifact set

## Architecture in three sentences

Three layers: `raw/` is the immutable source mirror (Confluence pages, vendor docs, and product-intelligence transcripts); `wiki/` is the LLM-curated knowledge layer organized by article type and authority; `AGENTS.md` is the operating spec the LLM reads. Operations: ingest (Confluence pages, vendor docs on demand), compile (raw → wiki), query (index-guided), platform-research-review (transcripts to grounded claim records), align (5 verification levels), publish (review-folder HTML or Confluence pages), archive. The pattern combines Karpathy's wiki model with Cole's compiler refinements, adapted for engineering documentation.

## Two Lanes

Second Brain uses explicit path prefixes so occasional contributors can tell what a file is for:

- `workspace-*` means everyday use of Second Brain for company/project work. Examples: `raw/workspace-confluence/`, `wiki/workspace-standards/`, `.github/prompts/workspace-query.prompt.md`.
- `platform-*` means work on Second Brain itself. Examples: `raw/platform-transcripts/`, `wiki/platform-research/`, `.cursor/agents/platform-transcript-librarian.md`, `.cursor/agents/platform-research-reviewer.md`.

If the task is "use Second Brain to ingest, query, generate, align, publish, or archive work docs," use the workspace lane. If the task is "make Second Brain better," use the platform lane.

## Quick start

```bash
# 1. Clone
git clone <repo-url>
cd second-brain

# 2. Configure
cp .env.example .env
# Edit .env with your Atlassian Cloud credentials (email + API token, or OAuth)

# 3. Verify
python scripts/verify-setup.py

# 4. Open in VS Code
code .

# 5. Open the same folder in Obsidian (the bundled .obsidian/ config opens to wiki/index.md)

# 6. In Copilot chat, run the onboarding prompt
# Type or invoke: /second-brain
# (or open .github/prompts/second-brain.prompt.md and run as prompt file)
```

The onboarding conversation walks you through default in-scope Confluence spaces with authority and domain mappings, naming conventions, and your first project setup.

## Supported agents

The repo ships with operating instructions readable by any AI coding agent. Per-agent shim files live in their conventional locations and reference `AGENTS.md` for full content.

| Agent | Shim location | Tested |
|---|---|---|
| GitHub Copilot (VS Code) | `.github/copilot-instructions.md` | Yes (primary v1 surface) |
| Claude Code | `CLAUDE.md` | Reads AGENTS.md natively |
| Cursor | `.cursor/rules/agents.mdc` | Speculative; please open an issue if behavior diverges |
| Windsurf | `.windsurfrules` | Speculative; please open an issue if behavior diverges |
| OpenAI Codex CLI | `AGENTS.md` (read directly) | Reads AGENTS.md natively |

Verify your agent's prompt-file invocation behavior; conventions in this space shift quarterly.

## Optional convenience plugins

Not required. Add only when your own friction triggers them.

| Plugin | When useful |
|---|---|
| obsidian-visualizer (VS Code extension) | If you constantly switch to Obsidian just to see graph view |
| Open in VS Code (Obsidian plugin) | If you frequently start in Obsidian and want a one-click jump to VS Code |
| Obsidian MD for VSCode (willasm extension) | If quick-capture from VS Code into a daily log emerges as a recurring need |

Avoid: Foam and Dendron (alternatives to Obsidian, not complements; conflict with this repo's conventions).

## Repo layout (high level)

```
README.md                 You are here
AGENTS.md                 Canonical operating spec for any agent
.github/                  Copilot shim, lane-labeled prompts, agent skills
CLAUDE.md, .cursor/, .windsurfrules   Per-agent shims
docs/                     Brief, PRD, architecture rationale, roadmap, setup kit, writing-style exemplar
config/                   second-brain.example.yml; user's local config gitignored
templates/personas/       CEO populated in v1; Engineer/Architect/PM/Director/VP stubs for v1.x
raw/workspace-*           Everyday source mirror (gitignored content)
raw/platform-*            Second Brain platform research sources (gitignored content)
wiki/workspace-*          Everyday curated knowledge layer (gitignored content)
wiki/platform-*           Second Brain platform research outputs (gitignored content)
confluence-review/        Local HTML preview output (gitignored)
quarantine/               Failed conversion artifacts (gitignored)
reports/                  Lint and platform-research-review reports (gitignored)
reference-documents/      Manual drops of external standards or specs
.obsidian/                Bundled vault config defaults
scripts/                  verify-setup.py and minimal helpers (most operations are LLM-driven)
```

## Optional Platform Research Review

Use `/platform-transcript-librarian` to import transcripts, sync the queue register, and process reviews (stops for your input before writing `raw/**`). Use `/platform-research-review` when transcripts, interviews, meeting notes, or product ideas discuss how to improve Second Brain. The workflow extracts atomic claims, grounds them against `AGENTS.md`, `product-brief.md`, `PRD.md`, and related docs, then writes claim records and impact reports under `wiki/platform-research/` and `reports/platform-research-review/`.

Research review is intentionally not a compile path: transcripts can influence draft ADRs and experiments, but they do not directly become canonical standards, roadmap items, or product requirements.

## Documentation map

| Document | Purpose |
|---|---|
| `product-brief.md` | Why this exists, who it serves, scope, constraints |
| `PRD.md` | What v1 builds, functional requirements, user stories, milestones |
| `AGENTS.md` | How any agent operates the system |
| `docs/architecture-rationale.md` | Design decisions and tradeoffs |
| `docs/roadmap.md` | Phase sequencing for v1 |
| `docs/setup-kit.md` | Step-by-step adoption guide |
| `docs/adoption-checklist.md` | Quick first-run checklist |
| `docs/platform-intelligence/platform-research-review-setup.md` | Optional transcript-to-claim review workflow |
| `docs/style/exemplar-published-doc.md` | Writing-quality target for authored artifacts |

## Enterprise considerations

If you are on Atlassian Cloud Enterprise tier:

- Personal API tokens may be disabled by your tenant policy. The `.env` accepts both API-token and OAuth credentials; configure whichever your tenant allows.
- IP allowlisting may block your local machine. Confirm with your Atlassian admin before first ingest.
- Atlassian Guard / SSO policies may require OAuth rather than personal tokens.
- Audit logs will capture every API call. Recommended: heads-up to IT before first ingest of large spaces.

## Constraints (current)

- Single-user local. v1 does not support shared wikis. Each user clones and runs their own instance.
- Confluence Cloud Enterprise is the v1 source. Server, Data Center, SharePoint, OneNote, Jira are deferred to v1.x.
- LLM access via GitHub Copilot agent mode. No separate Anthropic API key required.

## License

`[NEEDS DECISION — MIT, Apache 2.0, or other? Default proposal: MIT for maximum adoption.]`

## Contribution model

`[NEEDS DECISION — accept community PRs from the start, or yours-only initially? Default proposal: yours-only for v1; consider community contributions in v1.x once the core stabilizes.]`

## Status

v1 in build: **Phases 1A–2 complete** — vendor wiki (14 concepts, 4 Base views, lint-clean). **Phase 3 active.** Confluence deferred (Phase 1B). See `docs/phase-2-exit-report.md` and `docs/roadmap.md`.
