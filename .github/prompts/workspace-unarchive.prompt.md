---
description: Reverse an archive operation. Move content from wiki/workspace-archives/ back to its original location.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-unarchive

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are restoring a previously archived wiki entity to active status.

## Inputs

- Path to a wiki/workspace-archives/ directory or file

## Pre-flight

- Verify the path exists in `wiki/workspace-archives/`
- Determine the original location (mirror outside `archives/`)
- Check if a conflicting entity exists at the original location. If so, refuse and surface.

## Workflow

### Step 1: Confirm

Show the user:

```
About to unarchive: {archived path}
Restore to: {original path}
Original archive date: {from frontmatter}
Original archive reason: {from frontmatter}

Proceed? (y/n)
```

### Step 2: Move

```
wiki/workspace-archives/projects/{slug}/  →  wiki/workspace-projects/{slug}/
wiki/workspace-archives/standards/...     →  wiki/workspace-standards/...
```

### Step 3: Update frontmatter

For every file in the restored set, remove or set to false:

```yaml
archived: false
unarchived_at: {ISO timestamp}
```

Keep `archived_at` and `archive_reason` for historical record.

### Step 4: Update wiki/index.md

Re-add to active catalog.

### Step 5: Append to log

```
## [{ISO timestamp}] unarchive | {path}
- Restored to: {original path}
- Files updated: {count}
```

## Note on consequences

Unarchiving an entity does not automatically re-establish prior cross-project references. If other projects had depended on this entity before it was archived, they were restated. They will not auto-rewire to the unarchived entity. The user must explicitly add references where desired.
