---
id: spec_infinite_bootstrap_loop
kind: context_doc
title: "CEX Peak Architecture: Infinite Bootstrap Loop"
version: 1.0.0
quality: null
created: 2026-04-07
purpose: Full spec for autonomous infinite self-building loop with max throughput
---

# CEX Peak Architecture: Infinite Bootstrap Loop

## Vision

CEX builds itself from zero. N07 orchestrates continuously, 6 nuclei work
in parallel (each with sub-agents), artifacts flow through 8F, quality gates
filter, and the flywheel never stops. N07 never idles.

## Bill of Materials (from zero)

| Component | Files | Tokens est. |
|-----------|-------|------------|
| Builder ISOs (13 per kind) | 1,630 | 24.5M |
| Kind KCs | 123 | 1.8M |
| Domain KCs | 88 | 1.3M |
| Templates + examples | 377 | 5.7M |
| Pillar schemas | 12 | 0.2M |
| Tools (.py) | 59 | 0.9M |
| Rules + configs | 15 | 0.2M |
| Nucleus artifacts | 313 | 4.7M |
| Sub-agents | 125 | 1.9M |
| **TOTAL** | **2,742** | **41.1M** |

## Throughput Estimates

| Configuration | Artifacts/hour | Time to build all |
|--------------|---------------|-------------------|
| 6 nuclei solo | 180 | 15.2h |
| 6 nuclei x4 sub-agents | 720 | 3.8h |
| + continuous batching | 864 | 3.2h |

## Architecture

```
overnight_infinite.cmd (loop forever)
  |
  +-- N07 (pi --continue, resumes state)
  |     |
  |     +-- WORK + DISPATCH (non-blocking interleaved)
  |     |     |
  |     |     +-- N01 + sub-agents (research)
  |     |     +-- N02 + sub-agents (marketing)
  |     |     +-- N03 + sub-agents (build)
  |     |     +-- N04 + sub-agents (knowledge)
  |     |     +-- N05 + sub-agents (code)
  |     |     +-- N06 + sub-agents (commercial)
  |     |     |
  |     |     +-- = 6 nuclei x (1 + 4 sub-agents) = 30 LLM streams
  |     |
  |     +-- When context approaching limit:
  |           write state to disk, exit cleanly
  |
  +-- SLEEP 10s
  +-- RESTART N07 (pi --continue, fresh context)
```

## 5 Blockers and Solutions

### Blocker 1: N07 Context Exhaustion (dies at 1M tokens)

**Problem**: N07 fills its 1M context and can't continue orchestrating.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **pi --continue** | pi natively supports `--continue` flag to resume previous session | EXISTS in pi |
| **pi /handoff** | Extension that extracts context and creates new focused session | EXISTS as pi extension (handoff.ts) |
| **pi compact()** | Built-in compaction that summarizes conversation to free tokens | EXISTS in pi SDK |
| **mission_state.yaml** | CEX-specific checkpoint file on disk with task queue + progress | NEEDS BUILD |

**Recommended approach**: Combine `mission_state.yaml` (CEX state) with pi's `/handoff` (context transfer).

```yaml
# .cex/runtime/mission_state.yaml
mission: full_bootstrap
started: 2026-04-07T20:00:00
wave: 3
tasks_total: 2742
tasks_completed: 847
tasks_in_progress:
  n01: {task: "research_kc_batch_12", started: "2026-04-07T22:14:00"}
  n03: {task: "build_isos_wave3", started: "2026-04-07T22:14:30"}
next_tasks:
  - {nucleus: n03, kind: prompt_template, count: 9}
  - {nucleus: n04, kind: knowledge_card, count: 15}
quality_gate:
  passed: 830
  failed: 17
  retried: 12
tokens_used: 12400000
```

**Implementation**: N05 builds `cex_mission_state.py` (read/write/update checkpoint).
N07 reads on boot, writes before context exhaustion.

