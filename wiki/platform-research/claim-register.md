# Research Claim Register

This register tracks transcript-derived claims about Second Brain.

Transcripts are product-intelligence evidence. They are not canonical knowledge by default.

## Decision Legend

| Decision | Meaning |
|---|---|
| `adopt` | Implement or document immediately after user approval |
| `experiment` | Test before adoption |
| `defer` | Valuable but blocked by dependency |
| `reject` | Harmful, redundant, generic, or misaligned |
| `monitor` | External market/vendor claim to revisit later |

## Decision index

Quick navigation for review. Full rejection history lives in `wiki/platform-research/rejected-ideas.md`.

| Decision | Claim IDs |
|---|---|
| adopt | RC-2026-05-27-001, RC-2026-05-27-002, RC-2026-05-27-004, RC-2026-05-27-006, RC-2026-05-27-010, RC-2026-05-27-014, RC-2026-05-27-016, RC-2026-05-27-017, RC-2026-05-27-018, RC-2026-05-27-032, RC-2026-05-27-035, RC-2026-05-27-039, RC-2026-05-27-082, RC-2026-05-27-087, RC-2026-05-27-089, RC-2026-05-27-090, RC-2026-05-27-091, RC-2026-05-27-092, RC-2026-05-27-093, RC-2026-05-27-097, RC-2026-05-27-098, RC-2026-05-27-105, RC-2026-05-27-111, RC-2026-05-27-113, RC-2026-05-27-115, RC-2026-05-27-137, RC-2026-05-27-147, RC-2026-05-27-157, RC-2026-05-27-158, RC-2026-05-27-160, RC-2026-05-27-161, RC-2026-06-09-003, RC-2026-06-09-009, RC-2026-06-09-011, RC-2026-06-09-012 |
| experiment | RC-2026-05-27-003, RC-2026-05-27-007, RC-2026-05-27-008, RC-2026-05-27-009, RC-2026-05-27-012, RC-2026-05-27-015, RC-2026-05-27-019, RC-2026-05-27-020, RC-2026-05-27-021, RC-2026-05-27-024, RC-2026-05-27-029, RC-2026-05-27-030, RC-2026-05-27-031, RC-2026-05-27-036, RC-2026-05-27-037, RC-2026-05-27-038, RC-2026-05-27-042, RC-2026-05-27-083, RC-2026-05-27-094, RC-2026-05-27-102, RC-2026-05-27-103, RC-2026-05-27-107, RC-2026-05-27-112, RC-2026-05-27-114, RC-2026-05-27-135, RC-2026-05-27-136, RC-2026-05-27-138, RC-2026-05-27-139, RC-2026-05-27-140, RC-2026-05-27-141, RC-2026-05-27-142, RC-2026-05-27-146, RC-2026-05-27-148, RC-2026-05-27-149, RC-2026-05-27-162, RC-2026-05-27-163, RC-2026-05-27-164, RC-2026-05-27-165, RC-2026-05-27-166, RC-2026-05-27-167, RC-2026-06-09-001, RC-2026-06-09-004, RC-2026-06-09-005, RC-2026-06-09-007, RC-2026-06-09-013 |
| defer | RC-2026-05-27-005, RC-2026-05-27-011, RC-2026-05-27-086, RC-2026-05-27-088, RC-2026-05-27-106, RC-2026-06-09-002, RC-2026-06-09-015 |
| reject | RC-2026-05-27-009a, RC-2026-05-27-013, RC-2026-05-27-023, RC-2026-05-27-025, RC-2026-05-27-026, RC-2026-05-27-027, RC-2026-05-27-033, RC-2026-05-27-034, RC-2026-05-27-040, RC-2026-05-27-041, RC-2026-05-27-084, RC-2026-05-27-085, RC-2026-05-27-095, RC-2026-05-27-099, RC-2026-05-27-100, RC-2026-05-27-101, RC-2026-05-27-104, RC-2026-05-27-108, RC-2026-05-27-109, RC-2026-05-27-110, RC-2026-05-27-131, RC-2026-05-27-132, RC-2026-05-27-133, RC-2026-05-27-134, RC-2026-05-27-144, RC-2026-05-27-150, RC-2026-05-27-151, RC-2026-05-27-152, RC-2026-05-27-153, RC-2026-05-27-154, RC-2026-05-27-156, RC-2026-05-27-159, RC-2026-05-27-168, RC-2026-05-27-169, RC-2026-05-27-170, RC-2026-05-27-171, RC-2026-05-27-172, RC-2026-05-27-175, RC-2026-06-09-006, RC-2026-06-09-016, RC-2026-06-09-017, RC-2026-06-09-018 |
| monitor | RC-2026-05-27-022, RC-2026-05-27-096, RC-2026-05-27-143, RC-2026-05-27-145, RC-2026-05-27-155, RC-2026-05-27-173, RC-2026-05-27-174, RC-2026-06-09-008, RC-2026-06-09-010, RC-2026-06-09-014 |

Rejected claims and recurring rejection patterns: see `wiki/platform-research/rejected-ideas.md`. Next scheduled re-review: **2026-08-27**.

Implementation queue (stack-lift order): see `wiki/platform-research/implementation-backlog.md`.

## Claim Records

Add new records below. Use one YAML block per claim.

```yaml
claim_id: RC-2026-05-27-001
source_transcript: raw/platform-transcripts/second-brain-no-vector-database.txt
speaker: unknown
timestamp: "00:00:00-00:01:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should prefer structure-aware page-index retrieval over vector chunking for long documents because it preserves document hierarchy and produces a transparent navigation trail."
verbatim_excerpt: "Instead of chunking first, it builds a table of contents tree that captures the document's structure."
implied_assumption: "The documents Second Brain handles have meaningful hierarchy that can guide retrieval better than embedding similarity."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-query
  - workspace-compile
  - workspace-align-cite
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "Reinforces the current index-guided retrieval decision and gives it an eval target around long structured documents."
possible_regression: "A rigid tree can miss cross-cutting content if connections and aliases are weak."
validation_method: "Run a holdout of long structured Confluence pages and compare index-guided section selection against any future vector baseline."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "This is already aligned with Second Brain's no-embeddings v1 architecture and strengthens the inspectable retrieval policy."
next_action: "Implemented and accepted in PIC-2026-05-27-003."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-002
source_transcript: raw/platform-transcripts/second-brain-no-vector-database.txt
speaker: unknown
timestamp: "00:00:00-00:01:00"
claim_type: risk_claim
atomic_claim: "Chunking and similarity search can retrieve semantically similar but non-answering context, so Second Brain should not treat similarity as evidence of citation support."
verbatim_excerpt: "Similarity isn't relevance. You often get chunks with the same vibe, but not the exact answer you need."
implied_assumption: "Citation support requires claim-level verification rather than proximity in embedding space."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-align-cite
  - workspace-query
related_second_brain_principles:
  - citation_grounding
  - inspectable_retrieval
expected_benefit: "Supports keeping align-cite as a production check rather than relying on retrieval confidence."
possible_regression: "Overcorrecting against embeddings could defer useful hybrid retrieval after the wiki exceeds index-only scale."
validation_method: "Track citation precision failures by retrieval source once any alternative retriever exists."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "The claim reinforces a core Second Brain distinction: retrieved context is not the same as verified support."
next_action: "Implemented and accepted in PIC-2026-05-27-003."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-003
source_transcript: raw/platform-transcripts/second-brain-self-learning-ideas.txt
speaker: unknown
timestamp: "00:00:30-00:01:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should have an explicit, controlled gap-research loop that periodically identifies missing platform knowledge and proposes sources to review."
verbatim_excerpt: "a self-learning skill... weekly... go through your brain and find gaps of information and research YouTube or Google... to fill and update those gaps"
implied_assumption: "Unaddressed gaps can be detected safely without allowing external research to mutate canonical docs automatically."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - platform-research-review
  - platform-research-open-hypotheses
  - docs/platform-decision-records
related_second_brain_principles:
  - human_review_leverage
  - source_authority
  - inspectable_retrieval
expected_benefit: "Creates a safer route for proactive platform learning while preserving review gates."
possible_regression: "If automated too far, it could pull noisy sources into platform direction and erode scope discipline."
validation_method: "Run one monthly gap-review cycle that produces only candidate transcripts/sources and no canonical edits."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 8
decision: experiment
decision_rationale: "The idea is valuable if constrained to candidate-source discovery and review artifacts, not automatic wiki mutation."
next_action: "Implemented and accepted in PIC-2026-05-27-005; run first gap review when user invokes /platform-gap-review."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-004
source_transcript: raw/platform-transcripts/second-brain-self-learning-ideas.txt
speaker: unknown
timestamp: "00:00:00-00:00:30"
claim_type: architecture_proposal
atomic_claim: "A local file-backed knowledge base visible to the coding agent is a suitable substrate for an AI-maintained second brain."
verbatim_excerpt: "use Obsidian as the software... as long as your cloud code can see the file structure"
implied_assumption: "Plain files are enough for the agent to maintain durable knowledge without a hosted database."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS
  - workspace-wiki
  - platform-research
related_second_brain_principles:
  - filesystem_first
  - inspectability
expected_benefit: "Confirms the existing filesystem-first architecture."
possible_regression: "None if treated as reinforcement rather than a new feature."
validation_method: "No new validation needed; covered by existing setup and lint expectations."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "This is already implemented as a foundational architectural principle."
next_action: "No canonical change; keep as already-supported evidence in the synthesis."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-005
source_transcript: raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt
speaker: Matt
timestamp: "00:05:00-00:16:30"
claim_type: architecture_proposal
atomic_claim: "A distributed knowledge protocol with sparse sync could support team-scale knowledge sharing better than each user cloning and ingesting a full local vault."
verbatim_excerpt: "huge graphs of documents that grow over time... you wouldn't want to pull the entire thing"
implied_assumption: "Second Brain's single-user local model will eventually need partial synchronization semantics for team adoption."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-enter queue when blocker clears; update claim register decision."
affected_components:
  - workspace-sync
  - multi-user-v2
  - architecture-rationale
related_second_brain_principles:
  - inspectability
  - enterprise_fit
expected_benefit: "Could reduce duplicated Confluence API load and divergent per-user vaults in a future shared model."
possible_regression: "Would substantially expand v1 scope into distributed systems, merge protocols, and access-control complexity."
validation_method: "Defer until 3+ teammates request shared-vault adoption; then compare Git-only, GitKB-like, and hosted sync approaches."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -2
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 0
total_score: 2
decision: defer
decision_rationale: "Potentially important for v2, but it conflicts with the explicit v1 single-user local constraint."
next_action: "Track as a v2 sync architecture candidate; do not alter v1."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-006
source_transcript: raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt
speaker: Matt
timestamp: "00:08:00-00:11:00"
claim_type: problem_evidence
atomic_claim: "Persistent structured knowledge reduces agent context loss compared with ephemeral session plans."
verbatim_excerpt: "Context loss. You have to recover. And it compounds."
implied_assumption: "Agents perform better when durable project context is written into structured files across sessions."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-projects
  - wiki-log
  - platform-research
related_second_brain_principles:
  - filesystem_first
  - inspectability
  - junior_engineer_closure
expected_benefit: "Reinforces why Second Brain uses filesystem handoffs and project-stage artifacts."
possible_regression: "None if treated as support for existing behavior."
validation_method: "Compare project resumption quality with and without stage artifacts during pilot."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "This is core to the current design and should remain explicit in docs and evaluations."
next_action: "Mention as already-supported evidence in batch synthesis."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-007
source_transcript: raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt
speaker: Matt
timestamp: "00:10:30-00:25:30"
claim_type: architecture_proposal
atomic_claim: "A regenerable graph projection from canonical Markdown could improve traversal and visualization without making the graph database the source of truth."
verbatim_excerpt: "your canonical data is your markdown files. And the knowledge graph comes out of that."
implied_assumption: "Second Brain can gain graph benefits while preserving filesystem-first inspectability."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-views
  - platform-research
  - future-graph-projection
related_second_brain_principles:
  - filesystem_first
  - inspectability
  - maintainability
expected_benefit: "Could make relationships easier to debug while preserving Markdown as canonical."
possible_regression: "Building graph infrastructure prematurely could duplicate Obsidian graph/Bases and add complexity."
validation_method: "Prototype a read-only graph report from existing wikilinks and compare reviewer usefulness against Obsidian/Bases."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: -1
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 5
decision: experiment
decision_rationale: "A generated, disposable graph could fit the architecture if it remains non-canonical and proves useful."
next_action: "Deferred: user prefers Obsidian graph. Re-enter backlog when Obsidian/Bases is insufficient for relationship review."
correction_route: "Re-queue in implementation-backlog.md when user wants custom graph projection."
owner: unassigned
status: deferred
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-008
source_transcript: raw/platform-transcripts/Graphify_-_Instant_Knowledge_Graph_for_Claude_Code_Antigravity_FREE.txt
speaker: unknown
timestamp: "00:00:30-00:04:30"
claim_type: architecture_proposal
atomic_claim: "A cached graph report read at session start can reduce repeated file reads and improve first-answer quality."
verbatim_excerpt: "every new session means a new hire... Graphify builds the senior colleague"
implied_assumption: "Session-start summaries can improve agent orientation without replacing source inspection."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - agent-onboarding
  - workspace-query
  - platform-research
related_second_brain_principles:
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "Could reduce repeated orientation work when agents start on this repo."
possible_regression: "A stale graph report could mislead agents if treated as authoritative."
validation_method: "Run paired agent tasks with and without a generated graph summary and compare read count, correctness, and time to answer."
impact_scores:
  governance: 0
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 2
decision: experiment
decision_rationale: "Worth testing as orientation support, but not as canonical knowledge or a v1 dependency."
next_action: "Deferred with RC-007; use Obsidian graph for orientation unless custom summary is needed."
correction_route: "Re-queue when RC-007 is re-entered or user requests session-start orientation tooling."
owner: unassigned
status: deferred
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-009
source_transcript: raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt
speaker: unknown
timestamp: "00:03:30-00:09:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should offer a regenerable authoring-time orientation map over wiki articles, project artifact paths, and cached Confluence/vendor Markdown so agents compile publishable jr-engineer-executable sets with fewer blind reads—not repo-wide static code graph indexing for v1."
verbatim_excerpt: "everything merges into one graph"
implied_assumption: "Compile-time orientation improves publish closure when paired with align-cite and inline rules at publish."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Track with RC-008 experiment in open-hypotheses.md; approve via implementation backlog or reject via backlog rollback."
affected_components:
  - workspace-query
  - workspace-compile
  - platform-research-review
related_second_brain_principles:
  - junior_engineer_closure
  - inspectable_retrieval
  - citation_grounding
expected_benefit: "Faster compile-time pull of the right standards and sources before publish; See Also remains verification-only."
possible_regression: "Orientation map mistaken for canonical truth or substitute for inlined rules at publish."
validation_method: "Holdout: citation precision and closure lint pass rate vs baseline index-only workflow."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Re-reviewed 2026-05-27 under closure-compile brief. Safer variant supports compile-for-publish; full code-graph form rejected as RC-2026-05-27-009a."
next_action: "Merge experiment with RC-008 session orientation; do not install Graphify by default."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-009a
source_transcript: raw/platform-transcripts/OpenCode_+_Graphify_-_Stop_Wasting_Tokens_in_Opencode_Every_Developer_Use_this.txt
speaker: unknown
timestamp: "00:03:30-00:09:30"
claim_type: architecture_proposal
atomic_claim: "A graph builder that combines static code analysis, local transcription, and model-extracted document concepts should orient v1 Second Brain across mixed code and documentation corpora like an IDE assistant."
verbatim_excerpt: "It reads every class, every function, every import, and every call"
implied_assumption: "Second Brain v1 should index repositories like Graphify/OpenCode."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Reopen only if code-as-source v2 ADR approved."
affected_components:
  - code-as-source-v2
related_second_brain_principles:
  - inspectability
expected_benefit: "None for v1 governance band."
possible_regression: "Duplicates generic IDE codebase assistant scope."
validation_method: "N/A for v1."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -2
  differentiation: -1
  enterprise_fit: 0
  human_review_leverage: 0
total_score: -2
decision: reject
decision_rationale: "As stated: v1 codebase indexing is out of scope per product-brief and AGENTS.md."
next_action: "Reject as stated; see RC-2026-05-27-009 safer variant."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-010
source_transcript: raw/platform-transcripts/Why_2026_Is_the_Year_to_Build_a_Second_Brain_And_Why_You_NEED_One.txt
speaker: unknown
timestamp: "00:09:00-00:21:30"
claim_type: workflow_proposal
atomic_claim: "Reliable second-brain systems need a low-friction capture point, schema-backed routing, an audit trail, confidence guardrails, proactive surfacing, and easy correction."
verbatim_excerpt: "The receipt fixes that... confidence scores... the fix button makes corrections trivial"
implied_assumption: "Trust mechanisms matter more than raw automation capability for long-term adoption."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - platform-research-review
  - workspace-ingest-confluence
  - workspace-lint
  - wiki-log
related_second_brain_principles:
  - inspectability
  - human_review_leverage
  - fail_closed
expected_benefit: "Provides a reusable trust-loop pattern for future workflow automations."
possible_regression: "Adding proactive nudges too early could create noisy workflow automation before core ingestion is stable."
validation_method: "Apply the pattern first to platform research review outputs: audit trail, confidence status, and explicit correction route."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 11
decision: adopt
decision_rationale: "This directly supports Second Brain's governance and trust model without requiring generic automation."
next_action: "Implemented and accepted in PIC-2026-05-27-002."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-011
source_transcript: raw/platform-transcripts/Why_2026_Is_the_Year_to_Build_a_Second_Brain_And_Why_You_NEED_One.txt
speaker: unknown
timestamp: "00:14:30-00:16:00"
claim_type: workflow_proposal
atomic_claim: "Daily and weekly proactive digests can turn a passive knowledge base into an active support loop."
verbatim_excerpt: "The tap on the shoulder... daily slack... weekly summary"
implied_assumption: "Users benefit when the system surfaces relevant next actions instead of requiring manual search."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: unvalidated
correction_route: "Re-enter queue when blocker clears; update claim register decision."
affected_components:
  - workflow-automations-v1x
  - workspace-lint
  - platform-research
related_second_brain_principles:
  - human_review_leverage
  - closure
expected_benefit: "Could improve adoption and follow-through after the core workspace loop works."
possible_regression: "Can become noisy telemetry-like automation or drift into generic productivity assistant behavior."
validation_method: "Defer until v1 has real usage data; then test a local weekly digest from wiki/log.md with no telemetry."
impact_scores:
  governance: 0
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: -1
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 1
decision: defer
decision_rationale: "Potentially useful, but it sits outside v1 governance/closure essentials and risks generic assistant scope creep."
next_action: "Keep as v1.x workflow automation candidate after core pilot."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-012
source_transcript: raw/platform-transcripts/Researcher_at_Stanford_released_a_new_paper_for_an_automated_ai_agent_harmess_ai_tech_fyp.txt
speaker: unknown
timestamp: "00:00:00-00:01:30"
claim_type: evaluation_proposal
atomic_claim: "Second Brain quality should be improved by monitoring harness failures and using failure traces to propose prompt or workflow changes."
verbatim_excerpt: "your model doesn't matter if your harness is broken... failure traces and all the logs"
implied_assumption: "Prompt/workflow quality can be improved systematically from logged failures rather than ad hoc edits."
current_design_status: partially_supported
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-lint
  - platform-research-review
  - docs/platform-decision-records
related_second_brain_principles:
  - inspectability
  - maintainability
  - human_review_leverage
expected_benefit: "Could make prompt improvements evidence-driven."
possible_regression: "Automatic harness mutation would bypass review and could destabilize core rules."
validation_method: "Run an advisory-only prompt-failure review that produces draft ADRs, never direct prompt edits."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 10
decision: experiment
decision_rationale: "Failure-trace review fits Second Brain if it stays advisory and approval-gated."
next_action: "Create an experiment for a quarterly harness-failure review report."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-013
source_transcript: raw/platform-transcripts/Robot_girlfriends_recursive_AI_agents_full_AI_research_Happy_Horse_-_AI_NEWS.txt
speaker: unknown
timestamp: "00:09:30-00:12:30"
claim_type: architecture_proposal
atomic_claim: "Recursive multi-agent systems that communicate in latent space should replace text-based agent review loops for Second Brain."
verbatim_excerpt: "Instead of AI agents talking to each other in text, they collaborate in their own latent space"
implied_assumption: "Latent-space agent loops are available, inspectable, controllable, and better for governed documentation work."
current_design_status: contradicted
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - agent-chain
  - platform-research-review
related_second_brain_principles:
  - inspectability
  - governance
  - human_review_leverage
expected_benefit: "Potential speed and accuracy gains if the research matures."
possible_regression: "Latent collaboration is opaque and conflicts with inspectable retrieval, claim traceability, and human review."
validation_method: "No implementation; monitor only for future explainable/inspectable variants."
impact_scores:
  governance: -2
  closure: 0
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: -1
  differentiation: 0
  enterprise_fit: -1
  human_review_leverage: -1
total_score: -8
decision: reject
decision_rationale: "This directly weakens inspectability, which is a core Second Brain differentiator."
next_action: "Record as rejected as stated; monitor only for inspectable variants."
next_review_after: 2026-08-27
rejection_register: wiki/platform-research/rejected-ideas.md#rc-2026-05-27-013--latent-space-recursive-agent-loops
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-014
source_transcript: raw/platform-transcripts/Robot_girlfriends_recursive_AI_agents_full_AI_research_Happy_Horse_-_AI_NEWS.txt
speaker: unknown
timestamp: "00:21:30-00:24:30"
claim_type: workflow_proposal
atomic_claim: "Research artifacts should preserve claims, experiments, code/config, failed attempts, logs, and evidence rather than only a polished narrative."
verbatim_excerpt: "you get the entire trajectory... every experiment, every failure, every tweak"
implied_assumption: "AI-maintained project knowledge is more useful when failed paths and evidence are preserved for later agents."
current_design_status: partially_supported
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - platform-research-review
  - docs/platform-decision-records
  - reports/platform-research-review
related_second_brain_principles:
  - inspectability
  - grounding
  - human_review_leverage
expected_benefit: "Strengthens the platform research lane by making decision history and failed ideas durable."
possible_regression: "Capturing everything could create report bloat unless summaries and claim records stay structured."
validation_method: "Add lightweight failed-attempt and evidence sections to platform research synthesis reports, then assess reviewer value."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 11
decision: adopt
decision_rationale: "This fits the platform research lane and reinforces traceable product decisions."
next_action: "Implemented and accepted in PIC-2026-05-27-001."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-015
source_transcript: raw/platform-transcripts/GitKB_-_Distributed_Knowledge_Graph_+_Texas_Ready_AI_2-30Min_Talks.txt
speaker: Steve
timestamp: "00:31:30-00:55:30"
claim_type: risk_claim
atomic_claim: "AI systems should maintain intent records, risk-management evidence, and audit trails so future regulatory questions can be answered."
verbatim_excerpt: "making a record that says when we build our system we are intending to do ABC and we are not building it to do bad things XYZ"
implied_assumption: "Even a local documentation compiler benefits from explicit intent and safety records."
current_design_status: partially_supported
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - wiki-log
  - docs/platform-decision-records
  - platform-research-review
related_second_brain_principles:
  - governance
  - auditability
  - no_telemetry
expected_benefit: "Improves enterprise readiness and makes platform evolution auditable."
possible_regression: "Over-legalizing the workflow could slow personal-tool iteration."
validation_method: "Keep intent records lightweight inside ADRs and progress logs; do not add heavy compliance machinery in v1."
impact_scores:
  governance: 2
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 1
total_score: 9
decision: experiment
decision_rationale: "Intent records fit the existing ADR/log pattern, but legal claims need validation before hard requirements."
next_action: "Implemented and accepted in PIC-2026-05-27-004; validate on next 3 platform ADRs (H-005)."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-016
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:18:30-00:19:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should use a three-layer raw/wiki/schema compiler substrate with the agent maintaining the wiki layer from immutable raw inputs."
verbatim_excerpt: "we have the raw folder where basically all the raw files are going to go. We have the wiki folder where the guides and everything else... We have the schema slash the cache file"
implied_assumption: "Filesystem Markdown layers plus a schema file are sufficient for governed knowledge compilation without a hosted database."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Reinforcement only; approve via implementation backlog if canonical doc update desired; reject via backlog rollback."
affected_components:
  - AGENTS
  - docs/architecture-rationale
  - workspace-compile
related_second_brain_principles:
  - filesystem_first
  - inspectability
expected_benefit: "Confirms Karpathy+Cole compiler pattern already in AGENTS.md and architecture rationale."
possible_regression: "None if treated as reinforcement rather than a new substrate change."
validation_method: "No new validation required; covered by existing setup and lint expectations."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "Direct alignment with Second Brain three-layer architecture and closure-compile compiler lens."
next_action: "Cite as reinforcement in batch synthesis; no canonical change required."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-017
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:19:30-00:20:30"
claim_type: architecture_proposal
atomic_claim: "Index- or catalog-first page loading with wikilink graph navigation beats chunk-vector retrieval for compile-time reasoning over structured documentation."
verbatim_excerpt: "Claude reads the index, the catalog picks the pages that are most relevant. Claude loads these pages fully... Claude navigates to pull the related things"
implied_assumption: "Document hierarchy and explicit links preserve inspectable retrieval trails better than embedding similarity alone."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Bundle with RC-001/002; approve via backlog or reject via rollback."
affected_components:
  - workspace-query
  - workspace-compile
  - wiki/index
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "Reinforces page-index retrieval policy before publish and align-cite verification."
possible_regression: "Weak index maintenance could miss cross-cutting content if connections are sparse."
validation_method: "Holdout on long structured sources: compare index-guided section picks vs any future vector baseline."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Matches RC-001/002 and v1 no-embeddings compile-time grounding policy."
next_action: "Reference in synthesis; keep align-cite mandatory at publish."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-018
source_transcript: raw/platform-transcripts/Pinecone_Just_Demoted_Vector_Search._Here_s_the_Knowledge_Layer.txt
speaker: unknown
timestamp: "00:14:30-00:17:00"
claim_type: workflow_proposal
atomic_claim: "Define the agent-data retrieval contract (fields, sources, authority, freshness) before choosing storage or index primitives."
verbatim_excerpt: "write the bundle; pick primitives"
implied_assumption: "Contract-first bundle design prevents database-first retrieval mistakes and keeps compile scoped to governed context."
current_design_status: partially_supported
evidence_supplied_by_speaker: principle
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Accepted PIC-008; reject via backlog rollback. Obsidian hot-cache evidence re-homed to RC-163 experiment (H-2026-05-27-026)."
affected_components:
  - workspace-compile
  - workspace-query
  - workspace-start-project
  - AGENTS
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
  - fail_closed
  - junior_engineer_closure
expected_benefit: "Compile-time pulls the right standards and sources; fewer blind reads; evaluable bundle completeness."
possible_regression: "Checklist overhead on small artifacts; teams may treat it as bureaucracy."
validation_method: "Five project compile sessions with contract checklist vs baseline; measure align-cite pass rate and orientation read count."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 0
  enterprise_fit: 2
  human_review_leverage: 1
total_score: 11
decision: adopt
decision_rationale: "Aligns with closure-compile brief and RC-001/002 page-index policy; makes contract-before-primitives explicit at compile time."
next_action: "Accepted PIC-008; monitor RC-162/165 experiments that depend on RC-018."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-019
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:22:30-00:23:00"
claim_type: evaluation_proposal
atomic_claim: "Scheduled wiki lint for contradictions, stale claims, and orphan pages supports publish closure maintenance beyond one-off workspace-lint runs."
verbatim_excerpt: "every two weeks you tell Claude run a wiki lint, find contradictions or from pages, stale claims, output lint report"
implied_assumption: "Periodic wiki hygiene catches compile drift before published artifacts violate closure or citation rules."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; phase 1 report-only; reject via backlog rollback."
affected_components:
  - workspace-lint
  - wiki/platform-research
related_second_brain_principles:
  - junior_engineer_closure
  - inspectability
  - citation_grounding
expected_benefit: "Proactive closure hygiene aligned with existing lint inventory."
possible_regression: "Auto-fix without approval could mutate wiki unsafely."
validation_method: "Run one manual wiki lint cycle; compare findings to workspace-lint baseline."
impact_scores:
  governance: 2
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 11
decision: experiment
decision_rationale: "Strong compile/closure alignment; must start report-only with user-approved fixes."
next_action: "Prototype wiki-focused lint extension of workspace-lint."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-020
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:22:30-00:23:00"
claim_type: workflow_proposal
atomic_claim: "Dropping updated files into raw/ should trigger targeted recompile of affected wiki pages rather than full-vault rescans."
verbatim_excerpt: "drop the change log MD into the raw file. Tell Claude new file in raw, update the wiki... It reads it, finds the affected wiki page, updates them"
implied_assumption: "Incremental compile keeps wiki aligned with immutable raw sources at lower cost."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md."
affected_components:
  - workspace-compile
  - wiki/log
  - raw/
related_second_brain_principles:
  - filesystem_first
  - maintainability
expected_benefit: "Timely compile-time updates after ingest without stale published references."
possible_regression: "Missed cross-page updates if dependency graph is incomplete."
validation_method: "Pilot raw-drop handler on one Confluence or transcript ingest batch."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 2
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 8
decision: experiment
decision_rationale: "Aligns with ingest-sync compile in AGENTS.md but lacks formal targeted-update workflow."
next_action: "Spec targeted recompile trigger alongside wiki/log.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-021
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:11:00-00:11:30"
claim_type: workflow_proposal
atomic_claim: "An agent-driven wikilink pass during compile improves cross-source discovery before publish while body prose stays link-free at review/published."
verbatim_excerpt: "for each note, find other notes that are systematically related and add Wiki links to them. Start at the most connected topics"
implied_assumption: "Compile-time linking aids grounding; publish closure still requires moving navigation to See Also."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; enforce status-aware body-prose-clean rule."
affected_components:
  - workspace-compile
  - workspace-align-closure
related_second_brain_principles:
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "Better compile-time discovery without weakening published artifact self-sufficiency."
possible_regression: "Over-linking draft artifacts could leak wikilinks into review/published if finalize is skipped."
validation_method: "Compile one raw batch with auto-wikilink pass; verify closure lint passes after finalize."
impact_scores:
  governance: 0
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 6
decision: reject
decision_rationale: "Superseded by RC-148 (PIC-023): topic/entity compile with mandatory ## Sources and raw-backed connections replaces a blind wikilink pass; auto-linking risks closure violations if finalize skipped."
next_action: "Use RC-148 compile phases and topic-entity-compile template; do not add standalone auto-wikilink PIC."
next_review_after: 2026-08-28
rejection_register: wiki/platform-research/rejected-ideas.md
owner: unassigned
status: closed
last_reviewed: 2026-05-28
```

