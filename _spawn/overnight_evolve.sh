#!/bin/bash
# CEX Overnight Evolve -- Continuous batching with all dispatch modes
# Chains: sweep -> crew -> cascade -> grid in cycles
# Total cost: $0 (all local Ollama inference)
#
# Usage:
#   bash _spawn/overnight_evolve.sh              # default: 3 cycles
#   bash _spawn/overnight_evolve.sh 10           # 10 cycles
#   bash _spawn/overnight_evolve.sh unlimited    # run until killed

export OLLAMA_API_BASE="${OLLAMA_API_BASE:-http://localhost:11434}"
CEX_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$CEX_ROOT"

MAX_CYCLES="${1:-3}"
CYCLE=0
TOTAL_IMPROVED=0
TOTAL_TIME=0
LOG_FILE=".cex/runtime/overnight_evolve.log"
mkdir -p .cex/runtime

echo "============================================================"
echo "  CEX Overnight Evolve -- Continuous Batching"
echo "  Cycles: $MAX_CYCLES | Cost: \$0 | GPU: RTX 5070 Ti"
echo "  Started: $(date)"
echo "============================================================"
echo ""

log() { echo "[$(date +%H:%M:%S)] $1" | tee -a "$LOG_FILE"; }

# --- PHASE 1: Python-first scoring (0 tokens, instant) ---
phase_python_score() {
    log "PHASE 1: Python scoring (L1+L2, 0 tokens)"
    python _tools/cex_auto_research.py run --mode yolo --max-targets 20 2>&1 | tail -5
}

# --- PHASE 2: Sweep -- bulk improve KCs with thin content ---
phase_sweep() {
    log "PHASE 2: Sweep -- improve thin KCs"
    # Find KCs under 30 lines (thin content)
    THIN_KCS=""
    COUNT=0
    for f in P01_knowledge/library/kind/kc_*.md; do
        [ -f "$f" ] || continue
        LINES=$(wc -l < "$f")
        if [ "$LINES" -lt 30 ]; then
            THIN_KCS="$THIN_KCS $f"
            COUNT=$((COUNT + 1))
            [ $COUNT -ge 4 ] && break
        fi
    done
    if [ -n "$THIN_KCS" ]; then
        log "  Found $COUNT thin KCs to expand"
        bash _spawn/dispatch_aider.sh sweep "$THIN_KCS" $COUNT 2>&1 | tail -3
    else
        log "  No thin KCs found"
    fi
}

# --- PHASE 3: Crew -- mixed-model domain tasks ---
phase_crew() {
    log "PHASE 3: Crew -- generate missing artifacts"

    # Auto-generate task files based on gaps
    # Find kinds without KCs
    python -c "
import json, os
km = json.load(open('.cex/kinds_meta.json', encoding='utf-8'))
existing = set(f.replace('kc_','').replace('.md','') for f in os.listdir('P01_knowledge/library/kind') if f.startswith('kc_'))
missing = [k for k in km if k not in existing][:2]
if missing:
    for i, kind in enumerate(missing):
        nuc = 'n03' if i == 0 else 'n04'
        desc = km[kind].get('description', kind)
        with open(f'{nuc}_task.md', 'w') as f:
            f.write(f'Create file: P01_knowledge/library/kind/kc_{kind}.md\n')
            f.write(f'Knowledge card about: {kind}\n')
            f.write(f'Description: {desc}\n')
            f.write(f'Include YAML frontmatter: id: kc_{kind}, kind: knowledge_card, title, version: 1.0.0, quality: null\n')
        print(f'  Task: {nuc} -> kc_{kind}.md')
    print(f'  Generated {len(missing)} tasks')
else:
    print('  All kinds have KCs!')
" 2>&1

    if [ -f n03_task.md ] || [ -f n04_task.md ]; then
        bash _spawn/dispatch_aider.sh crew research 2>&1 | tail -3
        rm -f n03_task.md n04_task.md n01_task.md
    fi
}

