# AGENTS.md - Second Brain Operating Spec

> Canonical schema and operating instructions for any AI coding agent (Copilot, Claude Code, Cursor, Windsurf, Codex CLI, etc.) working with this repo. Per-agent shim files (`.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`) reference this document for full content. If you are an agent reading a shim, also read this file.

## Purpose

Second Brain is a personal knowledge base maintained by an LLM, sourced from the user's organizational documentation (Confluence first; Jira and others later) plus on-demand vendor documentation, and used to author new project documentation that is grounded in canonical sources and executable by a junior engineer using only the published artifact set.

This document tells you how the system is structured, how to ingest content, how to maintain the wiki layer, how to author project artifacts, how to verify alignment and closure, and how to publish.

## Scope discipline

Target band: governance-and-closure. The capabilities Second Brain implements:

- Claim-domain authority and vendor truth arbitration
- Vendor truth validation with TTL-cached vendor docs
- Junior-engineer-executable closure rule (published artifact set must be self-sufficient)
- Multi-page stage-gated technical-doc generation with Confluence-storage-format output
- Mandatory section-level citation discipline across multi-page artifacts
- Inspectable retrieval enforced before generation as policy
- Project artifact lifecycle (in-progress / published / archived) with cross-project dependency rules

Out of scope (covered by alternatives such as Rovo, Glean, Microsoft Copilot for M365, Notion AI, Sourcegraph Cody): generic enterprise search, Q&A, multi-step agents without governance constraints, IDE-integrated codebase chat, basic page templates.

When the user asks for a feature, classify it as governance-band or generic-band. Generic-band requests should be declined or punted to the appropriate alternative tool. Governance-band requests can be considered. The `product-brief.md` §1.2 capability table and §8.1 Risk 7 are the canonical scope filter.

---

## The compiler analogy

Adapted from Cole's claude-memory-compiler:

```
raw/                = source code        (immutable input)
LLM (this agent)    = compiler           (extracts and organizes knowledge)
wiki/               = executable         (structured, queryable knowledge base)
align + lint        = test suite         (correctness and closure checks)
queries + drafts    = runtime            (using the knowledge to produce work)
```

The user does not manually organize the wiki. They configure scope, request operations, and review artifacts. You do the synthesis, cross-referencing, citation, alignment checking, and bookkeeping.

---

## Architecture: three layers + agent chain

### Three layers

1. **`raw/` - immutable source**
   - `raw/confluence/{space-key}/pages/{page-id}--{slug}.md` and `attachments/`
   - `raw/jira/{project-key}/tickets/` (v1.x)
   - `raw/external/{vendor}/{topic}/{slug}.md` for cached vendor docs
   - `raw/transcripts/{slug}/transcript.md` for product-intelligence transcripts
   - You read from here; you never modify it after the initial ingest write.

2. **`wiki/` - LLM-curated knowledge**
   - You own this directory entirely. The user reads it; you write it.
   - Subdirectories defined below.

3. **`AGENTS.md` (this file) - the schema**
   - Tells you how to behave. Co-evolves with the user as the project domain develops.

### Agent chain (project workflow)

When the user (CEO) declares a project intent, you orchestrate this chain:

```
CEO declares high-level project intent
   ↓
VP Agent (works with CEO) → wiki/projects/{slug}/01-vp-brief/product-brief.md
   ↓
PM Agent (uses VP output) → wiki/projects/{slug}/02-pm-prd/product-requirements.md
   ↓
Architect Agent (if technical) → wiki/projects/{slug}/03-architecture/architectural-approaches.md
   ↓
Engineer Agent → wiki/projects/{slug}/04-engineering/{spec-files}.md
   ↓
Engineer-led finalize step → status: review
```

Each agent has a prompt file in `.github/prompts/{agent}-agent.prompt.md` with role definition, input contract, output contract, source-of-truth scope, and human checkpoint logic.

CEO reviews and edits between stages. Do not invoke the next agent without explicit CEO approval.

---

## Source authority and domain

Every source carries two tags:

### Authority levels

