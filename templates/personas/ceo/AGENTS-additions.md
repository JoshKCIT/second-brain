# AGENTS.md additions for CEO persona

The CEO operator uses the standard schema documented in the repo-root `AGENTS.md`. **No persona-specific schema additions are required for v1.**

## Why no additions

- Article types (concept, connection, qa, standards, recommendations, informational, project-artifact) cover everything a CEO operator typically authors or queries.
- The agent chain (CEO → VP → PM → Architect → Engineer) is already CEO-centric by design.
- Authority-and-domain tagging works without per-persona variation.
- Closure rules apply uniformly.

## Operating-mode notes the CEO should know

These are not schema additions; they are operating-mode reminders relevant to the CEO operator specifically:

- **Tone:** Direct, terse, technical. Skip pleasantries; surface the substantive answer first.
- **Review cadence:** Between every agent stage. Do not let the chain run unattended.
- **Scope discipline:** Default in-scope spaces are configured at setup; resist adding spaces project-by-project unless they are genuinely needed (broader scope means slower retrieval and more noise).
- **Vendor truth:** When a vendor capability is named in any artifact, demand the vendor citation. Do not accept "we always thought X was true" as sufficient.
- **Closure enforcement:** Always run `align-closure` before publish. The jr-engineer-executable bar protects future readers, including future-you.

## When persona-specific additions might emerge

If you find yourself repeatedly authoring the same shape of artifact that does not fit existing types (e.g., "investor update," "strategic decision rationale" with non-ADR shape), add a new type here and document the frontmatter and structure. Then update the relevant prompts to handle the new type.

For now, leave this file as-is.
