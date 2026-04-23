# CEX Spawn Playbook -- The Complete Operations Manual

**Version**: 2.0.0 | **Updated**: 2026-04-08 | **Runtime**: Claude Code native (all nuclei)

---

## GOLDEN RULE

```
N07 runs in Claude Code (orchestrator terminal).
Nuclei N01-N06 run in separate Claude Code windows (Windows CMD).
From N07, ONLY `bash _spawn/dispatch.sh` creates visible windows.
```

**NEVER from N07:**
- `start cmd /k ...` -- Windows CMD syntax, not bash
- `cmd /c boot\n03.ps1` -- wrong shell, wont open new window
- Direct `powershell -File ...` -- works but bypasses session tracking

**ALWAYS from N07:**
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
bash _spawn/dispatch.sh solo n03 "Read .cex/runtime/handoffs/n03_task.md and execute."

# All nuclei (all use Claude Code + Opus 4.6)
bash _spawn/dispatch.sh solo n01 "research task"     # claude opus-4-6
bash _spawn/dispatch.sh solo n02 "marketing task"    # claude opus-4-6
bash _spawn/dispatch.sh solo n03 "build task"        # claude opus-4-6
bash _spawn/dispatch.sh solo n04 "knowledge task"    # claude opus-4-6
bash _spawn/dispatch.sh solo n05 "code review"       # claude opus-4-6
bash _spawn/dispatch.sh solo n06 "pricing task"      # claude opus-4-6
```

---

## 2. GRID DISPATCH (up to 6 parallel)

### Pre-requisites: Write handoffs first
```
.cex/runtime/handoffs/
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
| claude   | claude   | claude   |
| research | market   | build    |
+----------+----------+----------+
|  N04     |  N05     |  N06     |  y=520  (bottom row)
| (0,520)  | (640,520)| (1280,520)|
| claude   | claude   | claude   |
| knowledge| ops      | commerce |
+----------+----------+----------+
Cell: 640x520px | Screen: 1920x1080 (WorkingArea: 1920x1040)
```

### Window Sizing for Different Monitors

| Resolution | Cell W | Cell H | Columns | Rows | Notes |
|------------|--------|--------|---------|------|-------|
| 1920x1080 | 640 | 520 | 3 | 2 | Primary setup |
| 2560x1440 | 853 | 720 | 3 | 2 | 1440p monitor |
| 3840x2160 | 960 | 540 | 4 | 4 | 4K -- up to 16 slots |
| 1366x768 | 683 | 384 | 2 | 2 | Laptop -- max 4 slots |

Formula: `cellW = screenW / columns`, `cellH = (screenH - taskbar) / rows`

---

## 3. CONTINUOUS BATCHING (>6 tasks)

When you have more tasks than slots:

### Handoff Naming (MANDATORY)
```
.cex/runtime/handoffs/{MISSION}_batch_{N}_{nucleus}.md
```

### How it works
```
Slot finishes -> signal in .cex/runtime/signals/
  -> Monitor detects (poll every 30s)
  -> Checks queue: more batches for this nucleus?
  -> Yes: dispatch next batch, zero idle time
  -> No: mark nucleus done, keep monitoring others
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
| Outputs in committed paths | .cex/runtime/pids/ is gitignored |
| Naming: {MISSION}_batch_{N}_{nucleus} | Monitor groups queues by pattern |

---

## 4. MONITORING

### Quick check
```bash
bash _spawn/dispatch.sh status
```

### What N07 checks (non-blocking)
```bash
git log --oneline --since="5 minutes ago"    # recent commits from nuclei
bash _spawn/dispatch.sh status               # process alive?
ls .cex/runtime/signals/signal_*             # completion signals
```

### Status meanings
| Status | Meaning | Action |
|--------|---------|--------|
| RUNNING | Process alive, working | Wait |
| COMPLETE | Signal received | Kill process, consolidate |
| STUCK | Alive but no activity for 15min | Investigate or respawn |
| CRASHED | Process died without signal | Respawn |

### Monitor detects 4 layers:
1. **Signal file**: .cex/runtime/signals/signal_{nucleus}_*.json
2. **Git commits**: commits with nucleus name since spawn
3. **Process alive**: CMD PID still running
4. **Stale detection**: alive + no signal + no commit for 15min = STUCK

---

## 5. PROCESS MANAGEMENT (Session-Aware v4.0)

Multiple N07 orchestrators can run simultaneously.
Each spawn records a session ID in the PID file.

```bash
# Stop MY session's nuclei only (safe -- default)
bash _spawn/dispatch.sh stop

# Stop specific nucleus (surgical)
bash _spawn/dispatch.sh stop n03

# Stop ALL nuclei (DANGEROUS -- kills other N07's processes too)
bash _spawn/dispatch.sh stop --all

# Preview what would be killed (safe)
bash _spawn/dispatch.sh stop --dry-run
```

### Kill Tree (correct method on Windows)
```bash
# CORRECT: taskkill with /T flag = tree-kill
taskkill /F /PID <pid> /T

# WRONG: Stop-Process -- does NOT kill child processes
# WRONG: dispatch.sh stop -- may not match orphaned processes
```

---

## 6. WAVE CYCLE (full orchestration lifecycle)

