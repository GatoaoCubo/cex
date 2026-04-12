---
id: n04_task
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n04_task_taxonomy.md + .yaml
core: true
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: task
quality: 9.1
tags: [task, p04, reusable, kind-kc]
tldr: "Structured framework for defining task execution patterns with phase-based workflows and quality gates"
when_to_use: "Designing, reviewing, or reasoning about task artifacts"
keywords: [task, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [task]
density_score: 8.9
---

# Task

## Spec
```yaml
kind: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n04_task_taxonomy.md + .yaml
core: true
```

## What It Is
A task is a structured framework for defining repeatable execution patterns with phase-based workflows and quality gates. It defines a specific workflow that can be executed across different contexts while maintaining consistency and quality. Tasks are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A task answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Chain` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.Module.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| trigger_type | enum | "user_invocable" | user_invocable (slash commands) vs agent_only (programmatic) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "markdown" | Structured output vs natural language |
| timeout_seconds | int | 3
```