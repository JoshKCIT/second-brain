# Research Review Setup

## Purpose

The research-review workflow evaluates transcripts, meeting notes, interviews, and product-improvement discussions as product intelligence for Second Brain.

It does not import those sources into canonical knowledge. Transcript-derived claims must be extracted, grounded, scored, and routed through a decision artifact before they influence standards, roadmap, architecture, or product requirements.

## Use with a Transcript

Place a transcript here:

```text
raw/transcripts/{slug}/transcript.md
```

Optional metadata:

```text
raw/transcripts/{slug}/metadata.yml
```

Then invoke the research-review prompt:

```text
/research-review Review @raw/transcripts/{slug}/transcript.md for Second Brain product impact.

Use @AGENTS.md, @product-brief.md, @PRD.md, @docs/architecture-rationale.md, @docs/roadmap.md, and @wiki/research/claim-register.md if present.

Extract atomic claims, score each claim, update the claim register, and write the research impact report.

Do not modify raw files, standards, recommendations, PRD, product brief, roadmap, architecture rationale, or AGENTS.md.
```

In Cursor, you can also invoke the `research-reviewer` subagent directly for the same workflow.

## Expected Outputs

```text
wiki/research/transcript-analyses/{slug}-claims.md
reports/research-review/{slug}-impact-report.md
wiki/research/claim-register.md
```

Optional outputs:

```text
docs/decision-records/DRAFT-{claim_id}-{short-title}.md
```

## Acceptance Criteria

A successful review:

- Extracts atomic claims rather than vague themes.
- Classifies every claim.
- Identifies assumptions and validation gaps.
- Scores each claim across the nine axes.
- Rejects attractive but governance-damaging ideas.
- Distinguishes adoptable claims from experiments.
- Does not edit protected canonical files directly.

## Protected Files

Research review may create or update:

```text
wiki/research/**
reports/research-review/**
docs/decision-records/DRAFT-*.md
```

It must not directly modify:

```text
raw/**
wiki/standards/**
wiki/recommendations/**
PRD.md
product-brief.md
docs/roadmap.md
docs/architecture-rationale.md
AGENTS.md
```

If a canonical file should change, the agent should create a draft decision record instead.
