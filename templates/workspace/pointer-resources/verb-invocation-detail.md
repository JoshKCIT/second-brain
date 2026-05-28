# Verb invocation detail (RC-165)

Expanded descriptions for `.github/prompts/` operations. Shims list verb **names** only; read this file when using an unfamiliar verb.

## Workspace lane

| Verb | Purpose |
|---|---|
| `second-brain` | Onboarding; configure scope, authority mappings |
| `workspace-start-project` | Orchestrate CEO → VP → PM → Architect → Engineer chain |
| `workspace-vp-agent` | Strategic product brief |
| `workspace-pm-agent` | Product requirements document |
| `workspace-architect-agent` | Architecture approaches (technical projects) |
| `workspace-engineer-agent` | Engineering specs + finalize step |
| `workspace-thinking-partner` | Interview-style exploration; `thinking-notes/` only (RC-117) |
| `workspace-ingest-confluence` | Confluence → `raw/`; compile approval-gated (RC-146) |
| `workspace-ingest-vendor-doc` | Fetch vendor doc via defuddle → `raw/workspace-external/` |
| `workspace-compile` | Raw → wiki; explicit batch approval required |
| `workspace-query` | Index-guided Q&A; optional `--file-back` to `wiki/workspace-qa/` |
| `workspace-session-audit` | End-of-session orientation/handoff proposals (RC-164) |
| `workspace-align-cite` | Verify citations match sources; `--advisory` for non-blocking |
| `workspace-align-conformance` | Advisory structure/terminology vs standards |
| `workspace-align-coverage` | Advisory requirements coverage |
| `workspace-align-vendor-truth` | Vendor claims cite vendor-domain sources |
| `workspace-align-closure` | Publish set, wikilinks, cross-project rules |
| `workspace-publish` | Review HTML or Confluence branch |
| `workspace-archive` / `workspace-unarchive` | Project lifecycle |
| `workspace-lint` | Structural + engineering health checks |

## Platform lane

| Verb | Purpose |
|---|---|
| `platform-transcript-librarian` | Import transcripts, sync register, review queue |
| `platform-research-review` | Claim extraction, scoring, draft ADRs |
| Implementation backlog loop | One approved ADR change at a time |

## Skills (`.github/skills/`)

| Skill | Use when |
|---|---|
| `obsidian-markdown` | Authoring wiki or project Markdown |
| `obsidian-bases` | Creating `.base` navigation views |
| `defuddle` | Cleaning vendor web pages for ingest |
| `platform-transcript-librarian` | Transcript import workflow |
| `platform-research-review` | Transcript claim review |
| `session-audit` | Session-end preference capture |

## See also

- Routing table: `templates/workspace/routing-map.md`
- Operations detail: `AGENTS.md` § Core operations
