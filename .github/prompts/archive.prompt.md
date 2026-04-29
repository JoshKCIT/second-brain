---
description: Move a completed or deprecated project, standard, or recommendation to wiki/archives/. Excluded from default search and reference.
mode: agent
---

# /archive

You are archiving a wiki entity (project, standard, recommendation, etc.) so it stays on disk for audit but is excluded from default search and reference.

## Inputs

- Path to a wiki/ directory or file
- Optional reason (free-text; logged)

## Pre-flight

- Verify the path exists in `wiki/`
- For projects: verify all artifacts have `status: published` or are explicitly being archived from in-progress (with a stronger user confirmation)
- Check if any other wiki entity references this one. If so, list them and warn: archiving will violate the closure rule for those references.

## Workflow

### Step 1: Confirm

Show the user:

```
About to archive: {path}
Reason: {reason or "not provided"}

Inbound references found: {count}
- {referencing entity 1}
- ...

Archiving will exclude this entity from default search and reference. Other entities that link to it will fail align-closure until they are restated. Proceed? (y/n)
```

Wait for explicit y.

### Step 2: Move

```
wiki/projects/{slug}/         →  wiki/archives/projects/{slug}/
wiki/standards/{team}/{slug}.md  →  wiki/archives/standards/{team}/{slug}.md
wiki/recommendations/...      →  wiki/archives/recommendations/...
```

Use file system mv. Preserve directory structure.

### Step 3: Update frontmatter

For every file in the moved set, set:

```yaml
archived: true
archived_at: {ISO timestamp}
archive_reason: {reason}
```

### Step 4: Update wiki/index.md

Remove the archived entries from the active catalog. Add an entry to the archived section (or a separate archived index).

### Step 5: Append to log

```
## [{ISO timestamp}] archive | {path}
- Moved to: wiki/archives/{...}
- Reason: {reason}
- Inbound references that may now violate closure: {count}
- Files updated with archived frontmatter: {count}
```

### Step 6: Closure consequences

If inbound references exist, surface:

```
The following entities link to the archived item and may now violate align-closure:
- {entity 1}
- ...

Recommended actions:
1. Restate each entity to remove the dependency
2. Run align-closure on each to verify
3. The cross-project dependency rule applies: in-progress projects cannot reference archived projects
```

## Unarchive

To reverse, use `unarchive.prompt.md`. The reverse is explicit and not auto-triggered.

## On error

If mv fails (permission, conflict, etc.):

- Surface the error
- Do not partially archive (transaction: all files in the set move, or none)
- Suggest manual remediation