| Level | Meaning |
|---|---|
| `standard` | Authoritative; takes precedence in conflicts |
| `recommendation` | Strong guidance; can be overridden with reason |
| `informational` | Background context; not binding |

### Domains

| Domain | Authoritative for... | Examples |
|---|---|---|
| `internal` | Internal architecture, decisions, patterns, runbooks | Architecture team space, SRE runbooks |
| `vendor:{name}` | What the named vendor's product can do | `vendor:aws`, `vendor:snowflake`, `vendor:atlassian` |
| `industry:{name}` | Regulatory, compliance, or industry norms | `industry:nist`, `industry:hipaa` |

### Conflict resolution rule

**The source authoritative for the claim's domain wins.** If internal docs say "S3 cannot be encrypted" and AWS docs say it can, AWS wins because the claim is a vendor capability. The internal doc is flagged as outdated by `align-vendor-truth`.

When citing in generated artifacts:
- Internal architecture claims: cite internal sources (Architecture, Security, Audit, etc.)
- Vendor capability claims: cite vendor docs from `raw/external/{vendor}/`
- Compliance claims: cite industry standards

---

## Article types in `wiki/`

```
wiki/
├── index.md              # Master catalog; Obsidian home; embeds Base views
├── log.md                # Append-only chronological build log
├── standards/            # Authority: standard
├── recommendations/      # Authority: recommendation
├── informational/        # Authority: informational (default for ungraded)
├── concepts/             # Atomic knowledge articles compiled from raw sources
├── connections/          # Cross-cutting insights linking 2+ concepts
├── qa/                   # Filed query answers (compounding knowledge)
├── research/             # Transcript-derived product intelligence; not canonical knowledge
├── projects/{slug}/      # Project-specific artifact sets (per-stage subdirs)
├── archives/             # Completed and deprecated content (excluded from default search)
└── views/                # Obsidian Base files for live navigation
```

### Concept article (`wiki/concepts/{slug}.md`)

```markdown
---
title: "Concept Name"
type: concept
authority: standard | recommendation | informational
domain: internal | vendor:aws | industry:nist | ...
aliases: [alternate-name]
tags: [domain, topic]
sources:
  - "raw/confluence/SECURITY/pages/12345--encryption-at-rest.md"
status: published
created: 2026-04-28
updated: 2026-04-28
---

# Concept Name

[2-4 sentence core explanation]

## Key Points

- [Self-contained bullet points]

## Details

[Deeper explanation, encyclopedia-style paragraphs]

## See Also

- [[concepts/related-concept]] — How it connects

## Sources

- [[raw/confluence/SECURITY/pages/12345--encryption-at-rest]] (Section 3.2)
```

### Standard / Recommendation / Informational article

Same shape as concept; lives in `wiki/standards/{team}/{slug}.md` etc. The directory placement encodes the authority. Frontmatter `domain` is required.

### Connection article (`wiki/connections/{slug}.md`)

```markdown
---
title: "Connection: X and Y"
type: connection
connects:
  - "concepts/concept-x"
  - "concepts/concept-y"
sources:
  - "raw/confluence/SPACE/pages/...md"
status: published
created: 2026-04-28
updated: 2026-04-28
---

# Connection: X and Y

## The Connection

[What links these concepts]

## Key Insight

[The non-obvious relationship]

## Evidence

[Examples drawn from sources]

## See Also

- [[concepts/concept-x]]
- [[concepts/concept-y]]
```

### Q&A article (`wiki/qa/{slug}.md`)

```markdown
---
title: "Q: Original Question"
type: qa
question: "The exact question asked"
consulted:
  - "concepts/article-1"
  - "concepts/article-2"
status: published
filed: 2026-04-28
---

# Q: Original Question

## Answer

[Synthesized answer with section-anchored citations]

## Sources Consulted

- [[concepts/article-1]] — Relevant because...
- [[concepts/article-2]] — Provided context on...

## Follow-Up Questions

- [Open questions raised by the answer]
```

### Research claim register (`wiki/research/claim-register.md`)

Research review captures transcript-derived product-intelligence claims. These claims are evidence for product decisions, not canonical internal standards, vendor truth, or roadmap facts.

