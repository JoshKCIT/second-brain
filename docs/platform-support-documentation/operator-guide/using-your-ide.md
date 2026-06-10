---
title: "Using your IDE"
audience: operator
generated: true
last_sync: 2026-06-10T20:00:00Z
status: published
sources:
  - "README.md"
  - ".github/copilot-instructions.md"
  - "CLAUDE.md"
  - ".cursor/rules/agents.mdc"
---

# Using your IDE

Second Brain is **IDE-agnostic**. Prompts live in `.github/prompts/`; each IDE reads a shim that points agents to [AGENTS.md](../../../AGENTS.md). Invoke operations in agent chat — not by editing wiki by hand for routine work.

## Copilot

**Primary v1 surface:** VS Code + GitHub Copilot.

1. Open repo root in VS Code
2. Enable Copilot **agent mode** with a current model
3. Type `/second-brain`, `/workspace-query`, etc. in chat
4. Copilot loads [.github/copilot-instructions.md](../../../.github/copilot-instructions.md) automatically

If slash commands are not discovered, open the matching `.github/prompts/{name}.prompt.md` file and run as a prompt file.

## Cursor

1. Open repo in Cursor
2. Agent reads [.cursor/rules/agents.mdc](../../../.cursor/rules/agents.mdc)
3. Use the same slash command names in Cursor agent chat
4. Routing table: [templates/workspace/routing-map.md](../../../templates/workspace/routing-map.md)

Cursor shim is provided; report behavioral differences vs Copilot via issues.

## Claude Code

1. Install Claude Code CLI; clone repo
2. Claude reads [CLAUDE.md](../../../CLAUDE.md) and AGENTS.md at root
3. Invoke the same verb names in conversation
4. Auth: Claude subscription credentials in `~/.claude/.credentials.json`

No extra repo setup beyond standard clone and verify-setup.

## Windsurf

1. Open repo in Windsurf
2. Agent reads [.windsurfrules](../../../.windsurfrules)
3. Same verb vocabulary as other IDEs

Treat as best-effort parity with Copilot until formally tested.

## Prompt discovery

| Method | When |
|--------|------|
| Slash command in chat | IDE discovers `.github/prompts/*.prompt.md` |
| Open prompt file directly | Slash commands unavailable |
| Routing map | Find task → invoke → read-first paths |
| [verb-reference.md](verb-reference.md) | When / Approve / Outputs per verb |
| [feature-catalog.md](feature-catalog.md) | Complete capability index |

All prompts declare `inherits: AGENTS.md` — Tier-1 rules cannot be overridden by prompt text.

### Troubleshooting invocation

| Symptom | Fix |
|---------|-----|
| Slash command not found | Open `.github/prompts/{verb}.prompt.md` directly |
| Agent ignores approval gate | Quote RC-146; stop session; revert wiki diff |
| Wrong lane behavior | Cite routing-map row; clarify workspace vs platform |
| Stale agent context | Start new chat; point to `handoff.md` or support doc page |

### Multi-IDE teams

Teams may mix Copilot, Cursor, and Claude Code on the same repo. Verb names and prompt files are shared — only the shim file differs. Document your team's chosen IDE in internal runbooks; support docs stay IDE-neutral.

## See Also

- [getting-started.md](../user-guide/getting-started.md)
- [everyday-workflows.md](../user-guide/everyday-workflows.md)
- [troubleshooting.md](../user-guide/troubleshooting.md)

## Sources consulted

- README.md, copilot-instructions.md, CLAUDE.md, agents.mdc
