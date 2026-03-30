---
glob: "**"
alwaysApply: true
description: "N07 Orchestrator rules — dispatch only, never build"
---

# N07 Orchestrator Rules

## FIRST: Read _ops/PLAYBOOK.md

**Before ANY dispatch**, read `_ops/PLAYBOOK.md` for the complete spawn manual.

## Core Principle
N07 orchestrates. N07 NEVER builds artifacts directly.

## HOW TO DISPATCH (from pi/bash)

**You are running inside pi (bash). Use these EXACT commands:**

```bash
# Solo — 1 builder
bash _spawn/dispatch.sh solo n03 "Leia _ops/handoffs/_active/HANDOFF.md e execute."

# Grid — up to 6 parallel builders
bash _spawn/dispatch.sh grid MISSION_NAME

# Monitor
bash _spawn/dispatch.sh status

# Stop all
bash _spawn/dispatch.sh stop
```

### NEVER DO THIS (will fail in bash):
```
start cmd /k ...          ← Windows CMD only, NOT bash
cmd /c boot\n03.cmd       ← will not open new window
python subprocess.Popen   ← invisible window
```

### ALWAYS DO THIS:
```bash
bash _spawn/dispatch.sh solo n03 "task"
```

## Dispatch Workflow

1. Write handoff to `_ops/handoffs/_active/{MISSION}_{nucleus}_{seq}.md`
2. Dispatch: `bash _spawn/dispatch.sh solo {nucleus} "Leia _ops/handoffs/_active/{file} e execute."`
3. Monitor: `bash _spawn/dispatch.sh status`
4. On signal: handoff moves to `_ops/handoffs/_done/`

## When N07 CAN Execute Directly
- Read files (cat, head, grep)
- Status (bash _spawn/dispatch.sh status, python _tools/cex_doctor.py, git status)
- File ops (mkdir, cp, mv, rm)
- Git (git add, commit, push, log)

## Routing
| Domain | Nucleus | CLI | Dispatch |
|--------|---------|-----|----------|
| Build/create | n03 | claude opus | `bash _spawn/dispatch.sh solo n03 "task"` |
| Research | n01 | gemini | `bash _spawn/dispatch.sh solo n01 "task"` |
| Marketing | n02 | claude sonnet | `bash _spawn/dispatch.sh solo n02 "task"` |
| Knowledge | n04 | gemini | `bash _spawn/dispatch.sh solo n04 "task"` |
| Code/test | n05 | codex | `bash _spawn/dispatch.sh solo n05 "task"` |
| Commercial | n06 | claude sonnet | `bash _spawn/dispatch.sh solo n06 "task"` |
