---
title: "Getting started"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "README.md"
  - "docs/platform-support-documentation/user-guide/adoption-checklist.md"
  - ".github/prompts/second-brain.prompt.md"
  - "scripts/verify-setup.py"
---

# Getting started

This is the **canonical install and first-run walkthrough** for Second Brain (v2). Target: complete setup in under 30 minutes with Atlassian credentials available. Vendor-only setup (no Confluence) is supported via defuddle and public doc URLs.

Build phase note: platform foundation and Phases 1A–2 (vendor cache + wiki compile) are complete. **Phase 3** (query + agent chain) is the active workspace track. Phase 1B (Confluence ingest) remains blocked until Atlassian access. See [docs/product/roadmap.md](../../product/roadmap.md) and [docs/product/vendor-catalog.md](../../product/vendor-catalog.md).

## Prerequisites

Install before cloning:

| Tool | Purpose |
|------|---------|
| Git | Clone and version the repo |
| Python 3.12+ | `verify-setup.py`, ingest/compile scripts |
| Node.js + `defuddle` | Vendor doc fetch: `npm install -g defuddle` |
| VS Code, Cursor, Claude Code, or Windsurf | AI agent host |
| Obsidian (optional) | Browse `wiki/index.md` as a vault |
| Atlassian API token or OAuth (optional) | Confluence ingest — skip for vendor-only demo |

Supported OS: Windows, macOS, Linux.

### Config file overview

`config/second-brain.yml` (gitignored) stores:

- Default in-scope Confluence spaces with **authority** (standard / recommendation / informational) and **domain** (internal / vendor / industry)
- Vendor revalidation TTL overrides
- Confluence sync cadence reminders

Never commit secrets or personal scope to git — only `*.example.yml` files are tracked.

### Build phase expectations

Phases 1A–2 are complete (vendor caches, compile workflow, Base views). Phase 3 adds the agent chain and first real projects. Confluence ingest (Phase 1B) requires Atlassian credentials when your tenant is ready. Current status: [docs/product/roadmap.md](../../product/roadmap.md).

## Credentials

Clone and configure secrets:

```bash
git clone <repo-url> second-brain
cd second-brain
cp .env.example .env
cp config/second-brain.example.yml config/second-brain.yml
```

Open `.env` and fill in:

- `ATLASSIAN_SITE_URL` — e.g. `https://yourcompany.atlassian.net` (no trailing slash)
- `ATLASSIAN_EMAIL` — your account email
- `ATLASSIAN_API_TOKEN` — from Atlassian security settings

If your tenant requires OAuth instead of personal tokens, fill OAuth fields and leave the API token blank. OAuth respects SSO; personal tokens may not work with Atlassian Guard.

Copy RSS config if you plan to use the RSS lane:

```bash
cp config/rss-feeds.example.yml config/rss-feeds.yml
```

## Verify setup

```bash
python scripts/verify-setup.py
```

This script:

- Validates `.env` and tests Atlassian connectivity (when configured)
- Creates runtime directories: `raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/`
- Initializes `wiki/index.md` and `wiki/log.md` if missing
- Runs unit tests (non-blocking warnings may appear)

**Common verify failures:**

- **Auth fails** — refresh API token; remove trailing slash from site URL; try OAuth if SSO is required
- **IP allowlisted** — confirm with Atlassian admin
- **Audit logging** — Enterprise Cloud logs API calls; notify security before large ingests

Optional vendor demo without Confluence:

```bash
python scripts/seed-vendor-docs.py --yes
python scripts/compile-workspace-external.py
```

Compile still requires explicit approval (RC-146) when writing to `wiki/`.

## IDE open

### VS Code (primary v1 surface)

```bash
code .
```

Enable GitHub Copilot agent mode with a current Claude or GPT model. Copilot reads [.github/copilot-instructions.md](../../../.github/copilot-instructions.md) automatically.

### Obsidian

Open Obsidian → "Open another vault" → select the `second-brain` folder. Bundled `.obsidian/` opens to `wiki/index.md` (empty until first compile).

```text
Repo folder  →  IDE (agent chat)  +  Obsidian (wiki browse)
```

## Onboarding

In your agent chat, invoke:

```text
/second-brain
```

If slash commands are not discovered, open [.github/prompts/second-brain.prompt.md](../../../.github/prompts/second-brain.prompt.md) manually.

Onboarding walks you through:

1. Confirming Atlassian tenant (from `.env`)
2. Listing default in-scope Confluence spaces with authority and domain mappings
3. Persisting choices to `config/second-brain.yml`
4. Optionally starting first ingest or project

Lane reminder: use `workspace-*` commands for everyday work; `platform-*` only when improving Second Brain itself.

## First ingest

If onboarding did not run ingest:

```text
/workspace-ingest-confluence
```

Provide a Confluence space key, page URL, or page ID list. The agent fetches to `raw/workspace-confluence/`. **Compile to wiki requires separate approval** — see [workflow-ingest.md](workflow-ingest.md).

Vendor-only ingest:

```text
/workspace-ingest-vendor-doc
```

## First project

```text
/workspace-start-project
```

Declare project intent. The orchestrator runs VP → PM → Architect (if technical) → Engineer. You review and edit between stages. See [workflow-project-chain.md](workflow-project-chain.md).

Track progress with [adoption-checklist.md](adoption-checklist.md) and [first-week-checklist.md](first-week-checklist.md).

## Per-agent IDE

| IDE | Config read automatically |
|-----|---------------------------|
| **GitHub Copilot (VS Code)** | `.github/copilot-instructions.md` |
| **Claude Code** | `CLAUDE.md`, `AGENTS.md` |
| **Cursor** | `.cursor/rules/agents.mdc` |
| **Windsurf** | `.windsurfrules` |

Details: [using-your-ide.md](../operator-guide/using-your-ide.md).

Claude Code auth uses subscription credentials in `~/.claude/.credentials.json`. Cursor and Windsurf shims are provided; report issues if behavior diverges from Copilot.

### Instruction stack reminder

Every IDE ultimately defers to three tiers: `AGENTS.md` (Tier 1), lane prompts (Tier 2), and optional project files (Tier 3). IDE shims only add invocation hints — they cannot override approval gates or compile rules. If an agent claims a shim overrides RC-146, reject the action.

### Obsidian alongside IDE

Obsidian is not an agent host — use it to browse `wiki/index.md`, follow wikilinks at draft status, and read published project artifacts. Authoring happens in IDE agent chat; Obsidian is the reader view.

When setup completes, run `/workspace-lint` and browse `wiki/index.md`. Read [how-second-brain-works.md](how-second-brain-works.md) if you skipped the mental model.

## See Also

- [how-second-brain-works.md](how-second-brain-works.md)
- [first-week-checklist.md](first-week-checklist.md)
- [workflow-ingest.md](workflow-ingest.md)
- [everyday-workflows.md](everyday-workflows.md)
- [troubleshooting.md](troubleshooting.md)
- [AGENTS.md](../../../AGENTS.md)

## Sources consulted

- README.md, user-guide/adoption-checklist.md, second-brain.prompt.md, scripts/verify-setup.py
