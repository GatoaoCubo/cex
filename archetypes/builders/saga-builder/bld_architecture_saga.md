---
id: bld_architecture_saga
kind: knowledge_card
pillar: P08
title: "Architecture: saga Relationships"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: null
tags: [architecture, saga, P12]
llm_function: CONSTRAIN
tldr: "How saga relates to workflow, process_manager, dispatch_rule, and signal."
density_score: null
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
