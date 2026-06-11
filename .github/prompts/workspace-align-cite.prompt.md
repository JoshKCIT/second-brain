---
description: Verify every cited claim in a project artifact resolves to a source containing the cited content. Hybrid gate — a deterministic core (second-brain align-cite) runs automatically before publish and blocks; this LLM layer adds semantic judgment and never relaxes a mechanical FAIL.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-align-cite

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are verifying citation integrity in a project artifact. Every claim that has a citation must actually be supported by the cited source. Adapted from a three-layer verification pattern: extract claims, verify against sources, adversarial review for hallucination patterns.

## Hybrid gate (Decision A): deterministic core runs first

This gate has two halves. The **deterministic core** runs first and is the
publish blocker; your LLM layer runs second and adds semantic judgment.

**Deterministic core (mechanical, in code):**

```
second-brain align-cite {artifact-path-or-slug}
```

(equivalently `python -m second_brain align-cite ...`). It writes
`reports/workspace-align-cite-{project}-{date}.md` and exits non-zero on any of:
every cited `sources:` path must exist; every quoted span (blockquote or long
inline quote) must occur verbatim in a cited source; a `domain: vendor:X`
artifact must cite at least one `vendor:X` source. **A non-zero exit is a hard
block.**

**Your LLM layer (this prompt) runs second:**

- Operate on the rows the deterministic core marked **PASS**.
- You may **downgrade** a mechanical PASS to FAIL (e.g. a bad-faith match: the
  cited source contains the words but contradicts the claim in context).
- You may **never upgrade** a mechanical FAIL to PASS. A deterministic FAIL
  stands regardless of your judgment.
- Cover what the mechanical layer cannot: paraphrased claims, semantic support,
  hallucination patterns, cross-domain conflicts.

Invariant: retrieval may decide what to read; only this verification decides what
may publish.

## Inputs

- Path to one artifact, OR a project slug (in which case run on every artifact in `wiki/workspace-projects/{slug}/`)
- Optional `--strict` flag: also flag claims that lack citations (advisory; not all claims require citation)
- Optional `--advisory` flag (PH-004): same verification layers; **non-blocking** at stage gates. Use before CEO review per `templates/workspace/advisory-align-cite-per-stage.md`

## Three-layer verification

### Layer 1: Self-audit (extract claims)

Re-read the artifact critically. Extract every verifiable claim: facts, statistics, citations, dates, decisions, capability assertions. For each claim, note:

- Claim text
- Claimed source (the citation in the artifact)
- Domain (internal, vendor:X, industry:Y, undeclared)
- Whether the claim is in body prose, See Also, frontmatter, or comments

Categorize claims:

- **CITED**: has an explicit citation
- **UNCITED**: makes a fact-bearing assertion without citation
- **OPINION**: subjective; not subject to citation

### Layer 2: Source verification (per claim)

For each CITED claim:

1. Resolve the citation: locate the source file or URL
2. Read the source content
3. Verify the source contains content supporting the claim
4. Rate: VERIFIED (source contains the claim), PLAUSIBLE (source is on-topic but does not directly state the claim), UNVERIFIED (cannot find supporting content), DISPUTED (source contradicts the claim), FABRICATION RISK (source does not exist, link is broken, or claim matches a hallucination pattern)

For citation targets:

- `wiki/...` paths: read the wiki article
- `raw/...` paths: read the raw page
- External URLs: do not fetch live; trust the cached `raw/workspace-external/` if it exists, otherwise mark as PLAUSIBLE with note "external source not cached locally"
- Confluence URLs (when source is `raw/workspace-confluence/{space}/pages/.../`): treat the `raw/` cache as the source of truth

### Layer 3: Adversarial review

Switch posture: assume the artifact contains errors. Check against hallucination patterns:

- **Fabricated citations:** citation points to a file or URL that does not exist
- **Confident specificity on uncertain topics:** specific numbers or dates without source
- **Missing qualifiers:** absolute statements that should be hedged
- **Temporal confusion:** claims using outdated information
- **Cross-domain conflict:** vendor claim cited from internal source (or vice versa); also caught by `align-vendor-truth`

## Output

Write a structured report to:

- **Default (blocking):** `reports/workspace-align-cite-{artifact-slug}-{date}.md`
- **`--advisory` (PH-004):** `reports/workspace-advisory-align-cite-{stage}-{slug}-{date}.md` where `{stage}` is `vp-brief`, `pm-prd`, `architecture`, or `engineering` from artifact frontmatter

```markdown
# align-cite report: {artifact}

Date: {ISO timestamp}
Artifact: {path}
Claims extracted: {N}
- VERIFIED: {count}
- PLAUSIBLE: {count}
- UNVERIFIED: {count}
- DISPUTED: {count}
- FABRICATION RISK: {count}

## Violations

### {Severity: error / warning} - Claim N

**Claim:** {text}
**Cited source:** {citation}
**Rating:** {DISPUTED | FABRICATION RISK | etc.}
**Issue:** {specific problem}
**Suggested action:** {refetch source / restate claim / verify externally}

[repeat per violation]

## Uncited claims (if --strict)

[list]

## Summary

{Overall pass/fail; severity breakdown; recommended next step.}
```

## Pass/fail criteria

- **PASS:** zero DISPUTED or FABRICATION RISK ratings; UNVERIFIED count is acceptable (advisory only)
- **FAIL:** any DISPUTED or FABRICATION RISK rating

When invoked from `start-project` **Step 12** (pre-publish gate), a FAIL blocks publish unless the user explicitly overrides; overrides are logged.

When invoked with **`--advisory` (PH-004)** before a CEO stage gate:

- Use the same PASS/FAIL ratings in the report header
- Label summary as `Status: pass (advisory)` or `Status: fail (advisory)`
- **Never block** gate progression, PH-003 forward, or PH-005 reopen
- Update stage `handoff.md` **Advisory cite check** per `templates/workspace/advisory-align-cite-per-stage.md`
- Recommend fixing DISPUTED / FABRICATION RISK items before CEO approval; CEO may proceed anyway

## Append to log

**Blocking run:**

```
## [{ISO timestamp}] align-cite | {artifact}
- Claims: {N}
- Verified: {N}
- Violations: {N}
- Status: pass | fail
- Report: {report path}
```

**Advisory run (PH-004):**

```
## [{ISO timestamp}] advisory-align-cite | {slug} | {stage}
- Artifact: {path}
- Claims: {N}
- Violations: {N}
- Status: pass (advisory) | fail (advisory) | skipped
- Report: {report path or —}
```

## Limitations (be honest with the user)

- VERIFIED means "source found containing the claim," not "definitively correct." Sources can be wrong.
- The verification uses the same model that may have produced the original output; it catches structural issues but not subtle factual errors that pass all three layers.
- Web sources cited in artifacts are not fetched live; offline cache is trusted.
