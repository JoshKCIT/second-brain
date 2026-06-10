# DRAFT ADR: RC-2026-06-09-013 - Three-Pass Compile Orientation Map

## Status

Draft

## Source Claim

- Claim ID: RC-2026-06-09-013
- Source transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
- Speaker: unknown
- Timestamp: 00:02:00-00:03:30, 00:07:30-00:11:30
- Claim type: workflow_proposal

## Context

Graphify builds orientation in three passes: (1) deterministic structure (tree-sitter, no LLM), (2) media transcription, (3) LLM semantic enrichment for unstructured docs. Second Brain already experiments with disposable orientation maps (RC-008, RC-009) deferred in favor of Obsidian graph. This ADR proposes a Graphify-inspired **three-pass disposable orientation artifact** for compile-time agent routing over the compiled wiki—not repo-wide Graphify installation.

## Decision

Experiment with a regenerable `orientation-map` (draft-tier, non-canonical) generated at compile or session start:

1. **Pass 1 (deterministic, zero LLM):** Traverse `wiki/index.md`, in-scope article frontmatter, wikilinks, and section headings; emit structure graph or outline.
2. **Pass 2 (optional, low-cost):** Extract text from attachments/media in raw when present (no auto-write to wiki).
3. **Pass 3 (LLM, scoped):** Semantic summaries only for unstructured inbox/quarantine items not yet compiled—never promote to wiki without approval.

Agents may read the map for routing; align-cite and publish closure rules unchanged.

## Intent

- **Intended outcome:** Reduce blind reads during compile and project authoring without treating the map as evidence or canonical knowledge.
- **In scope:** Pilot script or verb producing disposable Markdown/JSON orientation report; lint ensuring no wiki promotion without compile approval.
- **Out of scope:** Graphify dependency; always-on hooks; substituting align-cite; indexing `scripts/` as product retrieval substrate.

## Safety and non-goals

- **Safety posture:** Orientation map is advisory; `validation_status: unvalidated` on any LLM-derived pass-3 nodes; fail closed on inference write-back (RC-020).
- **Non-goals:** Persistent agent memory; canonical graph database; token-optimization as primary success metric without closure checks.

## Regulatory posture (optional)

- **Legal/regulatory claims:** none
- **Notes:** N/A

## Rationale

Extends RC-009 safer variant with a concrete pipeline pattern from transcript evidence. Keeps structure-first discipline (RC-001) while limiting LLM cost to genuinely unstructured inputs.

## Impact Scores

governance +1, closure +1, grounding +0, inspectability +1, maintainability -1, human_review_leverage +1; total +3 (experiment band with upside)

## Alternatives Considered

1. **Install Graphify** — rejected (RC-009a; external tooling dependency).
2. **Obsidian graph only** — current default; re-enter if insufficient (RC-007/008 deferred).
3. **Full embedding index** — holdout-gated; out of v1 scope.

## Consequences

### Positive

- May reduce orientation reads on multi-standard compile tasks.
- Pass 1 aligns with inspectable, deterministic retrieval policy.

### Negative / Risks

- Stale orientation map misleads agents if not regenerated.
- Pass 3 could leak unvalidated inferences into agent context.

### Safeguards

- TTL or session-scoped regeneration; watermark `not_canonical: true`.
- Holdout: align-cite pass rate and publish closure vs baseline index-only workflow.
- No default enablement; CEO-approved pilot only.

## Validation Plan

- One workspace project compile pilot: compare orientation read count, align-cite violations, and time-to-first-draft vs baseline.
- Track in `wiki/platform-research/open-hypotheses.md` as H-2026-06-09-004.

## Files Proposed for Future Change

- `templates/workspace/orientation-map.md` (new scaffold)
- `.github/prompts/workspace-compile.prompt.md` (optional advisory read)
- `scripts/generate-orientation-map.py` (pilot)
- `wiki/platform-research/open-hypotheses.md`
