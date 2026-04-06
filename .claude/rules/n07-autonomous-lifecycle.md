---
glob: "**"
alwaysApply: true
description: "N07 autonomous lifecycle -- poll, kill, dispatch, consolidate without user intervention"
---

# N07 Autonomous Lifecycle

## The Problem This Solves

N07 was dispatching nuclei but NOT:
- Polling for completion signals
- Killing completed/idle processes
- Auto-dispatching next wave
- Consolidating results

The user had to manually invoke /consolidate, /status, stop commands.
That defeats the purpose of an orchestrator.

## The Rule

**After ANY dispatch, N07 MUST enter the autonomous lifecycle loop.**
No user intervention required. No /commands needed.

## The Loop

```
DISPATCH wave
  |
  v
POLL (every 60s, up to 45min)
  |-- check .cex/runtime/signals/ for new signal files
  |-- check git log for nucleus commits
  |-- if nucleus signaled: KILL its processes immediately
  |
  v
GATE (all nuclei in wave signaled?)
  |-- YES: KILL any remaining processes, CONSOLIDATE, dispatch NEXT wave
  |-- NO: keep polling
  |-- TIMEOUT: report, ask user
  |
  v
CONSOLIDATE
  |-- verify deliverables exist
  |-- run cex_doctor.py
  |-- archive signals
  |-- clean PID file
  |
  v
NEXT WAVE (if exists)
  |-- write handoffs
  |-- dispatch
  |-- re-enter POLL loop
```

## How to Kill Processes (CORRECT METHOD)

```bash
# CORRECT: taskkill with /T flag = tree-kill (parent + all children)
taskkill /F /PID <pid> /T

# WRONG: Stop-Process -- does NOT kill child processes
# Stop-Process -Id <pid> -Force   # <-- ORPHANS claude.exe + node.exe

# WRONG: dispatch.sh stop -- uses session ID which may not match
# bash _spawn/dispatch.sh stop    # <-- unreliable for orphan cleanup
```

### Finding what to kill

```powershell
# List all claude/node/cmd processes with start times
Get-Process claude, node, cmd -EA SilentlyContinue |
    Select-Object Id, ProcessName, StartTime | Format-Table

# Identify MY processes (DO NOT KILL):
# - powershell with title "p - cex" (pi/N07)
# - node started at same time as pi (pi runtime)
# - cmd started at same time as pi (pi shell)

# Kill ALL except my own + actively working nuclei:
Get-Process claude -EA SilentlyContinue |
    Where-Object { $_.Id -ne <working_nucleus_pid> } |
    ForEach-Object { taskkill /F /PID $_.Id /T }
```

## Implementation in Practice

After dispatching a wave, N07 should:

1. Note the PIDs and start times of dispatched processes
2. Wait 60 seconds
3. Check for signals: `ls .cex/runtime/signals/signal_*_fullgrid_*.json`
4. Check git log: `git log --oneline --since="5 minutes ago"`
5. For each completed nucleus:
   a. Verify its deliverables exist (files listed in handoff)
   b. Kill its process tree: `taskkill /F /PID <pid> /T`
   c. Remove from PID tracking
6. When all nuclei in wave complete:
   a. Run `python _tools/cex_doctor.py` (quick health check)
   b. Archive wave signals
   c. Dispatch next wave
7. After final wave: full consolidation report

## What N07 Should NEVER Need the User For

- Killing idle processes (do it autonomously after signal)
- Dispatching next wave (do it after gate passes)
- Running /status (N07 polls internally)
- Running /consolidate (N07 does it after final wave)
- Injecting context about spawn/stop mechanics (this rule IS the context)

## What N07 SHOULD Ask the User

- GDP decisions (tone, audience, style) -- BEFORE first dispatch
- Quality gate failures (artifact below 8.0) -- re-dispatch or accept?
- Timeout situations (nucleus stuck > 45min) -- wait or kill?
