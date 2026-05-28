---
title: "Workstream Scaffold — {workstream label}"
type: project-sub-scaffold
project: "{slug}"
stage: vp-brief | pm-prd | architecture | engineering
workstream: "{workstream-slug}"
inherits: AGENTS.md
instruction_stack_tier: 3
publish_scope: exclude
draft_tier: true
not_canonical: true
status: draft
created: {ISO date}
updated: {ISO date}
---

# Workstream — {workstream label}

> **Tier 3 — draft-tier only.** Inherits `AGENTS.md` and the stage agent prompt. Does not override approval gates, align-cite, or align-closure. Not part of the published artifact set.

## Workstream intent

One paragraph: what this sub-effort delivers within the parent stage.

## Scope (this workstream)

- In scope: {bullets}
- Out of scope: {bullets}

## Local conventions

Optional voice, terminology, or focus rules for this thread. Do not duplicate Tier-1 governance bullets.

## Handoff to stage artifact

When this workstream produces decisions:

1. Summarize verified outcomes for parent stage `handoff.md` or the stage artifact body.
2. Record sources in stage artifact frontmatter — not in sub-scaffold alone.
3. Do not promote this file to `review` or publish set.

## See also

- Parent stage handoff: `../handoff.md`
- Sub-scaffold README: `templates/workspace/project-sub-scaffold/README.md`
