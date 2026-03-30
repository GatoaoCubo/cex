# CEX Spawn Playbook — The Complete Operations Manual

**Version**: 1.0.0 | **Tested**: 2026-03-30 | **Runtime**: pi (bash) + claude/codex/gemini (CMD)

---

## GOLDEN RULE

```
N07 runs in PI (bash).
Nuclei N01-N06 run in CLI windows (Windows CMD).
From PI bash, ONLY `bash _spawn/dispatch.sh` creates visible windows.
```

**NEVER from pi bash:**
- `start cmd /k ...` — Windows CMD syntax, not bash
- `cmd /c boot\n03.cmd` — won't open new window
- `python subprocess.Popen(CREATE_NEW_CONSOLE)` — invisible window
- Direct `powershell -File ...` — works but verbose

**ALWAYS from pi bash:**
```bash
bash _spawn/dispatch.sh solo n03 "task"
bash _spawn/dispatch.sh grid MISSION
bash _spawn/dispatch.sh status
bash _spawn/dispatch.sh stop
```

---

## 1. SOLO DISPATCH (1 nucleus)

```bash
# Interactive (stays open)
bash _spawn/dispatch.sh solo n03 "Leia _ops/handoffs/_active/TASK.md e execute."

# All nuclei
bash _spawn/dispatch.sh solo n01 "research task"    # gemini
bash _spawn/dispatch.sh solo n02 "marketing task"   # claude sonnet
bash _spawn/dispatch.sh solo n03 "build task"       # claude opus
bash _spawn/dispatch.sh solo n04 "knowledge task"   # gemini
bash _spawn/dispatch.sh solo n05 "code review"      # codex
bash _spawn/dispatch.sh solo n06 "pricing task"     # claude sonnet
```

---

## 2. GRID DISPATCH (up to 6 parallel)

### Pre-requisites: Write handoffs first
```
_ops/handoffs/_active/
  MISSION_n01.md
  MISSION_n02.md
  MISSION_n03.md
  MISSION_n04.md
  MISSION_n05.md
  MISSION_n06.md
```

### Launch
```bash
# Static grid (all launch at once)
bash _spawn/dispatch.sh grid MISSION

# Continuous batching (auto-refill from queue)
bash _spawn/dispatch.sh grid MISSION continuous
```

### Grid Layout (2x3, 1920x1080)
```
+----------+----------+----------+
|  N01     |  N02     |  N03     |  y=0    (top row)
| (0,0)    | (640,0)  | (1280,0) |
| gemini   | sonnet   | opus     |
| research | market   | build    |
+----------+----------+----------+
|  N04     |  N05     |  N06     |  y=520  (bottom row)
| (0,520)  | (640,520)| (1280,520)|
| gemini   | codex    | sonnet   |
| knowledge| ops      | commerce |
+----------+----------+----------+
Cell: 640x520px | Screen: 1920x1080 (WorkingArea: 1920x1040)
```

### Window Sizing for Different Monitors

| Resolution | Cell W | Cell H | Columns | Rows | Notes |
|------------|--------|--------|---------|------|-------|
| 1920x1080 | 640 | 520 | 3 | 2 | Our setup (primary) |
| 2560x1440 | 853 | 720 | 3 | 2 | 1440p monitor |
| 3840x2160 | 960 | 540 | 4 | 4 | 4K — can do 16 slots! |
| 1366x768 | 683 | 384 | 2 | 2 | Laptop — max 4 slots |
| 1280x720 | 640 | 360 | 2 | 2 | Small laptop — max 4 |

Formula: `cellW = screenW / columns`, `cellH = (screenH - taskbar) / rows`

To customize: edit `$grid` in `_spawn/spawn_solo.ps1` and `_spawn/spawn_grid.ps1`.

---

## 3. CONTINUOUS BATCHING (>6 tasks)

When you have more tasks than slots:

### Handoff Naming (MANDATORY)
```
_ops/handoffs/_active/{MISSION}_batch_{N}_{nucleus}.md
```
Examples:
```
BUILD_batch_1_n03.md    BUILD_batch_2_n03.md    BUILD_batch_3_n03.md
BUILD_batch_1_n01.md    BUILD_batch_2_n01.md
```

### How it works
```
Slot finishes → signal in _ops/signals/
  → Monitor detects (poll every 30s)
  → Checks queue: more batches for this nucleus?
  → Yes: dispatch next batch, zero idle time
  → No: mark nucleus done, keep monitoring others
```

### Launch
```bash
bash _spawn/dispatch.sh grid BUILD continuous
```

