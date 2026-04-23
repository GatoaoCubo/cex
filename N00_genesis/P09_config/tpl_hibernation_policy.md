---
id: hp_{{backend}}
kind: hibernation_policy
pillar: P09
title: "Hibernation Policy: {{backend}}"
target_backend: daytona | modal | singularity | generic
idle_trigger:
  type: no_activity_seconds | no_requests_seconds | explicit_signal
  threshold_seconds: 900
wake_on:
  - incoming_request
  - scheduled_cron
  - explicit_signal
state_persistence:
  keep_memory: true
  snapshot_disk: true
  checkpoint_cadence_seconds: 60
wake_latency_sla_seconds: 10
cost_savings_estimate_pct: 70
version: 1.0.0
quality: null
tags: [hermes_origin, hibernation, serverless, cost]
tldr: "Idle trigger, wake conditions, state persistence, and cost savings for backend hibernation"
domain: infrastructure
density_score: 1.0
updated: "2026-04-22"
related:
  - bld_architecture_schedule
  - bld_architecture_checkpoint
  - p01_kc_schedule
  - p11_qg_schedule
---

## Purpose

A hibernation_policy defines how an agent workload transitions between active and idle states
to minimize compute cost without sacrificing responsiveness. It specifies the idle trigger
(when to sleep), wake conditions (when to wake), state persistence (what to preserve across
cycles), and SLA constraints (maximum acceptable wake latency). This kind pairs with
`terminal_backend` (same backend slug) to form a complete execution + lifecycle configuration.

## Policy Overview

**Target backend:** {{target_backend}}
**Purpose:** {{one-line description of what this policy governs}}
**Nucleus owner:** N05 Operations

## Idle Trigger

| Field | Value |
|-------|-------|
| Trigger type | {{idle_trigger.type}} |
| Threshold | {{idle_trigger.threshold_seconds}}s |

```
Idle trigger fires when:
  - no_activity_seconds: no tool calls, agent messages, or I/O for N seconds
  - no_requests_seconds: no inbound HTTP/gRPC requests for N seconds (serverless only)
  - explicit_signal: hibernation is triggered by an external signal (e.g., orchestrator)
```

## Wake Conditions

| Condition | Description |
|-----------|-------------|
| `incoming_request` | Any inbound HTTP/WebSocket request wakes the workload |
| `scheduled_cron` | A cron expression fires a pre-warm on schedule |
| `explicit_signal` | N07 or the orchestrator sends an explicit wake command |

## State Persistence

| Setting | Value | Description |
|---------|-------|-------------|
| keep_memory | {{state_persistence.keep_memory}} | Snapshot in-process memory before sleep |
| snapshot_disk | {{state_persistence.snapshot_disk}} | Checkpoint filesystem to durable storage |
| checkpoint_cadence_seconds | {{state_persistence.checkpoint_cadence_seconds}} | Periodic checkpoint interval while active |

## SLA

| Metric | Value | Notes |
|--------|-------|-------|
| Wake latency SLA | {{wake_latency_sla_seconds}}s | Max acceptable cold-start time |
| Cost savings estimate | {{cost_savings_estimate_pct}}% | Estimated idle-cost reduction |

## Backend-Specific Defaults

| Backend | Idle threshold | Wake latency | Cost savings | Snapshot support |
|---------|---------------|-------------|-------------|-----------------|
| `daytona` | 900s | 5-10s | 70-80% | Full (workspace snapshot) |
| `modal` | 300s | 2-5s | 60-90% | Partial (function state only) |
| `singularity` | 1800s | 15-30s | 50-70% | Full (container checkpoint) |
| `generic` | 900s | varies | varies | Depends on infrastructure |

## Lifecycle State Machine

```
ACTIVE --> (idle trigger) --> CHECKPOINTING --> HIBERNATED
                                                    |
                            (wake condition) -------+
                                    |
                                    v
                              WAKING --> ACTIVE
```

| State | Description | Cost |
|-------|-------------|------|
| `ACTIVE` | Workload running, accepting requests | Full compute cost |
| `CHECKPOINTING` | Saving state before hibernation | Brief compute spike |
| `HIBERNATED` | No compute, state persisted to storage | Storage-only cost |
| `WAKING` | Restoring state from checkpoint | Brief compute spike |

## Idle Threshold Reference

Different workload profiles require different idle thresholds.

