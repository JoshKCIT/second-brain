---
description: Full-regen platform support documentation from repo inventory and canonical sources. No wiki writes.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: platform
---

# /platform-sync-support-docs

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply.
- **Tier 2:** This prompt adds platform-lane scope for derived documentation only.

**Non-overridable:** no `wiki/**` writes; CEO accepts merge (y/n or PR) before commit.

## Purpose

Regenerate **all** pages under `docs/platform-support-documentation/` as a **self-contained operator and new-user manual** (v2). Synthesize from canonical sources; `AGENTS.md` and prompts remain authoritative for behavior.

## Read first

- `docs/platform-support-documentation/.inventory/inventory.json` (run inventory script first)
- `templates/workspace/routing-map.md`
- `AGENTS.md` (routing + core operations structure only — do not paste full Tier-1 lists)
- `docs/platform-support-documentation/user-guide/adoption-checklist.md`
- `templates/workspace/raw-inbox-staging.md`
- `templates/workspace/rss-feed-lifecycle.md`
- `templates/workspace/inter-stage-contract.md`
- `templates/workspace/handoff.md`
- `templates/workspace/chain-profiles/`
- `templates/workspace/pointer-resources/verb-invocation-detail.md`
- Key prompts: `second-brain`, `workspace-ingest-confluence`, `workspace-compile`, `workspace-start-project`, `workspace-publish`, `workspace-review-rss`
- `docs/platform-decision-records/` (label DRAFT as not shipped)
- `README.md`, `scripts/README.md`

## Pipeline

1. `python scripts/sync-support-doc-inventory.py --root . --write`
2. Read inventory and canonical sources listed above.
3. **Full regen:** rewrite hub README and every page listed in **Page inventory** below.
4. Update `docs/platform-support-documentation/manifest.yml` (`last_sync`, `sources_consulted`, `pages_written`, counts, `inventory_hash`).
5. `python scripts/lint-platform-support-docs.py --root . --strict`
6. Optional: `reports/platform-support-doc-sync-{date}.md` diff summary.
7. Stop: **Accept sync batch? (y/n)** — do not commit on no.

## Write scope (allowlist)

- `docs/platform-support-documentation/**`
- `reports/platform-support-doc-sync-*.md`

**Never:** `wiki/**`, `AGENTS.md`, protected workspace/PRD files.

## Page inventory (22 pages)

### Hub

- `README.md` — audience routing, learning path (Day 0 → Week 1 → ongoing)

### User guide

| Page | Required sections |
|------|-------------------|
| `how-second-brain-works.md` | Three layers, Compiler analogy, Lanes, What agents do, What you approve |
| `getting-started.md` | Prerequisites, Credentials, Verify setup, IDE open, Onboarding, First ingest, First project, Per-agent IDE |
| `adoption-checklist.md` | Prerequisites checklist, Setup checklist, First project checklist, Ongoing rhythm checklist, Red flags |
| `first-week-checklist.md` | Day 0, Days 1, Days 3, Ongoing rhythm, Red flags |
| `workflow-ingest.md` | Confluence flow, Vendor flow, Inbox staging, RSS flow, Approval gates, Worked example, Approval checkpoints |
| `workflow-compile-and-query.md` | Compile batch, RC-146 gate, Query flow, File-back, Worked example, Approval checkpoints |
| `workflow-project-chain.md` | Stage table, CEO gates, Handoff locks, Finalize and publish, Worked example, Approval checkpoints |
| `workflow-align-and-publish.md` | Align cite, Align closure, Vendor truth, Publish branches, Worked example, Approval checkpoints |
| `everyday-workflows.md` | Quick reference table, Workflow index |
| `troubleshooting.md` | Common gotchas, Auth issues, Defuddle issues, Lint remediation |

### Operator guide

| Page | Required sections |
|------|-------------------|
| `concepts-for-operators.md` | Approval culture, RC-146, RC-151, Citation and closure, PH-006 |
| `using-your-ide.md` | Copilot, Cursor, Claude Code, Windsurf, Prompt discovery |
| `ceo-approval-guide.md` | Compile batches, Stage gates, Publish gate, Platform escalation |
| `glossary.md` | Term table (≥20 terms) |
| `lanes-and-approval-gates.md` | Lane table, RC-146, RC-151, CEO workflow |
| `verb-reference.md` | Workspace verbs, Platform verbs, Per-verb detail (top 10: When / Approve / Outputs each) |
| `feature-catalog.md` | Workspace lane, Platform lane, Scripts, Config files |
| `platform-lane-overview.md` | When to escalate, Transcript flow, PIC pointer |

### Engineer reference (light touch)

- `architecture-map.md`, `scripts-and-automation.md`, `adr-index.md`, `extending-the-platform.md` — cross-link new workflow pages; document v2 lint depth checks in scripts-and-automation.

## Depth bar (v2)

Adapt `docs/style/exemplar-published-doc.md`: term definitions before use, decision tables, worked examples, plain-language governance.

| Page class | Min words | Extra |
|------------|-----------|-------|
| how-second-brain-works, getting-started | 800 | ≥1 flow diagram |
| workflow-*.md | 500 | Worked example + approval checkpoints |
| concepts-for-operators, ceo-approval-guide | 400 | RC-146 and RC-151 in plain language |
| verb-reference | 600 | Top 10 workspace verbs: When / Approve / Outputs |
| troubleshooting | 400 | ≥8 problem rows |
| glossary | 300 | ≥20 terms |

**Every workflow page:** audience + purpose, decision table (when to use vs alternatives), process flow diagram, worked example (invoke → agent → approve → artifacts), common mistakes (≥3).

**Status:** user/operator pages use `status: published` after v2 regen.

**Install:** `user-guide/getting-started.md` is the canonical install doc (no separate setup-kit file).

**Forbidden:** Verbatim copy of full Tier-1 rule lists from `AGENTS.md` (RC-165). Link to AGENTS for authority.

## Frontmatter

- `title`, `audience`, `generated: true`, `last_sync`, `sources` (paths that exist), `status: published` (user/operator) or `draft` (engineer if thin)
- Body ends with `## Sources consulted`

## Sources consulted

- sync-support-doc-inventory.py, lint-platform-support-docs.py, support_doc_common.py, routing-map.md
