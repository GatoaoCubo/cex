---
id: n06_task
kind: task
type: task
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_task_n06.md + .yaml
core: true
---

# Knowledge Card Artifact Enhancement Guide

## What Is a Knowledge Card
A knowledge card is a structured repository of reusable expertise with defined phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Knowledge cards are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A knowledge card answers "what phases execute to achieve this expertise?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Platform Implementation
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `KnowledgeCard` / `RunnableSequence` | Sequential execution with defined steps |
| LlamaIndex | `KnowledgePipeline` / `IngestionPipeline` | Multi-step workflows with phase management |
| CrewAI | `Task` + `Process` | Task definition with sequential/hierarchical execution |
| DSPy | `dspy.KnowledgeCard.forward()` method | Structured computation with defined phases |
| Haystack | `Pipeline` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `GroupChat` workflow | Multi-agent conversation patterns |
| Microsoft Semantic Kernel | `Plan` / `KernelFunction` | Function orchestration with step management |

## Core Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| trigger_type | enum | "user_invocable" | user_invocable (slash commands) vs agent_only (programmatic) |
| phases | array | required | More phases = granular control vs complexity |
| input_schema | object | {} | Strong typing vs flexibility |
| output_format | string | "markdown" | Structured output vs natural language |
| timeout_seconds | int | 300 | Execution time limit vs complex workflows |

## Lifecycle Phases
| Phase | Purpose | Input | Output |
|-------|---------|-------|--------|
| discover | Context gathering | user_input, environment | context_data |
| configure | Parameter setup | context_data, user_preferences | configuration |
| execute | Main workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |

## Trigger Mechanisms
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/commit", "/deploy" | User types exact command |
| keyword_match | "debug", "optimize" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_knowledge_card("analyze") | Programmatic call from agent |

## Quality Assurance
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate skill |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Scenarios
```yaml
# User-invocable knowledge card (slash command)
trigger_type: user_invocable
slash_command: "/review"
phases: [discover, analyze, report]

# Agent-only knowledge card (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_knowledge_card('data_analysis')"
phases: [load, transform, analyze, export]

# Event-driven knowledge card
trigger_type: event_driven
event_pattern: "file_change:*.py"
phases: [detect, lint, test, notify]
```

## Common Pitfalls
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase knowledge card | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in knowledge card | Mixing concerns | Use agent for identity, knowledge card for expertise |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Strategies
- **F2 BECOME**: Knowledge cards are loaded by agents to extend capabilities
- **F3 INJECT**: Knowledge cards can inject domain-specific knowledge
- **F5 CALL**: Knowledge cards orchestrate tool usage across phases
- **Handoffs**: Knowledge cards can be passed between nuclei for specialized execution
- **Memory**: Knowledge cards can persist state between phases via memory_scope

## Industry Applications
| Company | Use Case | Knowledge Card Type |
|--------|---------|---------------------|
| GitHub | Code review automation | p04_knowledge_card_review |
| Salesforce | Sales process optimization | p04_knowledge_card_sales |
| IBM | Technical documentation | p04_knowledge_card_docs |
| AWS | Cloud infrastructure | p04_knowledge_card_infra |
| Microsoft | DevOps automation | p04_knowledge_card_devops |
| Google | Search engine optimization | p04_knowledge_card_seo |

## Production Reference: OpenClaude Bundled Knowledge Cards
OpenClaude ships ~20 bundled knowledge cards as battle-tested implementations:

| Knowledge Card | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /simplify | slash_command | 3-parallel-agent review | p04_knowledge_card_simplify |
| /verify | slash_command | adversarial verification | p04_knowledge_card_verify |
| /compact | agent_invoked | 9-section summarization | p04_knowledge_card_compact |
| /loop | slash
