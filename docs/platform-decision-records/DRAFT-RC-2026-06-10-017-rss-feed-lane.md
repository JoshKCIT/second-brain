# DRAFT-RC-2026-06-10-017 — RSS feed lane (workspace)

## Status

Draft — pending CEO approval for promotion.

## Context

High-volume vendor and industry news arrives via RSS/Atom. Scanning thousands of items manually does not scale. Second Brain already has RC-146 inbox staging and vendor cache lanes; a dedicated **gitignored** capture lane with config-driven triage and CEO promote/archive/dismiss is needed.

## Decision

Add workspace-lane RSS funnel:

1. **Capture** — `scripts/ingest-rss.py` → `raw/workspace-rss-feed/items/` (immutable body after write).
2. **Triage** — `scripts/triage-rss.py` deterministic scoring; optional `/workspace-triage-rss` for `borderline` only.
3. **Review** — `/workspace-review-rss` promote (defuddle) / archive / dismiss via register queue.
4. **Compile** — existing `/workspace-compile` with **explicit batch approval** (RC-146); no change to compile gate.
5. **Phase 2** — `/workspace-align-rss-impact` advisory reports only.

Tracked schema: `config/rss-feeds.example.yml`, prompts, scripts, tests. Personal data: `config/rss-feeds.yml`, `raw/workspace-rss-feed/**` gitignored.

## Non-goals (preserved)

- **RC-151** — no unattended wiki compile.
- **RC-153** — no Slack/email push; queue is in-repo.
- RSS items are **not** vendor truth until `align-vendor-truth` against `raw/workspace-external/`.
- No platform-lane promotion into `wiki/workspace-standards/**` without approval.

## Consequences

- New scripts: `ingest-rss.py`, `triage-rss.py`, `sync-rss-register.py`, `promote-rss-item.py`.
- New prompts: `workspace-ingest-rss`, `workspace-triage-rss`, `workspace-review-rss`, `workspace-align-rss-impact` (Phase 2).
- Lifecycle: `templates/workspace/rss-feed-lifecycle.md`.
- Tests: `tests/workspace_rss/`, fixtures under `tests/fixtures/workspace-rss/`.

## Validation

| ID | Check |
|----|-------|
| G-1 | Ingest/triage prompts contain no instruction to write `wiki/**` |
| G-2 | Review defers compile to `/workspace-compile` with y/n |
| G-3 | No script schedules unattended compile |
| G-4 | Re-run ingest does not mutate existing item bodies |
| G-5 | Promoted vendor news stays informational until align-vendor-truth |
| G-6 | `raw/workspace-rss-feed/` contents gitignored |

Automated: `python -m unittest discover -s tests/workspace_rss`.

### E2E smoke checklist (manual)

| Step | Action | Expected |
|------|--------|----------|
| 1 | Copy `config/rss-feeds.example.yml` → `config/rss-feeds.yml`; enable 2–3 feeds | Config valid |
| 2 | `python scripts/ingest-rss.py --yes` | New files under `items/`; log entry |
| 3 | `python scripts/triage-rss.py --yes` | Majority `auto_skip`; queue ≤ max_queue_size |
| 4 | `python scripts/sync-rss-register.py` | Readable `rss-register.md` |
| 5 | `/workspace-review-rss` — promote 1, archive/dismiss others | `promoted/{id}/article.md` |
| 6 | `/workspace-compile` on promoted path | CEO y/n; wiki updated on y |
| 7 | `wiki/index.md` | New article lists raw path in sources |
| 8 | `python scripts/lint-workspace.py` | No new blocking errors |

## See also

- `templates/workspace/rss-feed-lifecycle.md`
- `templates/workspace/raw-inbox-staging.md` (RC-146)
- RC-151, RC-153 decision records
