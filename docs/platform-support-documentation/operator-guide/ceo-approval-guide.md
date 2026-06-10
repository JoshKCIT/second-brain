---
title: "CEO approval guide"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "AGENTS.md"
  - "templates/workspace/inter-stage-contract.md"
  - "docs/platform-decision-records/RC-2026-05-27-146-raw-inbox-staging.md"
  - ".github/prompts/platform-sync-support-docs.prompt.md"
---

# CEO approval guide

When to say **yes**, **no**, or **wait** as the human approver in Second Brain. Agents optimize for helpfulness; your job is to protect canonical truth and scope.

## Compile batches

**Trigger:** Agent lists raw paths and proposed wiki targets after ingest or `/workspace-compile`.

| Response | When |
|----------|------|
| **Yes** | You reviewed the list; scope is correct; ready for wiki update |
| **No** | Wrong pages, wrong authority mapping, or need smaller batch first |
| **Wait** | Need to fix `config/second-brain.yml` mappings or raw quarantine first |

Never feel pressured to approve large batches — RC-146 allows incremental compiles.

## Stage gates

**Trigger:** Stage artifact at `stage_gate: awaiting_ceo_review`.

| Response | When |
|----------|------|
| **Approved, proceed** | Artifact acceptable; lock decisions for downstream |
| **Revise** | Agent should edit; do not proceed yet |
| **Reopen upstream** | PH-005 — invalidates downstream; orchestrator resets stage |

Explicit locks beat implicit approval — if scope changed in your edits, say what is locked.

## Publish gate

**Trigger:** Artifacts at `status: review`; you want external output.

| Step | Pass criteria |
|------|---------------|
| align-cite | Citations match sources |
| align-closure | No forbidden wikilinks; cross-project clean |
| align-vendor-truth | Vendor claims cite vendor raw (if applicable) |
| Review HTML | Jr-engineer can execute from set alone |
| Confluence push | Only after aligns pass or logged override |

Override aligns only with explicit acknowledgment — violations logged.

## Platform escalation

**Trigger:** Session proposes changing AGENTS.md, PRD, standards, or stack from transcript/product idea.

| Response | Action |
|----------|--------|
| **Defer** | Continue workspace work; note idea for later |
| **Escalate** | Switch to `platform-research-review` or transcript librarian |
| **Never** | Accept silent edits to protected files from workspace lane |

Approved changes flow: draft ADR → CEO approve → `platform-implement-backlog` PIC cycle.

**Support doc regen:** `/platform-sync-support-docs` ends with **Accept sync batch? (y/n)** — same merge discipline.

## Decision framework

Use this quick framework when the agent waits for you:

| Question | If yes | If no |
|----------|--------|-------|
| Do I understand every path in the batch? | Consider compile yes | Ask for smaller batch |
| Did I edit scope in this stage artifact? | List locks explicitly | Ask agent to extract locks |
| Are aligns clean? | Proceed to publish review | Fix or override with logged reason |
| Is this a product idea about Second Brain? | Escalate platform lane | Continue workspace work |

## Red lines (always no)

- Silent wiki compile without RC-146 prompt
- Publishing with known align-cite failures without override log
- Merging transcript claims into workspace standards without research review
- Auto-committing support doc regen without reading diff

When agents present a diff, skim `Sources consulted` on changed support pages — every cited path should exist on disk before merge.

Keep a personal log of override reasons when you bypass align — audit trails help future you and teammates.

## See Also

- [concepts-for-operators.md](concepts-for-operators.md)
- [lanes-and-approval-gates.md](lanes-and-approval-gates.md)
- [platform-lane-overview.md](platform-lane-overview.md)

## Sources consulted

- AGENTS.md, inter-stage-contract.md, RC-146 ADR, platform-sync-support-docs.prompt.md
