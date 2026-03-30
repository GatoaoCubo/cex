# /consolidate — Collect, Verify, Stop, Commit

**Purpose**: N07 consolidation loop after nucleus dispatch completes.
**When**: After `dispatch.sh status` shows COMPLETE or after checking git log/signals.

---

## PROTOCOL

### Step 1: DETECT completion
```bash
# Check signals (new files since dispatch)
ls -lt .cex/runtime/signals/ | head -5

# Check git commits from nuclei
git log --oneline -10

# Check if CLI process still alive
powershell -Command "Get-Process claude,codex,gemini -EA SilentlyContinue | Select Id,ProcessName,CPU"
```

### Step 2: VERIFY quality
```bash
# Doctor health check
python _tools/cex_doctor.py

# Check for quality:null that should have been filled
grep -r "^quality: null" {TARGET_DIR}/ --include="*.md"

# Verify compilation happened
ls {TARGET_DIR}/compiled/*.yaml
```

### Step 3: STOP processes
```bash
bash _spawn/dispatch.sh stop
```

### Step 4: CONSOLIDATE
```bash
# Stage all changes from nucleus work
git add -A

# Review what changed
git diff --cached --stat

# Commit consolidation (N07 wrapper commit)
git commit -m "[N07] consolidate {MISSION} — {summary}"

# Push
git push
```

### Step 5: ARCHIVE handoff
```bash
# Move completed handoff to done
mv .cex/runtime/handoffs/{nucleus}_task.md .cex/runtime/handoffs/_done/
```

### Step 6: REPORT
Output summary:
```
=== CONSOLIDATION REPORT ===
Mission:    {name}
Nucleus:    {N0x}
Duration:   {X}min
Commits:    {N} by nucleus
Artifacts:  {N} modified
Doctor:     {PASS/WARN/FAIL}
Quality:    {score or null}
Status:     CONSOLIDATED ✅
```

---

## QUICK USAGE

After dispatching N03 and seeing it complete:
```
/consolidate
```

N07 runs all 6 steps automatically.

---

**Version**: 1.0.0 | **Origin**: codexa-core consolidate skill adapted for CEX
