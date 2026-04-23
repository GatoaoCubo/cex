---
id: session_state_n03
kind: session_state
nucleus: n03
pillar: P10
mirrors: N00_genesis/P10_memory/templates/tpl_session_state.md
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  engineering_fields: [active_files, recent_diffs, open_tasks, compile_status]
version: 1.0.0
quality: 8.5
tags: [mirror, n03, engineering, hermes_assimilation, session_state]
tldr: "N03 dev session state: tracks active files, recent diffs, open tasks, compile status. Engineering-specific snapshot."
created: "2026-04-18"
related:
  - bld_architecture_session_state
  - p03_sp_session_state_builder
  - bld_knowledge_card_session_state
  - p01_kc_session_state
  - bld_collaboration_session_state
  - session-state-builder
  - p08_pat_context_compaction
  - p01_kc_context_overflow
  - p12_dr_software_project
  - agent_card_engineering_nucleus
density_score: 1.0
updated: "2026-04-22"
---

## Axioms

1. **Session state is ephemeral** -- never persist decisions here; decisions go in `decision_manifest.yaml`.
2. **Engineering context is code-centric** -- active files and compile status are first-class fields.
3. **Refresh on context compaction** -- `cex_hooks_native.py post-compact` triggers a session_state refresh.

## N03 Session State Schema

```yaml
content_session_id: {{STABLE_UUID}}
memory_session_id: {{SDK_SESSION_ID_OR_NULL}}
compression_status: pending | done

# Engineering-specific fields (N03 overrides)
active_files:
  - path: N03_engineering/P02_model/agent_n03.md
    status: in_progress | staged | committed
recent_diffs:
  - path: N03_engineering/P11_feedback/revision_loop_policy_n03.md
    change: created
    timestamp: 2026-04-18T14:00:00
open_tasks:
  - id: task_001
    kind: knowledge_card
    status: planned | in_progress | blocked
compile_status:
  last_run: 2026-04-18T13:55:00
  result: pass | fail
  failing_files: []
```

## Snapshot Template (N03 Engineering)

- Goal: [active_build_goal]
- Stage: [8F_stage_currently_at]
- Active backend: [local | docker | devcontainer]
- Compile: [pass | fail -- N files failing]

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Storing decisions in session_state | Decisions lost on compaction | Write to decision_manifest.yaml instead |
| No compile_status field | Silent failures carried forward | Always populate compile_status after F8 |
| Stale active_files list | Wrong context injected | Refresh on every F8 COLLABORATE |
| Skipping post-compact hook | Session context lost | `cex_hooks_native.py post-compact` is mandatory |

## Integration

- Refreshed by: `cex_hooks_native.py post-compact` and `post-tool-use`
- Read by: F3 INJECT (provides active context to next build)
- Upstream: all N03 build actions update session_state
- Downstream: N07 reads n03 session_state for orchestration decisions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_session_state]] | upstream | 0.29 |
| [[p03_sp_session_state_builder]] | upstream | 0.26 |
| [[bld_knowledge_card_session_state]] | upstream | 0.25 |
| [[p01_kc_session_state]] | related | 0.25 |
| [[bld_collaboration_session_state]] | related | 0.23 |
| [[session-state-builder]] | related | 0.23 |
| [[p08_pat_context_compaction]] | upstream | 0.23 |
| [[p01_kc_context_overflow]] | upstream | 0.22 |
| [[p12_dr_software_project]] | downstream | 0.22 |
| [[agent_card_engineering_nucleus]] | upstream | 0.21 |