```yaml
claim_id: RC-2026-05-27-022
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:21:30-00:22:00"
claim_type: market_claim
atomic_claim: "Vector databases such as Pinecone become necessary when a personal corpus exceeds roughly one hundred sources or about one million tokens."
verbatim_excerpt: "a hundred sources, max capacity sweet spot beyond that pine cones, the right tool"
implied_assumption: "Index-only filesystem retrieval fails at Karpathy-scale personal archives without hybrid search."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when holdout eval for hybrid retrieval exists; do not adopt without eval."
affected_components:
  - workspace-query
  - docs/architecture-rationale
related_second_brain_principles:
  - inspectable_retrieval
  - vendor_truth
expected_benefit: "Informs future scale planning if validated for enterprise Confluence corpora."
possible_regression: "Premature vector adoption weakens citation inspectability and v1 scope discipline."
validation_method: "Holdout eval on org-scale corpus before changing no-embeddings policy."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 0
decision: monitor
decision_rationale: "Contradicts v1 no-embeddings policy; Karpathy-scale threshold unvalidated for governed enterprise docs."
next_action: "Monitor only; reference RC-001 ADR before any hybrid retriever."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-023
source_transcript: raw/platform-transcripts/Claude_Code_+_Obsidian_-_Build_a_Second_Brain_That_Actually_Learns.txt
speaker: unknown
timestamp: "00:12:30-00:13:30"
claim_type: risk_claim
atomic_claim: "Hot-cache orientation can substitute for align-cite verification and inlined publish rules when agents treat the summary as authoritative."
verbatim_excerpt: "read as a first contact so it makes every future agent query faster... instead of for it going out there into the wild and trying to gather information"
implied_assumption: "Session summaries are sufficient evidence for published vendor and internal claims."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; use RC-018 safer orientation variant only."
affected_components:
  - workspace-align-cite
  - workspace-publish
related_second_brain_principles:
  - citation_grounding
  - junior_engineer_closure
  - fail_closed
expected_benefit: "Faster answers if verification is skipped."
possible_regression: "Bypasses align-cite and inlined rules; published sets become non-executable slop."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: -1
  inspectability: -2
  maintainability: 0
  differentiation: -1
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -13
decision: reject
decision_rationale: "Conflicts with closure rule and align-cite; hot cache must not replace verification at publish."
next_action: "Record in rejected-ideas.md; keep RC-018 as safer variant."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-024
source_transcript: raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt
speaker: Naranzay
timestamp: "00:20:00-00:20:45"
claim_type: workflow_proposal
atomic_claim: "Clearly scoped subtasks with dedicated agent prompts improve artifact output quality in Second Brain stage-gated project workflows."
verbatim_excerpt: "you need to divide things to the tasks and you need to define each task very clearly. If you do this, your output quality increases"
implied_assumption: "Task-scoped prompting transfers from personal productivity demos to governed workspace agent chain handoffs."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Track in open-hypotheses.md; refine workspace agent prompts via backlog."
affected_components:
  - workspace-start-project
  - workspace-vp-agent
  - workspace-pm-agent
  - workspace-architect-agent
  - workspace-engineer-agent
related_second_brain_principles:
  - human_review_leverage
  - junior_engineer_closure
expected_benefit: "Reinforces existing CEO-gated agent chain with sharper per-stage contracts."
possible_regression: "Over-fragmentation could slow handoffs if stage boundaries are unclear."
validation_method: "Pilot prompt refinement on one project stage; measure review iterations before publish."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 8
decision: experiment
decision_rationale: "Only transferable idea under closure-compile lens; applies to project stages not personal dashboards."
next_action: "Reference in workspace agent prompt refinement; no new storage."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-025
source_transcript: raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt
speaker: Naranzay
timestamp: "00:08:00-00:08:30"
claim_type: architecture_proposal
atomic_claim: "Notion with MCP connectors should replace filesystem Markdown as Second Brain primary substrate and canonical store."
verbatim_excerpt: "my notion is the main place main storage where i save the data and in chpt and cloud will have an access about those things"
implied_assumption: "Hosted Notion databases provide better inspectability and governance than raw/wiki Markdown layers."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; keep filesystem-first architecture."
affected_components:
  - AGENTS
  - raw/
  - wiki/
related_second_brain_principles:
  - filesystem_first
  - inspectability
  - source_authority
expected_benefit: "Familiar personal dashboard UX for life-OS use cases."
possible_regression: "Abandons immutable raw layer, approval gates, and governance-band scope."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: -1
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: -1
total_score: -11
decision: reject
decision_rationale: "Contradicts filesystem-first AGENTS.md and product-brief; generic-band Notion alternative."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-026
source_transcript: raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt
speaker: Naranzay
timestamp: "00:04:30-00:05:30"
claim_type: workflow_proposal
atomic_claim: "Multi-LLM cross-critique orchestration should drive Second Brain compile and review loops instead of approval-gated single-agent workflows."
verbatim_excerpt: "i like when the lms are criticizing each other because they are all giving me more insider... three of them needs to communicate somehow about the outputs"
implied_assumption: "Cross-model debate produces better governed documentation than inspectable claim-level review artifacts."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; keep platform-research-review single-lane audit trail."
affected_components:
  - workspace-compile
  - platform-research-review
related_second_brain_principles:
  - inspectability
  - human_review_leverage
  - fail_closed
expected_benefit: "Broader brainstorming for personal life-OS builds."
possible_regression: "No claim-level audit trail; weakens align-cite and human review leverage."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -2
  maintainability: -1
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -13
decision: reject
decision_rationale: "Generic personal-assistant pattern; lacks inspectable governance required for publish closure."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-027
source_transcript: raw/platform-transcripts/How_did_I_build_a_second_brain_with_AI.txt
speaker: Naranzay
timestamp: "00:11:00-00:11:45"
claim_type: product_requirement
atomic_claim: "PARA architecture with a weekly HQ dashboard is a core Second Brain v1 requirement for governed documentation work."
verbatim_excerpt: "PARA architecture, the storage engine... create one weekly HQ page that filters your notion databases to show only today's top three priorities"
implied_assumption: "Personal productivity dashboards equal enterprise documentation compiler requirements."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; out of governance-and-closure band."
affected_components:
  - product-brief
  - PRD
related_second_brain_principles:
  - scope_discipline
expected_benefit: "Visual task management for personal life OS."
possible_regression: "Scope creep into generic productivity assistant territory."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -1
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: -1
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: 0
total_score: -5
decision: reject
decision_rationale: "Generic productivity pattern outside governance-and-closure band per product-brief scope filter."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-029
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Carolina
timestamp: "00:08:30-00:09:30"
claim_type: workflow_proposal
atomic_claim: "A materials-versus-notes capture taxonomy with explicit attribution discipline improves publish-time citation grounding in Second Brain."
verbatim_excerpt: "material is everything that is not mine... notes is everything that i created... i cannot use without giving credit to the person"
implied_assumption: "Separating external materials from owned notes maps cleanly to authority and domain tags at compile time."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; pilot on raw/ ingest metadata."
affected_components:
  - raw/
  - workspace-compile
  - workspace-align-cite
related_second_brain_principles:
  - source_authority
  - citation_grounding
expected_benefit: "Clearer compile input for align-cite and vendor vs internal separation."
possible_regression: "Taxonomy overhead if not automated during ingest."
validation_method: "Pilot materials/notes tags on one platform-transcript and Confluence ingest path."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 1
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: experiment
decision_rationale: "Bridges capture to compile with citation discipline; not yet formalized in raw/ schema."
next_action: "Experiment capture taxonomy on ingest paths."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-030
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Carolina
timestamp: "00:09:30-00:10:45"
claim_type: workflow_proposal
atomic_claim: "Project or focus metadata on captured sources enables compile-time assembly of relevant standards and raw pages for a given artifact."
verbatim_excerpt: "filter by several things... edit the property and i'll come here to focus i'm going to go to my workshop"
implied_assumption: "Scoped metadata reduces blind vault reads during project documentation compile."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; merge with RC-009 orientation-map experiment."
affected_components:
  - config/second-brain.yml
  - workspace-compile
  - workspace-query
related_second_brain_principles:
  - scoped_retrieval
  - inspectable_retrieval
expected_benefit: "Compile-time pull of in-scope standards before publish."
possible_regression: "Incorrect focus tags could omit required standards from compile context."
validation_method: "Pilot focus metadata on one workspace project compile."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Safer RC-009 variant scoped to project compile not repo-wide graph indexing."
next_action: "Merge with RC-009 in open-hypotheses.md; pilot project scoping."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-031
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Eduardo
timestamp: "00:11:30-00:12:30"
claim_type: architecture_proposal
atomic_claim: "A disposable manuscript map or canvas can orient authoring without becoming canonical knowledge or replacing publish closure checks."
verbatim_excerpt: "create a a new map... manuscript this will allow me to bring in the right files... using this as my main ground for this project"
implied_assumption: "Authoring orientation artifacts are regenerable and non-authoritative at publish time."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; merge with RC-009; reject if promoted to canonical wiki."
affected_components:
  - workspace-projects
  - workspace-compile
related_second_brain_principles:
  - junior_engineer_closure
  - inspectable_retrieval
expected_benefit: "Faster draft assembly; See Also remains verification-only at publish."
possible_regression: "Manuscript map mistaken for published artifact or citation source."
validation_method: "One project draft with disposable map; verify align-closure passes after finalize."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Matches closure-compile disposable orientation pattern; not canonical."
next_action: "Merge with RC-009 orientation-map experiment."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-032
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Ethan
timestamp: "00:28:00-00:28:45"
claim_type: principle_claim
atomic_claim: "Expert or primary-source validation should precede treating domain research as compile input for published artifacts."
verbatim_excerpt: "consulting calls... way better than the AI... have like AI fact check it... I wouldn't rely on AI a hundred percent of the time"
implied_assumption: "Perplexity or Grok captures remain product intelligence until validated against primary sources."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Reinforcement for vendor-truth workflow; approve canonical touch via backlog only."
affected_components:
  - workspace-align-vendor-truth
  - workspace-ingest-vendor-doc
  - workspace-align-cite
related_second_brain_principles:
  - vendor_truth
  - citation_grounding
  - fail_closed
expected_benefit: "Strengthens existing vendor-truth and align-cite gates at publish."
possible_regression: "None if treated as policy reinforcement not new automation."
validation_method: "No new validation; enforce requires_external_validation on unvalidated captures."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 2
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 1
total_score: 12
decision: adopt
decision_rationale: "Reinforces vendor-truth and fail-closed policy before compile promotes research to published artifacts."
next_action: "Cite in synthesis; optional doc reinforcement via approved backlog."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-033
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Ethan
timestamp: "00:07:00-00:07:15"
claim_type: architecture_proposal
atomic_claim: "Google Docs or Notion should be the primary capture store instead of immutable raw/ Markdown mirrors in Second Brain."
verbatim_excerpt: "create a google doc and i'm just gonna paste it... call this my pokemon vending machine gtm"
implied_assumption: "Siloed SaaS capture is equivalent to filesystem-first immutable raw ingestion."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; ingest via raw/ mirrors with approval gates."
affected_components:
  - raw/
  - workspace-ingest-confluence
related_second_brain_principles:
  - filesystem_first
  - source_authority
expected_benefit: "Fast ad hoc capture for personal projects."
possible_regression: "Bypasses immutable raw layer, scoped compile, and citation traceability."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -1
  enterprise_fit: -1
  human_review_leverage: -1
total_score: -9
decision: reject
decision_rationale: "Contradicts filesystem-first immutable raw/ architecture."
next_action: "Record in rejected-ideas.md; route captures through raw/ ingest."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-034
source_transcript: raw/platform-transcripts/Analog_vs._AI_-_Which_is_better_for_your_Second_Brain.txt
speaker: Carolina
timestamp: "00:22:00-00:22:30"
claim_type: workflow_proposal
atomic_claim: "Published artifacts should accept wholesale AI-generated outlines and modules without human distill and inlined execution rules."
verbatim_excerpt: "suggesting me to have module one and two and then a lab... no no no no that's not I was thinking... I want to do it myself"
implied_assumption: "AI-generated workshop structure is sufficient for jr-engineer-executable published sets."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; require human distill and inline rules at publish."
affected_components:
  - workspace-publish
  - workspace-align-closure
  - docs/style
related_second_brain_principles:
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Faster first drafts for personal content."
possible_regression: "Published artifacts become non-executable slop without inlined standards."
validation_method: "N/A; rejected as stated; speaker rejects pattern in transcript."
impact_scores:
  governance: -1
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -10
decision: reject
decision_rationale: "Conflicts with jr-engineer closure and authenticity; speaker explicitly rejects wholesale AI modules."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-035
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:02:00-00:03:30"
claim_type: architecture_proposal
atomic_claim: "Karpathy raw/wiki/outputs plus schema file without Obsidian matches Second Brain's governed compiler model."
verbatim_excerpt: "three folders and one file on your computer... raw... wiki... outputs... Claude MD at the top"
implied_assumption: "Filesystem compiler pattern does not require Obsidian or vector stores."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Reinforcement only; approve via backlog if doc update desired."
affected_components:
  - AGENTS
  - docs/architecture-rationale
related_second_brain_principles:
  - filesystem_first
expected_benefit: "Validates architecture for adopters without Obsidian dependency."
possible_regression: "None as reinforcement."
validation_method: "No new validation required."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "Direct architecture rationale section 1 alignment."
next_action: "Cite in batch synthesis."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-036
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:20:30-00:22:30"
claim_type: workflow_proposal
atomic_claim: "An outputs/ folder for query artifacts should feed back into the compile loop parallel to workspace-qa filing."
verbatim_excerpt: "every time you ask the agent, a question you like the answer to, you can then save that back"
implied_assumption: "Saved Q&A outputs compound knowledge when routed through compile not direct wiki mutation."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; must remain approval-gated."
affected_components:
  - workspace-qa
  - workspace-compile
related_second_brain_principles:
  - grounding
  - human_review_leverage
expected_benefit: "Compounding answers into curated wiki with review gates."
possible_regression: "Direct save without review pollutes canonical wiki."
validation_method: "Pilot outputs to qa to compile path on platform research lane."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Useful if routed through workspace-qa and compile, not auto-wiki."
next_action: "Design gated outputs feedback loop."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-037
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:24:00-00:28:00"
claim_type: evaluation_proposal
atomic_claim: "Monthly health check auditing contradictions, orphaned refs, unsourced claims, and stale wiki articles extends publish closure maintenance."
verbatim_excerpt: "flag contradictions... broken backlinks... claims not backed by a source... stale articles, anything that's out of date, older than 90 days"
implied_assumption: "Scheduled lint cadence catches compile drift before publish violations."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; phase 1 report-only."
affected_components:
  - workspace-lint
  - platform-research-review
related_second_brain_principles:
  - junior_engineer_closure
  - inspectability
expected_benefit: "Proactive closure hygiene aligned with vendor TTL thinking."
possible_regression: "Auto-fix without approval could mutate wiki unsafely."
validation_method: "Run one manual health check; measure findings vs workspace-lint."
impact_scores:
  governance: 2
  closure: 2
  grounding: 1
  vendor_truth: 1
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 12
decision: experiment
decision_rationale: "Strong compile/closure alignment; must start report-only with user action phase."
next_action: "Prototype monthly wiki health check skill."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-038
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:09:30-00:10:30"
claim_type: architecture_proposal
atomic_claim: "An ingested registry or changelog should track last-processed raw files for incremental compile."
verbatim_excerpt: "memory file that simply lists when... the last action was taken... what is new in the raw files"
implied_assumption: "Incremental compile reduces cost and missed updates vs full vault scan."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR."
affected_components:
  - workspace-compile
  - wiki/log
related_second_brain_principles:
  - filesystem_first
  - maintainability
expected_benefit: "Efficient compile-time processing for publish pipeline."
possible_regression: "Registry drift if not append-only and audited."
validation_method: "Pilot ingested registry on one Confluence ingest batch."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 2
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 8
decision: experiment
decision_rationale: "Compile efficiency supports timely publish grounding."
next_action: "Spec ingested registry alongside wiki/log.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-039
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:03:00-00:03:30"
claim_type: architecture_proposal
atomic_claim: "Moderate corpora on the order of 100 articles or 400k words do not require vector RAG when index-guided retrieval is used."
verbatim_excerpt: "around 100 articles and 400,000 words, and the LLM handles it fine maintaining an index"
implied_assumption: "Index navigation scales to personal/small-team doc sets without embeddings."
current_design_status: already_supported
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: validated_against_design
correction_route: "Bundle with RC-001; reject via backlog rollback."
affected_components:
  - workspace-query
  - docs/architecture-rationale
related_second_brain_principles:
  - inspectable_retrieval
expected_benefit: "Reinforces v1 no-embeddings policy for moderate scope."
possible_regression: "May not transfer to 10k+ page Confluence without eval."
validation_method: "Holdout eval at org-scale before changing policy."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: adopt
decision_rationale: "Reinforces RC-001 and architecture rationale defer-embeddings."
next_action: "Note enterprise-scale caveat in synthesis."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-040
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:20:30-00:21:00"
claim_type: workflow_proposal
atomic_claim: "Liked Q&A answers should auto-save back to wiki or raw without human review for self-improvement."
verbatim_excerpt: "save that back into raw or into the wiki. And the system gets smarter the more you use it"
implied_assumption: "Unreviewed feedback loops safely improve canonical knowledge."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; use RC-036 gated variant."
affected_components:
  - workspace-wiki
  - platform-research
related_second_brain_principles:
  - governance
  - source_authority
expected_benefit: "Faster compounding."
possible_regression: "Bypasses approval gates (RP-2026-05-27-001)."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -9
decision: reject
decision_rationale: "Matches rejected self-learning auto-update pattern."
next_action: "Record in rejected-ideas.md; safer variant RC-036."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-041
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:24:30-00:25:30"
claim_type: workflow_proposal
atomic_claim: "Health check should auto-fill wiki gaps via web search without user approval gates."
verbatim_excerpt: "find missing data, and fill the gaps with web search"
implied_assumption: "Automated web fill is safe for governed documentation."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review 2026-08-27; use report-only health check."
affected_components:
  - workspace-ingest-vendor-doc
  - workspace-lint
related_second_brain_principles:
  - vendor_truth
  - fail_closed
expected_benefit: "Faster gap closure."
possible_regression: "Unvalidated vendor claims enter wiki; bypasses fetch-on-demand TTL."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: -2
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: -1
  human_review_leverage: -1
total_score: -10
decision: reject
decision_rationale: "Violates vendor-truth and fail-closed policy."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-042
source_transcript: raw/platform-transcripts/Build_A_Claude_Knowledge_Base_That_Self-Improves.txt
speaker: unknown
timestamp: "00:17:30-00:18:30"
claim_type: workflow_proposal
atomic_claim: "Anti-AI writing style rules applied during wiki compile improve published artifact prose quality and closure readability."
verbatim_excerpt: "make sure that it's read your anti-AI writing style guide... Wikipedia anti-AI writing style"
implied_assumption: "Compile-time style enforcement reduces publish rework."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR."
affected_components:
  - workspace-compile
  - docs/style
related_second_brain_principles:
  - junior_engineer_closure
expected_benefit: "Cleaner published prose; less finalize rework."
possible_regression: "Over-rigid style rules may block necessary technical precision."
validation_method: "Apply writing rules to one project finalize; measure review iterations."
impact_scores:
  governance: 0
  closure: 2
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Supports body-prose-clean and exemplar quality bar at compile."
next_action: "Pilot writing-rules.md in workspace-compile prompt."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-066
source_transcript: raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt
speaker: unknown
timestamp: "00:07:30-00:09:00"
claim_type: architecture_proposal
atomic_claim: "Three layers: always-on rules (shims/AGENTS), specialist agents (chain), on-demand skills/prompts (workflows)."
verbatim_excerpt: "custom instructions are always loaded... custom agents are on -demand specialists with their own context window and tool permissions... skills are on -demand workflows with step -by -step recipes"
implied_assumption: "Governance schema, stage agents, and verb prompts compose without one layer replacing another."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS
  - .github/prompts
  - .github/skills
related_second_brain_principles:
  - filesystem_first
  - fail_closed
expected_benefit: "Reinforces lane-labeled governance: schema always on, specialists on demand, recipes pulled in for verbs."
possible_regression: "None if treated as reinforcement rather than Copilot product pivot."
validation_method: "No new validation required; maps to existing AGENTS.md agent chain and prompt/skill layout."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Direct alignment with Second Brain's instructions/agents/skills separation under different names."
next_action: "Reinforcement only; optional platform-intelligence cite."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-067
source_transcript: raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt
speaker: unknown
timestamp: "00:01:30-00:02:00"
claim_type: workflow_proposal
atomic_claim: "Path-scoped instructions apply only when editing matching wiki/raw/project paths during compile."
verbatim_excerpt: "path specific instructions... apply to lines at the top that say only apply me when working in these files"
implied_assumption: "Directory-scoped compile hints reduce context bloat without forking canonical standards."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-compile
  - config/second-brain.yml
related_second_brain_principles:
  - scoped_retrieval
  - maintainability
expected_benefit: "Targeted compile/query orientation per project path without loading global instructions."
possible_regression: "Path rules could fork team standards per folder if not tied to authority tags."
validation_method: "Prototype path-scoped compile hints for wiki/workspace-projects/{slug}/ only."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "config/second-brain.yml scoping exists; path-specific instruction files are not implemented."
next_action: "Prototype path-scoped compile hints tied to project paths."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-068
source_transcript: raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt
speaker: unknown
timestamp: "00:05:30-00:07:30"
claim_type: workflow_proposal
atomic_claim: "Multi-step repeatable workflows belong in skills/prompts, not always-loaded global instructions."
verbatim_excerpt: "skills only show up when you need them... you wouldn't want a five -step pr workflow loaded into every conference conversation that's just wasted context"
implied_assumption: "On-demand operation prompts prevent context bloat while preserving explicit multi-step publish/align flows."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - .github/prompts
  - .github/skills
  - AGENTS
related_second_brain_principles:
  - inspectability
  - maintainability
expected_benefit: "Prevents context bloat and keeps multi-step publish/align flows in explicit prompts/skills."
possible_regression: "Over-fragmenting workflows into skills could obscure discoverability without index guidance."
validation_method: "Audit workspace-* and platform-* prompts for always-on vs on-demand separation."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 2
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 9
decision: adopt
decision_rationale: "Operation-specific prompts vs canonical AGENTS.md already supported."
next_action: "Reinforcement only."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-069
source_transcript: raw/platform-transcripts/Custom_Instructions_vs_Custom_Agents_vs_Agent_Skills_Explained.txt
speaker: unknown
timestamp: "00:03:30-00:04:30"
claim_type: risk_claim
atomic_claim: "Specialist agents should declare tool/scope restrictions (read-only reviewer vs full editor)."
verbatim_excerpt: "docs writer it can only read files edit files and use glob... it doesn't have terminal access... keeps the agent focused and... safer"
implied_assumption: "Explicit permission boundaries strengthen fail-closed platform and workspace review lanes."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - platform-transcript-librarian
  - platform-research-review
  - .github/agents
related_second_brain_principles:
  - fail_closed
  - human_review_leverage
expected_benefit: "Tool/scope restrictions strengthen fail-closed platform and workspace review lanes."
possible_regression: "Over-restricting agents could block legitimate compile operations without clear escalation."
validation_method: "Document explicit read-only vs editor scopes in platform reviewer agent definitions."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: adopt
decision_rationale: "Approval-gated mutations and librarian checkpoints exist; explicit tool deny lists can be strengthened."
next_action: "Strengthen scope text in platform reviewer prompts."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-070
source_transcript: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
speaker: unknown
timestamp: "00:07:00-00:07:30"
claim_type: architecture_proposal
atomic_claim: "Out-of-loop automation requires programmatic agent/harness APIs, not terminal-only babysitting."
verbatim_excerpt: "your agents must have programmatic support this is how you move into Outloop agent decoding... so that you don't have to sit behind the terminal 24 7 and babysit your agent"
implied_assumption: "Second Brain align/lint and compile hooks may eventually need programmatic invocation outside interactive sessions."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - scripts
  - workspace-lint
  - workspace-align-cite
related_second_brain_principles:
  - inspectability
  - fail_closed
expected_benefit: "Enables CI-driven align/lint without terminal babysitting while preserving approval gates."
possible_regression: "Autonomous programmatic mutation could bypass human checkpoints if not scoped to read-only checks."
validation_method: "Scoped programmatic align/lint invocation via scripts/ + CI without autonomous wiki mutation."
impact_scores:
  governance: 1
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 6
decision: experiment
decision_rationale: "AGENTS.md approval-gated operations exist; no shipped programmatic SDK for out-of-loop doc workflows."
next_action: "Defer until concrete no-terminal align/lint workflow is scoped."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-071
source_transcript: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
speaker: unknown
timestamp: "00:03:00-00:05:00"
claim_type: workflow_proposal
atomic_claim: "Specialized roles with isolated context and handoffs improve complex doc work (maps to agent chain)."
verbatim_excerpt: "each agent gets its own role description its own set of allowed tools and it runs in its own context window it's like handing off a task to a colleague"
implied_assumption: "Stage-gated specialists with inspectable markdown handoffs outperform monolithic agent sessions for documentation work."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-projects
  - .github/prompts
related_second_brain_principles:
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Stage-gated specialists with isolated context match workspace agent chain and CEO checkpoints."
possible_regression: "None if treated as reinforcement of existing chain."
validation_method: "Compare multi-stage project artifact quality against single-agent baseline on pilot project."
impact_scores:
  governance: 1
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "CEO→VP→PM→Architect→Engineer chain with stage artifacts already supported."
next_action: "Reinforcement only."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-072
source_transcript: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
speaker: unknown
timestamp: "00:08:00-00:19:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should adopt Pi-style fully customizable coding harness as its core runtime."
verbatim_excerpt: "there are many coding agents but this one is mine... fully customizable, open source, it's yours"
implied_assumption: "A forkable terminal harness should replace the governed documentation compiler substrate."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - product-brief
  - AGENTS
related_second_brain_principles:
  - filesystem_first
  - differentiation
expected_benefit: "Maximum agent harness customization for coding tasks."
possible_regression: "Reframes Second Brain as customizable coding terminal product — scope creep into Cody/Copilot territory."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: 0
  maintainability: -1
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: 0
total_score: -7
decision: reject
decision_rationale: "Second Brain is a governed doc compiler, not a coding-agent IDE."
next_action: "Record in rejected-ideas.md; keep Cursor/Claude as authoring tools."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-073
source_transcript: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
speaker: unknown
timestamp: "00:25:30-00:26:00"
claim_type: risk_claim
atomic_claim: "Default YOLO/full-permission agent mode is appropriate for governed documentation work."
verbatim_excerpt: "Pi runs in YOLO mode out of the box... there's no real mode in Pi. It's just YOLO mode. It's just do whatever you want"
implied_assumption: "Permissionless automation accelerates documentation work without safety tradeoffs."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - AGENTS
  - platform-research
related_second_brain_principles:
  - fail_closed
  - governance
expected_benefit: "Faster agent execution without permission prompts."
possible_regression: "YOLO defaults undermine approval-gated ingest/publish and fail-closed research safety."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -9
decision: reject
decision_rationale: "Contradicts fail-closed, explicit allowlists, and approval gates in AGENTS.md."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-074
source_transcript: raw/platform-transcripts/The_Pi_Coding_Agent_-_The_ONLY_REAL_Claude_Code_COMPETITOR.txt
speaker: unknown
timestamp: "00:39:00-00:39:30"
claim_type: market_claim
atomic_claim: "Open-source forkable harness (Pi) hedges vendor lock-in for coding agents; Pi powers OpenClaw lineage."
verbatim_excerpt: "this is the agent decoding tool that powers open claw previously malt bot previously clawed bot"
implied_assumption: "Second Brain should track Pi/OpenClaw as potential platform substrate or dependency."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when external validation is available; do not promote without validation."
affected_components:
  - product-brief
related_second_brain_principles:
  - differentiation
expected_benefit: "Vendor hedge awareness for portable skill patterns."
possible_regression: "Premature platform pivot toward agentic coding harness market noise."
validation_method: "Validate Pi↔OpenClaw lineage and enterprise fit against primary sources."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 1
decision: monitor
decision_rationale: "External product claim unvalidated; monitor for portable skill patterns only."
next_action: "Monitor Pi/OpenClaw; no platform substrate experiments in v1."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-075
source_transcript: raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt
speaker: unknown
timestamp: "00:06:00-00:07:30"
claim_type: workflow_proposal
atomic_claim: "Master repeatable skills/SOPs before always-on autonomous agent stacks."
verbatim_excerpt: "what you really need are good skills... repeatable SOPs that you can switch between all of the different models that are your employees"
implied_assumption: "Skills-first design with human gates should precede autonomous always-on agents."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - .github/skills
  - platform-transcript-librarian
related_second_brain_principles:
  - fail_closed
  - human_review_leverage
expected_benefit: "Skills-first + human gates before autonomy matches fail-closed platform research safety."
possible_regression: "None if treated as reinforcement."
validation_method: "Audit platform skills and librarian checkpoints against skills-before-autonomy pattern."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Approval-gated verbs, librarian checkpoints, and skills in .github/skills/ already supported."
next_action: "Reinforcement only; optional onboarding doc via approved ADR."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-076
source_transcript: raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt
speaker: unknown
timestamp: "00:04:30-00:05:30"
claim_type: principle_claim
atomic_claim: "Start with one concrete workflow bottleneck, not influencer automation bundles."
verbatim_excerpt: "just focusing on one problem or one bottleneck inside of your workflow what is something that you hate doing"
implied_assumption: "Governance-band scope discipline requires solving one concrete pain point before generic automation."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - product-brief
  - docs/roadmap
related_second_brain_principles:
  - differentiation
  - governance
expected_benefit: "One-bottleneck focus prevents generic assistant scope creep."
possible_regression: "None if treated as scope guidance reinforcement."
validation_method: "Apply scope filter from product-brief capability table to new feature requests."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "Aligns with v1 governance band and deferred digest/automation scope."
next_action: "Reinforcement only."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-077
source_transcript: raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt
speaker: unknown
timestamp: "00:00:00-00:02:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should be built on OpenClaw/Hermes always-on personal agents."
verbatim_excerpt: "OpenClaw and Hermes are not suitable for beginners... do you really trust an agent to use your computer"
implied_assumption: "Always-on personal agents with full-device access should replace filesystem Markdown compiler."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - product-brief
  - AGENTS
related_second_brain_principles:
  - filesystem_first
  - fail_closed
expected_benefit: "Always-on automation for personal productivity."
possible_regression: "Always-on personal agents bypass citation, authority tags, and immutability of raw/."
validation_method: "N/A; rejected as stated."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: 0
total_score: -8
decision: reject
decision_rationale: "Second Brain is filesystem Markdown compiler, not VPS babysitter."
next_action: "Record in rejected-ideas.md; no OpenClaw integration in v1."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-078
source_transcript: raw/platform-transcripts/Why_OpenClaw_and_Hermes_are_distractions_do_this_instead_to_become_AI_fluent.txt
speaker: unknown
timestamp: "00:07:00-00:07:30"
claim_type: workflow_proposal
atomic_claim: "Portable skills/prompts let the same SOP run across models/tools without retraining the org stack."
verbatim_excerpt: "a skill that you have inside a simpler system can then be ported over to OpenCloud or Herbie and that's when you can start automating everything"
implied_assumption: "Markdown prompts and skills are the portable unit; canonical knowledge stays in wiki/."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - .github/skills
  - .github/prompts
  - AGENTS
related_second_brain_principles:
  - filesystem_first
  - maintainability
expected_benefit: "Portable SOPs across tools align with Markdown prompts/skills, not vendor lock-in."
possible_regression: "Porting skills without wiki grounding could duplicate canonical knowledge."
validation_method: "Verify platform skills run unchanged across Cursor and Copilot shims."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: adopt
decision_rationale: "Prompt files + skills + AGENTS.md schema already support portable SOPs."
next_action: "Reinforcement only."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-079
source_transcript: raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt
speaker: unknown
timestamp: "00:01:00-00:02:00"
claim_type: workflow_proposal
atomic_claim: "Link review/decision context to artifact revisions in-repo (log + stage dirs) for publish traceability."
verbatim_excerpt: "discussions around changes still live outside the git history... we can't get the discussion around every change to be tracked with the code"
implied_assumption: "Publish-time closure requires traceable rationale beside artifact history, not Slack-only threads."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - wiki/log.md
  - workspace-projects
  - reports
related_second_brain_principles:
  - inspectability
  - human_review_leverage
expected_benefit: "Improves inspectability and human review leverage for publish/align without Slack-only rationale."
possible_regression: "Unstructured log append could add noise without improving closure if format is undefined."
validation_method: "Template decision snippet append format for publish/align events; one pilot cycle."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 8
decision: experiment
decision_rationale: "wiki/log.md append-only audit exists; PR/Slack discussion split is problem evidence."
next_action: "Prototype structured decision append on publish/align."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-080
source_transcript: raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt
speaker: unknown
timestamp: "00:05:30-00:07:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain collaboration should abandon GitHub PR branches for email/patch-only kernel workflow."
verbatim_excerpt: "the traditional way to do this is to create an entity that just contains the changes this is called a patch"
implied_assumption: "Kernel-style patch workflow improves documentation collaboration over GitHub PR branches."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-publish
related_second_brain_principles:
  - junior_engineer_closure
  - enterprise_fit
expected_benefit: "Distributed git-native collaboration without GitHub dependency."
possible_regression: "Patch/mail-list workflow fights jr-engineer closure and existing GitHub-based team habits."
validation_method: "N/A; rejected as stated for v1."
impact_scores:
  governance: 0
  closure: -2
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: 0
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -6
decision: reject
decision_rationale: "Second Brain artifacts are Markdown in git; patch workflow adds friction without closure gain."
next_action: "Record in rejected-ideas.md; keep GitHub/git; store decision records under reports/ + wiki/log.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-081
source_transcript: raw/platform-transcripts/You_ve_Been_Using_Git_Wrong.txt
speaker: unknown
timestamp: "00:10:00-00:11:30"
claim_type: principle_claim
atomic_claim: "GitHub centralizes code while distributing merge ownership; relevant for future multi-user vault, not v1."
verbatim_excerpt: "git workflow gives you a distributed code base that revolves around a central set of owners while using the github workflow gives you a centralized code base but with distributed ownership"
implied_assumption: "Team-scale collaboration model choice matters when Second Brain moves beyond single-user local constraint."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when external validation is available; do not promote without validation."
affected_components:
  - multi-user-v2
  - docs/roadmap
related_second_brain_principles:
  - enterprise_fit
expected_benefit: "Informs future multi-user vault rollout and merge policy design."
possible_regression: "Premature team-collaboration design could expand v1 scope."
validation_method: "Revisit with RC-005 when multi-user scope opens; compare GitHub vs git-native ownership."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 0
  enterprise_fit: 2
  human_review_leverage: 0
total_score: 3
decision: monitor
decision_rationale: "v1 single-user local constraint; defer team-scale sync to v2."
next_action: "Revisit with RC-005 when multi-user scope opens."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-082
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:05:30-00:10:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should treat AGENTS.md (and agent shims) as the top-level navigation map agents read each session before routing into wiki/raw/project paths."
verbatim_excerpt: "this cloud .md file is basically the instruction layer or the map for your AI agent on cloud code or co-work on how to navigate the second brain folder"
implied_assumption: "A single root instruction file is sufficient for orientation when paired with index.md."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - workspace-query
  - .cursor/rules
related_second_brain_principles:
  - inspectable_retrieval
  - filesystem_first
expected_benefit: "Reinforces session-start routing for compile-time grounding without new infrastructure."
possible_regression: "Root map bloat increases token cost if not kept scoped."
validation_method: "Compare agent orientation steps with and without explicit AGENTS.md read in pilot sessions."
impact_scores:
  governance: 1
  closure: 0
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 7
decision: adopt
decision_rationale: "Already canonical; transcript validates closure-compile authoring-time orientation pattern."
next_action: "No code change; reference in platform onboarding docs when user approves."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-083
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:10:00-00:10:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should add scoped nested instruction files (Karpathy-style) for major wiki subtrees to improve agent routing efficiency without expanding the root AGENTS.md."
verbatim_excerpt: "separate CloudMD documents for each of the subfolders to basically instruct Cloud also how these subfolders are structured, which is a technique and best practice Andrej Karpathy came up with"
implied_assumption: "Subtree-specific routing reduces mis-reads and token waste on large vaults."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - wiki/workspace-projects
  - workspace-compile
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Better compile-time scoping on large repos; lower full-vault reads."
possible_regression: "Instruction drift across nested files if not linted."
validation_method: "Pilot nested ROUTING.md under one active project; measure mis-routed reads in a 5-task holdout."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 5
decision: experiment
decision_rationale: "Plausible compile-time gain; not yet specified in AGENTS.md beyond stage folders."
next_action: "Add H-2026-05-27-011; draft scoped routing template after user approval."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-084
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:14:30-00:16:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should run a scheduled OS operator that ingests Slack/meetings and autonomously updates or deletes strategy and context files in the wiki."
verbatim_excerpt: "it might delete even files that became irrelevant because of the updates you can imagine if we discussed a strategic change in our business that it can actually start adapting the strategy document"
implied_assumption: "Real-time connector ingest is safe without per-change human approval."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-compile
  - wiki/workspace-standards
related_second_brain_principles:
  - source_authority
  - human_review_leverage
expected_benefit: "Fresher organizational context for agents."
possible_regression: "Unapproved mutation of standards and strategy; breaks immutable raw and publish closure."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -8
decision: reject
decision_rationale: "Conflicts with approval-gated mutations and rejected autonomous wiki mutation patterns (RC-059, RP-001)."
next_action: "Record in rejected-ideas.md; safer variant is quarantine + human-reviewed compile only."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-085
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:19:30-00:22:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should run weekly autonomous optimizer passes that merge duplicates, delete stale files, and reorganize folder structure without explicit user approval."
verbatim_excerpt: "spots duplicates for example in your second brain and merges them it also detects stale context flags files that are unreachable and resolves conflicting information in the brain"
implied_assumption: "Automated hygiene improves publish closure without risking canonical drift."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - wiki
  - workspace-lint
related_second_brain_principles:
  - governance
  - human_review_leverage
expected_benefit: "Lower token use and cleaner vault."
possible_regression: "Silent deletion/reorg of published references; audit trail loss."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -8
decision: reject
decision_rationale: "Report-only lint (RC-019) is the safer variant; autonomous merge/delete bypasses CEO approval."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-086
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:27:30-00:30:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain v1 requires an MCP-exposed remote vault (e.g., Railway) so cloud routines can update the brain when the laptop is closed."
verbatim_excerpt: "build an mcp out of your second brain... these routines are run on the cloud we can't actually give them access to local folders on our computer"
implied_assumption: "Unattended cloud mutation is necessary for a complete second brain."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-enter queue when blocker clears; update claim register decision."
affected_components:
  - platform-infrastructure
  - ingest-automation
related_second_brain_principles:
  - filesystem_first
expected_benefit: "24/7 ingest and hygiene for distributed teams."
possible_regression: "Adds hosted dependency and weakens local inspectability."
validation_method: "Revisit with multi-user v2; compare CI ingest vs MCP remote vault."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 0
decision: defer
decision_rationale: "Infrastructure-heavy; v1 solo-user local constraint does not require cloud MCP vault."
next_action: "Bundle with RC-005 multi-user deferral."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-087
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:24:00-00:24:30"
claim_type: principle_claim
atomic_claim: "Second Brain should prefer local filesystem vault access over Notion/Google Drive MCP for agent retrieval accuracy, speed, and token efficiency."
verbatim_excerpt: "mcps basically add a complexity layer... it comes at a cost of accuracy of context or retrieval it comes at a cost of speed mcps take longer than folder access"
implied_assumption: "Enterprise documentation can stay git-backed Markdown."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - raw
  - workspace-ingest-confluence
related_second_brain_principles:
  - filesystem_first
  - inspectability
expected_benefit: "Confirms v1 substrate choice vs generic Notion-band tools."
possible_regression: "None if treated as reinforcement."
validation_method: "No new validation; aligns with product-brief scope filter."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 8
decision: adopt
decision_rationale: "Matches filesystem-first architecture and prior RC-025 rejection of Notion-primary."
next_action: "Document as reinforcement in platform intelligence brief when user approves."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-088
source_transcript: raw/platform-transcripts/5_Skills_to_Build_an_AI_Operating_System_Like_The_1%_Full_Guide.txt
speaker: Ben
timestamp: "00:22:30-00:27:00"
claim_type: product_requirement
atomic_claim: "Second Brain v1 must ship real-time team vault sync with per-folder read/write permissions (Relay-style) for shared organizational context."
verbatim_excerpt: "we do want to have those permission and control settings... relay allows you to real-time sync context in multiple folders automatically"
implied_assumption: "Team alignment requires live bidirectional vault sync in v1."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-enter queue when blocker clears; update claim register decision."
affected_components:
  - multi-user-v2
  - wiki
related_second_brain_principles:
  - enterprise_fit
expected_benefit: "Shared business context across team agents."
possible_regression: "Premature complexity and permission bugs on canonical standards."
validation_method: "Revisit with RC-005; evaluate git-based collaboration vs Obsidian Relay."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: -1
  differentiation: 0
  enterprise_fit: 2
  human_review_leverage: 0
total_score: 1
decision: defer
decision_rationale: "v1 single-user local constraint; team sync is v2 with explicit merge policy."
next_action: "Link to RC-005 and RC-081 monitor items."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-089
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:06:30-00:07:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain's compile step (raw sources reordered into wiki projections) creates governed knowledge products that could not exist in traditional code-only pipelines."
verbatim_excerpt: "you can just take these documents and basically recompile them in a different way and reorder them and create something that is new and interesting as a reframing of the data"
implied_assumption: "LLM synthesis is valuable when bounded by source authority and citations."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-compile
  - wiki
related_second_brain_principles:
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "External validation of core product thesis."
possible_regression: "None as reinforcement."
validation_method: "Reference in architecture-rationale user-approved update."
impact_scores:
  governance: 1
  closure: 2
  grounding: 2
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 10
decision: adopt
decision_rationale: "Core compiler analogy; directly supports governance-and-closure band."
next_action: "Cite in platform decision narrative; no structural change required."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-090
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:09:30-00:11:00"
claim_type: principle_claim
atomic_claim: "Second Brain should treat align-cite and align-closure as verifiable publish gates because LLM automation peaks in verifiable domains."
verbatim_excerpt: "this round of LLMs can easily automate what you can verify... they end up basically progressing and creating these like jagged entities that really peak in capability in kind of like verifiable domains like math and code"
implied_assumption: "Citation verification is mechanically checkable enough to anchor trust."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-align-cite
  - workspace-align-closure
related_second_brain_principles:
  - citation_grounding
  - inspectable_retrieval
expected_benefit: "Strengthens policy to keep align-* mandatory before publish."
possible_regression: "Over-trusting verifiable checks on fuzzy conformance topics."
validation_method: "Track publish block rate and false-pass audits on pilot artifacts."
impact_scores:
  governance: 2
  closure: 2
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 13
decision: adopt
decision_rationale: "Explains why retrieval confidence cannot substitute for align-cite (complements RC-002)."
next_action: "Cross-reference in closure-compile brief and align prompts."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-091
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:11:30-00:13:30"
claim_type: risk_claim
atomic_claim: "Second Brain must keep human directors in the loop for non-verifiable publish and architecture decisions because frontier models are jagged across domains."
verbatim_excerpt: "you need to actually be in the loop a little bit... if you're not in the circuits then you have to really look at fine tuning"
implied_assumption: "CEO stage gates remain necessary even as agents accelerate drafting."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-agent-chain
  - workspace-publish
related_second_brain_principles:
  - human_review_leverage
  - governance
expected_benefit: "Justifies explicit CEO approvals between project stages."
possible_regression: "Could be misread as discouraging agent automation entirely."
validation_method: "Audit override logs when align-* flags non-verifiable conformance gaps."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 2
total_score: 10
decision: adopt
decision_rationale: "Matches existing agent chain and fail-closed platform research rules."
next_action: "No change; use in hiring/training narrative for agent-native doc authors."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-092
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:15:30-00:16:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain workspace workflows should follow agentic engineering: accelerate drafting with agents while preserving the pre-AI publish quality bar (no vibe-coded slop in published artifacts)."
verbatim_excerpt: "agentic engineering is about preserving the quality bar of what existed before in professional software... you're still responsible for your software just as before"
implied_assumption: "Speed gains come from orchestration, not from skipping align-* checks."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-agent-chain
  - workspace-publish
related_second_brain_principles:
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Vocabulary for selling governance band vs vibe-coded doc dumps."
possible_regression: "None as reinforcement."
validation_method: "Compare published artifact align-closure pass rates before/after agent chain pilots."
impact_scores:
  governance: 2
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 12
decision: adopt
decision_rationale: "Directly maps to draft→review→published lifecycle and body-prose-clean rule."
next_action: "Add to closure-compile brief examples when user approves doc edit."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-093
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:28:00-00:29:00"
claim_type: principle_claim
atomic_claim: "Second Brain operators cannot outsource understanding; the CEO/agent director must own intent, spec, and oversight while agents fill implementation detail."
verbatim_excerpt: "you can outsource your thinking, but you can't outsource your understanding"
implied_assumption: "Compilers amplify directors who already know what 'done' means."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-agent-chain
  - platform-research-review
related_second_brain_principles:
  - human_review_leverage
expected_benefit: "Reinforces CEO checkpoints and skeptical platform review."
possible_regression: "None."
validation_method: "N/A — policy reinforcement."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 8
decision: adopt
decision_rationale: "Matches CEO review between stages and platform research fail-closed policy."
next_action: "Quote in VP/PM agent prompts when user approves prompt pass."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-094
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:25:30-00:26:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain onboarding and setup docs should ship agent-native copy-paste skills as the primary interface, with human-readable URLs in See Also only."
verbatim_excerpt: "what is the thing I should copy paste to my agent?... every time I'm told, you know, go to this URL or something like that, it's just like, oh"
implied_assumption: "Agent executors are the primary reader for setup and ops flows."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - docs/setup-kit.md
  - .github/prompts
  - .github/skills
related_second_brain_principles:
  - inspectability
  - human_review_leverage
expected_benefit: "Faster agent-led setup without weakening published closure rules."
possible_regression: "Skills drift from AGENTS.md if not linted."
validation_method: "Pilot agent-native setup skill; measure time-to-first successful workspace-compile."
impact_scores:
  governance: 1
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 5
decision: experiment
decision_rationale: "Bounded improvement to platform onboarding; does not change publish artifacts."
next_action: "Draft DRAFT-RC-2026-05-27-094-agent-native-onboarding.md; add H-2026-05-27-012."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-095
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:05:30-00:06:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should replace multi-stage Markdown artifact pipelines with one-shot neural I/O (prompt in, published doc out) for governed documentation."
verbatim_excerpt: "all of my menu gen is spurious... the software 3.0 paradigm is a lot more raw... there's no need to have any of the app in between"
implied_assumption: "Intermediate artifacts add no governance value."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-projects
  - workspace-publish
related_second_brain_principles:
  - junior_engineer_closure
  - citation_grounding
expected_benefit: "Faster output for exploratory apps."
possible_regression: "Destroys traceability, align-cite, and jr-engineer closure."
validation_method: "N/A — rejected for enterprise doc compiler."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -13
decision: reject
decision_rationale: "MenuGen anti-pattern for governed docs; conflicts with stage-gated artifact set."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-096
source_transcript: raw/platform-transcripts/Andrej_Karpathy_-_From_Vibe_Coding_to_Agentic_Engineering.txt
speaker: Andrej Karpathy
timestamp: "00:07:30-00:09:00"
claim_type: market_claim
atomic_claim: "Software 3.0 will make most explicit application and documentation code obsolete as neural nets become the host process."
verbatim_excerpt: "the neural net becomes kind of like the host process and the CPU has become kind of like the coprocessor"
implied_assumption: "Second Brain should plan to delete compile/lint infrastructure."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when external validation is available; do not promote without validation."
affected_components:
  - docs/roadmap
related_second_brain_principles:
  - differentiation
expected_benefit: "Long-range strategic awareness."
possible_regression: "Premature deprecation of governance tooling."
validation_method: "Monitor lab roadmaps; no v1 action."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 1
decision: monitor
decision_rationale: "Broad paradigm claim; not actionable for v1 without primary validation."
next_action: "Revisit 2026-08-27 batch; no implementation."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-097
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:11:30-00:12:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain's separation of immutable raw/, curated wiki/, and AGENTS.md plus index/log matches the teachable LLM-wiki compiler pattern."
verbatim_excerpt: "we have the raw folder... the wiki this is the ai generated markdown files... you have the agents .md file... the index .md file... the log file"
implied_assumption: "Karpathy demo and Second Brain share the same structural invariants."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - raw
  - wiki
related_second_brain_principles:
  - filesystem_first
  - citation_grounding
expected_benefit: "External tutorial validation of architecture choices."
possible_regression: "None."
validation_method: "N/A — reinforcement."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 9
decision: adopt
decision_rationale: "Direct structural match to AGENTS.md three-layer model."
next_action: "Reference in README/platform intelligence when user approves."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-098
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:14:30-00:15:30"
claim_type: workflow_proposal
atomic_claim: "Compile from raw to wiki must run on explicit user-triggered process/ingest commands, not as an automatic side effect of chat."
verbatim_excerpt: "nothing's going to happen automatically we actually need it to tell it to process the files inside of raw for anything to actually happen"
implied_assumption: "Human intent gates when sources become curated knowledge."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-ingest-confluence
related_second_brain_principles:
  - human_review_leverage
  - source_authority
expected_benefit: "Confirms approval-gated compile invariant."
possible_regression: "None."
validation_method: "N/A — policy already in AGENTS.md."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 2
total_score: 11
decision: adopt
decision_rationale: "Matches approval-gated mutations despite tutorial later contradicting with automations."
next_action: "Contrast with rejected RC-100/101 in onboarding examples."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-099
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:01:30-00:03:00"
claim_type: product_requirement
atomic_claim: "Second Brain v1 must include journal and CRM chat layers grounded on the wiki as core product requirements."
verbatim_excerpt: "the two elements that I think are probably the most useful... are gonna be the Wiki and the journal... CRM... journal directly into the system"
implied_assumption: "Personal life-OS features are in governance-and-closure band."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - product-brief
related_second_brain_principles:
  - differentiation
expected_benefit: "Higher engagement for solo creators."
possible_regression: "Scope creep into generic assistant; weak enterprise closure."
validation_method: "N/A — out of band."
impact_scores:
  governance: -1
  closure: -1
  grounding: 0
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -8
decision: reject
decision_rationale: "Generic personal OS; RC-063 already rejected CRM-in-vault pattern."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-100
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:29:00-00:30:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should run hourly unattended automation to compile all unprocessed raw files into wiki without per-batch approval."
verbatim_excerpt: "set mine to hourly... if there are any unprocessed files inside the raw directory please process them now"
implied_assumption: "Unreviewed web clips are safe to promote to curated wiki automatically."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-compile
related_second_brain_principles:
  - human_review_leverage
  - source_authority
expected_benefit: "Hands-free ingest."
possible_regression: "Pollutes wiki with unvetted consumer content; violates approval gates."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -11
decision: reject
decision_rationale: "Conflicts with approval-gated ingest and RC-051 passive indexing rejection."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-101
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:18:30-00:19:00"
claim_type: workflow_proposal
atomic_claim: "Every workspace query should automatically create or update wiki articles and index entries without human review."
verbatim_excerpt: "as you ask questions the Wiki further and further and further builds out based on the questions you were asking"
implied_assumption: "Compounding Q&A wiki improves enterprise documentation quality."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-query
  - wiki/workspace-qa
related_second_brain_principles:
  - human_review_leverage
  - citation_grounding
expected_benefit: "Faster knowledge accumulation."
possible_regression: "Unreviewed claims enter wiki; RC-040 pattern."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -11
decision: reject
decision_rationale: "Matches RC-040 auto Q&A wiki rejection; workspace-qa requires explicit --file-back."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-102
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:19:30-00:20:00"
claim_type: workflow_proposal
atomic_claim: "After successful compile, Second Brain should move raw sources to raw/processed/ for ingest hygiene while keeping them immutable evidence."
verbatim_excerpt: "move the source file from the root raw directory to raw slash processed"
implied_assumption: "Relocation within raw/ does not break immutability if treated as append-only archive state."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-compile
  - raw
related_second_brain_principles:
  - inspectability
  - maintainability
expected_benefit: "Clearer orphan-source linting and operator visibility."
possible_regression: "Broken wikilinks if paths change without compile update."
validation_method: "Pilot on one ingest batch; run workspace-lint orphan-source check."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 5
decision: experiment
decision_rationale: "Hygiene-only; safer than autonomous wiki mutation if raw remains evidence."
next_action: "Add H-2026-05-27-013; update compile prompt after user approval."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-103
source_transcript: raw/platform-transcripts/Build_An_AI_Second_Brain_Knowledge_Base_Step-By-Step.txt
speaker: Matt Wolf
timestamp: "00:21:00-00:21:30"
claim_type: workflow_proposal
atomic_claim: "Compile must add bidirectional links from every wiki article to its immutable raw source to prevent orphan curated pages."
verbatim_excerpt: "cross link any Wiki pages generated or updated to the original source page basically I don't want these pages orphaned"
implied_assumption: "Back-links improve align-cite and compile-time traceability."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-align-cite
related_second_brain_principles:
  - citation_grounding
  - inspectable_retrieval
expected_benefit: "Faster citation verification and orphan detection."
possible_regression: "Extra wikilinks at draft only; must not appear in published body prose."
validation_method: "Merge pilot with RC-050; measure align-cite violation rate."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Aligns with Sources section requirement; may combine with RC-050."
next_action: "Track in open-hypotheses.md with H-2026-05-27-007."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-131
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:03:30-00:04:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should adopt Notion LifeOS SaaS (master databases, dashboards, personal agent integration) as its primary knowledge substrate instead of filesystem-first Markdown."
verbatim_excerpt: "Life OS is a complete personal operating system I've built for Notion... all of it integrates with your personal agent"
implied_assumption: "Notion's database UX and agent chat replace git-tracked raw/wiki separation."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - raw
  - wiki
  - AGENTS.md
related_second_brain_principles:
  - filesystem_first
  - source_authority
  - junior_engineer_closure
expected_benefit: "Easier onboarding via Notion chat agent and polished dashboards."
possible_regression: "Loss of immutability, citation traceability, and approval-gated compile."
validation_method: "N/A — rejected; reinforces RC-2026-05-27-025/033."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -13
decision: reject
decision_rationale: "Contradicts filesystem-first architecture; Notion is generic-band personal OS, not governed doc compiler."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-132
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:06:30-00:07:00"
claim_type: product_requirement
atomic_claim: "Second Brain should distribute capability via a downloadable Notion template marketplace model rather than git-tracked Markdown artifacts."
verbatim_excerpt: "The whole system is downloadable as a Notion template on the marketplace"
implied_assumption: "Template duplication is preferable to version-controlled repo schemas."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - templates
  - distribution
related_second_brain_principles:
  - inspectability
  - maintainability
expected_benefit: "Faster consumer onboarding for personal productivity users."
possible_regression: "Fork drift; no align-cite/closure toolchain on marketplace copies."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -1
  enterprise_fit: -1
  human_review_leverage: 0
total_score: -7
decision: reject
decision_rationale: "Second Brain distributes via git repo, prompts, and skills — not SaaS template marketplace."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-133
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:17:00-00:17:30"
claim_type: architecture_proposal
atomic_claim: "Credit-based Notion custom agents should be Second Brain's primary agent runtime instead of lane-labeled IDE prompts with approval gates."
verbatim_excerpt: "Have you graduated to using Notion custom agents on credit? And how do you feel about it?"
implied_assumption: "Vendor-hosted credit agents provide better governance than local prompt/skill files."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - platform-verbs
  - .github/prompts
related_second_brain_principles:
  - approval_gated_mutations
  - fail_closed
expected_benefit: "Richer Notion-native automation for personal users."
possible_regression: "Opaque credit spend; bypasses filesystem audit trail and human checkpoints."
validation_method: "N/A — rejected regardless of Notion pricing validation."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: -1
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -12
decision: reject
decision_rationale: "Credit-based vendor agents conflict with fail-closed, approval-gated platform operations."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-134
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:05:30-00:06:30"
claim_type: product_requirement
atomic_claim: "PACT personal life dashboard (plan, action, capture, track) with habits, workouts, and time sheets is a v1 Second Brain requirement."
verbatim_excerpt: "everything is organized around what I call PACT. That is to plan... action... capture... And finally, track"
implied_assumption: "Personal life operating system scope equals governed enterprise documentation compiler."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - product-scope
related_second_brain_principles:
  - governance_and_closure_band
expected_benefit: "Holistic personal productivity in one surface."
possible_regression: "Scope creep into generic assistant territory (same class as RC-027 PARA)."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -7
decision: reject
decision_rationale: "Generic personal OS out of governance-and-closure product band."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-135
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:13:30-00:15:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should expose a centralized agent hub compile artifact bundling global instructions, skills registry, and agent-readable scoped knowledge pointers."
verbatim_excerpt: "We've added an agent hub for storing agent instructions... a skills database and knowledge bases that are specifically designed for agents to read"
implied_assumption: "Agents perform better with an explicit index of instructions, skills, and KB scopes than ad hoc repo traversal."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - .github/prompts
  - .github/skills
  - wiki/index.md
related_second_brain_principles:
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "Faster agent orientation; clearer separation of always-on vs on-demand guidance."
possible_regression: "Hub becomes stale second canonical if not generated from AGENTS.md."
validation_method: "Pilot generated hub index from prompts/skills; measure orientation read count on 5 compile tasks."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Maps Notion DB hub to Markdown compile artifact; aligns with RC-066 three-layer taxonomy."
next_action: "Draft ADR; add H-2026-05-27-014 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-136
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:14:00-00:16:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should implement global agent instructions plus a specialist sub-agent registry with mode picker routing to stage-appropriate prompts."
verbatim_excerpt: "The mode picker would then choose from the sub-agents that you've created... pick from the specialist agents database"
implied_assumption: "Explicit sub-agent registry improves quality vs monolithic always-on instructions."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - .github/prompts
  - workspace agent chain
related_second_brain_principles:
  - multi_step_orchestration
  - human_review_leverage
expected_benefit: "Clearer handoffs between VP/PM/Architect/Engineer and platform reviewers."
possible_regression: "Registry sprawl if sub-agents lack input/output contracts."
validation_method: "Document registry schema; pilot on one workspace project stage chain."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Reinforces existing agent chain with explicit registry artifact; safer than Notion mode picker UI."
next_action: "Draft ADR; add H-2026-05-27-015 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-137
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:15:30-00:16:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should maintain an on-demand skills/SOP library for singular tasks that agents pull in only when executing a specific verb."
verbatim_excerpt: "a skills and SOP library... create specific skills for singular tasks and then point your agent at them"
implied_assumption: "Task-scoped skills reduce context bloat vs loading all workflows globally."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Document reinforcement in platform ADR or backlog; reject via backlog rollback."
affected_components:
  - .github/skills
  - .github/prompts
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Prevents always-on instruction bloat; matches operation-specific prompts."
possible_regression: "Skill proliferation without lint if undocumented."
validation_method: "Audit skills/ prompt parity; ensure each workspace verb has explicit skill or prompt."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "Already reflected in RC-068; Notion tour reinforces on-demand skill pattern."
next_action: "No new ADR required; reference in agent hub experiment ADR."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-138
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:14:30-00:15:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should generate a pre-formatted schema/path map of all content locations so agents always read and write to the correct raw/wiki/project paths."
verbatim_excerpt: "we've pre-formatted the master database table with every single database that exists in this template... always put information and find information in the right place"
implied_assumption: "Explicit routing table reduces mis-filed agent writes better than implicit repo conventions."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - wiki/index.md
  - AGENTS.md
  - config/second-brain.yml
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
expected_benefit: "Fewer orphan writes; faster compile-time scoping."
possible_regression: "Stale map if not generated; dual canonical with AGENTS.md."
validation_method: "Merge with RC-018 orientation map pilot; 5-task holdout for mis-routed paths."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 6
decision: experiment
decision_rationale: "Safer filesystem variant of Notion master DB table; must be generated not hand-maintained."
next_action: "Track in open-hypotheses.md with H-2026-05-27-016."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-139
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:12:30-00:13:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should enforce an internal vs external knowledge taxonomy separating org-authored notes from external clippings and references."
verbatim_excerpt: "split the knowledge base into internal and external notes... AI meeting notes... knowledge base... external knowledge, references and notes that come externally"
implied_assumption: "Lane separation reduces clutter and improves compile routing."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - raw/workspace-confluence
  - raw/workspace-external
  - workspace-compile
related_second_brain_principles:
  - source_authority
  - claim_domain
expected_benefit: "Clearer authority tagging; fewer vendor claims cited from internal sources."
possible_regression: "Over-rigid split if hybrid sources not tagged."
validation_method: "Pilot frontmatter capture_lane: internal|external on one ingest batch."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 1
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: experiment
decision_rationale: "Aligns with existing raw lane split; makes compile policy explicit."
next_action: "Draft ADR; add H-2026-05-27-017 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-140
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:17:30-00:20:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should maintain a dedicated meeting-notes capture lane in raw/ separate from curated wiki knowledge, with compile approval before promotion."
verbatim_excerpt: "What I think you should be doing with AI meeting notes is saving them in a single place... dedicated location for everything you talk about"
implied_assumption: "Conversational capture is evidence, not canonical knowledge until compiled."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - raw/platform-transcripts
  - workspace-ingest
  - workspace-compile
related_second_brain_principles:
  - immutable_raw
  - approval_gated_mutations
expected_benefit: "Preserves platform-research pattern for workspace meetings; prevents transcript-as-canonical."
possible_regression: "Extra lane complexity if not scoped per project."
validation_method: "Define raw/workspace-meetings/ schema; pilot one meeting ingest with compile gate."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Platform transcripts already demonstrate lane; extend pattern to workspace meetings with gates."
next_action: "Draft ADR; add H-2026-05-27-018 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-141
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:18:30-00:19:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should use universal cross-corpus tags in frontmatter so humans and agents can scope retrieval consistently across raw and wiki."
verbatim_excerpt: "we can have a tag system... if you relate a note with a tag... you can give the tag to your AI to search using it"
implied_assumption: "Shared tag vocabulary beats ad hoc folder navigation for cross-linking."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - wiki frontmatter
  - wiki/index.md
  - workspace-query
related_second_brain_principles:
  - inspectable_retrieval
  - page_index_retrieval
expected_benefit: "Scoped query without vector search; agent-readable filters."
possible_regression: "Tag sprawl without controlled vocabulary lint."
validation_method: "Pilot tags in config/second-brain.yml; compare query precision on 10 questions."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 5
decision: experiment
decision_rationale: "Frontmatter tags exist; universal controlled vocabulary is net-new."
next_action: "Track in open-hypotheses.md with H-2026-05-27-019."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-142
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating) / Jakob
timestamp: "00:10:00-00:10:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should emit a weekly command-center pulse as a locked read-only disposable report aggregating key metrics, never as canonical wiki source truth."
verbatim_excerpt: "gives you a weekly pulse... treat this as a reporting view. You don't do anything with it and it gives you a great snapshot"
implied_assumption: "Orientation summaries belong in reports/, not curated wiki."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - reports
  - wiki/log.md
  - workspace-lint
related_second_brain_principles:
  - inspectability
  - disposable_orientation
expected_benefit: "CEO orientation without polluting wiki; complements RC-019 lint cadence."
possible_regression: "Report mistaken for canonical if not labeled disposable."
validation_method: "Generate one pulse from log.md + lint; verify no wiki writes."
impact_scores:
  governance: 1
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Explicit disposable report pattern; safer than Notion locked DB view as truth."
next_action: "Draft ADR; add H-2026-05-27-020 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-143
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:24:30-00:25:00"
claim_type: market_claim
atomic_claim: "Notion Personal Agent chat materially improves LifeOS template adoption and user success rates compared to manual onboarding."
verbatim_excerpt: "We've seen such a better uptake and kind of success rate of users of our large templates since Notion Personal Agent was released"
implied_assumption: "Notion chat agent onboarding transfers to Second Brain Cursor/Copilot setup."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when Notion vendor docs cached; do not adopt credit-agent model."
affected_components:
  - onboarding
related_second_brain_principles:
  - human_review_leverage
expected_benefit: "Lower setup friction for complex templates."
possible_regression: "Over-reliance on chat vs reading AGENTS.md schema."
validation_method: "Compare Second Brain setup-kit agent-only vs doc-first onboarding times."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 1
decision: monitor
decision_rationale: "Anecdotal Notion vendor claim; may inform setup-kit copy-paste skills (RC-094) not substrate."
next_action: "Monitor; no ADR."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-144
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:19:30-00:20:00"
claim_type: workflow_proposal
atomic_claim: "Meeting-note AI should automatically extract tasks and write them into action databases without human compile approval."
verbatim_excerpt: "you could start automating AI processes to draw out tasks and put them into the task database"
implied_assumption: "Automated task promotion from conversational capture is safe without align-cite."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-compile
  - workspace-projects
related_second_brain_principles:
  - approval_gated_mutations
  - citation_grounding
expected_benefit: "Faster personal task capture from meetings."
possible_regression: "Ungrounded action items enter project artifacts; bypasses CEO review."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -11
decision: reject
decision_rationale: "Auto-promotion from meeting capture conflicts with approval-gated compile and align-cite."
next_action: "Record in rejected-ideas.md; safer variant is draft task list in reports/ for CEO approval."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-145
source_transcript: raw/platform-transcripts/How_I_Organise_My_Life_Using_Notion_-_In_the_AI_Era.txt
speaker: Simon (Better Creating)
timestamp: "00:20:30-00:20:45"
claim_type: market_claim
atomic_claim: "Notion AI meeting notes are among the best capture systems and should be the default enterprise meeting-ingest path for Second Brain."
verbatim_excerpt: "everyone should be doing this and I really think that Notion's meeting note system is one of the best"
implied_assumption: "Notion meeting quality exceeds governed raw/ ingest with compile gates."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review when Notion meeting-notes vendor doc cached under raw/workspace-external/notion/."
affected_components:
  - workspace-ingest
related_second_brain_principles:
  - vendor_truth
  - source_authority
expected_benefit: "Integrated meeting capture in one SaaS surface."
possible_regression: "Vendor lock-in; transcripts not immutable git evidence."
validation_method: "Compare Notion export fidelity vs existing transcript ingest path."
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
decision: monitor
decision_rationale: "Unvalidated vendor superiority claim; RC-140 safer pattern uses raw lane regardless of capture tool."
next_action: "Monitor; optional Notion doc fetch for vendor-truth check."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-105
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:01:30-00:02:00"
claim_type: principle_claim
atomic_claim: "Second Brain must treat personal understanding and publish-time accountability as non-delegable—agents may draft, but humans own comprehension and sign-off."
verbatim_excerpt: "The one thing which you cannot outsource is your personal understanding... You can't delegate accountability."
implied_assumption: "Automated drafting without human comprehension breaks governance and jr-engineer closure."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-publish
  - workspace-align-closure
  - workspace-projects agent chain
related_second_brain_principles:
  - junior_engineer_closure
  - human_review_leverage
  - citation_grounding
expected_benefit: "Reinforces CEO stage checkpoints and inlined rules at publish instead of trusting model fluency."
possible_regression: "Over-emphasis on manual review could slow throughput if checkpoints are duplicated."
validation_method: "Audit one published artifact set for inlined rules without wikilink delegation."
impact_scores:
  governance: 2
  closure: 2
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 2
total_score: 11
decision: adopt
decision_rationale: "Core to Second Brain's governed compiler—understanding stays with the CEO/engineer reviewer, not the model."
next_action: "Draft ADR RC-105; reinforce in finalize and publish prompts after user approval."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-106
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:02:30-00:04:00"
claim_type: principle_claim
atomic_claim: "Second Brain's primary product narrative should be ground-level workflow empowerment per team, not frontier model competition."
verbatim_excerpt: "real value for the economy and society is created at the ground level. Workflow by workflow... at the individual level."
implied_assumption: "Enterprise documentation compilers win by fitting existing jobs, not by building bigger models."
current_design_status: partially_supported
evidence_supplied_by_speaker: citation
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-enter queue when enterprise deployment playbook scope is approved."
affected_components:
  - product-positioning
  - docs/roadmap
related_second_brain_principles:
  - governance_band_scope
expected_benefit: "Aligns marketing with governance-and-closure niche."
possible_regression: "Could dilute focus into generic productivity assistant positioning."
validation_method: "Defer until product-brief positioning review with user approval."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 2
decision: defer
decision_rationale: "Directionally aligned but not a concrete Second Brain mechanism; blocked on protected positioning docs."
next_action: "Revisit with user-approved product-brief/roadmap edit pass."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-107
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:13:00-00:13:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain onboarding should teach governed tool assembly (skills, prompts, lint scripts) rather than model selection or vibe-coded glue code."
verbatim_excerpt: "I was just assembling tools. It's just tool assembly."
implied_assumption: "Composable governed verbs beat monolithic agent runtimes for enterprise documentation."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - second-brain onboarding prompt
  - .github/skills
  - .github/prompts
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Reduces attraction to consumer agent stacks; clarifies compiler mental model."
possible_regression: "Documentation sprawl if every tool is listed without scope discipline."
validation_method: "Add assembly map to onboarding; measure time-to-first successful compile in pilot."
impact_scores:
  governance: 1
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 6
decision: experiment
decision_rationale: "Fits compiler analogy; needs a concrete onboarding artifact, not keynote rhetoric alone."
next_action: "Track H-2026-05-27-014 in open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-108
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:06:00-00:08:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should use an always-on WhatsApp/nano-claw personal agent as its primary user interface for daily cognitive overload."
verbatim_excerpt: "nano-claw provides the platform. It allows me to communicate through WhatsApp with my agent."
implied_assumption: "Messaging-channel agents are enterprise-safe and equivalent to governed documentation workflows."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - runtime
  - security
related_second_brain_principles:
  - approval_gated_mutations
  - no_telemetry
expected_benefit: "Ubiquitous mobile access for personal tasks."
possible_regression: "Unauditable channel, third-party ToS risk, scope creep into consumer automation."
validation_method: "N/A — rejected for v1 workspace/platform lanes."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -2
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -14
decision: reject
decision_rationale: "Duplicates out-of-scope consumer agent band; conflicts with filesystem-first, approval-gated design."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-109
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:09:00-00:09:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should adopt an entity-edge graph memory with local embeddings as the canonical knowledge substrate instead of immutable raw plus curated wiki."
verbatim_excerpt: "a memory system with graphs. So it's got entities, the edges are entities, causality, temporal relationships"
implied_assumption: "Graph proximity and semantic search replace claim-level citation verification."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-query
  - workspace-compile
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
expected_benefit: "Rich relationship navigation for personal memory."
possible_regression: "Non-inspectable memory; similarity mistaken for support (RC-002)."
validation_method: "N/A — rejected; safer variant is index/section-tree plus align-cite."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -2
  maintainability: -1
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -12
decision: reject
decision_rationale: "Graph+embedding substrate weakens authority tags and align-cite; repeats RC-009 rejection pattern."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-110
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:10:30-00:11:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should auto-generate Obsidian wikis from personally curated databases via LLM-supervised wiki generation without per-batch human approval."
verbatim_excerpt: "Andrzej Kaparty came up with his LLM supervised wiki generation, so I added that in as well."
implied_assumption: "Personal curation quality substitutes for authority tagging and compile-time citation checks."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; submit safer variant as new claim."
affected_components:
  - workspace-compile
  - wiki
related_second_brain_principles:
  - approval_gated_mutations
  - source_authority
expected_benefit: "Faster personal knowledge surfacing."
possible_regression: "Auto-mutation of wiki; ungrounded pages become canonical by accident."
validation_method: "N/A — rejected; safer variant is approval-gated compile from raw/."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -11
decision: reject
decision_rationale: "Matches RC-059/101 auto-wiki rejection; consumer second-brain pattern, not governed compiler."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-111
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:16:00-00:16:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain pipelines must pair LLM synthesis steps with deterministic expert-rule checks and must not route every validation step through the model."
verbatim_excerpt: "there is still a role for deterministic systems. There is still a role for expert rule-based systems."
implied_assumption: "Lint and align scripts are first-class citizens equal to generation prompts."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-align-cite
  - workspace-align-closure
  - workspace-lint
  - scripts/lint-platform-research.py
related_second_brain_principles:
  - citation_grounding
  - inspectable_retrieval
  - junior_engineer_closure
expected_benefit: "Fail-closed publish gate; reduces hammer-everything-with-LLM anti-pattern."
possible_regression: "Rigid rules without LLM assist for edge-case conformance advisory."
validation_method: "Require align-cite + align-closure + lint pass before publish on pilot project."
impact_scores:
  governance: 2
  closure: 2
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 2
  enterprise_fit: 2
  human_review_leverage: 1
total_score: 14
decision: adopt
decision_rationale: "Already embodied in align-* and lint; keynote provides external validation of hybrid design."
next_action: "Draft ADR RC-111; document required deterministic gate ordering."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-112
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:12:30-00:21:00"
claim_type: principle_claim
atomic_claim: "Second Brain should support deployment-at-edge patterns—local lint/align reports and scoped verify—without adopting consumer messaging-agent runtimes."
verbatim_excerpt: "I'm a believer in deployment at the edge... my most daily use agent is running off a Raspberry Pi"
implied_assumption: "Air-gapped or low-connectivity review still needs governed artifact validation."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-lint
  - scripts
related_second_brain_principles:
  - enterprise_fit
  - inspectable_retrieval
expected_benefit: "Review closure offline in regulated environments."
possible_regression: "Scope creep into hardware agent babysitting vs documentation compiler."
validation_method: "Pilot one offline lint+align report bundle; no autonomous wiki writes."
impact_scores:
  governance: 1
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 0
total_score: 7
decision: experiment
decision_rationale: "Safer variant of edge deployment—validation at edge, not WhatsApp agent at edge."
next_action: "Track H-2026-05-27-015 in open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-113
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:18:30-00:19:00"
claim_type: principle_claim
atomic_claim: "Second Brain differentiation should emphasize governed tools, prompts, and verification workflows over frontier model selection."
verbatim_excerpt: "Tools matter more than models."
implied_assumption: "Model swaps do not fix missing citations, authority tags, or closure rules."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md positioning
  - .github/prompts
  - .github/skills
related_second_brain_principles:
  - governance_band_scope
  - differentiation
expected_benefit: "Scope discipline vs generic assistants; reinforces compiler metaphor."
possible_regression: "Under-investment in retrieval quality if interpreted as anti-improvement."
validation_method: "Scope-filter checklist on new feature requests cites tools-over-models principle."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 2
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: adopt
decision_rationale: "Aligns with governance-and-closure north star and RC-075 skills-first pattern."
next_action: "Reference in scope-filter reviews; optional merge into onboarding ADR with RC-107."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-114
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:05:00-00:13:30"
claim_type: risk_claim
atomic_claim: "Second Brain should formalize fail-closed mutation gates—explicit human approval per shell invocation and per write path—with short auditable allowlists."
verbatim_excerpt: "NanoClaw insists that you approve for every time you give bash access to the agent."
implied_assumption: "Containerization and per-action approval reduce blast radius of agent mistakes."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - approval-gated mutations
  - platform-transcript-librarian
  - workspace-ingest
related_second_brain_principles:
  - fail_closed
  - inspectable_retrieval
expected_benefit: "Clearer operator trust loop; fewer silent wiki/raw mutations."
possible_regression: "Approval fatigue if gates are duplicated without UX consolidation."
validation_method: "Publish per-verb approval matrix; pilot on one ingest+compile cycle."
impact_scores:
  governance: 2
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 1
total_score: 10
decision: experiment
decision_rationale: "Already policy-level supported; needs concrete matrix artifact, not nano-claw runtime."
next_action: "Track H-2026-05-27-016 in open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-115
source_transcript: raw/platform-transcripts/Building_a_Second_Brain_-_Opportunities_Risks_and_Implications_for_AI_Adoption_in_Singapore.txt
speaker: Dr Vivian Balakrishnan
timestamp: "00:14:30-00:15:00"
claim_type: principle_claim
atomic_claim: "Second Brain operators and CEOs must use the system hands-on before governing it—stage checkpoints are mandatory, not optional briefings."
verbatim_excerpt: "You cannot govern a technology that you have only been briefed on. You better get your hands dirty."
implied_assumption: "Policy makers and doc owners need experiential limits knowledge, not slide decks."
current_design_status: already_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-projects agent chain
  - platform-research-review
related_second_brain_principles:
  - human_review_leverage
  - governance_band_scope
expected_benefit: "Reduces blind adoption of transcript or vendor hype into canonical docs."
possible_regression: "Slower executive onboarding if checkpoints are heavyweight."
validation_method: "Verify agent-chain prompts block next stage without explicit CEO approval string."
impact_scores:
  governance: 2
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 2
total_score: 9
decision: adopt
decision_rationale: "Maps directly to CEO reviews between VP→PM→Architect→Engineer in AGENTS.md."
next_action: "Reinforce in second-brain onboarding; bundle with RC-105 ADR."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-116
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:15:30-00:16:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain draft-stage agents should support an explicit thinking mode (frontmatter or prompt contract) that forbids publish-shaped artifact generation until the user switches to artifact mode."
verbatim_excerpt: "one of the big things here is that I'm in thinking mode, not writing mode yet... in the front matter actually, where I've told Claude code, like, don't help me write anything right now"
implied_assumption: "Models default to generative output; explicit mode separation improves exploration quality before compile."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-projects
  - workspace-vp-agent
  - workspace-pm-agent
related_second_brain_principles:
  - human_review_leverage
  - junior_engineer_closure
expected_benefit: "Reduces premature draft slop; keeps exploration inspectable in draft-tier files."
possible_regression: "Users forget to switch modes; thinking notes mistaken for publish-ready content."
validation_method: "Pilot agent_mode frontmatter on one draft project; count unpublishable fragments before review transition."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 10
decision: experiment
decision_rationale: "Strong draft-stage guardrail; needs pilot before canonical prompt changes."
next_action: "Draft ADR RC-116; add H-2026-05-27-021 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-117
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:22:00-00:23:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should offer a thinking-partner sub-agent that asks interview questions and logs notes without producing stage publish artifacts."
verbatim_excerpt: "you're a collaborative thinking partner specializing in helping people explore complex problems... don't try to write the thing"
implied_assumption: "Separating exploration agent from ghostwriter agent improves requirements clarity."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-pm-agent
  - workspace-vp-agent
related_second_brain_principles:
  - human_review_leverage
  - inspectable_retrieval
expected_benefit: "Richer problem exploration before PM/Engineer handoff; complements RC-055 identity packs."
possible_regression: "Extra agent complexity; thinking notes promoted without sources."
validation_method: "A/B one PM stage with vs without thinking-partner pass; CEO rates requirement clarity."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 8
decision: experiment
decision_rationale: "Aligns with stage-gated chain; complements RC-055/058 without replacing agents."
next_action: "Draft ADR RC-117; link to RC-116 mode flag."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-118
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:14:30-00:15:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain project stages should support end-of-day daily progress logs synthesized from that day's draft notes to preserve multi-session continuity."
verbatim_excerpt: "at the end of each day, I have the AI write up the changes... the things I learned that day that are gonna help me push this talk along"
implied_assumption: "Dated progress summaries reduce restart friction better than chat memory alone."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: unvalidated
correction_route: "Merge with RC-058 pilot; approve experiment ADR; reject via backlog rollback."
affected_components:
  - workspace-projects
  - finalize
related_second_brain_principles:
  - filesystem_first
  - human_review_leverage
expected_benefit: "Inspectable session continuity adjacent to RC-058 handoff."
possible_regression: "Stale or hallucinated progress summaries if not grounded in file reads."
validation_method: "Pilot daily-progress/ subfolder for two sessions; measure resumption without re-brief."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 10
decision: reject
decision_rationale: "Superseded by RC-130 (PIC-011): project-stage-scaffold includes daily-progress/ as draft-tier evidence; standalone daily-progress experiment duplicates accepted scaffold without added governance lift."
next_action: "Use templates/workspace/project-stage-scaffold/README.md daily-progress/; pilot via H-2026-05-27-023 (RC-130 only)."
next_review_after: 2026-08-28
rejection_register: wiki/platform-research/rejected-ideas.md
owner: unassigned
status: closed
last_reviewed: 2026-05-28
```

