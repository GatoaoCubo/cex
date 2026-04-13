---
id: n06_task
kind: task
type: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: n06_task.md
core: true
---

# Improve LLM Agent Frameworks Comparison Artifact

## Overview of LLM Agent Frameworks
LLM agent frameworks provide structured methodologies for building autonomous systems. This document compares leading frameworks across key dimensions:

| Framework | Core Focus | Best For | Complexity |
|----------|-----------|----------|------------|
| LangChain | Sequential execution | Chatbots, data pipelines | Medium |
| LlamaIndex | Document understanding | RAG systems, knowledge bases | High |
| CrewAI | Task orchestration | Multi-agent systems | High |
| DSPy | Structured computation | NLP pipelines | Medium |
| Haystack | Pipeline architecture | Search engines | High |
| AutoGen | Multi-agent conversations | Customer support | Medium |
| Semantic Kernel | Function orchestration | Enterprise apps | High |

## Framework Comparison Table
| Feature | LangChain | LlamaIndex | CrewAI | DSPy | Haystack | AutoGen | Semantic Kernel |
|--------|----------|-----------|-------|-----|---------|--------|----------------|
| Sequential Execution | ✅ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Multi-Step Workflows | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Task Definition | ✅ | ❌ | ✅ | ❌ | ❌ | ✅ | ❌ |
| DAG Execution | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| Memory Management | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Plugin Support | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Community | Large | Medium | Medium | Small | Medium | Medium | Small |

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

## Production Reference: OpenClaude Bundled Cores
OpenClaude ships ~20 bundled cores as battle-tested implementations:

| Core | Trigger | Pattern | CEX Equivalent |
|------|--------|---------|----------------|
| /optimize | slash_command | 3-parallel-agent review | p04_core_optimize |
| /benchmark | slash
```