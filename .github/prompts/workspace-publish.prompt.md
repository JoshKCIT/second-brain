---
description: Branch dispatcher for publishing a project. Asks "review or Confluence?", routes to prepare-for-confluence (HTML preview) or publish-to-confluence (API push).
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-publish

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are publishing a project artifact (or set). The user picks: local review preview, or push to Confluence.

## Inputs

- Path to one artifact, OR a project slug (publishes the entire active set)

## Pre-flight: alignment gates

These gates are **hybrid** (Decision A): a deterministic core in code emits a
machine-checkable PASS/FAIL, then the prompt's LLM layer adds semantic judgment.
**The deterministic verdict is the publish blocker; the LLM layer never relaxes a
mechanical FAIL** — it may only downgrade a mechanical PASS to FAIL on a bad-faith
match.

Run automatically, in order, before either branch:

1. **Deterministic align-cite (blocking):**
   ```
   second-brain align-cite {artifact-path-or-slug}
   ```
   (equivalently `python -m second_brain align-cite ...`). This writes
   `reports/workspace-align-cite-{project}-{date}.md` and exits non-zero on any
   FAIL (missing cited source path, fabricated quoted span, or a `vendor:*`
   artifact that cites no matching vendor source). A non-zero exit is a hard
   block — the LLM cannot overturn it.
2. `workspace-align-cite.prompt.md` (LLM layer) against the artifact(s) — runs on
   the rows the deterministic core marked PASS; may add FAILs, never removes them.
3. `workspace-align-closure.prompt.md` against the project.

If the deterministic core exits non-zero, or any LLM layer reports violations:

- Show the violations (and the deterministic report path)
- Ask the user: "Align gates failed. Options: (a) fix violations and retry, (b) override and proceed (logged), (c) cancel."
- Do not proceed without explicit choice
- If override: append to `wiki/log.md` with override reason. (A human may override;
  the model may not.)

## Step 1: Branch decision

Ask the user: "Review (local HTML preview) or Confluence (push as new pages)?"

- **review** → invoke `workspace-prepare-for-confluence.prompt.md`
- **confluence** → invoke `workspace-publish-to-confluence.prompt.md`

## Step 2: Optional final align checks

If the user chose Confluence, also offer:

- Run `align-vendor-truth` for vendor claims?
- Run `align-conformance` and `align-coverage` for fuller verification?

These are advisory; not blocking.

## Step 3: Execute

Invoke the chosen branch. Wait for it to complete.

## Step 4: Update status

After successful publish:

- For review: artifact stays at status `review`; the HTML preview is just a preview
- For Confluence: transition status to `published` on every published artifact; update `wiki/workspace-projects/{slug}/meta.yml`: `status: published`, `stage_gate: approved`, `updated` timestamp (PH-001)
- **Scaffold cleanup (RC-130):** Offer CEO choice to archive or delete per-stage `research/`, `chats/`, `daily-progress/`, and `handoff.md` under `wiki/workspace-projects/{slug}/`. Published jr-engineer set excludes scaffold; optional move to `wiki/workspace-archives/projects/{slug}/scaffold/` for audit.

## Step 5: Append to log

```
## [{ISO timestamp}] publish | {slug or artifact}
- Branch: review | confluence
- Pre-publish align: cite-deterministic={pass|fail|override}, cite-llm={pass|fail|override}, closure={pass|fail|override}
- Output: {confluence-review/... path or Confluence URLs}
- Status updated to: published (if Confluence branch)
```

## On error

If publish fails partway:

- Surface the failure
- Do not partially update status (atomic: either all artifacts publish to confluence or none transition to `published`)
- Offer to retry or rollback (rollback removes any Confluence pages created in this run if the API supports delete)