````markdown
# Research Claim Register

## Claim Records

```yaml
claim_id: RC-YYYY-MM-DD-001
source_transcript: raw/transcripts/path/to/transcript.md
claim_type: product_requirement
atomic_claim: ""
current_design_status: unsupported
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 0
decision: adopt | experiment | defer | reject | monitor
decision_rationale: ""
next_action: ""
```
````

Research-review agents may write `wiki/research/**`, `reports/research-review/**`, and `docs/decision-records/DRAFT-*.md`. They must not directly update `wiki/standards/**`, `wiki/recommendations/**`, `PRD.md`, `product-brief.md`, `docs/roadmap.md`, `docs/architecture-rationale.md`, `AGENTS.md`, or any `raw/**` source mirror based on transcript claims.

### Project stage artifact (`wiki/projects/{slug}/0X-{stage}/{name}.md`)

```markdown
---
title: "Document Title"
type: project-artifact
project: "{slug}"
stage: "vp-brief" | "pm-prd" | "architecture" | "engineering"
status: draft | review | published | archived
authored_by_agent: vp | pm | architect | engineer
sources:
  - "wiki/standards/architecture/microservice-sizing.md"
  - "raw/external/aws/s3/encryption.md"
created: 2026-04-28
updated: 2026-04-28
---

# Document Title

[Body prose. At draft status, wikilinks allowed. At review/published, body must be link-free.]

## See Also

[Optional navigation; only at review/published]

## Open Questions

[Optional; allowed at any status]
```

---

## Index format

`wiki/index.md` is the primary navigation entry. Structure:

```markdown
# Knowledge Base Index

## Active projects

[Embed: wiki/views/active-projects.base, or table here]

## Standards by team

[Embed: wiki/views/standards-by-team.base]

## Recent activity

[Embed: wiki/views/recent-activity.base]

## All concepts

| Article | Authority | Domain | Sources | Updated |
|---|---|---|---|---|
| [[concepts/encryption-at-rest]] | Standard | Internal | 2 | 2026-04-28 |
| ... |

## All connections

| Article | Connects | Updated |
|---|---|---|

## Stale vendor docs

[Embed: wiki/views/stale-vendor-docs.base]
```

You update this file on every compile. It is the agent's primary retrieval mechanism for queries: read `index.md` first to identify relevant articles, then read those articles in full.

---

## Log format

`wiki/log.md` is append-only, parseable by grep. Format:

```markdown
# Build Log

## [2026-04-28T14:30:00Z] ingest | Confluence space ARCH
- Pages fetched: 47
- Pages compiled: 45
- Quarantined: 2 ([[quarantine/2026-04-28/12345]], [[quarantine/2026-04-28/12346]])
- Wiki articles created: [[concepts/microservice-sizing]], [[standards/architecture/microservice-sizing]]
- Index updated

## [2026-04-28T15:12:00Z] query | "What is our microservice sizing standard?"
- Consulted: [[standards/architecture/microservice-sizing]], [[concepts/service-boundaries]]
- Filed to: [[qa/microservice-sizing-explained]]

## [2026-04-28T16:00:00Z] align-vendor-truth | wiki/projects/customer-data-replatform/02-pm-prd/product-requirements.md
- Vendor claims checked: 7
- Violations: 1 (Snowflake claim cited internal source instead of vendor doc)
- Resolution suggested: refetch raw/external/snowflake/data-types.md

## [2026-04-28T16:30:00Z] publish | review | wiki/projects/customer-data-replatform/02-pm-prd/product-requirements.md
- Output: confluence-review/customer-data-replatform/product-requirements-2026-04-28-1630.html
- align-cite: passed
- align-closure: passed
```

---

## Wikilinks and the closure rule

### Closure rule

A project's **active authored set** is the documents inside `wiki/projects/{slug}/0X-{stage}/`. The set must be jr-engineer-executable using only itself.

### Body prose rule (status-aware)

| Status | Body wikilinks allowed in prose? |
|---|---|
| `draft` | Yes (agent collaboration) |
| `review` | No (move to `## See Also` or frontmatter) |
| `published` | No |
| `archived` | No (frozen state) |

