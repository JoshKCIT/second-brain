# DRAFT ADR: RC-2026-05-27-167 - Project Subfolder Rule Stacking

## Status

Draft

## Source Claim

- Claim ID: RC-2026-05-27-167
- Source transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
- Speaker: Jeff
- Timestamp: 00:16:30-00:17:00
- Claim type: workflow_proposal

## Context

Jeff nests project folders under workstations, each with local CLAUDE.md, memory.md, and resources. Second Brain has RC-058 handoff and RC-130 stage scaffold but no explicit three-level stack contract for project sub-scaffolds within a stage.

## Decision

Allow optional project sub-scaffolds under `wiki/workspace-projects/{slug}/0X-{stage}/` (e.g., `subprojects/{name}/`) with local orientation and resources. Sub-scaffold rules inherit root AGENTS + stage prompt; excluded from published artifact set at align-closure.

## Intent

- **Intended outcome:** Long-running sub-efforts (workstreams, deliverable threads) without personal-life workstation sprawl.
- **In scope:** Template, start-project prompt option, align-closure exclusion rule.
- **Out of scope:** Cowork Email HQ / personal finance workstations.

## Safety and non-goals

- **Safety posture:** Sub-scaffolds are draft-tier; publish set remains stage artifact files only.
- **Non-goals:** Cross in-progress project dependencies via sub-scaffold wikilinks.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none

## Rationale

Enterprise-safe mapping of Cowork project nesting; bundles RC-058 + RC-130.

## Impact Scores

Total: 9 (experiment)

## Alternatives Considered

- Flat stage dirs only — sufficient for small projects but weak for multi-thread stages.
- Cowork 30 workstations — rejected (RC-168).

## Consequences

### Positive

- Inspectable sub-effort context; supports RC-161 stacking at project depth.

### Negative / Risks

- Folder sprawl; engineers confuse scaffold with publish artifacts.

### Safeguards

- Frontmatter `publish_scope: exclude` on sub-scaffold files; finalize checklist.

## Validation Plan

One pilot project with sub-scaffold for two weeks; align-closure confirms published set excludes scaffold paths.

## Files Proposed for Future Change

- `templates/workspace/project-sub-scaffold/` (new)
- `.github/prompts/workspace-start-project.prompt.md`
- `docs/platform-decision-records/DRAFT-RC-2026-05-27-130-project-stage-scaffold.md` (cross-link)
