# Example: Board Prep Document

A common CEO workflow: produce a board prep document grounded in current org commitments, with vendor capability claims validated.

## Scenario

The CEO needs to prepare materials for the next board meeting covering: Q3 progress on the data platform initiative, current security and compliance posture, and vendor cost trajectory for Snowflake.

## Workflow

### Step 1: Start the project

```
/workspace-start-project
```

Declare intent:

- Project name: `q4-board-prep`
- Description: "Board prep covering Q3 data platform progress, security posture, vendor cost trajectory"
- Business outcome: "Board has clear, sourced view of current state and risk profile"
- Technical: yes (touches data platform architecture and vendor specifics)
- Concerns: vendor truth on Snowflake costs, current Audit team commitments are unclear

### Step 2: Let the agent chain produce the artifact set

The chain produces:

- VP brief: strategic framing for the board (Q3 lens, current state, risk posture)
- PM PRD: requirements for what the board pack must contain (sections, length, audience)
- Architect doc: data platform architecture summary with current vendor commitments
- Engineer specs: actual section drafts for the board pack

### Step 3: Vendor truth validation

When the Architect Agent cites Snowflake costs or capabilities, it should pull fresh Snowflake pricing and capability docs:

```
The agent will offer: "About to cite Snowflake compute pricing. Cached doc is 95 days old (past 90-day TTL). Refetch? (y/n)"
```

Approve. Defuddle pulls current Snowflake pricing page. The cite refreshes.

### Step 4: Cross-project synthesis

If the architecture doc or engineer specs need to reference past published projects (e.g., the original "data platform migration" project from earlier in the year), the cross-project rule applies:

- If the past project is `published`: cite freely
- If `archived`: cannot cite without unarchiving or restating
- If `in-progress`: surface the dependency; resolve before continuing

### Step 5: Run align-cite and align-vendor-truth

Before publish:

```
/workspace-align-cite (runs automatically pre-publish)
/workspace-align-vendor-truth (run on demand for board materials)
```

`align-vendor-truth` verifies every Snowflake claim cites the vendor doc, not internal interpretations.

### Step 6: Publish to review

```
/workspace-publish
```

Choose `review`. Open the HTML preview in browser. Read as if you were a board member: is each claim supported? Is the language at the right altitude for board consumption?

### Step 7: Refine and republish (loop as needed)

Edit drafts. Re-run finalize. Re-run align checks. Re-publish to review.

### Step 8: Final publish

When the preview reads well and align checks pass, publish to Confluence (or export to PDF, depending on board pack format; PDF export is v1.x).

## Notes

- For a board prep specifically, you may want to run `align-coverage` against any compliance standards that obligate disclosure (e.g., regulatory teams' documentation standards). It is best-effort but useful as a safety net.
- The artifact set lives in `wiki/workspace-projects/q4-board-prep/`. Archive after the meeting if you want it out of active reference; the content stays on disk.
