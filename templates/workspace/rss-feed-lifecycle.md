# RSS feed lifecycle (workspace lane)

Personal **signal ingestion** for vendor and industry news. Extends RC-146 inbox staging: capture in gitignored `raw/workspace-rss-feed/`, curate via triage queue, promote selectively, compile to wiki only after explicit batch approval.

## Funnel

```text
Feeds (config) → ingest-rss → items/ (immutable)
              → triage-rss (deterministic) → auto_skip | queue
              → workspace-triage-rss (optional LLM on borderline only)
              → sync-rss-register → rss-register.md
              → workspace-review-rss → promote | archive | dismiss
              → promoted/ full article (defuddle)
              → workspace-compile (RC-146 y/n) → wiki/
              → workspace-align-rss-impact (Phase 2, advisory)
```

## Paths

| Path | Role |
|------|------|
| `config/rss-feeds.yml` | Feeds + interest rules (gitignored; copy from example) |
| `raw/workspace-rss-feed/items/` | Lightweight RSS capture |
| `raw/workspace-rss-feed/promoted/` | Full article after CEO promote |
| `raw/workspace-rss-feed/rss-register.md` | Review queue index |
| `raw/workspace-rss-feed/.state/` | Dedupe and triage audit |

## Item states

| `inbox_status` | Meaning |
|----------------|---------|
| `unprocessed` | In funnel; not yet decided |
| `promoted` | Full article fetched; ready for compile |
| `archived` | Read; not hub-worthy; retained for audit |
| `dismissed` | Noise; retained for audit |

| `triage_status` | Meaning |
|-----------------|---------|
| `pending` | Not yet triaged |
| `auto_skip` | Below threshold; hidden from queue |
| `suggested` | Review queue |
| `high_signal` | Top of review queue |
| `borderline` | LLM triage optional |

## CEO review (`/workspace-review-rss`)

Work **only** the review queue in `rss-register.md` (typically ≤ `max_queue_size` items).

Each queue entry includes **`summary_excerpt`** (RSS teaser), **`matched_rules`**, and **`review_flags`** (e.g. `fixture_url` for test feeds). Open **`source_url`** in a browser before **promote** — promote runs defuddle on that URL.

Per `item_id`:

- **promote** — fetch full URL via defuddle → `promoted/{item_id}/article.md`
- **archive** — set `inbox_status: archived`
- **dismiss** — set `inbox_status: dismissed` (use for noise and `fixture_url` items)

## Compile handoff (RC-146)

After promote, invoke `/workspace-compile` with promoted raw paths only.

1. Agent lists paths and proposed wiki targets.
2. CEO answers **Compile these N items to wiki? (y/n)**.
3. Agent creates/updates wiki articles; updates `wiki/index.md` and `wiki/log.md`.

**You do not** scan the full RSS corpus at compile time.

## Authority

- RSS captures default to `authority: informational`.
- Vendor **capability** claims require `align-vendor-truth` against `raw/workspace-external/` before publish.
- News does not override internal standards without explicit review.

## Non-goals

- No unattended wiki compile (RC-151).
- No Slack/email push (RC-153).
- No auto-promote to wiki from triage.

## E2E smoke checklist

| Step | Command / verb | Pass |
|------|----------------|------|
| 1 | Copy example config; enable feeds | |
| 2 | `ingest-rss.py --yes` | items + log |
| 3 | `triage-rss.py --yes` | auto_skip majority; queue capped |
| 4 | `sync-rss-register.py` | register readable |
| 5 | `/workspace-review-rss` | promote / archive / dismiss |
| 6 | `/workspace-compile` (y) | wiki articles |
| 7 | `lint-workspace.py` | no new blockers |

## See also

- `templates/workspace/raw-inbox-staging.md` — RC-146 compile gate
- `.github/prompts/workspace-ingest-rss.prompt.md`
- `.github/prompts/workspace-review-rss.prompt.md`
- `docs/platform-decision-records/DRAFT-RC-2026-06-10-017-rss-feed-lane.md`