### Blocker 2: Sub-agents Inside Each Nucleus (6x -> 30x)

**Problem**: Each nucleus runs 1 LLM instance. Could run 1 + 4 sub-agents.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **pi subagent extension** | Official pi extension: spawns isolated pi subprocesses, supports parallel (max 8, 4 concurrent), chain mode, streaming | EXISTS as pi example extension |
| **Agent .md files** | YAML frontmatter defines agent: name, tools, model | EXISTS (pi convention) |
| **Parallel mode** | `{ tasks: [{agent, task}, ...] }` — runs up to 4 concurrent | EXISTS in subagent extension |
| **Chain mode** | `{ chain: [{agent, task with {previous}}, ...] }` — sequential with context passing | EXISTS in subagent extension |

**Recommended approach**: Install subagent extension in each nucleus boot.

```
.pi/agents/                          # Project-level agents for CEX
  builder-iso.md                     # Sub-agent: builds 1 ISO file
  kc-writer.md                       # Sub-agent: writes 1 KC
  example-generator.md               # Sub-agent: generates 1 example
  template-filler.md                 # Sub-agent: fills 1 template
```

Each nucleus boot loads the subagent extension. When N03 gets "build 13 ISOs for citation-builder", it spawns:
- 4 parallel sub-agents, each building 3-4 ISOs
- Total time: 1/4 of solo

**Constraint**: pi subagent max = 8 tasks, 4 concurrent per invocation.
With 6 nuclei x 4 concurrent = 24 parallel LLM streams.

**Implementation**:
1. Install subagent extension: symlink from pi examples to `.pi/extensions/subagent/`
2. Create 4-6 CEX-specific agent .md files in `.pi/agents/`
3. Update boot scripts to include subagent extension
4. Update handoff format to support parallel sub-tasks

### Blocker 3: Git Conflicts (6 nuclei writing same repo)

**Problem**: Multiple nuclei committing simultaneously causes merge conflicts
on shared files (kinds_meta.json, _schema.yaml).

**Solutions found**:

| Solution | How | Pros | Cons |
|----------|-----|------|------|
| **Branch-per-nucleus** | Each nucleus works in `n0X/task` branch, N07 merges | Clean isolation | Merge overhead, N07 must resolve |
| **Lock files** | `.cex/runtime/locks/{file}.lock` with PID | Simple | Deadlocks if nucleus crashes |
| **Append-only directories** | Each nucleus writes only to its own `N0X_*/` dir | Zero conflicts | Shared files (kinds_meta) still conflict |
| **N07 consolidation queue** | Nuclei write to staging dir, N07 applies to main | Zero conflicts | Delay between produce and commit |
| **git worktrees** | Each nucleus gets its own worktree of same repo | Full isolation | Complex setup, disk space |

**Recommended approach**: Hybrid — append-only for artifacts + lock files for shared resources.

Current reality: nuclei ALREADY mostly write to their own directories.
The only shared files that conflict:
- `.cex/kinds_meta.json` — N07 should be sole writer (nuclei propose, N07 applies)
- `P{xx}/_schema.yaml` — same, N07 applies
- `archetypes/builders/` — conflict-free if each nucleus builds different kinds

**Implementation**:
1. Create `_tools/cex_lock.py` — atomic file locking (PID-based, auto-expire 5min)
2. Rule: nuclei NEVER edit kinds_meta.json or _schema.yaml directly
3. Rule: nuclei write proposals to `.cex/runtime/proposals/{nucleus}_{file}.yaml`
4. N07 reads proposals, applies to shared files, commits

### Blocker 4: Continuous Batching (no wave gaps)

**Problem**: Current model is wave-based — dispatch all, wait all, consolidate, next wave.
Idle time between waves wastes throughput.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **Event-driven dispatcher** | N07 checks git log every ~30s, dispatches next task immediately when a nucleus finishes | PATTERN EXISTS (non-blocking lifecycle rule) |
| **Task queue file** | `.cex/runtime/task_queue.yaml` with prioritized tasks, N07 pops and dispatches | NEEDS BUILD |
| **cex_mission_runner.py** | Already supports multi-wave with signal polling | EXISTS but wave-based |

