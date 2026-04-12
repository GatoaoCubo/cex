---
id: n02_task
kind: knowledge_card
type: kind
pillar: P02
title: "Task — Structured workflow execution for repeatable operations"
version: 1.1.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.2
tags: [task, p02, workflow, operation, execution, automation]
tldr: "Structured workflow definition with phase management, resource allocation, and quality assurance for repeatable operations"
when_to_use: "Designing, validating, or executing operational workflows"
keywords: [task, workflow, phase, operation, automation, execution, resource]
feeds_kinds: [task]
density_score: 8.9
---

# Task

## Spec
```yaml
kind: task
pillar: P02
llm_function: EXECUTOR
max_bytes: 4096
naming: p02_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured workflow definition with phase management, resource allocation, and quality assurance. It represents a specific operation that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what steps execute to achieve this operation?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Airflow | `DAG` / `Operator` | Sequential execution with defined steps |
| Prefect | `Flow` / `Task` | Multi-step workflows with phase management |
| Apache Beam | `Pipeline` | Explicit DAG execution with phase transitions |
| Kubeflow | `Pipeline` | Resource allocation and orchestration |
| Luigi | `Task` | Sequential execution with dependencies |
| Dagster | `Job` / `Asset` | Structured computation with defined phases |
| Apache NiFi | `ProcessGroup` | Graphical workflow execution |
| AWS Step Functions | `StateMachine` | Visual workflow orchestration |
| Azure Data Factory | `Pipeline` | Cloud-native workflow execution |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| phase_sequence | array | required | More phases = granular control vs complexity |
| resource_requirements | object | {} | Explicit allocation vs flexibility |
| quality_criteria | object | {} | Structured validation vs adaptability |
| timeout_seconds | int | 3300 | Execution time limit vs complex workflows |
| retry_policy | object | {max_retries: 3} | Resilience vs resource consumption |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| prepare | Resource allocation | task_config, environment | resource_state |
| execute | Main workflow | resource_state, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| archive | Data retention | validated_output, policy | final_record |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| schedule | "0 12 * * *" | Cron-based execution |
| dependency | taskA.complete → taskB.start | Conditional execution |
| event | file_change:*.csv | System event-driven |
| signal | "ready_to_execute" | Manual activation |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phase_sequence not empty | Cannot execute workflow |
| H02_resources_valid | resource_requirements valid | Resource allocation failure |
| H03_criteria_defined | quality_criteria valid | Validation errors |
| H04_timeout_set | timeout_seconds > 0 | Execution timeout |

## Usage Examples
```yaml
# Scheduled task (cron)
phase_sequence: [prepare, execute, validate, archive]
resource_requirements:
  memory: 4GB
  cpu: 2
timeout_seconds: 3600
quality_criteria:
  accuracy: 0.95
  completeness: 0.98

# Dependency-driven task
phase_sequence: [prepare, execute, validate]
resource_requirements:
  database: "prod_db"
  api_key: "secret_key"
trigger_type: dependency
trigger_pattern: "taskA.complete"

# Event-driven task
phase_sequence: [detect, process, archive]
resource_requirements:
  storage: "cloud_bucket"
trigger_type: event
event_pattern: "file_upload:*.csv"
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a function | Use action_prompt for one-off tasks |
| No resource definition | Cannot allocate resources | Use resource_requirements for parameterization |
| Hard-coded criteria | Not reusable | Use quality_criteria for validation |
| Agent identity in task | Mixing concerns | Use agent for identity, task for operation |

## Integration Points
- **F2 BECOME**: Tasks are scheduled by orchestrators to execute operations
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~24 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /analyze | schedule | 3-phase data processing | p02_task_analyze |
| /process | dependency | 5-step transformation | p02_task_process |
| /archive | event | 2-phase retention | p02_task_archive |
| /monitor | signal | 7-step observation | p02_task_monitor |
| /optimize | schedule | 4-phase refinement | p02_task_optimize |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter,
not as code. The task body IS the prompt injected when the task triggers. This
maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /analyze):
- Phase 1: Resource allocation (CPU, memory, storage)
- Phase 2: Dispatch 3 workers concurrently, each with the full dataset + specialized focus
- Phase 3: Aggregate findings and generate output
This pattern generalizes: any task can dispatch parallel sub-workers with typed foci.

**Analysis scratchpad pattern** (from /optimize):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Batch processing | Multiple items processed in parallel | p02_task_batch |
| Pipeline orchestration | Sequential task execution | p02_task_pipeline |
| Conditional branching | Task execution based on criteria | p02_task_branch |
| Background execution | Runs silently after N turns | p02_task_background |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p02_task_verify |
```
```