---
id: p01_kc_cex_orchestration_architecture
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "CEX Orchestration Architecture -- Multi-Process Pattern for LLM Agent Coordination"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n01_intelligence
domain: meta
quality: 9.2
tags: [orchestration, multi-process, ipc, signals, handoffs, architecture, meta, dispatch, session]
tldr: "CEX spawns independent CLI processes (one per nucleus) coordinated through file-based IPC -- handoffs, signals, PIDs -- not in-process threads or function calls"
when_to_use: "Understanding how CEX coordinates multiple LLM agents; comparing to CrewAI/AutoGen/LangGraph; debugging orphan processes; designing new dispatch patterns"
keywords: [dispatch, spawn, signal, handoff, session-aware, taskkill, process-tree, file-ipc, nucleus, pid]
feeds_kinds: [knowledge_card, instruction, system_prompt, workflow, daemon]
linked_artifacts:
  - _spawn/dispatch.sh
  - _spawn/spawn_solo.ps1
  - _spawn/spawn_stop.ps1
  - _spawn/spawn_grid.ps1
  - _tools/signal_writer.py
  - _tools/cex_signal_watch.py
  - _tools/cex_mission_runner.py
  - boot/n03.cmd
  - .cex/runtime/pids/spawn_pids.txt
  - .claude/rules/n07-orchestrator.md
  - .claude/rules/n07-autonomous-lifecycle.md
density_score: null
related:
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p08_ac_orchestrator
  - bld_knowledge_card_nucleus_def
  - p12_wf_orchestration_pipeline
  - p01_kc_orchestration
  - p02_agent_admin_orchestrator
  - dispatch
  - p12_sc_admin_orchestrator
  - p12_wf_admin_orchestration
---

# CEX Orchestration Architecture

## What It Is

CEX coordinates up to 7 LLM agents (nuclei N01-N07) as **independent OS processes**, each running in its own CMD window with its own CLI session. N07 (the orchestrator) never builds artifacts -- it dispatches tasks, polls for completion, kills finished processes, and chains waves. Communication happens entirely through the filesystem: handoff files carry tasks, signal files confirm completion, and PID files track process ownership.

This is fundamentally different from in-process orchestration frameworks. Each nucleus is a separate `claude` CLI invocation with its own context window, its own MCP server connections, and its own git access. If one nucleus crashes, the others continue. If the orchestrator crashes, nuclei finish their work and signal anyway.

## The Spawn Model

### How N07 Dispatches a Nucleus

```
N07 (Claude Code CLI) ──> dispatch.sh solo n03 "task"
                    │
                    ├── Write handoff: .cex/runtime/handoffs/n03_task.md
                    ├── Kill any existing N03 (kill-before-spawn)
                    ├── Read nucleus_models.yaml for CLI + model
                    │
                    └── Start-Process cmd /k boot/n03.cmd
                          │
                          ├── Set window title: CEX-N03-BUILDER
                          ├── Set window color: 1F (blue)
                          ├── Set CEX_NUCLEUS=N03
                          │
                          └── claude -p [flags] "...read handoff..."
                                │
                                ├── Reads n03_task.md
                                ├── Executes 8F pipeline
                                ├── git commit results
                                ├── Writes signal JSON
                                └── Process exits (auto)
```

### The `-p` Mode Auto-Exit Pattern

Every boot script runs the CLI in **`-p` (pipe/prompt) mode**, not interactive mode. This is the critical design choice:

```cmd
claude -p %FLAGS% %MODEL% %MCP% %SETTINGS% --name N03-Builder "...prompt..."
```

In `-p` mode, `claude` reads the prompt, executes the work (including tool calls, file edits, git commits), then **exits automatically**. No human interaction needed. The CMD window stays open after exit only for the `pause` command at the end of the boot script, which lets the operator inspect output before the window closes.

This differs from interactive mode (`claude` without `-p`) where the CLI waits for user input in a REPL loop. Interactive mode would require a human at each terminal -- defeating the purpose of autonomous dispatch.

### Grid Dispatch (Parallel Waves)

