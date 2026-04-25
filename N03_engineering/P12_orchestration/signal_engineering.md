---
id: p12_sig_builder_nucleus
kind: signal
8f: F8_collaborate
pillar: P12
title: Signal Definitions -- Builder Nucleus
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [signal, builder, N03]
tldr: "File-based IPC signals: 4 types (building/complete/error/retry), JSON payload with nucleus+kind+quality+path, written to .cex/runtime/signals/, polled by N07 or signal_watch.py."
density_score: 0.88
related:
  - p04_fd_builder_toolkit
  - p06_if_builder_nucleus
  - p08_ac_builder_nucleus
  - p03_pt_builder_construction
  - p12_dr_builder_nucleus
  - p12_sig_admin_orchestration
  - p12_ho_builder_nucleus
  - signal-builder
  - p03_ch_builder_pipeline
  - bld_collaboration_signal
---

# Signals: Builder Nucleus

## Format

JSON files written to signal directory.

| Field | Type | Description |
|-------|------|-------------|
| nucleus | string | N03 |
| status | enum | building, complete, error, retry |
| kind | string | What kind was being built |
| quality | float | Score (0.0 if error) |
| timestamp | ISO 8601 | When emitted |
| path | string | Artifact path (null if error) |
| message | string | Human-readable status |

## Types

- **complete**: Artifact passes F7, saved + compiled + indexed
- **error**: F7 fails after max retries, or hard failure
- **retry**: F7 soft-fails, pipeline returns to F6
- **building**: Emitted at F1 start to indicate work in progress

## Delivery

File naming: {nucleus}_{kind}_{status}_{timestamp}.json
Monitors poll the signal directory at configurable interval.

## Signal File Example

```json
{
  "nucleus": "n03",
  "status": "complete",
  "kind": "agent",
  "quality": 9.2,
  "timestamp": "2026-04-25T14:30:00Z",
  "path": "N03_engineering/P02_model/agent_research.md",
  "message": "Agent artifact built via 8F. H01-H07 passed. Compiled to YAML.",
  "session_id": "n07_abc123"
}
```

## Signal Lifecycle

| Phase | Who Writes | Who Reads | File Pattern |
|-------|-----------|-----------|--------------|
| F1 start | Runner | N07 (optional) | `signal_n03_building_{ts}.json` |
| F7 pass | Runner | N07 consolidate | `signal_n03_complete_{ts}.json` |
| F7 fail (retryable) | Runner | Runner itself | `signal_n03_retry_{ts}.json` |
| F7 fail (hard) | Runner | N07 escalation | `signal_n03_error_{ts}.json` |

## Consumer Patterns

- **N07 interactive**: polls via `git log --since` + `dispatch.sh status` (non-blocking)
- **Mission runner**: blocks via `signal_watch.py --expect n03 --timeout 3600`
- **Cleanup**: archived to `.cex/runtime/archive/` after consolidation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_fd_builder_toolkit]] | upstream | 0.38 |
| [[p06_if_builder_nucleus]] | upstream | 0.37 |
| [[p08_ac_builder_nucleus]] | upstream | 0.32 |
| [[p03_pt_builder_construction]] | upstream | 0.31 |
| [[p12_dr_builder_nucleus]] | related | 0.30 |
| [[p12_sig_admin_orchestration]] | sibling | 0.28 |
| [[p12_ho_builder_nucleus]] | related | 0.27 |
| [[signal-builder]] | related | 0.26 |
| [[p03_ch_builder_pipeline]] | upstream | 0.25 |
| [[bld_collaboration_signal]] | related | 0.25 |
