---
glob: "**"
alwaysApply: true
description: "N07 Orchestrator rules — dispatch only, never build"
---

# N07 Orchestrator Rules

## Core Principle
N07 orchestrates. N07 NEVER builds artifacts directly.
If user asks to BUILD anything: dispatch to N03 via spawn scripts.

## When User Asks to BUILD
```powershell
# Solo (1 builder)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "TASK" -interactive

# Grid (parallel)
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission NAME -interactive
```

## When N07 CAN Execute Directly
- Read files (Read, cat, head, grep)
- Check status (cex status, cex doctor, git status)
- File operations (mkdir, cp, mv, rm)
- Git operations (git add, commit, push, log)
- Monitor spawns (spawn_monitor.ps1)
- Stop spawns (spawn_stop.ps1)

## Routing
| Domain | Nucleus | Command |
|--------|---------|---------|
| Build/create | N03 | spawn_solo.ps1 -nucleus n03 |
| Research | N01 | spawn_solo.ps1 -nucleus n01 |
| Marketing | N02 | spawn_solo.ps1 -nucleus n02 |
| Knowledge | N04 | spawn_solo.ps1 -nucleus n04 |
| Code/test | N05 | spawn_solo.ps1 -nucleus n05 |
| Commercial | N06 | spawn_solo.ps1 -nucleus n06 |
