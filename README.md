# Second Brain

**Second Brain is a folder on your computer that an AI assistant helps you organize.** You pull in public vendor docs (from AWS, Snowflake, etc.) — and, if you have it, company docs from Confluence — the AI turns them into a searchable wiki, and then helps you write new project documents that cite the right sources.

**Start with the vendor path.** It needs no company credentials and works the moment you finish setup: point the AI at public AWS/Snowflake/etc. docs and it builds a cited wiki you can query and write from. Confluence ingest is an optional add-on that requires Atlassian access — layer it in later.

You do not need to be a developer to use it. You do need to install a few free tools — **full walkthrough:** [How it works](docs/platform-support-documentation/user-guide/how-second-brain-works.md) → [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) (or start at the [platform support documentation](docs/platform-support-documentation/README.md) index).

---

## What you will actually do

1. **Download** this repo to your laptop.
2. **Open it** in VS Code (or Cursor) with an AI assistant turned on.
3. **Ask the AI to ingest public vendor docs** (AWS, Snowflake, …) — no credentials needed. This is the fastest way to see it work.
4. **Ask the AI** to answer questions or start a new project (product brief → requirements → specs).
5. **Optionally connect** your Atlassian account later so the AI can also pull Confluence pages.
6. **Read the results** in Obsidian (a free note-taking app) or in VS Code.

The AI does the heavy lifting. Your job is to review what it produces and say yes or no before anything important gets saved or published.

---

## What you need before you start

Install Git, Python 3.12+, Node.js, and an AI-capable IDE (VS Code, Cursor, Claude Code, or Windsurf) before cloning. Obsidian is optional but recommended for browsing the wiki. Atlassian credentials are only needed for Confluence ingest.

Full prerequisites table, install links, and timing: [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) in the platform support manual.

---

## Setup

**Install and first-run walkthrough:** [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) in the platform support manual (target: under 30 minutes).

Quick sanity check after clone:

```bash
cp .env.example .env          # or copy on Windows
cp config/second-brain.example.yml config/second-brain.yml
pip install -r requirements.txt   # installs the two Python deps (feedparser, pyyaml)
python scripts/verify-setup.py
```

Then open the repo in your IDE, optional Obsidian vault on the same folder, and invoke `/second-brain` in chat.

---

## Start here: the vendor path (no Confluence needed)

The fastest, lowest-friction way to see Second Brain work — and the recommended
first run — uses **public vendor documentation only**: no Atlassian account, no
company credentials. Populate the wiki from AWS/Snowflake/etc. docs, then query
and write from it. See the vendor demo in [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) (Verify setup section). Add Confluence ingest once the vendor path feels comfortable.

---

## Everyday commands

Type slash commands in your AI chat; prompts live in `.github/prompts/`. Most common:

| You want to… | Type this |
|--------------|-----------|
| Get oriented / change settings | `/second-brain` |
| Pull a public vendor doc (no credentials) | `/workspace-ingest-vendor-doc` |
| Ask a question about the wiki | `/workspace-query` |
| Start a new project doc set | `/workspace-start-project` |
| Pull Confluence pages (needs Atlassian) | `/workspace-ingest-confluence` |

Full verb list, approval gates, and workflow deep-dives: [Everyday workflows](docs/platform-support-documentation/user-guide/everyday-workflows.md) and [verb reference](docs/platform-support-documentation/operator-guide/verb-reference.md).

---

## Where things live (simple map)

Think of three layers:

```
raw/     = Source copies (Confluence pages, vendor PDFs/web pages). Treat as read-only evidence.
wiki/    = Organized knowledge the AI maintains. This is what you read and search.
AGENTS.md = Rulebook the AI reads so it behaves consistently.
```

**Everyday work** uses `workspace-*` paths (e.g. `wiki/workspace-standards/`, `wiki/workspace-projects/`). **Improving Second Brain itself** uses `platform-*` paths — ignore unless you are working on the product.

| Folder | Purpose |
|--------|---------|
| `config/` | Your settings (`second-brain.yml` — local, not in git) |
| `docs/` | Product canon, support manual, build history |
| `.github/prompts/` | All the `/command` prompts the AI uses |

Deeper map (lanes, lifecycles, gitignored content): [How Second Brain works](docs/platform-support-documentation/user-guide/how-second-brain-works.md) and [architecture map](docs/platform-support-documentation/engineer-reference/architecture-map.md).

---

## Which AI tool should I use?

This repo works with GitHub Copilot (VS Code), Cursor, Claude Code, and Windsurf. You do **not** need a separate OpenAI or Anthropic API key for normal use — your editor's AI subscription is enough.

Per-IDE setup and shim files: [Using your IDE](docs/platform-support-documentation/operator-guide/using-your-ide.md).

---

## Troubleshooting

| Problem | What to try |
|---------|-------------|
| AI ignores `/commands` | Open the matching file in `.github/prompts/` manually and run it as a prompt |
| Empty wiki after ingest | Check `wiki/log.md` for errors; look in `quarantine/` for failed pages |
| "Stale vendor doc" warning | AI will offer to refetch; say yes, or run `/workspace-ingest-vendor-doc` |
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
| Understand the system, then install | [How it works](docs/platform-support-documentation/user-guide/how-second-brain-works.md) → [Getting started](docs/platform-support-documentation/user-guide/getting-started.md) |
| Printable setup / adoption checkboxes | [Adoption checklist](docs/platform-support-documentation/user-guide/adoption-checklist.md) |
| Daily operator / verb lookup | [Everyday workflows](docs/platform-support-documentation/user-guide/everyday-workflows.md) or [verb reference](docs/platform-support-documentation/operator-guide/verb-reference.md) |
| CEO approval and governance | [CEO approval guide](docs/platform-support-documentation/operator-guide/ceo-approval-guide.md) |
| Engineer / contributor | [Architecture map](docs/platform-support-documentation/engineer-reference/architecture-map.md) |
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
