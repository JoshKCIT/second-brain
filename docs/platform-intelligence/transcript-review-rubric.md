# Transcript Review Rubric

## Purpose

This rubric governs how Second Brain evaluates transcripts from researchers, engineers, stakeholders, and users who discuss how to improve the platform.

The rubric prevents informal discussion from becoming canonical knowledge without review.

## North Star

Second Brain is a governed documentation compiler that produces stage-gated, source-arbitrated, junior-engineer-executable artifact sets with claim-level traceability.

## Non-Negotiable Boundary

Research transcripts may influence Second Brain, but they may not directly become Second Brain.

## What "Better" Means

A claim makes Second Brain better if it improves one or more of these axes without unacceptable regression elsewhere.

| Axis | Better means | Worse means |
|---|---|---|
| Governance | Stronger authority tagging, conflict handling, auditability | More untraceable synthesis |
| Closure | A junior engineer can execute using only the artifact set | Hidden assumptions or missing implementation details |
| Grounding | Claims cite canonical internal or vendor sources | Plausible but uncited output |
| Vendor truth | Vendor capability claims are revalidated against vendor docs | Stale internal claims override vendor truth |
| Inspectability | Retrieval, conflicts, decisions, and rationale are visible | Opaque agent autonomy |
| Maintainability | Simpler conventions, fewer brittle scripts, clean lifecycle | Complex workflow theater |
| Differentiation | Strengthens the governance-and-closure niche | Rebuilds generic RAG, chat, or agent features |
| Enterprise fit | Respects access controls, audit trails, legal, and compliance constraints | Encourages shadow IT or uncontrolled ingestion |
| Human review leverage | Humans review meaningful decisions | Humans rubber-stamp huge AI outputs |

## Claim Taxonomy

Each transcript-derived claim must have exactly one primary type.

| Type | Definition |
|---|---|
| `problem_evidence` | Evidence that a user, engineer, reviewer, or stakeholder experiences a pain |
| `product_requirement` | A proposed behavior Second Brain should support |
| `architecture_proposal` | A proposed implementation or technical design |
| `workflow_proposal` | A proposed human or agent process |
| `evaluation_proposal` | A proposed way to test quality, closure, accuracy, or adoption |
| `market_claim` | A claim about vendors, competitors, standards, tools, or external capabilities |
| `risk_claim` | A claim about security, compliance, hallucination, maintainability, misuse, or adoption risk |
| `principle_claim` | A claim that changes what Second Brain should value |

## Impact Scoring

Score every claim from `-2` to `+2` on each axis.

```text
+2 = strong improvement
+1 = likely improvement
 0 = neutral or unclear
-1 = likely regression
-2 = strong regression
```

## Decision Rules

| Decision | Rule |
|---|---|
| `adopt` | Total score >= +6, no -2 scores, low uncertainty, no unresolved authority conflict |
| `experiment` | Total score +2 to +5, or high uncertainty with plausible upside |
| `defer` | Useful but blocked by missing infrastructure, access, evals, or enterprise constraint |
| `reject` | Total score <= 0, or weakens governance, grounding, inspectability, or closure |
| `monitor` | External market/vendor claim worth tracking but not actionable yet |

## Skeptical Review Questions

For every claim, ask:

1. What assumption must be true for this claim to help?
2. What would a strong skeptic argue?
3. Does this claim make Second Brain more governed, grounded, and executable, or merely more automated?
4. Does this claim preserve the boundary between raw evidence and canonical knowledge?
5. Does this claim duplicate vendor-native enterprise AI features without strengthening Second Brain's niche?
6. Does this claim increase or reduce human review leverage?
7. Can a junior engineer execute better because of this change?
8. Can the change be validated with a realistic documentation task?

## Protected-File Rule

Transcript-derived claims must not directly update:

```text
wiki/workspace-standards/**
wiki/workspace-recommendations/**
PRD.md
product-brief.md
docs/roadmap.md
docs/architecture-rationale.md
AGENTS.md
```

If a claim should affect one of these files, create a draft ADR or recommendation first.

## Example Judgments

### Reject as Stated

Claim:

> Second Brain should automatically update standards pages whenever someone mentions a new best practice in a meeting.

Rationale:

This bypasses source authority, owner review, and canonical-source validation. Better variant: convert the meeting statement into a candidate claim routed through platform research review.

### Adopt or Already Supported

Claim:

> Every generated architecture section should cite the internal standard or vendor page that justifies it.

Rationale:

This strengthens grounding, inspectability, governance, and junior-engineer closure.

### Experiment

Claim:

> A VP, PM, Architect, and Engineer agent should produce docs in sequence.

Rationale:

This fits stage-gated artifact production, but it must be tested against realistic docs. It may become performative unless each agent has a hard acceptance contract.
