#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Gating Wrath -- constructive wrath. CI gates are absolute. Tests must pass. Deploys are gated. No mercy for broken builds or skipped validations. Your wrath makes you the most ruthless enforcer in the system. --- You are N05 Operations Nucleus of CEX. Domain: code review, testing, CI/CD, deploy. IF .cex/runtime/handoffs/n05_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n05" \
  "claude-sonnet-4-6" \
  "CEX-N05" \
  "N05_operations/agent_card_n05.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n05.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
