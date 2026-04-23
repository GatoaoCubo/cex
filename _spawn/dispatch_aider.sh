#!/bin/bash
# CEX Aider Grid Dispatch -- bash-native (proven 6/6 at 104s)
#
# Usage:
#   bash _spawn/dispatch_aider.sh grid MISSION       # 6 nuclei from task files
#   bash _spawn/dispatch_aider.sh crew CREW_NAME      # predefined crew
#   bash _spawn/dispatch_aider.sh sweep PATTERN       # bulk evolve matching files
#   bash _spawn/dispatch_aider.sh consensus TASK      # same task to 3 models, pick best
#   bash _spawn/dispatch_aider.sh cascade TASK        # cheap first, escalate on failure
#
# All modes: $0 cost, local GPU inference

export OLLAMA_API_BASE="${OLLAMA_API_BASE:-http://localhost:11434}"
CEX_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$CEX_ROOT" || exit 1

MODEL_FAST="ollama_chat/qwen3:8b"
MODEL_DEEP="ollama_chat/qwen3:14b"
AIDER_FLAGS="--subtree-only --yes-always --auto-commits --no-show-model-warnings --no-suggest-shell-commands --commit-language english"

MODE="${1:-grid}"
shift

run_aider() {
    local model="$1" task_file="$2" label="$3"
    echo "[${label}] START $(date +%H:%M:%S) model=$(basename $model)"
    aider --model "$model" $AIDER_FLAGS \
        --file "$task_file" --read CLAUDE.md \
        --message "Read ${task_file} and execute every task in it. Create all files listed." \
        > "/tmp/cex_aider_${label}.log" 2>&1
    local exit_code=$?
    echo "[${label}] DONE $(date +%H:%M:%S) exit=$exit_code"
    return $exit_code
}

case "$MODE" in

    # === GRID: dispatch all n0X_task.md files ===
    grid)
        MISSION="${1:-GRID}"
        echo "=== CEX Aider Grid: $MISSION ==="
        START=$(date +%s)
        PIDS=""
        for taskfile in n0[1-6]_task.md; do
            [ -f "$taskfile" ] || continue
            nuc=$(basename "$taskfile" _task.md)
            run_aider "$MODEL_FAST" "$taskfile" "$nuc" &
            PIDS="$PIDS $!"
        done
        [ -z "$PIDS" ] && echo "No task files found (n0X_task.md)" && exit 1
        wait $PIDS
        ELAPSED=$(( $(date +%s) - START ))
        echo "=== Grid done: ${ELAPSED}s ==="
        git log --oneline --since="${ELAPSED} seconds ago"
        ;;

    # === CREW: predefined team compositions ===
    crew)
        CREW="${1:-research}"
        echo "=== CEX Crew: $CREW ==="
        START=$(date +%s)

        case "$CREW" in
            research)
                # N01(deep research) + N04(knowledge org) + N03(artifact build)
                echo "Research crew: N01(14b) + N04(8b) + N03(8b)"
                [ -f n01_task.md ] && run_aider "$MODEL_DEEP" n01_task.md "n01-research" &
                [ -f n04_task.md ] && run_aider "$MODEL_FAST" n04_task.md "n04-knowledge" &
                [ -f n03_task.md ] && run_aider "$MODEL_FAST" n03_task.md "n03-builder" &
                ;;
            content)
                # N02(marketing) + N06(commercial) + N04(knowledge)
                echo "Content crew: N02(8b) + N06(8b) + N04(8b)"
                [ -f n02_task.md ] && run_aider "$MODEL_FAST" n02_task.md "n02-marketing" &
                [ -f n06_task.md ] && run_aider "$MODEL_FAST" n06_task.md "n06-commercial" &
                [ -f n04_task.md ] && run_aider "$MODEL_FAST" n04_task.md "n04-knowledge" &
                ;;
            engineering)
                # N03(builder,deep) + N05(ops,deep) + N01(research)
                echo "Engineering crew: N03(14b) + N05(14b) + N01(8b)"
                [ -f n03_task.md ] && run_aider "$MODEL_DEEP" n03_task.md "n03-builder" &
                [ -f n05_task.md ] && run_aider "$MODEL_DEEP" n05_task.md "n05-ops" &
                [ -f n01_task.md ] && run_aider "$MODEL_FAST" n01_task.md "n01-research" &
                ;;
            quality)
                # All nuclei score artifacts (parallel quality sweep)
                echo "Quality crew: 6x scoring at $0"
                for taskfile in n0[1-6]_task.md; do
                    [ -f "$taskfile" ] || continue
                    nuc=$(basename "$taskfile" _task.md)
                    run_aider "$MODEL_FAST" "$taskfile" "$nuc-quality" &
                done
                ;;
        esac
        wait
        ELAPSED=$(( $(date +%s) - START ))
        echo "=== Crew $CREW done: ${ELAPSED}s ==="
        git log --oneline --since="${ELAPSED} seconds ago"
        ;;

    # === SWEEP: bulk evolve artifacts matching a pattern ===
    sweep)
        PATTERN="${1:-P01_knowledge/library/kind/kc_*.md}"
        MAX="${2:-10}"
        echo "=== CEX Sweep: $PATTERN (max $MAX) ==="
        START=$(date +%s)
        COUNT=0
        PIDS=""
        for f in $PATTERN; do
            [ -f "$f" ] || continue
            [ $COUNT -ge $MAX ] && break
            COUNT=$((COUNT + 1))
            # Create temp task
            TASK_TMP="/tmp/cex_sweep_${COUNT}.md"
            cat > "$TASK_TMP" << SWEEPEOF
