---
id: p09_arch_task_queue
kind: knowledge_card
8f: F3_inject
pillar: P09
title: "Task Queue Specification — Continuous/Infinite Bootstrap Mode"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
domain: runtime-orchestration
quality: 9.2
tags: [task-queue, continuous-mode, infinite-bootstrap, dispatch, runtime, P09]
tldr: "File-based task queue for overnight/infinite mode. Priority levels, lifecycle states, dequeue protocol, and auto-replenishment."
density_score: 0.91
related:
  - continuous_batching_report
  - p08_ac_orchestrator
  - bld_examples_pattern
  - p01_kc_runtime_state
  - tpl_runtime_state
  - p02_agent_admin_orchestrator
  - p12_wf_orchestration_pipeline
  - p03_sp_orchestration_nucleus
  - p03_pt_orchestration_task_dispatch
  - p08_pat_continuous_batching
---

# Task Queue Specification

## Purpose

The infinite bootstrap mode (`overnight_infinite.cmd` + `--continuous` flag in `cex_mission_runner.py`) requires a persistent task queue that:

1. **Feeds nuclei** with work items without human intervention
2. **Prioritizes** critical tasks over nice-to-haves
3. **Tracks lifecycle** from creation through completion
4. **Auto-replenishes** by scanning for gaps, stale artifacts, and pending improvements
5. **Survives crashes** — file-based, no in-memory state lost on process death

## Architecture

```
.cex/runtime/queue/
  pending/           # Tasks waiting to be dispatched
  active/            # Currently being executed by a nucleus
  done/              # Completed tasks (kept for audit trail)
  failed/            # Tasks that failed or timed out
  queue_config.yaml  # Queue settings (max parallel, priorities, TTL)
```

### Queue Entry Format

Each task is a single YAML file in the appropriate subdirectory:

```yaml
# .cex/runtime/queue/pending/tq_20260407_153000_n03_build_agent_card.yaml
---
id: tq_20260407_153000_n03_build_agent_card
kind: task_queue_entry
created: 2026-04-07T15:30:00-03:00
source: auto_scan              # auto_scan | manual | evolve | mission_decompose
priority: 2                    # 1=critical, 2=normal, 3=low, 4=background
nucleus: n03                   # target nucleus (n01-n06)
intent: "Build agent_card for N02 marketing nucleus"
context:                       # pre-loaded references for the nucleus
  - N02_marketing/README.md
  - archetypes/builders/agent-card-builder/bld_instruction_agent_card.md
  - P01_knowledge/library/kind/kc_agent_card.md
depends_on: []                 # IDs of tasks that must complete first
max_retries: 1                 # retry count before moving to failed/
timeout_seconds: 1800          # per-attempt timeout (30 min default)
estimated_depth: medium        # shallow | medium | deep (dispatch-depth compliance)
tags: [agent_card, n02, gap]
```

### Lifecycle States

```
  PENDING ──dispatch──> ACTIVE ──success──> DONE
     |                    |
     |                    +──timeout──> PENDING (retry) or FAILED
     |                    +──crash──>   PENDING (retry) or FAILED
     |
     +──cancel──> DONE (status=cancelled)
     +──supersede──> DONE (status=superseded, replaced_by=<new_id>)
```

| State | Directory | Meaning |
|-------|-----------|---------|
| PENDING | `queue/pending/` | Waiting for dispatch |
| ACTIVE | `queue/active/` | Dispatched to a nucleus, awaiting signal |
| DONE | `queue/done/` | Completed successfully (signal received) |
| FAILED | `queue/failed/` | Exhausted retries or manually cancelled |

State transitions are atomic file moves (rename, not copy+delete).

### State Transition Metadata

When a task moves states, these fields are appended:

```yaml
# Added when PENDING -> ACTIVE
dispatched_at: 2026-04-07T15:35:00-03:00
session_id: s1712345678
attempt: 1

# Added when ACTIVE -> DONE
completed_at: 2026-04-07T15:52:00-03:00
quality_score: 9.0
signal_file: signal_n03_20260407_155200.json
duration_seconds: 1020

# Added when ACTIVE -> FAILED
failed_at: 2026-04-07T16:05:00-03:00
failure_reason: timeout
attempt: 2
```

## Priority Levels

| Level | Name | Use Case | Dispatch Order |
|-------|------|----------|----------------|
| 1 | Critical | Blocking dependencies, broken infrastructure | First — preempts all |
| 2 | Normal | Standard build/improve tasks | FIFO within priority |
| 3 | Low | Nice-to-have improvements, polish | After all P1/P2 clear |
| 4 | Background | Evolve loops, speculative research | Only when queue is otherwise empty |

Within the same priority, tasks are dispatched oldest-first (FIFO).

## Dequeue Protocol

The continuous-mode loop in `cex_mission_runner.py` follows this protocol each cycle:

```
1. SCAN queue/pending/ for tasks, sorted by (priority ASC, created ASC)
2. GROUP by nucleus — max 1 active task per nucleus at a time
3. CHECK dependencies — skip tasks whose depends_on IDs are not in done/
4. CHECK concurrency — respect queue_config.yaml max_parallel (default: 6)
5. For each selected task:
   a. Acquire CexLock("queue_dequeue") — prevents race with other loops
   b. Move file: pending/ -> active/
   c. Append dispatched_at + session_id + attempt
   d. Write handoff to .cex/runtime/handoffs/n0X_task.md
   e. Dispatch: bash _spawn/dispatch.sh solo n0X "task"
   f. Release lock
6. POLL signals every 30s for active tasks
7. On signal received:
   a. Move file: active/ -> done/
   b. Append completed_at + quality_score + duration
   c. If quality_score < 8.0 AND retries remain: move back to pending/ (re-queue)
8. On timeout:
   a. If attempt < max_retries: move back to pending/, increment attempt
   b. Else: move to failed/
9. LOOP back to step 1
```

