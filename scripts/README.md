# Scripts

| Script | Purpose |
|--------|---------|
| `verify-setup.py` | Phase 1A: create runtime dirs, init `wiki/index.md` and `wiki/log.md`, check config, defuddle, optional Atlassian |
| `seed-vendor-docs.py` | Fetch seed URLs from `config/vendor-seed-stack.yml` into `raw/workspace-external/` |
| `revalidate-vendor-docs.py` | Scan vendor cache TTL status (`--dry-run` default) |
| `lint-platform-research.py` | Validate platform research artifacts |

## Phase 1A quick start (AWS, Snowflake, Informatica)

```bash
pip install pyyaml
npm install -g defuddle

copy config\second-brain.example.yml config\second-brain.yml
python scripts\verify-setup.py
python scripts\seed-vendor-docs.py --yes
```

Seed catalog: `config/vendor-seed-stack.yml`
