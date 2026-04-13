---
id: p01_kc_supabase_mcp
kind: knowledge_card
type: platform
pillar: P04
title: "Supabase MCP — Deep Knowledge for platform"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: platform
quality: 9.1
tags: [platform, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about platform artifacts"
keywords: [platform, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [platform]
density_score: 0.92
---

# Supabase MCP

## Spec
```yaml
kind: platform
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_platform_{{name}}.md + .yaml
core: true
```

## What It Is
A platform is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Platforms are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A platform answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

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
| agent_invoked | crew.use_platform("analyze") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate platform |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable platform (slash command)
trigger_type: user_invocable
slash_command: "/deploy"
phases: [discover, analyze, report]

# Agent-only platform (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_platform('data_analysis')"
phases: [load, transform, analyze, export]

# Event-driven platform
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase platform | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in platform | Mixing concerns | Use agent for identity, platform for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Platforms are loaded by agents to extend capabilities
- **F3 INJECT**: Platforms can inject domain-specific knowledge
- **F5 CALL**: Platforms orchestrate tool usage across phases
- **Handoffs**: Platforms can be passed between nuclei for specialized execution
- **Memory**: Platforms can persist state between phases via memory_scope

Platforms enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Platforms
OpenClaude ships ~18 bundled platforms as battle-tested implementations:

| Platform | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /deploy | slash_command | 3-parallel-agent review | p04_platform_deploy |
| /audit | slash_command | adversarial verification | p04_platform_audit |
| /optimize | agent_invoked | 9-section summarization | p04_platform_optimize |
| /schedule | slash_command | recurring cron schedule | p04_platform_schedule (future) |
| /diagnose | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Platforms are defined as prompt text with frontmatter,
not as code. The platform body IS the prompt injected when the platform triggers. This
maps directly to CEX's platform-as-artifact model.

**Parallel dispatch pattern** (from /deploy):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any platform can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /optimize):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Platform Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial platform | Agent explicitly tries to BREAK the implementation | p04_platform_audit |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_platform_deploy |
| Scratchpad platform | <analysis> block for private reasoning, stripped from output | p04_platform_optimize |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_platform_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_platform_audit |
