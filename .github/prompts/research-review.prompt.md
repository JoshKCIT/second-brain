---
description: Review transcripts, meeting notes, or product-improvement discussions as controlled product intelligence. Extract claims, ground them against Second Brain docs, score product impact, and write research-review artifacts without mutating canonical docs.
mode: agent
---

# /research-review

You are reviewing a transcript, meeting note, interview, or product-improvement discussion for the Second Brain project.

## Objective

Extract atomic claims from the source, evaluate whether each claim would make Second Brain better or worse, and produce controlled research-review artifacts.

## Inputs

Use the transcript or note specified by the user, normally under:

```text
raw/transcripts/{slug}/transcript.md
```

Inspect these project files when present:

```text
AGENTS.md
product-brief.md
PRD.md
docs/architecture-rationale.md
docs/roadmap.md
wiki/research/claim-register.md
config/research-review.example.yml
```

## North Star

Second Brain is a governed documentation compiler that produces stage-gated, source-arbitrated, junior-engineer-executable artifact sets with claim-level traceability.

## Non-Negotiable Rule

Research transcripts may influence Second Brain, but they may not directly become Second Brain.

Treat transcripts as product-intelligence evidence, not canonical knowledge. A transcript can justify a candidate claim, experiment, rejection, or draft ADR. It cannot by itself justify changing standards, recommendations, the roadmap, the PRD, architecture rationale, or raw source mirrors.

## Required Steps

1. Normalize transcript metadata.
2. Segment transcript into discussion blocks.
3. Extract atomic claims.
4. Classify each claim using the approved taxonomy.
5. Identify assumptions and evidence quality.
6. Ground each claim against existing Second Brain docs.
7. Run skeptical review.
8. Score each claim on the nine impact axes.
9. Decide: `adopt`, `experiment`, `defer`, `reject`, or `monitor`.
10. Update or create `wiki/research/claim-register.md`.
11. Write `wiki/research/transcript-analyses/{slug}-claims.md`.
12. Write `reports/research-review/{slug}-impact-report.md`.
13. Draft ADRs only for adopted or experimental claims.

## Protected Files

Do not directly modify:

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

If a protected file should change, create a draft decision record under `docs/decision-records/DRAFT-*.md` instead, then ask for explicit approval before any follow-up mutation.

## Output Files

For a transcript at:

```text
raw/transcripts/{slug}/transcript.md
```

write:

```text
wiki/research/transcript-analyses/{slug}-claims.md
reports/research-review/{slug}-impact-report.md
```

Update or create:

```text
wiki/research/claim-register.md
```

If a claim is adopted or moved to experiment, optionally create:

```text
docs/decision-records/DRAFT-{claim_id}-{short-title}.md
```

## Final Response

Summarize:

- Files created or updated
- Claim counts by decision
- Strongest adoption or experiment candidate
- Strongest rejection
- Validation gaps
- Protected files not modified
