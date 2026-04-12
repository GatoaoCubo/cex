---
id: p04_kc_task
kind: knowledge_card
type: kind
pillar: P04
title: "Task — Structured Workflow for task execution"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p04, reusable, kind-kc]
tldr: "Structured workflow with defined steps, dependencies, and outcomes for repeatable execution"
when_to_use: "Planning, executing, or reviewing task artifacts"
keywords: [task, workflow, dependency, outcome, execution, lifecycle]
feeds_kinds: [task]
density_score: null
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured workflow with defined steps, dependencies, and expected outcomes. It represents a specific action that must be completed within a defined context. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what steps execute to achieve this outcome?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Task` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `Pipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| task_type | enum | "user_assigned" | user_assigned (manual) vs system_event (automatic) |
| dependencies | array | [] | More dependencies = better control vs complexity |
| expected_output | object | {} | Strong typing vs flexibility |
| priority | string | "medium" | Execution priority vs resource allocation |
| deadline | datetime | null | Time constraint vs flexibility |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Define requirements | user_input, context | task_spec |
| execute | Main workflow | task_spec, tools | raw_results |
| review | Quality assurance | raw_results, criteria | validated_output |
| close | Finalize and archive | validated_output | task_record |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| user_assigned | "Assign task to developer" | User explicitly requests action |
| system_event | "File change detected" | Automated trigger by system event |
| deadline_reached | "Task deadline approaching" | Time-based trigger |
| dependency_completion | "All dependencies resolved" | Conditional trigger based on other tasks |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| T01_task_defined | task_type and dependencies not empty | Cannot execute workflow |
| T02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| T03_dependencies_met | All dependencies resolved | Execution fails |
| T04_output_format | Defined output structure | Unpredictable results |
| T05_deadline_met | Deadline not exceeded | Task considered overdue |

## Usage Examples
```yaml
# User-assigned task
task_type: user_assigned
dependencies: [task_123, task_456]
phases: [plan, execute, review, close]
expected_output:
  status: "completed"
  artifacts: [file_789, report_101]

# System-event triggered task
task_type: system_event
trigger_pattern: "file_change:*.md"
phases: [execute, review, close]
expected_output:
  validation: "passed"
  timestamp: "2026-04-05T14:30:00Z"
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Hard-coded dependencies | Not reusable | Use dependency declarations |
| Ignoring deadlines | Poor resource management | Set explicit deadlines |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to execute specific actions
- **F3 INJECT**: Tasks can inject contextual requirements
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /assign | user_assigned | Manual task assignment | p04_task_assign |
| /auto | system_event | Automatic execution | p04_task_auto |
| /review | user_assigned | Quality check | p04_task_review |
| /monitor | system_event | Continuous monitoring | p04_task_monitor |
| /archive | deadline_reached | Task closure | p04_task_archive |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter,
not as code. The task body IS the prompt injected when the task triggers. This
maps directly to CEX's task-as-artifact model.

**Parallel execution pattern** (from /assign):
- Phase 1: Identify task requirements
- Phase 2: Dispatch multiple agents concurrently, each with the full context + specialized focus
- Phase 3: Aggregate findings and finalize task
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /review):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Auto-executing task | Runs automatically when conditions are met | p04_task_auto |
| Parallel review | Multiple focused agents analyze same context concurrently | p04_task_review |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_review |
| Background execution | Runs silently after N turns, executes and archives | p04_task_monitor |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_review |
