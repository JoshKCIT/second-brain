---
title: "Verb reference"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "templates/workspace/routing-map.md"
  - "templates/workspace/pointer-resources/verb-invocation-detail.md"
  - ".github/prompts/second-brain.prompt.md"
---

# Verb reference

Task → prompt mapping for Second Brain. Expanded descriptions: [verb-invocation-detail.md](../../../templates/workspace/pointer-resources/verb-invocation-detail.md).

## Workspace verbs

| Verb | Summary |
|------|---------|
| `second-brain` | Onboarding and scope config |
| `workspace-start-project` | Project agent chain orchestrator |
| `workspace-vp-agent` | Product brief |
| `workspace-pm-agent` | PRD |
| `workspace-architect-agent` | Architecture approaches |
| `workspace-engineer-agent` | Engineering specs + finalize |
| `workspace-ingest-confluence` | Confluence → raw |
| `workspace-ingest-vendor-doc` | Vendor URL → raw/workspace-external |
| `workspace-ingest-rss` | RSS ingest + triage + register |
| `workspace-compile` | Raw → wiki (RC-146 approval) |
| `workspace-query` | Index-guided Q&A |
| `workspace-align-cite` | Citation verification |
| `workspace-align-closure` | Publish-set closure |
| `workspace-publish` | HTML preview or Confluence branch |
| `workspace-lint` | Wiki + engineering lint |
| `workspace-session-audit` | Session handoff proposals |
| `workspace-thinking-partner` | Exploration; thinking-notes only |

## Platform verbs

| Verb | Summary |
|------|---------|
| `platform-transcript-librarian` | Import transcripts, sync register |
| `platform-research-review` | Claim extraction and scoring |
| `platform-implement-backlog` | PIC cycle; ADR promotion on accept |
| `platform-sync-support-docs` | Regenerate support documentation set |

## Per-verb detail

Top workspace verbs with operator-oriented **When**, **Approve**, and **Outputs**.

### second-brain

- **When:** First-time setup; configuring in-scope Confluence spaces and `config/second-brain.yml`
- **Approve:** Confirm space list, authority/domain mappings, and config writes before persist
- **Outputs:** Updated `config/second-brain.yml`; optional first ingest/project kickoff; initialized wiki index/log if missing

### workspace-ingest-confluence

- **When:** Pulling Confluence pages into raw for later compile
- **Approve:** Compile is separate — say y/n on compile batch only after ingest completes
- **Outputs:** `raw/workspace-confluence/{space}/pages/`; quarantine entries on failure; ingest manifest in chat

### workspace-compile

- **When:** Raw pages ready to become or update wiki articles
- **Approve:** **Required RC-146** — "Compile these N items to wiki? (y/n)" before any wiki write
- **Outputs:** Updated `wiki/**`, `wiki/index.md`, append `wiki/log.md`; optional connection articles

### workspace-query

- **When:** Question against existing wiki; exploration without project artifact edits
- **Approve:** Read-only by default; confirm if agent proposes `--file-back` to `wiki/workspace-qa/`
- **Outputs:** Answer in chat with Sources consulted list; optional Q&A article file

### workspace-start-project

- **When:** New or resumed project documentation chain from CEO intent
- **Approve:** CEO gate at every stage before next agent; meta.yml stage transitions
- **Outputs:** `wiki/workspace-projects/{slug}/**`, `meta.yml`, stage handoffs, log entries

### workspace-align-cite

- **When:** Before publish or when citation quality is in doubt; `--advisory` at stage gates
- **Approve:** Not required for report; approve artifact fixes before publish
- **Outputs:** Structured violation report under `reports/`; no wiki mutation from align alone

### workspace-align-closure

- **When:** Artifacts at review/published; before confluence publish branch
- **Approve:** Resolve violations or explicit publish override
- **Outputs:** Closure report: wikilinks, cross-project deps, TODO markers

### workspace-publish

- **When:** Project set at review status; ready for HTML preview or Confluence push
- **Approve:** Confluence branch runs align-cite/closure first; CEO confirms override if failures
- **Outputs:** `confluence-review/{slug}/*.html` or Confluence pages; status may move to published

### workspace-lint

- **When:** Health check after compile, weekly/monthly hygiene, troubleshooting
- **Approve:** Not required; approve agent fixes if you request cleanup
- **Outputs:** `reports/workspace-lint-{date}.md` with structural and engineering findings

### workspace-ingest-vendor-doc

- **When:** Caching vendor documentation before citing vendor capabilities
- **Approve:** Compile batch separate; refetch prompts when past TTL
- **Outputs:** `raw/workspace-external/{vendor}/{topic}/`; index may update on compile

### workspace-align-vendor-truth

- **When:** Artifacts cite cloud/vendor capabilities (AWS, Snowflake, etc.)
- **Approve:** Approve vendor refetch if cache stale; fix citations before publish
- **Outputs:** Advisory report; suggested vendor raw paths to cite

### workspace-archive

- **When:** Project complete or deprecated; remove from active index lists
- **Approve:** Confirm slug correct — archive moves `wiki/workspace-projects/{slug}/` to archives
- **Outputs:** `archived: true` frontmatter; updated `wiki/index.md`; log entry

## Summary table

| Verb category | Approval pattern |
|---------------|-------------------|
| Ingest | Raw write OK; compile separate |
| Compile | RC-146 batch y/n |
| Project chain | CEO gate each stage |
| Align | Report only; fix before publish |
| Publish | Align pass or logged override |
| Query | Read-only unless file-back |

For optional stages (technical writer, architect reviewer), see [feature-catalog.md](feature-catalog.md) — same approval pattern at stage gates.

Platform verbs (`platform-*`) follow research review and PIC merge gates — see [platform-lane-overview.md](platform-lane-overview.md).

## See Also

- [feature-catalog.md](feature-catalog.md)
- [using-your-ide.md](using-your-ide.md)
- [everyday-workflows.md](../user-guide/everyday-workflows.md)

## Sources consulted

- routing-map.md, verb-invocation-detail.md, .github/prompts/
