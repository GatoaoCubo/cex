---
id: p12_dag_builder_construction
kind: dag
pillar: P12
title: "DAG — N03 Builder Task Dependencies"
version: 2.0.0
created: 2026-04-07
updated: 2026-04-07
author: builder_agent
domain: construction
quality: 9.1
tags: [dag, builder, N03, dependencies, orchestration, pipeline]
tldr: "Dependency graph for N03 builder artifacts — identity before orchestration, schema before quality gate."
density_score: 0.93
linked_artifacts:
  primary: "N03_builder/orchestration/workflow_builder.md"
  related:
    - N03_builder/orchestration/dispatch_rule_builder.md
    - N07_admin/orchestration/dag_admin.md
---

# DAG — N03 Builder Task Dependencies

## Purpose

Defines the dependency order for building N03 fractal artifacts. Some artifacts reference others and must be built in sequence. Independent artifacts can be built in parallel within a grid dispatch.

## Dependency Graph

```
                    ┌─────────────┐
                    │   README    │
                    │  (root)     │
                    └──────┬──────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │  Agent   │ │  System  │ │  Agent   │
        │  Card    │ │  Prompt  │ │  Def     │
        │  (P08)   │ │  (P03)   │ │  (P02)   │
        └────┬─────┘ └────┬─────┘ └────┬─────┘
             │             │            │
             └──────┬──────┘            │
                    │                   │
        ┌───────────┼───────────┐       │
        ▼           ▼           ▼       ▼
  ┌──────────┐ ┌──────────┐ ┌─────────────┐
  │Knowledge │ │ Schema   │ │Architecture │
  │  Card    │ │  (P06)   │ │   (P08)     │
  │  (P01)   │ │          │ │             │
  └────┬─────┘ └────┬─────┘ └──────┬──────┘
       │             │              │
       └──────┬──────┘              │
              ▼                     │
        ┌──────────┐               │
        │ Quality  │               │
        │  Gate    │               │
        │  (P07)   │               │
        └────┬─────┘               │
             │                     │
             └──────┬──────────────┘
                    ▼
  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
  │ Dispatch │ │ Workflow │ │ Handoff  │ │  Signal  │
  │  Rule    │ │  (P12)   │ │  (P12)   │ │  (P12)   │
  │  (P12)   │ │          │ │          │ │          │
  └──────────┘ └──────────┘ └──────────┘ └──────────┘
       │             │            │            │
       └──────┬──────┴────────────┴────────────┘
              ▼
        ┌──────────┐ ┌──────────┐
        │  Spawn   │ │  Memory  │
        │  Config  │ │ Records  │
        │  (P12)   │ │  (P10)   │
        └──────────┘ └──────────┘
```

## Build Waves

### Wave 0 (Independent — no dependencies)
- `README.md` — fractal module description

### Wave 1 (Depends on README)
- `agents/agent_builder.md` — agent definition
- `prompts/system_prompt_builder.md` — system prompt
- `agent_card_n03.md` — root agent card

### Wave 2 (Depends on Wave 1)
- `architecture/agent_card_builder.md` — component map
- `knowledge/knowledge_card_builder.md` — knowledge card
- `schemas/artifact_schema_builder.md` — schema definition

### Wave 3 (Depends on Wave 2)
- `quality/quality_gate_builder.md` — quality gate

### Wave 4 (Depends on Waves 1-3)
- `orchestration/dispatch_rule_builder.md` — routing rules
- `orchestration/workflow_builder.md` — workflow definitions
- `orchestration/handoff_builder.md` — handoff contract
- `orchestration/signal_builder.md` — signal protocol

### Wave 5 (Depends on Wave 4)
- `orchestration/spawn_config_builder.md` — spawn configuration
- `memory/8f_pipeline_mastery.md` — learning record

## Comparison of Build Waves

| Wave | Dependencies | Artifacts Built | Parallelism | Purpose |
|------|--------------|------------------|-------------|---------|
| 0    | None         | README.md        | Full        | Module description |
| 1    | Wave 0       | Agent, Prompt, Card | Full | Core definitions |
| 2    | Wave 1       | Architecture, Knowledge, Schema | Full | Structural foundations |
| 3    | Wave 2       | Quality Gate     | Sequential  | Validation layer |
| 4    | Waves 1-3    | Dispatch, Workflow, Handoff, Signal | Partial | Orchestration rules |
| 5    | Wave 4       | Spawn Config, Memory Records | Sequential | Final configuration |

## Parallel Opportunities

Within each wave, all artifacts are independent and can be built in parallel. Cross-wave dependencies are strict — do not build Wave N+1 until Wave N completes.

## References

- N07 master DAG: N07_admin/orchestration/dag_admin.md
- Workflow: N03_builder/orchestration/workflow_builder.md

## Boundary

Acyclic graph of dependencies between tasks. Not a workflow (direct execution) nor a component_map (P08, components).

## Related Kinds

- **Workflow**: Defines execution steps that depend on completed DAG artifacts
- **Component Map**: Describes system components that require DAG completion for validation
- **Quality Gate**: Enforces standards that must be satisfied before DAG progression
- **Dispatch Rule**: Uses DAG outputs to determine task routing
- **Artifact Schema**: Provides data structure definitions required by DAG nodes

## 8F Pipeline Function

Primary function: **PRODUCE**