## Auto-Replenishment Sources

When `queue/pending/` is empty, the system scans for new work:

| Source | Scanner | Priority | What it finds |
|--------|---------|----------|---------------|
| `cex_doctor.py` | FAIL/WARN results | 2 | Missing artifacts, broken builders |
| `cex_auto.py --scan` | Gap detection | 3 | Nuclei with fewer artifacts than peers |
| `cex_evolve.py --scan` | Staleness check | 4 | Artifacts not updated in 30+ days |
| `cex_flywheel_audit.py` | Doc-vs-practice | 3 | Mismatches between docs and implementation |
| Manual | User drops YAML in `pending/` | 1-4 | Anything — user sets priority |

Auto-replenishment writes new task entries to `queue/pending/` with `source: auto_scan`.

## Queue Configuration

```yaml
# .cex/runtime/queue/queue_config.yaml
---
max_parallel: 6                    # max concurrent nuclei (matches grid capacity)
max_pending: 50                    # cap to prevent runaway auto-scan
dequeue_interval_seconds: 30       # how often the loop checks for new work
task_timeout_default: 1800         # 30 min default per task
stale_active_ttl: 3600             # 60 min — active task with no signal = stale
auto_replenish: true               # scan for new work when queue empties
replenish_cooldown: 300            # 5 min between auto-scans
priority_starve_limit: 10          # after 10 P2 tasks, force 1 P3 even if P2 pending
quality_requeue_threshold: 8.0     # below this score = re-queue for improvement
max_retries_default: 1             # attempts before FAILED
```

## Concurrency Rules

| Rule | Rationale |
|------|-----------|
| Max 1 active task per nucleus | Each nucleus = 1 pi process = 1 context window |
| Max 6 total active tasks | Hardware limit (6 nuclei, N07 orchestrates) |
| Dependency resolution before dispatch | Prevents building on incomplete foundations |
| Lock on dequeue | Prevents two loops from dispatching same task |
| No self-dispatch | N07 manages queue; nuclei never dequeue for themselves |

## Failure Handling

| Failure | Detection | Response |
|---------|-----------|----------|
| Timeout | `stale_active_ttl` exceeded, no signal | Re-queue or FAILED |
| Crash | PID dead (checked via `cex_lock._pid_alive`) | Re-queue or FAILED |
| Low quality | Signal received but `quality_score < 8.0` | Re-queue with `source: quality_retry` |
| Corrupt output | `cex_doctor.py` reports FAIL on produced artifact | Re-queue with added context |
| Dependency dead | Required task in `failed/` | Move dependent to `failed/` with reason |

## Integration Points

| Component | Role |
|-----------|------|
| `cex_mission_runner.py --continuous` | Main dequeue loop, signal polling |
| `cex_mission_state.py` | Persists overall mission progress across crashes |
| `cex_lock.py` | Atomic dequeue, prevents double-dispatch |
| `signal_writer.py` | Nuclei signal completion (triggers state transition) |
| `cex_signal_watch.py` | Blocking poll for signal arrival |
| `cex_auto.py --scan` | Auto-replenishment source |
| `cex_evolve.py --scan` | Staleness-based replenishment |
| `cex_doctor.py` | Health-based replenishment + post-completion validation |
| `.claude/rules/shared-file-proposal.md` | Prevents file conflicts during concurrent queue execution |
| `overnight_infinite.cmd` | Boot script that starts the continuous loop |

## CLI Interface

```bash
# List pending tasks
python _tools/cex_queue.py --list pending

# List all tasks (pending + active + done + failed)
python _tools/cex_queue.py --list all

# Add a task manually
python _tools/cex_queue.py --add --nucleus n03 --intent "Build missing agent card" --priority 2

# Cancel a task
python _tools/cex_queue.py --cancel tq_20260407_153000_n03_build_agent_card

# Re-queue a failed task
python _tools/cex_queue.py --requeue tq_20260407_153000_n03_build_agent_card

# Drain queue (cancel all pending)
python _tools/cex_queue.py --drain

# Stats
python _tools/cex_queue.py --stats
```

## Overnight Mode Integration

```
overnight_infinite.cmd
  |
  +-> python _tools/cex_mission_runner.py --continuous --timeout 28800
        |
        +-> [dequeue loop]
              |-> scan pending/ -> dispatch -> poll signals -> state transition
              |-> if empty: auto-replenish -> loop
              |-> if all failed/done + no replenish: exit 0
              |-> if --timeout reached: stop all nuclei, exit 0
```

The `--timeout 28800` (8 hours) ensures the loop stops by morning.
`cex_mission_state.py` checkpoints progress every cycle so a crash resumes cleanly.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[continuous_batching_report]] | upstream | 0.33 |
| [[p08_ac_orchestrator]] | upstream | 0.27 |
| [[bld_examples_pattern]] | upstream | 0.26 |
| [[p01_kc_runtime_state]] | sibling | 0.23 |
| [[tpl_runtime_state]] | downstream | 0.23 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.22 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.22 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.22 |
| [[p03_pt_orchestration_task_dispatch]] | upstream | 0.22 |
| [[p08_pat_continuous_batching]] | upstream | 0.21 |
