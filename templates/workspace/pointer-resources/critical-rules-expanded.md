# Critical rules — expanded reference (RC-165)

Optional depth for Tier-2 shims. **Compact numbered rules stay in default load.** Read when interpreting edge cases.

## 1. Filesystem-first

Every artifact is plain Markdown or JSON. No proprietary databases; git and Obsidian are the runtime.

## 2. Citation-grounded

Every factual claim in generated artifacts links to a source path or URL. Retrieval confidence does not substitute for cite verification at publish.

## 3. Read-before-write (RC-122)

Read scoped index/catalog and relevant sources before proposing artifact edits. Record consulted paths in frontmatter `sources`. Question before generating.

## 4. Authority + domain

Each source carries `authority` (`standard` / `recommendation` / `informational`) and `domain` (`internal`, `vendor:{name}`, `industry:{name}`). The source authoritative for the claim's domain wins conflicts.

## 5. Approval-gated mutations

Ingest, sync, archive, remove, and publish require explicit user approval after diff or preview. Compile into wiki requires batch approval (RC-146).

## 6. Scoped retrieval

Default in-scope sources from `config/second-brain.yml`; projects add scope via `meta.yml`. Do not read the full vault without scope.

## 7. Multi-step orchestration

Agents hand off through `wiki/workspace-projects/{slug}/0X-{stage}/`. Resumable via `handoff.md`, `meta.yml`, and optional scaffolds.

## 8. LLM owns wiki

Humans read wiki content. Direct human edits set `manually_edited: true` for lint visibility.

## 9. Vendor truth TTL

Vendor docs cached in `raw/workspace-external/`; revalidate per TTL (90 days default, 365 hard max). Stale cache flagged before cite.

## 10. Project closure

Published artifact set must be jr-engineer-executable using only that set. No hidden dependencies on draft scaffolds or orientation.

## 11. Body-prose-clean

At `review` and `published`, body prose has no internal `[[wikilinks]]`. Navigation in `## See Also` or frontmatter. Draft allows wikilinks for agent collaboration.

## 12. Three-state lifecycle

`in-progress` (`draft`, `review`) → `published` → `archived`. In-progress projects cannot reference other in-progress or archived projects.

## 13. Citation patterns

- **Vendor:** parenthetical attribution in body + vendor URL in See Also
- **Internal standards:** inline relevant rules in body + Confluence URL in See Also

## 14. Safety

Fail closed; explicit tool allowlists; append-only audit in `wiki/log.md`; no secrets in artifacts or logs.

## 15. No telemetry

No phone-home or analytics from Second Brain operations.

## See also

- Compact list: any Tier-2 shim § Critical rules
- Canonical: `AGENTS.md`
