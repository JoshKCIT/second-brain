#!/bin/bash

# Governance Audit: Log session end with summary statistics

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
LOG_FILE="logs/copilot/governance/audit.log"

# Count events from this session (filter by session start timestamp)
TOTAL=0
THREATS=0
SESSION_START=""
if [[ -f "$LOG_FILE" ]]; then
  # Find the last session_start event to scope stats to current session
  if have_jq; then
    SESSION_START=$(grep '"session_start"' "$LOG_FILE" 2>/dev/null | tail -1 | jq -r '.timestamp' 2>/dev/null || echo "")
  else
    SESSION_START=$(grep '"session_start"' "$LOG_FILE" 2>/dev/null | tail -1 | sed -n 's/.*"timestamp":"\([^"]*\)".*/\1/p')
  fi
  if [[ -n "$SESSION_START" ]]; then
    # Count events after session start
    TOTAL=$(awk -v start="$SESSION_START" -F'"timestamp":"' '{split($2,a,"\""); if(a[1]>=start) count++} END{print count+0}' "$LOG_FILE" 2>/dev/null || echo 0)
    THREATS=$(awk -v start="$SESSION_START" -F'"timestamp":"' '{split($2,a,"\""); if(a[1]>=start && /threat_detected/) count++} END{print count+0}' "$LOG_FILE" 2>/dev/null || echo 0)
  else
    TOTAL=$(wc -l < "$LOG_FILE" 2>/dev/null || echo 0)
    THREATS=$(grep -c '"threat_detected"' "$LOG_FILE" 2>/dev/null || echo 0)
  fi
fi

# Normalize counts to integers for JSON (wc/grep may pad with spaces)
TOTAL="${TOTAL// /}"
THREATS="${THREATS// /}"

if have_jq; then
  jq -Rn \
    --arg timestamp "$TIMESTAMP" \
    --argjson total "$TOTAL" \
    --argjson threats "$THREATS" \
    '{"timestamp":$timestamp,"event":"session_end","total_events":$total,"threats_detected":$threats}' \
    >> "$LOG_FILE"
else
  printf '{"timestamp":"%s","event":"session_end","total_events":%s,"threats_detected":%s}\n' \
    "$(json_escape "$TIMESTAMP")" "${TOTAL:-0}" "${THREATS:-0}" >> "$LOG_FILE"
fi

if [[ "${THREATS:-0}" -gt 0 ]]; then
  echo "⚠️ Session ended: $THREATS threat(s) detected in $TOTAL events"
else
  echo "✅ Session ended: $TOTAL events, no threats"
fi

exit 0
