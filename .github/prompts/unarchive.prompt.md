---
description: Reverse an archive operation. Move content from wiki/archives/ back to its original location.
mode: agent
---

# /unarchive

You are restoring a previously archived wiki entity to active status.

## Inputs

- Path to a wiki/archives/ directory or file

## Pre-flight

- Verify the path exists in `wiki/archives/`
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
wiki/archives/projects/{slug}/  →  wiki/projects/{slug}/
wiki/archives/standards/...     →  wiki/standards/...
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
