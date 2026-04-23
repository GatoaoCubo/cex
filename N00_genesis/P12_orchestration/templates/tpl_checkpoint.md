---
id: p12_checkpoint
kind: checkpoint
pillar: P12
version: 1.0.0
title: "Template — Checkpoint"
tags: [template, checkpoint, state, resume, orchestration]
tldr: "Saves pipeline state at a point-in-time for pause/resume. Captures completed steps, accumulated context, and resume instructions. Enables fault-tolerant execution."
quality: 9.0
related:
  - p01_kc_checkpoint
  - bld_architecture_checkpoint
  - p03_sp_checkpoint_builder
  - checkpoint-builder
  - bld_collaboration_checkpoint
  - bld_instruction_checkpoint
  - bld_knowledge_card_checkpoint
  - bld_examples_checkpoint
  - p11_qg_checkpoint
  - bld_output_template_checkpoint
---

# Checkpoint: [CHECKPOINT_ID]

## Purpose
[WHAT execution this checkpoint captures — 8F build, multi-step mission, session]

## Checkpoint Schema
```yaml
id: "[CHECKPOINT_ID]"
session_id: "[SESSION_ID]"
nucleus: "[N01-N07]"
created: "[ISO8601]"
step_completed: [1-8]
total_steps: [8]
status: [paused | failed | timeout]
resume_from: [NEXT_STEP]
```

## State Snapshot

| Field | Content | Size |
|-------|---------|------|
| constraints | Loaded schema + config | ~500B |
| identity | System prompt + manifest | ~1KB |
| knowledge | Injected KCs + examples | ~2KB |
| partial_output | Generated so far | variable |
| errors | Errors encountered | variable |
| timings | Duration per completed step | ~200B |

## Resume Protocol
1. Load checkpoint from `.cex/runtime/checkpoints/`
2. Restore RunState from snapshot
3. Skip steps [1..step_completed]
4. Execute from `resume_from` step
5. On success: delete checkpoint
6. On failure: update checkpoint with new state

## Storage
```
.cex/runtime/checkpoints/
  ckpt_{session_id}_{timestamp}.json
```
- **Retention**: 24h for completed, 7d for failed
- **Max size**: 64KB per checkpoint
- **Cleanup**: Cron job or on-session-start sweep

## When to Checkpoint
- Before LLM call (F6) — most expensive, most likely to fail
- After each completed step — enables granular resume
- On error — capture state for debugging
- On timeout — save progress before kill

## Quality Gate
- [ ] Step number and total tracked
- [ ] Resume instruction is explicit (which step to restart)
- [ ] State is serializable (no live objects)
- [ ] Retention policy prevents disk fill

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_checkpoint]] | related | 0.53 |
| [[bld_architecture_checkpoint]] | upstream | 0.53 |
| [[p03_sp_checkpoint_builder]] | upstream | 0.49 |
| [[checkpoint-builder]] | related | 0.48 |
| [[bld_collaboration_checkpoint]] | related | 0.46 |
| [[bld_instruction_checkpoint]] | upstream | 0.46 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.45 |
| [[bld_examples_checkpoint]] | upstream | 0.44 |
| [[p11_qg_checkpoint]] | upstream | 0.41 |
| [[bld_output_template_checkpoint]] | upstream | 0.41 |
