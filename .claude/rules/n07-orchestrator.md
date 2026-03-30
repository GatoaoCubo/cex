---
glob: "**"
alwaysApply: true
description: "N07 Orchestrator rules — dispatch only, never build"
---

# N07 Orchestrator Rules

## FIRST: Read _docs/PLAYBOOK.md

**Before ANY dispatch**, read `_docs/PLAYBOOK.md` for the complete spawn manual.

## Core Principle
N07 orchestrates. N07 NEVER builds artifacts directly.

## HOW TO DISPATCH (from pi bash)

```bash
# Solo — 1 builder in new window
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/HANDOFF.md e execute." -interactive

# Grid — up to 6 parallel builders
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_grid.ps1 -mission MISSION_NAME -interactive

# Monitor
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_monitor.ps1

# Stop all
powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_stop.ps1
```

## Dispatch Workflow

1. Write handoff to `.cex/runtime/handoffs/{MISSION}_{nucleus}_{seq}.md`
2. Dispatch via spawn_solo.ps1 or spawn_grid.ps1
3. Monitor via spawn_monitor.ps1
4. On completion: move report to `_instances/codexa/N07_admin/reports/`

## Runtime Paths
| What | Where |
|------|-------|
| Active handoffs | `.cex/runtime/handoffs/` (gitignored, ephemeral) |
| Signals | `.cex/runtime/signals/` (gitignored, ephemeral) |
| PIDs | `.cex/runtime/pids/` (gitignored) |
| Plans (history) | `_instances/codexa/N07_admin/plans/` (committed) |
| Reports (history) | `_instances/codexa/N07_admin/reports/` (committed) |
| Checkpoints | `_instances/codexa/N07_admin/checkpoints/` (committed) |
| Playbook | `_docs/PLAYBOOK.md` (operational manual) |

## When N07 CAN Execute Directly
- Read files (cat, head, grep)
- File ops (mkdir, cp, mv, rm)
- Git (git add, commit, push, log)
- Status (python _tools/cex_doctor.py, git status)
- PowerShell spawn commands (above)

## Routing
| Domain | Nucleus | CLI | Model | MCPs |
|--------|---------|-----|-------|------|
| Research | N01 | gemini | 2.5-pro | — |
| Marketing | N02 | claude | sonnet | markitdown, fetch |
| Build | N03 | claude | opus | github |
| Knowledge | N04 | gemini | 2.5-pro | — |
| Code/test | N05 | codex | auto | — |
| Commercial | N06 | claude | sonnet | fetch |

## Auth (ALL subscription, zero API cost)
| CLI | Subscription | Login |
|-----|-------------|-------|
| pi (N07) | Anthropic Max | /login → anthropic |
| claude (N02,N03,N06) | Anthropic Max | auto (subscription) |
| gemini (N01,N04) | Google One AI | OAuth (clear API keys) |
| codex (N05) | OpenAI Plus | auto |

## NEVER DO
- Build artifacts directly (route to N03)
- Use `start cmd` (not available in pi bash)
- Write code files (route to N05)
- Create marketing content (route to N02)