External Markdown links (`[text](url)`) for vendor docs and public references are allowed in body at any status.

### Cross-project rule

An `in-progress` project (status `draft` or `review` on any of its files) cannot reference:
- Another `in-progress` project
- An `archived` project

It CAN reference:
- A `published` project
- Internal `wiki/standards/`, `wiki/recommendations/`, `wiki/concepts/` content
- External vendor docs (in raw/external/)
- External public URLs

When `align-closure` detects a forbidden cross-project dependency, present the user with options:
1. Finish the dependency project (move it to `published`)
2. Archive the dependency project (move it to `wiki/archives/`; the dependent project must then be restated)
3. Restate the dependent project to remove the dependency

### Vendor citation pattern

In body prose: parenthetical attribution.
> S3 supports server-side encryption with KMS-managed keys (per AWS docs).

In `## See Also`: external link.
> - [AWS S3 Server-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html) (cached 2026-04-28)

The cached vendor doc in `raw/external/{vendor}/{topic}/{slug}.md` is the actual source; the See Also URL points to the live source for the reader to verify.

### Internal standard reference pattern

In body prose: inline the relevant rules.
> Per the Architecture team's microservice sizing standard, services with fewer than three deployments per quarter and one or fewer engineers should remain consolidated rather than split. New services require Architecture review.