```yaml
claim_id: RC-2026-05-27-119
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:31:00-00:32:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain agents should support a catch-up-on-research workflow that reads project files modified in the last N days by filesystem date before proposing next actions."
verbatim_excerpt: "can you catch me up on the last three days of research... it's just gonna go read all the stuff"
implied_assumption: "Date-scoped file reads are a reliable, inspectable substitute for chat memory on resume."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-query
  - workspace-projects
related_second_brain_principles:
  - inspectable_retrieval
  - read_before_write
expected_benefit: "Transparent resume path; aligns with page-index retrieval over embeddings."
possible_regression: "Misses relevant older context if date window too narrow."
validation_method: "Pilot catch-up prompt on one project; reviewer confirms all cited files exist and match dates."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: reject
decision_rationale: "Superseded by RC-130 research/ + RC-058 handoff + RC-122 read-before-write: catch-up-on-research is covered by resume reads of handoff, research/, and scoped query—not a separate experiment."
next_action: "Document catch-up path in draft-tier-map.md; use workspace-query or stage agent resume reads."
next_review_after: 2026-08-28
rejection_register: wiki/platform-research/rejected-ideas.md
owner: unassigned
status: closed
last_reviewed: 2026-05-28
```

```yaml
claim_id: RC-2026-05-27-120
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:18:30-00:20:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain compile agents should start sessions at repository root so scoped reads can reach the full wiki/raw corpus for relevance discovery during draft compile."
verbatim_excerpt: "I'm starting it in the full obsidian vault... we're in the root directory, all this stuff is in the root directory"
implied_assumption: "Broader corpus access improves compile-time source discovery without harming governance."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Bound with config/second-brain.yml scope; approve experiment ADR; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-query
  - config/second-brain.yml
related_second_brain_principles:
  - scoped_retrieval
  - inspectable_retrieval
expected_benefit: "Better compile-time source surfacing when bounded by project scope config."
possible_regression: "Unscoped reads leak out-of-scope content and weaken align-cite."
validation_method: "Pilot with explicit scope paths; 5-task holdout for mis-routed reads (merge RC-067)."
impact_scores:
  governance: 0
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 3
decision: experiment
decision_rationale: "Useful only with config scope guardrails; personal vault pattern does not transfer unbounded."
next_action: "Merge pilot with RC-067 path-scoped compile hints."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-121
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:16:30-00:24:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should allow importing external chat transcripts into project-stage evidence folders as draft-tier informational sources."
verbatim_excerpt: "I've got chats... taking chats I'm having in other things... chats I was having with chat GPT and Claude and grok"
implied_assumption: "External chats are equivalent to ingested raw evidence when clipped into project folders."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; draft-only + authority tags required; reject via backlog rollback."
affected_components:
  - workspace-projects
  - platform-transcript-librarian
related_second_brain_principles:
  - source_authority
  - approval_gated_mutations
expected_benefit: "Preserves exploration context in filesystem for compile without chat-only memory."
possible_regression: "Ungrounded chat content promoted to wiki or cited as standards."
validation_method: "Pilot chats/ import on one project; align-cite must flag chat-only citations at publish."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 6
decision: experiment
decision_rationale: "Safer as draft evidence in project scaffold; not workspace canonical ingest."
next_action: "Include in RC-130 scaffold; require authority: informational on imports."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-122
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:25:30-00:26:30"
claim_type: principle_claim
atomic_claim: "Second Brain workspace agents should default to read-before-write: prioritize scoped reads, questioning, and source inspection over generative artifact output."
verbatim_excerpt: "there's entirely too much focus on its ability to write and not enough focus on its ability to read... its ability to read is incredible"
implied_assumption: "Most daily value is comprehension and synthesis, not generation."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-agent-chain
  - workspace-query
  - workspace-compile
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
  - read_before_write
expected_benefit: "Explicit principle reinforces RC-001/002 and reduces uncited generation."
possible_regression: "Slower first response if over-applied without scope bounds."
validation_method: "Codify in agent prompts; verify read lists logged before first write in next three runs."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 11
decision: adopt
decision_rationale: "Already aligned with page-index retrieval policy; worth explicit codification."
next_action: "Draft ADR RC-122; queue in implementation backlog after user approval."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-123
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:34:30-00:35:30"
claim_type: market_claim
atomic_claim: "Enterprise AI adoption succeeds when models fit organizational 'nooks and crannies' without forcing unified tooling (Thomas's English muffin theory)."
verbatim_excerpt: "my Thomas's English muffin Theory of AI which is that it like gets into the nooks and crannies"
implied_assumption: "AI reduces change-management friction vs past enterprise software centralization."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Monitor; re-review when enterprise client case study available; do not adopt roadmap from anecdote alone."
affected_components:
  - product-positioning
related_second_brain_principles:
  - enterprise_fit
  - governance
expected_benefit: "Useful positioning narrative for governed compiler that meets teams where they work."
possible_regression: "Used to justify bypassing standards and unified citation discipline."
validation_method: "Track Fortune-50 client evidence from Alephic/Every; compare to Second Brain scope filter."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 2
decision: monitor
decision_rationale: "Interesting enterprise narrative; unvalidated and could excuse governance bypass if misapplied."
next_action: "Re-review 2026-08-27 or on first validated enterprise case study."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-124
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:37:30-00:39:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should support tacit cross-repo code sharing where agents read one repository and reimplement patterns in another without modular libraries."
verbatim_excerpt: "we just added her to the sparkle repo and I was just like just ask Claude code to figure out how it works and just do your own version"
implied_assumption: "AI translation replaces shared libraries for heterogeneous stacks."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: unvalidated
correction_route: "Defer until code-as-source v2 scope approved; reject if proposed for v1 doc compiler."
affected_components:
  - out-of-scope-codebase-assistant
related_second_brain_principles:
  - scope_discipline
expected_benefit: "Engineering productivity across repos."
possible_regression: "Scope creep into IDE codebase assistant territory (RC-009 pattern)."
validation_method: "N/A until v2 code lane approved."
impact_scores:
  governance: -1
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: 0
  human_review_leverage: 0
total_score: -3
decision: defer
decision_rationale: "Useful for eng teams but explicitly out of v1 governance-and-closure doc-compiler scope."
next_action: "Re-enter when code-as-source v2 scope is approved."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-125
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:11:00-00:11:30"
claim_type: product_requirement
atomic_claim: "Second Brain v1 should require PARA method vault organization (Projects/Areas/Resources/Archives) for all users."
verbatim_excerpt: "you can see I'm, I'm following the, the para method"
implied_assumption: "Personal PKM taxonomy is necessary for governed enterprise documentation."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; overlaps RC-027."
affected_components:
  - wiki-structure
related_second_brain_principles:
  - scope_discipline
expected_benefit: "Familiar personal organization for note-takers."
possible_regression: "Forces consumer PKM patterns on enterprise compiler; duplicates RC-027 rejection."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -8
decision: reject
decision_rationale: "PARA is personal PKM; Second Brain uses authority/type-based wiki layout; RC-027 already rejected."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-126
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "01:00:00-01:02:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should require or recommend home-server deployment (mini PC, Tailscale VPN, Termius) for phone-based Claude Code access."
verbatim_excerpt: "in my basement, I have a mini PC... tail scale lets you set up these very simple VPNs... Termius is just a terminal"
implied_assumption: "Mobile terminal access to a home server is a core second-brain deployment pattern."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - deployment
related_second_brain_principles:
  - scope_discipline
  - approval_gated_mutations
expected_benefit: "Work from phone anywhere on personal vault."
possible_regression: "Ops burden, security surface, distracts from governance-and-closure product."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: 0
  vendor_truth: 0
  inspectability: -1
  maintainability: -2
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -9
decision: reject
decision_rationale: "Practitioner-specific infra; not enterprise doc-compiler deployment; generic mobile access scope."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-127
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:05:30-00:08:00"
claim_type: product_requirement
atomic_claim: "Second Brain should integrate Grok voice mode (or comparable voice UI) as a product capability for research and thinking."
verbatim_excerpt: "I use quite a bit of, uh, uh, grok voice mode... I just find grok's voice mode to be significantly smarter than anybody else is"
implied_assumption: "Voice mode superiority is stable and relevant to governed documentation compiler."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review per rejected-ideas.md; vendor claims require primary-source validation before adopt."
affected_components:
  - out-of-scope-voice-ui
related_second_brain_principles:
  - scope_discipline
  - vendor_truth
expected_benefit: "Hands-free research during commute."
possible_regression: "Generic chat/voice assistant scope; unvalidated vendor superiority claim."
validation_method: "N/A — rejected for v1 product."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: -1
  inspectability: -2
  maintainability: -1
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: -1
total_score: -11
decision: reject
decision_rationale: "Voice UI is generic-band; vendor anecdote unvalidated; fails scope filter vs Rovo/Copilot/Grok apps."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-128
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:02:30-00:03:30"
claim_type: product_requirement
atomic_claim: "Second Brain product direction should be personal Obsidian PKM with Claude Code as primary interface—not a governed enterprise documentation compiler."
verbatim_excerpt: "probably my number one cloud code use is using it as a tool to interact with my notes... switched over to Obsidian"
implied_assumption: "Personal note vault equals Second Brain north star."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md; safer variant is draft-stage project ergonomics only."
affected_components:
  - product-definition
related_second_brain_principles:
  - junior_engineer_closure
  - source_authority
  - governance
expected_benefit: "Low-friction personal knowledge work."
possible_regression: "Abandons authority tagging, align-cite, stage-gated publish closure."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -12
decision: reject
decision_rationale: "Explicit scope conflict with governed doc compiler; consumer PKM is generic-band."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-129
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:49:00-00:51:30"
claim_type: product_requirement
atomic_claim: "Second Brain should target vibe-coding education for children (e.g., v0 apps for 10-year-olds) as in-scope product direction."
verbatim_excerpt: "I encouraged her to uh vibe code an app to do it... she did 75 revs on v zero"
implied_assumption: "Consumer coding education belongs in enterprise documentation compiler roadmap."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md."
affected_components:
  - out-of-scope-education
related_second_brain_principles:
  - scope_discipline
expected_benefit: "Inspirational anecdote for AI literacy."
possible_regression: "Scope drift into consumer ed-tech and vibe-coding hype."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -8
decision: reject
decision_rationale: "Off-scope per product-brief governance band; no bearing on jr-engineer-executable artifact sets."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-130
source_transcript: raw/platform-transcripts/Claude_Code_Can_Be_Your_Second_Brain.txt
speaker: Noah Breyer
timestamp: "00:16:00-00:17:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain workspace projects should use a standard draft-stage scaffold with chats/, daily-progress/, research/, and thinking notes alongside stage artifacts."
verbatim_excerpt: "I've got chats... daily progress... research that's where I've got a bunch of like articles and PDFs"
implied_assumption: "Folder conventions improve multi-session compile without PARA-wide vault mandates."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; bundle with RC-058; reject via backlog rollback."
affected_components:
  - workspace-projects
  - workspace-start-project
related_second_brain_principles:
  - filesystem_first
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Operationalizes RC-058 with inspectable evidence layout; excluded from published set until compiled."
possible_regression: "Scaffold mistaken for publish artifact set; folder sprawl at publish."
validation_method: "Pilot scaffold on one project; verify align-closure excludes scaffold from published set."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: experiment
decision_rationale: "Project-scoped safer variant of personal PKM folders; extends RC-058 without PARA mandate."
next_action: "Draft ADR RC-130; merge with H-2026-05-27-009."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-146
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:07:30-00:08:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should use an explicit raw/ inbox folder for unprocessed captures and require user-approved compile before promoting content into curated wiki."
verbatim_excerpt: "it's in this folder called raw, and this is just anything I dump in here. This is my inbox."
implied_assumption: "Separating capture from compile preserves immutability while keeping clipper workflows teachable."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - raw/
  - workspace-compile
  - workspace-ingest-confluence
related_second_brain_principles:
  - filesystem_first
  - approval_gated_mutations
  - source_authority
expected_benefit: "Safer variant of Karpathy clipper→raw workflow; keeps compile inspectable and approval-gated."
possible_regression: "Operators treat raw/ as mutable wiki or skip approval on batch compile."
validation_method: "Pilot ingest prompt documenting inbox staging; verify compile requires explicit user approval per batch."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Already partially in AGENTS.md; worth explicit inbox+approval documentation in compile prompts."
next_action: "Draft ADR RC-146; pilot with one ingest batch."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-147
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:08:30-00:09:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should expose AGENTS.md-style routing files with ingest sub-prompts that tell IDE agents how to process raw sources on explicit user command."
verbatim_excerpt: "you've got this little file here called Agents .md... ingest when the user adds a source and asks the LLM to process it, do these steps"
implied_assumption: "Prompt routing in-repo is more durable and inspectable than chat-only instructions."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - .github/prompts/
  - workspace-compile
related_second_brain_principles:
  - filesystem_first
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "Confirms teachable Karpathy pattern matches canonical agent routing; practitioners can copy from tutorials."
possible_regression: "Duplicate prompt files drift from AGENTS.md unless single canonical source maintained."
validation_method: "No new validation; covered by existing shims referencing AGENTS.md."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 11
decision: adopt
decision_rationale: "Direct reinforcement of existing AGENTS.md + prompt shim architecture demonstrated at scale in Karpathy tutorials."
next_action: "Verified baseline; reference in onboarding examples."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-148
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:05:30-00:06:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain compile should create or update topic and entity pages with cross-links anchored to immutable raw sources, similar to Wikipedia-style concept graphs."
verbatim_excerpt: "I've got topics and entities here... the large language model, reading these text files and going, this text file kind of looks like this text file. Let's connect the two."
implied_assumption: "LLM-discovered cross-links improve retrieval if every link traces to raw evidence."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-concepts
  - workspace-connections
related_second_brain_principles:
  - citation_grounding
  - source_authority
  - junior_engineer_closure
expected_benefit: "Structured topic/entity compile from raw improves navigation without embedding-only retrieval."
possible_regression: "Ungrounded LLM links become canonical without align-cite; personal PKM topics pollute workspace standards."
validation_method: "Pilot compile on one batch; align-cite verifies every wikilink target has matching raw excerpt."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 6
decision: experiment
decision_rationale: "Concept/connection articles exist; experiment formalizes topic/entity compile steps with mandatory Sources sections."
next_action: "Draft ADR RC-148; pilot on one Confluence compile batch."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-149
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:09:00-00:09:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain ingest should validate duplicate source URLs before compile to skip already-processed captures."
verbatim_excerpt: "before processing validate that the same source URL, it hasn't already been processed. A lot of times I'll throw the same YouTube video in there"
implied_assumption: "URL dedup reduces orphan raw noise without weakening immutability."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-ingest-vendor-doc
  - workspace-ingest-confluence
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Reduces duplicate raw entries and compile waste; improves lint orphan-source signal."
possible_regression: "False-positive dedup skips legitimate re-ingest after source version change."
validation_method: "Add URL hash check to compile prompt; measure duplicate raw files on one ingest pilot."
impact_scores:
  governance: 0
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 5
decision: experiment
decision_rationale: "Low-risk compile hygiene; complements RC-102 processed-folder experiment."
next_action: "Bundle with RC-146 pilot; document dedup rule in compile prompt."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-150
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:06:30-00:07:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain workspace lane should default to Obsidian Chrome clipper dumps of YouTube transcripts, tweets, and articles without authority or domain frontmatter."
verbatim_excerpt: "Obsidian Chrome extension... I just click add to Obsidian... saves the entire transcript already here"
implied_assumption: "Consumer web clips are equivalent to enterprise Confluence/vendor sources."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; safer variant is platform-research lane or tagged workspace ingest."
affected_components:
  - raw/
  - workspace-ingest
related_second_brain_principles:
  - source_authority
  - governance
  - vendor_truth
expected_benefit: "Fast personal capture for marketers."
possible_regression: "Ungrounded wiki pollution; authority conflicts; align-cite failures at publish."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: -1
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -13
decision: reject
decision_rationale: "Repeats RC-104; workspace lane requires Confluence/vendor/internal authority tags."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-151
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:09:30-00:10:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should run scheduled nightly Codex automations that process all unprocessed raw/ files without per-batch human approval."
verbatim_excerpt: "set to run at 1250 AM pretty much every single day... it processes everything that was in the raw folder"
implied_assumption: "Unattended compile is safe when prompts are written once."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - workspace-compile
  - approval_gated_mutations
related_second_brain_principles:
  - approval_gated_mutations
  - governance
  - human_review_leverage
expected_benefit: "Hands-free overnight processing for personal vaults."
possible_regression: "Silent wiki mutation; no audit checkpoint; aligns with RC-100/059 rejections."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -12
decision: reject
decision_rationale: "Conflicts with approval-gated mutations and fail-closed compile policy in AGENTS.md."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-152
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:05:00-00:06:30"
claim_type: product_requirement
atomic_claim: "Second Brain product direction should be a personal Obsidian topics/entities wiki built from consumer YouTube and article clips—not a governed enterprise documentation compiler."
verbatim_excerpt: "you've created all the stuff that you like and the LLMs are stitching it together to make it its own little mini internet"
implied_assumption: "Personal curated internet equals Second Brain north star."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md; safer variant is compile ergonomics only."
affected_components:
  - product-definition
related_second_brain_principles:
  - junior_engineer_closure
  - source_authority
  - governance
expected_benefit: "Low-friction personal knowledge for creators."
possible_regression: "Abandons authority tagging, stage-gated publish, align-cite closure."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -12
decision: reject
decision_rationale: "Duplicates RC-128 personal Obsidian PKM rejection; generic-band vs governance-and-closure niche."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-153
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:17:30-00:18:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should deliver proactive 9am Slack morning briefs with business recommendations derived from wiki content without explicit approval gates."
verbatim_excerpt: "every morning in Slack, I get a message at 9 a .m. that says like, based on the stuff that you've saved... here's what I recommend you try next"
implied_assumption: "Proactive AI recommendations from personal wiki are safe to act on without review."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-messaging-automation
related_second_brain_principles:
  - approval_gated_mutations
  - governance
  - human_review_leverage
expected_benefit: "Surfaces saved research as actionable next steps."
possible_regression: "Unreviewed recommendations sent to team channels; no audit trail; generic assistant scope."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -1
  human_review_leverage: -2
total_score: -11
decision: reject
decision_rationale: "Proactive messaging automation without gates duplicates rejected personal-ops patterns; RC-142 safer variant is disposable report only."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-154
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:18:30-00:19:30"
claim_type: product_requirement
atomic_claim: "Second Brain v1 should include a personal networking CRM in the wiki for conference contacts and conversation recall."
verbatim_excerpt: "I created a sort of personal networking CRM inside of it as well... saves the contact information of the people inside of the Wiki as well"
implied_assumption: "Contact CRM belongs in governed documentation compiler scope."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-crm
related_second_brain_principles:
  - scope_discipline
  - governance
expected_benefit: "Better networking recall for creators."
possible_regression: "PII in wiki without enterprise controls; duplicates RC-063 rejection."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -9
decision: reject
decision_rationale: "Generic personal CRM scope; RC-063 already rejected CRM-in-Obsidian pattern."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-155
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:20:00-00:21:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should adopt sitemap-watcher automations that alert when competitor or vendor sites add new pages for competitive intelligence."
verbatim_excerpt: "automation that looks at the website's site map and alerts me whenever there's a new page added to the website"
implied_assumption: "Sitemap diffs are reliable signals for vendor capability changes worth wiki ingest."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Monitor; re-review when vendor-truth fetch workflow covers watched URLs."
affected_components:
  - workspace-ingest-vendor-doc
  - vendor_truth
related_second_brain_principles:
  - vendor_truth
  - approval_gated_mutations
expected_benefit: "Early competitive/vendor doc awareness for workspace projects."
possible_regression: "Auto-ingest ToS noise; unvalidated vendor claims enter wiki without TTL fetch."
validation_method: "Track as candidate for vendor-truth revalidation cadence; no auto wiki writes."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 1
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 2
decision: monitor
decision_rationale: "Useful external intel pattern but requires vendor-truth fetch+approval before any workspace cite."
next_action: "Re-review when vendor doc TTL workflow covers competitive watchlist."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-156
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:23:00-00:24:30"
claim_type: product_requirement
atomic_claim: "Second Brain v1 should cross-reference daily journal entries with wiki content to deliver personalized advice grounded in saved clips."
verbatim_excerpt: "it cross -references my journal with everything that's in my wiki... based on everything you've saved over time, here's what I found that's relevant"
implied_assumption: "Journal+wiki advice loop is core enterprise documentation compiler value."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-journal
related_second_brain_principles:
  - scope_discipline
  - junior_engineer_closure
expected_benefit: "Personal reflection support for creators."
possible_regression: "Generic coaching scope; duplicates RC-099 journal rejection."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: 0
total_score: -8
decision: reject
decision_rationale: "Journal layer is generic personal PKM; not jr-engineer-executable artifact compiler scope."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-157
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:10:30-00:11:30"
claim_type: principle_claim
atomic_claim: "Second Brain workspace query must ground answers in compiled wiki sources and list traceable source references—not LLM parametric knowledge alone."
verbatim_excerpt: "you can see exactly what it referenced from within my wiki here... and then it shows the sources, and these are various sources inside of my Wiki"
implied_assumption: "Showing wiki sources makes answers auditable and actionable for governed work."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - workspace-query
  - workspace-align-cite
related_second_brain_principles:
  - citation_grounding
  - inspectable_retrieval
  - junior_engineer_closure
expected_benefit: "Reinforces index-guided query with explicit source listing before publish-bound synthesis."
possible_regression: "Source lists mistaken for align-cite pass without verification."
validation_method: "Codify in workspace-query prompt; verify source paths exist on next three queries."
impact_scores:
  governance: 2
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 11
decision: adopt
decision_rationale: "Matt's demo mirrors workspace-query + RC-002 distinction; worth explicit codification alongside RC-122."
next_action: "Draft ADR RC-157; queue after RC-122 in backlog."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-158
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:15:00-00:15:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain IDE agents should open the local repo or Obsidian vault folder as the project root so agents have filesystem-first read/write access to raw and wiki layers."
verbatim_excerpt: "create a new project, use an existing folder... select whatever folder you have installed your Obsidian vault on"
implied_assumption: "Folder-scoped agent access is sufficient without hosted knowledge APIs."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - setup-kit
related_second_brain_principles:
  - filesystem_first
  - inspectability
expected_benefit: "Confirms practitioner onboarding path matches Second Brain local-repo model."
possible_regression: "Unscoped full-vault reads without config/second-brain.yml bounds."
validation_method: "Document in setup-kit; scope reads per project config."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: adopt
decision_rationale: "Reinforces RC-004 filesystem-first; Obsidian is optional viewer over same Markdown tree."
next_action: "Verified baseline; reference in onboarding."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-159
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:16:00-00:16:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should enable Gmail inbox auto-response using wiki and calendar context without explicit per-email approval."
verbatim_excerpt: "skim my entire inbox and look for emails that you can respond to based on what's on my calendar and what's in my Wiki"
implied_assumption: "Autonomous email drafting from personal wiki is safe for enterprise documentation workflows."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-email-automation
related_second_brain_principles:
  - approval_gated_mutations
  - governance
  - human_review_leverage
expected_benefit: "Email triage automation for busy founders."
possible_regression: "Unreviewed outbound messages; PII exposure; generic Copilot/Gmail scope."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -12
decision: reject
decision_rationale: "Proactive email automation without gates is generic-band and audit-hostile."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-160
source_transcript: raw/platform-transcripts/I_Built_A_Second_Brain_With_Codex_in_15_Minutes_Matt_Wolfe.txt
speaker: Matt Wolfe
timestamp: "00:01:00-00:03:30"
claim_type: architecture_proposal
atomic_claim: "The Karpathy LLM-wiki pattern—save Markdown captures, LLM cross-links them, query with source context—validates Second Brain's raw-to-wiki documentation-compiler architecture."
verbatim_excerpt: "he was experimenting with building, like, this internal wiki... save these Markdown files into Obsidian... the LLM looks at all of the stuff... and sort of cross -links them"
implied_assumption: "Mass-market Karpathy tutorials converge on the same compiler shape Second Brain already implements with governance extensions."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - architecture-rationale
  - product-positioning
related_second_brain_principles:
  - filesystem_first
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "External validation that teachable Karpathy pattern matches product thesis; differentiation is governance layer on top."
possible_regression: "Used to justify skipping authority tags because 'Karpathy did not need them' for personal wikis."
validation_method: "Reference in product positioning; contrast governance extensions vs consumer tutorials."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: adopt
decision_rationale: "Independent practitioner validation of RC-097 three-layer model; Second Brain adds authority, align-cite, and closure."
next_action: "Verified baseline; cite in onboarding vs consumer PKM contrast."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-161
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:03:30-00:05:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain should use explicit hierarchical instruction stacking: root AGENTS.md/CLAUDE.md as constitution plus scoped stage, workstation, or project shims that add rules without duplicating root policy."
verbatim_excerpt: "The root Claude .md file is the constitution... state level laws stack on top... rules in my newsletter HQ workstation only apply when I'm working on my newsletter"
implied_assumption: "Scoped rule files reduce context load while preserving global governance invariants."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve draft ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - .github/prompts/
  - workspace-projects
related_second_brain_principles:
  - filesystem_first
  - governance
  - human_review_leverage
expected_benefit: "Makes existing agent chain and stage directories explicit; prevents Cowork-style life-OS sprawl."
possible_regression: "Deep nesting without routing maps causes agents to miss scoped rules."
validation_method: "Document stacking contract in ADR; verify one multi-stage project loads root + stage shims only."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Maps cleanly to AGENTS.md + workspace agent prompts + stage dirs; adopt documents pattern without Cowork paths."
next_action: "Accepted PIC-009; monitor RC-162/165 experiments that depend on RC-161."
owner: unassigned
status: accepted
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-162
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:07:00-00:07:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain root AGENTS shim should include a routing map table mapping task types to project stages, wiki subtrees, or prompt verbs."
verbatim_excerpt: "The routing map section contains a table that tells co -work which workstation folder to load for which type of task"
implied_assumption: "Explicit task-to-path routing improves inspectable orientation without auto-retrieval."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - .github/prompts/
  - workspace-query
related_second_brain_principles:
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "Reduces mis-routed reads; complements RC-018 retrieval contract and RC-135 agent hub."
possible_regression: "Stale routing tables misdirect agents if not maintained with prompt changes."
validation_method: "Pilot routing section; 5-task holdout for mis-routed compile reads."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "High inspectability upside; needs pilot to avoid duplicating wiki/index navigation."
next_action: "Draft ADR RC-162; merge with RC-018 orientation map pilot."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-163
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:06:30-00:08:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should use a disposable session orientation file (memory.md pattern) for active projects and session notes that is explicitly not wiki canonical truth."
verbatim_excerpt: "memory .md file is like a notepad that stores things co -work should remember between sessions... active projects and work followed by a list of all the active projects"
implied_assumption: "Session orientation can live outside wiki if promotion to canonical knowledge requires compile and align-cite."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - workspace-projects
  - wiki/log.md
related_second_brain_principles:
  - approval_gated_mutations
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Safer resumption than chat-only context; complements RC-058 handoff without wiki pollution."
possible_regression: "Orientation file mistaken for published artifact or canonical standard."
validation_method: "Pilot orientation.md per stage; lint ensures no wiki promotion without compile path."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 9
decision: experiment
decision_rationale: "RC-020 disposable memory class; experiment enforces fail-closed wiki boundary."
next_action: "Draft ADR RC-163; bundle with RC-058 handoff pilot."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-164
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:18:30-00:19:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain should offer an end-of-session audit skill that scans conversation for unsaved preferences and proposes orientation updates only after explicit user approval."
verbatim_excerpt: "whenever I'm done working with a session in cowork, I type forward slash session audit... look for unsaved principles and preferences it needs to remember for next time"
implied_assumption: "Structured session close reduces silent memory drift better than ad hoc remember-this writes."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: unvalidated
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - .github/skills/
  - workspace-projects
  - finalize
related_second_brain_principles:
  - approval_gated_mutations
  - human_review_leverage
  - inspectable_retrieval
expected_benefit: "Captures session learnings with audit trail; safer than RC-169 auto memory writes."
possible_regression: "Skill auto-writes to wiki or orientation without user confirm."
validation_method: "Pilot skill on three sessions; verify zero writes without explicit approval."
impact_scores:
  governance: 2
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 10
decision: experiment
decision_rationale: "Strong governance upside; experiment because skill design must fail closed on wiki writes."
next_action: "Draft ADR RC-164; add optional session-audit skill template."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-165
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:07:30-00:07:30,00:19:30-00:20:00"
claim_type: architecture_proposal
atomic_claim: "Second Brain root AGENTS shims should stay lean (target under ~300 lines) and use pointer references to on-demand resource files instead of inlining all detail."
verbatim_excerpt: "references. These are pointers to files in our root zero zero resources folder that co -work only reads when it needs to... keep your root Claude .md file within 300 lines"
implied_assumption: "Default-loaded instructions should minimize token cost while preserving depth via pointers."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; track in open-hypotheses.md; reject via backlog rollback."
affected_components:
  - AGENTS.md
  - CLAUDE.md
  - .cursor/rules/
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Lower default context load; aligns with RC-018 pointer-based retrieval bundles."
possible_regression: "Over-pointerization hides critical governance rules from default load."
validation_method: "Audit shim line counts; verify critical rules remain in root or mandatory read list."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 2
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 7
decision: experiment
decision_rationale: "Operational hygiene adjacent RC-018; experiment to preserve fail-closed rules in default load."
next_action: "Draft ADR RC-165; audit AGENTS shims after RC-161 ADR."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-166
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:03:00-00:03:30,00:08:30-00:09:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain workspace agents should load voice/identity principles via pointer reference before artifact output, not inline ad hoc tone instructions."
verbatim_excerpt: "read this Jeff's voice principles, markdown file before outputting anything to Jeff... co -work will tell you that the voice principles file has been updated"
implied_assumption: "Structured identity packs reduce tone guessing at compile time."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; cross-link RC-055 ADR; reject via backlog rollback."
affected_components:
  - templates/personas/
  - .github/prompts/workspace-vp-agent.prompt.md
  - .github/prompts/workspace-pm-agent.prompt.md
related_second_brain_principles:
  - human_review_leverage
  - junior_engineer_closure
expected_benefit: "Extends RC-055 with on-demand pointer loading pattern from resources folder."
possible_regression: "Auto-extracted voice profiles from Gmail become canonical without CEO review."
validation_method: "A/B one VP brief with pointer-loaded identity pack vs without."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 9
decision: experiment
decision_rationale: "RC-055 already queued; experiment adds pointer-on-demand loading, rejects Gmail auto-extraction as canonical."
next_action: "Cross-link RC-055 ADR; document pointer pattern in persona template README."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-167
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:16:30-00:17:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain workspace projects should support three-level rule stacking: root AGENTS + stage/workstation shim + optional project subfolder scaffold with local orientation and resources."
verbatim_excerpt: "under my dedicated workstations, I also have project sub folders... Each project gets its own cloud MD memory, MD, and resources folder"
implied_assumption: "Nested project scaffolds improve multi-session work without personal-life workstation sprawl."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve experiment ADR; bundle RC-058/130; reject via backlog rollback."
affected_components:
  - workspace-projects
  - workspace-start-project
related_second_brain_principles:
  - filesystem_first
  - junior_engineer_closure
  - human_review_leverage
expected_benefit: "Operationalizes RC-058 handoff and RC-130 scaffold with explicit rule stacking contract."
possible_regression: "Deep nesting excluded from published set at align-closure; folder sprawl."
validation_method: "Pilot one project with sub-scaffold; verify published artifact set excludes scaffold dirs."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 9
decision: experiment
decision_rationale: "Safer enterprise mapping of Cowork workstation/project nesting; bundle with RC-130 ADR."
next_action: "Draft ADR RC-167; merge with H-2026-05-27-023 scaffold pilot."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-168
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:05:00-00:06:00"
claim_type: product_requirement
atomic_claim: "Second Brain product substrate should be a Claude Cowork personal OS folder with life workstations (Email HQ, personal finances) as the primary architecture."
verbatim_excerpt: "create a folder in your documents and name it co -work OS... Email HQ... personal finances"
implied_assumption: "Consumer personal life OS equals Second Brain north star."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - product-definition
related_second_brain_principles:
  - scope_discipline
  - governance
  - junior_engineer_closure
expected_benefit: "Low-friction personal productivity for creators."
possible_regression: "Abandons governed doc compiler niche for generic personal OS."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -2
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -11
decision: reject
decision_rationale: "Generic-band consumer personal OS; duplicates RC-128 personal PKM rejection."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-169
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:06:30-00:08:00"
claim_type: product_requirement
atomic_claim: "Second Brain should treat agent-written memory.md entries on remember-this commands as durable canonical truth without validation or approval gates."
verbatim_excerpt: "when I say, remember this, write the information to memory .md... co -work has persistent Memory"
implied_assumption: "Session memory writes are equivalent to compiled wiki knowledge."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - wiki/
  - workspace-projects
related_second_brain_principles:
  - approval_gated_mutations
  - citation_grounding
  - source_authority
expected_benefit: "Fast personal recall for Cowork users."
possible_regression: "Ungrounded orientation becomes truth; bypasses align-cite and authority tags."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -2
  grounding: -2
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -14
decision: reject
decision_rationale: "Conflicts with RC-020 disposable memory and fail-closed wiki promotion; RC-163 safer variant only."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-170
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:08:30-00:09:00,00:17:30-00:17:45"
claim_type: product_requirement
atomic_claim: "Second Brain should default to Gmail connector auto-ingestion and thread search for email drafting without per-action approval."
verbatim_excerpt: "connected your co -work to Gmail via connectors... search my Gmail send folder... before drafting any email, search Gmail for existing threads"
implied_assumption: "Email connector access is safe as default workspace capability."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-email-automation
related_second_brain_principles:
  - approval_gated_mutations
  - governance
  - scope_discipline
expected_benefit: "Email context for personal productivity workflows."
possible_regression: "PII ingestion without gates; duplicates RC-159/063 rejections and generic Copilot scope."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -12
decision: reject
decision_rationale: "Auto Gmail ingestion without approval is generic-band and audit-hostile."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-171
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:14:30-00:16:00"
claim_type: product_requirement
atomic_claim: "Second Brain should support bulk credit card statement ingestion and automatic expense classification without explicit approval gates."
verbatim_excerpt: "I share the past 12 months of my credit card statements... cowork read every transaction... built a master spending tracker spreadsheet"
implied_assumption: "Personal finance bulk ingest is in-scope for enterprise documentation compiler."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-finance-ingest
related_second_brain_principles:
  - approval_gated_mutations
  - governance
  - scope_discipline
expected_benefit: "Personal finance tracking for creators."
possible_regression: "Sensitive PII bulk ingest without audit; outside governance-and-closure band."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -2
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -12
decision: reject
decision_rationale: "Personal finance ingestion is consumer personal OS scope; fails approval-gated ingest policy."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-172
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:18:00-00:18:30"
claim_type: product_requirement
atomic_claim: "Second Brain should use Notion as external command center and auto-create project pages with connector-driven property filling."
verbatim_excerpt: "set up a project in notion... cowork knows all of my notion conventions found under my command center, cloud .md, it creates the project page"
implied_assumption: "Notion project substrate is compatible with filesystem-first governed compiler."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - out-of-scope-notion-substrate
related_second_brain_principles:
  - filesystem_first
  - source_authority
  - scope_discipline
expected_benefit: "Notion UX for personal project tracking."
possible_regression: "Duplicates RC-025/RC-131 Notion substrate rejections; splits source of truth."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: -1
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -12
decision: reject
decision_rationale: "Notion command center conflicts with filesystem-first Confluence publish path."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-173
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:10:00-00:10:30"
claim_type: principle_claim
atomic_claim: "Surfacing implied context (writing style, active projects, conventions) in disposable orientation layers improves AI outputs without replacing citation discipline."
verbatim_excerpt: "Implied context is the stuff you inherently know, but forget to tell the AI every time... They remember it for you, so co -work always has the full picture"
implied_assumption: "Orientation layers reduce repeated CEO re-explanation if bounded from wiki truth."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Monitor; re-review when RC-163 orientation pilot completes."
affected_components:
  - workspace-projects
  - templates/personas/
related_second_brain_principles:
  - human_review_leverage
  - inspectable_retrieval
expected_benefit: "Principle supports RC-055/058/163 without Cowork memory-as-truth pattern."
possible_regression: "Confused with RC-169 if orientation promoted to wiki without compile."
validation_method: "Measure restart friction in RC-163 pilot vs baseline."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 5
decision: monitor
decision_rationale: "Principle already partially encoded in RC-058/055; monitor until orientation pilot data exists."
next_action: "Re-review after RC-163 experiment or 2026-08-27."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-174
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:19:30-00:20:30"
claim_type: market_claim
atomic_claim: "Defaulting to Sonnet model plus lean root instructions materially reduces token cost for 80% of Second Brain agent tasks without quality loss."
verbatim_excerpt: "default to the Sonnet model because 80 % of the time Sonnet is more than enough. And it's a fifth of the cost of Opus"
implied_assumption: "Model tier choice is independent of governance requirements for compile and align-cite workloads."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Monitor; re-review when vendor pricing and task-mix benchmarks validated."
affected_components:
  - agent-runtime
  - AGENTS.md
related_second_brain_principles:
  - maintainability
expected_benefit: "Cost hygiene for high-frequency agent sessions."
possible_regression: "Under-powered model on multi-step align-cite or closure checks."
validation_method: "Benchmark Sonnet vs Opus on align-cite holdout when user approves eval."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 0
  maintainability: 1
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 2
decision: monitor
decision_rationale: "Vendor pricing and quality claims unvalidated; lean root (RC-165) separable from model choice."
next_action: "Re-review when Anthropic pricing docs and Second Brain task benchmarks available."
owner: unassigned
status: open
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-05-27-175
source_transcript: raw/platform-transcripts/My_Simple_Claude_Cowork_System_for_normal_people.txt
speaker: Jeff
timestamp: "00:20:30-00:21:00"
claim_type: market_claim
atomic_claim: "Second Brain product mandate should include urgent adoption of a compounding personal-context OS because delayed starts permanently fall behind."
verbatim_excerpt: "you need to start building a system like this today... the rules. The memory, the patterns compound every single session"
implied_assumption: "Consumer personal context compounding equals enterprise documentation compiler urgency."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after."
affected_components:
  - product-definition
related_second_brain_principles:
  - scope_discipline
  - governance
expected_benefit: "Motivational framing for personal AI fluency."
possible_regression: "Scope pressure to ship consumer life-OS features over governance band."
validation_method: "N/A — rejected."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: -2
  enterprise_fit: -2
  human_review_leverage: -1
total_score: -8
decision: reject
decision_rationale: "Marketing urgency for personal OS is not Second Brain product scope; adopt instruction patterns only."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-08-27
owner: unassigned
status: closed
last_reviewed: 2026-05-27
```

