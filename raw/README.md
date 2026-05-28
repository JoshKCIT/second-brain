# raw/ — immutable source layer

Content in this directory is **write-once evidence**. Agents read from here; they do not modify files after the initial ingest write.

## Layout

| Path | Purpose |
|---|---|
| `workspace-confluence/{space-key}/pages/` | Confluence page mirrors |
| `workspace-external/{vendor}/{topic}/` | Cached vendor documentation |
| `workspace-inbox/{YYYY-MM-DD}/` | Manual clips and unprocessed captures (RC-146) |
| `workspace-jira/{project-key}/tickets/` | Jira tickets (v1.x) |
| `platform-transcripts/{slug}/` | Platform-lane product intelligence (not workspace compile input) |

## Inbox vs curated wiki

Captures land in scoped `raw/` paths first. Compilation into `wiki/` requires **explicit user approval per batch** (RC-146). See `templates/workspace/raw-inbox-staging.md`.

## Immutability

- Do not edit body content after ingest
- Re-ingest changed sources as new versions with updated `content_hash`
- Compile state tracked separately in gitignored `state.json`

## See also

- `AGENTS.md` § Architecture — three layers
- RC-146 staging: `templates/workspace/raw-inbox-staging.md`
