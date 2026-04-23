---
quality: 8.6
quality: 7.8
id: p12_pm_grid_dispatch
kind: process_manager
pillar: P12
title: "Process Manager: GridDispatch"
version: 0.1.0
correlation_key: "mission_id"
start_event: "GridDispatched"
terminal_states: [COMPLETED, FAILED]
states: [CREATED, WAVE_DISPATCHED, NUCLEI_RUNNING, WAVE_COMPLETE, ALL_WAVES_COMPLETE, CONSOLIDATING, COMPLETED, FAILED]
subscribed_events:
  - "GridDispatched"
  - "NucleusSignalReceived"
  - "WaveTimedOut"
  - "ConsolidationComplete"
  - "ConsolidationFailed"
commands_issued:
  - "DispatchWave -> dispatch.sh (grid)"
  - "KillOrphanProcesses -> dispatch.sh (stop)"
  - "RunConsolidate -> cex_doctor.py + git commit"
  - "DispatchCompensationWave -> dispatch.sh (solo fallback)"
timeout_strategy:
  WAVE_DISPATCHED: "5m: action=CHECK_PID_ALIVE"
  NUCLEI_RUNNING: "45m: action=TIMEOUT -> transition to FAILED"
compensation:
  - "On FAILED from NUCLEI_RUNNING: issue KillOrphanProcesses to dispatch.sh"
  - "On FAILED from CONSOLIDATING: issue DispatchCompensationWave for failed nuclei"
persistence: file
tags: [process_manager, grid_dispatch, P12, orchestration, mission]
tldr: "GridDispatch process: starts on GridDispatched, routes NucleusSignalReceived per wave, issues DispatchWave + KillOrphanProcesses + RunConsolidate, compensates on timeout."
related:
  - p12_wf_admin_orchestration
  - p01_kc_orchestration_best_practices
  - p02_agent_admin_orchestrator
  - n07_output_orchestration_audit
  - p08_ac_admin_orchestrator
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration
  - p12_wf_orchestration_pipeline
  - p08_ac_orchestrator
  - p03_sp_admin_orchestrator
density_score: 1.0
updated: "2026-04-22"
---

# Process Manager: GridDispatch

Coordinates the multi-wave lifecycle of a grid mission dispatch.
N07 orchestrator uses this process manager pattern (implemented in `cex_mission_runner.py`)
to manage concurrent nucleus execution without blocking the orchestrator's own reasoning loop.

A unique GridDispatch instance is created per `mission_id`.
One mission may contain multiple waves; each wave is a fresh WAVE_DISPATCHED -> WAVE_COMPLETE cycle.

## Correlation

**Key**: `mission_id` -- unique per `/mission` or `/grid` invocation (e.g., `CONTRIB_STRESS_TEST_20260419`)
**Storage**: `.cex/runtime/pids/spawn_pids.txt` (live state) + `.cex/runtime/signals/` (completion events)

## States

| State | Description | Terminal? |
|-------|-------------|-----------|
| CREATED | GridDispatched received, handoffs written, not yet dispatched | No |
| WAVE_DISPATCHED | `dispatch.sh grid` called, PIDs recorded | No |
| NUCLEI_RUNNING | All nuclei of current wave alive, awaiting signals | No |
| WAVE_COMPLETE | All nuclei in wave signaled complete | No |
| ALL_WAVES_COMPLETE | Final wave signaled; no more waves planned | No |
| CONSOLIDATING | cex_doctor + git commit consolidation underway | No |
| COMPLETED | Consolidation done, signals archived | YES |
| FAILED | Timeout or consolidation failure; compensation triggered | YES |

## Event Routing

