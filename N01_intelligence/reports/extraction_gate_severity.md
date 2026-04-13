---
id: p01_kc_extraction_gate_severity
kind: knowledge_card
type: kind
pillar: P04
title: "Extraction Gate Severity — Deep Knowledge for extraction gate severity"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: extraction_gate_severity
quality: 9.1
tags: [extraction_gate_severity, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about extraction gate severity artifacts"
keywords: [extraction_gate_severity, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [extraction_gate_severity]
density_score: null
---

# Extraction Gate Severity

## Spec
```yaml
kind: extraction_gate_severity
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_extraction_gate_severity_{{name}}.md + .yaml
core: true
```

## What It Is
Extraction gate severity is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Extraction gate severity is NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). An extraction gate severity answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

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
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | user_input, environment | context_data |
| configure | Parameter setup | context_data, user_preferences | configuration |
| execute | Main workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/commit", "/deploy" | User types exact command |
| keyword_match | "debug", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_skill("analyze") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate skill |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable skill (slash command)
trigger_type: user_invocable
slash_command: "/review"
phases: [discover, analyze, report]

# Agent-only skill (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_skill('data_analysis')"
phases: [load, transform, analyze, export]

# Event-driven skill
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase skill | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in skill | Mixing concerns | Use agent for identity, skill for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Skills are loaded by agents to extend capabilities
- **F3 INJECT**: Skills can inject domain-specific knowledge
- **F5 CALL**: Skills orchestrate tool usage across phases
- **Handoffs**: Skills can be passed between nuclei for specialized execution
- **Memory**: Skills can persist state between phases via memory_scope

Extraction gate severity enables modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Skills
OpenClaude ships ~18 bundled skills as battle-tested implementations:

| Skill | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /simplify | slash_command | 3-parallel-agent review | p04_skill_simplify |
| /verify | slash_command | adversarial verification | p04_skill_verify |
| /compact | agent_invoked | 9-section summarization | p04_skill_compact |
| /loop | slash