```
N07 Workflow:
  1. PLAN     -> /plan <goal> or write plan manually
  2. GUIDE    -> /guide (GDP: user decides WHAT, LLM decides HOW)
  3. HANDOFF  -> Write .cex/runtime/handoffs/{MISSION}_{nucleus}.md
  4. DISPATCH -> bash _spawn/dispatch.sh grid MISSION
  5. MONITOR  -> git log + dispatch.sh status (non-blocking)
  6. COLLECT  -> Verify deliverables exist
  7. STOP     -> bash _spawn/dispatch.sh stop
  8. COMMIT   -> git add + git commit -m "[N07] consolidate wave N"
  9. ARCHIVE  -> Move handoffs to archive
  10. REPEAT  -> Next wave with new handoffs
```

### Wave Pattern (multi-phase with dependencies)
```
Wave 1: N01 + N03 (research + build foundation)
  -> dispatch -> monitor -> complete -> stop -> commit
Wave 2: N04 + N02 (knowledge + marketing)
  -> dispatch -> monitor -> complete -> stop -> commit
Wave 3: N05 + N06 (operations + monetize)
  -> dispatch -> monitor -> complete -> stop -> commit
```

### Autonomous Mission Runner
```bash
python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --mission NAME --timeout 3600
```
Does: dispatch grid -> poll signals (blocking) -> stop -> quality gate -> consolidate.
Multi-wave: automatically chains waves, no user intervention needed.

---

## 7. HANDOFF TEMPLATE

```markdown
---
mission: MISSION_NAME
nucleus: n03
wave: 1
created: 2026-04-08T14:00:00-03:00
---

# N03 Task: {Title}

## Mission Context
Brief description of what this wave accomplishes.

## DECISIONS (from user)
See: .cex/runtime/decisions/decision_manifest.yaml

## Context (pre-loaded for you)
Your agent card: N03_engineering/agent_card_n03.md

## Relevant artifacts (READ these before producing)
1. archetypes/builders/{kind}-builder/ (13 ISOs)
2. P01_knowledge/library/kind/kc_{kind}.md

## Tasks
1. Task 1
2. Task 2

## Expected Output
1. File: {path}
2. Kind: {kind}
```

Nuclei commit and signal autonomously. No manual intervention needed.

---

## 8. BOOT SCRIPTS

Each nucleus has a boot script in `boot/`:

```cmd
@echo off
title CEX-N03 [claude+opus]
set CEX_NUCLEUS=N03
set CEX_ROOT=%~dp0..
cd /d "%CEX_ROOT%"
claude --dangerously-skip-permissions --permission-mode bypassPermissions --no-chrome --model claude-opus-4-6 ...
```

### CLI x Nucleus Matrix (all Claude Code, all Opus)

| Nucleus | Boot Script | CLI | Model | Context |
|---------|------------|-----|-------|---------|
| N07 | boot/cex.ps1 | claude | opus-4-6 | 1M |
| N01 | boot/n01.ps1 | claude | opus-4-6 | 1M |
| N02 | boot/n02.ps1 | claude | opus-4-6 | 1M |
| N03 | boot/n03.ps1 | claude | opus-4-6 | 1M |
| N04 | boot/n04.ps1 | claude | opus-4-6 | 1M |
| N05 | boot/n05.ps1 | claude | opus-4-6 | 1M |
| N06 | boot/n06.ps1 | claude | opus-4-6 | 1M |

---

## 9. OVERNIGHT / AFK OPERATION

### Setup for overnight continuous batching
```bash
# 1. Write all handoffs (e.g., 20 batch handoffs for n03)
# .cex/runtime/handoffs/OVERNIGHT_batch_{1..20}_n03.md

# 2. Launch continuous grid
bash _spawn/dispatch.sh grid OVERNIGHT continuous

# 3. Go AFK. Monitor auto-refills slots as they complete.

# 4. Next morning: check results
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

## 10. ERROR HANDLING

```bash
# STUCK: nucleus alive but no output for 15min
bash _spawn/dispatch.sh stop n03
# Simplify handoff, respawn

# CRASHED: process died without signal
bash _spawn/dispatch.sh stop
# Check git log for partial commits, respawn

# GIT CONFLICT: two nuclei edited same file
git status
# Use shared-file proposal pattern (see .claude/rules/shared-file-proposal.md)
# Lesson: handoffs must target different files
```

---

## FILES

| File | Purpose |
|------|---------|
| `_spawn/dispatch.sh` | Bash wrapper (N07 entry point) |
| `_spawn/spawn_solo.ps1` | PowerShell: spawn 1 nucleus + position |
| `_spawn/spawn_grid.ps1` | PowerShell: spawn grid + continuous batching |
| `_spawn/spawn_monitor.ps1` | PowerShell: signal + stuck detection |
| `_spawn/spawn_stop.ps1` | PowerShell: session-aware stop (v4.0) |
| `_tools/signal_writer.py` | Python: nuclei write completion signals |
| `boot/{nucleus}.cmd` | CMD: boot script per nucleus |
| `.cex/runtime/` | Runtime workspace (handoffs, signals, pids) |

---

*Playbook v2.0 -- Claude Code native. All nuclei Opus 4.6 1M. Session-aware dispatch v4.0. 2026-04-08.*
