---
title: "Adoption checklist"
audience: user
generated: true
last_sync: 2026-06-09T00:00:00Z
status: published
sources:
  - "docs/product/roadmap.md"
  - ".github/prompts/second-brain.prompt.md"
  - "scripts/verify-setup.py"
---

# Adoption checklist

Printable checkbox path for first-time setup. **Detailed walkthrough:** [getting-started.md](getting-started.md). **Week-one narrative:** [first-week-checklist.md](first-week-checklist.md). Target: complete in under 30 minutes.

**Note:** This checklist is for operators adopting the repo (setup, first project, ongoing rhythm). Current platform build phase: see [docs/product/roadmap.md](../../product/roadmap.md) (Phase 3 active as of 2026-06-09; Phases 1A–2 complete).

## Prerequisites checklist

- [ ] VS Code installed
- [ ] GitHub Copilot extension installed and authenticated (or Claude Code, Cursor, or Windsurf)
- [ ] Obsidian installed (free download from obsidian.md)
- [ ] Python 3.12+ available
- [ ] `defuddle` CLI installed: `npm install -g defuddle`
- [ ] Git installed
- [ ] Atlassian Cloud account with API token OR OAuth credentials
- [ ] Read access to the Confluence spaces you plan to ingest

## Setup checklist

- [ ] Cloned the repo: `git clone <url> second-brain && cd second-brain`
- [ ] Copied `.env.example` to `.env`
- [ ] Filled `.env` with Atlassian credentials (URL, email, API token or OAuth)
- [ ] Ran `python scripts/verify-setup.py`; all checks passed
- [ ] Opened the repo in VS Code
- [ ] Opened the same folder as a vault in Obsidian
- [ ] Invoked `/second-brain` in Copilot chat for onboarding
- [ ] Configured at least one default in-scope Confluence space with authority and domain
- [ ] `config/second-brain.yml` saved and reviewed
- [ ] Ran first ingest of a small Confluence space (10-20 pages recommended)
- [ ] Verified `wiki/index.md` populated in Obsidian
- [ ] Ran `/workspace-lint`; no errors

## First project checklist

- [ ] Invoked `/workspace-start-project`
- [ ] Declared project intent
- [ ] VP Agent produced `01-vp-brief/product-brief.md`
- [ ] Reviewed and approved (or edited) the VP brief
- [ ] PM Agent produced `02-pm-prd/product-requirements.md`
- [ ] Reviewed and approved the PRD
- [ ] (If technical) Architect Agent produced `03-architecture/architectural-approaches.md`
- [ ] Reviewed and approved
- [ ] Engineer Agent produced `04-engineering/{specs}.md`
- [ ] Reviewed and approved drafts
- [ ] Engineer Agent ran finalize step; status moved to `review`
- [ ] Pre-publish align: `align-cite` and `align-closure` passed (or violations resolved)
- [ ] Ran `/workspace-publish` → review; opened HTML preview folder
- [ ] Read the preview in browser; verified jr-engineer-executable bar
- [ ] Ran `/workspace-publish` → confluence (or kept as review only); pages created in Confluence
- [ ] Project status moved to `published`

## Ongoing rhythm checklist

- [ ] Weekly: `/workspace-ingest-confluence --sync` to refresh in-scope spaces
- [ ] Monthly: `/workspace-lint` for wiki health check
- [ ] Per query: if vendor truth is involved, run `/workspace-align-vendor-truth` and accept or refresh stale caches
- [ ] After 90 days: vendor docs revalidate via `/workspace-revalidate-vendor-docs`
- [ ] Per project: archive when complete; do not let archived projects bleed into active work

## Red flags

If any of the following emerges, pause and address:

- [ ] Citation precision feels low (the LLM seems to cite irrelevant sources)
  - Action: review `align-cite` reports; refine the wiki articles being cited; consider the source-domain tagging
- [ ] Cross-project dependencies blocking your work
  - Action: apply the closure rule resolution (finish the dependency, archive it, or restate)
- [ ] Vendor truth contradictions detected
  - Action: refresh vendor docs; flag the outdated internal source to the team that owns it
- [ ] Quarantine folder filling up
  - Action: review failed conversions; the converter may need iteration on specific Confluence macros
- [ ] Lint reports many warnings on every run
  - Action: invest a session in cleanup; address orphans, sparse articles, missing backlinks

## See Also

- [getting-started.md](getting-started.md)
- [first-week-checklist.md](first-week-checklist.md)
- [docs/product/roadmap.md](../../product/roadmap.md)

## Sources consulted

- docs/product/roadmap.md, second-brain.prompt.md, scripts/verify-setup.py