For multi-nucleus missions, `dispatch.sh grid MISSION` reads handoff files from `.cex/runtime/handoffs/` and spawns all nuclei simultaneously. Each nucleus window is positioned in a 2x3 grid on screen using Win32 `MoveWindow`:

```
┌──────────┬──────────┬──────────┐
│ N01      │ N02      │ N03      │
│ (0,0)    │ (640,0)  │ (1280,0) │
├──────────┼──────────┼──────────┤
│ N04      │ N05      │ N06      │
│ (0,520)  │ (640,520)│ (1280,520│
└──────────┴──────────┴──────────┘
```

## File-Based IPC

CEX uses **no sockets, no message queues, no shared memory, no API calls** between processes. All inter-process communication flows through files on disk, version-controlled by git.

### Handoff Files (Task Input)

```
Path: .cex/runtime/handoffs/{nucleus}_task.md
Direction: N07 -> nucleus
Format: YAML frontmatter + markdown body
Contains: task description, decision manifest reference, completion instructions
```

Written by `spawn_solo.ps1` before the nucleus boots. The nucleus prompt says "read and execute the handoff file immediately." The handoff includes a `## DECISIONS` section pointing to `decision_manifest.yaml` so nuclei never re-ask the user.

### Signal Files (Completion Output)

```
Path: .cex/runtime/signals/signal_{nucleus}_{timestamp}.json
Direction: nucleus -> N07
Format: JSON
Contains: nucleus, status, quality_score, mission, timestamp
```

Written by the nucleus at the end of its work via `signal_writer.py`. N07 polls this directory to detect completion. Each signal is a separate timestamped file -- never overwritten, never deleted during a mission (archived after consolidation).

Example signal:
```json
{
  "nucleus": "n03",
  "status": "complete",
  "quality_score": 9.0,
  "mission": "BRAND_LAUNCH",
  "timestamp": "2026-04-06T14:32:01+00:00"
}
```

### PID Files (Process Tracking)

```
Path: .cex/runtime/pids/spawn_pids.txt
Format: {cmd_pid} {nucleus} {cli} {session_id} {timestamp}
Example: 14320 n03 claude s1743900123 2026-04-06_14:30:01
```

Each spawned process appends one line. Used for three purposes:
1. **Kill-before-spawn**: When respawning a nucleus, kill the old PID first
2. **Session filtering**: `stop` only kills PIDs with matching session ID
3. **Crash detection**: `cex_signal_watch.py` checks if PIDs are still alive

## Session-Aware Process Management

### The Problem

Multiple orchestrators (N07 instances) can run simultaneously on the same machine -- one running a build mission, another doing brand work. A naive `stop` command would kill all of them.

### The Solution

Each dispatch session gets a stable identifier stored in `.cex/runtime/pids/.my_session`:

```bash
# Generated once per N07 session, inherited by all dispatches
export CEX_SESSION_ID="s$(date +%s)"   # e.g., s1743900123
```

PID entries include the session ID:
```
14320 n03 claude s1743900123 2026-04-06_14:30:01
15100 n01 claude s1743900456 2026-04-06_14:35:22   # different session
```

Stop commands filter by session:
- `stop` -- kills only MY session's nuclei (default, safe)
- `stop n03` -- kills N03 regardless of session (surgical, explicit)
- `stop --all` -- kills every CEX process on the machine (dangerous)
- `stop --dry-run` -- preview without killing

### Process Tree Killing

Windows processes form trees: `cmd.exe` spawns `claude.exe`, which spawns `node.exe` (MCP servers), which may spawn `uvx`, `uv`, `python` (MCP server runtimes).

```
cmd.exe (boot/n03.cmd)
  └── claude.exe (CLI)
        ├── node.exe (MCP: filesystem)
        ├── node.exe (MCP: github)
        └── uvx.exe (MCP: custom)
              └── python.exe (server)
```

Killing only `claude.exe` orphans the node/python children. CEX uses `taskkill /F /PID {pid} /T` where `/T` means **tree-kill** -- the parent and all descendants die together.

