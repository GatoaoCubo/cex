---
quality: 8.7
quality: 8.0
id: p04_es_nucleus_signals
kind: event_stream
8f: F8_collaborate
pillar: P04
title: "Event Stream: Nucleus Signal System"
version: 0.1.0
event_types:
  - "nucleus_complete"
  - "nucleus_error"
  - "handoff_dispatched"
  - "quality_gate_passed"
  - "quality_gate_failed"
  - "wave_complete"
  - "mission_complete"
  - "consolidation_done"
producer: "signal_writer.py (all nuclei N01-N07)"
consumer_groups:
  - name: "n07_orchestrator"
    offset_policy: latest
    lag_tolerance: "30 seconds"
  - name: "mission_runner"
    offset_policy: earliest
    lag_tolerance: "60 seconds"
  - name: "quality_monitor"
    offset_policy: latest
    lag_tolerance: "300 seconds"
partition_key: "nucleus"
partition_count: 7
retention_hours: 168
retention_bytes: "1GB"
delivery: at_least_once
schema_format: json
schema_registry: "N03_engineering/P06_schema/event_schema_nucleus_signal.md"
compatibility_mode: BACKWARD
throughput_estimate: "0.5 events/sec (burst: 7 events/sec during grid dispatch)"
ordering_guarantee: per_partition
monitoring:
  lag_threshold: "10 events"
  alert_on: [consumer_lag, producer_error]
tags: [event_stream, nucleus_signals, P04, orchestration, signal_writer]
tldr: "Nucleus signal event stream: 8 event types, 7 partitions (per nucleus), 168h retention, at-least-once delivery."
created: "2026-04-19"
updated: "2026-04-19"
author: n03_engineering
related:
  - p12_wf_orchestration_pipeline
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration_best_practices
  - p08_ac_orchestrator
  - n07_output_orchestration_audit
  - p12_sig_builder_nucleus
  - p12_wf_admin_orchestration
  - p02_agent_admin_orchestrator
  - p03_sp_orchestration_nucleus
  - p01_ctx_cex_project
density_score: 1.0
---

## Producer

**Service**: `_tools/signal_writer.py` -- invoked by every nucleus (N01-N07) at F8 COLLABORATE
**Throughput**: ~0.5 events/sec sustained; burst to 7/sec during full grid dispatch (all 6 nuclei signaling within seconds)
**Encoding**: JSON (plain, no schema registry binary encoding -- signals are human-readable)

### Event Envelope

Every signal written by `signal_writer.py` follows this structure:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| nucleus | string | YES | Emitting nucleus: n01-n07 or mission phase (w1, w2, ...) |
| status | string | YES | Event type: complete, error, dispatched, gate_passed, gate_failed |
| quality_score | float 0-10 | YES | Artifact quality (0.0 if not applicable) |
| mission | string | NO | Mission name (empty for solo dispatch) |
| wave | int | NO | Wave number within mission |
| timestamp | ISO 8601 | YES | UTC timestamp of signal emission |
| mission_phase | string | NO | Present when nucleus field is a wave ID (w1, w2) |

### Signal File Naming

```
.cex/runtime/signals/signal_{nucleus}_{timestamp}.json           # solo
.cex/runtime/signals/signal_{nucleus}_{mission}_w{wave}_{ts}.json # mission
```

## Consumer Groups

| Group | Offset Policy | Lag Tolerance | Purpose |
|-------|--------------|---------------|---------|
| n07_orchestrator | latest | 30 seconds | Real-time wave management: detect completion, trigger next wave, kill idle processes |
| mission_runner | earliest | 60 seconds | `cex_mission_runner.py` blocking poll: waits for all expected nuclei before proceeding |
| quality_monitor | latest | 300 seconds | `cex_quality_monitor.py` snapshots: detect regressions, track trends |

### Consumer Behaviors

**n07_orchestrator** (primary consumer):
- Polls via `git log --since` + `ls .cex/runtime/signals/` (non-blocking, 2-second cost)
- On `nucleus_complete`: verifies deliverables, kills process tree, marks nucleus done
- On all wave nuclei complete: triggers consolidation + next wave dispatch
- Never uses `cex_signal_watch.py` (blocking -- reserved for headless mission_runner)

**mission_runner** (headless consumer):
- Uses `cex_signal_watch.py --expect n01,n02,... --timeout 3600 --poll 30`
- Blocking poll: sleeps between checks, exits when all expected signals arrive or timeout
- On timeout: checks PID health, reports crashed nuclei

**quality_monitor** (passive consumer):
- Reads all signals periodically, extracts quality_score trends
- Flags regressions: score dropping below 8.0 for a nucleus over 3+ signals

## Partitioning

**Key**: `nucleus` -- ensures all events from one nucleus land on the same logical partition
**Count**: 7 partitions (one per nucleus N01-N07)
**Ordering**: per_partition -- events from N03 are strictly ordered; cross-nucleus ordering is not guaranteed

### Why Per-Nucleus Partitioning

Each nucleus operates independently. N07 needs to track "did N03 complete?" not "did N03 complete before N01?". Per-nucleus partitioning guarantees that a single nucleus's lifecycle events (dispatched -> complete/error) are always ordered, enabling correct state machine transitions without cross-partition coordination.

## Retention

**Time**: 168 hours (7 days)
**Bytes**: 1 GB (signals are ~300 bytes each; 1 GB holds ~3.3 million signals)
**Replay window**: consumers can read back up to 7 days of signal history

### Retention Rationale

- 7-day window covers a full work week of missions
- Allows post-mortem analysis of failed dispatches
- `cex_quality_monitor.py` needs historical signals for trend detection
- Signals older than 7 days are archived to `.cex/runtime/signals/archive/`

## Schema

**Format**: JSON (plain text, no binary encoding)
**Registry**: `N03_engineering/P06_schema/event_schema_nucleus_signal.md` (existing artifact)
**Compatibility**: BACKWARD -- new fields can be added; existing fields never removed or renamed

### Schema Evolution Rules

| Change | Allowed? | Reason |
|--------|----------|--------|
| Add new field | YES | Consumers ignore unknown fields |
| Remove existing field | NO | Breaks consumers expecting the field |
| Rename field | NO | Equivalent to remove + add (breaking) |
| Change field type | NO | Consumers parse by expected type |
| Add new status value | YES | Consumers should handle unknown statuses gracefully |

## Operations

**Lag SLA**: consumer lag < 10 events; if N07 has not processed a signal within 30 seconds of emission, something is wrong (N07 frozen, context compacted, or process crashed).

**Producer errors**: signal_writer.py raises `ValueError` on invalid nucleus or quality_score. These are hard failures (no silent drops). Alert if any nucleus fails to signal within 15 minutes of dispatch.

**Health checks**:

| Check | Method | Frequency |
|-------|--------|-----------|
| Signal directory writable | `SIGNAL_DIR.mkdir(parents=True, exist_ok=True)` | Every write |
| Nucleus validity | Regex + set membership in signal_writer.py | Every write |
| Stale process detection | PID file check + `Get-Process` | Every 60-90 seconds (N07 poll) |
| Signal file integrity | JSON parse validation | On read by consumer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_orchestration_pipeline]] | downstream | 0.37 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.37 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.37 |
| [[p08_ac_orchestrator]] | downstream | 0.36 |
| [[n07_output_orchestration_audit]] | downstream | 0.35 |
| [[p12_sig_builder_nucleus]] | downstream | 0.35 |
| [[p12_wf_admin_orchestration]] | downstream | 0.34 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.33 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.33 |
| [[p01_ctx_cex_project]] | upstream | 0.29 |
