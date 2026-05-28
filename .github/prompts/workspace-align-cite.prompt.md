---
description: Verify every cited claim in a project artifact resolves to a source containing the cited content. Production-quality check. Runs automatically before publish.
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

## Inputs

- Path to one artifact, OR a project slug (in which case run on every artifact in `wiki/workspace-projects/{slug}/`)
- Optional `--strict` flag: also flag claims that lack citations (advisory; not all claims require citation)

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

Write a structured report to `reports/workspace-align-cite-{artifact-slug}-{date}.md`:

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

When invoked from `start-project` (pre-publish gate), a FAIL blocks publish unless the user explicitly overrides; overrides are logged.

## Append to log

```
## [{ISO timestamp}] align-cite | {artifact}
- Claims: {N}
- Verified: {N}
- Violations: {N}
- Status: pass | fail
- Report: {report path}
```

## Limitations (be honest with the user)

- VERIFIED means "source found containing the claim," not "definitively correct." Sources can be wrong.
- The verification uses the same model that may have produced the original output; it catches structural issues but not subtle factual errors that pass all three layers.
- Web sources cited in artifacts are not fetched live; offline cache is trusted.