# --- PHASE 4: Cascade -- try improving lowest-quality artifacts ---
phase_cascade() {
    log "PHASE 4: Cascade -- improve lowest quality artifacts"

    # Find an artifact with quality < 9.0
    TARGET=$(python -c "
import os, re
for root, dirs, files in os.walk('N01_intelligence'):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            content = open(path, encoding='utf-8', errors='ignore').read()
            m = re.search(r'quality:\s*([\d.]+)', content)
            if m and float(m.group(1)) < 8.5:
                print(path)
                exit()
" 2>/dev/null)

    if [ -n "$TARGET" ]; then
        log "  Target: $TARGET"
        cat > cascade_task.md << CEOF
Improve this file: $TARGET
1. Expand thin sections with more detail
2. Add tables where appropriate
3. Ensure all frontmatter fields are present
4. Improve density (tables > prose)
CEOF
        bash _spawn/dispatch_aider.sh cascade cascade_task.md 2>&1 | tail -3
        rm -f cascade_task.md
    else
        log "  No low-quality artifacts found"
    fi
}

# --- PHASE 5: Grid -- full parallel nucleus work ---
phase_grid() {
    log "PHASE 5: Grid -- parallel builds"

    # Generate tasks for all nuclei that have work
    python -c "
import json, os, random
km = json.load(open('.cex/kinds_meta.json', encoding='utf-8'))
existing = set(f.replace('kc_','').replace('.md','') for f in os.listdir('P01_knowledge/library/kind') if f.startswith('kc_'))
missing = [k for k in km if k not in existing]
random.shuffle(missing)

nuclei = ['n01','n02','n03','n04','n05','n06']
for i, kind in enumerate(missing[:6]):
    nuc = nuclei[i % 6]
    desc = km[kind].get('description', kind)
    with open(f'{nuc}_task.md', 'w') as f:
        f.write(f'Create file: P01_knowledge/library/kind/kc_{kind}.md\n')
        f.write(f'Knowledge card about: {kind}\n')
        f.write(f'Description: {desc}\n')
        f.write(f'Include YAML frontmatter: id: kc_{kind}, kind: knowledge_card, title, version: 1.0.0, quality: null\n')
    print(f'  {nuc} -> kc_{kind}.md')
print(f'  Generated {min(len(missing),6)} tasks')
" 2>&1

    TASK_COUNT=$(ls n0[1-6]_task.md 2>/dev/null | wc -l)
    if [ "$TASK_COUNT" -gt 0 ]; then
        bash _spawn/dispatch_aider.sh grid OVERNIGHT 2>&1 | tail -5
        rm -f n0[1-6]_task.md
    else
        log "  No tasks to dispatch"
    fi
}

# === MAIN LOOP ===
while true; do
    CYCLE=$((CYCLE + 1))
    if [ "$MAX_CYCLES" != "unlimited" ] && [ $CYCLE -gt "$MAX_CYCLES" ]; then
        break
    fi

    CYCLE_START=$(date +%s)
    log ""
    log "========== CYCLE $CYCLE / $MAX_CYCLES =========="

    phase_python_score
    phase_sweep
    phase_crew
    phase_cascade
    phase_grid

    CYCLE_TIME=$(( $(date +%s) - CYCLE_START ))
    TOTAL_TIME=$((TOTAL_TIME + CYCLE_TIME))

    # Count improvements
    NEW_COMMITS=$(git log --oneline --since="${CYCLE_TIME} seconds ago" | wc -l)
    TOTAL_IMPROVED=$((TOTAL_IMPROVED + NEW_COMMITS))

    log "CYCLE $CYCLE DONE: ${CYCLE_TIME}s, $NEW_COMMITS commits"
    log "RUNNING TOTAL: ${TOTAL_IMPROVED} improvements in ${TOTAL_TIME}s"

    # Brief pause between cycles
    sleep 5
done

echo ""
echo "============================================================"
echo "  Overnight Evolve Complete"
echo "  Cycles: $CYCLE | Improvements: $TOTAL_IMPROVED | Time: ${TOTAL_TIME}s"
echo "  Finished: $(date)"
echo "============================================================"