## The Autonomous Lifecycle Loop

After dispatching a wave, N07 enters a poll-gate-kill-consolidate loop:

```
DISPATCH wave (1-6 nuclei)
       │
       ▼
POLL every 30-60s:
  ├── ls .cex/runtime/signals/ for new signal files
  ├── git log --since="5min" for nucleus commits
  └── check PID aliveness (crash detection)
       │
       ▼
GATE: all nuclei signaled?
  ├── YES: proceed to CONSOLIDATE
  ├── NO:  keep polling
  └── TIMEOUT (45min): report, ask user
       │
       ▼
CONSOLIDATE:
  ├── Verify deliverables exist (files from handoff)
  ├── Run cex_doctor.py (health check)
  ├── Kill remaining processes (tree-kill)
  ├── Archive signals and handoffs
  └── Dispatch NEXT wave (if multi-wave mission)
```

The `cex_signal_watch.py` tool implements the blocking poll: it checks signals + PID health every N seconds, returns when all expected nuclei have signaled or a crash/timeout occurs. The `cex_mission_runner.py` wraps the full lifecycle: handoffs, dispatch, poll, stop, quality gate, consolidate, next wave.

## How This Differs from In-Process Frameworks

| Dimension | CEX (multi-process) | CrewAI / AutoGen / LangGraph |
|-----------|--------------------|-----------------------------|
| **Process model** | Independent OS processes, one per agent | Single Python process, agents as objects/threads |
| **Isolation** | Full -- separate context windows, separate crashes | Shared memory, one crash kills all |
| **Communication** | File-based (handoffs, signals, git) | In-memory function calls, message passing |
| **Context window** | Each nucleus gets its own 1M tokens | Shared or partitioned within one window |
| **State persistence** | Git commits -- survives any crash | In-memory -- lost on crash unless checkpointed |
| **Debugging** | Read the files, check git log | Attach debugger, parse logs |
| **Scaling** | One machine, 6 parallel windows | Single process, async coroutines |
| **Orchestrator coupling** | Loose -- nuclei finish even if N07 crashes | Tight -- orchestrator death kills agents |
| **Tool access** | Each nucleus has its own MCP servers | Shared tool registry |
| **Recovery** | Resume by re-reading signals + git | Re-run from checkpoint (if implemented) |

### Why CEX Chose Multi-Process

1. **LLM CLI tools are designed as processes.** `claude`, `gemini`, `codex` are CLI binaries, not Python libraries. Running them as subprocesses is the natural integration.
2. **Context window isolation.** A 1M-token context per nucleus means each agent has full space to load ISOs, knowledge, and examples without competing for tokens.
3. **Crash isolation.** When N03 hits a bug, N01/N02/N04/N05/N06 keep working. No shared state to corrupt.
4. **Observable.** Each nucleus has a visible CMD window with color-coded title. The operator can watch all 6 agents working simultaneously.
5. **Git as the integration bus.** Every nucleus commits its work. Git log becomes the activity feed. Merge conflicts are the coordination protocol.

### The Tradeoff

Multi-process is heavier. Spawning 6 CLI sessions takes 10-15 seconds. File I/O for IPC adds latency (though signals are < 1KB). And Windows process management requires careful tree-killing. For simple two-agent conversations, in-process is faster. For complex multi-domain missions with 6 specialist agents, the isolation benefits dominate.

## Anti-Patterns Discovered

### 1. Stop-Process vs taskkill /T

**Bad:** `Stop-Process -Id $pid -Force`
Kills only the target process. On Windows, child processes (claude.exe, node.exe, python.exe) are orphaned and keep running, consuming resources and holding file locks.

**Good:** `taskkill /F /PID $pid /T`
The `/T` flag tree-kills: walks the process tree and terminates every descendant before the parent.

**Discovery:** After multiple missions, the machine had 20+ orphaned node.exe processes from killed CLI sessions. Each held open MCP server sockets. New nuclei failed to bind to those ports.

### 2. Encoding Crashes in Print Output

**Bad:** Using Unicode characters (em-dashes, smart quotes, emoji) in Python `print()` statements.

