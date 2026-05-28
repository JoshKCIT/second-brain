# Architecture Rationale

**Status:** v1.0
**Last updated:** 2026-04-28

This document records the design decisions behind Second Brain v1, the alternatives considered, and the tradeoffs accepted. It is the place to come when a future contributor (or a future you) asks "why did we do it this way?"

---

## 1. Pattern: Karpathy + Cole, not pure RAG

**Decision:** Use Karpathy's three-layer wiki pattern (raw / curated wiki / schema document) with Cole's compiler refinements (two-stage extraction, formalized article types, structured index and log, tight conventions, state tracking, lint).

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Pure RAG (NotebookLM-style) | LLM rediscovers knowledge per query; no compounding; no synthesis durability |
| Karpathy alone | Lacks implementation depth; no formalized article types or lint check inventory |
| Cole alone | Source model is Claude Code conversations, not Confluence pages; capture mechanism (Claude Code hooks) does not work in Copilot |
| Custom design from scratch | Wheel reinvention; both Karpathy and Cole have validated patterns |

**Why this combination:** Karpathy provides the conceptual model; Cole provides the implementation discipline. Adapting Cole's source layer from conversations to Confluence and his capture mechanism from hooks to LLM-invoked operations gives us a working pattern with proven UX.

**Tradeoff:** The wiki layer can drift over time as the LLM accumulates content. Mitigation: lint includes contradiction check; periodic full re-lint cadence; status-aware enforcement.

---

## 2. Distribution: GitHub repo, not hosted service

**Decision:** Ship as a clonable GitHub repository. Each user clones, configures `.env`, and runs locally.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| SaaS / hosted service | Adds operations burden; conflicts with single-user local model; data sovereignty concerns |
| npm / pip package | Less discoverable; package boundary fights against the "fork and adapt" expectation |
| Submitted PR to existing repo (Cole, Karpathy) | Cole's repo is conversations-as-source; Karpathy's is a gist; neither is a base for this product |

**Why GitHub repo:** Matches the user's stated goal ("people pull it down"). Fork-and-adapt is the natural extension model. OSS governance (PRs, issues, forks) is appropriate for the dev-kit framing.

**Tradeoff:** N users mean Nx Confluence API consumption against shared spaces and N divergent vault states. Acceptable in v1 because Second Brain is per-user research, not team artifact.

---

## 3. Single-user local in v1

**Decision:** Each user maintains their own wiki. No shared backend. No cross-user merge.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Shared wiki on a network drive | Concurrency complexity; merge conflict resolution; out of scope for a v1 |
| Cloud-hosted wiki with multi-user | Operations burden; security review; conflicts with local-first principle |
| Per-team wiki with sync | Sync semantics and merge protocols are research-grade; defer |

**Why single-user:** Karpathy's pattern is fundamentally personal. Multi-user wikis require merge protocols, conflict resolution, and access control that are not yet designed. Single-user-with-clone-distribution is the simplest model that scales to "many people each have their own."

**Tradeoff:** No team source of truth. Each user's wiki drifts based on their own ingest cadence and queries. Acceptable for personal research; revisit at v1.x if 3+ teammates ask to adopt.

---

## 4. Schema docs: AGENTS.md canonical + per-agent shims (Pattern 2)

**Decision:** `AGENTS.md` is the canonical operating spec. Per-agent shim files (`.github/copilot-instructions.md`, `CLAUDE.md`, `.cursor/rules/agents.mdc`, `.windsurfrules`) live in their conventional locations and reference AGENTS.md for full content. Each shim is operationally sufficient on its own (50-100 lines covering essentials).

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Single canonical file, manual copy by user | Pushes setup work to user; first-run friction conflicts with "clone and it works" goal |
| Setup script that creates the right shim | Symlink fragility on Windows; setup-step failure mode |
| Pick one agent, ignore others | User explicitly wants the repo to support multiple agents (since adopters use VS Code, Cursor, Claude Code variously) |

