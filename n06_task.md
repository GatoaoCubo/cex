---
id: p01_kc_memory
kind: knowledge_card
type: kind
pillar: P04
title: "Memory — Deep Knowledge for memory"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: memory
quality: 9.1
tags: [memory, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about memory artifacts"
keywords: [memory, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [memory]
density_score: null
---

# Memory

## Spec
```yaml
kind: memory
pillar: P04
llm_function: TOOL
max_bytes: 4064
naming: p04_memory_{{name}}.md + .yaml
core: true
```

## What It Is
A memory is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Memories are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A memory answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Memory` / `ConversationBufferMemory` | Persistent memory across interactions |
| LlamaIndex | `Memory` / `VectorStoreMemory` | Semantic memory with vector embeddings |
| CrewAI | `Memory` + `Process` | Task-specific memory with hierarchical execution |
| DSPy | `dspy.Memory` | Structured memory with retrieval patterns |
| Haystack | `Memory` with nodes | Explicit memory management in pipelines |
| AutoGen | `Memory` workflow | Multi-agent conversation memory patterns |
| Microsoft Semantic Kernel | `Memory` / `KernelMemory` | Function-aware memory with context |

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
| slash_command | "/recall", "/archive" | User types exact command |
| keyword_match | "remember", "store" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_memory("context") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate memory |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable memory (slash command)
trigger_type: user_invocable
slash_command: "/recall"
phases: [discover, analyze, report]

# Agent-only memory (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_memory('context')"
phases: [load, transform, analyze, export]

# Event-driven memory
trigger_type: event_driven
event_pattern: "file_change:*.md"
phases: [detect, lint, test, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase memory | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in memory | Mixing concerns | Use agent for identity, memory for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Memories are loaded by agents to extend capabilities
- **F3 INJECT**: Memories can inject domain-specific knowledge
- **F5 CALL**: Memories orchestrate tool usage across phases
- **Handoffs**: Memories can be passed between nuclei for specialized execution
- **Memory**: Memories can persist state between phases via memory_scope

## Production Reference: OpenClaude Bundled Memories
OpenClaude ships ~18 bundled memories as battle-tested implementations:

| Memory | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /recall | slash_command | 3-parallel-agent review | p04_memory_recall |
| /archive | slash_command | adversarial verification | p04_memory_archive |
| /context | agent_invoked | 9-section summarization | p04_memory_context |
| /loop | slash_command | recurring cron schedule | p04_memory_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Memories are defined as prompt text with frontmatter,
not as code. The memory body IS the prompt injected when the memory triggers. This
maps directly to CEX's memory-as-artifact model.

**Parallel dispatch pattern** (from /recall):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any memory can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /context):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Memory Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial memory | Agent explicitly tries to BREAK the implementation | p04_memory_archive |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_memory_recall |
| Scratchpad memory | <analysis> block for private reasoning, stripped from output | p04_memory_context |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_memory_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_memory_verify |
```
