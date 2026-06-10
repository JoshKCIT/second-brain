---
description: Ingest RSS/Atom feeds, run deterministic triage, sync register. No wiki writes.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-ingest-rss

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed.

## Purpose

Poll configured RSS/Atom feeds into gitignored `raw/workspace-rss-feed/`, score items deterministically, and rebuild the review register. **Does not write `wiki/**`.**

## Read first

- `config/rss-feeds.yml` (or prompt user to copy from `config/rss-feeds.example.yml`)
- `templates/workspace/rss-feed-lifecycle.md`
- `templates/workspace/post-ingest-manifest.md` (ingest-rss fields)

## Pipeline

1. Confirm `config/rss-feeds.yml` exists; if not, instruct user to copy the example and enable feeds.
2. Run:

```bash
python scripts/ingest-rss.py --root . --yes
python scripts/triage-rss.py --root . --yes
python scripts/sync-rss-register.py --root .
```

3. Read `raw/workspace-rss-feed/rss-register.md` summary counts.
4. Print manifest (see below). **Do not** invoke `/workspace-compile` unless user separately requests review or compile.

## Optional LLM pass

If register shows `borderline` items and user wants LLM triage, hand off to `/workspace-triage-rss` before `/workspace-review-rss`.

## Manifest

```text
--- Second Brain manifest ---
Operation: ingest-rss
Batch: {ISO timestamp}

Feeds polled: {N}
Items fetched (new): {N}
Auto-skipped (triage): {N}
Review queue: {N} (suggested / high_signal / borderline)
Promoted awaiting compile: {N}

Register: raw/workspace-rss-feed/rss-register.md

Next suggested step:
  - /workspace-triage-rss (if borderline items)
  - /workspace-review-rss (CEO promote / archive / dismiss)

No wiki writes in this operation (RC-146).
--- end manifest ---
```

## Write scope

- `raw/workspace-rss-feed/**` via scripts only
- `wiki/log.md` append on ingest batch (script)
- **Never** `wiki/workspace-concepts/**`, `wiki/index.md`, or project artifacts without separate compile approval
