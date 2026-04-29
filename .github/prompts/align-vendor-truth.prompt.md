---
description: Verify vendor-domain claims cite vendor sources, not stale internal claims. Catches the S3-encryption-style failure mode where internal docs misrepresent vendor capabilities.
mode: agent
---

# /align-vendor-truth

You are verifying that claims about vendor capabilities (AWS, Snowflake, Atlassian, etc.) are cited from vendor sources, not from internal documentation that may be stale or incorrect.

## Inputs

- Path to one artifact, OR a project slug (run on every artifact in the project)

## Workflow

### Step 1: Identify vendor-domain claims

Re-read the artifact. Extract every claim that makes an assertion about a vendor's product, service, or capability. Examples:

- "AWS S3 supports server-side encryption with KMS-managed keys"
- "Snowflake Time Travel retention is configurable up to 90 days"
- "Atlassian Confluence Cloud rate limits are per-tenant"

For each claim, identify:
- The named vendor (or inferred from context)
- The vendor's domain tag (`vendor:aws`, `vendor:snowflake`, etc.)
- The current citation (which source the artifact attributes the claim to)

### Step 2: Verify citation domain

For each vendor claim, check:

- **Pass:** citation source's `domain` matches the claim's vendor domain (e.g., AWS claim cites `raw/external/aws/...` or another `domain: vendor:aws` source)
- **Fail:** citation source has a different domain (e.g., AWS claim cites `raw/confluence/INTERNAL/...` with `domain: internal`)

### Step 3: Verify cache freshness

For passing citations (correct vendor domain), check the `revalidate_after` frontmatter:

- **Fresh:** `revalidate_after` in the future. No action.
- **Stale (under hard max):** past `revalidate_after` but under `hard_max_age_days`. Flag as warning; offer refetch.
- **Hard-stale:** past `hard_max_age_days`. Flag as error; refetch required before publish.

### Step 4: Suggest remediation per violation

For each violation:

- **Wrong-domain citation:** suggest the vendor doc to fetch (`/ingest-vendor-doc {vendor} {topic} {URL}`). After fetch, re-cite using the new vendor source. The internal source is flagged as outdated; surface to the team owning that source.
- **Stale cache:** suggest `/ingest-vendor-doc` with the existing vendor URL to refresh.
- **Hard-stale cache:** require refetch before the artifact can be published.

## Output

Write a structured report to `reports/align-vendor-truth-{artifact-slug}-{date}.md`:

```markdown
# align-vendor-truth report: {artifact}

Date: {ISO timestamp}
Artifact: {path}
Vendor claims found: {N}
- Correctly cited (vendor source, fresh): {count}
- Wrong domain: {count}
- Stale cache (under hard max): {count}
- Hard-stale cache: {count}

## Violations

### Wrong-domain citation

**Claim:** {text}
**Current citation:** {source} (domain: {domain})
**Expected domain:** vendor:{vendor}
**Suggested vendor source:** {URL}
**Action:** Run `/ingest-vendor-doc {vendor} {topic} {URL}` then re-cite.

### Stale cache

**Claim:** {text}
**Cached source:** {raw/external/...} (fetched {date}, {N days} old)
**TTL:** {N days}
**Action:** Run `/revalidate-vendor-docs` (or `/ingest-vendor-doc` for this URL specifically).

[repeat per violation]

## Summary

{Pass/fail; counts; recommended next step.}
```

## Pass/fail criteria

- **PASS:** no wrong-domain citations and no hard-stale caches
- **FAIL:** any wrong-domain citation or hard-stale cache (warning-level for stale-under-hard-max)

When invoked pre-publish, a FAIL blocks publish unless the user explicitly overrides.

## Append to log

```
## [{ISO timestamp}] align-vendor-truth | {artifact}
- Vendor claims: {N}
- Wrong-domain: {N}
- Stale: {N}
- Status: pass | fail
- Report: {path}
```

## Limitations

- The check identifies "claims that look like vendor capability claims" by pattern matching and LLM judgment; it can miss claims that are paraphrased away from the vendor's terminology
- "Fresh" means within the configured TTL, not "definitively current with the vendor's latest docs." Vendors change their docs; the cache is a snapshot.
- The check does not verify that the cached vendor doc actually contains the cited content (that is `align-cite`'s job); these checks are complementary
