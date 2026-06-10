---
title: "First week checklist"
audience: user
generated: true
last_sync: 2026-06-09T00:00:00Z
status: published
sources:
  - "docs/platform-support-documentation/user-guide/adoption-checklist.md"
  - "templates/workspace/routing-map.md"
---

# First week checklist

Narrative adoption path for your first seven days with Second Brain. Use alongside [getting-started.md](getting-started.md) for install detail and **[adoption-checklist.md](adoption-checklist.md)** for printable checkbox tracking.

## Day 0 — Install and orient

Read [how-second-brain-works.md](how-second-brain-works.md) first, then follow [getting-started.md](getting-started.md) through verify-setup and `/second-brain` onboarding. Check off prerequisites and setup items in [adoption-checklist.md](adoption-checklist.md).

**Day 0 success:** `verify-setup.py` passes; onboarding conversation complete; you understand raw vs wiki and approval gates.

## Days 1–2 — First ingest and wiki browse

Run a small Confluence ingest (10–20 pages) or vendor-only demo per [workflow-ingest.md](workflow-ingest.md). Approve compile when prompted (RC-146). Browse `wiki/index.md` in Obsidian and run `/workspace-query` on one real question.

## Days 3–7 — First project to review

Week 1 goal: one small project from intent to review HTML. Follow [workflow-project-chain.md](workflow-project-chain.md) stage by stage. Track milestones in [adoption-checklist.md](adoption-checklist.md) under **First project checklist**.

Between stages, say **proceed** only when you mean to lock decisions for downstream agents. Reopening an upstream stage invalidates downstream artifacts (PH-005).

## Ongoing rhythm

After week 1, adopt a lightweight rhythm:

| Cadence | Action |
|---------|--------|
| Weekly | `/workspace-ingest-confluence --sync` for in-scope spaces |
| Per query | `/workspace-query`; run `/workspace-align-vendor-truth` when citing vendor capabilities |
| Monthly | `/workspace-lint` for wiki health |
| ~90 days | `/workspace-revalidate-vendor-docs` for TTL stale caches |
| Per project | Archive when complete — `/workspace-archive` |
| RSS (optional) | `/workspace-ingest-rss` → review queue → compile promoted items only |

Session end: optional `/workspace-session-audit` for handoff proposals to `handoff.md` / `orientation.md`. Full checkbox list: [adoption-checklist.md](adoption-checklist.md) **Ongoing rhythm**.

## Red flags

Pause and address before continuing:

| Signal | Action |
|--------|--------|
| Citation precision feels low | Run `align-cite`; refine wiki articles being cited; check source-domain tags |
| Cross-project dependency blocking work | Finish dependency project, archive it, or restate dependent project (closure rule) |
| Vendor truth contradictions | Refresh vendor cache; flag outdated internal source to owning team |
| `quarantine/` filling up | Review failed Confluence conversions; iterate on macro handling |
| Lint warnings every run | Dedicate a cleanup session — orphans, sparse articles, stale vendor docs |
| Agent editing protected files mid-project | Escalate to platform lane (PH-006); do not accept workspace PRD/standards edits from transcript claims |

See [adoption-checklist.md](adoption-checklist.md) **Red flags** for checkbox form.

## See Also

- [adoption-checklist.md](adoption-checklist.md)
- [getting-started.md](getting-started.md)
- [workflow-project-chain.md](workflow-project-chain.md)
- [workflow-align-and-publish.md](workflow-align-and-publish.md)
- [ceo-approval-guide.md](../operator-guide/ceo-approval-guide.md)

## Sources consulted

- user-guide/adoption-checklist.md, templates/workspace/routing-map.md
