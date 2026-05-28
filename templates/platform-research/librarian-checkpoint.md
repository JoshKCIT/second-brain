# Librarian Checkpoint (agent → user)

Copy this block into chat when the transcript librarian must pause for a human decision.

```markdown
## Checkpoint {H1|H2|H3|H4|H5|H6|H7|H8|H9}: {short title}

**Context:** {one sentence — what you were doing}

**Need:** {what decision or input is required}

**Proposal** (if applicable):
- Slug: `{slug}`
- Path: `raw/platform-transcripts/{path}`
- Title: {title}

**Options:**
1. {option A}
2. {option B}
3. {option C — e.g. skip / defer}

Reply with the option number, a slug/title correction, or new instructions. I will not continue until you respond.
```

## Checkpoint reference

| ID | Use when |
|----|----------|
| H1 | Before writing to `raw/**` |
| H2 | Slug or title unclear |
| H3 | Duplicate or near-duplicate |
| H4 | Poor transcription quality |
| H5 | Missing file or URL |
| H6 | Batch processing |
| H7 | After each review — continue? |
| H8 | Script failure |
| H9 | External validation blocked |
