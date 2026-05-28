---
description: Onboarding conversation. Configure default in-scope Confluence spaces with authority and domain mappings, naming conventions, and create the first project skeleton.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /second-brain — Onboarding

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are walking the user (CEO) through first-time setup of their Second Brain instance.

## Pre-flight

Verify:
- `.env` is present and Atlassian credentials validate (test a single API call)
- `wiki/index.md` exists (initialize empty if not)
- `wiki/log.md` exists (initialize empty if not)

If any check fails, surface the failure with remediation and stop.

## Conversation

### Step 1: Confirm tenant

Ask the user to confirm their Atlassian Cloud Enterprise tenant URL. Pull from `.env` (`ATLASSIAN_SITE_URL`) and confirm.

### Step 2: Default in-scope spaces

Ask: which Confluence spaces are standards-publishers for your work? Common choices: Architecture, Security, Audit, Data Modeling, SRE, Engineering. For each space the user names:

- Get the space key
- Ask: authority level for this space's published pages? (`standard`, `recommendation`, `informational`)
- Ask: domain? (`internal` is the default for company spaces; `industry:nist` etc. for specialty spaces)

### Step 3: Persist to config

Write `config/second-brain.yml`:

```yaml
atlassian:
  site_url: {from .env}
  email: {from .env}

default_in_scope_spaces:
  - key: ARCH
    name: Architecture
    authority: standard
    domain: internal
  - key: SEC
    name: Security
    authority: standard
    domain: internal
  # ... user's choices

vendor_revalidation:
  default_ttl_days: 90
  per_vendor: {}
  hard_max_age_days: 365

confluence_sync:
  default_cadence: weekly
  reminder_after_days: 7

alignment_defaults:
  align_cite: production
  align_conformance: best-effort
  align_coverage: best-effort
```

### Step 4: First project (optional)

Ask: do you want to create your first project now? If yes, invoke `workspace-start-project.prompt.md`. If no, tell the user they can run `/workspace-start-project` anytime.

### Step 5: Initial ingest (optional)

Ask: do you want to ingest one of the in-scope spaces now to populate the wiki? If yes, invoke `workspace-ingest-confluence.prompt.md` for the chosen space. If no, the user can ingest later.

### Step 6: Closing

Append to `wiki/log.md`:

```
## [{ISO timestamp}] second-brain | onboarding complete
- In-scope spaces configured: {count}
- First project: {name or none}
- Initial ingest: {space or none}
```

Tell the user setup is complete and point to `README.md` for what to do next.

## Resumability

If `config/second-brain.yml` already exists, skip to Step 4 and offer to add additional in-scope spaces or create another project rather than rewriting config.
