# .github/hooks/

Hook configurations ported from awesome-copilot. Each hook is a folder containing a `README.md` with installation and configuration details and a `hooks.json` with event triggers.

## Critical: Copilot compatibility verification needed

These hooks target the GitHub Copilot coding-agent session model and use events: `sessionStart`, `sessionEnd`, `userPromptSubmitted`, `preToolUse`, `postToolUse`, `errorOccurred`.

Our primary workflow is prompt-file invocations from Copilot chat (`/start-project`, `/ingest-confluence`, etc.), which may or may not fire the same events depending on Copilot's current session model. Before relying on any hook in production:

1. Verify the hook actually fires when expected during our prompt-driven workflow
2. Test with a small repo and observe whether `sessionEnd` and other events trigger
3. Adjust if the events do not align (consider adapting to a Python script invoked via prompt instead of a hook, or wait until Copilot's hook model evolves)

## Ported hooks

| Hook | Purpose | Events | Status |
|---|---|---|---|
| `secrets-scanner/` | Scan modified files at session end for leaked secrets, credentials, API keys, private keys, connection strings | `sessionEnd` | Ported; verify Copilot trigger before relying |
| `tool-guardian/` | Block dangerous tool operations at preToolUse (rm -rf, git push --force, DROP TABLE, chmod 777, etc.) | `preToolUse` | Ported; verify Copilot trigger |
| `session-logger/` | Log session activity (start, end, user prompts) for audit and analysis | `sessionStart`, `sessionEnd`, `userPromptSubmitted` | Ported; needs adaptation to write to `wiki/log.md` in our structured format |
| `governance-audit/` | Scan prompts for threat signals; log governance events | `sessionStart`, `sessionEnd`, `userPromptSubmitted` | Ported; optional v1.x activation |

## Installation per hook

Each hook folder includes its own `README.md` with installation steps. Generally:

1. Ensure the hook scripts are executable: `chmod +x .github/hooks/{hook-name}/*.sh`
2. Reference the hook's `hooks.json` from your Copilot configuration (placement varies by Copilot version)
3. Test in a sandbox repo before enabling in active work

## Adaptation needs

`session-logger` writes to a generic logs directory by default. Adapt to write to `wiki/log.md` in the structured format documented in `AGENTS.md`:

```
## [{ISO timestamp}] {operation} | {description}
- {detail}
```

This adaptation is queued for build week 1.

## Build-week-1 verification checklist

Before declaring hooks operational:

- [ ] `secrets-scanner` fires at `sessionEnd` and catches a planted test secret
- [ ] `tool-guardian` blocks a planted destructive command at `preToolUse`
- [ ] `session-logger` writes to `wiki/log.md` (after adaptation) on session start and end
- [ ] `governance-audit` is verified or explicitly deferred to v1.x
