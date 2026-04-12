---
id: core_kc
kind: knowledge_card
type: kind
pillar: P01
title: "Core — Fundamental System Knowledge"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: core
quality: 9.1
tags: [core, p01, foundational, kind-kc]
tldr: "System foundation with structured knowledge types, trigger conditions, and lifecycle management for all CEX artifacts"
when_to_use: "Building, reviewing, or reasoning about system foundation artifacts"
keywords: [core, types, trigger, lifecycle, foundation]
feeds_kinds: [skill, task, provider, model, theme, session]
density_score: null
---

# Core

## Spec
```yaml
kind: core
pillar: P01
llm_function: SYSTEM
max_bytes: 8192
naming: p01_core_{{name}}.md + .yaml
core: true
```

## What It Is
The Core is the foundational knowledge system for all CEX artifacts. It defines the structured types, trigger conditions, and lifecycle management that govern how all knowledge cards (skills, tasks, providers, models, themes, sessions) operate within the CEX framework. The Core answers "what fundamental principles govern this system?" while other kinds answer more specific operational questions.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BasePromptTemplate` | System-level template management |
| LlamaIndex | `Document` + `Service` | Knowledge foundation with execution layers |
| CrewAI | `Crew` + `Process` | System-level orchestration framework |
| DSPy | `dspy.Module` | System-level computation architecture |
| Haystack | `DocumentStore` + `Retriever` | Knowledge foundation with retrieval layers |
| AutoGen | `GroupChat` + `Agent` | System-level conversation architecture |
| Microsoft Semantic Kernel | `Kernel` + `Function` | System-level execution framework |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| type | enum | "system" | Core type vs specialized kinds |
| trigger_type | enum | "system" | System-wide triggers vs kind-specific |
| lifecycle | array | ["create", "update", "delete"] | Full lifecycle management vs partial |
| dependencies | array | [] | System-level dependencies vs kind-specific |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "json" | Structured output vs natural language |

## Phase Structure
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| define | System foundation | user_input, environment | system_data |
| validate | Schema verification | system_data, criteria | validated_output |
| execute | Core operation | validated_output, tools | core_result |
| complete | Finalization | core_result | system_result |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| system_command | "/init", "/bootstrap" | System-level commands |
| keyword_match | "create", "update" | Natural language contains keywords |
| event_driven | system_event, time_schedule | System event occurs |
| agent_invoked | crew.use_core("bootstrap") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_type_defined | type in allowed values | Cannot instantiate core |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate system |
| H03_dependencies_resolved | dependencies fully resolved | System errors |
| H04_input_schema | Valid JSON schema format | Runtime parameter errors |
| H05_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# System-level core (bootstrap)
trigger_type: system
slash_command: "/bootstrap"
phases: [define, validate, execute, complete]

# Agent-invoked core (evolution)
trigger_type: agent_invoked
invoke_pattern: "crew.use_core('evolve')"
phases: [define, validate, execute, complete]

# Event-driven core (auto-upgrade)
trigger_type: event_driven
event_pattern: "system_event:upgrade"
phases: [define, validate, execute, complete]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase core | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in core | Mixing concerns | Use agent for identity, core for system |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Core is loaded by all nuclei to define system behavior
- **F3 INJECT**: Core injects system-level knowledge into all artifacts
- **F5 CALL**: Core orchestrates system-wide operations across phases
- **Handoffs**: Core can be passed between nuclei for specialized execution
- **Memory**: Core persists system state between phases via memory_scope

The Core enables modular, reusable system definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Cores
OpenClaude ships ~3 bundled cores as battle-tested implementations:

| Core | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /bootstrap | system_command | 3-phase system initialization | p01_core_bootstrap |
| /evolve | agent_invoked | 9-section system upgrade | p01_core_evolve |
| /audit | event_driven | 12-step system validation | p01_core_audit |

**Key architectural insight**: Cores are defined as system-level prompt text with frontmatter,
not as code. The core body IS the prompt injected when the core triggers. This
maps directly to CEX's core-as-artifact model.

**Parallel execution pattern** (from /bootstrap):
- Phase 1: System scan (dependency check)
- Phase 2: Dispatch 3 agents concurrently, each with the full scan + specialized focus
- Phase 3: Aggregate findings and apply upgrades directly
This pattern generalizes: any core can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /audit):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Core Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial core | Agent explicitly tries to BREAK the implementation | p01_core_audit |
| Parallel execution | Multiple focused agents analyze same system concurrently | p01_core_bootstrap |
| Scratchpad core | <analysis> block for private reasoning, stripped from output | p01_core_audit |
| Background extract | Runs silently after N turns, extracts persistent memories | p01_core_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p01_core_audit |
