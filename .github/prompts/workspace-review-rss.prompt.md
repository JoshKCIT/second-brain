---
description: Present RSS review queue; CEO promote, archive, or dismiss by item_id. Compile deferred to workspace-compile.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-review-rss

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.

**Non-overridable:** compile requires explicit batch approval (RC-146); no unattended wiki writes (RC-151).

## Purpose

CEO reviews the **review queue** in `raw/workspace-rss-feed/rss-register.md` (not the full feed corpus). Actions per `item_id`: **promote**, **archive**, **dismiss**.

## Read first

- `raw/workspace-rss-feed/rss-register.md` (includes `summary_excerpt`, `review_flags`)
- `templates/workspace/rss-feed-lifecycle.md`
- `config/rss-feeds.yml` (`interest.max_queue_size`)

## Present queue (required format)

For **each** item in **Review queue**, present a **review card** with all of:

| Field | Source |
|-------|--------|
| `item_id` | register |
| Title | register |
| Feed + `domain` + `authority` | register |
| `published_at` | register |
| `triage_score` + `triage_status` | register |
| `summary_excerpt` | register (if missing, read `raw_path` body) |
| `matched_rules` | register |
| `review_flags` | register — explain `fixture_url` → dismiss; `no_summary` → open URL first |
| `source_url` | register — CEO should open before promote |
| **Suggested action** | agent: promote / archive / dismiss + one-line rationale tied to stack (`config/rss-feeds.yml` interest) |

Do **not** present only a table of IDs and scores. The CEO must be able to decide without opening item files manually.

Optional for `borderline` items: offer `/workspace-triage-rss` LLM pass before CEO decides.

Ask CEO for actions, e.g.:

```text
promote: 2517e6ff011af745
archive: abc123, def456
dismiss: rest
```

## Actions

### promote

1. Run (or use defuddle skill equivalent):

```bash
python scripts/promote-rss-item.py --root . --item-id {item_id}
```

2. On defuddle failure: note quarantine path `raw/workspace-rss-feed/quarantine/{item_id}/` in register `notes` after sync.
3. Re-run `python scripts/sync-rss-register.py --root .`

**Do not promote** items with `review_flags: fixture_url`.

### archive / dismiss

1. Run:

```bash
python scripts/update-rss-inbox.py --root . --item-id {item_id} --status archived
python scripts/update-rss-inbox.py --root . --item-id {item_id} --status dismissed
```

2. Sync register.

**Do not** mutate item body prose (immutable capture).

## Compile handoff (RC-146)

After promote actions, if any items have `inbox_status: promoted`:

```text
Ready to compile {N} promoted item(s) to wiki?
Paths:
  - raw/workspace-rss-feed/promoted/{item_id}/article.md
Compile these to wiki? (y/n)
```

- On **y**: invoke `/workspace-compile` with the path list only.
- On **n**: stop; promoted items remain in register **Promoted awaiting compile**.

## Write scope

- `raw/workspace-rss-feed/**` (items metadata, promoted/, register)
- **No** `wiki/**` except via `/workspace-compile` after explicit CEO approval

## Authority

Promoted articles remain `authority: informational` until `align-vendor-truth` at publish time.