```yaml
claim_id: RC-2026-06-09-001
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:00:00-00:01:00"
claim_type: problem_evidence
atomic_claim: "Agent doom loops (repeating broken solutions) are primarily an observability failure over failure trajectories, not raw model incapability."
verbatim_excerpt: "try the exact same broken solution, and then just fail again... break that doom loop"
implied_assumption: "Structured failure context would break repeat-error cycles in Second Brain agent runs."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment pilot on one lint/align failure review; reject via backlog rollback."
affected_components:
  - platform-research-review
  - workspace-lint
related_second_brain_principles:
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "Better root-cause visibility reduces wasted agent iterations."
possible_regression: "Over-engineered trace tooling before failure volume exists."
validation_method: "Pilot structured doom-loop tagging on one advisory failure report."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 0
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 6
decision: experiment
decision_rationale: "Aligns with RC-012 advisory posture; needs pilot before adopt."
next_action: "Link to RC-012 failure-review experiment when failure data exists."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-002
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:02:00-00:02:30"
claim_type: problem_evidence
atomic_claim: "Manual harness debugging does not scale against massive unstructured agent logs (up to millions of tokens per investigation)."
verbatim_excerpt: "sift through up to 10 million tokens of raw, unstructured log data just trying to find a single actionable signal"
implied_assumption: "Second Brain will accumulate enough agent trace volume to require automated distillation."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Re-enter when RC-012 failure-data blocker clears; defer until then."
affected_components:
  - wiki/log.md
  - reports/
related_second_brain_principles:
  - inspectability
  - governance
expected_benefit: "Motivates structured failure reports over raw log dumps."
possible_regression: "Building trace infrastructure before real failures exist."
validation_method: "Defer until lint/align/publish failure corpus available."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 5
decision: defer
decision_rationale: "Useful problem framing but blocked by RC-012 missing failure traces."
next_action: "Re-review when roadmap RC-012 blocker clears."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-003
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:02:30-00:03:00"
claim_type: principle_claim
atomic_claim: "Agent harness improvement is bottlenecked by observability quality, not base model capability."
verbatim_excerpt: "agent evolution isn't actually bottlenecked by agent capability. It's bottlenecked by observability"
implied_assumption: "Second Brain should invest in inspectable failure signals before model-tier upgrades."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Reinforce in platform ADR narrative; approve via implementation backlog if codified."
affected_components:
  - AGENTS.md
  - platform-research-review
related_second_brain_principles:
  - inspectable_retrieval
  - governance
  - human_review_leverage
expected_benefit: "Prioritizes align/lint/reporting over generic model swaps."
possible_regression: "Used to justify autonomy without observability investment."
validation_method: "Cross-check against RC-001 page-index and RC-012 advisory review."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: adopt
decision_rationale: "Strong alignment with verifiability and inspectable retrieval policy; low uncertainty."
next_action: "Reinforce alongside RC-090/012 in platform narrative."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-004
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:03:30-00:04:30"
claim_type: architecture_proposal
atomic_claim: "Platform harness should expose file-typed components (prompts, skills, scripts, shims) with explicit edit action space and VCS revert per component."
verbatim_excerpt: "decouple it into seven distinct component types... every single failure maps cleanly to a single file"
implied_assumption: "Explicit component map improves failure attribution for Second Brain platform ops."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve experiment ADR for component map; reject via backlog rollback."
affected_components:
  - .github/prompts/
  - .github/skills/
  - scripts/
  - AGENTS.md
related_second_brain_principles:
  - inspectability
  - maintainability
expected_benefit: "Faster failure-to-file routing in platform debugging."
possible_regression: "Documentation overhead if map drifts from repo layout."
validation_method: "Publish component map; test on 3 platform failure attributions."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 8
decision: experiment
decision_rationale: "Structure exists implicitly; explicit map is low-risk experiment."
next_action: "Add harness component map to platform-research templates."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-005
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:04:00-00:04:30"
claim_type: workflow_proposal
atomic_claim: "Failure review should distill raw agent traces into structured root-cause summaries before proposing harness changes."
verbatim_excerpt: "agent debugger distills those logs into a layered, drill-down, evidentiary... structured, bite-sized insights"
implied_assumption: "Distilled summaries improve RC-012 advisory failure review quality."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Extend RC-012 experiment; track in open-hypotheses.md."
affected_components:
  - platform-research-review
  - reports/
related_second_brain_principles:
  - inspectability
  - human_review_leverage
expected_benefit: "CEO-readable failure packages instead of raw trace dumps."
possible_regression: "Distillation omits evidence needed for align-cite verification."
validation_method: "One advisory failure report with layered trace summary; CEO rates usefulness."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 2
total_score: 10
decision: experiment
decision_rationale: "Extends RC-012 safely; high inspectability upside with approval gates preserved."
next_action: "Add trace distillation section to RC-012 DRAFT ADR on next PIC cycle."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-006
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:04:30-00:05:00"
claim_type: workflow_proposal
atomic_claim: "Second Brain should run an unattended Evolve-agent loop that autonomously edits and commits harness changes round after round without human approval."
verbatim_excerpt: "an Evolve agent just unattendedly edits and commits changes to the workspace. Round after round"
implied_assumption: "Autonomous harness commits improve Second Brain faster than CEO-gated PIC cycles."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Re-review per rejected-ideas.md next_review_after; safer variant is RC-012 advisory reports only."
affected_components:
  - AGENTS.md
  - .github/prompts/
  - wiki/
related_second_brain_principles:
  - governance
  - approval_gated_mutations
  - human_review_leverage
expected_benefit: "Faster harness iteration on coding benchmarks."
possible_regression: "Silent mutation of Tier-1 rules; audit trail loss; duplicates RC-085/100 rejections."
validation_method: "N/A — rejected."
impact_scores:
  governance: -2
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -1
  enterprise_fit: -2
  human_review_leverage: -2
total_score: -10
decision: reject
decision_rationale: "Violates approval-gated mutations and RC-012 no-auto-mutate posture."
next_action: "Record in rejected-ideas.md."
next_review_after: 2026-09-09
owner: unassigned
status: closed
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-007
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:05:00-00:05:30"
claim_type: evaluation_proposal
atomic_claim: "Platform harness changes should ship with falsifiable change manifests, predicted outcomes, verification commands, and rollback on failed verification."
verbatim_excerpt: "writes a change manifest... self-declared prediction... verifies if that specific file-level edit actually improved... rolls it back"
implied_assumption: "PIC accept/rollback gains explicit falsifiability without autonomous commits."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve DRAFT ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - wiki/platform-research/implementation-backlog.md
  - platform-implement-backlog
related_second_brain_principles:
  - governance
  - inspectability
expected_benefit: "Clearer accept/reject criteria for platform changes."
possible_regression: "Template friction on small PIC items."
validation_method: "Apply manifest to next 3 PIC cycles; measure rollback clarity."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 10
decision: experiment
decision_rationale: "Extends existing PIC loop with verifiable predictions; preserves human gates."
next_action: "Draft ADR RC-2026-06-09-007; add hypothesis to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-008
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:05:30-00:06:30"
claim_type: market_claim
atomic_claim: "A-H-E raised Terminal Bench 2 pass rate from 69.7% to 77.0% in 10 iterations with a fixed GPT-4 base model, outperforming a human-designed Codex harness at 71.9%."
verbatim_excerpt: "10 iterations of AHE lifted the pass rate from 69.7% to a massive 77.0%... crushes the human-designed codex harness, which sits at 71.9%"
implied_assumption: "Benchmark gains transfer to governed documentation compiler workloads."
current_design_status: unsupported
evidence_supplied_by_speaker: data
requires_external_validation: true
validation_status: unvalidated
correction_route: "Monitor; re-review when primary paper and benchmark artifacts validated."
affected_components:
  - out-of-scope-benchmarks
related_second_brain_principles:
  - scope_discipline
expected_benefit: "External evidence that harness tuning beats model swaps on coding tasks."
possible_regression: "Cited in product docs without validation; justifies autonomy scope creep."
validation_method: "Fetch primary paper; reproduce or verify Terminal Bench 2 claim."
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
decision: monitor
decision_rationale: "Unvalidated benchmark from secondary explainer; fail-closed for adopt."
next_action: "Do not cite in canonical docs until validated."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-009
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:06:30-00:07:30"
claim_type: risk_claim
atomic_claim: "Auto-evolving system prompts causes performance regression; Second Brain must forbid autonomous mutation of AGENTS.md, tier-2 shims, and stage prompts."
verbatim_excerpt: "if you let it evolve the system prompt alone, performance actually goes down. It regresses"
implied_assumption: "Code-based tools and scripts are the safe evolution surface; prose instructions require human approval."
current_design_status: partially_supported
evidence_supplied_by_speaker: data
requires_external_validation: false
validation_status: validated_against_design
correction_route: "Approve DRAFT ADR via implementation backlog; ablation cited as motivation only—policy grounded in RC-012/161."
affected_components:
  - AGENTS.md
  - .cursor/rules/agents.mdc
  - CLAUDE.md
  - .github/prompts/
related_second_brain_principles:
  - governance
  - instruction_stacking
  - human_review_leverage
expected_benefit: "Prevents instruction-stack entropy and governance regression."
possible_regression: "Over-constrains legitimate CEO-approved prompt improvements."
validation_method: "Codify policy; verify no autonomous prompt writes outside PIC."
impact_scores:
  governance: 2
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 2
  differentiation: 1
  enterprise_fit: 2
  human_review_leverage: 2
total_score: 12
decision: adopt
decision_rationale: "Strong governance fit; ablation claim unvalidated but policy matches existing RC-012/161 posture—adopt as explicit guardrail not benchmark citation."
next_action: "DRAFT ADR RC-2026-06-09-009; validate ablation when primary paper available."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-010
source_transcript: raw/platform-transcripts/Agentic_AI_Evolution_-_Watching_a_Coding_Agent_Evolve_in_Real-Time.txt
speaker: unknown
timestamp: "00:07:30-00:08:00"
claim_type: principle_claim
atomic_claim: "Applied AI engineer role shifts from builder to evolution overseer with human approval at each harness mutation."
verbatim_excerpt: "Are we no longer builders, but just overseers of evolution?"
implied_assumption: "CEO operator model maps to overseer not autonomous builder."
current_design_status: partially_supported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Monitor; re-review when RC-012/163 pilots complete."
affected_components:
  - workspace agent chain
  - platform-implement-backlog
related_second_brain_principles:
  - human_review_leverage
  - governance
expected_benefit: "Reinforces CEO gates between stages and PIC accept."
possible_regression: "Interpreted as license to remove builder/engineer agent chain."
validation_method: "Compare against RC-093 director accountability; no scope reduction."
impact_scores:
  governance: 1
  closure: 0
  grounding: 1
  vendor_truth: 0
  inspectability: 0
  maintainability: 0
  differentiation: 0
  enterprise_fit: 1
  human_review_leverage: 1
total_score: 4
decision: monitor
decision_rationale: "Already partially encoded in CEO stage gates; monitor until harness review pilot data."
next_action: "Re-review after RC-012 or RC-163 experiment results."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-011
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:02:00-00:02:30"
claim_type: principle_claim
atomic_claim: "Graphify pass-1 deterministic tree-sitter extraction (classes, functions, imports, call graphs) without LLM cost corroborates Second Brain's structure-first page-index retrieval over embedding-first orientation."
verbatim_excerpt: "On the first pass, we are looking at the code structure, and this is completely free... tree sitter parses your code files... This runs locally with no LLM involved."
implied_assumption: "Inspectable hierarchy and explicit connections should be extracted before semantic enrichment."
current_design_status: already_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: validated_against_design
correction_route: "Reinforces RC-001; reject embedding-first orientation via backlog rollback if contradicted."
affected_components:
  - workspace-query
  - docs/architecture-rationale.md
related_second_brain_principles:
  - inspectable_retrieval
  - citation_grounding
expected_benefit: "External corroboration for RC-001 page-index policy when evaluating graph/RAG proposals."
possible_regression: "Misread as mandate to add Graphify or code-graph infrastructure in v1."
validation_method: "Map pass-1 pattern to wiki index + section-tree navigation; no Graphify install required."
impact_scores:
  governance: 1
  closure: 1
  grounding: 2
  vendor_truth: 0
  inspectability: 2
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 9
decision: adopt
decision_rationale: "Aligns with accepted RC-001; Graphify evidence supports structure-before-semantic discipline without adopting the product."
next_action: "No new PIC item; cite as corroboration in retriever heuristic ADR RC-2026-06-09-012."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-012
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:04:00-00:05:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain should document a retriever-selection heuristic: structure-aware page-index or deterministic graphs for wired/hierarchical corpora; holdout-gated embedding GraphRAG only for unstructured cross-document policy corpora."
verbatim_excerpt: "Graphify isn't using any embedding system whatsoever... GraphRAG... is great for something that's more unstructured."
implied_assumption: "Corpus structure determines retriever choice; v1 wiki is predominantly hierarchical Markdown."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Approve DRAFT ADR via implementation backlog; reject via backlog rollback."
affected_components:
  - docs/architecture-rationale.md
  - workspace-query
  - platform-research-review
related_second_brain_principles:
  - inspectable_retrieval
  - source_authority
expected_benefit: "Clearer scope filter when reviewing graph vs RAG transcript claims; prevents IDE-tool scope creep."
possible_regression: "Heuristic misapplied to justify premature embedding adoption without holdout."
validation_method: "Apply table to next three graph/RAG platform reviews; check consistent defer/reject decisions."
impact_scores:
  governance: 1
  closure: 1
  grounding: 1
  vendor_truth: 0
  inspectability: 1
  maintainability: 1
  differentiation: 1
  enterprise_fit: 1
  human_review_leverage: 0
total_score: 7
decision: adopt
decision_rationale: "Codifies implicit RC-001 future-retriever gate into an explicit decision rule without enabling embeddings in v1."
next_action: "DRAFT ADR RC-2026-06-09-012; queue in implementation-backlog after user approval."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-013
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:02:00-00:03:30"
claim_type: workflow_proposal
atomic_claim: "Second Brain compile-time orientation maps should use a three-pass pattern: deterministic wiki structure extraction (zero LLM), optional media text extraction, then LLM semantic enrichment only for unstructured sources—output remains disposable and non-canonical."
verbatim_excerpt: "three different passes... first pass... completely free... second pass... transcribed... third pass on docs, papers, and images... where the large language model actually comes in."
implied_assumption: "Most compile orientation value comes from pass-1 structure; LLM cost should be limited to unstructured inputs."
current_design_status: partially_supported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Approve experiment ADR via backlog; track H-2026-06-09-004; reject via backlog rollback."
affected_components:
  - workspace-compile
  - workspace-query
  - platform-research
related_second_brain_principles:
  - junior_engineer_closure
  - inspectable_retrieval
  - human_review_leverage
expected_benefit: "May reduce blind orientation reads during multi-standard compile without weakening align-cite."
possible_regression: "Orientation map mistaken for canonical truth or align-cite substitute."
validation_method: "Pilot one project: orientation read count and align-cite pass rate vs index-only baseline."
impact_scores:
  governance: 1
  closure: 1
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: -1
  differentiation: 1
  enterprise_fit: 0
  human_review_leverage: 1
total_score: 4
decision: experiment
decision_rationale: "Extends RC-009 safer variant with concrete Graphify-inspired pipeline; worth piloting as disposable draft-tier artifact."
next_action: "DRAFT ADR RC-2026-06-09-013; add H-2026-06-09-004 to open-hypotheses.md."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-014
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:09:30-00:11:00"
claim_type: market_claim
atomic_claim: "In one OpenDesign repo demo, Graphify graph queries used ~80K tokens versus ~200K tokens for explorer-agent file traversal on the same trace question, with equivalent answer quality."
verbatim_excerpt: "about 200,000 tokens total, versus over here on the non -Graphify version, we only used about 80,000. So about 40 % of the total cost"
implied_assumption: "Token savings on code repos transfer to Second Brain wiki compile workloads."
current_design_status: unsupported
evidence_supplied_by_speaker: anecdotal
requires_external_validation: true
validation_status: unvalidated
correction_route: "Monitor; re-review when wiki-orientation pilot produces comparable metrics."
affected_components:
  - platform-research
  - RC-2026-05-27-008
related_second_brain_principles:
  - inspectable_retrieval
expected_benefit: "Anecdotal ROI signal for orientation-map experiments if validated on wiki tasks."
possible_regression: "Product decisions driven by unvalidated codebase token demos."
validation_method: "Reproduce paired task on wiki compile orientation holdout; record token/read counts."
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
decision: monitor
decision_rationale: "Single sponsored demo on a codebase; fail-closed for adopt/experiment until validated on Second Brain workloads."
next_action: "Re-review after RC-013 pilot or RC-008 re-entry."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-015
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:11:30-00:12:00"
claim_type: workflow_proposal
atomic_claim: "Deterministic AST-only graph rebuild on each commit (no LLM API cost) can keep agent orientation maps fresh for living repositories and parallel team edits."
verbatim_excerpt: "graphify hook install, it's gonna auto -rebuild after each commit. And that is the AST only. There's no API cost associated with that."
implied_assumption: "Second Brain needs always-fresh orientation over a frequently mutating repo."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Defer until RC-013 pilot; re-queue via implementation-backlog when orientation infrastructure exists."
affected_components:
  - agent-onboarding
  - platform-implement-backlog
related_second_brain_principles:
  - inspectable_retrieval
  - maintainability
expected_benefit: "Low-cost freshness for disposable orientation artifacts if pilot succeeds."
possible_regression: "Commit hooks create hidden agent dependencies outside approval gates."
validation_method: "After RC-013 pilot, measure stale-orientation incidents with and without incremental refresh."
impact_scores:
  governance: 0
  closure: 0
  grounding: 0
  vendor_truth: 0
  inspectability: 1
  maintainability: 0
  differentiation: 0
  enterprise_fit: 0
  human_review_leverage: 0
total_score: 1
decision: defer
decision_rationale: "Useful only after orientation-map experiment infrastructure exists; Graphify-specific hooks not v1 dependencies."
next_action: "Blocked on RC-2026-06-09-013 experiment outcome."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-016
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:06:30-00:07:30"
claim_type: product_requirement
atomic_claim: "Second Brain should ship Graphify skills and always-on graphify cloud install hooks so IDE agents automatically query a repo knowledge graph every session."
verbatim_excerpt: "Graphify Cloud install, that means it's always going to use Graphify to answer. I don't have to be explicit. It literally becomes a hook."
implied_assumption: "Second Brain's primary users need always-on codebase graph orientation like Claude Code developers."
current_design_status: contradicted
evidence_supplied_by_speaker: example
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Reject; reopen only with explicit code-as-source v2 ADR."
affected_components:
  - agent-onboarding
  - .github/skills
related_second_brain_principles:
  - governance
  - approval_gated_mutations
expected_benefit: "None for v1 governance band."
possible_regression: "Silent agent dependencies on external indexing; bypasses approval gates."
validation_method: "N/A — out of v1 scope per product-brief §1.2 and RC-009a."
impact_scores:
  governance: -1
  closure: 0
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -1
  enterprise_fit: 0
  human_review_leverage: 0
total_score: -5
decision: reject
decision_rationale: "IDE-assistant hook bundling duplicates rejected RC-009a boundary; conflicts with approval-gated platform mutations."
next_action: "Mirror in rejected-ideas.md."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-017
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:09:00-00:09:30"
claim_type: architecture_proposal
atomic_claim: "A pre-built knowledge graph map lets agents answer repository questions accurately without repeated file traversal, reducing the need for source inspection and citation verification on orientation queries."
verbatim_excerpt: "the actual value is the fact that now, we have handed Cloud Code a map to the Open Design repository, and I can now ask questions about it and get accurate responses."
implied_assumption: "Graph traversal accuracy substitutes for align-cite verification."
current_design_status: contradicted
evidence_supplied_by_speaker: anecdotal
requires_external_validation: false
validation_status: supported_by_current_design
correction_route: "Reject; same correction route as RC-2026-05-27-023."
affected_components:
  - workspace-align-cite
  - workspace-query
related_second_brain_principles:
  - citation_grounding
  - junior_engineer_closure
expected_benefit: "None — weakens core differentiator."
possible_regression: "Published artifacts cite graph summaries instead of verified sources."
validation_method: "N/A — conflicts with RC-002 retrieved-context-is-not-citation-support."
impact_scores:
  governance: -2
  closure: -1
  grounding: -2
  vendor_truth: 0
  inspectability: -1
  maintainability: 0
  differentiation: -2
  enterprise_fit: 0
  human_review_leverage: -1
total_score: -9
decision: reject
decision_rationale: "Directly conflicts with citation-grounded query and align-cite; same failure mode as rejected hot-cache orientation claims."
next_action: "Mirror in rejected-ideas.md."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```

