# Example: Strategy Synthesis Across Teams

A common CEO query pattern: synthesize current commitments from multiple teams to ground a strategic decision or external communication.

## Scenario

The CEO is preparing for a board meeting and needs to summarize the org's current commitments around data security and access control across the Security, Audit, and Engineering teams.

## Invocation

```
/workspace-query "What are our current commitments and standards around data security and access control across the Security, Audit, and Engineering teams? Cite specific standards." --file-back
```

## Expected agent behavior

1. Read `wiki/index.md` and identify articles in `wiki/workspace-standards/security/`, `wiki/workspace-standards/audit/`, and `wiki/workspace-standards/engineering/` that touch the question
2. Read each in full
3. Synthesize an answer that:
   - Lists each team's published commitments at standard authority
   - Identifies overlap, gaps, and contradictions across teams
   - Cites every claim to its specific standard (with section anchor where possible)
   - Flags any standard that depends on stale vendor docs (and offers to refresh)
4. With `--file-back`: persist the synthesis as `wiki/workspace-qa/data-security-and-access-control-commitments-{date}.md`
5. Update `wiki/index.md` and `wiki/log.md`

## Expected output shape

```markdown
# Q: What are our current commitments around data security and access control?

## Answer

### Security team commitments

[Synthesized from wiki/workspace-standards/security/* with citations]

### Audit team commitments

[Synthesized from wiki/workspace-standards/audit/* with citations]

### Engineering team commitments

[Synthesized from wiki/workspace-standards/engineering/* with citations]

### Overlaps, gaps, and conflicts

- **Overlap:** {area where multiple teams have aligned commitments}
- **Gap:** {area where no team has clear commitment}
- **Conflict:** {area where teams disagree; with citation to each}

## Sources Consulted

- [{standard 1}]({wiki path}) - Security team
- ...

## Follow-Up Questions

- [Open questions raised by the synthesis]
```

## After the synthesis is filed

The filed `wiki/workspace-qa/` article becomes available for future queries. The next time this question (or a related one) is asked, the LLM can read the existing synthesis instead of re-deriving.

## When the answer is partial

If the synthesis cannot be complete (e.g., the Audit team's standards are not yet ingested), the agent reports gaps explicitly and offers remediation: "I cannot answer the Audit portion without ingesting the Audit space. Run `/workspace-ingest-confluence AUDIT` to populate it, then re-query."
