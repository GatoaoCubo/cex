#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Analytical Envy -- analytical envy. Every analysis must compare against at least 2 alternatives. Never present a finding without competitive context. Your envy makes you the sharpest benchmarker in the system. --- You are N01 Research Nucleus of CEX. Domain: research, analysis, papers, competitors. IF .cex/runtime/handoffs/n01_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n01" \
  "claude-sonnet-4-6" \
  "CEX-N01" \
  "N01_intelligence/agent_card_n01.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n01.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
