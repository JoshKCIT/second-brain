---
description: Review transcripts, meeting notes, or product-improvement discussions as controlled product intelligence. Extract claims, ground them against Second Brain docs, score product impact, and write platform-research-review artifacts without mutating canonical docs.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: platform
---

# /platform-research-review

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are reviewing a transcript, meeting note, interview, or product-improvement discussion for the Second Brain project.

## Objective

Extract atomic claims from the source, evaluate whether each claim would make Second Brain better or worse, and produce controlled platform-research-review artifacts.

## Inputs

Use the transcript or note specified by the user, normally under:

```text
raw/platform-transcripts/{slug}/transcript.md
```

Inspect these project files when present:

```text
AGENTS.md
product-brief.md
PRD.md
docs/architecture-rationale.md
docs/roadmap.md
wiki/platform-research/transcript-register.md
wiki/platform-research/claim-register.md
wiki/platform-research/rejected-ideas.md
wiki/platform-research/open-hypotheses.md
wiki/platform-research/implementation-backlog.md
config/platform-research-review.example.yml
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
10. Update or create `wiki/platform-research/claim-register.md`.
11. Write `wiki/platform-research/transcript-analyses/{slug}-claims.md`.
12. Write `reports/platform-research-review/{slug}-impact-report.md`.
13. Draft ADRs only for adopted or experimental claims.
14. For every `reject` decision, add or update a full record in `wiki/platform-research/rejected-ideas.md` with rationale, safer variant, and `next_review_after`.
15. For recurring unsafe patterns, add `RP-*` records in `wiki/platform-research/rejected-ideas.md`.
16. For batch reviews, write `reports/platform-research-review/batch-synthesis-{date}.md` and update `wiki/platform-research/implementation-backlog.md` with stack-lift priority scores for adopt/experiment/defer claims.
17. Run `python scripts/sync-transcript-register.py --root .` to update the transcript queue index.
18. Run `python scripts/lint-platform-research.py --root .` before finishing.

## Trust loop

Apply the trust-loop pattern to every review output. Template: `templates/platform-research/trust-loop.md`.

1. **Capture** — preserve raw transcript; do not mutate `raw/**`.
2. **Schema** — write typed claim records with required trust fields.
3. **Audit** — log decisions in claim register and impact report.
4. **Confidence** — set `validation_status` on every claim.
5. **Guardrail** — fail closed: do not `adopt` when `requires_external_validation: true` and `validation_status` is `unvalidated`.
6. **Surface** — impact report includes `## Trust Loop Summary` and `## Correction Routes`.
7. **Correct** — set `correction_route` on every claim so the user can approve, reject, or reopen without reading the full transcript.

## Artifact package

Each review produces a claim-plus-evidence package:

```text
wiki/platform-research/transcript-register.md
wiki/platform-research/claim-register.md
wiki/platform-research/rejected-ideas.md
wiki/platform-research/open-hypotheses.md
wiki/platform-research/implementation-backlog.md
wiki/platform-research/transcript-analyses/{slug}-claims.md
reports/platform-research-review/{slug}-impact-report.md
docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md
```

Do not promote transcript claims into canonical docs. After the user approves a draft ADR, use the implementation backlog to deliver one approved change at a time with validation and rollback.

## Controlled platform gap review (experiment RC-2026-05-27-003)

Separate from transcript review. Use `.github/prompts/platform-research-review/gap-review.prompt.md` or invoke `/platform-gap-review` when the user wants a proactive platform gap scan.

- **Cadence:** monthly, manual, user-triggered
- **Outputs:** `reports/platform-research-review/gap-review-{date}.md`; optional updates to `open-hypotheses.md`
- **Must not:** ingest sources, mutate protected files, or update workspace wiki
- **Must:** check `rejected-ideas.md` before proposing rediscovered unsafe patterns

Template: `templates/platform-research/gap-review-report.md`

## Protected Files

Do not directly modify:

```text
raw/**
wiki/workspace-standards/**
wiki/workspace-recommendations/**
PRD.md
product-brief.md
docs/roadmap.md
docs/architecture-rationale.md
AGENTS.md
```

If a protected file should change, create a draft decision record under `docs/platform-decision-records/DRAFT-*.md` instead, then ask for explicit approval before any follow-up mutation.

## Output Files

For a transcript at:

```text
raw/platform-transcripts/{slug}/transcript.md
```

write:

```text
wiki/platform-research/transcript-analyses/{slug}-claims.md
reports/platform-research-review/{slug}-impact-report.md
```

Update or create:

```text
wiki/platform-research/claim-register.md
wiki/platform-research/rejected-ideas.md
wiki/platform-research/open-hypotheses.md
```

If a claim is rejected, add a full historical record to `wiki/platform-research/rejected-ideas.md` (not just a one-line summary).

If a claim is adopted or moved to experiment, optionally create:

```text
docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md
```

Use `templates/platform-research/platform-adr.md` (includes lightweight **Intent**, **Safety and non-goals**, and optional **Regulatory posture** sections per experiment RC-2026-05-27-015). Do not copy unvalidated legal claims from transcripts into canonical requirements.

## Final Response

Summarize:

- Files created or updated
- Claim counts by decision
- Strongest adoption or experiment candidate
- Strongest rejection
- Validation gaps
- Protected files not modified
