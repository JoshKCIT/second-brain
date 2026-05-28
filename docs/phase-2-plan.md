# Phase 2 plan — Wiki layer and compile workflow

**Status:** In progress  
**Prerequisite:** Phase 1A complete (vendor caches under `raw/workspace-external/`)  
**Blocked parallel track:** Phase 1B (Confluence) until Atlassian access

---

## Goal

Make the wiki layer a **coherent, navigable, lint-clean retrieval substrate** (RC-001) without Confluence. Vendor raw caches compile into concepts; Obsidian Bases replace hand-maintained tables where possible; structural lint catches drift before Phase 3 projects.

---

## Work breakdown

| # | Deliverable | What “done” means | Tool / path |
|---|-------------|-------------------|-------------|
| 2.1 | **Obsidian Base views** | Four `.base` files in `wiki/workspace-views/`; embedded from `wiki/index.md` | `concepts-catalog.base`, `active-projects.base`, `recent-activity.base`, `stale-vendor-docs.base` |
| 2.2 | **Batch compile (vendor raw)** | Every `raw/workspace-external/**/*.md` referenced by a `wiki/workspace-concepts/` article | `python scripts/compile-workspace-external.py` |
| 2.3 | **Connection article** | At least one cross-vendor connection (AWS ↔ Snowflake data plane) | `wiki/workspace-connections/` |
| 2.4 | **Index + log discipline** | `wiki/index.md` catalog tables current; compile appends to `wiki/log.md` | Updated on each compile |
| 2.5 | **Workspace lint (structural)** | Script implements checks 1–7 + orphan sources + stale vendor TTL | `python scripts/lint-workspace.py` |
| 2.6 | **Frontmatter validation** | Part of lint-workspace (check 7) | Same script |
| 2.7 | **Quarantine behavior** | Documented layout + README for failed ingest/compile | `quarantine/README.md` |
| 2.8 | **Post-ingest manifest** | Documented UX template agents print after ingest/compile batch | `templates/workspace/post-ingest-manifest.md` |
| 2.9 | **Phase 2 exit report** | Lint report with zero errors on vendor-only wiki | `reports/workspace-lint-{date}.md`, `docs/phase-2-exit-report.md` |

---

## Exit criteria (from roadmap)

- Wiki layer coherent: index, concepts for all vendor caches, ≥1 connection  
- Base views render in Obsidian  
- `python scripts/lint-workspace.py` → **0 errors** (warnings acceptable)  
- Without Confluence: no requirement for 100-page ingest bar  

---

## Sequence (this session)

```text
2.1 Base views
    ↓
2.2 compile-workspace-external.py → run on all vendor raw
    ↓
2.3 Connection article + index refresh
    ↓
2.5 lint-workspace.py → fix errors
    ↓
2.7–2.8 docs (quarantine + manifest)
    ↓
2.9 exit report → mark Phase 2 complete in roadmap
```

---

## After Phase 2

| Phase | Focus |
|-------|--------|
| **Phase 3** | `/workspace-start-project` — first real artifact set |
| **Phase 1B** | Confluence ingest when credentials exist |
| **Phase 4** | align-cite / align-vendor-truth on published artifacts |

---

## See also

- `docs/roadmap.md` — canonical phase list  
- `docs/phase-1a-exit-report.md` — vendor bootstrap closure  
- `.github/prompts/workspace-compile.prompt.md` — agent-driven compile (LLM quality)  
- `scripts/compile-workspace-external.py` — deterministic batch compile (Phase 2 bootstrap)
