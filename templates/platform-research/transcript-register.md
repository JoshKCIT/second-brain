# Platform Transcript Register

Operational index of product-intelligence sources under `raw/platform-transcripts/`. This file is the queue board: what is imported, what is ready for `/platform-research-review`, and what is already reviewed.

Sync after import or review:

```bash
python scripts/sync-transcript-register.py --root .
```

## Status legend

| Status | Meaning |
|--------|---------|
| `queued` | Present in `raw/platform-transcripts/`; not yet reviewed |
| `partial` | Review started — claims analysis or impact report missing |
| `reviewed` | Claims analysis and impact report both exist |
| `skipped` | User marked intentionally not reviewed (duplicate, noise, off-scope) |

## Summary

| Slug | Status | Source | Claims | Impact |
|------|--------|--------|--------|--------|
| _Run sync to populate._ | | | | |

## Records

Add one YAML block per transcript. The sync script updates `status`, artifact paths, and the summary table; preserve `title`, `notes`, and `skipped` when set manually.

```yaml
slug: example-slug
status: queued
source: raw/platform-transcripts/example-slug/transcript.md
title: ""
imported: YYYY-MM-DD
reviewed: ""
claims_analysis: ""
impact_report: ""
notes: ""
```
