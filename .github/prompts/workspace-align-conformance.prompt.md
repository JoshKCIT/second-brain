---
description: Verify a project artifact's structure, terminology, and decisions match each in-scope standard's conventions. Best-effort tier (advisory; LLM judgment).
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-align-conformance

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are checking that a project artifact conforms to the conventions of each in-scope standard. Best-effort tier: outputs are advisory; LLM judgment is subjective.

## Inputs

- Path to one artifact, OR a project slug
- The project's in-scope standards (from `wiki/workspace-projects/{slug}/meta.yml` and `config/second-brain.yml`)

## Workflow

### Step 1: Identify applicable standards

For each in-scope standard, decide whether it applies to this artifact:

- Architecture standards apply to architecture and engineering artifacts
- Security standards apply if the artifact touches authentication, authorization, data handling
- Audit standards apply if the artifact has compliance implications
- Coding standards apply to engineering specs only
- Documentation standards apply to all artifacts

### Step 2: Per-standard conformance check

For each applicable standard, verify three dimensions:

**Structure:**
- Does the artifact use the section structure the standard expects?
- Example: Architecture standard requires "Decision Rationale" section in every architecture doc; check the artifact has it.

**Terminology:**
- Does the artifact use the standard's vocabulary consistently?
- Example: Standard uses "service" instead of "microservice"; check the artifact does the same.

**Decisions:**
- Does the artifact's decisions align with the standard's recommended choices?
- Example: Standard recommends OpenTelemetry for observability; check the artifact does not use a different stack without justification.

For each dimension, rate: CONFORMS (matches), PARTIAL (mostly matches with minor deviations), DEVIATES (clear non-compliance), N/A (not addressed by the standard).

### Step 3: Output

Write a structured report to `reports/workspace-align-conformance-{artifact-slug}-{date}.md`:

```markdown
# align-conformance report: {artifact}

Date: {ISO timestamp}
Artifact: {path}
Quality tier: best-effort (advisory)

## Per-standard results

### {Standard name} (Authority: standard, Domain: internal)

**Structure:** CONFORMS | PARTIAL | DEVIATES | N/A
- {Specific observations}

**Terminology:** CONFORMS | PARTIAL | DEVIATES | N/A
- {Specific observations}

**Decisions:** CONFORMS | PARTIAL | DEVIATES | N/A
- {Specific observations}

[repeat per standard]

## Summary

{Overall conformance assessment; recommended revisions if any.}
```

## Pass/fail criteria

This check is **advisory**, not gating. Output is informational; the user judges whether to act on it.

When invoked pre-publish, a DEVIATES rating produces a warning, not a block.

## Append to log

```
## [{ISO timestamp}] align-conformance | {artifact}
- Standards checked: {N}
- Conforms: {N}
- Partial: {N}
- Deviates: {N}
- Quality tier: best-effort (advisory)
- Report: {path}
```

## Honesty about limitations

State explicitly in the report:

> This check uses LLM judgment to assess subjective conformance. Results may be inconsistent across runs. Use as a starting point for review, not as a gating decision. v1.x will improve this check with rule-based extraction or labeled exemplars.
