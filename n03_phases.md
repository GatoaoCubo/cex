---
id: n03_phases_terminology_sweep
kind: phases
type: improvement
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_phases_terminology_sweep.md + .yaml
core: true
version: 1.0.0
created: 2026-04-08
updated: 2026-04-08
author: builder_knowledge
domain: terminology_sweep
quality: 9.1
tags: [phases, p04, reusable, kind-phases]
tldr: "Structured phase refinement with trigger conditions, lifecycle management, and cross-industry alignment for repeatable terminology organization"
when_to_use: "Building, reviewing, or reasoning about phase artifacts"
keywords: [phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [phases]
density_score: 8.8
---

# Phases

## Spec
```yaml
kind: phases
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_phases_{{name}}.md + .yaml
core: true
```

## What It Is
Phases are structured workflow segments with defined trigger conditions, lifecycle management, and cross-industry alignment. They define a specific sequence of operations for organizing terminology across domains. Phases are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A phase answers "what sequence of operations achieves this terminology organization?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Industry Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| ISO 21001 | Quality management system | Standardized phase frameworks |
| IEEE 12207 | Software engineering | Phase lifecycle management |
| NIST SP 800-128 | Information security | Phase standardization practices |
| OSHA 300 | Occupational safety | Phase consistency protocols |
| IEC 61850 | Power systems | Phase interoperability standards |
| ISO 8601 | Date and time | Phase formatting conventions |
| ISO 11179 | Metadata registries | Phase management frameworks |

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
| slash_command | "/phase", "/sequence" | User types exact command |
| keyword_match | "define", "clarify" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_phase("ontology") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate phase |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Industry References
| Standard | Description | Application |
|---------|-------------|------------|
| ISO 21001 | Quality management system | Phase governance frameworks |
| IEEE 12207 | Software engineering | Phase lifecycle management |
| NIST SP 800-128 | Information security | Phase standardization practices |
| OSHA 300 | Occupational safety | Phase consistency protocols |
| IEC 61850 | Power systems | Phase interoperability standards |
| ISO 8601 | Date and time | Phase formatting conventions |
| ISO 11179 | Metadata registries | Phase management frameworks |

## Practical Examples
```yaml
# User-invocable phase (slash command)
trigger_type: user_invocable
slash_command: "/sequence"
phases: [discover, analyze, standardize]

# Agent-only phase (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_phase('ontology')"
phases: [load, map, refine, export]

# Event-driven phase
trigger_type: event_driven
event_pattern: "file_change:*.md"
phases: [detect, audit, standardize, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase phase | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in phase | Mixing concerns | Use agent for identity, phase for terminology organization |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Phases are loaded by agents to extend terminology organization capabilities
- **F3 INJECT**: Phases can inject domain-specific terminology
- **F5 CALL**: Phases orchestrate tool usage across phases
- **Handoffs**: Phases can be passed between nuclei for specialized execution
- **Memory**: Phases can persist state between phases via memory_scope

Phases enable modular, reusable terminology organization that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Phases
OpenClaude ships ~18 bundled phases as battle-tested implementations:

| Phase | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /sequence | slash_command | 3-parallel-agent review | p04_phase_sequence |
| /standardize | slash_command | adversarial verification | p04_phase_standardize |
| /compact | agent_invoked | 9-section summarization | p04_phase_compact |
| /loop | slash
```