**Why Pattern 2:** Works out of the box across the major agents. Canonical content lives in one place. Maintenance burden is small (4 thin files to keep aligned with AGENTS.md when its structure changes).

**Tradeoff:** Verifying each agent honors the indirection takes a 30-minute test per agent before v1 release. AGENTS.md convention is still emerging (gaining adoption from OpenAI Codex CLI, Claude Code; less established for Cursor and Windsurf).

---

## 5. Confluence ingestion: spike MCP first, API as fallback

**Decision (revised April 2026):** Build week 1 spikes the Atlassian Rovo MCP Server (GA as of April 2026) as the primary data-layer path. If the MCP exposes the page metadata Second Brain needs (ADF body, version, last-modified, labels, ancestors, attachments) and works on the user's Enterprise tenant, use it. Otherwise, fall back to the user's existing API-based ingestion skill ported into the repo. The brief's §1.2 frames this: MCP is a connector, not a governance engine; whether it works for our data-layer use case is what the spike answers.

**Alternatives considered:**

| Alternative | Why rejected as v1 primary |
|---|---|
| API-first with MCP as alternative (the prior decision) | Now reversed: MCP being GA reduces the build burden if it works. The user's API skill is fallback, not default. |
| Custom Python pipeline from scratch | The user's existing API skill works as fallback; greenfield is wasteful |
| confluence-markdown-exporter or similar library | Format and frontmatter requirements differ from off-the-shelf converters; defer unless MCP and API both fail |

**Why MCP-first now:** Atlassian Rovo MCP Server reached GA between v1 planning and build start. It uses signed-in user permissions (no separate IP allowlisting concerns), exposes Rovo Search/fetch and product actions, and is supported by Atlassian. If it provides the metadata fidelity Second Brain needs, the build saves the porting effort and gets ongoing Atlassian-maintained data-layer support.

**Tradeoff:** MCP filters page content through Rovo's data layer; some metadata may be stripped or transformed in ways the REST API does not. The build-week-1 spike is the gate. If MCP is insufficient, the user's API skill ports in and the schema/frontmatter handling is unchanged.

---

## 6. Vendor doc handling: fetch-on-demand + cache + TTL

**Decision:** Vendor docs are fetched on demand when an agent is about to cite a vendor capability. Cached to `raw/workspace-external/{vendor}/{topic}/` with frontmatter. Default TTL 90 days; per-vendor overrides; hard max 365 days. Defuddle CLI extracts clean Markdown.

**Alternatives considered:**

| Alternative | Why rejected for v1 |
|---|---|
| Defer all vendor doc handling to v1.x | Vendor truth validation is the differentiator that addresses the S3-encryption-style failure mode; skipping it weakens the design |
| Pre-ingest vendor docs ahead of time via vendor MCPs | AWS docs alone are tens of thousands of pages; MCPs may not exist or be mature for all needed vendors; ingest cost is high upfront |
| Hit vendor docs at query time with no cache | Re-fetches every query; unreliable due to dynamic JS; expensive |

**Why fetch + cache + TTL:** The user's proposal balances cost and freshness. First fetch pays for the page once; cache reuses for the TTL window; revalidation handles staleness. Defuddle is the right tool for the fetch step (already proven; clean output).

**Tradeoff:** Web fetching is fragile (sites change, dynamic JS, occasional rate limits). TTL-based revalidation handles staleness but a vendor page disappearing mid-cache leaves a broken cite source. Mitigation: refresh cycle; manual refetch path; vendor MCP migration in v1.x.

---

## 7. Authority + domain tagging on every source

**Decision:** Every source carries two metadata tags: authority (standard, recommendation, informational) and domain (internal, vendor:aws, vendor:snowflake, industry:nist, etc.). Conflict resolution defers to the source authoritative for the claim's domain.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Authority alone | Does not handle vendor truth (the S3 example): an internal standard might claim something incorrect about S3, but treating it as authoritative is wrong because the claim is a vendor capability |
| Domain alone | Loses the standard-vs-recommendation-vs-informational distinction within a domain |
| No tagging; LLM judges per query | LLM judgment is inconsistent across queries; explicit tags provide predictable behavior |

