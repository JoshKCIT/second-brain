# Product Brief: Second Brain

**Status:** Draft v0.1 (scaffolded; gaps marked `[NEEDS INPUT]`)
**Owner:** Josh
**Last updated:** 2026-04-28

This document precedes and informs the Product Requirements Document. Its purpose is to lock the problem, the user, the constraints, and the success criteria so that the PRD can specify a solution against a stable foundation. Everything in the PRD should trace back to a statement in this brief.

---

## 1. Problem statement

### 1.1 The problem
Engineers, architects, and directors at [ORG] spend significant time locating, synthesizing, and citing information that lives across a large Confluence instance (10,000+ pages, ~10 departments). The current workflow has two failure modes:

1. **Rovo is adequate for short Q&A but inadequate for multi-step structured documentation generation.** Atlassian Intelligence (Rovo) is the org's current AI search and generation layer. Specific failure modes observed:
   - **Truncated responses.** Rovo stops mid-way through providing answers on non-trivial generation tasks. Likely cause: one-shot orchestration combined with output-token limit.
   - **Poor detail when documentation is vast.** When the relevant Confluence corpus is large, Rovo returns shallow answers or misses material. Likely cause: context-window limit and naive retrieval.
   - **No multi-page templating.** Rovo cannot apply a single formatting template across multiple pages or sections in one workflow.
   - **Weak architectural synthesis.** When asked to match candidate architectural approaches against spec requirements, Rovo provides sub-par answers or fails to respond. This is the highest-value failure to fix: hardest to do manually, most repeatable across teams, and closest to the documents the user actually needs to produce.

2. **Documentation drafting.** Producing a runbook, ADR, design document, or status summary today is a manual exercise in copy-paste from Confluence, with no automated grounding or citation.
   - Recent concrete example of this taking too long or producing a bad result: `[NEEDS INPUT]`

### 1.2 Evidence the problem is worth solving

Reconciled against public evidence as of April 29, 2026 (third-party scan of Rovo, Glean, Sourcegraph Cody, Notion AI, and Microsoft Copilot for M365 capabilities, plus first-person Rovo observations in §1.1).

**What Rovo and alternatives have closed since early 2025** (Second Brain should NOT re-build these):

- Generic enterprise search and Q&A (Rovo Search/Chat, Glean, Microsoft Copilot, Notion AI)
- Generic multi-step agent workflows (Glean has chained steps with branches, subagents, and memory; Microsoft Copilot has GA multi-step app-native actions in Word/Excel/PowerPoint)
- Basic page templates (Notion API/MCP)
- VS Code IDE integration with codebase + Confluence + Jira context (Rovo Dev is GA in VS Code; Sourcegraph Cody)
- Deep Research mode for structured reports from scoped sources (Rovo, with operational limits: 15-minute timeout, 30 requests per user per day)
- Atlassian Rovo MCP Server is GA and exposes Rovo Search/fetch and product actions to AI clients (ChatGPT, Claude, Cursor, GitHub Copilot, VS Code)

**What remains uncovered** (the Second Brain build case):

| Required capability | Available in Rovo / Glean / Cody / Notion / Copilot? | Why it matters |
|---|---|---|
| Source authority + domain tagging with claim-level conflict resolution (vendor:aws vs internal etc.) | Partial (Microsoft Copilot designates authoritative SharePoint sites for ranking; no tool resolves vendor-vs-internal claim conflicts by domain) | Internal claims about vendor capabilities can silently contradict vendor docs; no tool detects this |
| Vendor truth validation with TTL-cached vendor docs and revalidation | No | Vendor capabilities change; cached internal claims become stale and wrong |
| Junior-engineer-executable closure rule (published artifact set must be sufficient on its own) | No | Generated docs typically require follow-up conversation to use, defeating the purpose |
| Project artifact lifecycle (in-progress / published / archived) with cross-project dependency rules for AI-generated documentation | No (Jira/Confluence model workflow states; no AI-doc system enforces dependency validation across projects) | In-progress projects can tangle on each other with no enforcement |
| Mandatory section-level citation discipline for multi-page technical docs | No (Glean, Sourcegraph, and Microsoft offer deep-linked or section-anchor citations as features; none enforce them as policy across multi-page artifacts) | Verification requires reading the cited section, not the whole page |
| Inspectable retrieval enforced before generation as policy | No (Sourcegraph and Glean show retrieved chunks; neither enforces inspection as policy) | Cannot debug failed answers or missing context |
| Multi-page stage-gated technical-doc generation with Confluence-storage-format output | No (Rovo agents cannot emit Confluence storage-format XML reliably; Notion supports basic templates only; Glean and Microsoft strong on multi-step agents but not Confluence-grounded technical-doc focused) | Manual workaround for any structured doc set with cross-artifact alignment |