In `## See Also`: link to the Confluence URL (not the wiki article path).
> - [Microservice Sizing Standard](https://yourcompany.atlassian.net/wiki/spaces/ARCH/pages/12345/Microservice+Sizing+Standard) - Architecture team

The reader may not have access to the Confluence page. The inlined rules guarantee execution; the URL is a courtesy for verification.

---

## Core operations

### 1. Ingest (Confluence)

Use the user's existing API-based skill (REST API v2 with `body-format=atlas_doc_format`). Per-page workflow:

1. Fetch the page (and attachments and comments)
2. Convert ADF to Markdown
3. Write `raw/confluence/{space-key}/pages/{page-id}--{slug}.md` with frontmatter (`source_url`, `space_key`, `page_id`, `title`, `ancestors`, `version`, `last_modified`, `labels`, `ingested_at`, `content_hash`, `domain`, `authority`)
4. Compile (see operation 3 below) synchronously
5. Update `wiki/index.md` and `wiki/log.md`
6. On conversion failure: write payload + error to `quarantine/{date}/{page-id}/`; do NOT block the run

After the run, print a manifest:

```
Ingested: 47 pages (45 compiled, 2 quarantined)
Wiki articles created: 12
Wiki articles updated: 8
Index updated.
Run smoke-test query? (y/n)
```

The Atlassian Remote MCP Server is documented as an alternative path. Build week 1 spike validates whether it is viable on the user's tenant.

### 2. Ingest (vendor doc, on demand)

When you are about to cite a vendor capability, check:
- Is there a cached doc in `raw/external/{vendor}/` covering the topic?
- Is it within TTL (90 days default; per-vendor overrides; 365 day hard max)?

If no cache or stale: offer to fetch.

```
About to cite: "S3 supports server-side encryption with KMS-managed keys"
Cached AWS doc: raw/external/aws/s3/encryption.md (fetched 2026-01-15, 103 days old, beyond 90-day TTL)
Refetch? (y/n)
```

If yes:
1. Use `defuddle` skill to fetch and clean Markdown from the vendor URL
2. Write `raw/external/{vendor}/{topic}/{slug}.md` with frontmatter (`source_url`, `vendor`, `topic`, `fetched_at`, `revalidate_after`, `domain`, `authority`)
3. Update `wiki/index.md`
4. Append to `wiki/log.md`

### 3. Compile (raw → wiki)

When processing newly ingested raw/ pages:

1. Read the raw page
2. Read `wiki/index.md` to understand current knowledge state
3. Read existing wiki articles that may be affected
4. For each piece of knowledge in the raw page:
   - If a concept article covers this topic: UPDATE it; add the raw page as a source
   - If new: CREATE a new `wiki/concepts/` article
   - If the page is a standard (per the source-domain mapping in `config/second-brain.yml`): CREATE or UPDATE in `wiki/standards/{team}/`
5. If the page reveals a non-obvious connection between 2+ existing concepts: CREATE a `wiki/connections/` article
6. Use the `obsidian-markdown` skill for output formatting (frontmatter, wikilinks, callouts)
7. UPDATE `wiki/index.md` with new or modified entries
8. APPEND to `wiki/log.md`

Guidelines:
- A single raw page may touch 3-15 wiki articles
- Prefer updating existing articles over creating near-duplicates
- Every article must have valid frontmatter and a Sources section
- Encyclopedia style: factual, concise, self-contained

### 4. Query (index-guided)

1. Read `wiki/index.md` first
2. Identify 3-10 relevant articles based on the question
3. Read those articles in full
4. Synthesize an answer with section-anchored citations
5. If `--file-back`: create a `wiki/qa/` article and update index and log

### 5. Research review

Use `research-review` for transcripts, meeting notes, interviews, or product-improvement discussions about Second Brain.

1. Read the transcript under `raw/transcripts/**` or the user-specified source note
2. Read `AGENTS.md`, `product-brief.md`, `PRD.md`, `docs/architecture-rationale.md`, `docs/roadmap.md`, and `wiki/research/claim-register.md` when present
3. Segment the source into discussion blocks
4. Extract atomic claims and classify each claim
5. Ground claims against existing Second Brain docs and vendor docs when relevant
6. Run skeptical review and score each claim on governance, closure, grounding, vendor truth, inspectability, maintainability, differentiation, enterprise fit, and human review leverage
7. Decide `adopt`, `experiment`, `defer`, `reject`, or `monitor`
8. Write `wiki/research/transcript-analyses/{slug}-claims.md`
9. Update `wiki/research/claim-register.md`
10. Write `reports/research-review/{slug}-impact-report.md`
11. Create draft ADRs under `docs/decision-records/DRAFT-*.md` only for adopted or experimental claims

Research review is deliberately separated from compile. Transcripts may influence Second Brain through review artifacts and draft ADRs, but they do not become canonical knowledge by default.

### 6. Align (cite | conformance | coverage)

Three depths. Run `align-cite` automatically before publish; others on demand.

**align-cite** (production quality):
- Walk every citation in the artifact
- For each, verify the cited source exists and contains content matching the claim
- Output: structured report listing each violation (claim text, claimed source, problem)

**align-conformance** (best-effort, advisory):
- For each in-scope standard, check whether the artifact's structure, terminology, and decisions match
- Output: advisory report; user-judged

**align-coverage** (best-effort, advisory):
- For each in-scope standard, extract a requirements list
- Check the artifact addresses each relevant requirement
- Output: advisory report listing addressed and missing requirements

### 7. Align (vendor-truth)

- Identify vendor-domain claims in the artifact (claims about AWS, Snowflake, etc.)
- Verify each claim's citation is in the matching vendor domain (`raw/external/{vendor}/`)
- Flag claims that cite internal sources instead of vendor sources
- For flagged claims, suggest the vendor doc to fetch

### 8. Align (closure)

Status-aware. Read the artifact's `status` frontmatter and apply rules:

- All statuses: cross-project dependency check (no in-progress → in-progress; no in-progress → archived)
- `review` and `published`: body prose contains no `[[wikilinks]]`
- `published`: all TODO / Open-Questions / NEEDS-INPUT markers resolved or moved to a clearly-marked addendum

Output: structured report. Run automatically before publish.

### 9. Publish

Branch on user choice:

**Review branch:**
1. Convert Markdown to vanilla HTML (browser-readable preview, NOT Confluence storage format)
2. Write `confluence-review/{project-slug}/{doc-slug}-{timestamp}.html`
3. Print full path
4. Open the folder using OS-native opener (`explorer` Windows, `open` macOS, `xdg-open` Linux)

**Confluence branch:**
1. Run `align-cite` and `align-closure` automatically; block on violations unless user explicitly overrides; log overrides
2. Convert Markdown to Confluence storage format (or ADF)
3. Use the user's existing API code (or MCP server alternative) to create new pages in the target Confluence space

### 10. Archive

1. Move project directory: `wiki/projects/{slug}/` → `wiki/archives/projects/{slug}/`
2. Set `archived: true` and `archived_at: timestamp` in frontmatter on every file
3. Update `wiki/index.md` to remove from active project lists
4. Append to `wiki/log.md`

`unarchive` reverses: moves back to `wiki/projects/{slug}/`, removes archived frontmatter, updates index.

### 11. Lint

Seven structural checks plus engineering additions:

| Check | Type | Catches |
|---|---|---|
| Broken links | Structural | Wikilinks pointing to non-existent articles |
| Orphan pages | Structural | Articles with zero inbound links from other articles in the same set |
| Orphan sources | Structural | Raw pages not yet compiled |
| Stale articles | Structural | Source raw page changed since article was last compiled (content_hash differs) |
| Missing backlinks | Structural | A links to B but B does not link back |
| Sparse articles | Structural | Under 200 words |
| Contradictions | LLM | Conflicting claims across articles |
| Deprecated standards | Engineering | Standards marked deprecated still being referenced |
| Cross-team requirement conflicts | Engineering | Two teams' standards giving incompatible guidance |
| Missing alignment | Engineering | Project artifact lacks citation to relevant in-scope standards |
| Incomplete ingestion | Engineering | Page in `raw/` without a wiki article referencing it |
| Stale vendor docs | Engineering | Past TTL or hard max |
| Status-aware closure | Engineering | Body wikilinks at review/published; cross-project violations |
| Research review integrity | Engineering | Invalid claim records, report shape gaps, protected-file contamination |

Output: `reports/lint-{date}.md` with severity per finding.

---

## Lifecycle states

Project artifacts move through:

| State | Sub-states | Notes |
|---|---|---|
| `in-progress` | `draft`, `review` | Active project work |
| `published` | (single state) | Completed; referenceable by other projects |
| `archived` | (single state) | Removed from active consideration; on disk for audit |

Transition rules:
- `draft` → `review`: requires Engineer-led finalize step (body wikilinks removed, See Also populated, status updated)
- `review` → `published`: requires `align-cite` and `align-closure` to pass (or explicit override)
- `published` → `archived`: explicit `archive` operation
- `archived` → any: requires explicit `unarchive`

---

## Conventions

- **Wikilinks:** Obsidian-style `[[path/to/article]]` without `.md` extension. Section anchors: `[[file#heading]]`. Block IDs: `^block-id`.
- **Writing style:** Encyclopedia-style, factual, third-person where appropriate. Match the exemplar in `docs/style/exemplar-published-doc.md` for project artifacts.
- **Dates:** ISO 8601 (`YYYY-MM-DD` for dates; `YYYY-MM-DDTHH:MM:SSZ` for timestamps).
- **File naming:** lowercase, hyphens for spaces (e.g., `microservice-sizing-standard.md`).
- **Frontmatter:** Every article must have YAML frontmatter with at minimum `title`, `type`, `sources`, `status`, `created`, `updated`. Articles with authority require `authority` and `domain`.
- **Sources:** Always link back to the raw page or external URL that contributed.

---

## File structure (full)

```
second-brain/
├── README.md
├── AGENTS.md                              # this file
├── LICENSE
├── .gitignore
├── .env.example
│
├── .github/
│   ├── README.md
│   ├── copilot-instructions.md            # Copilot shim
│   ├── prompts/
│   │   ├── second-brain.prompt.md
│   │   ├── start-project.prompt.md
│   │   ├── vp-agent.prompt.md
│   │   ├── pm-agent.prompt.md
│   │   ├── architect-agent.prompt.md
│   │   ├── engineer-agent.prompt.md
│   │   ├── finalize.prompt.md
│   │   ├── ingest-confluence.prompt.md
│   │   ├── ingest-jira.prompt.md          # v1.x
│   │   ├── ingest-vendor-doc.prompt.md
│   │   ├── revalidate-vendor-docs.prompt.md
│   │   ├── compile.prompt.md
│   │   ├── query.prompt.md
│   │   ├── research-review.prompt.md
│   │   ├── research-review/
│   │   ├── align-cite.prompt.md
│   │   ├── align-conformance.prompt.md
│   │   ├── align-coverage.prompt.md
│   │   ├── align-vendor-truth.prompt.md
│   │   ├── align-closure.prompt.md
│   │   ├── publish.prompt.md
│   │   ├── prepare-for-confluence.prompt.md
│   │   ├── publish-to-confluence.prompt.md
│   │   ├── archive.prompt.md
│   │   ├── unarchive.prompt.md
│   │   └── lint.prompt.md
│   ├── agents/                            # placeholder
│   │   └── README.md
│   └── skills/
│       ├── README.md
│       ├── obsidian-markdown/SKILL.md
│       ├── obsidian-bases/SKILL.md
│       ├── defuddle/SKILL.md
│       └── research-review/SKILL.md
│
├── CLAUDE.md                              # Claude Code shim
├── .cursor/rules/agents.mdc               # Cursor shim
├── .windsurfrules                         # Windsurf shim
│
├── docs/
│   ├── product-brief.md
│   ├── PRD.md
│   ├── architecture-rationale.md
│   ├── roadmap.md
│   ├── progress-log.md
│   ├── product-intelligence/
│   ├── setup-kit.md
│   ├── adoption-checklist.md
│   └── style/
│       └── exemplar-published-doc.md
│
├── config/
│   ├── second-brain.example.yml
│   └── second-brain.yml                   # gitignored
│
├── templates/
│   └── personas/
│       ├── ceo/                           # populated in v1
│       ├── engineer/                      # stub
│       ├── architect/                     # stub
│       ├── product-manager/               # stub
│       ├── director/                      # stub
│       └── vp/                            # stub
│
├── raw/                                   # content gitignored; structure tracked
│   ├── README.md
│   ├── confluence/
│   ├── jira/                              # v1.x
│   ├── external/
│   └── transcripts/
│
├── wiki/                                  # content gitignored; structure tracked
│   ├── index.md
│   ├── log.md
│   ├── standards/
│   ├── recommendations/
│   ├── informational/
│   ├── concepts/
│   ├── connections/
│   ├── qa/
│   ├── research/
│   ├── projects/
│   ├── archives/
│   └── views/
│
├── confluence-review/                     # gitignored
├── quarantine/                            # gitignored
├── reports/                               # gitignored
│
├── reference-documents/
│   └── README.md
│
├── .obsidian/                             # tracked
│   ├── workspace.json
│   ├── app.json
│   └── plugins/
│
└── scripts/
    ├── verify-setup.py
    └── README.md
```

---

## Vendor doc TTL configuration

In `config/second-brain.yml`:

```yaml
vendor_revalidation:
  default_ttl_days: 90
  per_vendor: {}                 # user can override per vendor, e.g., aws: 60
  hard_max_age_days: 365

confluence_sync:
  default_cadence: weekly
  reminder_after_days: 7
```

Behavior:
- Within TTL: cache is fresh; cite with `(cached YYYY-MM-DD)` annotation
- Past TTL but under hard max: flag stale and offer refetch before citing
- Past hard max: always prompt for refetch; cannot cite without refresh

---

## Project closure rules (summary)

1. Body prose at `review` and `published` contains no `[[wikilinks]]`. Navigation goes in `## See Also` or frontmatter.
2. Vendor capability claims use parenthetical attribution + See Also link. Inline detail not required.
3. Internal team standards: inline the relevant rules + provide Confluence URL in See Also.
4. In-progress project cannot reference another in-progress or archived project. Resolution: finish, archive, or restate.
5. `align-closure` runs automatically before publish; violations block unless user explicitly overrides.
6. The bar: a junior engineer can execute the work using only the published artifact set.

---

## On co-evolution

This document is the operating spec, but it is also the user's working knowledge of how Second Brain operates. As you and the user discover better patterns, update this document. Record changes in `docs/progress-log.md`. The schema is yours to refine; the user's job is to direct the work and accept or reject your suggestions.
