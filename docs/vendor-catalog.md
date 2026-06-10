# Vendor documentation catalog

**Status:** v1.0
**Last updated:** 2026-06-09

Second Brain grounds **vendor capability claims** (what AWS, Snowflake, Terraform, etc. can do) in cached vendor documentation under `raw/workspace-external/{vendor}/`. Internal org docs (Confluence) are deferred until you have access; **vendor truth works without Atlassian.**

---

## How vendor docs fit the system

| Layer | Path | Role |
|-------|------|------|
| Cache (immutable after fetch) | `raw/workspace-external/{vendor}/{topic}/{slug}.md` | Primary source for `align-vendor-truth` |
| Wiki (optional) | `wiki/workspace-concepts/`, `wiki/workspace-standards/{vendor}/` | Compiled summaries when a topic is cited often |
| Project artifacts | `wiki/workspace-projects/{slug}/` | Body cites vendor claims with parenthetical + See Also URL |

**Authority rule:** For a claim about vendor behavior, `domain: vendor:{name}` wins over internal docs. See `AGENTS.md` and `docs/architecture-rationale.md` §6–7.

**Operations:**

- `/workspace-ingest-vendor-doc` — fetch one URL on demand (defuddle), cache with TTL
- `/workspace-align-vendor-truth` — flag vendor claims that cite internal sources instead of vendor cache
- `/workspace-revalidate-vendor-docs` — batch refresh stale caches (prompt; see `.github/prompts/`)

