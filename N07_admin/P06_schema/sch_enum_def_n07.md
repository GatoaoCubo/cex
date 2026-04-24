---
id: sch_enum_def_n07
kind: enum_def
8f: F1_constrain
pillar: P06
nucleus: n07
title: "Orchestrator Enumerations"
version: 1.0
quality: 8.0
tags: [enum-def, orchestration, dispatch, wave, signal]
related:
  - p12_wf_admin_orchestration
  - p01_kc_orchestration_best_practices
  - p12_wf_orchestration_pipeline
  - n07_output_orchestration_audit
  - p08_ac_orchestrator
  - p03_sp_orchestration_nucleus
  - p02_agent_admin_orchestrator
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration
  - continuous_batching_report
---
<!-- 8F: F1=P06/enum_def F2=enum-def-builder F3=nucleus_def_n07+n07-orchestrator F4=reason F5=call F6=produce F7=govern F8=collaborate -->

# Orchestrator Enumerations

## Purpose

Canonical closed-set enumerations for N07 orchestration. These values are the only
legal tokens in handoffs, signals, and mission plans. Consumers use exhaustive match
— no unknown-value handling required (`extensible: false` on all).

## Enumerations

### DISPATCH_MODE

How N07 spawns work. Pick one per task; no mixing within a single dispatch call.

| Value | Description | Behavior |
|-------|-------------|----------|
| solo | One nucleus, one artifact | `dispatch.sh solo n0X "task"` |
| grid | N nuclei in parallel, independent outputs | `dispatch.sh grid MISSION` |
| crew | N roles with ordered handoffs, one package | `cex_crew.py run <name>` |
| swarm | N builders of same kind, N independent outputs | `dispatch.sh swarm <kind> N` |

### WAVE_STATUS

Lifecycle of a single wave inside a mission. N07 reads this to gate next-wave dispatch.

| Value | Description | Behavior |
|-------|-------------|----------|
| pending | Wave defined, dispatch not yet issued | Block next wave |
| dispatched | PIDs written, processes started | Poll for signals |
| running | At least one nucleus signaled start | Continue polling |
| complete | All nuclei signaled complete | Gate passes; dispatch next wave |
| failed | One or more nuclei signaled error | Halt mission; report |
| timeout | Wave exceeded time budget | Escalate to user |

### SIGNAL_TYPE

Events emitted by nuclei via signal_writer. N07 consumes these to drive lifecycle.

| Value | Description | Behavior |
|-------|-------------|----------|
| start | Nucleus booted and task accepted | Update WAVE_STATUS to running |
| progress | Checkpoint within long task | Log only; no state change |
| complete | Task done, artifacts committed | Decrement pending count |
| error | Unrecoverable failure, no artifacts | Set WAVE_STATUS to failed |
| timeout | Nucleus self-reported time overrun | Same as error |

### CONSOLIDATION_ACTION

Ordered steps N07 executes after a wave reaches complete. Run in sequence.

| Value | Description | Behavior |
|-------|-------------|----------|
| verify | Check expected artifacts exist on disk | Fail fast if missing |
| stop | Kill completed nucleus process trees | `taskkill /F /PID <pid> /T` |
| commit | Stage + commit nucleus output (Gemini path) | `git add N0x && git commit` |
| archive | Move wave signals to `.cex/runtime/archive/` | Keeps runtime dir clean |
| report | Write consolidation summary to handoff dir | Input for next wave |

### HANDOFF_PRIORITY

Urgency tag on handoff files. N07 reads this to sequence dispatch when budget is tight.

| Value | Description | Behavior |
|-------|-------------|----------|
| critical | Blocking dependency; all other waves wait | Dispatch immediately |
| high | Near-blocking; dispatch in wave N+1 | Next scheduled wave |
| normal | Standard work; batch with others | Default |
| low | Optional enrichment; skip if time-constrained | Drop if budget exceeded |

### NUCLEUS_STATE

Runtime state of a single nucleus process. Tracked in PID file.

| Value | Description | Behavior |
|-------|-------------|----------|
| idle | Process alive, no active task | Safe to assign new task |
| booting | Boot script executing, task not yet loaded | Wait for start signal |
| active | Nucleus executing 8F pipeline | Do not interrupt |
| completing | F8 in progress (compile + commit + signal) | Wait for complete signal |
| crashed | Process dead, no signal received | Trigger error path |

### MISSION_PHASE

Top-level phases of a CEX mission. Maps to slash commands.

| Value | Description | Behavior |
|-------|-------------|----------|
| plan | Decompose goal into tasks and waves | `/plan` command |
| guide | GDP: collect subjective decisions from user | `/guide` command |
| spec | Write artifact specs and handoff files | `/spec` command |
| grid | Dispatch grid; autonomous execution | `/grid` command |
| consolidate | Verify, archive, report on completed grid | `/consolidate` command |

## Rationale

Orchestrating Sloth lens: every enum value maps to an unambiguous automated action.
N07 reads a value and executes -- no interpretation overhead, no branching on prose.
All sets are closed (`extensible: false`) so exhaustive match is always safe.

## Properties

| Property | Value |
|----------|-------|
| Kind | `enum_def` |
| Pillar | P06 |
| Nucleus | N07 |
| Enum count | 7 |
| Total values | 33 |
| Extensible | false (all) |
| Quality target | null (peer-assigned) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_admin_orchestration]] | downstream | 0.47 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.42 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.40 |
| [[n07_output_orchestration_audit]] | downstream | 0.39 |
| [[p08_ac_orchestrator]] | downstream | 0.38 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.38 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.37 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.37 |
| [[p01_kc_orchestration]] | upstream | 0.34 |
| [[continuous_batching_report]] | upstream | 0.33 |
