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

## The Loop (NON-BLOCKING — N07 never idles)

```
DISPATCH wave
  |
  v
WORK + MONITOR (interleaved, never blocking)
  |
  |-- DO: investigate, hydrate specs, write memory, plan next wave
  |     (N07 always has a backlog — architecture audits, spec updates,
  |      decision manifests, terminology checks, gap analysis)
  |
  |-- CHECK (every 2-3 own-tasks, ~2 seconds):
  |     git log --oneline --since="3 minutes ago"
  |     bash _spawn/dispatch.sh status
  |     (detect nucleus commits or signal completion)
  |
  |-- If nucleus committed: note it, continue own work
  |-- If ALL wave nuclei committed: CONSOLIDATE + DISPATCH next wave
  |-- If stuck >15min with no commits: investigate (check PID alive)
  |
  v
CONSOLIDATE (when wave complete)
  |-- verify deliverables exist
  |-- kill idle processes (only completed ones!)
  |-- run cex_doctor.py
  |-- git add + commit consolidation
  |
  v
NEXT WAVE
  |-- write handoffs
  |-- dispatch
  |-- IMMEDIATELY return to WORK + MONITOR
```

### ANTI-PATTERN: signal_watch blocking

**NEVER** run `python _tools/cex_signal_watch.py` as a blocking call.
It freezes N07 for minutes. Instead:
- Use `git log --since` + `dispatch.sh status` (non-blocking, 2 seconds)
- signal_watch is for `cex_mission_runner.py` (headless overnight runs), NOT for interactive N07

### What N07 works on while nuclei run

Always maintain a backlog. If backlog is empty, generate one:
1. Read a spec and verify it matches reality
2. Audit a pillar schema against industry terms
3. Write/update a memory file
4. Check artifact counts and quality distribution
5. Plan the next mission's waves
6. Update CLAUDE.md or metaphor dictionary
7. Investigate a new industry pattern

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