**Fetch tool (v1):** [defuddle](https://www.npmjs.com/package/defuddle) CLI on public documentation URLs. No vendor account required for read-only public docs.

---

## Integration tiers

### Tier A — On-demand URL cache (v1, use now)

Agent (or you) supplies a **specific documentation URL** when citing a capability. Defuddle extracts Markdown; Second Brain stores it with TTL frontmatter.

**Best for:** AWS, Azure, GCP, Snowflake, Postgres, Docker, GitHub, OpenAI, Anthropic, Microsoft 365, Informatica, IBM product docs, HashiCorp Terraform docs.

**Limits:** Does not crawl entire doc sites; does not replace site search; some pages with heavy JS may fail (retry or pick a stable HTML doc URL).

### Tier B — Vendor MCP servers (v1.x, optional per user)

When you configure an MCP server in Cursor/VS Code, agents can use structured tools **in addition to** (not instead of) cached Markdown for citations that must pass `align-cite`.

| MCP / integration | Typical use | Citation note |
|-------------------|-------------|---------------|
| Terraform MCP | Resource schemas, provider docs, plan context | Capability claims still cache to `vendor:terraform` or `vendor:hashicorp` URLs where possible |
| AWS / cloud MCPs (when available) | Live API metadata, service discovery | Use for drafting; **publish** still prefers cached vendor doc + `align-vendor-truth` |
| GitHub MCP | Repo/issue/PR context; built into Copilot CLI | Product behavior claims cite `vendor:github` **docs** cache; repo facts cite GitHub API/MCP with clear domain |
| OpenAI API | Drafting, Agents SDK orchestration | Capability claims cache to `vendor:openai` URLs; SDK/MCP tool output is not canonical until verified |
| Anthropic MCP connector | Remote MCP servers via Messages API (`mcp-client` beta) | MCP protocol originator; product claims cite `vendor:anthropic`; connected tool behavior cites the tool's vendor domain |
| Microsoft Learn MCP | Cross-product Learn doc search/fetch (`https://learn.microsoft.com/api/mcp`) | Drafting aid; **M365 / Copilot / Studio** claims cache to their product slug, not Learn MCP output |
| Copilot Studio + MCP | Studio agents **consume** external MCP servers via Power Platform connectors | Product behavior (auth, DLP, wizard) cites `vendor:microsoft-copilot-studio`; connected tool behavior cites the tool's vendor domain |

MCP output is **not** automatically canonical. Follow RC-002: retrieval and tool output ≠ citation support until verified against cached vendor doc or explicit source.

### Tier C — User content sources (not vendor truth)

| Source | Classification | v1 status |
|--------|----------------|-----------|
| Google Drive | User/org **internal** content (`domain: internal`), not vendor product docs | Out of scope for v1; see roadmap v1.x (SharePoint/OneNote pattern) |
| Confluence / Jira | Internal workspace sources | **Deferred** until Atlassian access (Phase 1B) |

Do not treat Google Drive or Confluence as `vendor:*` domains.

---

## Supported vendor slugs and doc roots

Use lowercase slugs in paths and `domain: vendor:{slug}`.

| Slug | Domain tag | Official doc root (starting points) | TTL override hint |
|------|------------|-------------------------------------|-------------------|
| `anthropic` | `vendor:anthropic` | https://platform.claude.com/docs/en | 60–90 days — Claude API; MCP protocol and connector docs |
| `aws` | `vendor:aws` | https://docs.aws.amazon.com/ | 60–90 days |
| `azure` | `vendor:azure` | https://learn.microsoft.com/en-us/azure/ | 90 days |
| `microsoft-copilot-studio` | `vendor:microsoft-copilot-studio` | https://learn.microsoft.com/en-us/microsoft-copilot-studio/ | 90 days — Power Platform agent builder; distinct from `vendor:azure` and M365 Copilot |
| `gcp` | `vendor:gcp` | https://cloud.google.com/docs | 90 days |
| `github` | `vendor:github` | https://docs.github.com/en | 90 days — Copilot, Actions, platform docs; see `config/github-seed-stack.yml` |
| `microsoft-365` | `vendor:microsoft-365` | https://learn.microsoft.com/en-us/microsoft-365/ | 90 days — productivity suite, Graph, Teams, SharePoint; not Azure platform |
| `microsoft-365-copilot` | `vendor:microsoft-365-copilot` | https://learn.microsoft.com/en-us/microsoft-365/copilot/ | 90 days — in-app M365 Copilot and declarative agents; distinct from `microsoft-copilot-studio` |
| `openai` | `vendor:openai` | https://developers.openai.com/api/docs | 60–90 days — API, Agents SDK, models |
| `snowflake` | `vendor:snowflake` | https://docs.snowflake.com/ | 30–60 days (frequent releases) |
| `informatica` | `vendor:informatica` | https://docs.informatica.com/ | 90 days |
| `ibm-db2-zos` | `vendor:ibm-db2-zos` | https://www.ibm.com/docs/en/db2-for-zos/12.0.0 | 90 days — use **SSEPEK static HTML** URLs (`/docs/en/SSEPEK_12.0.0/{book}/src/tpc/*.html`); `topic=` pages are hit-or-miss; encryption uses **manual ingest** (`config/vendor-seed-manual/`) |
| `ibm` | `vendor:ibm` | https://www.ibm.com/docs/en | 90 days (general IBM products) |
| `terraform` | `vendor:terraform` | https://developer.hashicorp.com/terraform/docs | 60 days |
| `docker` | `vendor:docker` | https://docs.docker.com/ | 90 days |
| `postgres` | `vendor:postgres` | https://www.postgresql.org/docs/ | 90 days (match major version in topic path) |

**Atlassian** (`vendor:atlassian`): Confluence/Jira **product** docs only—for example https://developer.atlassian.com/cloud/confluence/ — not your company's Confluence spaces. Company content uses `raw/workspace-confluence/` when Phase 1B is unblocked.

---

## Example: citing AWS S3 encryption in a project doc

1. Agent needs to claim KMS SSE support.
2. Run `/workspace-ingest-vendor-doc` with vendor `aws`, topic `s3-encryption`, URL from AWS docs.
3. Cache written to `raw/workspace-external/aws/s3-encryption/{slug}.md`.
4. Body prose: parenthetical attribution — *S3 supports SSE-KMS (per AWS docs).*
5. See Also: link to live AWS URL with `(cached YYYY-MM-DD)`.
6. Before publish: `/workspace-align-vendor-truth` ensures the claim cites `vendor:aws`, not an internal wiki article.

---

## Configuration

In `config/second-brain.yml` (from `config/second-brain.example.yml`):

- `vendor_revalidation` — TTL defaults and per-vendor overrides
- `vendor_sources` — enabled slugs, allowlisted domains, optional seed URLs for common topics

Allowlisting: if your environment restricts egress, add vendor doc domains (e.g. `docs.aws.amazon.com`, `learn.microsoft.com`) to your network or tool policy.

---

## Default stack seed (AWS + Snowflake + Informatica)

Tracked seeds: `config/vendor-seed-stack.yml` (8 starter topics). Fetch with:

```bash
python scripts/seed-vendor-docs.py --yes
```

| Vendor | Starter topics |
|--------|----------------|
| `aws` | S3 SSE/SSE-KMS, bucket policies, Glue security, IAM, VPC endpoints |
| `ibm-db2-zos` | Db2 12 intro, SQL, security, RACF, data sharing, utilities, app dev — see `config/ibm-db2-zos-seed-stack.yml` |
| `snowflake` | 44 in-scope features (objects, integrations, Cortex, governance) — see `config/snowflake-seed-stack.yml` |
| `snowflake` | Encryption, S3 load, storage integration, stages, Snowpipe, RBAC |
| `informatica` | Cloud DI getting started, product hub |
| `microsoft-copilot-studio` | Overview, generative orchestration, knowledge, MCP integration, publish/channels — see `config/microsoft-copilot-studio-seed-stack.yml` |
| `openai` | API platform, models, Agents SDK, tools — see `config/openai-seed-stack.yml` |
| `anthropic` | Claude API, models, tool use, MCP connector — see `config/anthropic-seed-stack.yml` |
| `microsoft-365` | Enterprise overview, Graph, Teams, SharePoint, Entra — see `config/microsoft-365-seed-stack.yml` |
| `microsoft-365-copilot` | M365 Copilot overview, agents, declarative agents, licensing — see `config/microsoft-365-copilot-seed-stack.yml` |
| `github` | Copilot, cloud/custom agents, MCP, Actions — see `config/github-seed-stack.yml` |

Seed one vendor:

```bash
python scripts/seed-vendor-docs.py --seed-file config/microsoft-copilot-studio-seed-stack.yml --yes
python scripts/seed-vendor-docs.py --seed-file config/openai-seed-stack.yml --yes
# …anthropic, microsoft-365, microsoft-365-copilot, github
```

---

## Build sequence without Confluence

When Atlassian access is unavailable:

1. **Phase 1A (complete in repo):** `verify-setup.py` without Atlassian gate; `seed-vendor-docs.py` + `revalidate-vendor-docs.py` for caches listed in `config/vendor-seed-stack.yml`.
2. **Phase 2 (complete in repo):** `compile-workspace-external.py`, `lint-workspace.py`, Base views under `wiki/workspace-views/` — regenerate wiki locally (gitignored).
3. **Phase 3 (active):** `/workspace-start-project` — agent chain grounded in **vendor docs + your drafts** until 1B.
4. **Phase 1B (blocked):** Atlassian MCP spike + Confluence ingest when `atlassian.enabled=true` and credentials exist.

See `docs/roadmap.md` for checklist items.

---

## Adding a new vendor

1. Pick a slug (lowercase, hyphenated).
2. Add an entry under `vendor_sources` in `config/second-brain.yml`.
3. Document the official doc root in this file (PR welcome).
4. Fetch pages on demand; do not bulk-crawl entire sites in v1.
5. If an MCP exists, note it under Tier B in this file when validated.

---

## See also

- `docs/architecture-rationale.md` §6 — fetch-on-demand + TTL decision
- `.github/prompts/workspace-ingest-vendor-doc.prompt.md` — ingest workflow
- `.github/prompts/workspace-align-vendor-truth.prompt.md` — alignment
- `docs/roadmap.md` — Phase 1A / 1B split
