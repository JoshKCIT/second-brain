---
title: "Everyday workflows"
audience: user
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "templates/workspace/routing-map.md"
  - "templates/workspace/pointer-resources/verb-invocation-detail.md"
  - "README.md"
---

# Everyday workflows

Quick reference for daily Second Brain operations. For depth, follow the **workflow index** links — each page includes worked examples and approval checkpoints.

## Quick reference table

| Goal | Invoke | Approval? |
|------|--------|-----------|
| Onboard / configure | `second-brain` | Config writes — confirm |
| Pull Confluence | `workspace-ingest-confluence` | Compile separate y/n |
| Fetch vendor doc | `workspace-ingest-vendor-doc` | Compile separate y/n |
| RSS funnel | `workspace-ingest-rss` → `workspace-review-rss` | Promote + compile y/n |
| Compile raw → wiki | `workspace-compile` | **RC-146 y/n** |
| Ask about wiki | `workspace-query` | Read-only |
| Start project chain | `workspace-start-project` | CEO gate each stage |
| Check citations | `workspace-align-cite` | Report only |
| Preview HTML | `workspace-publish` → review | Before confluence branch |
| Wiki health | `workspace-lint` | Report only |
| Vendor TTL scan | `workspace-revalidate-vendor-docs` | Refetch prompts |
| Session handoff | `workspace-session-audit` | handoff/orientation proposals |
| Explore ideas | `workspace-thinking-partner` | thinking-notes only |

Type commands in AI chat; prompts live in `.github/prompts/`. See [using-your-ide.md](../operator-guide/using-your-ide.md) if slash commands fail.

## Workflow index

| Topic | Deep-dive page |
|-------|----------------|
| Mental model | [how-second-brain-works.md](how-second-brain-works.md) |
| Install | [getting-started.md](getting-started.md) |
| Week 1 plan | [first-week-checklist.md](first-week-checklist.md) |
| Ingest all sources | [workflow-ingest.md](workflow-ingest.md) |
| Compile + query | [workflow-compile-and-query.md](workflow-compile-and-query.md) |
| Project chain | [workflow-project-chain.md](workflow-project-chain.md) |
| Align + publish | [workflow-align-and-publish.md](workflow-align-and-publish.md) |
| Problems | [troubleshooting.md](troubleshooting.md) |
| All verbs | [verb-reference.md](../operator-guide/verb-reference.md) |
| All features | [feature-catalog.md](../operator-guide/feature-catalog.md) |

## Typical day

**Morning:** optional RSS ingest + review queue. **Work session:** project stage agent or query. **After ingest:** compile batch when ready — small batches. **End of session:** optional session-audit for handoff notes.

**Weekly:** Confluence sync ingest for in-scope spaces. **Monthly:** workspace-lint cleanup.

## See Also

- [operator-guide/ceo-approval-guide.md](../operator-guide/ceo-approval-guide.md)
- [operator-guide/concepts-for-operators.md](../operator-guide/concepts-for-operators.md)
- [AGENTS.md](../../../AGENTS.md)

## Sources consulted

- routing-map.md, verb-invocation-detail.md, README.md