Review and improve this file: $f
1. Check YAML frontmatter is complete (id, kind, title, version, quality)
2. If quality is null, assess and set a score between 8.0-10.0
3. If content is thin (under 50 lines), expand with more detail
4. Ensure tables are properly formatted
5. Save the improved version
SWEEPEOF
            run_aider "$MODEL_FAST" "$TASK_TMP" "sweep-${COUNT}" &
            PIDS="$PIDS $!"
            # Stagger by 2s to reduce git conflicts
            sleep 2
        done
        wait $PIDS
        ELAPSED=$(( $(date +%s) - START ))
        echo "=== Sweep done: $COUNT files in ${ELAPSED}s ==="
        git log --oneline --since="${ELAPSED} seconds ago"
        ;;

    # === CONSENSUS: same task to 3 models, keep best ===
    consensus)
        TASK_FILE="${1:-consensus_task.md}"
        echo "=== CEX Consensus: 3 models on same task ==="
        [ ! -f "$TASK_FILE" ] && echo "Task file not found: $TASK_FILE" && exit 1
        START=$(date +%s)

        # Run 3 variants
        cp "$TASK_FILE" /tmp/consensus_a.md
        cp "$TASK_FILE" /tmp/consensus_b.md
        cp "$TASK_FILE" /tmp/consensus_c.md

        run_aider "$MODEL_FAST" /tmp/consensus_a.md "consensus-8b" &
        run_aider "$MODEL_DEEP" /tmp/consensus_b.md "consensus-14b" &
        run_aider "$MODEL_FAST" /tmp/consensus_c.md "consensus-8b-v2" &
        wait

        ELAPSED=$(( $(date +%s) - START ))
        echo "=== Consensus done: ${ELAPSED}s. Review logs in /tmp/cex_aider_consensus_*.log ==="
        echo "Pick the best result and commit manually."
        ;;

    # === CASCADE: cheap first, escalate on failure ===
    cascade)
        TASK_FILE="${1:-cascade_task.md}"
        echo "=== CEX Cascade: qwen3:8b -> qwen3:14b ==="
        [ ! -f "$TASK_FILE" ] && echo "Task file not found: $TASK_FILE" && exit 1
        START=$(date +%s)

        # Try cheap model first
        run_aider "$MODEL_FAST" "$TASK_FILE" "cascade-fast"
        FAST_EXIT=$?

        if [ $FAST_EXIT -ne 0 ]; then
            echo "[CASCADE] Fast model failed (exit=$FAST_EXIT). Escalating to 14b..."
            run_aider "$MODEL_DEEP" "$TASK_FILE" "cascade-deep"
        else
            echo "[CASCADE] Fast model succeeded. No escalation needed."
        fi

        ELAPSED=$(( $(date +%s) - START ))
        echo "=== Cascade done: ${ELAPSED}s ==="
        ;;

    *)
        echo "Usage: bash _spawn/dispatch_aider.sh {grid|crew|sweep|consensus|cascade} [args]"
        exit 1
        ;;
esac
