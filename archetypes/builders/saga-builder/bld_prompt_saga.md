---
quality: 8.0
quality: 7.7
id: bld_instruction_saga
kind: instruction
pillar: P12
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
title: "Saga Builder Instructions"
target: "saga-builder agent"
phases_count: 5
prerequisites:
  - "Business transaction is identified (what must succeed end-to-end)"
  - "At least 2 participant services or nuclei are known"
  - "Compensating action for each step is definable"
tags: [instruction, saga, P12, distributed_transaction]
llm_function: REASON
tldr: "Build a saga with forward steps, compensating actions, failure modes, and rollback sequence."
density_score: null
related:
  - bld_instruction_chain
  - p03_ins_workflow
  - p10_lr_chain_builder
  - p11_qg_workflow
  - bld_knowledge_card_workflow
  - p12_wf_builder_8f_pipeline
  - tpl_instruction
  - bld_architecture_chain
  - p11_qg_chain
  - p03_sp_workflow-builder
---
## Context
The saga-builder produces a `saga` artifact -- a distributed transaction specification where each step has a compensating action. If any step fails, completed steps are undone in reverse order. NOT workflow (no compensation), NOT process_manager (event routing without undo), NOT chain (prompt chaining).

**Input contract**:
- `saga_name`: string -- kebab-case transaction name
- `goal`: string -- one sentence: what the saga accomplishes end-to-end
- `steps`: list -- each with id, participant, action, compensating_action
- `topology`: enum -- choreography | orchestration
- `on_failure`: enum -- compensate_all | compensate_partial | abort

## Phases

### Phase 1: Define the Transaction Goal
State what succeeds if all steps complete. This is the saga's commit point.

### Phase 2: Enumerate Steps
For each step:
- `id`: step identifier
- `participant`: service or nucleus
- `action`: what the participant does (forward)
- `compensating_action`: what undoes the forward action
- `depends_on`: prior step ids (if ordered)
- `on_failure`: compensate | retry | skip

Assert: EVERY step has a compensating_action. No step without compensation.

### Phase 3: Define Rollback Sequence
List compensating actions in reverse order of steps completed:
- Step N fails -> execute compensating_action for steps N-1, N-2, ..., 1 in that order.

### Phase 4: Choose Topology
- `choreography`: each participant listens for events and decides own action (decentralized)
- `orchestration`: a central saga orchestrator sends commands to each participant (centralized)

### Phase 5: Compose Artifact
Required frontmatter: id, kind, pillar, saga_name, steps_count, topology, on_failure, quality: null.
Required body: Goal, Steps (table with forward + compensating), Rollback Sequence, Topology.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_chain]] | sibling | 0.38 |
| [[p03_ins_workflow]] | sibling | 0.37 |
| [[p10_lr_chain_builder]] | upstream | 0.36 |
| [[p11_qg_workflow]] | related | 0.33 |
| [[bld_knowledge_card_workflow]] | upstream | 0.33 |
| [[p12_wf_builder_8f_pipeline]] | related | 0.32 |
| [[tpl_instruction]] | sibling | 0.30 |
| [[bld_architecture_chain]] | upstream | 0.30 |
| [[p11_qg_chain]] | upstream | 0.29 |
| [[p03_sp_workflow-builder]] | upstream | 0.29 |
