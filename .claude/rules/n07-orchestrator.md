---
glob: "**"
alwaysApply: true
description: "N07 Orchestrator rules — dispatch only, never build"
quality: 9.0
title: "N07-Orchestrator"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# N07 Orchestrator Rules

## FIRST: Read CLAUDE.md (STEP 5 + STEP 8)

Before ANY action, check CLAUDE.md for current state and dispatch protocol.

## Reasoning Protocol
- 8F is your reasoning protocol (see `.claude/rules/8f-reasoning.md`).
  Even orchestration follows F1→F8: constrain scope, become orchestrator,
  inject mission context, reason about waves, call tools, produce handoffs,
  govern dispatch validity, collaborate by monitoring and consolidating.

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

# Stop MY session's nuclei only (safe — other N07s untouched)
bash _spawn/dispatch.sh stop

# Stop specific nucleus (surgical)
bash _spawn/dispatch.sh stop n03

# Stop ALL nuclei (DANGEROUS — kills other N07's processes too)
bash _spawn/dispatch.sh stop --all

# Preview what would be killed (always safe)
bash _spawn/dispatch.sh stop --dry-run
```

## Session-Aware Process Management (v4.0)

Multiple N07 orchestrators can run simultaneously on the same machine.
Each spawn records a **session ID** in the PID file:
```
{cmd_pid} {nucleus} {cli} {session_id} {timestamp}
```

**Rules:**
- `stop` = kills only MY session's nuclei (default, safe)
- `stop n03` = kills only that nucleus regardless of session (surgical)
- `stop --all` = kills everything including other N07's nuclei (explicit, dangerous)
- **NEVER** use `Get-Process claude | Stop-Process` — kills ALL claude processes globally

## Dispatch Workflow

1. Write handoff to `.cex/runtime/handoffs/{MISSION}_{nucleus}.md`
   **AND** copy to `n0X_task.md` (boot scripts read this file)
2. Dispatch: `bash _spawn/dispatch.sh solo|grid`
3. Monitor: `bash _spawn/dispatch.sh status` + `git log` + check signals
4. Consolidate: verify → stop → commit (for Gemini nuclei) → archive

## Consolidate Protocol (after nucleus completes)

1. **DETECT**: Check `git log`, `.cex/runtime/signals/`, process alive?
2. **VERIFY**: `python _tools/cex_doctor.py`
3. **STOP**: `bash _spawn/dispatch.sh stop` (kills MY session's CMD + child tree only)
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

### Process Cleanup (v4.0 — session-aware recursive kill-tree)
```bash
bash _spawn/dispatch.sh stop              # MY session only (safe)
bash _spawn/dispatch.sh stop n03          # specific nucleus (surgical)
bash _spawn/dispatch.sh stop --all        # everything (dangerous, explicit)
bash _spawn/dispatch.sh stop --dry-run    # preview
# Kill-Tree: cmd → claude.exe → node.exe(MCP) → uvx → uv → mcp-server → python
# Session-tracked: PID file has {pid} {nucleus} {cli} {session_id} {timestamp}
```

## Boot Architecture

All boots are ALWAYS interactive — task from handoff file, never CLI args.
This avoids nested-quote hell that kills CMD.

| Nucleus | CLI | Model | Auth | Sub-agents? |
|---------|-----|-------|------|-------------|
| **N07** | claude | opus-4-6 1M | Anthropic Max | — (orchestrator) |
| N01 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |
| N02 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |
| N03 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |
| N04 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |
| N05 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |
| N06 | claude | opus-4-6 1M | Anthropic Max | ✅ 5 parallel |

## Known Behaviors

- **All nuclei are Claude/Opus**: Fully autonomous — commit and signal on their own.
- **PID tracking**: Session-tagged. Format: `{pid} {nucleus} {cli} {session_id} {timestamp}`. File: `.cex/runtime/pids/spawn_pids.txt`
- **Multi-N07 safe**: `stop` only kills YOUR session. Other N07 orchestrators are untouched.

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
