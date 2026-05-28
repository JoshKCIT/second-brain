# Quarantine

Failed ingest or compile operations write artifacts here so the rest of a run can continue. Contents are **gitignored** except this README.

## Layout

```
quarantine/{YYYY-MM-DD}/{page-id-or-slug}/
  source.json   # raw payload (e.g. ADF) when conversion failed
  error.md      # human-readable error and context
```

Confluence ingest uses `page-id`; vendor or other sources may use a slug. See `AGENTS.md` (ingest operation) and `.github/prompts/workspace-ingest-confluence.prompt.md`.

## When to use

- ADF → Markdown conversion failure during Confluence ingest
- Vendor fetch or defuddle extraction failure (if not retried inline)
- Compile errors that must preserve the raw input for debugging

Do **not** block the full batch for a single quarantined item. Record counts in the post-ingest manifest (`templates/workspace/post-ingest-manifest.md`) and append a line to `wiki/log.md` when the wiki layer exists locally.

## Resolution

1. Inspect `error.md` and `source.json`
2. Fix converter coverage, URL, or permissions
3. Re-run ingest for that source only (with user approval)
4. Remove the quarantine folder after successful re-ingest (local cleanup)
