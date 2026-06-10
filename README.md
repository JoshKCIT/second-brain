# Second Brain

**Second Brain is a folder on your computer that an AI assistant helps you organize.** You pull in company docs (from Confluence) and public vendor docs (from AWS, Snowflake, etc.), the AI turns them into a searchable wiki, and then helps you write new project documents that cite the right sources.

You do not need to be a developer to use it. You do need to install a few free tools — **full walkthrough:** [Platform support documentation](docs/platform-support-documentation/README.md) → [Getting started](docs/platform-support-documentation/user-guide/getting-started.md).

---

## What you will actually do

1. **Download** this repo to your laptop.
2. **Open it** in VS Code (or Cursor) with an AI assistant turned on.
3. **Optionally connect** your Atlassian account so the AI can pull Confluence pages.
4. **Ask the AI** to ingest docs, answer questions, or start a new project (product brief → requirements → specs).
5. **Read the results** in Obsidian (a free note-taking app) or in VS Code.

The AI does the heavy lifting. Your job is to review what it produces and say yes or no before anything important gets saved or published.

---

## What you need before you start

Install these first. All are free except GitHub Copilot (your company may already provide it).

| Tool | Why you need it | Get it |
|------|-----------------|--------|
| **Git** | Download the repo | [git-scm.com](https://git-scm.com/) |
| **Python 3.12+** | Runs the setup checker | [python.org](https://www.python.org/downloads/) — on Windows, check “Add Python to PATH” |
| **Node.js** | Installs `defuddle` (fetches vendor web pages) | [nodejs.org](https://nodejs.org/) |
| **VS Code** or **Cursor** | Where you chat with the AI | [code.visualstudio.com](https://code.visualstudio.com/) or [cursor.com](https://cursor.com/) |
| **AI assistant** | Copilot, Claude Code, or Cursor Agent | Copilot extension in VS Code, or built into Cursor |
| **Obsidian** | Nice way to browse the wiki (optional but recommended) | [obsidian.md](https://obsidian.md/) |
| **Atlassian account** | Only if you want Confluence ingest | Your work login + API token |

**Time:** About 20–30 minutes for first setup if nothing goes wrong.

---

## Setup

**Install and first-run walkthrough:** [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) in the platform support manual (target: under 30 minutes).

Quick sanity check after clone:

```bash
cp .env.example .env          # or copy on Windows
cp config/second-brain.example.yml config/second-brain.yml
python scripts/verify-setup.py
```

Then open the repo in your IDE, optional Obsidian vault on the same folder, and invoke `/second-brain` in chat.

---

## Try it without Confluence (vendor demo)

If you do not have Confluence access yet, you can still populate the wiki with public vendor documentation:

```bash
python scripts/seed-vendor-docs.py --yes
python scripts/compile-workspace-external.py
python scripts/lint-workspace.py
```

Then open `wiki/index.md` in Obsidian. You should see concept articles about AWS, Snowflake, etc.

Ask the AI:

```
/workspace-query What does our cached Snowflake documentation say about data types?
```

---

## Everyday commands (plain English)

Type these in your AI chat. They match files in `.github/prompts/`.

| You want to… | Type this | What happens |
|--------------|-----------|--------------|
| Get oriented / change settings | `/second-brain` | Onboarding and config help |
| Pull Confluence pages | `/workspace-ingest-confluence` | Copies pages into `raw/`, updates wiki |
| Ask a question about the wiki | `/workspace-query` | AI reads the index and answers with sources |
| Start a new project doc set | `/workspace-start-project` | Runs VP → PM → Architect → Engineer chain |
| Check doc quality before publish | `/workspace-align-cite` | Verifies citations match sources |
| Preview docs as HTML | `/workspace-publish` | Creates files in `confluence-review/` |
| Health check on the wiki | `/workspace-lint` | Report in `reports/` |

**New project flow (simple version):**

1. `/workspace-start-project` — describe your project in plain language.
2. Review each stage (brief → requirements → architecture → engineering). Edit if needed; tell the AI when to continue.
3. Before publishing, run align checks the AI suggests.
4. `/workspace-publish` when you are happy with the output.

Detailed checklists: [adoption-checklist](docs/platform-support-documentation/user-guide/adoption-checklist.md) and [getting-started](docs/platform-support-documentation/user-guide/getting-started.md) in the platform support manual.

---

## Where things live (simple map)

Think of three layers:

```
raw/     = Source copies (Confluence pages, vendor PDFs/web pages). Treat as read-only evidence.
wiki/    = Organized knowledge the AI maintains. This is what you read and search.
AGENTS.md = Rulebook the AI reads so it behaves consistently.
```

**Everyday work** uses paths starting with `workspace-` (e.g. `wiki/workspace-standards/`, `wiki/workspace-projects/`).

**Improving Second Brain itself** uses `platform-` paths (transcripts, research). Ignore these unless you are working on the product.

Other folders you might see:

| Folder | Purpose |
|--------|---------|
| `config/` | Your settings (`second-brain.yml` — local, not in git) |
| `docs/` | Product canon, support manual, build history, maintainer log |
| `templates/` | Starting templates for projects and research |
| `reports/` | Lint and review reports the AI generates |
| `confluence-review/` | HTML previews before you publish to Confluence |
| `.github/prompts/` | All the `/command` prompts the AI uses |

Content in most of `raw/` (Confluence, Jira, transcripts), `wiki/`, and `reports/` is usually **not committed to git** — it lives on your machine. Exception: **`raw/workspace-external/`** vendor doc caches are tracked so engineers share the same vendor truth layer.

---

## Which AI tool should I use?

This repo works with several AI coding assistants. Pick one:

| Tool | How it loads instructions |
|------|---------------------------|
| **GitHub Copilot** (VS Code) | `.github/copilot-instructions.md` + prompt files |
| **Cursor** | `.cursor/rules/agents.mdc` + prompt files |
| **Claude Code** | `CLAUDE.md` + `AGENTS.md` |
| **Windsurf** | `.windsurfrules` + `AGENTS.md` |

You do **not** need a separate OpenAI or Anthropic API key for normal use — your editor’s AI subscription is enough.

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| AI ignores `/commands` | Open the matching file in `.github/prompts/` manually and run it as a prompt |
| Empty wiki after ingest | Check `wiki/log.md` for errors; look in `quarantine/` for failed pages |
| “Stale vendor doc” warning | AI will offer to refetch; say yes, or run `/workspace-ingest-vendor-doc` |
| AI wants to edit something you did not ask for | Say no — important changes need your approval by design |
| Company blocks API tokens | Use OAuth fields in `.env` instead; ask IT about IP allowlists |

More detail: [getting-started](docs/platform-support-documentation/user-guide/getting-started.md) and [troubleshooting](docs/platform-support-documentation/user-guide/troubleshooting.md).

---

## Why Second Brain? (short version)

Large companies scatter standards across many Confluence spaces. Generic AI chat can summarize pages, but it does not enforce **which source wins** when internal docs disagree with AWS, or whether your published spec is complete enough for a junior engineer to execute without guessing.

Second Brain is built for that **governance and closure** layer: tagged sources, citation checks, vendor doc freshness, and staged project artifacts. It is not trying to replace Confluence search or Microsoft Copilot for everyday Q&A.

Deep dive: `product-brief.md` and `PRD.md`.

---

## Optional: platform research lane

Only if you are improving Second Brain itself (reviewing transcripts, scoring product ideas):

- `/platform-transcript-librarian` — import and queue transcripts
- `/platform-research-review` — extract and score claims
- `/platform-implement-backlog` — implement approved changes one at a time

Setup: `docs/platform-intelligence/platform-research-review-setup.md`.

---

## Which doc should I read?

| Your goal | Start here |
|-----------|------------|
| Install, first ingest, first project | [Platform support documentation](docs/platform-support-documentation/README.md) → [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) |
| Printable setup / adoption checkboxes | [Adoption checklist](docs/platform-support-documentation/user-guide/adoption-checklist.md) |
| Product direction, phases, architecture | [docs/product/](docs/product/README.md) (roadmap, architecture rationale, vendor catalog) |
| Historical phase exit reports | [docs/build-history/](docs/build-history/README.md) |
| Maintainer changelog | [docs/progress-log.md](docs/progress-log.md) |
| Full agent rulebook | [AGENTS.md](AGENTS.md) |

---

## Documentation map

Three tiers — support manual (operators), product canon (direction), build history (audit trail):

| Tier | Path | Contents |
|------|------|----------|
| **Support manual** | [`docs/platform-support-documentation/`](docs/platform-support-documentation/README.md) | User, operator, and engineer guides — **start here** for install and workflows |
| **Product canon** | [`docs/product/`](docs/product/README.md) | Roadmap, architecture rationale, vendor catalog |
| **Build history** | [`docs/build-history/`](docs/build-history/README.md) | Phase plans and exit reports (Phases 1A–2) |
| **Maintainer log** | [`docs/progress-log.md`](docs/progress-log.md) | Chronological build notes |
| **Root specs** | [`PRD.md`](PRD.md), [`product-brief.md`](product-brief.md) | Product requirements and brief |

| Also useful | |
|-------------|--|
| [`scripts/README.md`](scripts/README.md) | Helper scripts reference |
| [`docs/platform-intelligence/`](docs/platform-intelligence/platform-research-review-setup.md) | Platform research lane setup |

---

## Enterprise notes

- Some tenants disable personal API tokens — use OAuth in `.env`.
- Large ingests may show up in Atlassian audit logs; tell IT before bulk pulls.
- v1 is **single-user local**: each person clones their own copy; there is no shared cloud wiki yet.

---

## Status

**Phases 1A–2 complete** — vendor wiki, lint tooling, agent prompts. **Phase 3 active** — agent chain and first projects. See [docs/product/roadmap.md](docs/product/roadmap.md).

---

## License

License TBD (MIT proposed). See repository settings for current license file.
