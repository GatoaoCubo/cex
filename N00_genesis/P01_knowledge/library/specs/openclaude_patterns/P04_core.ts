---
id: p04_kc_core
kind: knowledge_card
type: kind
pillar: P04
title: "Core — Deep Knowledge for core"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: core
quality: 9.0
tags: [core, p04, system, artifact]
tldr: "Structured core framework with quality gates, phase analysis, and cross-framework mapping"
when_to_use: "System refinement, quality assurance, or knowledge system enhancement"
keywords: [core, phases, trigger, improvement, lifecycle, quality]
feeds_kinds: [core]
density_score: 0.92
---

# Core Improvement Framework

## Spec
```yaml
kind: core
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_core_{{name}}.md + .yaml
core: true
```

## What It Is
A core is a structured unit of system work with defined phases, trigger conditions, and quality assurance mechanisms. It defines a specific workflow that can be executed repeatedly across different contexts. Cores are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A core answers "what phases execute to achieve this work?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `QueryPipeline` | Multi-step workflows with phase management |
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
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | user_input, environment | context_data |
| configure | Parameter setup | context_data, user_preferences | configuration |
| execute | Main workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |
| archive | Long-term storage | validated_output, metadata | archived_artifact |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/optimize", "/analyze" | User types exact command |
| keyword_match | "debug", "benchmark" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_core("data_analysis") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate core |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |
| H05_archive_valid | archive metadata not empty | Cannot store artifact |

## Usage Examples
```yaml
# User-invocable core (slash command)
trigger_type: user_invocable
slash_command: "/optimize"
phases: [discover, analyze, improve, validate, archive]

# Agent-only core (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_core('data_analysis')"
phases: [load, transform, analyze, export, archive]

# Event-driven core
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify, archive]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase core | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in core | Mixing concerns | Use agent for identity, core for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Cores are loaded by agents to extend capabilities
- **F3 INJECT**: Cores can inject domain-specific knowledge
- **F5 CALL**: Cores orchestrate tool usage across phases
- **Handoffs**: Cores can be passed between nuclei for specialized execution
- **Memory**: Cores can persist state between phases via memory_scope

Core enables modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Cores
OpenClaude ships ~20 bundled cores as battle-tested implementations:

| Core | Trigger | Pattern | CEX Equivalent |
|------|--------|---------|----------------|
| /optimize | slash_command | 3-parallel-agent review | p04_core_optimize |
| /benchmark | slash
