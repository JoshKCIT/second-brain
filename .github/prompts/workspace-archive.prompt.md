---
description: Move a completed or deprecated project, standard, or recommendation to wiki/workspace-archives/. Excluded from default search and reference.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-archive

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

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
wiki/workspace-projects/{slug}/         →  wiki/workspace-archives/projects/{slug}/
wiki/workspace-standards/{team}/{slug}.md  →  wiki/workspace-archives/standards/{team}/{slug}.md
wiki/workspace-recommendations/...      →  wiki/workspace-archives/recommendations/...
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
- Moved to: wiki/workspace-archives/{...}
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

To reverse, use `workspace-unarchive.prompt.md`. The reverse is explicit and not auto-triggered.

## On error

If mv fails (permission, conflict, etc.):

- Surface the error
- Do not partially archive (transaction: all files in the set move, or none)
- Suggest manual remediation
