# Setup Kit

**Status:** v1.0
**Last updated:** 2026-04-28

Step-by-step adoption guide for a new user setting up Second Brain on their machine. Target: a new user can complete setup in under 30 minutes assuming Atlassian credentials are available.

## Prerequisites

- Windows, macOS, or Linux
- VS Code installed
- GitHub Copilot extension installed and authenticated (or Claude Code, Cursor, or Windsurf)
- Obsidian installed (download from obsidian.md, free)
- Python 3.12+ for `verify-setup.py` and any helper scripts
- `defuddle` CLI: `npm install -g defuddle` (for vendor doc fetching)
- Git
- An Atlassian Cloud account with API token or OAuth credentials and read access to the Confluence spaces you intend to ingest

## Step-by-step

### 1. Clone the repo

```bash
git clone <repo-url> second-brain
cd second-brain
```

### 2. Configure credentials

```bash
cp .env.example .env
```

Open `.env` in your editor and fill in:

- `ATLASSIAN_SITE_URL` (e.g., `https://yourcompany.atlassian.net`, no trailing slash)
- `ATLASSIAN_EMAIL` (your account email)
- `ATLASSIAN_API_TOKEN` (from `id.atlassian.com/manage-profile/security/api-tokens`)

If your tenant requires OAuth instead of personal tokens, fill the OAuth fields and leave the API token blank.

### 3. Verify setup

```bash
python scripts/verify-setup.py
```

This validates `.env`, tests Atlassian connectivity, creates required runtime directories (`raw/`, `wiki/`, `confluence-review/`, `quarantine/`, `reports/`), and initializes empty `wiki/index.md` and `wiki/log.md`.

If the script reports failures, address them before continuing. Common failures and fixes:

- **Auth fails:** verify your API token is current; verify the tenant URL has no trailing slash; if your tenant disables personal tokens, switch to OAuth.
- **IP allowlisted:** your tenant may restrict API access to specific IPs. Confirm with your Atlassian admin.
- **Atlassian Guard / SSO:** OAuth respects SSO; personal tokens may not. Use OAuth if SSO is required.
- **Audit logging:** Enterprise Cloud generates audit log entries for every API call. Give your security team a heads-up before first ingest of large spaces.

### 4. Open in VS Code

```bash
code .
```

Ensure GitHub Copilot agent mode is enabled and points to a current Claude or GPT model.

### 5. Open in Obsidian

Open Obsidian → "Open another vault" → select the `second-brain` folder.

The bundled `.obsidian/` config opens to `wiki/index.md`. Initially, the index is empty; it populates after your first ingest.

### 6. Run onboarding

In Copilot chat, invoke the onboarding prompt:

```
/second-brain
```

(Or open `.github/prompts/second-brain.prompt.md` and run as a prompt file if your version of Copilot does not auto-discover slash commands.)

The conversation walks you through:

- Confirming your Atlassian tenant
- Listing default in-scope Confluence spaces with authority and domain mappings
- Persisting your choices to `config/second-brain.yml`
- Optionally creating your first project and running an initial ingest

### 7. First ingest (if not done in onboarding)

```
/ingest-confluence
```

Provide a Confluence space key, page URL, or page ID list. The agent fetches, converts, compiles, and reports a manifest. The wiki layer populates.

### 8. First project (if not done in onboarding)

```
/start-project
```

The agent walks you through declaring intent, then orchestrates the chain: VP Agent → PM Agent → Architect Agent (if technical) → Engineer Agent → finalize. You review and edit between stages.

### 9. First publish

After the agent chain produces artifacts and the finalize step transitions them to status `review`:

```
/publish
```

Choose `review` for an HTML preview (opens the `confluence-review/` folder); choose `confluence` for actual API push.

### Optional: Research review

Use this when transcripts, interviews, meeting notes, or product-improvement discussions contain claims about how Second Brain should evolve:

```text
/research-review
```

Place live transcripts under `raw/transcripts/{slug}/transcript.md`. The workflow writes product-intelligence artifacts under `wiki/research/` and `reports/research-review/`, and may draft ADRs under `docs/decision-records/`. It does not directly edit canonical standards, `PRD.md`, `product-brief.md`, `docs/roadmap.md`, `docs/architecture-rationale.md`, or `AGENTS.md`.

## Per-agent setup variants

### GitHub Copilot (VS Code) — primary v1 surface

- Already covered above
- Copilot reads `.github/copilot-instructions.md` automatically

### Claude Code

- Claude Code reads `CLAUDE.md` and `AGENTS.md` natively at the repo root
- Authentication uses your Claude subscription credentials in `~/.claude/.credentials.json`
- No additional setup needed beyond the standard Claude Code installation

### Cursor

- Cursor reads `.cursor/rules/agents.mdc` (already in place)
- Note: this shim is provided but not formally tested in v1; please open an issue if behavior diverges

### Windsurf

- Windsurf reads `.windsurfrules` (already in place)
- Same note as Cursor

## Common gotchas

- **Markdown rendering:** if Obsidian shows broken wikilinks, ensure the file paths in your wiki articles are correct. Use the `obsidian-markdown` skill (or invoke compile to regenerate).
- **`defuddle` not found:** install with `npm install -g defuddle`. Verify with `defuddle --version`.
- **Vendor fetches fail:** the vendor's site may have dynamic JavaScript that breaks defuddle. Try `defuddle parse {URL} --md` directly to debug.
- **Confluence rate limits:** Atlassian Cloud rate-limits per token. If a large ingest hits 429s, the agent backs off; for very large spaces, ingest in batches.
- **Permission changes:** if a Confluence page becomes inaccessible after ingest, the cached `raw/` copy remains; the user's permissions are checked at fetch time, not query time. Run `/lint` to detect stale references.

## When you finish setup

Run `/lint` to verify the wiki is in a clean state. Browse `wiki/index.md` in Obsidian. Read `PRD.md` and `AGENTS.md` to deepen your understanding of how the system operates.

If you are adopting Second Brain for a non-CEO operator persona, consult `templates/personas/{your-persona}/` for persona-specific tailoring (note: only `ceo/` is fully populated in v1; other personas have stubs that v1.x will fill in).
