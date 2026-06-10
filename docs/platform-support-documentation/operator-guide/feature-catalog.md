---
title: "Feature catalog"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "docs/platform-support-documentation/.inventory/inventory.json"
  - "templates/workspace/routing-map.md"
  - "scripts/README.md"
---

# Feature catalog

Complete index of Second Brain capabilities. **Canonical behavior:** [AGENTS.md](../../../AGENTS.md).

## Workspace lane

### Onboarding

| Feature | Prompt / doc |
|---------|----------------|
| Onboarding | `second-brain` — [.github/prompts/second-brain.prompt.md](../../../.github/prompts/second-brain.prompt.md) |
| Setup walkthrough | [user-guide/getting-started.md](../user-guide/getting-started.md) |

### Ingest

| Feature | Prompt / script |
|---------|-----------------|
| Confluence ingest | `workspace-ingest-confluence` |
| Vendor doc fetch | `workspace-ingest-vendor-doc` |
| RSS ingest | `workspace-ingest-rss` — [scripts/ingest-rss.py](../../../scripts/ingest-rss.py) |
| RSS triage (LLM borderline) | `workspace-triage-rss` |
| RSS review queue | `workspace-review-rss` |
| RSS hub impact (Phase 2) | `workspace-align-rss-impact` |
| Vendor revalidate | `workspace-revalidate-vendor-docs` |

### Compile and query

| Feature | Prompt |
|---------|--------|
| Compile raw → wiki | `workspace-compile` |
| Index-guided Q&A | `workspace-query` |

### Project chain

| Feature | Prompt |
|---------|--------|
| Orchestrator | `workspace-start-project` — [chain-profiles](../../../templates/workspace/chain-profiles/) |
| VP brief | `workspace-vp-agent` |
| PM PRD | `workspace-pm-agent` |
| Architecture | `workspace-architect-agent` |
| Engineering | `workspace-engineer-agent` |
| Technical writer (optional) | `workspace-technical-writer-agent` |
| Architect reviewer (optional) | `workspace-architect-reviewer-agent` |
| Thinking partner | `workspace-thinking-partner` |

### Align and publish

| Feature | Prompt |
|---------|--------|
| Citation verify | `workspace-align-cite` |
| Conformance (advisory) | `workspace-align-conformance` |
| Coverage (advisory) | `workspace-align-coverage` |
| Vendor truth | `workspace-align-vendor-truth` |
| Closure | `workspace-align-closure` |
| Publish preview / Confluence | `workspace-publish`, `workspace-publish-to-confluence`, `workspace-prepare-for-confluence` |
| Archive / unarchive | `workspace-archive`, `workspace-unarchive` |
| Lint | `workspace-lint` |

### Session

| Feature | Prompt |
|---------|--------|
| Session audit | `workspace-session-audit` |

## Platform lane

| Feature | Prompt |
|---------|--------|
| Transcript import | `platform-transcript-librarian` |
| Research review | `platform-research-review` |
| Research sub-prompts | `platform-research-review/claim-miner`, `platform-research-review/grounding-agent`, `platform-research-review/skeptic-agent`, `platform-research-review/product-impact-judge`, `platform-research-review/evaluation-designer`, `platform-research-review/gap-review`, `platform-research-review/transcript-intake` |
| PIC implementation | `platform-implement-backlog` |
| Support doc sync | `platform-sync-support-docs` |

## Scripts

| Script | Purpose |
|--------|---------|
| `verify-setup.py` | Bootstrap dirs, run tests |
| `seed-vendor-docs.py` | Vendor cache bootstrap |
| `revalidate-vendor-docs.py` | TTL scan |
| `compile-workspace-external.py` | Vendor raw → wiki concepts |
| `lint-workspace.py` | Wiki structural lint |
| `lint-platform-research.py` | Platform research artifact lint |
| `lint-platform-support-docs.py` | Support documentation lint |
| `sync-support-doc-inventory.py` | Support doc inventory |
| `sync-transcript-register.py` | Transcript queue index |
| `sync-rejected-register.py` | Rejected claims mirror |
| `sync-rss-register.py` | RSS register rebuild |
| `ingest-rss.py`, `triage-rss.py` | RSS funnel |
| `promote-rss-item.py`, `update-rss-inbox.py` | RSS CEO actions |
| `promote-platform-adr.py` | ADR promotion on PIC accept |

## Config files

| File | Purpose |
|------|---------|
| `config/second-brain.yml` | Scope, vendors, Confluence spaces (gitignored) |
| `config/second-brain.example.yml` | Tracked template |
| `config/rss-feeds.yml` | RSS feeds + interest rules (gitignored) |
| `config/rss-feeds.example.yml` | RSS template |
| `config/vendor-seed-stack.yml` | Vendor seed URLs |
| Vendor catalog doc | [docs/product/vendor-catalog.md](../../product/vendor-catalog.md) |

## Lifecycles

- [templates/workspace/rss-feed-lifecycle.md](../../../templates/workspace/rss-feed-lifecycle.md)
- [templates/workspace/raw-inbox-staging.md](../../../templates/workspace/raw-inbox-staging.md)

## Sources consulted

- inventory.json, routing-map.md, .github/prompts/, scripts/README.md
