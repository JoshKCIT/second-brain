# Engineer Persona Template (stub for v1.x)

This template is a documented stub. Population is queued for v1.x.

## Operating mode

The Engineer operator runs Second Brain to:

- Ingest in-scope architecture, coding, deployment, and runbook standards
- Produce technical documentation grounded in those standards (design docs, ADRs, runbooks, RFCs)
- Validate vendor capability claims against vendor docs
- Maintain a personal knowledge layer across multiple ongoing engineering projects

## Default in-scope source preferences (proposed for v1.x)

| Space | Authority | Domain |
|---|---|---|
| Architecture | standard | internal |
| Engineering Standards | standard | internal |
| SRE Runbooks | recommendation | internal |
| Security | standard | internal |
| Data Modeling | standard | internal |
| Vendor docs (AWS, Snowflake, etc., as needed) | standard | vendor:{name} |

## Common Engineer project doc types

- Architecture decision records (ADRs)
- Design documents
- Runbooks
- Implementation specs
- Migration plans
- Code review checklists tied to specific projects

## What needs to be populated for v1.x

- Specific in-scope source recommendations for typical engineering teams
- Engineer-tailored prompt overrides (if any)
- Example workflows: "I'm starting a new service" / "I'm doing a tech-debt audit" / "I'm onboarding to an existing system"
- Schema additions in `AGENTS-additions.md` if engineer-specific frontmatter or article types are needed
- Starter wiki structure
- Example exemplar published doc tailored to engineering output

## Status

Stub. To populate, see `templates/personas/ceo/README.md` for structure.
