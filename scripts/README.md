# Scripts

| Script | Purpose |
|--------|---------|
| `verify-setup.py` | Phase 1A: create runtime dirs, init `wiki/index.md` and `wiki/log.md`, check config, defuddle, optional Atlassian |
| `seed-vendor-docs.py` | Fetch seed URLs from `config/vendor-seed-stack.yml` into `raw/workspace-external/` |
| `revalidate-vendor-docs.py` | Scan vendor cache TTL status (`--dry-run` default) |
| `compile-workspace-external.py` | Batch-compile vendor raw → `wiki/workspace-concepts/` |
| `lint-workspace.py` | Structural wiki lint → `reports/workspace-lint-{date}.md` |
| `lint-platform-research.py` | Validate platform research artifacts |
| `ingest-rss.py` | Fetch RSS/Atom feeds → `raw/workspace-rss-feed/items/` (gitignored) |
| `triage-rss.py` | Deterministic interest scoring → triage_status on items |
| `sync-rss-register.py` | Rebuild `raw/workspace-rss-feed/rss-register.md` review queue |
| `promote-rss-item.py` | Fetch full article via defuddle → `promoted/{item_id}/article.md` |
| `update-rss-inbox.py` | Set `inbox_status` to `archived` or `dismissed` |
| `sync-transcript-register.py` | Rebuild transcript queue index (`wiki/platform-research/transcript-register.md`) |
| `sync-support-doc-inventory.py` | Build support-doc prompt/script inventory JSON |
| `lint-platform-support-docs.py` | Validate `docs/platform-support-documentation/` |
| `.github/workflows/validate-support-docs.yml` | CI: inventory drift + lint + tests (IDE-agnostic) |
| `sync-rejected-register.py` | Mirror rejected claims into `wiki/platform-research/rejected-ideas.md` |
| `promote-platform-adr.py` | On PIC accept: strip `DRAFT-` from ADR filename and sync repo references (PH-008). **`platform-implement-backlog` agent** runs `--claim-id` / `--pic-cycle` on accept; CEO does not run manually. |

## Phase 1A quick start (AWS, Snowflake, Informatica)

```bash
pip install pyyaml feedparser
npm install -g defuddle

copy config\second-brain.example.yml config\second-brain.yml
python scripts\verify-setup.py
python scripts\seed-vendor-docs.py --yes
python scripts\compile-workspace-external.py
python scripts\lint-workspace.py
```

Seed catalog: `config/vendor-seed-stack.yml` (all vendors); `config/aws-seed-stack.yml` (AWS); `config/ibm-db2-zos-seed-stack.yml` (Db2 12 for z/OS); `config/snowflake-seed-stack.yml` (Snowflake)
