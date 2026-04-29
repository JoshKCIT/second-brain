---
description: Verify a project artifact addresses every relevant requirement from in-scope standards. Gap analysis. Best-effort tier (advisory; LLM judgment).
mode: agent
---

# /align-coverage

You are checking whether a project artifact addresses every requirement from in-scope standards that applies to it. Best-effort tier: requirement extraction is non-trivial and LLM judgment is subjective.

## Inputs

- Path to one artifact, OR a project slug
- The project's in-scope standards

## Workflow

### Step 1: Extract requirements from each in-scope standard

For each in-scope standard, read its full content and extract a list of requirements: explicit obligations the standard places on dependent work. Examples:

- "Every service must emit OpenTelemetry traces"
- "All data at rest must use AES-256 encryption"
- "Audit logs must be retained for 7 years"

For each extracted requirement:

- Capture the requirement text
- Note whether it is mandatory ("must"), recommended ("should"), or optional ("may")
- Note the source standard

### Step 2: Determine applicability

For each extracted requirement, decide whether it applies to this artifact:

- Architecture artifacts: requirements about system design, components, integrations
- Engineering artifacts: requirements about implementation, testing, deployment
- PRDs: requirements about user-visible behavior, compliance attestation

Mark each requirement as APPLICABLE or NOT-APPLICABLE.

### Step 3: Check coverage

For each APPLICABLE requirement, search the artifact for content addressing it. Rate:

- ADDRESSED: artifact explicitly addresses this requirement (cited or restated)
- PARTIALLY: artifact references the area but does not fully address the requirement
- MISSING: artifact does not address this requirement

### Step 4: Output

Write a structured report to `reports/align-coverage-{artifact-slug}-{date}.md`:

```markdown
# align-coverage report: {artifact}

Date: {ISO timestamp}
Artifact: {path}
Quality tier: best-effort (advisory)

## Per-standard requirements

### {Standard name}

| Requirement | Mandatory? | Applicable? | Coverage |
|---|---|---|---|
| {req 1} | yes | yes | ADDRESSED |
| {req 2} | yes | yes | MISSING |
| {req 3} | should | yes | PARTIALLY |
| {req 4} | yes | no (not applicable to this artifact type) | N/A |

[repeat per standard]

## Coverage gaps (mandatory requirements only)

### MISSING

- **{requirement}** (from {standard}): suggested action: {what to add to the artifact}

### PARTIALLY

- **{requirement}** (from {standard}): suggested action: {what to clarify or expand}

## Summary

{Overall coverage; mandatory gap count; recommended actions.}
```

## Pass/fail criteria

This check is **advisory**, not gating.

When invoked pre-publish: any MISSING mandatory requirement produces a warning, not a block. The user judges whether the gap is acceptable for the project's scope.

## Append to log

```
## [{ISO timestamp}] align-coverage | {artifact}
- Standards: {N}
- Requirements extracted: {N}
- Applicable: {N}
- Addressed: {N}
- Partial: {N}
- Missing: {N}
- Mandatory missing: {N}
- Quality tier: best-effort (advisory)
- Report: {path}
```

## Honesty about limitations

State explicitly in the report:

> Requirement extraction is non-trivial and LLM-driven; some requirements may be missed (false negatives) and some non-requirements may be flagged as requirements (false positives). Use this report as a checklist guide, not as a definitive coverage statement. v1.x will improve this check with structured requirement extraction or labeled standards.

## Adoption recommendation

Run `align-coverage` before formal review by the standards-publishing teams (Architecture, Security, Audit). Their feedback may surface requirements the LLM missed; over time, refine the in-scope standards' wiki articles with explicit requirements lists to improve extraction accuracy.
