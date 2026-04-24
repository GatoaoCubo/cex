---
id: session_state_n07
kind: session_state
8f: F8_collaborate
nucleus: n07
pillar: P10
mirrors: N00_genesis/P10_memory/templates/tpl_session_state.md
overrides:
  tone: terse, dispatch-oriented, meta
  voice: imperative orchestrator
  sin_lens: PREGUICA ORQUESTRADORA
  required_fields:
    - target_nucleus
    - expected_deliverables
    - do_not_list
  quality_threshold: 9.2
  density_target: 0.90
  example_corpus: 3+ examples with full do-not lists
  orchestration_fields: [active_mission, wave_progress, dispatched_pids, signal_log, decision_state]
version: 1.0.0
quality: 8.3
tags: [mirror, n07, orchestration, session_state, hermes_assimilation]
tldr: "N07 mission session: active nuclei PIDs, wave progress, signal log, decision manifest state"
created: "2026-04-18"
related:
  - p01_kc_cex_orchestration_architecture
  - bld_memory_runtime_state
  - p12_wf_create_orchestration_agent
  - p12_wf_orchestration_pipeline
  - p01_kc_orchestration_best_practices
  - bld_collaboration_session_state
  - runtime-state-builder
  - bld_tools_session_state
  - p01_kc_session_backend
  - n07_output_orchestration_audit
density_score: 1.0
updated: "2026-04-22"
---

## Override Rationale

N07's session state tracks **dispatch state**, not code state. Where N03 tracks
active_files and compile_status, N07 tracks: which mission is active, which wave
is running, which nuclei are alive, and what signals have arrived.

## N07 Session State Schema

```yaml
content_session_id: {{STABLE_UUID}}
memory_session_id: {{SDK_SESSION_ID_OR_NULL}}
compression_status: pending | done

# Orchestration-specific fields (N07 overrides)
active_mission:
  name: {{MISSION_NAME}}
  plan: .cex/runtime/plans/plan_{{name}}.md
  spec: .cex/runtime/specs/spec_{{name}}.md
  started_at: 2026-04-18T14:00:00

wave_progress:
  current_wave: W1
  total_waves: 3
  completed_waves: []
  status: dispatching | monitoring | consolidating

dispatched_pids:
  - nucleus: n03
    pid: 12345
    worker_pids: [12346, 12347]
    started_at: 2026-04-18T14:01:00
    status: running | signaled | killed
  - nucleus: n01
    pid: 12350
    worker_pids: [12351]
    started_at: 2026-04-18T14:01:05
    status: running | signaled | killed

signal_log:
  - nucleus: n01
    event: complete
    score: 9.1
    received_at: 2026-04-18T14:05:00
  - nucleus: n03
    event: complete
    score: 9.0
    received_at: 2026-04-18T14:08:00

decision_state:
  manifest_path: .cex/runtime/decisions/decision_manifest.yaml
  locked_decisions: 5
  pending_decisions: 0
```

## Refresh Triggers

| Trigger | Action |
|---------|--------|
| post-compact hook | Refresh session_state from PID file + signal dir |
| wave_completion | Archive wave signals, update wave_progress |
| process_kill | Remove PID entry, update status |
| new_dispatch | Add PID entry, reset wave status |

## Ephemeral Contract

Session state is ephemeral. It dies with the session. Durable state goes to:
- Decisions: `decision_manifest.yaml`
- Lessons: `MEMORY.md`
- Signals: `.cex/runtime/archive/`

## Links

- N00 archetype: [[N00_genesis/P10_memory/templates/tpl_session_state.md]]
- N03 engineering sibling: [[N03_engineering/P10_memory/session_state_n03.md]]
- N04 knowledge sibling: [[N04_knowledge/P10_memory/session_state_n04.md]]
- PID tracking: [[.cex/runtime/pids/spawn_pids.txt]]
- Signal directory: [[.cex/runtime/signals/]]

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_orchestration_architecture]] | upstream | 0.32 |
| [[bld_memory_runtime_state]] | related | 0.29 |
| [[p12_wf_create_orchestration_agent]] | downstream | 0.29 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.28 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.27 |
| [[bld_collaboration_session_state]] | related | 0.27 |
| [[runtime-state-builder]] | related | 0.27 |
| [[bld_tools_session_state]] | upstream | 0.27 |
| [[p01_kc_session_backend]] | related | 0.26 |
| [[n07_output_orchestration_audit]] | downstream | 0.26 |
