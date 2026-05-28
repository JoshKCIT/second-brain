---
description: Status-aware closure check. At review/published, body prose contains no internal wikilinks. Cross-project dependency rules enforced. Junior-engineer-executable bar verified.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-align-closure

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are verifying that a project's authored set is jr-engineer-executable using only itself, and that body prose follows status-appropriate rules.

## Inputs

- Project slug (run on every artifact in `wiki/workspace-projects/{slug}/`)

## Status-aware rules

For each artifact, read its `status` frontmatter and apply the corresponding rules.

### `draft` (lenient)

- Body wikilinks ARE allowed (agent collaboration phase)
- TODOs, NEEDS-INPUT, Open Questions allowed
- Frontmatter must be present and complete

Check only:
- Frontmatter completeness
- No links to non-existent files (broken wikilinks)
- No cross-project dependency violations (always enforced regardless of status)

### `review` (stricter)

- Body prose must contain NO internal `[[wikilinks]]`
- Navigation links must live in `## See Also` section or in frontmatter (`related:`, `cross_refs:`)
- External URLs (`[text](url)`) are allowed in body
- TODOs, NEEDS-INPUT, Open Questions still allowed (but should be resolved before publish)

Check:
- All `draft`-tier checks
- Body-prose-clean: walk every `[[...]]` pattern in the artifact and verify it is inside `## See Also` or frontmatter
- Any wikilink in body is a violation

### `published` (strictest)

- All `review`-tier rules
- TODOs, NEEDS-INPUT must be resolved or moved to a clearly-marked addendum section
- Open Questions section is allowed (preserves transparency about unresolved items)
- Vendor citations follow parenthetical-plus-See-Also pattern
- Internal standards follow inline-rules-plus-Confluence-URL pattern (the URL goes in See Also; the rules are inline)

Check:
- All `review`-tier checks
- TODO / NEEDS-INPUT scan; flag any unresolved
- Vendor citation pattern compliance (claims like "AWS supports X" should have parenthetical + See Also; not just an inline URL)
- Internal standard citation pattern compliance (rules inlined in body; URL in See Also)

### `archived` (frozen)

- Read-only state; no checks needed beyond verifying `archived: true` and `archived_at` are set

## Cross-project dependency rule (enforced at every status)

For each `[[wikilink]]` in the artifact (whether in body, See Also, or frontmatter):

- If it points to another project (`wiki/workspace-projects/{other-slug}/...`), check the other project's status:
  - **Pass:** other project is `published`
  - **Fail:** other project is `in-progress` (any sub-status) or `archived`
- If it points to wiki/workspace-standards, wiki/workspace-recommendations, wiki/workspace-informational, wiki/workspace-concepts, wiki/workspace-connections: pass (these are referenceable regardless)
- External URLs and same-project wikilinks (in See Also, etc.): pass

For each FAIL on cross-project dependency, present resolution options to the user:

1. **Finish dependency:** the other project must transition to `published` first
2. **Archive dependency:** if the other project is no longer relevant, archive it; this artifact must then be restated to remove the dependency
3. **Restate:** rewrite this artifact to not depend on the other project (inline the needed content from the other project's published artifacts, or extract a `wiki/workspace-concepts/` article)

## Junior-engineer executability test (heuristic at published status)

For each artifact at `published`:

- Identify any place where the body refers to "the [Standard Name]" or similar without inlining the relevant rule. Flag these.
- Identify any place where the body says "see [link]" without summarizing what the link contains. Flag these.
- Identify undefined acronyms or jargon used in body prose. Flag these.

These flags are advisory; they help the author refine before publish but are not strict failures.

## Output

Write a structured report to `reports/workspace-align-closure-{slug}-{date}.md`:

```markdown
# align-closure report: {slug}

Date: {ISO timestamp}
Project: {slug}
Artifacts checked: {N}

## Per-artifact results

### {artifact path} (status: {status})
- Body wikilinks in violation: {count} ({list of locations})
- Cross-project dependency violations: {count}
- Unresolved TODO/NEEDS-INPUT (if published): {count}
- Vendor citation pattern issues: {count}
- Internal-standard citation pattern issues: {count}
- Jr-executability flags: {count}

## Cross-project dependency violations

### {artifact path} → {target project} (status: {target status})

**Resolution options:**
1. Finish {target project} (transition to published)
2. Archive {target project} (then restate this artifact)
3. Restate this artifact to remove the dependency

## Summary

{Pass/fail per artifact and overall; recommended next steps.}
```

## Pass/fail criteria

- **PASS at draft:** no broken wikilinks; no cross-project violations
- **PASS at review:** all draft checks + zero body-prose wikilinks
- **PASS at published:** all review checks + no unresolved TODOs/NEEDS-INPUT in body + citation patterns compliant

When invoked pre-publish, a FAIL blocks publish unless the user explicitly overrides; overrides are logged.

## Append to log

```
## [{ISO timestamp}] align-closure | {slug}
- Artifacts checked: {N}
- Status distribution: draft={N}, review={N}, published={N}
- Total violations: {N}
- Cross-project dependency violations: {N}
- Status: pass | fail
- Report: {path}
```