**Why both:** The S3-encryption example forces this: internal docs about S3 are about vendor behavior and should defer to AWS; internal docs about our internal architecture are about our stuff and should be authoritative. Two-dimensional tagging cleanly handles both.

**Tradeoff:** Users must classify sources at setup (which spaces are standards-publishers, which domains they cover). One-time setup work; pays back through correct conflict resolution.

---

## 8. Multi-agent workflow chain (CEO → VP → PM → Architect → Engineer)

**Decision:** Project documentation is produced by a chain of specialized LLM agents, each with a defined role, input contract, output contract, and source-of-truth scope. CEO reviews and edits between stages.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Single-agent workflow | Loses the staged-review benefit; CEO would have to review one massive output rather than progressive artifacts |
| Multi-agent with autonomous handoffs (no CEO review between stages) | Loses CEO control; LLM errors compound across stages without correction opportunity |
| Heavy multi-agent orchestration with sub-agent spawning | Research-grade complexity; out of scope for v1 |

**Why staged with checkpoints:** Each artifact (brief, PRD, architecture, implementation specs) is a distinct deliverable with its own quality criteria. CEO review between stages catches errors early. Filesystem checkpoints at `wiki/workspace-projects/{slug}/0X-{stage}/` provide explicit handoff state.

**Tradeoff:** Multi-stage takes longer wall-clock than single-shot. Mitigation: each stage produces a useful artifact; the CEO can stop at any stage if the project does not warrant the full chain.

---

## 9. Three-state project lifecycle + closure rule

**Decision:** Projects move through `in-progress` (with `draft` and `review` sub-states), `published`, and `archived` states. An in-progress project cannot reference another in-progress or archived project. A published project's authored set must be jr-engineer-executable using only that set.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Single state (in-progress vs done) | Does not handle the cross-project reference question; in-progress projects depending on each other create tangled dependencies |
| PARA-style 4-state taxonomy | PARA's actionability dimension conflicts with our authority/domain model; over-categorizes for our use |
| No closure rule; documents can link freely | Loses the jr-engineer-executable bar; documents become unreadable without the wiki context |

**Why this model:** Three states cleanly handle: active work (in-progress), curated reference (published), and archived audit trail (archived). The closure rule operationalizes the "executable by a jr engineer" bar that defines completeness. Status-aware lint allows agents to use wikilinks during draft authoring (when handoff matters) while requiring clean prose at review and published.

**Tradeoff:** Status transitions add lifecycle ceremony. Closure rule may produce false-positive lint violations during authoring. Mitigation: status-aware lint defers strict checks until review; explicit override paths exist with audit logging.

---

## 10. Body-prose-clean rule + vendor citation + internal standards patterns

**Decision:**

- Body prose at `review` and `published` contains no `[[wikilinks]]`. Navigation goes in `## See Also` or frontmatter.
- Vendor capability claims use parenthetical attribution + See Also link. Inline detail not required.
- Internal team standards: inline the relevant rules in body + provide Confluence URL in See Also.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| All citations inline | Bloats body prose; reduces readability for jr engineer |
| All citations as wikilinks throughout | Body prose becomes a navigation document; loses readability |
| Vendor citations always inline detail | Bloats body for vendor claims that the reader can verify externally |
| Internal standards as wikilinks | Jr engineer may not have access to the linked Confluence page; cannot execute |

**Why the asymmetric pattern:** Vendor truth is verifiable externally (jr engineer can read AWS docs themselves). Internal standards may not be accessible (Confluence permissions). The asymmetry reflects access reality: inline what the reader cannot otherwise reach; reference what they can.

**Tradeoff:** Asymmetric rules are harder to remember than uniform rules. Mitigation: codified in AGENTS.md and enforced by `align-closure`.

---

## 11. Defer embeddings until wiki passes ~500 articles

