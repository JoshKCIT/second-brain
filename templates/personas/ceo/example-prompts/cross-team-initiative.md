# Example: Cross-Team Strategic Initiative

A common CEO workflow: launch a strategic initiative requiring coordination and documentation across multiple teams.

## Scenario

The CEO is launching a customer-data-platform replatform initiative that touches Architecture, Security, Audit, Data Modeling, and Snowflake teams' published standards. The initiative needs full documentation that aligns with all in-scope standards and is executable by junior engineers across the involved teams.

## Workflow

### Step 1: Start the project

```
/start-project
```

Declare intent:

- Project name: `customer-data-platform-replatform`
- Description: "Replatform customer data warehouse from on-prem to cloud-native architecture using Snowflake, with full audit and security coverage"
- Business outcome: "Reduce data platform operational cost by 40%; meet new compliance requirements; enable real-time analytics use cases"
- Technical: yes
- Concerns: cross-team alignment, vendor capability validation, jr-engineer executability of resulting docs

### Step 2: Confirm broader in-scope spaces

When the CEO is asked about in-scope spaces, extend beyond the defaults:

- ARCH (Architecture)
- SEC (Security)
- AUDIT (Audit)
- DATA (Data Modeling)
- Plus a project-specific space if one exists for the initiative

The project's `meta.yml` records these.

### Step 3: VP Agent stage

The VP brief frames the strategic intent: why replatform, what changes, business outcome, top constraints (cost ceiling, compliance, timeline). Stakeholders include the affected teams' VPs.

### Step 4: PM Agent stage

The PRD elaborates:

- User personas affected (data analysts, app teams consuming data, audit reviewers)
- Functional requirements (workloads supported, query latency targets, data freshness SLAs)
- Non-functional requirements (cost ceiling, encryption at rest/in transit, retention policy, audit trail)
- Cited standards from each in-scope team

### Step 5: Architect Agent stage

The architecture doc compares 2-3 candidate approaches:

- Approach A: Lift-and-shift to Snowflake with minimal restructure
- Approach B: Re-architect with a new data model and Snowflake-native patterns
- Approach C: Hybrid (lift critical workloads first; restructure incrementally)

Each approach is evaluated against the cited standards. Vendor capability claims (e.g., "Snowflake supports zero-copy clones") are verified against fresh Snowflake docs.

ADRs are generated for major decisions (e.g., "ADR-0001: Choice of data modeling pattern", "ADR-0002: Authentication architecture").

### Step 6: Engineer Agent stage

Decomposed engineering specs:

- `04-engineering/overview.md` (roadmap, components, sequencing)
- `04-engineering/ingestion-pipeline.md` (per the data modeling standard)
- `04-engineering/security-controls.md` (per the Security standard)
- `04-engineering/audit-and-retention.md` (per the Audit standard)
- `04-engineering/snowflake-configuration.md` (per Snowflake docs)
- `04-engineering/testing-plan.md`
- `04-engineering/deployment.md`

Each spec is jr-engineer-executable: standards' rules inlined; vendor citations parenthetical-plus-See-Also.

### Step 7: Finalize

The Engineer Agent runs the finalize step on every artifact in the project. Body wikilinks are removed; navigation moves to See Also; status transitions to `review`.

### Step 8: Pre-publish align gates

```
/align-cite
/align-vendor-truth
/align-closure
```

All three should pass. If `align-coverage` is invoked (advisory), it surfaces any standard requirements not addressed.

### Step 9: Publish

Publish to Confluence under the initiative's project space. Each engineering spec becomes a Confluence page; the affected teams can review and comment in Confluence.

### Step 10: Cross-team review cycle

After Confluence publication, the affected teams review and provide feedback. The CEO operator pulls comments back into the wiki via re-ingest if needed; updates flow back through the agent chain on the next cycle.

### Step 11: Project closeout

When the implementation is delivered:

- Update each artifact to reflect what was actually built (if it diverged from spec)
- Run a final `/align-cite` and `/align-closure`
- Archive: `/archive wiki/projects/customer-data-platform-replatform/`
- The archived project's content stays on disk (gitignored locally) for future audit

## Notes

- This workflow demonstrates the full agent chain. Smaller initiatives may skip the Architect stage (non-technical) or use only a single Engineer Agent output rather than decomposed specs.
- The cross-project rule means future projects can reference this one's published artifacts (e.g., "per the customer-data-platform replatform's Snowflake configuration standard..."). Future projects cannot reference it while it is `in-progress`.
