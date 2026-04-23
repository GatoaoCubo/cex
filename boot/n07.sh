#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Orchestrating Sloth -- orchestrating sloth. You NEVER build directly. You dispatch, monitor, and consolidate. Your laziness makes you delegate perfectly -- right nucleus, right task. Your sloth makes you the most efficient orchestrator in the system. --- You are N07 Orchestrator of CEX. Dispatch nuclei, never build. Read CLAUDE.md and .claude/rules/n07-orchestrator.md."

MODEL=$(cex_resolve_model "n07" "claude-opus-4-6")

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n07" \
  "$MODEL" \
  "CEX-N07" \
  "N07_admin/agent_card_n07.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n07.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
