---
description: Fetch a vendor doc on demand using the defuddle skill, cache to raw/workspace-external/ with TTL frontmatter for revalidation.
mode: agent
inherits: AGENTS.md
instruction_stack_tier: 2
lane: workspace
---

# /workspace-ingest-vendor-doc

## Instruction stack (RC-161)

- **Tier 1:** Root invariants from `AGENTS.md` always apply; this prompt cannot override them.
- **Tier 2:** This file adds lane/stage scope only.
- **Tier 3:** Optional project files (`meta.yml`, `retrieval-contract.md`, stage scaffolds) add scope without restating root rules.

**Non-overridable:** approval-gated mutations; align-cite + align-closure before publish; citation-grounded claims; fail closed; platform research must not mutate canonical workspace docs without approval.

You are fetching a vendor documentation page (AWS, Snowflake, Atlassian, etc.) on demand because an agent is about to cite a vendor capability claim. The fetched page is cached locally with TTL frontmatter so future cites can reuse it.

## Inputs

- Vendor name (e.g., `aws`, `snowflake`, `atlassian`)
- Topic (short slug, e.g., `s3-encryption`, `snowflake-time-travel`)
- Vendor doc URL
- Triggering query (the question the agent was answering when it needed this doc)

## Pre-flight

Check `raw/workspace-external/{vendor}/{topic}/` for existing cached entry:

- If exists and `revalidate_after` is in the future: cache is fresh; return the cached file path. Do not refetch.
- If exists and `revalidate_after` has passed but `fetched_at + hard_max_age_days` is in the future: prompt the user to refetch ("This cache is N days old, beyond the {ttl} day TTL. Refetch? (y/n)"). On no, return the cached file with stale annotation. On yes, proceed.
- If `fetched_at + hard_max_age_days` has passed: must refetch. Force prompt.

TTL values come from `config/second-brain.yml` `vendor_revalidation`:
- `default_ttl_days` (90)
- `per_vendor: {vendor: ttl_days}` (per-vendor overrides)
- `hard_max_age_days` (365)

## Fetch pipeline

1. Use the `defuddle` skill (`.github/skills/defuddle/`) to fetch and clean the page:

```bash
defuddle parse {URL} --md -o {temp file}
```

2. Read the resulting Markdown.

3. Add frontmatter:

```yaml
---
source_url: {URL}
vendor: {vendor}
topic: {topic}
fetched_at: {ISO timestamp}
revalidate_after: {ISO timestamp = fetched_at + ttl_days}
fetched_by_query: {triggering query}
domain: vendor:{vendor}
authority: standard
---
```

4. Write to `raw/workspace-external/{vendor}/{topic}/{slug}.md` where `{slug}` is derived from the URL or topic.

   For manual URL-less clips, use `raw/workspace-inbox/{YYYY-MM-DD}/{slug}.md` per `templates/workspace/raw-inbox-staging.md` with `inbox_status: unprocessed`.

5. Append to `wiki/log.md`:

```
## [{ISO timestamp}] ingest-vendor-doc | {vendor}/{topic}
- Source: {URL}
- Fetched by query: {query}
- Cache valid until: {revalidate_after}
```

6. **Compile (optional, RC-146):** Only when the cached doc warrants a `wiki/workspace-concepts/` or `wiki/workspace-standards/{vendor}/` article **and** the user explicitly approves compile. Invoke `workspace-compile.prompt.md` for the batch; never auto-compile. For simple capability lookups (e.g., "does S3 support SSE-KMS"), the raw cache alone is sufficient.

## Return value

Return the path to the cached file. The calling agent uses this to:

- Quote the relevant capability with parenthetical attribution: "S3 supports SSE-KMS (per AWS docs)"
- Add a See Also link to the vendor URL: `[AWS S3 Encryption Documentation](https://docs.aws.amazon.com/...) (cached YYYY-MM-DD)`

## On fetch failure

- Defuddle error or empty result: report the failure; do not write a stub file
- Network / DNS / 404: same; surface to the user; suggest they verify the URL
- Allowlist block (if egress is restricted): suggest the user add the vendor's domain to their allowlist

The triggering agent should present the user with options: cite without verification (note the gap), pick a different source, or skip the claim.

## Revalidate command

The `/workspace-revalidate-vendor-docs` prompt enumerates all cached vendor docs whose `revalidate_after` is in the past and offers batch refresh. That prompt is built on top of this one (calls `/workspace-ingest-vendor-doc` for each stale entry).