Windows CMD windows default to cp1252 encoding. Python's `print()` uses the terminal codec. Any non-ASCII character triggers `UnicodeEncodeError` and crashes the nucleus mid-work.

**Good:** ASCII-only executable code. Use `[OK]`, `[FAIL]`, `[WARN]` instead of emoji. Use `--` instead of em-dash. Enforce via pre-commit hook (`cex_hooks.py`) and sanitizer (`cex_sanitize.py`).

**Discovery:** N03 crashed silently during a grid mission. Signal never written. N07 waited 45 minutes before timeout. Root cause: a log message with an em-dash character.

### 3. Orphan Processes After Crash

**Bad:** Assuming `dispatch.sh stop` catches everything. If a nucleus crashes before registering its PID, or if the PID file is corrupted, stop misses it.

**Good:** The stop script has 3 layers:
1. **PID file** -- primary, session-filtered
2. **Window title scan** -- catches processes spawned outside dispatch (only with `--all`)
3. **Orphan CLI scan** -- finds claude.exe/codex.exe with no parent CMD (only with `--all`)

**Discovery:** After a power interruption, PID file was truncated. Orphan nuclei kept running and committing to git, creating merge conflicts with the next mission.

### 4. Passing Task as CLI Argument

**Bad:** `claude -p "Build a knowledge card about...very long task..."`. Nested quotes in CMD are fragile. Special characters (`&`, `|`, `>`, `<`) break argument parsing.

**Good:** Write the task to a handoff file. The boot prompt says "read .cex/runtime/handoffs/n03_task.md and execute." No argument escaping needed.

**Discovery:** A task containing `&` was interpreted as a CMD operator, splitting the claude invocation into two commands. The nucleus received a truncated prompt and built garbage.

### 5. Interactive Mode for Autonomous Work

**Bad:** Launching `claude` without `-p` and expecting it to self-terminate. In interactive mode, the CLI waits for human input at the REPL -- the nucleus hangs forever.

**Good:** Always use `-p` mode for dispatched work. The nucleus receives the prompt, executes all tool calls autonomously, then exits. The boot script's `pause` at the end keeps the window open for inspection only.

**Discovery:** Early grid dispatches used interactive mode. All 6 windows sat waiting for input. The operator had to type in each window manually -- worse than having no orchestration at all.

## Key Files Reference

| File | Role |
|------|------|
| `_spawn/dispatch.sh` | Bash entry point: routes solo/grid/status/stop |
| `_spawn/spawn_solo.ps1` | Spawns one nucleus: write handoff, kill old, start cmd, record PID |
| `_spawn/spawn_grid.ps1` | Spawns all nuclei for a mission in parallel |
| `_spawn/spawn_stop.ps1` | Session-aware process termination (3 layers) |
| `_spawn/spawn_monitor.ps1` | Live status of running nuclei |
| `boot/n0{1-6}.cmd` | Per-nucleus boot: color, title, env, claude -p |
| `_tools/signal_writer.py` | Write completion signal JSON |
| `_tools/cex_signal_watch.py` | Blocking poll for nucleus signals |
| `_tools/cex_mission_runner.py` | Full autonomous lifecycle: waves, dispatch, poll, gate, consolidate |
| `.cex/runtime/handoffs/` | Task input files (N07 -> nucleus) |
| `.cex/runtime/signals/` | Completion output files (nucleus -> N07) |
| `.cex/runtime/pids/spawn_pids.txt` | Session-tagged process registry |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | sibling | 0.46 |
| [[p03_sp_orchestration_nucleus]] | downstream | 0.42 |
| [[p08_ac_orchestrator]] | downstream | 0.41 |
| [[bld_knowledge_card_nucleus_def]] | sibling | 0.40 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.40 |
| [[p01_kc_orchestration]] | sibling | 0.39 |
| [[p02_agent_admin_orchestrator]] | downstream | 0.38 |
| [[dispatch]] | downstream | 0.38 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.38 |
| [[p12_wf_admin_orchestration]] | downstream | 0.37 |