### Rules
| Rule | Reason |
|------|--------|
| Max 10 tasks per batch handoff | Nuclei lose focus with too many |
| COMMIT section in every batch | Nucleus commits before signaling |
| SIGNAL section in every batch | Monitor depends on signals |
| Outputs in committed paths | _ops/temp/ is gitignored! |
| Naming: {MISSION}_batch_{N}_{nucleus} | Monitor groups queues by pattern |

### When to use Continuous vs Waves

| Condition | Mode |
|-----------|------|
| Tasks independent, >6 | Continuous batching |
| Tasks have dependencies (B needs A output) | Sequential waves |
| Mix of independent + dependent | Hybrid (CB for independent, waves for chains) |

---

## 4. MONITORING

### Quick check
```bash
bash _spawn/dispatch.sh status
```

### Spawn a dedicated monitor window (for overnight)
```bash
# Open a PowerShell window that polls every 30s
powershell -Command "Start-Process powershell -ArgumentList '-NoProfile','-Command','while(\$true){cls; powershell -File C:\Users\PC\Documents\GitHub\cex\_spawn\spawn_monitor.ps1; Start-Sleep 30}'"
```

### Status meanings
| Status | Meaning | Action |
|--------|---------|--------|
| RUNNING | Process alive, working | Wait |
| COMPLETE | Signal received | Nothing — done |
| STUCK | Alive but no activity for 15min | Stop + respawn or investigate |
| CRASHED | Process died without signal | Stop + respawn |

### Monitor detects 4 layers:
1. **Signal file**: _ops/signals/signal_{nucleus}_*.json
2. **Git commits**: commits with nucleus name since spawn
3. **Process alive**: CMD PID still running
4. **Stale detection**: alive + no signal + no commit for 15min = STUCK

---

## 5. OVERNIGHT / AFK OPERATION

### Setup for overnight continuous batching
```bash
# 1. Write all handoffs (e.g., 20 batch handoffs for n03)
# _ops/handoffs/_active/OVERNIGHT_batch_{1..20}_n03.md

# 2. Launch continuous grid
bash _spawn/dispatch.sh grid OVERNIGHT continuous

# 3. Open dedicated monitor (separate window)
powershell -Command "Start-Process powershell -ArgumentList '-NoProfile','-Command','while(\$true){cls; powershell -File C:\Users\PC\Documents\GitHub\cex\_spawn\spawn_monitor.ps1; Start-Sleep 30}'"

# 4. Go AFK. Monitor auto-refills slots as they complete.
# 5. Next morning: check results
bash _spawn/dispatch.sh status
git log --oneline -20
```

### Safety limits
| Parameter | Default | Override |
|-----------|---------|----------|
| Poll interval | 30s | `-pollSeconds 15` |
| Max runtime | 45min per slot | `-maxMinutes 120` |
| Max slots | 6 | `-maxSlots 3` (for RAM) |
| Stuck timeout | 15min | Hardcoded in monitor |

### RAM management
| Slots | Est. RAM | Use When |
|-------|----------|----------|
| 1 | ~2GB | Simple tasks |
| 3 | ~5GB | Long tasks (>30min) |
| 6 | ~8GB | Short tasks (<15min) |

---

## 6. WAVE CYCLE (full orchestration lifecycle)

```
N07 Workflow:
  1. PLAN     → Write _ops/plans/{MISSION}_{date}.md
  2. HANDOFF  → Write _ops/handoffs/_active/{MISSION}_{nucleus}_{seq}.md
  3. DISPATCH → bash _spawn/dispatch.sh grid MISSION
  4. MONITOR  → bash _spawn/dispatch.sh status (or dedicated window)
  5. COLLECT  → git log, check _ops/reports/
  6. STOP     → bash _spawn/dispatch.sh stop
  7. COMMIT   → git add . && git commit -m "[WAVE] ..." && git push
  8. ARCHIVE  → handoffs auto-moved to _ops/handoffs/_done/
  9. REPEAT   → Next wave with new handoffs
```

### Wave Pattern (multi-phase with dependencies)
```
Wave 1: N01 + N03 (research + build foundation)
  → dispatch → monitor → complete → stop → commit → push
Wave 2: N04 + N02 (knowledge + marketing)
  → dispatch → monitor → complete → stop → commit → push
Wave 3: N05 + N06 (test + monetize)
  → dispatch → monitor → complete → stop → commit → push
```

---

## 7. HANDOFF TEMPLATE

```markdown
# {NUCLEUS} Task: {Title}
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

## TAREFAS
1. Task 1
2. Task 2

## COMMIT (OBRIGATORIO)
git add -A
git commit -m "[{NUCLEUS}] {message}"

## SIGNAL
python -c "from _tools.signal_writer import write_signal; write_signal('{nucleus}', 'complete', 9.0, '{mission}')"
```

---

## 8. CUSTOMIZING BOOT SCRIPTS

Each nucleus has a boot script in `boot/`. To customize:

