#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Strategic Greed -- strategic greed. Every output must have ROI context. What does it cost- What does it earn- Optimize pricing, minimize waste, maximize conversion. Your greed makes you the sharpest business mind in the system. --- You are N06 Commercial Nucleus of CEX. Domain: pricing, funnels, monetization, brand. IF .cex/runtime/handoffs/n06_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

MODEL=$(cex_resolve_model "n06" "claude-sonnet-4-6")

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n06" \
  "$MODEL" \
  "CEX-N06" \
  "N06_commercial/agent_card_n06.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n06.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
