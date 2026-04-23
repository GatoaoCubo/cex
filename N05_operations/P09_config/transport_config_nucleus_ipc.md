---
quality: 8.9
quality: 8.4
id: p09_tc_nucleus_ipc
kind: transport_config
pillar: P09
title: "Transport Config: Nucleus-to-Nucleus IPC"
version: "1.0.0"
transport_type: filesystem
created: "2026-04-19"
updated: "2026-04-19"
author: "n05_operations"
domain: "nucleus_ipc"
tags: [transport_config, nucleus_ipc, operations, signals, handoffs]
tldr: "Filesystem-based IPC for nucleus communication: signals via JSON, handoffs via Markdown, PIDs via text; no network transport needed."
related:
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p08_ac_orchestrator
  - p12_wf_orchestration_pipeline
  - p12_wf_admin_orchestration
  - n07_output_orchestration_audit
  - dispatch
  - agent_card_engineering_nucleus
  - p02_agent_admin_orchestrator
density_score: 1.0
---

## Transport Type Declaration

CEX nuclei communicate via **filesystem IPC** -- not network sockets, not HTTP, not gRPC. Each nucleus runs as an independent OS process (claude.exe / codex / gemini / ollama) with shared filesystem access to the repository working directory.

This is a deliberate architectural choice: filesystem IPC is the lowest-common-denominator transport that works across all 4 runtimes (Claude, Codex, Gemini, Ollama) without requiring any network stack or service discovery.

## Protocol-Specific Parameters

### Signal Channel (nucleus -> N07)

| Parameter | Value | Notes |
|-----------|-------|-------|
| transport | filesystem write | Atomic JSON file creation |
| path_pattern | .cex/runtime/signals/signal_{nucleus}_{mission}_{timestamp}.json | One file per signal event |
| format | JSON | Fields: nucleus, status, quality_score, timestamp, mission, wave |
| writer | _tools/signal_writer.py | Canonical signal producer |
| reader | _tools/cex_signal_watch.py (blocking) or git log (non-blocking) | N07 polls via git log; mission_runner uses signal_watch |
| atomicity | Write to temp file, then os.rename() | Prevents partial reads on Windows |
| retention | Until consolidation archives to .cex/runtime/archive/ | N07 archives after wave completion |

### Handoff Channel (N07 -> nucleus)

| Parameter | Value | Notes |
|-----------|-------|-------|
| transport | filesystem write | Markdown file with YAML frontmatter |
| path_pattern | .cex/runtime/handoffs/{MISSION}_{nucleus}.md | One file per nucleus per mission |
| copy_target | n0X_task.md (repo root) | Boot scripts read this file at startup |
| format | Markdown with YAML frontmatter | Fields: nucleus, task, created, mission, wave |
| writer | N07 orchestrator (direct write) or dispatch.sh | dispatch.sh copies handoff to n0X_task.md |
| reader | Nucleus boot script (boot/n0X.ps1) | Reads n0X_task.md at session start |
| race_condition | dispatch.sh cp happens AFTER dispatch; must not overwrite during active read | Known issue: feedback_grid_git_race_and_dispatch_stub |

### PID Channel (process tracking)

| Parameter | Value | Notes |
|-----------|-------|-------|
| transport | filesystem append | One line per spawned process |
| path | .cex/runtime/pids/spawn_pids.txt | Shared across all sessions |
| format | Text: {cmd_pid} {nucleus} {cli} {session_id} {timestamp} {worker_pids} | Session-tagged for multi-N07 safety |
| writer | _spawn/spawn_grid.ps1 | Post-launch enrichment adds worker PIDs |
| reader | _spawn/dispatch.sh status | Reads PID file + checks process liveness |
| cleanup | dispatch.sh stop (session-aware) | Only kills processes matching current session_id |

### Decision Channel (user -> nuclei)

| Parameter | Value | Notes |
|-----------|-------|-------|
| transport | filesystem write | YAML manifest |
| path | .cex/runtime/decisions/decision_manifest.yaml | Single file, overwritten per mission |
| format | YAML | Fields: mission, status, timestamp, decisions (key-value) |
| writer | N07 via GDP protocol | Written before first dispatch |
| reader | All nuclei (referenced in handoff) | Nuclei read manifest, never re-ask user |

## Security Configuration

| Parameter | Value | Notes |
|-----------|-------|-------|
| Encryption | None (local filesystem) | All data stays within repo working directory |
| Authentication | OS-level file permissions | Processes run as same user |
| Integrity | Git tracks all changes | git log provides full audit trail |
| Isolation | Session ID in PID file | Multi-N07 sessions isolated by session tag |

## Resilience Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Signal delivery guarantee | At-least-once | signal_writer.py creates file; N07 polls until found |
| Handoff delivery guarantee | Exactly-once | File written before dispatch; nucleus reads at boot |
| Stale signal detection | Timestamp comparison | Signals older than mission start are ignored |
| Orphan process detection | PID liveness check | dispatch.sh status checks if PID is alive via Get-Process |
| Stuck nucleus timeout | 15 minutes (configurable) | N07 investigates if no git commits in 15 min |
| Recovery on crash | Manual re-dispatch | N07 re-writes handoff and re-dispatches |

## QoS and Performance

| Metric | Value | Notes |
|--------|-------|-------|
| Signal write latency | <10ms | os.rename() is near-instant on local filesystem |
| Handoff read latency | <50ms | Small Markdown file (<5KB typical) |
| PID file contention | Minimal | Append-only; concurrent writes rare (grid spawns sequentially with 5s interval) |
| Maximum concurrent channels | 7 | One per nucleus (N01-N07); N00 genesis is not a runtime nucleus |
| Polling interval (non-blocking) | 60-90s | Per feedback_polling_intervals memory; git log check |
| Polling interval (blocking) | 30s | cex_signal_watch.py --poll 30 |

## Notes

This transport config documents CEX's actual IPC mechanism as of 2026-04-19. The filesystem-based approach was chosen for:

1. **Cross-runtime compatibility**: Ollama local models cannot make HTTP calls; Codex sandbox has no network; filesystem is universal
2. **Simplicity**: No service discovery, no port management, no connection pooling
3. **Auditability**: Every IPC event is a file in git history
4. **Zero dependencies**: No message broker, no Redis, no ZeroMQ

Trade-offs: No real-time push notification (polling required); no cross-machine communication (single-host only); file contention possible under extreme parallelism (>20 concurrent nuclei).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.45 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.40 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.40 |
| [[p08_ac_orchestrator]] | upstream | 0.39 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.39 |
| [[p12_wf_admin_orchestration]] | downstream | 0.34 |
| [[n07_output_orchestration_audit]] | downstream | 0.34 |
| [[dispatch]] | upstream | 0.30 |
| [[agent_card_engineering_nucleus]] | upstream | 0.29 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.29 |
