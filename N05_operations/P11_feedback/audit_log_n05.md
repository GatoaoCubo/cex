---
id: p11_al_n05_operations
kind: audit_log
8f: F8_collaborate
pillar: P11
title: "Audit Log Config -- N05 Operations"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: audit-log-builder
domain: operational-accountability
nucleus: N05
event_type: multi_category
log_level: info
quality: 9.1
tags: [audit_log, N05, compliance, dispatch]
tldr: "Immutable JSONL audit log for N05 -- 8 event types, 30-day retention, SOC2 CC6.1/CC7.1/CC11.2."
density_score: 1.0
related:
  - bld_schema_model_registry
  - n06_schema_brand_config
  - bld_schema_audit_log
  - bld_schema_experiment_tracker
  - p12_sig_builder_nucleus
  - bld_schema_nucleus_def
  - p12_wf_create_orchestration_agent
  - bld_schema_tagline
  - bld_schema_agent_grounding_record
  - bld_schema_prompt_compiler
---

## Event Catalog

| event_type     | actor        | resource             | action           |
|----------------|--------------|----------------------|------------------|
| dispatch_event | N07/operator | nucleus + mission    | dispatch         |
| build_event    | nucleus      | file_path + kind     | create/modify    |
| signal_event   | nucleus      | signal_file          | signal_complete  |
| compile_event  | hook         | .md + .yaml          | compile          |
| quality_event  | cex_score   | artifact_path        | score/gate       |
| process_event  | dispatch.sh | PID + nucleus        | start/stop/crash |
| config_event   | operator     | config + field       | update           |
| git_event      | nucleus/N07 | repo + branch        | commit/push      |

## Entry Schema (JSONL)

Required fields per line:

| field      | type   | notes                           |
|------------|--------|---------------------------------|
| timestamp  | string | ISO 8601 ms UTC                 |
| event_type | string | enum from catalog               |
| actor      | string | nucleus_id or tool              |
| resource   | string | path, PID, or config key        |
| action     | string | dispatch/create/signal/score    |
| result     | string | success / fail / crash          |
| trace_id   | string | uuid4 links events in 8F run    |

Optional: score, wave, session_id, exit_code, files_count.

## Storage Policy

| property    | value                                       |
|-------------|---------------------------------------------|
| format      | JSON Lines, UTF-8, append-only              |
| path        | .cex/runtime/audit/audit_{YYYY-MM-DD}.jsonl |
| rotation    | daily 00:00 UTC                             |
| retention   | 30 days local; then archive/                |
| immutability| append-only + SHA-256 footer per file       |

## Compliance Controls

| control  | implementation                           |
|----------|------------------------------------------|
| CC6.1    | process_event + config_event             |
| CC7.1    | quality_event fail + crash records       |
| CC11.2   | config_event with old/new values         |
| SOC2-INT | SHA-256 hash chain per file footer       |
| 8F-F8    | git_event via cex_hooks_native.py        |

## Sample Entry (dispatch_event)

```
{"timestamp":"2026-04-17T14:23:01.452Z","event_type":"dispatch_event","actor":"N07","resource":"N05","action":"dispatch","result":"success","trace_id":"a1b2c3d4","wave":"wave_1"}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | upstream | 0.30 |
| [[n06_schema_brand_config]] | upstream | 0.27 |
| [[bld_schema_audit_log]] | upstream | 0.26 |
| [[bld_schema_experiment_tracker]] | upstream | 0.26 |
| [[p12_sig_builder_nucleus]] | downstream | 0.24 |
| [[bld_schema_nucleus_def]] | upstream | 0.24 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.24 |
| [[bld_schema_tagline]] | upstream | 0.24 |
| [[bld_schema_agent_grounding_record]] | upstream | 0.24 |
| [[bld_schema_prompt_compiler]] | upstream | 0.23 |
