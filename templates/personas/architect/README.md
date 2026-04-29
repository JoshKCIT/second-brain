# Architect Persona Template (stub for v1.x)

This template is a documented stub. Population is queued for v1.x.

## Operating mode

The Architect operator runs Second Brain to:

- Ingest standards from multiple cross-cutting teams (Architecture, Security, Audit, Data, SRE, Engineering)
- Produce cross-system documentation (RFCs, system designs, integration specs, ADRs)
- Validate architectural choices against in-scope standards and vendor capabilities
- Maintain a personal synthesis across multiple architectural initiatives

## Default in-scope source preferences (proposed for v1.x)

| Space | Authority | Domain |
|---|---|---|
| Architecture | standard | internal |
| Security | standard | internal |
| Audit | standard | internal |
| Data Modeling | standard | internal |
| SRE Runbooks | recommendation | internal |
| Engineering Standards | recommendation | internal |
| Multiple vendor docs | standard | vendor:{name} |
| Industry standards (NIST, etc.) | standard | industry:{name} |

## Common Architect project doc types

- Architecture Decision Records (ADRs) — heavy use; the `adr-generator` agent is invoked frequently
- Cross-system architecture documents
- Integration specifications
- RFCs
- Capability assessments and option comparisons
- Migration architecture plans

## What needs to be populated for v1.x

- Architect-specific prompt overrides emphasizing comparison and tradeoff analysis
- Example workflows for cross-team initiatives
- Heavier emphasis on ADR generation in the agent chain
- Schema additions for system-design artifacts
- Starter wiki structure with cross-team standards pre-categorized

## Status

Stub. To populate, see `templates/personas/ceo/README.md` for structure.
