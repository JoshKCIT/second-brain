# Post-ingest / post-compile manifest (template)

Agents print this block after a batch ingest or compile completes.

```text
--- Second Brain manifest ---
Operation: {ingest-confluence | ingest-vendor-doc | ingest-rss | platform-sync-support-docs | compile}
Batch: {date-time}

Ingested: {N} sources ({created} new, {updated} refreshed, {failed} quarantined)
RSS (ingest-rss only): fetched {N} | auto_skip {N} | review queue {N} | promoted {N}
Raw inbox (unprocessed): {count} — paths: {list up to 5 or "none"} (RC-146)
Compiled to wiki: {count} | skipped (inbox): {count}
Topics created: {n} | updated: {n}
Connections created: {n} | updated: {n}
Wiki articles created: {list up to 5}
Wiki articles updated: {list up to 5}
Index updated: yes | no
Quarantined: {paths or "none"}

Stale vendor docs (past TTL): {count} — run /workspace-revalidate-vendor-docs

Next suggested step:
  - {compile | workspace-lint | workspace-query smoke test}

Run smoke-test query? (y/n)
--- end manifest ---
```
