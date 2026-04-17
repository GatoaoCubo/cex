---
id: ex_director_ops_health_monitor
kind: supervisor
pillar: P08
title: "N05 Operations Health Supervisor"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "supervisor-builder"
topic: "ops_health_monitor"
builders:
  - process-monitor
  - signal-monitor
  - artifact-monitor
  - resource-monitor
dispatch_mode: parallel
signal_check: true
wave_topology:
  - wave: 1
    builders: [process-monitor, signal-monitor, resource-monitor]
    gate: "signal_health_checks_complete"
  - wave: 2
    builders: [artifact-monitor]
    gate: "signal_artifact_audit_complete"
fallback_per_builder:
  process-monitor: escalate
  signal-monitor: alert
  artifact-monitor: quarantine
  resource-monitor: alert
llm_function: ORCHESTRATE
domain: "supervision, monitoring, failover"
quality: null
tags: [supervisor, operations, monitoring, failover, P08, N05]
tldr: "N05 health supervisor: parallel process+signal+resource checks then artifact audit. Actions: ALERT/RESTART/ESCALATE/QUARANTINE."
density_score: 0.91
---

## Identity

`ex_director_ops_health_monitor` supervises CEX runtime health across 4 builders.
Sources: `.cex/runtime/pids/`, `.cex/runtime/signals/`, `git log`. No daemon required --
runs inside N07's autonomous lifecycle or standalone via `cex_signal_watch.py`.
Wave 1 checks process+signal+resource in parallel; wave 2 audits artifacts after wave 1 clears.

## Builders

| Builder | Nucleus | Role |
|---------|---------|------|
| `process-monitor` | N05 | PID alive, worker responsive, orphan detection |
| `signal-monitor` | N05 | Expected signals received within timeout |
| `artifact-monitor` | N05 | Compile success, doctor pass, quality >= threshold |
| `resource-monitor` | N05 | Disk space, git repo size, token budget |

## Wave Topology

Wave 1: `process-monitor` + `signal-monitor` + `resource-monitor` -> `signal_health_checks_complete`
Wave 2: `artifact-monitor` -> `signal_artifact_audit_complete`
Gate: wave 2 blocked if wave 1 emits ESCALATE. Operator decision required before proceed.

## Dispatch Config

Mode: `parallel`. Signal check: true. Timeout: `60`s wave 1; `300`s wave 2.
Fallback: `process-monitor`: escalate; `signal-monitor`: alert;
`artifact-monitor`: quarantine; `resource-monitor`: alert.

Actions: ALERT (log + notify N07) | RESTART (kill + re-dispatch) |
ESCALATE (block + operator gate) | QUARANTINE (isolate + block compile).

## Routing

1. Triggers: `health check`, `monitor nuclei`, `signal timeout`, `orphan detected`
2. Keywords: `pid`, `signal`, `orphan`, `compile`, `quality gate`, `disk`, `token budget`
3. NOT when: solo 8F build, GDP decision phase, brand bootstrap

## Crew Role

**MONITORS** -- answers: "Are all nuclei healthy and producing valid artifacts?"
Exclusions: does not execute builds, write signals, or modify artifacts.
