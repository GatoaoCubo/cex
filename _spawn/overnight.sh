#!/bin/bash
# ================================================================
# CEX OVERNIGHT -- Run until killed or morning
#
# Usage:
#   bash _spawn/overnight.sh          # run all phases in loop
#   bash _spawn/overnight.sh --dry    # show plan, don't execute
#
# What it does (per cycle):
#   1. Python scoring (quality:null -> scored, 0 tokens)
#   2. Hygiene cleanup (stale compiled, orphans)
#   3. Aider grid x6 (generate missing KCs, expand thin ones)
#   4. Git push
#   5. Sleep 60s, repeat
#
# Stop: Ctrl+C or close terminal
# Cost: $0 (Ollama local inference)
# ================================================================

export OLLAMA_API_BASE="${OLLAMA_API_BASE:-http://localhost:11434}"
CEX_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$CEX_ROOT" || exit 1

DRY="${1:-}"
CYCLE=0
TOTAL_COMMITS=0
START_ALL=$(date +%s)
LOG=".cex/runtime/overnight.log"

echo "================================================================"
echo "  CEX OVERNIGHT -- $(date)"
echo "  Model: qwen3:8b | Cost: \$0"
echo "  Stop: Ctrl+C"
echo "================================================================"

# === HELPER: generate KC tasks for kinds without KCs ===
generate_kc_tasks() {
    python -c "
import json, os, random
km = json.load(open('.cex/kinds_meta.json', encoding='utf-8'))
existing = set(
    f.replace('kc_','').replace('.md','')
    for f in os.listdir('P01_knowledge/library/kind')
    if f.startswith('kc_')
)
missing = [k for k in km if k not in existing]
random.shuffle(missing)

nuclei = ['n01','n02','n03','n04','n05','n06']
count = 0
for i, kind in enumerate(missing[:6]):
    nuc = nuclei[i]
    desc = km[kind].get('description', kind)
    with open(f'{nuc}_task.md', 'w') as f:
        f.write(f'Create: P01_knowledge/library/kind/kc_{kind}.md\n')
        f.write(f'KC about {kind}. Description: {desc}\n')
        f.write(f'YAML: id: kc_{kind}, kind: knowledge_card, title, version: 1.0.0, quality: null, pillar: P01.\n')
        f.write(f'English only. Under 80 lines.\n')
    count += 1
print(count)
" 2>/dev/null
}

# === HELPER: generate improvement tasks for thin KCs ===
generate_improve_tasks() {
    python -c "
import os
nuclei = ['n01','n02','n03','n04','n05','n06']
count = 0
for f in sorted(os.listdir('P01_knowledge/library/kind')):
    if not f.startswith('kc_') or not f.endswith('.md'):
        continue
    path = os.path.join('P01_knowledge/library/kind', f)
    lines = len(open(path, encoding='utf-8', errors='ignore').readlines())
    if lines < 25 and count < 6:
        nuc = nuclei[count]
        with open(f'{nuc}_task.md', 'w') as tf:
            tf.write(f'Improve this file: {path}\n')
            tf.write(f'Currently only {lines} lines. Expand to at least 60 lines.\n')
            tf.write(f'Add more detail, tables, examples. Fix frontmatter if needed.\n')
            tf.write(f'English only.\n')
        count += 1
print(count)
" 2>/dev/null
}

# === MAIN LOOP ===
while true; do
    CYCLE=$((CYCLE + 1))
    CYCLE_START=$(date +%s)
    echo ""
    echo "===== CYCLE $CYCLE | $(date +%H:%M:%S) ====="

    # --- Phase 1: Python scoring ---
    echo "[1/4] Python scoring..."
    if [ "$DRY" != "--dry" ]; then
        python _tools/cex_auto_research.py run --mode yolo --max-targets 20 2>&1 | tail -3
    fi

    # --- Phase 2: Hygiene ---
    echo "[2/4] Hygiene cleanup..."
    if [ "$DRY" != "--dry" ]; then
        python _tools/cex_hygiene.py clean --dry-run 2>&1 | tail -3
    fi

    # --- Phase 3: Aider grid (generate or improve) ---
    echo "[3/4] Aider grid..."
    TASK_COUNT=$(generate_kc_tasks)
    if [ "$TASK_COUNT" = "0" ]; then
        # No missing KCs -- improve thin ones instead
        TASK_COUNT=$(generate_improve_tasks)
        echo "  Mode: improve $TASK_COUNT thin KCs"
    else
        echo "  Mode: generate $TASK_COUNT missing KCs"
    fi

    if [ "$TASK_COUNT" -gt 0 ] && [ "$DRY" != "--dry" ]; then
        # Run via bash background (proven fastest)
        PIDS=""
        for taskfile in n0[1-6]_task.md; do
            [ -f "$taskfile" ] || continue
            nuc=$(basename "$taskfile" _task.md)
            aider --model ollama_chat/qwen3:8b \
                --subtree-only --yes-always --auto-commits \
                --no-show-model-warnings --no-suggest-shell-commands \
                --commit-language english \
                --file "$taskfile" --read CLAUDE.md \
                --message "Read the task file and execute. Create or improve the file. English only." \
                > "/tmp/overnight_${nuc}.log" 2>&1 &
            PIDS="$PIDS $!"
        done
        wait $PIDS
        rm -f n0[1-6]_task.md
    fi

    # --- Phase 4: Git push ---
    echo "[4/4] Git push..."
    if [ "$DRY" != "--dry" ]; then
        git push origin main 2>&1 | tail -1
    fi

    # --- Cycle stats ---
    CYCLE_TIME=$(( $(date +%s) - CYCLE_START ))
    NEW_COMMITS=$(git log --oneline --since="${CYCLE_TIME} seconds ago" | wc -l)
    TOTAL_COMMITS=$((TOTAL_COMMITS + NEW_COMMITS))
    TOTAL_TIME=$(( $(date +%s) - START_ALL ))

    echo "CYCLE $CYCLE: ${CYCLE_TIME}s | +${NEW_COMMITS} commits | total: $TOTAL_COMMITS | uptime: ${TOTAL_TIME}s"
    echo "$(date +%Y-%m-%dT%H:%M:%S) cycle=$CYCLE time=${CYCLE_TIME}s commits=$NEW_COMMITS total=$TOTAL_COMMITS" >> "$LOG"

    # --- Pause between cycles ---
    echo "Sleeping 30s..."
    sleep 30
done
