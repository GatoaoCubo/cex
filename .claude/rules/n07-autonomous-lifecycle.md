---
glob: "**"
alwaysApply: true
description: "N07 autonomous lifecycle -- poll, kill, dispatch, consolidate without user intervention"
quality: 9.0
title: "N07-Autonomous-Lifecycle"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_cex_orchestration_architecture
  - n07_output_orchestration_audit
  - p01_kc_orchestration_best_practices
  - agent_card_n07
  - skill
  - p03_sp_admin_orchestrator
  - p03_sp_orchestration_nucleus
  - spec_infinite_bootstrap_loop
  - p12_wf_admin_orchestration
  - p08_ac_admin_orchestrator
---

# N07 Autonomous Lifecycle

## The Problem This Solves

N07 was dispatching nuclei but NOT:
1. Polling for completion signals
2. Killing completed/idle processes
3. Auto-dispatching next wave
4. Consolidating results

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
1. Use `git log --since` + `dispatch.sh status` (non-blocking, 2 seconds)
2. signal_watch is for `cex_mission_runner.py` (headless overnight runs), NOT for interactive N07

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
# - powershell with title "p - cex" (Claude Code/N07)
# - node started at same time as claude (Claude Code runtime)
# - cmd started at same time as claude (Claude Code shell)

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

1. Killing idle processes (do it autonomously after signal)
2. Dispatching next wave (do it after gate passes)
3. Running /status (N07 polls internally)
4. Running /consolidate (N07 does it after final wave)
5. Injecting context about spawn/stop mechanics (this rule IS the context)

## What N07 SHOULD Ask the User

1. GDP decisions (tone, audience, style) -- BEFORE first dispatch
2. Quality gate failures (artifact below 8.0) -- re-dispatch or accept?
3. Timeout situations (nucleus stuck > 45min) -- wait or kill?

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_orchestration_architecture]] | related | 0.52 |
| [[n07_output_orchestration_audit]] | related | 0.45 |
| [[p01_kc_orchestration_best_practices]] | related | 0.39 |
| [[agent_card_n07]] | related | 0.35 |
| [[skill]] | related | 0.34 |
| [[p03_sp_admin_orchestrator]] | related | 0.32 |
| [[p03_sp_orchestration_nucleus]] | related | 0.32 |
| [[spec_infinite_bootstrap_loop]] | related | 0.32 |
| [[p12_wf_admin_orchestration]] | related | 0.31 |
| [[p08_ac_admin_orchestrator]] | related | 0.31 |
