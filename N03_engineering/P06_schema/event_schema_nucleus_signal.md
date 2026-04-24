---
quality: 8.6
quality: 8.1
id: p06_evs_nucleus_signal
kind: event_schema
8f: F8_collaborate
pillar: P06
version: "1.0.0"
created: "2026-04-19"
updated: "2026-04-19"
author: "n03_engineering"
event_type: "cex.nucleus.signalEmitted.v1"
schema_version: "1.0.0"
source: "/nucleus/{nucleus_id}"
datacontenttype: "application/json"
tags: [event_schema, nucleus_signal, P06, cex, a2a]
tldr: "NucleusSignalEmitted v1: nucleus_id + status + score + artifacts[]. CloudEvents 1.0. Source: /nucleus/{id}. Consumed by N07 consolidation and signal_watch."
related:
  - p12_sig_builder_nucleus
  - p12_wf_orchestration_pipeline
  - p12_sig_admin_orchestration
  - bld_schema_nucleus_def
  - p12_wf_admin_orchestration
  - p01_kc_cex_orchestration_architecture
  - p01_kc_orchestration_best_practices
  - p12_wf_create_orchestration_agent
  - p08_ac_orchestrator
  - bld_knowledge_card_nucleus_def
density_score: 1.0
---

# Event Schema: NucleusSignalEmitted

The canonical completion signal emitted by every CEX nucleus (N01-N07) at the end of F8 COLLABORATE.
Consumed by N07 orchestrator, `cex_signal_watch.py`, and `cex_mission_runner.py` to detect
wave completion and trigger consolidation.

Produced by: `_tools/signal_writer.py::write_signal(nucleus_id, status, score)`
Stored at: `.cex/runtime/signals/signal_{nucleus}_{mission}_{timestamp}.json`

## CloudEvents Attributes

| Attribute | Value | Required | Notes |
|-----------|-------|----------|-------|
| specversion | "1.0" | YES | CloudEvents 1.0 |
| id | UUID v4 | YES | Unique per signal emission |
| type | "cex.nucleus.signalEmitted.v1" | YES | Reverse-DNS + version suffix |
| source | "/nucleus/{nucleus_id}" | YES | Emitting nucleus URI (e.g., /nucleus/n03) |
| subject | "{nucleus_id}" | REC | Short identifier of the emitting nucleus |
| time | RFC3339 timestamp | REC | Moment F8 COLLABORATE completes |
| datacontenttype | "application/json" | YES | Payload encoding |

## Payload Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12",
  "type": "object",
  "required": ["nucleus_id", "status", "score"],
  "properties": {
    "nucleus_id": {
      "type": "string",
      "pattern": "^n0[0-7]$",
      "description": "Canonical nucleus identifier: n00-n07"
    },
    "status": {
      "type": "string",
      "enum": ["complete", "failed", "error"],
      "description": "Outcome of the nucleus run: complete=F8 done, failed=quality gate exhausted, error=unhandled exception"
    },
    "score": {
      "type": "number",
      "minimum": 0.0,
      "maximum": 10.0,
      "description": "Quality score from F7 GOVERN. 0.0 if status=error. Null not allowed -- use 0.0 for unscored failures."
    },
    "mission": {
      "type": "string",
      "description": "Mission name that dispatched this nucleus run (e.g., CONTRIB_STRESS_TEST)"
    },
    "artifacts": {
      "type": "array",
      "items": {"type": "string"},
      "description": "List of artifact file paths produced during this run (relative to repo root)"
    },
    "session_id": {
      "type": "string",
      "description": "N07 session ID that spawned this nucleus. Used for session-aware stop targeting."
    },
    "wave": {
      "type": "integer",
      "minimum": 1,
      "description": "Mission wave number that produced this signal"
    }
  }
}
```

## Example Signal

```json
{
  "specversion": "1.0",
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "type": "cex.nucleus.signalEmitted.v1",
  "source": "/nucleus/n03",
  "subject": "n03",
  "time": "2026-04-19T14:22:00Z",
  "datacontenttype": "application/json",
  "data": {
    "nucleus_id": "n03",
    "status": "complete",
    "score": 9.0,
    "mission": "CONTRIB_STRESS_TEST",
    "artifacts": [
      "N03_engineering/P08_architecture/state_machine_8f_pipeline.md",
      "N03_engineering/P06_schema/aggregate_root_artifact.md"
    ],
    "session_id": "n07_20260419_142000",
    "wave": 1
  }
}
```

## Versioning

| Strategy | Rule | Notes |
|----------|------|-------|
| Add optional field | ALLOWED | Bump schema_version minor (e.g., 1.0.0 -> 1.1.0) |
| Add required field | PROHIBITED | Create v2: `cex.nucleus.signalEmitted.v2` |
| Remove/rename field | PROHIBITED | Create v2 and deprecate v1 for 2 releases |

## Consumers

| Consumer | Context | Action |
|----------|---------|--------|
| N07 orchestrator | Interactive mission monitoring | Detect wave completion, trigger next wave or consolidation |
| cex_signal_watch.py | Blocking poll (headless runs) | Unblocks when all expected nuclei have signaled |
| cex_mission_runner.py | Autonomous overnight execution | Routes to quality gate or compensation wave |
| GridDispatch process manager | State machine | Drives state transition WAVE_DISPATCHED -> WAVE_COMPLETE |

## References

- Writer: `_tools/signal_writer.py::write_signal()`
- Reader: `_tools/cex_signal_watch.py`
- Storage path pattern: `.cex/runtime/signals/signal_{nucleus}_{mission}_{ts}.json`
- Aggregate consuming this event: `N03_engineering/P06_schema/aggregate_root_artifact.md`
- Process manager: `N03_engineering/P12_orchestration/process_manager_grid_dispatch.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_sig_builder_nucleus]] | downstream | 0.36 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.35 |
| [[p12_sig_admin_orchestration]] | downstream | 0.33 |
| [[bld_schema_nucleus_def]] | related | 0.29 |
| [[p12_wf_admin_orchestration]] | downstream | 0.28 |
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.28 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.28 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.28 |
| [[p08_ac_orchestrator]] | downstream | 0.27 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.27 |
