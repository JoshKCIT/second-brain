#!/bin/bash

# Governance Audit: Log session start with governance context

set -euo pipefail

if [[ "${SKIP_GOVERNANCE_AUDIT:-}" == "true" ]]; then
  exit 0
fi

INPUT=$(cat)

mkdir -p logs/copilot/governance

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
source "$SCRIPT_DIR/common.sh"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
CWD=$(pwd)
LEVEL="${GOVERNANCE_LEVEL:-standard}"
AUDIT_LOG="logs/copilot/governance/audit.log"

if have_jq; then
  jq -Rn \
    --arg timestamp "$TIMESTAMP" \
    --arg cwd "$CWD" \
    --arg level "$LEVEL" \
    '{"timestamp":$timestamp,"event":"session_start","governance_level":$level,"cwd":$cwd}' \
    >> "$AUDIT_LOG"
else
  printf '{"timestamp":"%s","event":"session_start","governance_level":"%s","cwd":"%s"}\n' \
    "$(json_escape "$TIMESTAMP")" "$(json_escape "$LEVEL")" "$(json_escape "$CWD")" \
    >> "$AUDIT_LOG"
fi

echo "🛡️ Governance audit active (level: $LEVEL)"
exit 0
