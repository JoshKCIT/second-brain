# CEO Persona Template (v1, populated)

This is the populated persona template for the CEO operator. Used as the default persona when a new user clones the repo and runs `/second-brain` onboarding.

## Operating mode

The CEO is the literal operator: runs prompts, edits drafts, approves transitions. Tone of all prompts targeting the CEO is direct, terse, technical. The CEO is also the final reviewer at every agent-chain stage.

## Default in-scope source preferences

When onboarding a CEO operator, the `/second-brain` prompt suggests these spaces by default (the user can edit):

| Space | Authority | Domain | Why for CEO |
|---|---|---|---|
| Strategy | standard | internal | Strategic decisions and OKR context |
| Architecture | standard | internal | Cross-cutting tech decisions |
| Security | standard | internal | Compliance and risk posture |
| Audit | standard | internal | Regulatory and audit obligations |
| Product | recommendation | internal | Product team direction and roadmaps |
| Engineering Leadership | recommendation | internal | Engineering team commitments |
| Board materials | informational | internal | Board context (separate space if your org has one) |

## Common CEO project doc types

The agent chain produces these by default for CEO-driven projects:

- **Strategic initiative brief** (VP Agent) — the WHAT and WHY of a new initiative
- **Product or program PRD** (PM Agent) — translates strategy into shippable requirements
- **Architectural approaches** (Architect Agent, when technical) — option comparison for cross-cutting tech decisions
- **Implementation specs** (Engineer Agent) — handoff to teams that will execute

Other doc types the CEO may directly request via `/workspace-query` and `/file-back`:

- Decision rationale documents
- Stakeholder briefings
- Strategy memos
- Capability inventories across teams
- Status syntheses across active projects

## Example workflows

### Workflow A: Cross-functional initiative

1. CEO declares: "We need to migrate from on-prem data warehouse to Snowflake."
2. `/workspace-start-project` orchestrates VP → PM → Architect → Engineer
3. Architect Agent's vendor-truth check pulls fresh Snowflake docs to validate capability claims
4. Final published artifact set goes to Confluence as new pages under the project's chosen space

### Workflow B: Strategy synthesis

1. CEO needs to understand current Security team commitments before a board meeting
2. `/workspace-query "What are our current Security team commitments around data encryption and access control?" --file-back`
3. Agent reads in-scope Security wiki articles, synthesizes, files the answer as a `wiki/workspace-qa/` article
4. CEO uses the synthesis directly in the board prep doc

### Workflow C: Vendor commitment audit

1. CEO needs to know which of our published architectural decisions assume vendor capabilities that have changed
2. `/workspace-lint` flags stale vendor docs (past TTL); `/revalidate-vendor-docs` refreshes; `/workspace-align-vendor-truth` runs against active project artifacts
3. Surface contradictions to the relevant team owners

## Schema additions for CEO persona

None. The CEO uses the standard AGENTS.md schema. Per-persona schema additions would land in `templates/personas/ceo/AGENTS-additions.md` if needed; v1 has none.

## Starter wiki content

For a fresh CEO instance, the starter wiki may include:

- A `wiki/workspace-concepts/` article on the org's strategic priorities (user-edited)
- A `wiki/workspace-standards/strategy/` directory pre-seeded after the first ingest of the Strategy space
- A `wiki/workspace-projects/` placeholder for the first project

These are not pre-shipped; they emerge from the user's own ingestion and project work.
