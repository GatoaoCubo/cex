# 05 -- Grid Mission Dispatch

**Difficulty:** Advanced

## What it does

Demonstrates how N07 (Orchestrator) dispatches a grid mission:

1. Write handoff files for each nucleus
2. Dispatch all 6 nuclei in parallel via `dispatch.sh`
3. Monitor completion via signals and git log
4. Consolidate results

This is the highest-leverage pattern in CEX: 6 agents work simultaneously,
each following 8F, each producing artifacts in their domain.

## How to run

```bash
# Option A: Full CLI dispatch (requires Claude Code sessions)
python examples/05_grid_mission/main.py

# Option B: Use the /mission command in Claude Code
/mission build a developer community platform
```

## Architecture

```
N07 writes handoffs
    |
    +-- .cex/runtime/handoffs/DEVCOM_n01.md  (N01: research)
    +-- .cex/runtime/handoffs/DEVCOM_n02.md  (N02: marketing)
    +-- .cex/runtime/handoffs/DEVCOM_n03.md  (N03: engineering)
    +-- .cex/runtime/handoffs/DEVCOM_n04.md  (N04: knowledge)
    +-- .cex/runtime/handoffs/DEVCOM_n05.md  (N05: operations)
    +-- .cex/runtime/handoffs/DEVCOM_n06.md  (N06: commercial)
    |
    v
bash _spawn/dispatch.sh grid DEVCOM
    |
    +-- 6 parallel Claude Code sessions
    +-- Each reads its handoff, runs 8F, produces artifacts
    +-- Each signals completion via .cex/runtime/signals/
    |
    v
N07 consolidates: verify -> stop -> commit -> report
```

## Notes

- The `main.py` writes handoff files and shows the dispatch command.
  Actual dispatch requires `_spawn/dispatch.sh` (Bash + PowerShell).
- Grid dispatch is session-aware: multiple N07s can run simultaneously.
- Each nucleus auto-commits and signals on completion.
