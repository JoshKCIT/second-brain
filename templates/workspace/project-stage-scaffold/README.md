# Project stage evidence scaffold (RC-130)

Optional layout under each active stage directory. Extends RC-058 `handoff.md` with dated, inspectable draft-tier evidence. **Not** part of the published artifact set.

## Per-stage layout

```text
wiki/workspace-projects/{slug}/0X-{stage}/
├── handoff.md              # RC-058 session restart
├── research/               # clipped sources and reading notes
├── chats/                  # imported external chat transcripts
├── daily-progress/         # dated session summaries (RC-118/119 adjacent)
└── {stage-artifact}.md     # canonical stage output (VP brief, PRD, etc.)
```

## Folder rules

| Path | Purpose | Authority | Promotion |
|---|---|---|---|
| `research/` | Notes while reading scoped wiki/raw sources | draft, tag `domain` in frontmatter | Compile into stage artifact `sources`; never publish raw |
| `chats/` | External chat exports for evidence | informational | Cite in stage artifact if used; not canonical wiki |
| `daily-progress/` | End-of-session summaries (`YYYY-MM-DD.md`) | draft | Catch-up reads; merge into `handoff.md` at session end |
| `handoff.md` | Active restart context | draft-tier | Excluded from publish |

## File templates

- Research note: `templates/workspace/project-stage-scaffold/research-note.md`
- Daily progress: `templates/workspace/project-stage-scaffold/daily-progress.md`
- Chat import: `templates/workspace/project-stage-scaffold/chat-import.md`

## Agent usage

**On resume:** Read `handoff.md` (including PH-003 locked and forwarded open decisions when present), then scan `daily-progress/` (newest first, last 3 files) for catch-up.

**During work:** Write reading notes to `research/`; append session summary to `daily-progress/YYYY-MM-DD.md`.

**On session end:** Update `handoff.md`; ask CEO to confirm. Do not promote scaffold files to `review` or publish set.

**On reopen (PH-005):** Invalidated stage scaffolds stay on disk; do not promote to publish set until stage is re-approved.

**On publish:** Archive or delete scaffold folders per CEO choice; published set remains stage artifacts only.

## Finalize exclusions

Engineer finalize must **not** process files under `research/`, `chats/`, or `daily-progress/`.

## See also

- ADR: `docs/platform-decision-records/DRAFT-RC-2026-05-27-130-project-stage-scaffold.md`
- Handoff: `templates/workspace/handoff.md`
- RC-167 subfolder rule stacking (after RC-130)
