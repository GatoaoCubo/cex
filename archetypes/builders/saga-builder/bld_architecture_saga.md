---
quality: 8.2
quality: 7.8
id: bld_architecture_saga
kind: knowledge_card
pillar: P08
title: "Architecture: saga Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
tags: [architecture, saga, P12]
llm_function: CONSTRAIN
tldr: "How saga relates to workflow, process_manager, dispatch_rule, and signal."
density_score: null
related:
  - bld_collaboration_workflow
  - p11_qg_workflow
  - bld_memory_workflow
  - bld_architecture_workflow
  - p10_lr_chain_builder
  - p12_wf_builder_8f_pipeline
  - bld_architecture_chain
  - workflow-builder
  - bld_knowledge_card_workflow
  - p03_ins_workflow
---

# Architecture: saga

## Relationship Graph
```
[workflow] --> [saga] (saga extends workflow with compensation)
[signal] <-- [saga step] (each step emits completion signal)
[saga] --> [workflow] (on success: continue; on failure: compensate)
[process_manager] -- SIBLING -- [saga] (different coordination model)
```

## Kind Boundaries
| Kind | Relationship | Boundary |
|------|-------------|---------|
| workflow | PARENT PATTERN | workflow = steps without compensation; saga = steps WITH compensation |
| process_manager | SIBLING | process_manager routes events between services; saga manages transaction rollback |
| dispatch_rule | SIBLING | dispatch_rule is keyword routing; saga is transaction coordination |
| signal | CHILD | saga steps emit signals on completion or failure |
| canary_config | SIBLING | canary_config manages traffic; saga manages transaction integrity |

## Topology Comparison
| Topology | Mechanism | When to Use |
|----------|-----------|------------|
| Choreography | Each service listens for events and acts | Loosely coupled services; no central coordinator |
| Orchestration | Central saga coordinator commands each service | Tight control needed; easier to debug |

## Compensation Chain
```
Step 1 OK -> Step 2 OK -> Step 3 FAIL
                |
                v
Compensate Step 2 -> Compensate Step 1 (reverse order)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_workflow]] | downstream | 0.30 |
| [[p11_qg_workflow]] | downstream | 0.30 |
| [[bld_memory_workflow]] | downstream | 0.29 |
| [[bld_architecture_workflow]] | related | 0.29 |
| [[p10_lr_chain_builder]] | downstream | 0.28 |
| [[p12_wf_builder_8f_pipeline]] | downstream | 0.27 |
| [[bld_architecture_chain]] | related | 0.27 |
| [[workflow-builder]] | downstream | 0.27 |
| [[bld_knowledge_card_workflow]] | sibling | 0.27 |
| [[p03_ins_workflow]] | upstream | 0.25 |
