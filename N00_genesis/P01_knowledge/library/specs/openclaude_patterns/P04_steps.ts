---
id: p04_kc_steps
kind: knowledge_card
type: kind
pillar: P04
title: "Steps — Deep Knowledge for steps"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: steps
quality: 9.1
tags: [steps, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about steps artifacts"
keywords: [steps, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [steps]
density_score: 0.85
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
Steps is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Steps are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A steps answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` | Sequential execution with defined steps |
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
| agent_invoked | crew.use_steps("data_analysis") | Programmatic call from agent |

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
slash_command: "/review"
phases: [discover, analyze, report]

# Agent-only steps (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_steps('data_analysis')"
phases: [load, transform, analyze, export]

# Event-driven steps
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase steps | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in steps | Mixing concerns | Use agent for identity, steps for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Steps are loaded by agents to extend capabilities
- **F3 INJECT**: Steps can inject domain-specific knowledge
- **F5 CALL**: Steps orchestrate tool usage across phases
- **Handoffs**: Steps can be passed between nuclei for specialized execution
- **Memory**: Steps can persist state between phases via memory_scope

Steps enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Steps
OpenClaude ships ~18 bundled steps as battle-tested implementations:

| Step | Trigger | Pattern | CEX Equivalent |
|------|--------|---------|----------------|
| /simplify | slash_command | 3-parallel-agent review | p04_steps_simplify |
| /verify | slash_command | adversarial verification | p04_steps_verify |
| /compact | agent_invoked | 9-section summarization | p04_steps_compact |
| /loop | slash_command | recurring cron schedule | p04_steps_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Steps are defined as prompt text with frontmatter, not as code. The step body IS the prompt injected when the step triggers. This maps directly to CEX's step-as-artifact model.

**Parallel dispatch pattern** (from /simplify):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any step can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /compact):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Step Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial step | Agent explicitly tries to BREAK the implementation | p04_steps_verify |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_steps_simplify |
| Scratchpad step | <analysis> block for private reasoning, stripped from output | p04_steps_compact |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_steps_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_steps_verify |