**Decision:** No embeddings, no vector search, no hybrid retrieval in v1. **Page-index / structure-aware retrieval** is the default: the agent reads `wiki/index.md` and Base views, identifies relevant articles, reads them in full, and navigates long documents by hierarchy and section anchors rather than similarity chunking alone.

**Citation ≠ retrieval (RC-2026-05-27-002):** Semantic similarity or chunk proximity is not evidence of citation support. Retrieved context may inform drafting; `align-cite` verifies that each cited claim resolves to supporting source content before publish.

**Future retriever gate:** Any vector, hybrid, graph, or rerank retriever added after v1 must pass a holdout evaluation on long structured pages, demonstrating improved citation precision and inspectability without weakening junior-engineer closure. Until then, keep `align-cite` as a publish blocker.

Decision record: `docs/platform-decision-records/RC-2026-05-27-001-page-index-retrieval.md`

**Alternatives considered:**

| Alternative | Why rejected for v1 |
|---|---|
| BM25 search at v1 | Adds tooling burden; Cole and Karpathy both claim index-only is sufficient at <500 articles |
| Hybrid (BM25 + vector + RRF + rerank) at v1 | Significant complexity; not justified at expected v1 scale |
| sqlite-vec or LanceDB for vectors | Adds dependency on a young library (sqlite-vec is pre-1.0); embedding model choice creates lock-in |

**Why defer:** Karpathy's explicit claim ("works surprisingly well at moderate scale, ~100 sources, ~hundreds of pages") and Cole's specific band ("50-500 articles index-only") give us a defensible threshold. v1 is unlikely to exceed it. Adding embeddings prematurely is the kind of complexity that kills personal-tool projects.

**Tradeoff:** Index-guided retrieval can fail when the LLM cannot identify relevant articles from titles and one-line summaries alone. Mitigation: rich index format with embedded Base views; on failure, refine the index entry's summary.

---

## 12. Obsidian as canonical reader; zero plugins required

**Decision:** Obsidian is the canonical reader for the wiki. Repo ships a default `.obsidian/` config. No VS Code or Obsidian plugins are required for v1.

**Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Foam or Dendron as the reader | Foam/Dendron are alternatives to Obsidian, not complements; conflict with Obsidian-flavored markdown conventions |
| obsidian-visualizer (graph view in VS Code) required | Adds dependency without proportional value; user can install if friction surfaces |
| No reader; users open files in VS Code only | VS Code does not render wikilinks, callouts, or graph view natively; loses Obsidian's primary value |
| Custom Obsidian plugin for Second Brain | Adds maintenance surface; the filesystem contract is sufficient |

**Why Obsidian + zero plugins:** The filesystem is the integration layer between VS Code (authoring) and Obsidian (reading). Both apps look at the same Markdown files. No plugin needed for the core architecture. Optional convenience plugins documented in README for users who feel specific friction.

**Tradeoff:** Users without Obsidian installed lose the graph view, backlinks, and Bases. Mitigation: README documents Obsidian as required; setup-kit walks through install.

---

## 13. Naming: "Second Brain" not "Principal Second Brain"

**Decision:** Project named "Second Brain."

**Why:** Cleaner. "Principal" implied a specific seniority focus that does not match the multi-persona stub model.

**Tradeoff:** Conflicts with Tiago Forte's "Building a Second Brain" book (which inspired the name via the awesome-PARA-method repo). Acceptable: the trademark is on the book and course, not on the term.

---

## When this architecture is a poor fit

Second Brain is built for a specific shape of problem. It is not the right tool when:

- The source of truth is a strict relational or transactional system (use a database, not a wiki)
- Updates must be fully automated and immediately trusted (the human-in-the-loop principle is foundational here)
- The team cannot invest in maintaining schema and taxonomy (the AGENTS.md and authority/domain mappings co-evolve; static use degrades fast)
- Compliance constraints require stronger guarantees than markdown plus review (HIPAA, SOX, etc. may need formal records management)
- The use case is real-time collaboration (single-user local does not fit)
- The domain is non-textual (image-heavy, audio, video) without significant Markdown adaptation work
