# Platform support documentation

Self-contained operator and new-user manual for Second Brain. **Canonical behavior** remains [AGENTS.md](../../AGENTS.md), prompts under `.github/prompts/`, and accepted ADRs — this manual synthesizes those sources into readable workflows.

## Audience routing

| You are… | Start here |
|----------|------------|
| Brand-new user | [how-second-brain-works.md](user-guide/how-second-brain-works.md) → [getting-started.md](user-guide/getting-started.md) |
| Daily operator | [everyday-workflows.md](user-guide/everyday-workflows.md) + workflow pages below |
| CEO / approver | [ceo-approval-guide.md](operator-guide/ceo-approval-guide.md) + [lanes-and-approval-gates.md](operator-guide/lanes-and-approval-gates.md) |
| Engineer / contributor | [architecture-map.md](engineer-reference/architecture-map.md) |

## Learning path

| Phase | Goal | Read |
|-------|------|------|
| Day 0 | Understand the system and install | [how-second-brain-works.md](user-guide/how-second-brain-works.md), [getting-started.md](user-guide/getting-started.md) |
| Day 1 | First ingest and wiki browse | [workflow-ingest.md](user-guide/workflow-ingest.md), [workflow-compile-and-query.md](user-guide/workflow-compile-and-query.md) |
| Week 1 | First project through publish | [first-week-checklist.md](user-guide/first-week-checklist.md), [adoption-checklist.md](user-guide/adoption-checklist.md), [workflow-project-chain.md](user-guide/workflow-project-chain.md), [workflow-align-and-publish.md](user-guide/workflow-align-and-publish.md) |
| Ongoing | Rhythm and governance | [concepts-for-operators.md](operator-guide/concepts-for-operators.md), [troubleshooting.md](user-guide/troubleshooting.md) |

## Workflow pages

| Workflow | Page |
|----------|------|
| Ingest (Confluence, vendor, inbox, RSS) | [workflow-ingest.md](user-guide/workflow-ingest.md) |
| Compile and query | [workflow-compile-and-query.md](user-guide/workflow-compile-and-query.md) |
| Project agent chain | [workflow-project-chain.md](user-guide/workflow-project-chain.md) |
| Align and publish | [workflow-align-and-publish.md](user-guide/workflow-align-and-publish.md) |

## Operator reference

- [feature-catalog.md](operator-guide/feature-catalog.md) — complete capability index
- [verb-reference.md](operator-guide/verb-reference.md) — per-verb When / Approve / Outputs
- [glossary.md](operator-guide/glossary.md) — terms defined before use
- [using-your-ide.md](operator-guide/using-your-ide.md) — VS Code, Cursor, Claude Code, Windsurf

## Regeneration

Run `/platform-sync-support-docs` to full-regen all pages from repo sources. CEO approves merge after `python scripts/lint-platform-support-docs.py --root . --strict` passes.

## See also

- [adoption-checklist.md](user-guide/adoption-checklist.md) — printable checkbox adoption path
- [templates/workspace/pointer-resources/](../../templates/workspace/pointer-resources/) — agent depth on demand
