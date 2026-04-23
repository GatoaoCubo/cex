---
kind: architecture
id: bld_architecture_checkpoint
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of checkpoint — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Checkpoint"
version: "1.0.0"
author: n03_builder
tags: [checkpoint, builder, examples]
tldr: "Golden and anti-examples for checkpoint construction, demonstrating ideal structure and common pitfalls."
domain: "checkpoint construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - checkpoint-builder
  - bld_collaboration_checkpoint
  - p03_sp_checkpoint_builder
  - bld_instruction_checkpoint
  - p01_kc_checkpoint
  - bld_schema_checkpoint
  - bld_knowledge_card_checkpoint
  - bld_output_template_checkpoint
  - bld_examples_checkpoint
  - p11_qg_checkpoint
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| workflow_ref | Reference to the parent workflow artifact this checkpoint belongs to | checkpoint | required |
| step | Named step in the workflow at which state is captured | checkpoint | required |
| state | Map of serialized state keys, types, and size hints at capture time | checkpoint | required |
| ttl | Time-to-live policy — duration before cleanup or archival | checkpoint | required |
| resumable | Flag declaring whether workflow can re-enter from this checkpoint | checkpoint | required |
| parent_checkpoint | Reference to the previous checkpoint in the chain | checkpoint | optional |
| retry_count | Number of times the captured step has been retried | checkpoint | optional |
| error | Error message if the checkpoint captures a failed step state | checkpoint | optional |
| backend_store | External persistence layer (SQLite, Postgres, S3) that holds raw state values | P12 infra | external |
| guardrail | Execution constraints — state size cap, TTL enforcement, access policy | P11 | external |
| workflow | The workflow artifact whose execution this checkpoint tracks | P12 | producer |
| agent | Runtime caller that creates and reads checkpoints during workflow execution | P02 | consumer |
| signal | Lightweight event notification (stateless) — distinct from checkpoint | P12 | sibling |
## Dependency Graph
```
workflow      --produces--> checkpoint
step          --depends-->  checkpoint
state         --depends-->  checkpoint
ttl           --depends-->  checkpoint
checkpoint    --produces--> backend_store (raw values)
checkpoint    --produces--> resume_protocol
parent_checkpoint --depends--> checkpoint (chain)
guardrail     --depends-->  checkpoint (size + TTL enforcement)
agent         --depends-->  checkpoint (read/write during execution)
```
| From | To | Type | Data |
|------|----|------|------|
| workflow | checkpoint | produces | workflow_ref, step context |
| step | checkpoint | depends | step name, position in execution graph |
| state | checkpoint | depends | key-type-size schema for serialized values |
| ttl | checkpoint | depends | retention duration and cleanup policy |
| checkpoint | backend_store | produces | raw state values (not in artifact) |
| checkpoint | resume_protocol | produces | step-by-step re-entry instructions |
| parent_checkpoint | checkpoint | depends | chain linkage for rollback |
| guardrail | checkpoint | depends | max_bytes enforcement, TTL policy |
| agent | checkpoint | depends | create on step completion, read on resume |
## Boundary Table
| checkpoint IS | checkpoint IS NOT |
|---------------|------------------|
| Serialized state snapshot with workflow_ref | A stateless event notification (that is signal) |
| Bound to a named step in a specific workflow | Ephemeral session data without workflow context (that is session_state, P10) |
| Enables workflow resume after failure or pause | The workflow definition or execution graph (that is workflow/dag) |
| Has TTL — time-limited by design | A permanent data record or audit log entry |
| Schema contract — state shape, not raw values | A data store — raw values live in backend_store |
| Part of a chain — parent/child linkage | An isolated snapshot with no lineage |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| reference | workflow_ref, step | Bind checkpoint to its workflow execution context |
| state | state, error, retry_count | Capture and model the serialized execution state |
| policy | ttl, resumable | Govern retention duration and resume eligibility |
| chain | parent_checkpoint | Enable rollback and chain-based audit trail |
| governance | guardrail | Enforce size limits and TTL compliance |
| consumers | agent, workflow | Runtime actors that create and read checkpoints |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[checkpoint-builder]] | downstream | 0.73 |
| [[bld_collaboration_checkpoint]] | downstream | 0.72 |
| [[p03_sp_checkpoint_builder]] | upstream | 0.71 |
| [[bld_instruction_checkpoint]] | upstream | 0.63 |
| [[p01_kc_checkpoint]] | downstream | 0.63 |
| [[bld_schema_checkpoint]] | upstream | 0.61 |
| [[bld_knowledge_card_checkpoint]] | upstream | 0.59 |
| [[bld_output_template_checkpoint]] | upstream | 0.59 |
| [[bld_examples_checkpoint]] | upstream | 0.57 |
| [[p11_qg_checkpoint]] | downstream | 0.56 |
