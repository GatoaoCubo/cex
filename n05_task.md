---
id: n05_task
kind: knowledge_card
type: task
pillar: P05
title: "Task — Deep Knowledge for task execution"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p05, reusable, kind-kc]
tldr: "Reusable workflow with structured phases, trigger conditions, and lifecycle management for repeatable execution"
when_to_use: "Building, reviewing, or reasoning about task artifacts"
keywords: [task, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [task]
density_score: 0.92
---

# Task

## Spec
```yaml
kind: task
pillar: P05
llm_function: TOOL
max_bytes: 4096
naming: p05_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a reusable workflow with structured phases, trigger conditions, and lifecycle management. It defines a specific sequence of operations that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what steps execute to achieve this outcome?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Chain` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |
| OpenClaude | `CexTask` | Task-centric execution with phase lifecycle |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| trigger_type | enum | "user_invocable" | user_invocable (slash commands) vs agent_only (programmatic) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |
| dependencies | array | [] | Explicit dependencies vs implicit flow |
| concurrency | enum | "serial" | Parallel execution vs resource contention |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Context analysis | user_input, environment | context_data |
| prepare | Resource allocation | context_data, user_preferences | resources |
| execute | Main workflow | resources, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| archive | State persistence | validated_output, memory_scope | persisted_state |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/compile", "/deploy" | User types exact command |
| keyword_match | "build", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | task.use("analyze") | Programmatic call from agent |
| cron_schedule | "0 0 * * *" | Time-based automation |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |
| H05_dependencies_valid | All dependencies exist | Execution failures |
| H06_concurrency_valid | concurrency in allowed values | Resource contention |

## Usage Examples
```yaml
# User-invocable task (slash command)
trigger_type: user_invocable
slash_command: "/compile"
phases: [plan, prepare, execute, validate]

# Agent-only task (programmatic)
trigger_type: agent_only
invoke_pattern: "task.use('data_analysis')"
phases: [plan, prepare, execute, validate]
dependencies: ["preprocess", "validate"]
concurrency: "parallel"

# Event-driven task
trigger_type: event_driven
event_pattern: "file_change:*.ts"
phases: [detect, process, archive]
concurrency: "serial"

# Cron-scheduled task
trigger_type: cron_schedule
cron_expression: "0 0 * * *"
phases: [plan, execute, archive]
output_format: "json"
timeout_seconds: 600
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| No phase definition | Cannot execute workflow | Define clear phase sequence |
| Natural language output | Not reusable | Use structured output format |
| Hard-coded dependencies | Not reusable | Use dependency declarations |
| Mixed concurrency modes | Resource contention | Define explicit concurrency mode |
| Missing quality gates | Execution failures | Implement validation checks |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend capabilities
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

## Industry References
| Standard | Description | Relevance |
|---------|-------------|----------|
| ISO 26514 | AI Management Systems | Framework for task governance |
| IEEE 7000 | AI System Standards | Technical requirements for task design |
| NIST AI Risk Management | Risk assessment framework | Compliance alignment |
| OpenAI Prompt Engineering Guide | Best practices | Implementation reference |

## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /compile | slash_command | 3-parallel-agent execution | p05_task_compile |
| /deploy | slash_command | adversarial verification | p05_task_deploy |
| /analyze | agent_invoked | 9-section summarization | p05_task_analyze |
| /loop | cron_schedule | recurring cron schedule | p05_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter, not as code. The task body IS the prompt injected when the task triggers. This maps directly to CEX's task-as-artifact model.

**Parallel execution pattern** (from /compile):
- Phase 1: Analyze codebase structure (file scan)
- Phase 2: Dispatch 3 agents concurrently, each with the full codebase + specialized focus
- Phase 3: Aggregate findings and execute fixes directly
This pattern generalizes: any task can dispatch parallel sub-tasks with typed foci.

**Analysis scratchpad pattern** (from /analyze):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Task explicitly tries to BREAK the implementation | p05_task_validate |
| Parallel execution | Multiple focused agents analyze same code concurrently | p05_task_compile |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p05_task_analyze |
| Background extract | Runs silently after N turns, extracts persistent memories | p05_task_memory_extract |
| Rationalization counter | Lists excuses the task will generate, pre-emptively counters | p05_task_validate |
