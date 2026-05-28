# Open Research Hypotheses

Use this file to track unresolved ideas from transcript review that are not yet ready for adoption.

| Hypothesis ID | Source Claim | Hypothesis | Validation Method | Status | Owner |
|---|---|---|---|---|---|
| H-2026-05-27-001 | RC-2026-05-27-003 | A monthly platform gap-review loop can find useful source candidates without polluting canonical docs. | Prompt live at `.github/prompts/platform-research-review/gap-review.prompt.md`; run one cycle; measure user acceptance of candidates. | active | unassigned |
| H-2026-05-27-002 | RC-2026-05-27-007 | A disposable Markdown-derived graph report can improve relationship review without becoming source truth. | Deferred: user prefers Obsidian graph. Re-enter if Obsidian/Bases insufficient. | deferred | unassigned |
| H-2026-05-27-003 | RC-2026-05-27-008 | A session-start graph summary can reduce repeated orientation reads for agents. | Deferred with RC-007. Obsidian graph preferred for now. | deferred | unassigned |
| H-2026-05-27-004 | RC-2026-05-27-012 | Harness-failure traces can produce better prompt/rule improvement proposals than ad hoc prompt edits. | After several real failures, produce an advisory failure-review report and route changes through draft ADRs. | open | unassigned |
| H-2026-05-27-005 | RC-2026-05-27-015 | Lightweight intent and safety records improve platform auditability without adding compliance bloat. | Template live in `templates/platform-research/platform-adr.md`; measure clarity on the next three platform ADRs. | active | unassigned |
| H-2026-05-27-006 | RC-2026-05-27-011 | A local weekly digest from `wiki/log.md` could improve follow-through after core v1 workflows are used. | Defer until pilot data exists; test a no-telemetry digest from local logs only. | deferred | unassigned |
| H-2026-05-27-007 | RC-2026-05-27-050 | Verbatim excerpts in align-cite reports improve verification speed without weakening closure. | Pilot optional excerpt blocks on one published-bound artifact. | open | unassigned |
| H-2026-05-27-008 | RC-2026-05-27-055 | Mandatory identity packs before workspace agent stages reduce CEO edit burden on voice/tone. | A/B one VP brief with identity pack loaded vs not. | open | unassigned |
| H-2026-05-27-009 | RC-2026-05-27-058 | Stage-level handoff.md files improve multi-session project resumption vs chat-only context. | Template live at `templates/workspace/handoff.md`; pilot one project across two sessions. | active | unassigned |
| H-2026-05-27-007 | RC-2026-05-27-067 | Path-scoped compile hints tied to `config/second-brain.yml` improve citation precision before publish. | Pilot on one workspace project; compare align-cite pass rate vs baseline. | open | unassigned |
| H-2026-05-27-008 | RC-2026-05-27-070 | CI/programmatic align+lint without terminal sessions improves pre-publish validation. | One CI job emitting reports only; no autonomous wiki writes. | open | unassigned |
| H-2026-05-27-009 | RC-2026-05-27-079 | Structured decision snippets appended to `wiki/log.md` on publish/align improve auditability. | Template + 3 pilot events; reviewer rates traceability. | open | unassigned |
| H-2026-05-27-007 | RC-2026-05-27-020 | Session/orientation memory must stay disposable; unvalidated agent inferences must not write to durable wiki. | Spec fail-closed memory classes; lint for inference write-back without validation_status. | open | unassigned |
| H-2026-05-27-008 | RC-2026-05-27-023, RC-2026-05-27-050 | Metadata index + wikilink traversal improve compile-time scoping vs full-vault reads. | Merge with RC-009 orientation map; holdout citation precision test. | open | unassigned |
| H-2026-05-27-009 | RC-2026-05-27-057 | Domain-scoped query guardrails reduce unsafe out-of-scope synthesis. | Red-team workspace-query; spec scope schema in experiment ADR. | open | unassigned |
| H-2026-05-27-010 | RC-2026-05-27-059, RC-2026-05-27-060 | Convention-discovery bootstrap and lifecycle hooks align IDE agents with approval-gated mutations. | Advisory-only /init diff; hook requires explicit user confirm before commit/publish. | open | unassigned |
| H-2026-05-27-011 | RC-2026-05-27-083 | Scoped nested ROUTING.md files per wiki subtree improve agent compile-time scoping. | One project pilot; 5-task holdout for mis-routed reads. | open | unassigned |
| H-2026-05-27-012 | RC-2026-05-27-094 | Agent-native copy-paste setup skills reduce time-to-first compile vs URL-first docs. | Pilot setup-kit block; measure agent-only fresh-clone setup. | open | unassigned |
| H-2026-05-27-013 | RC-2026-05-27-102 | Moving compiled sources to raw/processed/ improves orphan-source lint clarity. | One ingest batch pilot; compare workspace-lint orphan counts. | open | unassigned |
| H-2026-05-27-007 | RC-2026-05-27-019 | Scheduled wiki lint (contradictions, stale, orphans) improves publish closure pass rate. | Run biweekly wiki lint on pilot; compare align-closure outcomes. | open | unassigned |
| H-2026-05-27-008 | RC-2026-05-27-055 | Materials vs notes capture taxonomy improves align-cite at publish. | Pilot frontmatter tags on one ingest path. | open | unassigned |
| H-2026-05-27-009 | RC-2026-05-27-063 | Monthly wiki health check (report-only phase 1) catches closure drift. | Run one manual health check; compare with workspace-lint. | open | unassigned |
| H-2026-05-27-020 | RC-2026-05-27-142 | Weekly command-center pulse as disposable report (not wiki truth). | Generate one pulse from log+lint; verify no wiki writes. | open | unassigned |
| H-2026-05-27-021 | RC-2026-05-27-116 | Thinking vs artifact mode frontmatter reduces premature publish-shaped output in draft stages. | Pilot agent_mode on one draft project; count slop fragments. | active | unassigned |
| H-2026-05-27-022 | RC-2026-05-27-117 | Thinking-partner sub-agent improves PM requirements before Engineer handoff. | A/B one PM stage with thinking-partner vs without. | active | unassigned |
| H-2026-05-27-023 | RC-2026-05-27-118, RC-119, RC-130 | Project stage scaffold + daily progress enables catch-up resumption. | Template live; pilot one project two weeks. | active | unassigned |
| H-2026-05-27-024 | RC-2026-05-27-122 | Explicit read-before-write in workspace prompts reduces uncited generation. | Log read lists before first write in three agent runs. | open | unassigned |
| H-2026-05-27-014 | RC-2026-05-27-107 | Governed tool-assembly map in onboarding reduces consumer-agent misconfiguration. | Add assembly diagram to second-brain prompt; measure time-to-first compile. | open | unassigned |
| H-2026-05-27-015 | RC-2026-05-27-112 | Offline lint+align report bundle supports edge deployment without messaging agents. | One air-gapped pilot; no wiki writes. | open | unassigned |
| H-2026-05-27-016 | RC-2026-05-27-114 | Per-verb mutation approval matrix reduces silent raw/wiki changes. | Publish matrix; pilot ingest+compile with explicit gates. | open | unassigned |
| H-2026-05-27-014 | RC-2026-05-27-135 | Generated agent hub index from prompts/skills/index improves compile orientation. | Pilot hub artifact; count orientation reads on 5 compile tasks. | open | unassigned |
| H-2026-05-27-015 | RC-2026-05-27-136 | Specialist sub-agent registry with mode routing improves stage handoffs. | Document registry schema; pilot one workspace project chain. | open | unassigned |
| H-2026-05-27-016 | RC-2026-05-27-138 | Generated path/schema map reduces mis-routed agent writes. | Merge RC-018 pilot; 5-task holdout. | open | unassigned |
| H-2026-05-27-017 | RC-2026-05-27-139 | Internal vs external capture_lane frontmatter improves compile routing. | Pilot on one ingest batch; align-vendor-truth check. | open | unassigned |
| H-2026-05-27-018 | RC-2026-05-27-140 | Dedicated raw/workspace-meetings/ lane with compile gate preserves evidence separation. | One meeting ingest pilot with approval checkpoint. | open | unassigned |
| H-2026-05-27-019 | RC-2026-05-27-141 | Controlled tag vocabulary in config improves scoped query without vectors. | 10-question holdout vs untagged baseline. | open | unassigned |
| H-2026-05-27-020 | RC-2026-05-27-142 | Weekly disposable pulse report from log+lint improves CEO orientation without wiki writes. | Generate one report; verify zero wiki mutation. | open | unassigned |
| H-2026-05-27-025 | RC-2026-05-27-162 | Task-type routing map in AGENTS shim reduces mis-routed compile reads. | 5-task holdout vs baseline; merge RC-018 orientation map. | active | unassigned |
| H-2026-05-27-026 | RC-2026-05-27-163 | Disposable orientation.md per stage improves resumption without wiki promotion. | Pilot two weeks; lint blocks wiki writes without compile. | active | unassigned |
| H-2026-05-27-027 | RC-2026-05-27-164 | Session audit skill captures preferences with explicit approval only. | Three sessions; zero unapproved writes. | active | unassigned |
| H-2026-05-27-028 | RC-2026-05-27-165 | Lean root shims with pointer resources reduce default context load. | Line audit; mandatory rules remain in default load. | active | unassigned |
| H-2026-05-27-029 | RC-2026-05-27-167 | Three-level rule stack with project sub-scaffolds supports RC-058/130. | One pilot; align-closure excludes scaffolds from publish set. | active | unassigned |
| H-2026-05-27-025 | RC-2026-05-27-146 | Explicit raw inbox staging with approval-gated compile preserves Karpathy clipper UX without nightly automation. | One ingest batch pilot; compile only after explicit user approval. | active | unassigned |
| H-2026-05-27-026 | RC-2026-05-27-148 | Topic/entity compile from immutable raw with mandatory Sources improves navigation without graph substrate. | One Confluence compile pilot; align-cite on all new links. | active | unassigned |
| H-2026-05-27-027 | RC-2026-05-27-149 | Duplicate source URL check before compile reduces raw noise without skipping versioned re-ingest. | Pilot dedup rule; measure false positives on version-changed sources. | open | unassigned |
