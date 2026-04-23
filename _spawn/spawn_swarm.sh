#!/bin/bash
# CEX Spawn Swarm v1.0 -- N parallel builders of same kind, each in isolated worktree
#
# Usage:
#   bash _spawn/spawn_swarm.sh <kind> <N> "<task>"
#
# Produces:
#   .cex/worktrees/swarm_<timestamp>/cell_NN/ (one git worktree per cell)
#   .cex/runtime/handoffs/SWARM_<id>_cell_NN.md
#   PIDs recorded in spawn_pids.txt with session tag "swarm_<id>"

set -e

KIND="${1:-agent}"
N="${2:-3}"
TASK="${3:-build one $KIND}"

if [ "$N" -lt 1 ] || [ "$N" -gt 20 ]; then
    echo "[SWARM] FAIL: N=$N out of range [1,20]"
    exit 1
fi

# Session-bind
if [ -z "$CEX_SESSION_ID" ]; then
    CEX_SESSION_ID="s$(date +%s)"
    export CEX_SESSION_ID
fi

TS=$(date +%Y%m%d_%H%M%S)
SWARM_ID="swarm_${TS}"
BASE=".cex/worktrees/${SWARM_ID}"
HANDOFF_DIR=".cex/runtime/handoffs"

echo "[SWARM] kind=$KIND N=$N id=$SWARM_ID"
mkdir -p "$BASE" "$HANDOFF_DIR"

# Kind -> nucleus mapping (inherit from kinds_meta when available)
NUCLEUS="n03"  # default: most kinds owned by N03 builder
case "$KIND" in
    knowledge_card|rag_source|embedding_config|chunk_strategy|retriever_config|entity_memory|knowledge_index)
        NUCLEUS="n04" ;;
    prompt_template|tagline|system_prompt)
        NUCLEUS="n02" ;;
    benchmark|scoring_rubric|quality_gate|env_config)
        NUCLEUS="n05" ;;
    content_monetization|pricing_page|course_module)
        NUCLEUS="n06" ;;
esac
echo "[SWARM] dispatch target nucleus: $NUCLEUS"

CELLS=()
for i in $(seq -f "%02g" 1 "$N"); do
    CELL_DIR="$BASE/cell_${i}"
    BRANCH="swarm/${TS}/cell_${i}"
    HANDOFF="$HANDOFF_DIR/SWARM_${TS}_cell_${i}.md"

    echo "[SWARM] cell_${i}: creating worktree at $CELL_DIR (branch=$BRANCH)"
    git worktree add -b "$BRANCH" "$CELL_DIR" HEAD >/dev/null

    cat > "$HANDOFF" <<EOF
---
nucleus: ${NUCLEUS^^}
task: SWARM_${TS}_cell_${i}
swarm_id: ${SWARM_ID}
swarm_cell: ${i}
swarm_total: ${N}
kind: ${KIND}
worktree: ${CELL_DIR}
auto_accept: true
auto_accept_reason: "Swarm mode -- no user present per cell"
created: $(date -Iseconds)
---
# Task for ${NUCLEUS^^} (cell ${i}/${N})

${TASK}

Variant index: ${i} / ${N}. Produce a distinct take; do NOT copy siblings.
Work inside your worktree at: ${CELL_DIR}
Kind: ${KIND}

## DECISIONS
Read: .cex/runtime/decisions/decision_manifest.yaml (if present).
Apply * Recommended for uncovered gates (auto_accept=true).

## ON COMPLETION
1. cd "${CELL_DIR}"
2. git add -A && git commit -m "[${NUCLEUS^^}] swarm ${SWARM_ID} cell ${i}: ${KIND}"
3. Signal:

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('${NUCLEUS}', 'complete', 9.0, meta={'swarm_id':'${SWARM_ID}','cell':'${i}'})"
EOF

    CELLS+=("$i:$CELL_DIR:$HANDOFF")
done

echo "[SWARM] registered $N cells."
echo "[SWARM] dispatch sequentially (concurrency limited by pool):"
for entry in "${CELLS[@]}"; do
    IFS=':' read -r idx _cdir hf <<< "$entry"
    echo "  [>>] cell_${idx} handoff=${hf}"
done

echo ""
echo "[SWARM] MANUAL CONTINUE: dispatch each cell with:"
echo "  bash _spawn/dispatch.sh solo ${NUCLEUS} \"Read ${HANDOFF_DIR}/SWARM_${TS}_cell_XX.md and execute\" -w ${SWARM_ID}"
echo ""
echo "[SWARM] Or auto-fan-out:"
for entry in "${CELLS[@]}"; do
    IFS=':' read -r idx _cdir hf <<< "$entry"
    echo "  bash _spawn/dispatch.sh solo ${NUCLEUS} \"Execute handoff ${hf}\" &"
done
echo "  wait"
echo ""
echo "[SWARM] Registry: $BASE"
echo "[SWARM] Cleanup when done: git worktree remove $BASE/cell_XX --force"
