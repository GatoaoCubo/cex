---
kind: knowledge_card
id: bld_knowledge_card_checkpoint
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for checkpoint production — workflow state snapshot specification
sources: LangGraph docs, Temporal event sourcing patterns, Prefect persistence model, CEX P12 spec
quality: 9.1
title: "Knowledge Card Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_checkpoint_builder
  - bld_collaboration_checkpoint
  - checkpoint-builder
  - bld_architecture_checkpoint
  - bld_instruction_checkpoint
  - p01_kc_checkpoint
  - p11_qg_checkpoint
  - bld_output_template_checkpoint
  - p10_lr_checkpoint_builder
  - bld_schema_checkpoint
---

# Domain Knowledge: checkpoint
## Executive Summary
Checkpoints are serialized workflow state snapshots taken at named steps, enabling resume
after failure, human-in-the-loop pauses, and audit trails. They are stateful (unlike signals),
workflow-bound (unlike session_state), and time-limited (TTL mandatory). The checkpoint is a
contract document — it defines the state schema and resume protocol, not the raw state values.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P12 (Orchestration) |
| llm_function | GOVERN |
| machine_format | yaml |
| naming | p12_ckpt_{workflow}.md |
| max_bytes | 2048 |
| id_prefix | p12_ck |
| id_pattern | `^p12_ck_[a-z][a-z0-9_]+$` |
| layer | runtime |
| core | true |
## Patterns
- **LangGraph checkpointing**: state persistence at graph nodes using SQLite or Postgres backends; human-in-the-loop resume via interrupt_before/interrupt_after; state is a typed dict snapshot per node invocation
- **Temporal event sourcing**: workflow state reconstructed from event history; automatic checkpointing at activity boundaries; versioned workflow definitions allow safe replay
- **Prefect persistence**: task state persisted with result caching; flow run state machine (Scheduled -> Running -> Completed/Failed/Crashed); checkpoint on retry enables cost-efficient reruns
- **Snapshot + log pattern**: full state snapshot at checkpoint creation; incremental event log between checkpoints; resume reconstructs final state from snapshot + log delta
- **Checkpoint chain**: each checkpoint holds parent_checkpoint reference; chain enables rollback to any previous stable state; chains must be pruned via TTL to avoid unbounded growth
| Pattern | When to use | Trade-off |
|---------|-------------|-----------|
| Full snapshot | Small state, infrequent checkpoints | Simple resume, high storage cost |
| Incremental | Large state, frequent checkpoints | Low storage, complex resume |
| Chain | Multi-step workflows needing rollback | Rollback capability, chain management overhead |
| Terminal | Final checkpoint after workflow complete | Audit trail, permanent storage required |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No TTL | Orphan checkpoints accumulate; storage bloat; stale state causes incorrect resume |
| Unbounded state size | Large checkpoints slow persistence and restore; serialize only resumption-critical keys |
| Non-serializable state | Objects that cannot be expressed as yaml/json cannot be persisted across process restarts |
| Missing workflow_ref | Orphan checkpoint — cannot be associated with a workflow for resume or audit |
| Raw values in artifact | Artifact becomes a data store; schema drift; security exposure of sensitive state |
| Skipping parent_checkpoint | Chain breaks; rollback becomes impossible; audit trail has gaps |
| resumable: false without explanation | Callers cannot determine if the checkpoint is a tombstone or a transient failure |
## Application
1. Identify the workflow and the step where the checkpoint is taken
2. List only the state keys needed to re-enter at that step (minimize state scope)
3. Define TTL based on workflow duration and SLA requirements
4. Document resume prerequisites (external dependencies, auth, idempotency)
5. Link to parent checkpoint for chain integrity
6. Validate: state keys typed, TTL set, resume steps enumerated, error field present
## References
- LangGraph: state persistence at graph nodes, SQLite/Postgres backends, human-in-the-loop
- Temporal: event sourcing, automatic checkpointing at activity boundaries
- Prefect: task state persistence, flow run state machines, result caching
- CEX P12: orchestration pillar, checkpoint kind, naming p12_ckpt_{workflow}.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_checkpoint_builder]] | downstream | 0.62 |
| [[bld_collaboration_checkpoint]] | downstream | 0.59 |
| [[checkpoint-builder]] | downstream | 0.54 |
| [[bld_architecture_checkpoint]] | downstream | 0.53 |
| [[bld_instruction_checkpoint]] | downstream | 0.50 |
| [[p01_kc_checkpoint]] | sibling | 0.49 |
| [[p11_qg_checkpoint]] | downstream | 0.49 |
| [[bld_output_template_checkpoint]] | downstream | 0.47 |
| [[p10_lr_checkpoint_builder]] | downstream | 0.45 |
| [[bld_schema_checkpoint]] | downstream | 0.44 |
