---
id: session_state_n05
kind: session_state
nucleus: n05
pillar: P10
mirrors: N00_genesis/P10_memory/templates/tpl_session_state.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Session State (Incident Context)"
version: 1.0.0
quality: 8.5
tags: [mirror, n05, operations, hermes_assimilation, session_state]
tldr: "N05 ops session state: incident context, recent alerts, open tickets, deploy status -- dual-ID tracking with search backend."
search_backend: sqlite_fts5
summarizer_model: null
related:
  - bld_memory_session_state
  - p01_kc_session_state
  - bld_schema_session_state
  - p01_kc_session_backend
  - bld_tools_session_state
  - bld_collaboration_session_state
  - session-state-builder
  - p03_sp_session_state_builder
  - bld_config_session_state
  - bld_architecture_session_backend
density_score: 1.0
updated: "2026-04-22"
---

## Session State Schema (Ops Flavor)

N05 session state captures operational context: active incidents, recent alerts,
deploy status, and open tickets. IRA lens: every session starts with full
situational awareness.

### Session IDs (Dual-ID Protocol)

```yaml
content_session_id: {{STABLE_UUID}}
memory_session_id: {{SDK_SESSION_ID_OR_NULL}}
compression_status: pending
search_backend: sqlite_fts5
```

### Ops-Specific Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| active_incidents | list | yes | Currently open incidents with severity |
| recent_alerts | list | yes | Alerts from last 1h |
| deploy_status | enum | yes | idle/deploying/rollback/blocked |
| open_tickets | list | no | Pending ops tickets |
| nucleus_health | map | yes | PID alive/dead status per nucleus |
| last_gate_result | object | yes | Most recent quality gate result |

### Snapshot Template

```yaml
snapshot:
  goal: {{active_operational_goal}}
  stage: {{current_stage}}
  owner: n05
  deploy_status: idle
  active_incidents: []
  recent_alerts: []
  nucleus_health:
    n01: unknown
    n02: unknown
    n03: unknown
    n04: unknown
    n05: alive
    n06: unknown
  last_gate_result:
    tool: cex_doctor.py
    passed: true
    timestamp: {{ISO8601}}
```

### Search Configuration

| Setting | Value | Notes |
|---------|-------|-------|
| Backend | sqlite_fts5 | HERMES default for session search |
| Index fields | goal, incidents, alerts, tickets | Searchable fields |
| Summarizer | null | Enable for long sessions (>50 turns) |
| Retention | 7d | Auto-prune after 7 days |

### Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Session DB corrupt | read error | create fresh session | log + alert |
| Search index stale | query returns 0 for known data | rebuild index | log |
| Memory overflow | session >3072 bytes | compress via summarizer | auto |
| Dual-ID mismatch | content_id != memory_id mapping | log warning | review |

### Expiry Rules

| Condition | Action |
|-----------|--------|
| Session idle >1h | Mark stale, compress |
| Session idle >24h | Archive to .cex/runtime/archive/ |
| Session idle >7d | Delete |
| Incident resolved | Keep 48h for post-mortem, then archive |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_session_state]] | related | 0.35 |
| [[p01_kc_session_state]] | related | 0.34 |
| [[bld_schema_session_state]] | upstream | 0.34 |
| [[p01_kc_session_backend]] | related | 0.33 |
| [[bld_tools_session_state]] | upstream | 0.30 |
| [[bld_collaboration_session_state]] | related | 0.29 |
| [[session-state-builder]] | related | 0.29 |
| [[p03_sp_session_state_builder]] | upstream | 0.29 |
| [[bld_config_session_state]] | upstream | 0.28 |
| [[bld_architecture_session_backend]] | upstream | 0.28 |
