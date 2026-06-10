---
description: Optional LLM triage for borderline RSS items only. Advisory; no wiki writes.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-triage-rss

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.

**Non-overridable:** no wiki mutations; deterministic triage already ran; this pass is advisory for `borderline` only.

## Purpose

Upgrade or downgrade **`borderline`** items only after `triage-rss.py` has run. Deterministic scoring handles bulk; LLM reads title/summary plus scoped hub context.

## Read first

- `raw/workspace-rss-feed/rss-register.md` (borderline section)
- `config/rss-feeds.yml` (`interest`, `wiki_index_hints`)
- `wiki/index.md` (catalog only; do not load entire wiki)
- Optional: articles under `wiki_index_hints` paths when relevant

## Scope

Process only records with `triage_status: borderline` and `inbox_status: unprocessed`.

For each item:

1. Read `raw_path` capture (title + summary body).
2. Compare against active projects (`wiki/workspace-projects/*/meta.yml` slugs) and index hints.
3. Decide: upgrade to `suggested` or `high_signal`, downgrade to `auto_skip`, or leave `borderline`.
4. Patch **frontmatter only** on the item file (`triage_status`, optional `notes` in register via sync).
5. Re-run `python scripts/sync-rss-register.py --root .`

## Rules

- **Do not** promote to wiki or set `inbox_status: promoted` here.
- **Do not** write `wiki/**`.
- Document reasoning in register `notes` when upgrading/downgrading (preserved on sync).

## Manifest

```text
--- Second Brain manifest ---
Operation: triage-rss-llm
Borderline reviewed: {N}
Upgraded: {N} | Downgraded: {N} | Unchanged: {N}

Next: /workspace-review-rss
--- end manifest ---
```
