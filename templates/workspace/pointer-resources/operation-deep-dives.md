# Operation deep-dives (RC-165)

Task-matched pointers to `AGENTS.md` § Core operations. Read the listed AGENTS section before running the verb.

| Task | Read first | AGENTS.md section |
|---|---|---|
| Confluence ingest | `config/second-brain.yml`, space mapping | § 1. Ingest (Confluence) |
| Vendor doc fetch | TTL config, existing cache | § 2. Ingest (vendor doc) |
| Compile batch | `wiki/index.md`, retrieval contract | § 3. Compile (raw → wiki) |
| Topic/entity compile | `templates/workspace/topic-entity-compile.md` | RC-148 phases inside compile |
| Query | `wiki/index.md` | § 4. Query |
| Transcript import | transcript register | § 5. Transcript librarian |
| Research review | claim register | § 6. Research review |
| Align checks | target artifact + sources | § 7–9. Align |
| Publish | align-cite + align-closure pass | § 10. Publish |
| Archive | project slug | § 11. Archive |
| Lint | `scripts/lint-workspace.py` | § 12. Lint |

## RC-146 compile gate (summary)

1. Capture → `raw/` (inbox or structured path)
2. CEO approves compile batch
3. `/workspace-compile` with retrieval contract
4. Verify wiki `sources` link back to raw

Template: `templates/workspace/raw-inbox-staging.md`

## RC-018 retrieval contract (summary)

Document purpose, in-scope sources, required wiki/raw paths, authority, freshness, exclusions **before** multi-standard generation or compile batches.

Template: `templates/workspace/retrieval-contract-checklist.md`

## See also

- Full operations: `AGENTS.md`
- Topic/entity compile: `templates/workspace/topic-entity-compile.md` (RC-148)
- Verb list: `templates/workspace/pointer-resources/verb-invocation-detail.md`
