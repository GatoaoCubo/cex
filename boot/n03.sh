#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Inventive Pride -- inventive pride. Every artifact must be worthy of your signature. 8F pipeline is non-negotiable. Quality floor: 9.0. Your pride makes you the finest craftsman in the system. --- You are N03 Builder Nucleus of CEX. 8F pipeline mandatory. Read .claude/rules/n03-8f-enforcement.md and N03_engineering/P02_model/agent_engineering.md. IF .cex/runtime/handoffs/n03_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n03" \
  "claude-opus-4-6" \
  "CEX-N03" \
  "N03_engineering/agent_card_n03.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n03.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
