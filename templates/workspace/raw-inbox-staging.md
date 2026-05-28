# Raw inbox staging (RC-146)

Teachable **capture → inbox → compile** workflow. Separates unprocessed clips in `raw/` from curated knowledge in `wiki/`.

## Mental model

```text
Capture (clip, fetch, ingest)  →  raw/ inbox paths  →  [CEO approval]  →  compile  →  wiki/
```

- **`raw/`** — immutable after write; evidence and inbox staging
- **`wiki/`** — LLM-curated, index-linked knowledge
- **Compile** — approval-gated mutation; always logs to `wiki/log.md`

No nightly or implicit auto-compile. Small batches still require explicit approval.

## Inbox paths

| Path | Use when | Authority / domain |
|---|---|---|
| `raw/workspace-inbox/{YYYY-MM-DD}/{slug}.md` | Manual clips, Chrome exports, ad-hoc captures | Set `authority` + `domain` before compile; default `informational` / `internal` until CEO confirms |
| `raw/workspace-confluence/{space}/pages/` | Confluence API ingest | From `config/second-brain.yml` mapping |
| `raw/workspace-external/{vendor}/{topic}/` | On-demand vendor doc fetch | `domain: vendor:{vendor}` |
| `raw/platform-transcripts/{slug}/` | Platform lane only | Not workspace compile input |

## Inbox capture frontmatter (manual clips)

```yaml
---
title: "{clip title}"
source_url: "{original URL if any}"
capture_method: manual-clip | browser-export | agent-ingest
captured_at: {ISO timestamp}
ingested_at: {ISO timestamp}
content_hash: {SHA-256 of body}
authority: informational
domain: internal
inbox_status: unprocessed
---
```

After successful compile, agents may add `compiled_at` and `wiki_articles` to `state.json` (gitignored); do not rewrite raw body.

## Operator workflow

1. **Capture** — drop clip or run ingest with `--raw-only` when compile is not wanted yet
2. **Review inbox** — list unprocessed raw paths (`workspace-lint` orphan_sources advisory)
3. **Approve compile** — CEO confirms batch: "Compile these N paths to wiki?"
4. **Run `/workspace-compile`** — retrieval contract (RC-018) + topic/entity phases (RC-148), then wiki writes
5. **Verify** — new wiki articles list raw path in `sources`; check manifest

## Prompt integration

| Operation | RC-146 behavior |
|---|---|
| `/workspace-compile` | **Hard stop** without explicit user approval listing paths |
| `/workspace-ingest-confluence` | Default: raw write then **ask** before compile; `--raw-only` skips compile |
| `/workspace-ingest-vendor-doc` | Writes cache to `raw/workspace-external/`; compile optional and approval-gated |

## Safeguards

- Compile never runs on `raw/platform-transcripts/**` for workspace wiki
- Orphan raw pages are **advisory** in lint — inbox is expected to hold unprocessed items
- Promotion from inbox does not delete raw files (immutability preserved)

## Out of scope

- Chrome clipper integration (operator copies manually)
- Unattended schedulers or nightly auto-compile (RC-151 rejected)

## See also

- Compile prompt: `.github/prompts/workspace-compile.prompt.md`
- Post-ingest manifest: `templates/workspace/post-ingest-manifest.md`
- Raw layer README: `raw/README.md`
- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-146-raw-inbox-staging.md`
