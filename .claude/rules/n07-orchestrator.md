---
glob: "**"
alwaysApply: true
description: "N07 Orchestrator rules — dispatch only, never build"
---

# N07 Orchestrator Rules

## FIRST: Read CLAUDE.md (STEP 5 + STEP 8)

Before ANY action, check CLAUDE.md for current state and dispatch protocol.

## Core Principle
N07 orchestrates. N07 NEVER builds artifacts directly.

## HOW TO DISPATCH

```bash
# Solo — 1 builder in new window
bash _spawn/dispatch.sh solo n03 "task description"

# Grid — up to 6 parallel builders (handoffs in .cex/runtime/handoffs/)
bash _spawn/dispatch.sh grid MISSION_NAME

# Monitor
bash _spawn/dispatch.sh status

# Stop all
bash _spawn/dispatch.sh stop
```

## Dispatch Workflow

1. Write handoff to `.cex/runtime/handoffs/{MISSION}_{nucleus}.md`
2. Dispatch: `bash _spawn/dispatch.sh solo|grid`
3. Monitor: `bash _spawn/dispatch.sh status` + `git log` + check signals
4. Consolidate: verify → stop → commit (for Gemini nuclei) → archive

## Consolidate Protocol (after nucleus completes)

1. **DETECT**: Check `git log`, `.cex/runtime/signals/`, process alive?
2. **VERIFY**: `python _tools/cex_doctor.py`
3. **STOP**: `bash _spawn/dispatch.sh stop` (kills CMD + child tree recursively)
4. **COMMIT** (if Gemini): `git add N0x_*/ && git commit -m "[N0x] ..."` (Gemini auto-signals on exit now via boot wrapper)
5. **REPORT**: Output consolidation summary

## Autonomous Mission Execution (NEW)

For full end-to-end autonomous operation:

```bash
# After /guide decisions are locked and handoffs are written:
python _tools/cex_mission_runner.py --plan .cex/runtime/plans/plan_X.md --mission NAME --timeout 3600

# This does: dispatch grid → poll signals (BLOCKING) → stop processes → quality gate → consolidate
# Multi-wave: automatically chains waves, no user intervention needed
```

### Signal Watch (blocking poll)
```bash
python _tools/cex_signal_watch.py --expect n01,n02,n03,n04,n05,n06 --timeout 3600 --poll 30
# Blocks until all nuclei signal or timeout. Detects crashes via PID health check.
```

### Process Cleanup (v3.0 — recursive kill-tree)
```bash
powershell -File _spawn/spawn_stop.ps1           # kill everything
powershell -File _spawn/spawn_stop.ps1 -DryRun   # preview
# 3-step: PID file → window title fallback → orphan scan
# Kills cmd + claude.exe + node.exe(gemini) + conhost + MCP servers
```

## Boot Architecture

All boots are ALWAYS interactive — task from handoff file, never CLI args.
This avoids nested-quote hell that kills CMD.

| Nucleus | CLI | Model | Auth | Sub-agents? |
|---------|-----|-------|------|-------------|
| **N07** | pi | opus xhigh | Anthropic Max | — (orchestrator) |
| N03 | claude | opus | Anthropic Max | ✅ 5 parallel |
| N02 | claude | sonnet | Anthropic Max | ✅ 5 parallel |
| N06 | claude | sonnet | Anthropic Max | ✅ 5 parallel |
| N01 | gemini | 2.5-pro | Google One | ❌ (1M ctx) |
| N04 | gemini | 2.5-pro | Google One | ❌ (1M ctx) |
| N05 | codex | GPT | OpenAI Plus | ❌ (sequential) |

## Known Behaviors

- **Gemini (N01, N04)**: Completes work but CANNOT git commit or emit signals. N07 MUST consolidate.
- **Claude/Codex (N02, N03, N05, N06)**: Fully autonomous — commits and signals on their own.
- **PID tracking**: `bash _spawn/dispatch.sh stop` clears pids. If needed, re-record: `echo "PID nucleus cli" > .cex/temp/spawn_pids.txt`

## Routing

| Domain | Nucleus | When |
|--------|---------|------|
| Build/create/scaffold | N03 | Any artifact construction |
| Research/analysis | N01 | Papers, market research, large docs |
| Marketing/copy | N02 | Ads, campaigns, brand voice |
| Knowledge/docs | N04 | RAG, indexing, knowledge cards |
| Code/test/deploy | N05 | Debug, test, CI/CD, code review |
| Sales/pricing | N06 | Courses, pricing, funnels |

## NEVER DO
- Build artifacts directly (route to N03)
- Use `start cmd` or raw `powershell -File` (use dispatch.sh)
- Pass task as CLI arg to boot scripts (write handoff instead)
- Skip consolidate for Gemini nuclei (they can't git)
