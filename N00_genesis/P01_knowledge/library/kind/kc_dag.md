---
id: p01_kc_dag
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P12
title: "DAG — Deep Knowledge for dag"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: dag
quality: 9.1
tags: [dag, P12, PRODUCE, kind-kc]
tldr: "Directed acyclic dependency graph defining execution order and parallelism for multi-task workflows"
when_to_use: "Building, reviewing, or reasoning about dag artifacts"
keywords: [dependencies, parallelism, topology]
feeds_kinds: [dag]
density_score: null
related:
  - bld_architecture_dag
  - bld_knowledge_card_dag
  - dag-builder
  - bld_collaboration_dag
  - p01_kc_workflow
  - bld_schema_dag
  - p11_qg_dag
  - p12_dag_builder_8f
  - bld_instruction_dag
  - p01_kc_orchestration_runtime
---

# DAG

## Spec
```yaml
kind: dag
pillar: P12
llm_function: PRODUCE
max_bytes: 3072
naming: p12_dag_{{pipeline}}.yaml
core: false
```

## What It Is
A DAG (Directed Acyclic Graph) is a dependency specification that defines which tasks must complete before others can start, enabling automatic parallelism detection and execution ordering. It encodes nodes (tasks/agents), edges (dependencies), and execution wave assignments. It is NOT workflow (P12 — workflow is the executable specification that includes steps, agents, and tools; DAG is the dependency structure only) nor component_map (P08 — maps system components and their relationships at architecture level).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableParallel` + `RunnableSequence` | LCEL composes parallel and sequential runnables into implicit DAG |
| LlamaIndex | `IngestionPipeline` + `Workflow` events | IngestionPipeline has sequential steps; Workflow has event-driven DAG |
| CrewAI | `Crew(tasks=[...])` with `context=[other_task]` | Task dependencies defined via context param; sequential default |
| DSPy | `dspy.Module.forward()` composition | Explicit Python function call graph; implicit DAG via control flow |
| Haystack | `Pipeline` (directed multigraph) | Native DAG: `pipeline.connect(comp_a.out, comp_b.in)` |
| OpenAI | N/A — custom orchestration required | No native DAG; implement via function chaining or workflow tools |
| Anthropic | N/A — custom orchestration required | Tool use with explicit ordering; no declarative DAG construct |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| nodes | list | required | Task/agent names; more nodes = more parallelism potential |
| edges | list | required | `[from, to]` dependency pairs; acyclic enforced |
| waves | map | auto | Execution waves (parallel groups); auto-computed from edges |
| critical_path | list | auto | Longest dependency chain; determines minimum execution time |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Wave-parallel execution | Multiple independent tasks | Wave 1: [research, scrape] parallel → Wave 2: [write] depends on both |
| Fan-out/fan-in | One task feeds multiple, then merge | task_A → [task_B, task_C, task_D] → task_E (merge) |
| Critical path optimization | Performance-critical pipelines | Identify critical path; prioritize resources on blocking tasks |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Cycle in dependency graph | Deadlock; execution never completes | Validate acyclicity before execution; topological sort fails on cycles |
| Sequential DAG with no parallel nodes | Same as a list; DAG overhead with no benefit | Review dependencies; most research + build tasks can parallelize |
| Overly fine-grained nodes | Scheduling overhead exceeds task duration | Batch micro-tasks into meaningful atomic units |

## Integration Graph
```
[workflow] --> [dag] --> [spawn_config]
[dispatch_rule] --^  |
                 [schedule]
```

## Decision Tree
- IF tasks have no dependencies THEN all in wave 1 (fully parallel)
- IF task B depends on task A THEN B in next wave after A
- IF cycle detected THEN fail fast — rearchitect dependencies
- DEFAULT: Auto-compute waves from edges; validate acyclicity before first execution

## Quality Criteria
- GOOD: Has nodes, edges, waves (or auto-computed); acyclicity validated; YAML parseable
- GREAT: Critical path identified; fan-out/fan-in nodes labeled; execution time estimate per wave
- FAIL: Contains cycles; sequential-only (no parallelism); nodes undefined; waves not computed

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_dag]] | upstream | 0.54 |
| [[bld_knowledge_card_dag]] | sibling | 0.48 |
| [[dag-builder]] | related | 0.47 |
| [[bld_collaboration_dag]] | related | 0.47 |
| [[p01_kc_workflow]] | sibling | 0.45 |
| [[bld_schema_dag]] | upstream | 0.40 |
| [[p11_qg_dag]] | upstream | 0.40 |
| [[p12_dag_builder_8f]] | related | 0.39 |
| [[bld_instruction_dag]] | upstream | 0.38 |
| [[p01_kc_orchestration_runtime]] | sibling | 0.38 |
