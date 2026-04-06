#!/bin/bash
# CEX Dispatch — bash wrapper for pi/N07
#
# Usage:
#   bash _spawn/dispatch.sh solo n03 "task"    # dispatch 1 nucleus
#   bash _spawn/dispatch.sh grid MISSION       # dispatch up to 6 parallel
#   bash _spawn/dispatch.sh status             # monitor running nuclei
#   bash _spawn/dispatch.sh stop               # stop MY session's nuclei only
#   bash _spawn/dispatch.sh stop n03           # stop only N03
#   bash _spawn/dispatch.sh stop --all         # stop ALL CEX nuclei (DANGEROUS)
#   bash _spawn/dispatch.sh stop --dry-run     # preview what would be killed

# --- Session ID: stable identifier for this orchestrator ---
# Each pi/N07 session sets CEX_SESSION_ID once. All dispatch calls inherit it.
# If not set, generate from timestamp (stable within same second).
# IMPORTANT: For multi-N07, set CEX_SESSION_ID before first dispatch.
if [ -z "$CEX_SESSION_ID" ]; then
    SESSION_FILE=".cex/runtime/pids/.my_session"
    if [ -f "$SESSION_FILE" ]; then
        export CEX_SESSION_ID=$(cat "$SESSION_FILE")
    else
        mkdir -p .cex/runtime/pids
        export CEX_SESSION_ID="s$(date +%s)"
        echo "$CEX_SESSION_ID" > "$SESSION_FILE"
    fi
fi
export CEX_SESSION_ID

MODE="${1:-solo}"
shift

case "$MODE" in
    solo)
        NUCLEUS="${1:-n03}"
        TASK="$2"
        echo "[DISPATCH] Solo: $NUCLEUS -> $TASK"
        # --- T09: Agent spawn pre-flight validation ---
        if command -v python &>/dev/null; then
            python _tools/cex_agent_spawn.py --validate --nucleus "$NUCLEUS" 2>/dev/null
            if [ $? -ne 0 ]; then
                echo "[DISPATCH] WARN: Agent validation failed for $NUCLEUS (proceeding anyway)"
            fi
        fi
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -interactive
        ;;
    grid)
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -interactive
        ;;
    status)
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_monitor.ps1
        ;;
    stop)
        # Parse stop arguments
        STOP_ARGS=""
        for arg in "$@"; do
            case "$arg" in
                --all)     STOP_ARGS="$STOP_ARGS -All" ;;
                --dry-run) STOP_ARGS="$STOP_ARGS -DryRun" ;;
                n0[1-7])   STOP_ARGS="$STOP_ARGS -Nucleus $arg" ;;
                s*)        STOP_ARGS="$STOP_ARGS -Session $arg" ;;
            esac
        done
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_stop.ps1 $STOP_ARGS
        ;;
    *)
        echo "Usage: bash _spawn/dispatch.sh {solo|grid|status|stop} [args]"
        echo ""
        echo "  stop              Stop MY session's nuclei only"
        echo "  stop n03          Stop only N03"
        echo "  stop --all        Stop ALL CEX nuclei (DANGEROUS)"
        echo "  stop --dry-run    Preview what would be killed"
        ;;
esac
