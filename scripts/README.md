# Scripts

| Script | Purpose |
|--------|---------|
| `verify-setup.py` | Phase 1A: create runtime dirs, init `wiki/index.md` and `wiki/log.md`, check config, defuddle, optional Atlassian |
| `seed-vendor-docs.py` | Fetch seed URLs from `config/vendor-seed-stack.yml` into `raw/workspace-external/` |
| `revalidate-vendor-docs.py` | Scan vendor cache TTL status (`--dry-run` default) |
| `compile-workspace-external.py` | Batch-compile vendor raw → `wiki/workspace-concepts/` |
| `lint-workspace.py` | Structural wiki lint → `reports/workspace-lint-{date}.md` |
| `lint-platform-research.py` | Validate platform research artifacts |
| `sync-transcript-register.py` | Rebuild transcript queue index (`wiki/platform-research/transcript-register.md`) |
| `sync-rejected-register.py` | Mirror rejected claims into `wiki/platform-research/rejected-ideas.md` |

## Phase 1A quick start (AWS, Snowflake, Informatica)

```bash
pip install pyyaml
npm install -g defuddle

copy config\second-brain.example.yml config\second-brain.yml
python scripts\verify-setup.py
python scripts\seed-vendor-docs.py --yes
python scripts\compile-workspace-external.py
python scripts\lint-workspace.py
```

Seed catalog: `config/vendor-seed-stack.yml`
