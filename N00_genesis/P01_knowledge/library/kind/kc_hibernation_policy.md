---
id: kc_hibernation_policy
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Knowledge Card: hibernation_policy"
version: 1.0
quality: 9.0
tags: [hibernation_policy, p09, config, serverless, cost, hermes]
tldr: "Idle-suspend rules for serverless/on-demand backends with state persistence and wake SLA"
when_to_use: "When a compute backend should auto-sleep during inactivity to eliminate idle-time cost"
density_score: 1.0
related:
  - bld_collaboration_session_backend
  - spec_infinite_bootstrap_loop
  - bld_memory_runtime_state
  - p11_qg_runtime_state
  - p03_sp_session_backend_builder
  - bld_collaboration_multi_modal_config
  - bld_knowledge_card_checkpoint
  - n05_competitive_ops
  - p01_vdb_pinecone
  - bld_collaboration_session_state
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+spec F4=plan F5=scan F6=produce F7=gate F8=save -->

## What is hibernation_policy?

A `hibernation_policy` is a P09 config artifact that declares the rules under which a serverless or on-demand execution backend suspends itself during idle periods to eliminate idle-time cost. It answers: *how long can a workload sit idle before sleeping, how is state preserved, how fast must it wake up?*

Hibernation is a cost-reduction strategy native to serverless platforms (Daytona, Modal) and supported on HPC backends (Singularity). Without a hibernation policy, a long-lived GPU cluster accumulates cost whether or not agents are actively using it.

**Origin:** NousResearch/hermes-agent -- "Runs on $5 VPS, GPU clusters, or serverless (Daytona/Modal) with hibernation-on-idle capability."

## Core Concepts

### Idle Trigger
The condition that causes the workload to enter hibernation:

| Type | Semantics | Use when |
|------|-----------|----------|
| `no_activity_seconds` | No tool calls, agent I/O, or messages for N seconds | Interactive agent workloads |
| `no_requests_seconds` | No inbound HTTP/gRPC requests for N seconds | HTTP-serving workloads (Modal web endpoints) |
| `explicit_signal` | An external signal (N07 orchestrator) commands hibernate | Batch jobs with known completion boundaries |

### Wake Conditions
Events that resume a hibernated workload:

| Condition | Trigger mechanism |
|-----------|------------------|
| `incoming_request` | HTTP/WebSocket request wakes serverless function |
| `scheduled_cron` | Pre-warm on schedule (avoids cold start at peak time) |
| `explicit_signal` | Orchestrator-issued wake command via backend API |

### State Persistence
What is preserved across the hibernate/wake cycle:

| Setting | Effect |
|---------|--------|
| `keep_memory: true` | In-process memory is snapshotted; resumes without re-initializing agent state |
| `snapshot_disk: true` | Filesystem checkpointed to durable storage (S3 / NFS); preserves model weights |
| `checkpoint_cadence_seconds` | How often active checkpoints fire (null = on-hibernate only; 60 = every minute) |

### Wake Latency SLA
The maximum acceptable cold-start time in seconds. Orchestrators use this value to route latency-sensitive tasks to warm instances vs. accepting a cold wake.

## Boundary

| Confused with | Correct distinction |
|---------------|---------------------|
| `cost_budget` | cost_budget = spend CAP (stop spending after $X); hibernation_policy = cost REDUCTION (sleep when idle) |
| `rate_limit_config` | rate_limit_config = throughput (RPM/TPM caps); hibernation_policy = idle-STATE management |
| `terminal_backend` | terminal_backend = WHERE code runs (daytona/modal/local); hibernation_policy = WHEN it sleeps |
| `runtime_rule` | runtime_rule = active-session timeouts/retries; hibernation_policy = inactivity/sleep lifecycle |

## Backend Support Matrix

| Backend | Hibernation | Native API | Max state restore |
|---------|-------------|-----------|------------------|
| daytona | YES | Workspace pause/resume | Full filesystem |
| modal | YES | Container scaling to 0 | Ephemeral (disk snap optional) |
| singularity | PARTIAL | Job suspend (SLURM) | Checkpoint to shared FS |
| docker | NO | No native hibernate | -- |
| ssh | NO | No native hibernate | -- |
| local | NO | Process is always live | -- |

## Typical Configuration Patterns

### Pattern 1: Serverless GPU with pre-warm schedule
```yaml
idle_trigger:
  type: no_requests_seconds
  threshold_seconds: 300  # 5 minutes
wake_on: [incoming_request, scheduled_cron]
state_persistence:
  keep_memory: false
  snapshot_disk: true
  checkpoint_cadence_seconds: null
wake_latency_sla_seconds: 30
cost_savings_estimate_pct: 85
```

### Pattern 2: Long-running agent workspace (Daytona)
```yaml
idle_trigger:
  type: no_activity_seconds
  threshold_seconds: 1800  # 30 minutes
wake_on: [incoming_request, explicit_signal]
state_persistence:
  keep_memory: true
  snapshot_disk: true
  checkpoint_cadence_seconds: 60
wake_latency_sla_seconds: 10
cost_savings_estimate_pct: 70
```

### Pattern 3: Batch job explicit signal
```yaml
idle_trigger:
  type: explicit_signal
  threshold_seconds: 0
wake_on: [explicit_signal, scheduled_cron]
state_persistence:
  keep_memory: false
  snapshot_disk: false
  checkpoint_cadence_seconds: null
wake_latency_sla_seconds: 60
cost_savings_estimate_pct: 60
```

## Relationship to terminal_backend

`hibernation_policy` and `terminal_backend` are sibling P09 artifacts that describe the same execution environment from complementary angles:

```
terminal_backend (p09_tb_modal) --(governs)--> [WHERE code runs]
hibernation_policy (p09_hp_modal) --(governs)--> [WHEN it sleeps]
```

Both share the `{{backend}}` slug in their IDs. The `terminal_backend` artifact may reference the hibernation_policy via the `hibernation_policy_ref` field (optional extension).

## Filing Convention
- Naming: `p09_hp_{{backend}}.yaml` (e.g. `p09_hp_modal.yaml`, `p09_hp_daytona.yaml`)
- Location: `environments/` directory alongside `terminal_backend` artifacts
- Nucleus: N05 Operations (owns all P09 runtime config)

## Related Kinds
- `terminal_backend` (P09) -- execution environment this policy governs
- `cost_budget` (P09) -- complementary spend cap (hibernation reduces cost; budget caps it)
- `runtime_rule` (P09) -- active-session rules; hibernation_policy covers the inactive boundary
- `secret_config` (P09) -- credentials for backend API hibernate/wake calls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_session_backend]] | downstream | 0.20 |
| [[spec_infinite_bootstrap_loop]] | related | 0.19 |
| [[bld_memory_runtime_state]] | downstream | 0.18 |
| [[p11_qg_runtime_state]] | downstream | 0.18 |
| [[p03_sp_session_backend_builder]] | downstream | 0.18 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.18 |
| [[bld_knowledge_card_checkpoint]] | sibling | 0.17 |
| [[n05_competitive_ops]] | downstream | 0.17 |
| [[p01_vdb_pinecone]] | related | 0.17 |
| [[bld_collaboration_session_state]] | downstream | 0.17 |
