---
name: platform-research-review
description: Review researcher transcripts, meeting notes, interviews, and product-improvement discussions for Second Brain product impact using claim extraction, grounding, skeptical scoring, and controlled decision records.
---

# Platform Research Review Skill

Use this skill when the user asks to evaluate transcripts, meeting notes, interviews, or product-improvement discussions for the Second Brain project.

## Purpose

Convert informal discussion into controlled product intelligence without allowing transcript-derived statements to become canonical knowledge by accident.

## Core Rule

Research transcripts may influence Second Brain, but they may not directly become Second Brain.

## Workflow

1. Identify the transcript under `raw/platform-transcripts/**` or the user-specified source note.
2. Inspect relevant project docs: `AGENTS.md`, `product-brief.md`, `PRD.md`, `docs/architecture-rationale.md`, `docs/roadmap.md`, and `wiki/platform-research/claim-register.md` if present.
3. Segment the transcript into discussion blocks.
4. Extract atomic claims.
5. Classify claims.
6. Ground claims against existing docs and relevant sources.
7. Score product impact.
8. Decide `adopt`, `experiment`, `defer`, `reject`, or `monitor`.
9. Update `wiki/platform-research/claim-register.md`.
10. Write `reports/platform-research-review/{slug}-impact-report.md`.
11. Create draft ADRs for adopted or experimental claims only.

## Write Boundaries

Allowed:

- `wiki/platform-research/**`
- `reports/platform-research-review/**`
- `docs/platform-decision-records/DRAFT-*.md`

Protected:

- `raw/**`
- `wiki/workspace-standards/**`
- `wiki/workspace-recommendations/**`
- `PRD.md`
- `product-brief.md`
- `docs/roadmap.md`
- `docs/architecture-rationale.md`
- `AGENTS.md`

## Quality Bar

A good platform-research-review output is not a transcript summary. It is a decision artifact that tells the user which claims improve Second Brain, which claims are dangerous, which claims need experiments, and which claims are generic roadmap noise.
