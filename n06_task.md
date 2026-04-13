---
id: p04_kc_task
kind: knowledge_card
type: kind
pillar: P04
title: "Task — Structured Workflow for task"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p04, reusable, kind-kc]
tldr: "Structured workflow decomposition with phase-based execution, trigger conditions, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about task artifacts"
keywords: [task, phases, trigger, reusable, workflow, lifecycle]
feeds_kinds: [task]
density_score: 0.85
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4064
naming: p04_task_{{name}}.md + .yaml
core: true
```

## What It Is
A task is a structured workflow decomposition with phase-based execution, trigger conditions, and lifecycle management. It defines a specific sequence of operations that can be executed repeatedly across different contexts. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what phases execute to achieve this workflow?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Task` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| task_type | enum | "user_invocable" | user_invocable (slash commands) vs system_defined (programmatic) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "markdown" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| plan | Context gathering | user_input, environment | context_data |
| execute | Main workflow | context_data, user_preferences | raw_results |
| monitor | Quality assurance | raw_results, criteria | validated_output |
| finalize | Post-processing | validated_output, metadata | final_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/analyze", "/optimize" | User types exact command |
| keyword_match | "debug", "audit" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_task("audit") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate task |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable task (slash command)
trigger_type: user_invocable
slash_command: "/audit"
phases: [plan, analyze, report]

# Agent-only task (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_task('data_analysis')"
phases: [load, transform, analyze, export]

# Event-driven task
trigger_type: event_driven
event_pattern: "file_change:*.ts"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase task | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in task | Mixing concerns | Use agent for identity, task for workflow |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Tasks are loaded by agents to extend capabilities
- **F3 INJECT**: Tasks can inject domain-specific knowledge
- **F5 CALL**: Tasks orchestrate tool usage across phases
- **Handoffs**: Tasks can be passed between nuclei for specialized execution
- **Memory**: Tasks can persist state between phases via memory_scope

Tasks enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Tasks
OpenClaude ships ~18 bundled tasks as battle-tested implementations:

| Task | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /analyze | slash_command | 3-parallel-agent review | p04_task_analyze |
| /audit | slash_command | adversarial verification | p04_task_audit |
| /optimize | agent_invoked | 9-section summarization | p04_task_optimize |
| /loop | slash_command | recurring cron schedule | p04_task_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tasks are defined as prompt text with frontmatter,
not as code. The task body IS the prompt injected when the task triggers. This
maps directly to CEX's task-as-artifact model.

**Parallel dispatch pattern** (from /analyze):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any task can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /optimize):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Task Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial task | Agent explicitly tries to BREAK the implementation | p04_task_audit |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_task_analyze |
| Scratchpad task | <analysis> block for private reasoning, stripped from output | p04_task_optimize |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_task_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_task_audit |