| Event Received | Current State | Next State | Command Issued | Target |
|----------------|--------------|-----------|----------------|--------|
| GridDispatched | (none) | CREATED | WriteHandoffs | file system |
| DispatchWave call | CREATED | WAVE_DISPATCHED | DispatchWave | dispatch.sh grid |
| NucleusSignalReceived (partial) | WAVE_DISPATCHED | NUCLEI_RUNNING | -- | -- |
| NucleusSignalReceived (all in wave) | NUCLEI_RUNNING | WAVE_COMPLETE | -- | -- |
| WaveComplete + more waves | WAVE_COMPLETE | WAVE_DISPATCHED | DispatchWave (next wave) | dispatch.sh grid |
| WaveComplete + no more waves | WAVE_COMPLETE | ALL_WAVES_COMPLETE | -- | -- |
| ConsolidationStart | ALL_WAVES_COMPLETE | CONSOLIDATING | RunConsolidate | cex_doctor + git |
| ConsolidationComplete | CONSOLIDATING | COMPLETED | KillOrphanProcesses | dispatch.sh stop |
| WaveTimedOut | NUCLEI_RUNNING | FAILED | KillOrphanProcesses | dispatch.sh stop --all |
| ConsolidationFailed | CONSOLIDATING | FAILED | DispatchCompensationWave | dispatch.sh solo |

## Commands

### DispatchWave(wave_number, handoff_paths)
- Target: `bash _spawn/dispatch.sh grid {MISSION}`
- Payload: `{mission_id: str, wave: int, nucleus_ids: list[str], handoff_paths: list[str]}`
- Idempotency: mission_id + wave number (re-dispatch of same wave skipped if PIDs alive)

### KillOrphanProcesses(session_id)
- Target: `bash _spawn/dispatch.sh stop` (session-aware)
- Payload: `{session_id: str, dry_run: bool}`
- Idempotency: safe to call multiple times; stop on already-dead PID is no-op

### RunConsolidate(mission_id)
- Target: `python _tools/cex_doctor.py` then `git add -A && git commit`
- Payload: `{mission_id: str, expected_artifacts: list[str]}`
- Idempotency: doctor is read-only; git commit is idempotent (no changes = no commit)

### DispatchCompensationWave(failed_nuclei)
- Target: `bash _spawn/dispatch.sh solo n0X "retry {task}"`
- Payload: `{nucleus_ids: list[str], retry_count: int}`
- Idempotency: compensation triggered at most once per FAILED transition

## Timeout

| State | Timeout | Action |
|-------|---------|--------|
| WAVE_DISPATCHED | 5 min | Check PID alive; log warning; stay in state |
| NUCLEI_RUNNING | 45 min | Issue KillOrphanProcesses; transition to FAILED |

## Compensation

On FAILED from NUCLEI_RUNNING:
1. Issue KillOrphanProcesses (session_id) to dispatch.sh -- clears orphaned claude.exe + node.exe
2. Log failed nucleus IDs to `.cex/runtime/signals/signal_FAILED_{mission}.json`

On FAILED from CONSOLIDATING:
1. Issue DispatchCompensationWave for nuclei whose deliverables are missing
2. Max 1 compensation wave per mission (second failure = human intervention required)

## References

- Implementation: `_tools/cex_mission_runner.py`
- Signal poll: `_tools/cex_signal_watch.py`
- PID tracking: `.cex/runtime/pids/spawn_pids.txt`
- Dispatch script: `_spawn/dispatch.sh`
- NucleusSignalEmitted schema: `N03_engineering/P06_schema/event_schema_nucleus_signal.md`
- 8F state machine: `N03_engineering/P08_architecture/state_machine_8f_pipeline.md`
- N07 autonomous lifecycle: `.claude/rules/n07-autonomous-lifecycle.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_admin_orchestration]] | related | 0.40 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.37 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.33 |
| [[n07_output_orchestration_audit]] | related | 0.33 |
| [[p08_ac_admin_orchestrator]] | upstream | 0.32 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.32 |
| [[p01_kc_orchestration]] | upstream | 0.32 |
| [[p12_wf_orchestration_pipeline]] | related | 0.31 |
| [[p08_ac_orchestrator]] | upstream | 0.31 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.31 |
