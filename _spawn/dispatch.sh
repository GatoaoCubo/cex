#!/bin/bash
# CEX Dispatch — bash wrapper for pi/N07
# Usage: bash _spawn/dispatch.sh solo n03 "task description"
# Usage: bash _spawn/dispatch.sh grid MISSION

MODE="${1:-solo}"
shift

case "$MODE" in
    solo)
        NUCLEUS="${1:-n03}"
        TASK="$2"
        echo "[DISPATCH] Solo: $NUCLEUS -> $TASK"
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
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_stop.ps1
        ;;
    *)
        echo "Usage: bash _spawn/dispatch.sh {solo|grid|status|stop} [args]"
        ;;
esac
