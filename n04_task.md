---
id: p01_kc_boot_config
kind: knowledge_card
type: kind
pillar: P01
title: "Boot Config — Deep Knowledge for boot config"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: boot_config
quality: 9.1
tags: [boot_config, p01, reusable, kind-kc]
tldr: "Reusable configuration template with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about boot config artifacts"
keywords: [boot_config, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [boot_config]
density_score: null
---

# Boot Config

## Spec
```yaml
kind: boot_config
pillar: P01
llm_function: TOOL
max_bytes: 4096
naming: p01_boot_config_{{name}}.md + .yaml
core: true
```

## What It Is
A boot config is a reusable configuration template with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Boot configs are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A boot config answers "what phases execute to achieve this configuration?" while agents answer "who am I?" and prompts answer "how do I communicate?"

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
# User-invocable boot config (slash command)
trigger_type: user_invocable
slash_command: "/configure"
phases: [discover, analyze, deploy]

# Agent-only boot config (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_boot_config('setup')"
phases: [load, validate, apply, export]

# Event-driven boot config
trigger_type: event_driven
event_pattern: "file_change:*.yml"
phases: [detect, validate, apply, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase boot config | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in boot config | Mixing concerns | Use agent for identity, boot config for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Boot configs are loaded by agents to extend capabilities
- **F3 INJECT**: Boot configs can inject domain-specific knowledge
- **F5 CALL**: Boot configs orchestrate tool usage across phases
- **Handoffs**: Boot configs can be passed between nuclei for specialized execution
- **Memory**: Boot configs can persist state between phases via memory_scope

Boot configs enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Boot Configs
OpenClaude ships ~18 bundled boot configs as battle-tested implementations:

| Boot Config | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /setup | slash_command | 3-parallel-agent review | p01_boot_config_setup |
| /validate | slash_command | adversarial verification | p01_boot_config_validate |
| /deploy | agent_invoked | 9-section summarization | p01_boot_config_deploy |
| /loop | slash_command | recurring cron schedule | p01_boot_config_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Boot configs are defined as prompt text with frontmatter,
not as code. The boot config body IS the prompt injected when the boot config triggers. This
maps directly to CEX's boot config-as-artifact model.

**Parallel dispatch pattern** (from /setup):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any boot config can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /deploy):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Boot Config Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial boot config | Agent explicitly tries to BREAK the implementation | p01_boot_config_validate |
| Parallel review | Multiple focused agents analyze same diff concurrently | p01_boot_config_setup |
| Scratchpad boot config | <analysis> block for private reasoning, stripped from output | p01_boot_config_deploy |
| Background extract | Runs silently after N turns, extracts persistent memories | p01_boot_config_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p01_boot_config_validate |
