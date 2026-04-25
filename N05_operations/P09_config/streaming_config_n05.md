---
id: p05_sc_n05_ops
kind: streaming_config
8f: F1_constrain
pillar: P05
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: streaming-config-builder
protocol: auto
buffer_bytes: 51200
heartbeat_interval_ms: null
reconnect_delay_ms: null
max_reconnect_attempts: null
max_connections: 5
backpressure_strategy: drop
timeout_ms: null
flush_interval_ms: 1000
quality: 8.9
tags: [streaming_config, auto, file-watcher, operations, N05, P05]
tldr: "File-based ops streams for N05: 5 channels (signal/audit/health/compile/dispatch), 100-event buffer, 1s flush, drop_oldest."
description: "Local file-watcher streaming for N05: signals, audit JSONL, health heartbeats, compile progress, dispatch lifecycle events."
density_score: 1.0
related:
  - bld_output_template_streaming_config
  - p03_sp_streaming_config_builder
  - bld_examples_streaming_config
  - p11_qg_streaming_config
  - n03_self_review_20260402
  - bld_instruction_streaming_config
  - p01_kc_signal
  - p01_kc_cex_orchestration_architecture
  - bld_schema_streaming_config
---

## Overview

File-based transport (protocol: auto) -- no HTTP server. N05 writes operational
events to `.cex/runtime/` subdirs; a tail-follower emits them to subscribers.
Transport is local only: file sink (normal) or stdout (DEBUG_STREAM=1).

Producer: N05 ops nucleus (signal_writer, compile pipeline, dispatch script).
Consumer: N07 monitor loop, cex_signal_watch.py, cex_doctor.py.

## Protocol Settings

| Parameter | Value | Notes |
|-----------|-------|-------|
| protocol | auto | File-watcher tail; no HTTP upgrade |
| content_type | application/x-ndjson | JSONL per event line |
| encoding | utf-8 | All payloads ASCII-safe UTF-8 |
| event_id | line_offset | Resume from last byte offset |
| signal_stream | .cex/runtime/signals/ | emit on new file |
| audit_stream | .cex/runtime/audit/ | emit per line appended |
| health_stream | .cex/runtime/health/ | emit per file update |
| compile_stream | .cex/runtime/compile/ | emit per file processed |
| dispatch_stream | .cex/runtime/pids/ | emit start/complete/fail |

## Flow Control

| Parameter | Value | Notes |
|-----------|-------|-------|
| buffer_bytes | 51200 | 100 events x ~512B avg JSONL line |
| flush_interval_ms | 1000 | Emit buffered events every 1s |
| backpressure_strategy | drop | drop_oldest; append-only logs tolerate loss |
| max_connections | 5 | One watcher per stream channel |

## Lifecycle

| Parameter | Value | Notes |
|-----------|-------|-------|
| heartbeat_interval_ms | null | No proxy in path; file-watcher has no idle timeout |
| timeout_ms | null | Watchers persist for nucleus lifetime |
| reconnect_delay_ms | null | File-based; no TCP reconnect |
| max_reconnect_attempts | null | Watcher re-polls on ENOENT until path exists |
| shutdown | graceful | Flush buffer, close file handles on SIGTERM |

## Event Schema

Each JSONL line follows this envelope:

```json
{
  "ts": "2026-04-25T14:30:00.000Z",
  "stream": "signal|audit|health|compile|dispatch",
  "nucleus": "n05",
  "event": "signal_received|heartbeat|compile_ok|dispatch_start",
  "payload": {},
  "seq": 12345
}
```

| Stream | Events | Avg Line Size | Burst Rate |
|--------|--------|---------------|------------|
| signal | signal_received, signal_sent, signal_expired | 256B | 10/min (gated) |
| audit | tool_call, permission_check, error_logged | 512B | 50/min peak |
| health | heartbeat, threshold_crossed, recovery | 128B | 1/min steady |
| compile | compile_start, compile_ok, compile_fail, drift_detected | 384B | 20/min during grid |
| dispatch | dispatch_start, dispatch_complete, dispatch_fail, pid_registered | 256B | 6/min max (1 per nucleus) |

## Operational Tuning

| Scenario | Adjustment | Reason |
|----------|------------|--------|
| Grid dispatch (6 nuclei) | buffer_bytes: 102400 | 2x buffer for burst |
| Solo build | buffer_bytes: 25600 | halve for low throughput |
| Debug mode | flush_interval_ms: 100 | near-realtime for troubleshooting |
| Overnight evolve | backpressure_strategy: block | preserve all events for audit |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_streaming_config]] | related | 0.23 |
| [[p03_sp_streaming_config_builder]] | upstream | 0.17 |
| [[bld_examples_streaming_config]] | downstream | 0.17 |
| [[p11_qg_streaming_config]] | downstream | 0.16 |
| [[n03_self_review_20260402]] | downstream | 0.16 |
| [[bld_instruction_streaming_config]] | upstream | 0.16 |
| [[p01_kc_signal]] | downstream | 0.16 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.15 |
| [[bld_schema_streaming_config]] | downstream | 0.15 |
