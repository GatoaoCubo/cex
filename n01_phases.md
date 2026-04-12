---
id: n01_phases_structure
kind: phases
type: guide
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_phases_{{name}}.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: phases
quality: 9.1
tags: [phases, p04, reusable, kind-kc]
tldr: "Structured framework for defining phase-based workflows with quality gates, parameterization, and framework integration"
when_to_use: "Building, reviewing, or reasoning about phase artifact patterns"
keywords: [phases, structure, workflow, orchestration, lifecycle, parallel]
feeds_kinds: [phases]
density_score: 8.9
---

# Phase Structure

## Spec
```yaml
kind: phases
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_phases_{{name}}.md + .yaml
core: true
```

## What It Is
A phase structure is a structured framework for defining phase-based workflows with quality gates, parameterization, and framework integration. It defines how tasks are decomposed into sequential or parallel phases, executed, and coordinated across different systems. Phase structures are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A phase structure answers "how do we sequence workflow execution?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Map
| Platform/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| Kubernetes | `Job` / `CronJob` | Phase-based task execution with scheduling |
| Docker | `Compose` | Multi-phase container orchestration |
| AWS Step Functions | `State Machine` | Visual workflow with parallel/sequential phases |
| Azure Data Factory | `Pipeline` | Multi-phase data processing framework |
| Apache Airflow | `DAG` | Directed acyclic graph for phase orchestration |
| Luigi | `Task` + `Pipeline` | Python-based phase coordination |
| Prefect | `Flow` / `Task` | Modern workflow orchestration with phase execution |
| Dask | `Parallel` / `Distributed` | Python library for parallel phase computing |
| Ray | `Actor` / `Task` | Distributed computing framework for phase execution |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| phase_type | enum | "sequential" | sequential (one after another) vs parallel (simultaneous) |
| phase_parallelism | int | 4 | Number of concurrent phases |
| resource_allocation | object | {} | Resource management vs flexibility |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |
| retry_policy | object | {max_retries: 3} | Error handling vs computational cost |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Workflow decomposition | user_input, environment | phase_graph |
| schedule | Resource allocation | phase_graph, user_preferences | resource_plan |
| execute | Phase execution | resource_plan, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| manual | /phase, /run | User initiates execution |
| automated | cron, webhook | System event triggers |
| conditional | threshold, alert | Based on data conditions |
| hybrid | manual + automated | Mixed trigger sources |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phase_defined | phase_type in allowed values | Cannot execute workflow |
| H02_parallelism_valid | phase_parallelism > 0 | Cannot activate phase structure |
| H03_resource_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# Sequential phase structure
phase_type: sequential
phase_parallelism: 1
phases: [plan, schedule, execute, validate]

# Parallel phase structure
phase_type: parallel
phase_parallelism: 8
phases: [plan, schedule, execute, validate]

# Conditional phase structure
phase_type: sequential
trigger_type: conditional
condition: "data > threshold"
phases: [plan, schedule, execute, validate]

# Hybrid phase structure
phase_type: parallel
trigger_type: hybrid
manual_trigger: true
cron_schedule: "0 0 * * *"
phases: [plan, schedule, execute, validate]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase structure | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Hard-coded parameters | Not reusable | Use resource_allocation for parameterization |
| Agent identity in phases | Mixing concerns | Use agent for identity, phases for orchestration |

## Integration Points
- **F2 BECOME**: Phase structures are loaded by orchestrators to extend capabilities
- **F3 INJECT**: Phases can inject execution parameters
- **F5 CALL**: Phases orchestrate tool usage across phases
- **Handoffs**: Phases can be passed between nuclei for specialized execution
- **Memory**: Phases can persist state between phases via memory_scope

Phase structures enable modular, reusable workflow orchestration that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Phase Structures
OpenClaude ships ~15 bundled phase structures as battle-tested implementations:

| Structure | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /sequential | slash_command | 3-phase review | p04_phases_sequential |
| /parallel | slash_command | adversarial verification | p04_phases_parallel |
| /async | agent_invoked | 9-section summarization | p04_phases_async |
| /cron | slash_command | recurring cron schedule | p04_phases_cron (future) |
| /monitor | slash, agent_invoked | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Phase structures are defined as prompt text with frontmatter,
not as code. The phase body IS the prompt injected when the structure triggers. This
maps directly to CEX's phase-as-artifact model.

**Parallel phase pattern** (from /parallel):
- Phase 1: Identify tasks (task decomposition)
- Phase 2: Dispatch 3 agents concurrently, each with the full task + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any phase structure can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /sequential):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Phase Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial phase | Agent explicitly tries to BREAK the implementation | p04_phases_parallel |
| Parallel review | Multiple focused agents analyze same task concurrently | p04_phases_parallel |
| Scratchpad phase | <analysis> block for private reasoning, stripped from output | p04_phases_async |
| Background execution | Runs silently after N turns, extracts persistent memories | p04_phases_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_phases_parallel |
