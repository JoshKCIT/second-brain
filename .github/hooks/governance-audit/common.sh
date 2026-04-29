#!/bin/bash
# Shared helpers for governance audit hooks (sourced by *.sh)

have_jq() {
  command -v jq &>/dev/null
}

# Minimal JSON string escape for printf-based NDJSON lines when jq is unavailable.
json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}