| Workload type | Recommended threshold | Rationale | Backend examples |
|---------------|----------------------|-----------|-----------------|
| Interactive agent (chat) | 300s (5 min) | Users may pause mid-conversation | Daytona, Modal |
| Batch processing | 60s (1 min) | No human latency; idle = done | Modal, Singularity |
| API service | 900s (15 min) | Traffic spikes are bursty | Docker, Modal |
| Development workspace | 1800s (30 min) | Developer context switching is slow | Daytona, local |
| GPU inference | 120s (2 min) | GPU cost is high; aggressive saves money | Modal (GPU), Singularity |
| Scheduled cron job | 0s (immediate) | Run and hibernate after completion | Any serverless |
| CI/CD runner | 30s | Short-lived by design | Docker, Modal |

## Resource Cleanup Sequence

When the idle trigger fires, resources are cleaned up in this deterministic order.

| Step | Action | Timeout | Rollback on failure |
|------|--------|---------|-------------------|
| 1 | Flush pending writes to disk | 10s | Retry once, then abort |
| 2 | Checkpoint in-memory state | 30s | Skip checkpoint, log warning |
| 3 | Snapshot filesystem | 60s | Skip snapshot, log warning |
| 4 | Drain active connections (graceful) | 15s | Force-close after timeout |
| 5 | Release GPU memory (if applicable) | 5s | `ollama stop` or CUDA cleanup |
| 6 | Emit hibernation signal to N07 | 2s | Signal failure is non-blocking |
| 7 | Suspend container/VM/process | 5s | Kill if suspend fails |

```yaml
# Cleanup sequence configuration
cleanup:
  flush_writes:
    timeout_seconds: 10
    retry: 1
  checkpoint_memory:
    enabled: "{{state_persistence.keep_memory}}"
    timeout_seconds: 30
    destination: ".cex/runtime/hibernation/checkpoint_{{backend}}.bin"
  snapshot_disk:
    enabled: "{{state_persistence.snapshot_disk}}"
    timeout_seconds: 60
    destination: "{{snapshot_storage_path}}"
  drain_connections:
    timeout_seconds: 15
    strategy: graceful_then_force
  release_gpu:
    enabled: auto_detect
    command: "ollama stop || nvidia-smi --gpu-reset"
  signal:
    type: hibernation_started
    target: ".cex/runtime/signals/signal_hibernation_{{backend}}.json"
```

## Wake Trigger Taxonomy

Wake triggers bring a hibernated workload back to active state.

| Trigger | Latency class | Auth required | Use case |
|---------|--------------|---------------|----------|
| `incoming_request` | Cold start (2-30s) | API token or webhook signature | Production API, chat agent |
| `scheduled_cron` | Pre-warm (0s effective) | System (cron daemon) | Batch jobs, daily reports |
| `explicit_signal` | Variable (1-10s) | N07 session token | Orchestrator dispatch |
| `dependency_wake` | Chained (5-60s) | Inter-service | Service A needs service B |
| `health_check` | Probe (1s) | None (public endpoint) | Load balancer probes |
| `manual_cli` | Immediate (1-5s) | Shell access | Developer debugging |

### Pre-warm Strategy

```
For scheduled workloads (cron-triggered):
  1. Cron fires at T-30s (30 seconds before actual task)
  2. Wake sequence starts: restore checkpoint, load model, warm cache
  3. At T=0, workload is fully warm and ready to process
  4. Effective cold-start latency: 0s (from task perspective)

For bursty API traffic:
  1. Keep 1 warm instance at all times (min_instances: 1)
  2. Hibernate overflow instances aggressively (threshold: 60s)
  3. Scale-to-zero only during known quiet hours (e.g., 2am-6am)
```

## Notes

- Pair this policy with `terminal_backend` (same {{backend}} slug) for complete execution config
- `wake_latency_sla_seconds` is informational -- orchestrators use it to route latency-sensitive tasks to warm instances
- For GPU workloads, `snapshot_disk: true` preserves model weights across hibernation cycles
- Set `checkpoint_cadence_seconds` lower for stateful agents (memory-heavy) to minimize data loss on crash
- For serverless backends (Modal), idle threshold can be aggressive (300s) since wake latency is low
- Monitor hibernation cycles in `.cex/runtime/hibernation/` for cost optimization insights

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `terminal_backend` | P09 | Backend execution config; hibernation_policy governs its idle behavior |
| `schedule` | P12 | Cron schedules can trigger pre-warm via `wake_on: scheduled_cron` |
| `env_config` | P09 | Environment variables may control hibernation thresholds per env |
| `secret_config` | P09 | Backend credentials for checkpoint storage (S3, GCS, etc.) |
| `sandbox_config` | P09 | Security isolation persists across hibernation cycles |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_schedule]] | upstream | 0.18 |
| [[bld_architecture_checkpoint]] | upstream | 0.16 |
| [[p01_kc_schedule]] | downstream | 0.16 |
| [[p11_qg_schedule]] | downstream | 0.15 |
