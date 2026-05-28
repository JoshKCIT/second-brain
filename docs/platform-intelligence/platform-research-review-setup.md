# Platform Research Review Setup

## Purpose

The platform-research-review workflow evaluates transcripts, meeting notes, interviews, and product-improvement discussions as product intelligence for Second Brain.

It does not import those sources into canonical knowledge. Transcript-derived claims must be extracted, grounded, scored, and routed through a decision artifact before they influence standards, roadmap, architecture, or product requirements.

## Use with a Transcript

Place a transcript here:

```text
raw/platform-transcripts/{slug}/transcript.md
```

Optional metadata:

```text
raw/platform-transcripts/{slug}/metadata.yml
```

Then invoke the platform-research-review prompt:

```text
/platform-research-review Review @raw/platform-transcripts/{slug}/transcript.md for Second Brain product impact.

Use @AGENTS.md, @product-brief.md, @PRD.md, @docs/architecture-rationale.md, @docs/roadmap.md, and @wiki/platform-research/claim-register.md if present.

Extract atomic claims, score each claim, update the claim register, and write the research impact report.

Do not modify raw files, standards, recommendations, PRD, product brief, roadmap, architecture rationale, or AGENTS.md.
```

In Cursor, you can also invoke the `platform-research-reviewer` subagent directly for the same workflow.

## Expected Outputs

```text
wiki/platform-research/transcript-analyses/{slug}-claims.md
reports/platform-research-review/{slug}-impact-report.md
wiki/platform-research/claim-register.md
wiki/platform-research/rejected-ideas.md
wiki/platform-research/open-hypotheses.md
```

For batch reviews, also produce:

```text
reports/platform-research-review/batch-synthesis-{date}.md
reports/platform-research-review/final-recommendations-{date}.md
wiki/platform-research/implementation-backlog.md
```

Optional outputs:

```text
docs/platform-decision-records/DRAFT-{claim_id}-{short-title}.md
reports/platform-research-review/claim-stack-analysis-{date}.md
```

## Artifact package

Platform research is structured claim-plus-evidence, not transcript summary. Each review should preserve:

- atomic claims with scores and decisions
- rejected ideas with rationale and re-review dates
- open experiments and validation targets
- stack-lift implementation ordering for approved claims

Run validation after each review:

```bash
python scripts/lint-platform-research.py --root .
```

## Trust loop

Platform research reviews apply the trust-loop pattern (`templates/platform-research/trust-loop.md`):

- Every claim record includes `validation_status` and `correction_route`.
- Fail closed: no `adopt` when external validation is required but still `unvalidated`.
- Impact reports include trust summary and correction routes.

## Implementation priority loop

After the user approves a draft ADR, deliver canonical changes one claim at a time:

1. Load `wiki/platform-research/implementation-backlog.md`
2. Select the top `queued` item with satisfied dependencies
3. Implement the smallest reversible change
4. Run `python -m unittest discover -s tests` and `python scripts/lint-platform-research.py --root .`
5. Present results to the user for accept or rollback
6. Re-score the backlog and continue

Process ADR: `docs/platform-decision-records/DRAFT-RC-implementation-priority-loop.md`

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
wiki/platform-research/**
reports/platform-research-review/**
docs/platform-decision-records/DRAFT-*.md
```

It must not directly modify:

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

If a canonical file should change, the agent should create a draft decision record instead.
