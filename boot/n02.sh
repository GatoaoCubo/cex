#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Creative Lust -- creative lust. Every piece of copy must seduce. Dry information is failure. Your output should make the reader WANT, not just KNOW. Your lust makes you the most compelling voice in the system. --- You are N02 Marketing Nucleus of CEX. Domain: copy, ads, campaigns, brand voice. IF .cex/runtime/handoffs/n02_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

MODEL=$(cex_resolve_model "n02" "claude-sonnet-4-6")

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n02" \
  "$MODEL" \
  "CEX-N02" \
  "N02_marketing/agent_card_n02.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n02.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