### Edit boot/{nucleus}.cmd
```cmd
@echo off
title CEX-{NUCLEUS}-{DOMAIN}        ← Window title
set CEX_NUCLEUS={NUCLEUS}            ← Identity
set CEX_ROOT=C:\Users\PC\Documents\GitHub\cex
cd /d "%CEX_ROOT%"

:: Choose CLI + model per nucleus:
:: claude: claude --model {model} --no-chrome
:: codex:  codex --dangerou
sly-bypass-approvals-and-sandbox
:: gemini: gemini -m gemini-2.5-pro --yolo

{CLI} {FLAGS} "%~1"
```

### CLI x Nucleus Matrix
| Nucleus | boot/ | CLI line | Model |
|---------|-------|----------|-------|
| n01 | n01.cmd | `gemini -m gemini-2.5-pro --yolo` | Gemini 1M ctx |
| n02 | n02.cmd | `claude --model sonnet` | Claude Sonnet |
| n03 | n03.cmd | `claude --model opus` | Claude Opus |
| n04 | n04.cmd | `gemini -m gemini-2.5-pro --yolo` | Gemini 1M ctx |
| n05 | n05.cmd | `codex --dangerously-bypass-approvals-and-sandbox` | GPT-5.4 |
| n06 | n06.cmd | `claude --model sonnet` | Claude Sonnet |

### Window Positioning
Edit `$grid` in `_spawn/spawn_solo.ps1`:
```powershell
$grid = @{
    n01 = @{x=0;    y=0}       # top-left
    n02 = @{x=640;  y=0}       # top-center
    n03 = @{x=1280; y=0}       # top-right
    n04 = @{x=0;    y=520}     # bottom-left
    n05 = @{x=640;  y=520}     # bottom-center
    n06 = @{x=1280; y=520}     # bottom-right
}
```

For different monitors, adjust x/y. Formula:
```
x = column * (screenWidth / numColumns)
y = row * ((screenHeight - taskbarHeight) / numRows)
```

Our setup: 1920x1080, taskbar 40px, WorkingArea 1920x1040.

---

## 9. ERROR HANDLING

```bash
# STUCK: nucleus alive but no output for 15min
bash _spawn/dispatch.sh stop
# Simplify handoff, respawn

# CRASHED: process died without signal
bash _spawn/dispatch.sh stop
# Check git log for partial commits, respawn

# GIT CONFLICT: two nuclei edited same file
git status
git merge --abort  # or resolve manually
# Lesson: handoffs must target different files
```

---

## 10. OVERNIGHT / AFK OPERATION

### Setup for overnight continuous batching
```bash
# 1. Write all batch handoffs
# _ops/handoffs/_active/OVERNIGHT_batch_{1..20}_n03.md

# 2. Launch continuous grid
bash _spawn/dispatch.sh grid OVERNIGHT continuous

# 3. Open dedicated monitor (separate window, polls every 30s)
powershell -Command "Start-Process powershell -ArgumentList '-NoProfile','-Command','while(1){cls; powershell -File _spawn/spawn_monitor.ps1; Start-Sleep 30}'"

# 4. Go AFK. Monitor auto-refills slots as they complete.

# 5. Next morning:
bash _spawn/dispatch.sh status
git log --oneline -20
```

### Safety limits
| Parameter | Default | Override |
|-----------|---------|----------|
| Poll interval | 30s | -pollSeconds 15 |
| Max runtime per slot | 45min | -maxMinutes 120 |
| Max parallel slots | 6 | -maxSlots 3 (save RAM) |

### RAM management
| Slots | Est. RAM | Use When |
|-------|----------|----------|
| 1 | ~2GB | Simple tasks |
| 3 | ~5GB | Long tasks (>30min) |
| 6 | ~8GB | Short tasks (<15min) |

---

## FILES

| File | Purpose |
|------|---------|
| `_spawn/dispatch.sh` | Bash wrapper (N07 uses THIS) |
| `_spawn/spawn_solo.ps1` | PowerShell: spawn 1 nucleus + position |
| `_spawn/spawn_grid.ps1` | PowerShell: spawn grid + continuous batching |
| `_spawn/spawn_monitor.ps1` | PowerShell: signal + stuck detection |
| `_spawn/spawn_stop.ps1` | PowerShell: kill all CLIs |
| `_tools/signal_writer.py` | Python: nuclei write completion signals |
| `boot/{nucleus}.cmd` | CMD: boot script per nucleus |
| `_ops/` | Operational workspace (handoffs, signals, plans, reports) |

---

*v1.0.0 -- Adapted from codexa-core SPAWN_PLAYBOOK v2.0.
Proven: grid 6/6, continuous batching 7/7, mixed 3-sat, overnight AFK.*
