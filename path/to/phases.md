---
id: phases_kc
kind: knowledge_card
type: kind
pillar: P01
title: "Phases — Structured Execution Lifecycle"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: phases
quality: 9.1
tags: [phases, p01, lifecycle, kind-kc]
tldr: "Standardized execution lifecycle with structured phases, trigger conditions, and state management for all CEX artifacts"
when_to_use: "Building, reviewing, or reasoning about lifecycle artifacts"
keywords: [phases, lifecycle, trigger, state, execution]
feeds_kinds: [skill, task, provider, model, theme, session]
density_score: null
---

# Phases

## Spec
```yaml
kind: phases
pillar: P01
llm_function: SYSTEM
max_bytes: 8192
naming: p01_phases_{{name}}.md + .yaml
core: true
```

## What It Is
Phases define the standardized execution lifecycle for all CEX artifacts. They provide a structured framework for managing the state transitions and operational flow of any knowledge card (skills, tasks, providers, models, themes, sessions) within the CEX system. Phases answer "what standardized lifecycle governs this execution?" while other kinds define more specific operational details.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableSequence` | Standardized execution lifecycle |
| LlamaIndex | `Pipeline` | Phased execution with state management |
| CrewAI | `Process` | Standardized workflow lifecycle |
| DSPy | `dspy.Module` | Phased computation architecture |
| Haystack | `Pipeline` with nodes | Standardized execution flow |
| AutoGen | `GroupChat` + `Agent` | Phased conversation architecture |
| Microsoft Semantic Kernel | `Kernel` + `Function` | Standardized execution framework |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| type | enum | "lifecycle" | Phases type vs specialized kinds |
| trigger_type | enum | "system" | System-wide triggers vs kind-specific |
| lifecycle | array | ["create", "update", "delete"] | Full lifecycle management vs partial |
| dependencies | array | [] | System-level dependencies vs kind-specific |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| define | Lifecycle foundation | user_input, environment | lifecycle_data |
| validate | Schema verification | lifecycle_data, criteria | validated_output |
| execute | Core operation | validated_output, tools | phase_result |
| complete | Finalization | phase_result | lifecycle_result |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| system_command | "/init", "/bootstrap" | System-level commands |
| keyword_match | "create", "update" | Natural language contains keywords |
| event_driven | system_event, time_schedule | System event occurs |
| agent_invoked | crew.use_phases("bootstrap") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_type_defined | type in allowed values | Cannot instantiate phases |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate system |
| H03_dependencies_resolved | dependencies fully resolved | System errors |
| H04_input_schema | Valid JSON schema format | Runtime parameter errors |
| H05_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# System-level phases (bootstrap)
trigger_type: system
slash_command: "/bootstrap"
phases: [define, validate, execute, complete]

# Agent-invoked phases (evolution)
trigger_type: agent_invoked
invoke_pattern: "crew.use_phases('evolve')"
phases: [define, validate, execute, complete]

# Event-driven phases (auto-upgrade)
trigger_type: event_driven
event_pattern: "system_event:upgrade"
phases: [define, validate, execute, complete]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase phases | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in phases | Mixing concerns | Use agent for identity, phases for system |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Phases are loaded by all nuclei to define execution flow
- **F3 INJECT**: Phases inject lifecycle management into all artifacts
- **F5 CALL**: Phases orchestrate system-wide operations across phases
- **Handoffs**: Phases can be passed between nuclei for specialized execution
- **Memory**: Phases persist execution state between phases via memory_scope

The Phases enable modular, reusable lifecycle definition that bridges the
gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Phases
OpenClaude ships ~3 bundled phases as battle-tested implementations:

| Phases | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /bootstrap | system_command | 3-phase system initialization | p01_phases_bootstrap |
| /evolve | agent_invoked | 9-section system upgrade | p01_phases_evolve |
| /audit | event_driven | 12-step system validation | p01_phases_audit |

**Key architectural insight**: Phases are defined as system-level prompt text with frontmatter,
not as code. The phases body IS the prompt injected when the phases trigger. This
maps directly to CEX's phases-as-artifact model.

**Parallel execution pattern** (from /bootstrap):
- Phase 1: System scan (dependency check)
- Phase 2: Dispatch 3 agents concurrently, each with the full scan + specialized focus
- Phase 3: Aggregate findings and apply upgrades directly
This pattern generalizes: any phases can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /audit):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Phases Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial phases | Agent explicitly tries to BREAK the implementation | p01_phases_audit |
| Parallel execution | Multiple focused agents analyze same system concurrently | p01_phases_bootstrap |
| Scratchpad phases | <analysis> block for private reasoning, stripped from output | p01_phases_audit |
| Background extract | Runs silently after N turns, extracts persistent memories | p01_phases_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p01_phases_audit |
