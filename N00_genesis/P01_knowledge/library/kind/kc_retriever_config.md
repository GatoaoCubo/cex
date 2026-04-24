---
id: p01_kc_retriever_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "Retriever Configuration — Deep Knowledge for retriever configuration"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: retriever_config
quality: 9.1
tags: [retriever_config, p04, reusable, kind-kc]
tldr: "Reusable configuration framework with structured phases, trigger conditions, and lifecycle management for repeatable retrieval workflows"
when_to_use: "Building, reviewing, or reasoning about retriever configuration artifacts"
keywords: [retriever_config, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [retriever_config]
density_score: null
related:
  - p01_kc_hook
  - p01_kc_steps
  - p01_kc_server_tools
  - p01_kc_supabase_mcp
  - p01_kc_skill
  - retriever-config-builder
  - skill-builder
  - bld_knowledge_card_skill
  - bld_collaboration_retriever_config
  - p11_qg_skill
---

# Retriever Configuration

## Spec
```yaml
kind: retriever_config
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_retriever_config_{{name}}.md + .yaml
core: true
```

## What It Is
A retriever configuration is a reusable framework for defining structured retrieval workflows with trigger conditions and lifecycle management. It defines a specific pattern for how information should be retrieved and processed across different contexts. Retriever configurations are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A retriever configuration answers "what phases execute to achieve this retrieval pattern?" while agents answer "who am I?" and prompts answer "how do I communicate?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RetrievalChain` / `VectorStoreRetriever` | Structured retrieval with defined phases |
| LlamaIndex | `Retriever` / `VectorStoreIndex` | Multi-step retrieval workflows with phase management |
| CrewAI | `RetrievalTask` + `Process` | Task definition with sequential/hierarchical retrieval execution |
| DSPy | `dspy.Retrieve` method | Structured computation with defined retrieval phases |
| Haystack | `Retriever` with nodes | Explicit DAG execution with phase transitions |
| AutoGen | `RetrievalAgent` workflow | Multi-agent retrieval patterns |
| Microsoft Semantic Kernel | `RetrievalPlan` / `KernelFunction` | Function orchestration with step management |

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
| execute | Main retrieval workflow | configuration, tools | raw_results |
| validate | Quality assurance | raw_results, criteria | validated_output |

## Trigger Patterns
| Trigger Type | Example | Activation |
|--------------|---------|------------|
| slash_command | "/retrieve", "/query" | User types exact command |
| keyword_match | "search", "find" | Natural language contains keywords |
| event_driven | file_change, time_schedule | System event occurs |
| agent_invoked | crew.use_retriever("search") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate retriever |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable retriever (slash command)
trigger_type: user_invocable
slash_command: "/retrieve"
phases: [discover, query, format]

# Agent-only retriever (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_retriever('search')"
phases: [load, parse, query, export]

# Event-driven retriever
trigger_type: event_driven
event_pattern: "file_change:*.md"
phases: [detect, parse, query, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase retriever | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in retriever | Mixing concerns | Use agent for identity, retriever for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Retriever configurations are loaded by agents to extend retrieval capabilities
- **F3 INJECT**: Retriever configurations can inject domain-specific knowledge
- **F5 CALL**: Retriever configurations orchestrate tool usage across phases
- **Handoffs**: Retriever configurations can be passed between nuclei for specialized execution
- **Memory**: Retriever configurations can persist state between phases via memory_scope

Retriever configurations enable modular, reusable retrieval pattern definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Retriever Configurations
OpenClaude ships ~18 bundled retriever configurations as battle-tested implementations:

| Retriever | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /search | slash_command | 3-parallel-agent review | p04_retriever_search |
| /query | slash_command | adversarial verification | p04_retriever_query |
| /fetch | agent_invoked | 9-section summarization | p03_retriever_fetch |
| /loop | slash_command | recurring cron schedule | p04_retriever_loop (future) |
| /stuck | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Retriever configurations are defined as prompt text with frontmatter,
not as code. The retriever configuration body IS the prompt injected when the retriever triggers. This
maps directly to CEX's retriever configuration-as-artifact model.

**Parallel dispatch pattern** (from /search):
- Phase 1: Identify changes (git diff)
- Phase 2: Dispatch 3 agents concurrently, each with the full diff + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any retriever configuration can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /fetch):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Retriever Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial retriever | Agent explicitly tries to BREAK the implementation | p04_retriever_query |
| Parallel review | Multiple focused agents analyze same diff concurrently | p04_retriever_search |
| Scratchpad retriever | <analysis> block for private reasoning, stripped from output | p03_retriever_fetch |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_retriever_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_retriever_query |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_hook]] | sibling | 0.60 |
| [[p01_kc_steps]] | sibling | 0.59 |
| [[p01_kc_server_tools]] | sibling | 0.58 |
| [[p01_kc_supabase_mcp]] | sibling | 0.53 |
| [[p01_kc_skill]] | sibling | 0.48 |
| [[retriever-config-builder]] | upstream | 0.31 |
| [[skill-builder]] | related | 0.31 |
| [[bld_knowledge_card_skill]] | sibling | 0.31 |
| [[bld_collaboration_retriever_config]] | downstream | 0.28 |
| [[p11_qg_skill]] | downstream | 0.27 |
