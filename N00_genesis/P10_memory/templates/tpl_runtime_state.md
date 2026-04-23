---
id: tpl_runtime_state
kind: runtime_state
pillar: P10
version: 1.0.0
title: "Template — Runtime State"
tags: [template, runtime, state, session, checkpoint]
tldr: "Captures the ephemeral state of a running agent or pipeline. Includes current step, accumulated context, timing, errors, and checkpoint data for pause/resume."
quality: 9.0
related:
  - p12_checkpoint
  - p03_sp_checkpoint_builder
  - p09_arch_task_queue
  - p01_kc_checkpoint
  - bld_collaboration_session_state
  - bld_knowledge_card_checkpoint
  - p11_qg_checkpoint
  - bld_collaboration_checkpoint
  - bld_architecture_checkpoint
  - bld_output_template_checkpoint
---

# Runtime State: [SESSION_ID]

## Purpose
[WHAT execution this state tracks — 8F build, multi-step workflow, agent session]

## State Schema
```yaml
session_id: "[UUID]"
nucleus: "[N01-N07]"
kind: "[artifact kind being produced]"
status: [running | paused | completed | failed]
started_at: "[ISO8601]"
updated_at: "[ISO8601]"
current_step: [1-8]
```

## Step Progress

| Step | Status | Duration | Output |
|------|--------|----------|--------|
| F1 CONSTRAIN | [done\|running\|pending] | [Nms] | constraints loaded |
| F2 BECOME | [done\|running\|pending] | [Nms] | identity set |
| F3 INJECT | [done\|running\|pending] | [Nms] | N KCs injected |
| F4 REASON | [done\|running\|pending] | [Nms] | plan generated |
| F5 CALL | [done\|running\|pending] | [Nms] | tools scanned |
| F6 PRODUCE | [done\|running\|pending] | [Nms] | artifact generated |
| F7 GOVERN | [done\|running\|pending] | [Nms] | N/N gates passed |
| F8 COLLABORATE | [done\|running\|pending] | [Nms] | saved + committed |

## Accumulated Context
```yaml
constraints: { max_bytes: N, fields: N, id_pattern: "..." }
identity: { builder: "...", persona: "..." }
knowledge: { kcs: N, examples: true, memory: true }
artifact_size: N  # bytes produced so far
```

## Checkpoint (for pause/resume)
```yaml
checkpoint:
  last_completed_step: [F1-F8]
  state_snapshot: "[serialized RunState]"
  resume_from: [F2-F8]
  reason: "[why paused — timeout, manual, error]"
```

## Error Log
```yaml
errors:
  - step: [FN]
    error: "[error message]"
    timestamp: "[ISO8601]"
    retried: [true | false]
    resolved: [true | false]
```

## Cleanup Policy
- **On completion**: Archive to `.cex/learning_records/`, delete runtime state
- **On failure**: Preserve for debugging, auto-cleanup after [24h]
- **On pause**: Preserve indefinitely until manual resume or cleanup

## Quality Gate
- [ ] Session ID is unique
- [ ] Status reflects actual pipeline state
- [ ] Timing tracked per step
- [ ] Checkpoint enables resume from last completed step

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_checkpoint]] | downstream | 0.35 |
| [[p03_sp_checkpoint_builder]] | upstream | 0.28 |
| [[p09_arch_task_queue]] | upstream | 0.26 |
| [[p01_kc_checkpoint]] | downstream | 0.25 |
| [[bld_collaboration_session_state]] | related | 0.24 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.23 |
| [[p11_qg_checkpoint]] | downstream | 0.23 |
| [[bld_collaboration_checkpoint]] | downstream | 0.23 |
| [[bld_architecture_checkpoint]] | upstream | 0.22 |
| [[bld_output_template_checkpoint]] | upstream | 0.22 |