**Recommended approach**: Enhance `cex_mission_runner.py` with continuous mode.

```python
# Current (wave-based):
dispatch_wave(nuclei) → wait_all() → consolidate() → next_wave()

# Target (continuous):
while tasks_remain():
    for nucleus in idle_nuclei():
        task = pop_next_task(nucleus.domain)
        dispatch(nucleus, task)
    sleep(30)
    check_completions()  # git log + signals
    consolidate_completed()
```

**Implementation**: N05 adds `--continuous` flag to `cex_mission_runner.py`.

### Blocker 5: Infinite Runtime (overnight_infinite.cmd)

**Problem**: N07 eventually exhausts context or crashes. Need auto-restart.

**Solutions found**:

| Solution | How | Status |
|----------|-----|--------|
| **CMD loop** | `@echo off` + `:loop` + `goto loop` with pi inside | PATTERN EXISTS (overnight_h1.cmd) |
| **pi --continue** | Resume previous session with context | EXISTS in pi |
| **pi /handoff** | Create focused new session from current context | EXISTS as extension |
| **pi compact()** | SDK method to compress conversation | EXISTS in pi |
| **mission_state.yaml** | State file survives restart | NEEDS BUILD |

**Recommended approach**: CMD loop + mission_state.yaml + pi --continue.

```cmd
@echo off
title CEX INFINITE BOOTSTRAP
:loop
echo [%time%] Starting N07 session...

pi --model anthropic/claude-opus-4-6 ^
   --append-system-prompt "N07_admin/agent_card_n07.md" ^
   --append-system-prompt ".cex/config/context_self_select.md" ^
   "Read .cex/runtime/mission_state.yaml. Continue the mission from where it left off. When context is 80%% full, write state and exit with message EXIT_CHECKPOINT."

echo [%time%] N07 exited. Restarting in 10s...
timeout /t 10 /nobreak
goto loop
```

**Key**: N07 must write `mission_state.yaml` BEFORE exiting. The next instance reads it and continues seamlessly.

## Implementation Roadmap

| Step | What | Nucleus | Depends on | Effort |
|------|------|---------|-----------|--------|
| 1 | `cex_mission_state.py` (checkpoint R/W) | N05 | — | 1 dispatch |
| 2 | `overnight_infinite.cmd` (auto-restart loop) | N05 | Step 1 | 1 dispatch |
| 3 | `cex_lock.py` (shared file locking) | N05 | — | 1 dispatch |
| 4 | Proposal pattern for shared files | N07 (rule) | Step 3 | N07 direct |
| 5 | Install subagent extension + create CEX agents | N05 | — | 1 dispatch |
| 6 | Update boot scripts for subagent support | N05 | Step 5 | 1 dispatch |
| 7 | `--continuous` mode in mission_runner | N05 | Steps 1,3 | 1 dispatch |
| 8 | Task queue file + auto-prioritization | N05 | Step 7 | 1 dispatch |
| 9 | Full integration test (mini bootstrap) | N07 | Steps 1-8 | 1 mission |

**Estimated total**: 8 dispatches + 1 integration test.
With continuous batching: ~2 hours to build the infrastructure.
Then the infrastructure builds CEX: ~3-4 hours for full from-zero bootstrap.

## Throughput at Peak

| Metric | Value |
|--------|-------|
| Parallel LLM streams | 24 (6 nuclei x 4 sub-agents) |
| Tokens per hour | ~36M |
| Artifacts per hour | 720-864 |
| Time for full CEX from zero | ~3-4 hours |
| N07 context cycles | ~7 (41M / 6M per cycle, continuous restart) |
| Total wall time | ~4-5 hours (including N07 restarts) |
| Human intervention required | Zero (after /mission start) |
