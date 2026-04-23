#!/bin/bash
# CEX Dispatch -- bash wrapper for claude/N07
#
# Usage:
#   bash _spawn/dispatch.sh solo n03 "task"    # dispatch 1 nucleus
#   bash _spawn/dispatch.sh grid MISSION       # dispatch up to 6 parallel
#   bash _spawn/dispatch.sh status             # monitor running nuclei
#   bash _spawn/dispatch.sh stop               # stop MY session's nuclei only
#   bash _spawn/dispatch.sh stop n03           # stop only N03
#   bash _spawn/dispatch.sh stop --all         # stop ALL CEX nuclei (DANGEROUS)
#   bash _spawn/dispatch.sh stop --dry-run     # preview what would be killed
#   bash _spawn/dispatch.sh swarm <kind> <N> "<task>"   # N parallel worktrees
#   bash _spawn/dispatch.sh solo n03 "task" -w <id>     # run in isolated worktree
#   bash _spawn/dispatch.sh grid MISSION -w             # grid with worktree per cell

# --- Session ID: stable identifier for this orchestrator ---
# Each claude/N07 session sets CEX_SESSION_ID once. All dispatch calls inherit it.
# If not set, generate from timestamp (stable within same second).
# IMPORTANT: For multi-N07, set CEX_SESSION_ID before first dispatch.
if [ -z "$CEX_SESSION_ID" ]; then
    SESSION_FILE=".cex/runtime/pids/.my_session"
    if [ -f "$SESSION_FILE" ]; then
        _val=$(cat "$SESSION_FILE")
        if [[ "$_val" =~ ^s[0-9]+$ ]]; then
            export CEX_SESSION_ID="$_val"
        else
            CEX_SESSION_ID="s$(date +%s)"
            export CEX_SESSION_ID
            echo "$CEX_SESSION_ID" > "$SESSION_FILE"
        fi
    else
        mkdir -p .cex/runtime/pids
        CEX_SESSION_ID="s$(date +%s)"
        export CEX_SESSION_ID
        echo "$CEX_SESSION_ID" > "$SESSION_FILE"
    fi
fi
export CEX_SESSION_ID

MODE="${1:-solo}"
shift

# --- Parse -w / --worktree flag (BORIS_MERGE B8) ---
# Scans remaining args, strips the flag, exports CEX_WORKTREE for downstream boot wrappers.
WORKTREE_ID=""
_new_args=()
while [ $# -gt 0 ]; do
    case "$1" in
        -w|--worktree)
            shift
            WORKTREE_ID="${1:-auto}"
            [ "$WORKTREE_ID" = "auto" ] && WORKTREE_ID="wt_$(date +%s)"
            ;;
        *)
            _new_args+=("$1")
            ;;
    esac
    shift || true
done
set -- "${_new_args[@]}"
if [ -n "$WORKTREE_ID" ]; then
    export CEX_WORKTREE="$WORKTREE_ID"
    export CEX_WORKTREE_DIR=".cex/worktrees/$WORKTREE_ID"
    echo "[DISPATCH] Worktree isolation: $CEX_WORKTREE_DIR"
    if [ ! -d "$CEX_WORKTREE_DIR" ]; then
        git worktree add -b "worktree/$WORKTREE_ID" "$CEX_WORKTREE_DIR" HEAD >/dev/null 2>&1 || true
    fi
fi