```yaml
claim_id: RC-2026-06-09-018
source_transcript: raw/platform-transcripts/This_Open_Source_Repo_Just_Solved_Claude_Code_s_1_Problem.txt
speaker: unknown
timestamp: "00:00:30-00:03:30"
claim_type: architecture_proposal
atomic_claim: "Second Brain v1 should index raw/workspace-confluence and mixed media via Graphify's full three-pass pipeline (AST + Whisper transcription + LLM semantic docs) as the primary retrieval substrate."
verbatim_excerpt: "it allows your AI coding assistant... to map your entire project, code, docs, PDF images, and videos into a knowledge graph that you can query instead of gripping through the files."
implied_assumption: "Second Brain v1 retrieval should mirror IDE codebase assistants."
current_design_status: unsupported
evidence_supplied_by_speaker: example
requires_external_validation: true
validation_status: unvalidated
correction_route: "Reject; reopen only with code-as-source v2 ADR."
affected_components:
  - workspace-query
  - workspace-compile
  - raw/workspace-confluence
related_second_brain_principles:
  - inspectable_retrieval
  - source_authority
expected_benefit: "None for v1 governance band."
possible_regression: "Duplicates Sourcegraph/Cody scope; bypasses page-index and compile approval gates."
validation_method: "N/A — rejected per RC-009a boundary."
impact_scores:
  governance: -1
  closure: -1
  grounding: -1
  vendor_truth: 0
  inspectability: -1
  maintainability: -1
  differentiation: -2
  enterprise_fit: 0
  human_review_leverage: 0
total_score: -7
decision: reject
decision_rationale: "Full Graphify-style indexing over workspace raw sources is RC-009a-class scope creep into IDE codebase assistants."
next_action: "Mirror in rejected-ideas.md."
owner: unassigned
status: open
last_reviewed: 2026-06-09
```
