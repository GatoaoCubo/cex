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
3. **STOP**: `bash _spawn/dispatch.sh stop`
4. **COMMIT** (if Gemini): `git add N0x_*/ && git commit -m "[N0x] ..."` (Gemini can't git)
5. **SIGNAL** (if Gemini): `python -c "from _tools.signal_writer import write_signal; ..."`
6. **REPORT**: Output consolidation summary

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
