---
id: p01_kc_steps
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "Steps — Foundation for pattern"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: steps
quality: 9.1
tags: [steps, p04, reusable, kind-kc]
tldr: "Reusable foundation with structured phases, triggers, and lifecycle management for repeatable workflow execution"
when_to_use: "Building, reviewing, or reasoning about steps artifacts"
keywords: [steps, phases, trigger, reusable, workflow, lifecycle]
feeds_kinds: [steps]
density_score: null
related:
  - p01_kc_hook
  - p01_kc_server_tools
  - p01_kc_supabase_mcp
  - p01_kc_retriever_config
  - p01_kc_skill
  - p01_kc_workflow
  - bld_knowledge_card_workflow
  - bld_instruction_chain
  - p11_qg_workflow
  - bld_knowledge_card_skill
---

# Steps

## Spec
```yaml
kind: steps
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_steps_{{name}}.md + .yaml
core: true
```

## What It Is
Steps is a reusable foundation with structured phases, trigger conditions, and lifecycle management. It defines a sequence of actions that can be executed repeatedly across different contexts. Steps are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A steps answers "what phases execute to achieve this workflow?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` / `Step` | Sequential execution with defined steps |
| LlamaIndex | `Pipeline` / `Step` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Step definition with sequential/hierarchical execution |
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
| slash_command | "/run", "/execute" | User types exact command |
| keyword_match | "start", "process" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_steps("process") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate steps |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable steps (slash command)
trigger_type: user_invocable
slash_command: "/run"
phases: [discover, execute, report]

# Agent-only steps (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_steps('process')"
phases: [load, transform, execute, export]

# Event-driven steps
trigger_type: event_driven
event_pattern: "file_change:*.txt"
phases: [detect, process, validate, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase steps | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in steps | Mixing concerns | Use agent for identity, steps for workflow |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Steps are loaded by agents to extend foundational capabilities
- **F3 INJECT**: Steps can inject domain-specific knowledge
- **F5 CALL**: Steps orchestrate tool usage across phases
- **Handoffs**: Steps can be passed between nuclei for specialized execution
- **Memory**: Steps can persist state between phases via memory_scope

Steps enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Steps
OpenClaude ships ~18 bundled steps as battle-tested implementations:

| Steps | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /run | slash_command | 3-parallel-agent execution | p04_steps_run |
| /process | slash_command | adversarial processing | p04_steps_process |
| /analyze | agent_invoked | 9-section analysis | p04_steps_analyze |
| /loop | slash_command | recurring cron schedule | p04_steps_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |
```
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_hook]] | sibling | 0.64 |
| [[p01_kc_server_tools]] | sibling | 0.61 |
| [[p01_kc_supabase_mcp]] | sibling | 0.56 |
| [[p01_kc_retriever_config]] | sibling | 0.52 |
| [[p01_kc_skill]] | sibling | 0.51 |
| [[p01_kc_workflow]] | sibling | 0.40 |
| [[bld_knowledge_card_workflow]] | sibling | 0.38 |
| [[bld_instruction_chain]] | upstream | 0.35 |
| [[p11_qg_workflow]] | downstream | 0.32 |
| [[bld_knowledge_card_skill]] | sibling | 0.32 |