**Direct first-person evidence (§1.1) and corroborating Atlassian Community reports (2025-2026):**

- Rovo truncates on non-trivial generation tasks (§1.1, direct observation)
- Rovo cannot apply formatting templates across multiple pages in one workflow (§1.1, direct observation)
- Rovo gives sub-par or no answer on architectural-synthesis queries (§1.1, direct observation)
- Manual space selection/workspace-publishing required for Rovo-generated Confluence pages (Atlassian Community 2025-2026)
- Rovo agents cannot output Confluence storage-format XML/HTML or trigger richer formatting (Atlassian Community)
- Rovo unreliable at reading Confluence databases, attachments, images, and Assets objects (Reddit/Community reports)

**The Atlassian Rovo MCP Server is GA but is a connector, not a governance engine.** It exposes Rovo Search/fetch and product actions to external AI clients via signed-in user permissions. It does not store or cache content, does not provide structured staged generation, and does not implement vendor validation, lifecycle rules, or closure checks. This is useful as the data layer for Second Brain (validates the build-week-1 spike target) but does not substitute for the governance capabilities listed above.

**The build is justified because:**

1. The remaining capability gaps are real and not on Atlassian's published roadmap as of April 2026
2. The build leverages existing infrastructure (Rovo MCP as data layer, Copilot agent mode, MCP standard, the user's existing API ingestion skill as fallback) so foundational engineering is reduced
3. Build cost (10-14 weeks of LLM-assisted solo build) is comparable to the cost of waiting for Atlassian to add governance capabilities (12-24 months estimated, no guarantee of design fit)

**Scope discipline:** every Second Brain feature must answer "does this address a governance/closure/vendor-truth gap, or am I re-building a generic capability the alternatives already provide?" Generic-band features (enterprise search, Q&A, generic multi-step agents, basic templates, IDE-integrated codebase chat) are explicitly out of scope; see §8.1 Risk 7.

### 1.3 Why now

Three triggers converged in 2026:

- **Capability availability.** GitHub Copilot agent mode is stable; the MCP standard has been adopted (Atlassian Rovo MCP Server is GA); cross-agent skill specifications are emerging (`agentskills.io`). The building blocks for a system of this scope exist that did not in early 2025.
- **Cost shift.** LLM-assisted solo builds are realistic for systems of this scope. What required a 3-person team in 2024 can be built by one person in 10-14 weeks in 2026, with the agent chain itself doing most of the implementation work.
- **Governance gap is durable.** Rovo, Glean, Microsoft Copilot, and Notion AI have substantially closed generic capabilities since early 2025 (search, Q&A, multi-step agents, basic templates), but the governance capabilities Second Brain targets (claim-domain authority, vendor TTL revalidation, jr-executable closure, multi-page lifecycle, mandatory section citations) are not on any published roadmap. Waiting for vendors to add them is a bet that may not pay off; even if shipped, the design may not fit the multi-agent governed workflow needed.

---

## 2. Target users and use cases

### 2.1 Primary user
`[NEEDS INPUT — designate one: Engineer, Architect, or Director. The PRD draft treated all three as equal, which dilutes design decisions. The other two should be designated secondary; their needs ride on the primary's surface.]`

### 2.2 Jobs to be done

For each job, specify how often it occurs today and roughly how long it takes, so success can be measured against the current state.

| # | Job | Frequency | Time today | Primary pain |
|---|---|---|---|---|
| 1 | "Match candidate architectural approaches against spec requirements; produce a comparison or rationale document" *(named in §1.1 as the highest-value Rovo failure; candidate v1 doc type)* | `[NEEDS INPUT]` | `[NEEDS INPUT]` | Rovo gives sub-par or no answer; manual cross-referencing is high-effort |
| 2 | "Apply a formatting template across multiple Confluence pages or sections in one workflow" *(named in §1.1 as a Rovo failure)* | `[NEEDS INPUT]` | `[NEEDS INPUT]` | Rovo cannot do this in one workflow; manual is repetitive |
| 3 | "Find the canonical doc on X across multiple spaces" | `[NEEDS INPUT]` | `[NEEDS INPUT]` | `[NEEDS INPUT]` |
| 4 | "Draft a runbook for X grounded in existing docs" | `[NEEDS INPUT]` | `[NEEDS INPUT]` | `[NEEDS INPUT]` |
| 5 | "Draft an ADR for X" | `[NEEDS INPUT]` | `[NEEDS INPUT]` | `[NEEDS INPUT]` |
| 6 | `[NEEDS INPUT — add other recurring jobs]` | | | |

### 2.3 Anti-personas (who this is NOT for)
- Non-technical staff
- Users without Confluence access
- `[NEEDS INPUT — anyone else explicitly excluded?]`

---

## 3. Vision

One paragraph that any reader can repeat back without paraphrase. Draft based on the conversation; revise to taste:

> Second Brain is a local-first knowledge and documentation system for engineers, architects, and directors at [ORG]. It runs inside VS Code with GitHub Copilot. The user ingests scoped Confluence content into a local Markdown vault, queries that vault with hybrid retrieval, and generates new documentation grounded in canonical sources with verifiable citations. It is distinct from Atlassian Intelligence (Rovo) because the user controls the retrieval scope per project, can inspect every retrieved chunk before generation, and gets section-level citations rather than page-level pointers.

`[CONFIRM, REVISE, OR REPLACE]`

---

## 4. How it should function

### 4.1 Working principles
1. **Filesystem-first.** Every artifact is plain Markdown or JSON, inspectable without the tool.
2. **Citation-grounded.** No generated claim without a source link to a Confluence page and section.
3. **Approval-gated mutations.** Ingestion, sync, remove, and archive require explicit user approval after a diff preview.
4. **Scoped retrieval.** Per-project space scoping is first-class. Cross-department noise is suppressed by default.
5. **No telemetry.** No phone-home, no analytics in v1.
6. **Inspectable retrieval.** The user can see every retrieved chunk before generation, with provenance.
7. `[NEEDS INPUT — additional principles?]`

### 4.2 Key flows (sketch; PRD will detail)
1. Setup: clone, configure `.env`, run `secondbrain init`
2. Project: create project, select in-scope Confluence spaces
3. Ingest: provide Confluence URL, review diff, approve, vault populates
4. Query: ask question, receive cited answer scoped to the active project
5. Generate: ask for a doc type, receive cited draft written to project directory
6. Sync: re-fetch in-scope spaces, review diff, approve
7. Archive or remove: explicit, with confirmation

---

## 5. Scope notes

### 5.1 In scope for v1

`[NEEDS INPUT — pick one. The two candidates differ by roughly a factor of three in build calendar.]`

**Option A — Vertical slice (3-4 weeks build, validates core hypothesis):**
- One Confluence space ingestion
- BM25-only retrieval with citations
- Generation for one doc type (e.g., runbook)
- Manual re-run of ingest as the "sync" mechanism
- CLI surface only
- No rerank, no archive, no backup, no run history beyond logs

**Option B — Full v1 (3-6 months build, current PRD draft):**
- Multi-space ingestion with project scoping
- Hybrid retrieval (BM25 + vector + RRF + optional rerank + neighbor expansion)
- Generation for multiple doc types
- Sync with diff review
- Archive, remove, backup, run history, quarantine
- CLI + Copilot agent (MCP) surfaces

### 5.2 Out of scope for v1
- Multi-user / shared vault
- Write-back to Confluence (Second Brain reads only)
- Real-time collaboration
- Mobile or web UI
- Knowledge sources beyond Confluence (no Slack, Drive, GitHub, Notion in v1)
- General-purpose chat or assistant behavior
- `[NEEDS INPUT — anything else explicitly out?]`

---

## 6. Constraints

### 6.1 Hard constraints (cannot be violated)
- **IDE.** VS Code + GitHub Copilot. Cursor and Cody are not options.
- **Source.** Atlassian Cloud, Enterprise tier (Confluence + Jira on the same tenant). Confluence is the canonical knowledge source for v1; Jira ingestion deferred to v1.x.
- **Build team.** Solo engineer (Josh) + LLM build agent inside Copilot. No PM, designer, or QA.
- **Access.** Governed by the user's existing Confluence permissions. No ACL bypass.
- **Secrets.** Stored in `.env` only. Never written to vault, index, or run manifests.
- **Ingestion path.** Confluence ingestion path determined by build-week-1 spike; both Atlassian Rovo MCP Server (GA April 2026) and REST API v2 are viable. `docs/product/architecture-rationale.md` §5 carries the rationale and the gate criteria for the spike.

### 6.2 Soft constraints (preferences with override paths)
- **Local-first storage.** Override path: `[NEEDS INPUT — under what circumstances would a shared backend be acceptable?]`
- **No telemetry.** Override path: `[NEEDS INPUT — would opt-in telemetry for retrieval-quality measurement be acceptable?]`
- **Single-user.** Override path: `[NEEDS INPUT — at what point would multi-user become a v1.x priority?]`

### 6.3 Resource constraints
- **Build calendar.** 10-14 weeks of focused solo build for v1 with the full scope. Re-evaluation gates at week 8 (per §7.3 kill criterion 2).
- **Recurring API budget.** No monthly ceiling. Spend is shaped by vendor TTL defaults (90 days), Confluence sync cadence (weekly), on-demand vendor doc fetching, and per-project compile cost. If costs become a concern, add `monthly_budget_usd` to `config/second-brain.yml` for advisory tracking; not enforced.

---

## 7. Success criteria

The current PRD's metrics lack measured baselines. Each criterion below specifies a measurement protocol so the metric is computable rather than aspirational.

### 7.1 Adoption signal (binary, primary)
After a 4-week pilot using v1 against your own work, do you prefer Second Brain to (Rovo + manual drafting) for at least 2 of the top 4 jobs in §2.2? If not, the hypothesis is not validated and v1.x should not proceed.

### 7.2 Quantitative targets

For each, the protocol must be defined before the build, not after.

| Metric | Protocol | Target |
|---|---|---|
| Time to first acceptable draft of [doc type] | Stopwatch on N=10 sessions, baseline measured pre-build | `[NEEDS INPUT]` |
| Citation precision | 30-query labeled holdout; rate each cited claim 1 (supported) / 0 (not) by independent reviewer | `[NEEDS INPUT, recommend ≥80%]` |
| Retrieval recall@5 | Same holdout; mark each query's known-relevant pages and check top-5 | `[NEEDS INPUT, recommend ≥70%]` |

### 7.3 Kill criteria

The project should be stopped (not iterated) if any of the following thresholds is breached:

1. **Citation precision floor.** If after tuning, `align-cite` cannot reach 70% precision on a 30-claim labeled holdout, citation grounding is not real and the project's core differentiator fails. Measure after Phase 4.

2. **Build calendar reality.** If by week 8 of build, the agent chain is not producing usable end-to-end output on at least one real project, the workflow has fundamental issues. Reassess scope: cut to a vertical slice (one persona, one doc type, BM25-only retrieval) or stop entirely.

3. **Junior-engineer executability fails repeatedly.** If the first 3 published projects fail the jr-engineer-executability test when actually attempted by a real jr engineer (the engineer cannot complete the work without follow-up), the closure rule is not being applied correctly. Revise the closure rule and the agent prompts; if the bar still cannot be met after revision, the v1 hypothesis fails.

4. **`align-vendor-truth` false-positive rate erodes trust.** If the lint produces false-positive rates above 30% over 50 invocations, the user starts ignoring it, defeating its purpose. Drop the check from v1 and reconsider the vendor truth approach.

5. **Foundational ingestion path broken.** If neither the Atlassian MCP spike nor porting the user's existing API skill produces a working ingestion path by end of build week 2, the foundational data layer does not exist. Pause and reassess whether v1 can proceed.

---

## 8. Risks and open questions

### 8.1 Top risks (ranked)
1. **Build-vs-buy underestimated for generic capabilities.** Per §1.2, Rovo (Search, Chat, Agents, Studio, Canvas, MCP server, Rovo Dev in VS Code), Glean, Microsoft Copilot for M365, Notion AI, and Sourcegraph Cody cover generic enterprise search, Q&A, multi-step agents, IDE-integrated codebase chat, and basic templating. The Atlassian Rovo MCP Server is GA. **Mitigation:** narrow Second Brain's positioning to governance and closure capabilities only (claim-domain authority, vendor TTL revalidation, inspectable retrieval as policy, mandatory section citations, multi-page closure, lifecycle and cross-project rules). Do not re-build generic capabilities the alternatives provide. Test Rovo MCP as the data layer in build week 1; if it works, use it instead of porting the API skill.
2. **Confluence content quality.** Most large instances have 30-60% stale or duplicate pages. Garbage-in-garbage-out for generation. **Mitigation:** page curation (label allowlist, owner allowlist) at ingestion; do not ingest indiscriminately.
3. **ADF macro coverage.** ADF→Markdown conversion has an open-ended long tail. **Mitigation:** quarantine + iterative coverage; reconsider storage format if its converter ecosystem is materially better.
4. **Citation accuracy.** LLMs cite confidently and incorrectly. URL resolution does not equal claim support. **Mitigation:** NLI-based or rule-based claim-to-source verification, or a strong UX warning that drafts are starting points only.
5. **Single-user vs reusable dev-kit contradiction.** Cannot ship both as currently described. Ten engineers each cloning and ingesting the same Confluence creates ten divergent vaults and 10x API pressure. **Mitigation:** pick one architecture before tech-stack discussion.
6. **Build calendar optimism.** Solo build of full v1 in 6-10 weeks is aggressive. Realistic estimate is 3-6 months for full v1, or 3-4 weeks for the vertical slice in §5.1 Option A.
7. **Scope creep into competitor territory.** The temptation to add generic enterprise search, Q&A, generic multi-step agents, IDE-integrated codebase chat, or basic page templates would put Second Brain in direct competition with Rovo, Glean, Microsoft Copilot, Notion AI, and Sourcegraph Cody on dimensions where they are stronger. **Mitigation:** every feature must answer "is this in the governance/closure/vendor-truth band, or in the generic AI-workflow band?" Generic-band features get cut. The §1.2 capability table is the canonical scope filter; reject any v1.x feature proposal that does not appear in the gap table.

### 8.2 Open questions (load-bearing — must resolve before PRD finalizes)
1. **Single-user local or shared service?** Determines architecture and recurring cost. Cannot be deferred.
2. **Which specific Rovo failure modes is Second Brain built to fix?** Determines the differentiator and which features are load-bearing vs decoration. Without this, the build risks producing different failure modes rather than fewer.
3. **v1 scope: vertical slice (Option A) or full (Option B)?** Determines build calendar, validation timeline, and which decisions matter in v1 vs v1.x.
4. **Primary surface: CLI, Copilot agent (MCP), or both?** Determines the integration model and constrains LLM and framework choices.
5. **Confluence Cloud, Server, or Data Center?** Affects API surface and authentication.

### 8.3 Open questions (deferable to build time)
- Embedding model and reranker (decide after a small benchmark on representative pages)
- Markdown converter library (decide after a sample-page evaluation)
- Backup target (default to local directory; revisit if needed)
- Encryption at rest (default to OS-level full-disk encryption in v1)
- Multi-language content (default English-only in v1 unless evidence demands otherwise)

---

## 9. Decisions log (running)

Record decisions here with date and rationale as they resolve. Each decision retired from §8.2 should land here with a one-line summary.

| Date | Decision | Rationale | Question retired |
|---|---|---|---|
| `[YYYY-MM-DD]` | `[decision text]` | `[one line]` | `[OQ#]` |

---

## Appendix: Connection to PRD

Once this brief is filled in:
- §1 → PRD §1.2 Product summary and §6 Narrative
- §2 → PRD §3 User personas and §10 User stories
- §3 → PRD §1.2 and §2 Goals
- §4.1 → PRD §5.4 UX highlights and §8 Technical considerations
- §4.2 → PRD §5.2 Core experience
- §5 → PRD §2.3 Non-goals and §4 Functional requirements
- §6 → PRD §8 Technical considerations
- §7 → PRD §7 Success metrics
- §8 → PRD Open Questions

The PRD should not introduce new decisions. If the PRD needs something not covered here, that is a signal to come back to this brief.
