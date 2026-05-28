# Claims Analysis: OpenCode + Graphify

## Source

- Transcript: `raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt`
- Processing limitations: tool tutorial and sponsored content; product claims are unvalidated.
- Review lens: `docs/platform-intelligence/closure-compile-review-brief.md` (2026-05-27 re-review)

## Executive Judgment

Under a **closure–compile** lens, this transcript is about **authoring-time orientation** across many sources so agents can draft **publishable, self-contained** artifact sets—not about becoming a generic IDE codebase assistant. The mixed graph idea is misaligned **as stated** (static code analysis + repo indexing for v1), but a **safer variant** aligns with RC-008: a disposable orientation map over wiki, project artifacts, and cached vendor/Confluence-derived Markdown to reduce blind reads before `align-cite` and publish.

## Extracted Claims

| Claim ID | Type | Decision | Summary |
|---|---|---|---|
| RC-2026-05-27-009 | `architecture_proposal` | experiment | **Safer variant:** regenerable cross-source orientation map (standards, concepts, project stages, vendor cache) at session start to compile jr-engineer-executable publish sets—not v1 repo-wide code indexing. |
| RC-2026-05-27-009a | `architecture_proposal` | reject | **As stated:** full mixed code/docs/media graph via static analysis + transcription for generic coding-agent orientation (IDE assistant scope). |

## Re-review (closure–compile lens)

| Field | Prior (scope) | Updated |
|---|---|---|
| RC-2026-05-27-009 | `reject` — codebase assistant | `experiment` — safer variant for compile-time pull; pairs with RC-008 |
| Primary risk reframed | “Scope creep to Cody” | “Canonical graph replaces inline rules at publish” — mitigated by disposable, non-canonical orientation |

## Grounding Notes

- `AGENTS.md` closure rule: published body inlines executable rules; See Also holds verification links.
- Page-index retrieval (RC-001/002) already covers structure-aware compile; orientation map is an optional accelerator, not evidence.
- Full code-as-source indexing remains v2; reject **009a** preserves that boundary.

## Recommended Next Actions

- Experiment: session orientation report over `wiki/index.md` + in-scope articles (with RC-008).
- Do not install Graphify/OpenCode hooks by default.
- Evaluate against holdout: citation precision and publish closure unchanged or improved.
