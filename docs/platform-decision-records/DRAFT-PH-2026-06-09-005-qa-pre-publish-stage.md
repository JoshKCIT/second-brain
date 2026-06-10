# DRAFT ADR: PH-2026-06-09-005 - QA Pre-Publish Stage

## Status

Draft

## Context

Makes align-cite, align-closure, and workspace-lint an explicit human-visible checkpoint before publish — especially useful for jr-engineer closure validation.

## Decision

Add `.github/prompts/workspace-qa-agent.prompt.md` that orchestrates:

1. `workspace-align-cite` (production)
2. `workspace-align-closure`
3. `workspace-lint` (project scope)

Output: structured report under `reports/`; optional chain stage `qa` before `ready-for-publish`. Does not auto-publish.

## Intent

- **In scope:** Prompt bundling existing verbs; profile optional stage.
- **Out of scope:** Autonomous publish; replacing mandatory pre-publish checks in `workspace-publish`.

## Approval

- Pending PIC; depends on PH-2026-06-09-001
