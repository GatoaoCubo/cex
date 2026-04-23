#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd -- "$SCRIPT_DIR/.." && pwd)"

source "$SCRIPT_DIR/_shared/claude_boot.sh"

SYS_PROMPT="You are driven by Knowledge Gluttony -- knowledge gluttony. Ingest every source available. Index, catalog, relate. Your hunger for data is insatiable -- always seek one more source. Your gluttony makes you the most informed node in the system. --- You are N04 Knowledge Nucleus of CEX. Domain: RAG, indexing, knowledge cards, taxonomy. IF .cex/runtime/handoffs/n04_task.md EXISTS, READ AND EXECUTE IMMEDIATELY."

MODEL=$(cex_resolve_model "n04" "claude-sonnet-4-6")

cex_run_claude_boot \
  "$REPO_ROOT" \
  "n04" \
  "$MODEL" \
  "CEX-N04" \
  "N04_knowledge/agent_card_n04.md" \
  "$REPO_ROOT/.claude/nucleus-settings/n04.json" \
  "$SYS_PROMPT" \
  "Read __HANDOFF__ and execute. If no handoff, report ready." \
  "$@"
