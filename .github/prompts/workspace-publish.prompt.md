---
description: Branch dispatcher for publishing a project. Asks "review or Confluence?", routes to prepare-for-confluence (HTML preview) or publish-to-confluence (API push).
mode: agent
---

# /workspace-publish

You are publishing a project artifact (or set). The user picks: local review preview, or push to Confluence.

## Inputs

- Path to one artifact, OR a project slug (publishes the entire active set)

## Pre-flight: alignment gates

Before either branch, run automatically:

1. `workspace-align-cite.prompt.md` against the artifact(s)
2. `workspace-align-closure.prompt.md` against the project

If either reports violations:

- Show the violations
- Ask the user: "Align gates failed. Options: (a) fix violations and retry, (b) override and proceed (logged), (c) cancel."
- Do not proceed without explicit choice
- If override: append to `wiki/log.md` with override reason

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
- For Confluence: transition status to `published` on every published artifact; update `wiki/workspace-projects/{slug}/meta.yml` `status: published`

## Step 5: Append to log

```
## [{ISO timestamp}] publish | {slug or artifact}
- Branch: review | confluence
- Pre-publish align: cite={pass|fail|override}, closure={pass|fail|override}
- Output: {confluence-review/... path or Confluence URLs}
- Status updated to: published (if Confluence branch)
```

## On error

If publish fails partway:

- Surface the failure
- Do not partially update status (atomic: either all artifacts publish to confluence or none transition to `published`)
- Offer to retry or rollback (rollback removes any Confluence pages created in this run if the API supports delete)