# --- Pre-flight MCP gather for non-Claude runtimes ---
# When dispatching to runtimes without MCP access (ollama, codex, gemini),
# run Phase 0 to inject external context into handoffs.
_preflight_mcp() {
    local nucleus="$1"
    local handoff="$2"
    if [ ! -f "$handoff" ]; then
        return 0
    fi
    if ! command -v python &>/dev/null; then
        return 0
    fi
    # Extract kind from handoff (if present)
    local kind
    kind=$(python -c "
import re, sys
text = open('$handoff', encoding='utf-8', errors='ignore').read()
m = re.search(r'kind[=:]\s*(\w+)', text, re.IGNORECASE)
print(m.group(1) if m else '')
" 2>/dev/null)
    if [ -z "$kind" ]; then
        return 0
    fi
    # Check if kind needs external context
    local needs
    needs=$(python _tools/cex_router_v2.py --check-kind "$kind" --json 2>/dev/null | python -c "import sys,json; d=json.load(sys.stdin); print(d.get('requires_external_context', False))" 2>/dev/null)
    if [ "$needs" = "True" ]; then
        local task_text
        task_text=$(head -20 "$handoff" | grep -v '^---' | head -5 | tr '\n' ' ')
        echo "[PREFLIGHT] Phase 0 MCP gather for $nucleus (kind=$kind)"
        python _tools/cex_preflight_mcp.py --nucleus "$nucleus" --kind "$kind" \
            --task "$task_text" --gather 2>/dev/null || true
    fi
}

case "$MODE" in
    solo)
        NUCLEUS="${1:-n03}"
        TASK="$2"
        echo "[DISPATCH] Solo: $NUCLEUS -> $TASK"
        # --- T09: Agent spawn pre-flight validation ---
        if command -v python &>/dev/null; then
            if ! python _tools/cex_agent_spawn.py --validate --nucleus "$NUCLEUS" 2>/dev/null; then
                echo "[DISPATCH] WARN: Agent validation failed for $NUCLEUS (proceeding anyway)"
            fi
        fi
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -interactive
        ;;
    swarm)
        KIND="${1:-agent}"
        N="${2:-3}"
        TASK="${3:-build one $KIND}"
        echo "[DISPATCH] Swarm: $N parallel $KIND (worktree per cell)"
        bash _spawn/spawn_swarm.sh "$KIND" "$N" "$TASK"
        ;;
    grid)
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION (cli=claude)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli claude -interactive
        ;;
    grid-haiku)
        MISSION="${1:-DEFAULT}"
        _RESOLVED_MODEL=$(python3 -c "
import sys
sys.path.insert(0, '.')
try:
    from _tools.cex_model_resolver import get_preflight_model
    print(get_preflight_model('cloud').get('model', 'claude-haiku-4-5-20251001'))
except Exception:
    print('claude-haiku-4-5-20251001')
" 2>/dev/null || echo "claude-haiku-4-5-20251001")
        MODEL="${2:-$_RESOLVED_MODEL}"
        echo "[DISPATCH] Grid: $MISSION (cli=claude, model=$MODEL)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli claude -interactive -Model "$MODEL"
        ;;
    grid-gemini)
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION (cli=gemini)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli gemini -interactive
        ;;
    grid-aider)
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION (cli=aider, model=ollama/qwen3:14b, cost=\$0)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid_aider.ps1 -mission "$MISSION"
        ;;
    grid-codex)
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION (cli=codex)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli codex -interactive
        ;;
    grid-ollama)
        # Interactive 3x2 tiled windows, each running boot/n0X_ollama.ps1 -> ollama_nucleus.py
        MISSION="${1:-DEFAULT}"
        MODEL="${2:-qwen3:8b}"
        echo "[DISPATCH] Grid: $MISSION (cli=ollama, model=$MODEL, interactive, cost=\$0)"
        export OLLAMA_MODEL="$MODEL"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli ollama -interactive
        ;;
    solo-ollama)
        # Interactive single window, boot/n0X_ollama.ps1 -> ollama_nucleus.py
        NUCLEUS="${1:-n03}"
        MODEL="${2:-qwen3:8b}"
        TASK="${3:-}"
        echo "[DISPATCH] Solo-Ollama: $NUCLEUS via $MODEL (interactive)"
        _preflight_mcp "$NUCLEUS" ".cex/runtime/handoffs/${NUCLEUS}_task.md"
        export OLLAMA_MODEL="$MODEL"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -cli ollama -interactive
        ;;
    solo-codex)
        # Interactive single window, boot/n0X_codex.ps1 -> codex CLI
        NUCLEUS="${1:-n03}"
        TASK="${2:-}"
        echo "[DISPATCH] Solo-Codex: $NUCLEUS (interactive)"
        _preflight_mcp "$NUCLEUS" ".cex/runtime/handoffs/${NUCLEUS}_task.md"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -cli codex -interactive
        ;;
    solo-gemini)
        # Interactive single window, boot/n0X_gemini.ps1 -> gemini CLI
        NUCLEUS="${1:-n03}"
        TASK="${2:-}"
        echo "[DISPATCH] Solo-Gemini: $NUCLEUS (interactive)"
        _preflight_mcp "$NUCLEUS" ".cex/runtime/handoffs/${NUCLEUS}_task.md"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -cli gemini -interactive
        ;;
    grid-litellm)
        # Interactive 3x2 tiled, each window runs boot/n0X_litellm.ps1 -> litellm proxy
        # Proxy must be running: powershell -File boot/litellm_proxy.ps1
        MISSION="${1:-DEFAULT}"
        echo "[DISPATCH] Grid: $MISSION (cli=litellm, proxy=:4000, interactive)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission "$MISSION" -cli litellm -interactive
        ;;
    solo-litellm)
        # Interactive single window, boot/n0X_litellm.ps1 -> litellm proxy
        NUCLEUS="${1:-n03}"
        TASK="${2:-}"
        echo "[DISPATCH] Solo-LiteLLM: $NUCLEUS (model alias cex-$NUCLEUS, interactive)"
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus "$NUCLEUS" -task "$TASK" -cli litellm -interactive
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
        # shellcheck disable=SC2086
        powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_stop.ps1 $STOP_ARGS
        ;;
    ollama)
        # Headless dispatch via 8F pipeline + Ollama (no Claude Code CLI needed)
        NUCLEUS="${1:-n03}"
        MODEL="${2:-qwen3:8b}"
        HANDOFF="${3:-}"
        echo "[DISPATCH] Ollama: $NUCLEUS via $MODEL"
        # Read task from handoff file or n0x_task.md
        if [ -z "$HANDOFF" ]; then
            HANDOFF=".cex/runtime/handoffs/${NUCLEUS}_task.md"
        fi
        if [ ! -f "$HANDOFF" ]; then
            echo "[FAIL] No handoff found: $HANDOFF"
            exit 1
        fi
        _preflight_mcp "$NUCLEUS" "$HANDOFF"
        # Run 8F pipeline with Ollama model
        INTENT=$(head -1 "$HANDOFF" | sed 's/^#* *//')
        python _tools/cex_8f_runner.py \
            --execute \
            --model "ollama/$MODEL" \
            --nucleus "$NUCLEUS" \
            --context-file "$HANDOFF" \
            "$INTENT"
        echo "[DONE] $NUCLEUS via Ollama/$MODEL"
        ;;
    ollama-grid)
        # Parallel Ollama dispatch (all nuclei via local models)
        MISSION="${1:-DEFAULT}"
        MODEL="${2:-qwen3:8b}"
        echo "[DISPATCH] Ollama Grid: $MISSION via $MODEL"
        HANDOFF_DIR=".cex/runtime/handoffs"
        # Pre-flight MCP for all handoffs before parallel launch
        for hf in "$HANDOFF_DIR"/${MISSION}_n0*.md; do
            if [ -f "$hf" ]; then
                NUC_PF=$(echo "$hf" | grep -o 'n0[1-7]')
                _preflight_mcp "$NUC_PF" "$hf"
            fi
        done
        PIDS=""
        for hf in "$HANDOFF_DIR"/${MISSION}_n0*.md; do
            if [ -f "$hf" ]; then
                NUC=$(echo "$hf" | grep -o 'n0[1-7]')
                echo "  [>>] Starting $NUC..."
                INTENT=$(head -1 "$hf" | sed 's/^#* *//')
                python _tools/cex_8f_runner.py \
                    --execute \
                    --model "ollama/$MODEL" \
                    --nucleus "$NUC" \
                    --context-file "$hf" \
                    "$INTENT" &
                PIDS="$PIDS $!"
            fi
        done
        if [ -z "$PIDS" ]; then
            echo "[FAIL] No handoffs found for mission: $MISSION"
            exit 1
        fi
        echo "[WAIT] Waiting for $PIDS..."
        # shellcheck disable=SC2086
        wait $PIDS
        echo "[DONE] Ollama Grid complete: $MISSION"
        ;;
    *)
        echo "Usage: bash _spawn/dispatch.sh {solo|grid|grid-gemini|grid-codex|grid-ollama|solo-ollama|solo-codex|solo-gemini|grid-litellm|solo-litellm|ollama|ollama-grid|status|stop} [args]"
        echo ""
        echo "  solo n03 \"task\"           Spawn 1 Claude Code nucleus (interactive)"
        echo "  grid MISSION              Spawn up to 6 Claude Code nuclei (interactive 3x2)"
        echo "  grid-gemini MISSION       Spawn up to 6 Gemini CLI nuclei"
        echo "  grid-codex MISSION        Spawn up to 6 Codex CLI nuclei"
        echo "  solo-ollama n04 qwen3:8b \"task\"  Spawn 1 Ollama nucleus (interactive window)"
        echo "  grid-ollama MISSION qwen3:8b     Spawn up to 6 Ollama nuclei (interactive 3x2, free)"
        echo "  solo-litellm n04 \"task\"          Spawn 1 LiteLLM nucleus (proxy decides backend)"
        echo "  grid-litellm MISSION             Spawn up to 6 LiteLLM nuclei (interactive 3x2, proxy)"
        echo "  ollama n03 qwen3:8b       Run 1 nucleus via Ollama headless (cex_8f_runner)"
        echo "  ollama-grid MISSION ...   Run all nuclei via Ollama headless"
        echo "  status                    Monitor running nuclei"
        echo "  stop                      Stop MY session's nuclei only"
        echo "  stop n03                  Stop only N03"
        echo "  stop --all                Stop ALL CEX nuclei (DANGEROUS)"
        echo "  stop --dry-run            Preview what would be killed"
        echo "  swarm <kind> <N> \"task\"   Spawn N parallel builders of same kind in worktrees"
        echo ""
        echo "Flags (apply to solo/grid):"
        echo "  -w, --worktree [id]       Run in isolated git worktree (auto-creates if missing)"
        ;;
esac
