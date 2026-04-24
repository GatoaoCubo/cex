---
id: p01_kc_server_tools
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "Server Tools — Deep Knowledge for server tools"
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: builder_knowledge
domain: server_tools
quality: 9.1
tags: [server_tools, p04, reusable, kind-kc]
tldr: "Reusable capability with structured phases, triggers, and lifecycle management for repeatable workflows"
when_to_use: "Building, reviewing, or reasoning about server tools artifacts"
keywords: [server_tools, phases, trigger, reusable, capability, workflow, lifecycle]
feeds_kinds: [server_tools]
density_score: null
related:
  - p01_kc_hook
  - p01_kc_steps
  - p01_kc_supabase_mcp
  - p01_kc_skill
  - p01_kc_retriever_config
  - skill-builder
  - bld_knowledge_card_skill
  - p01_kc_workflow
  - p03_ins_skill_builder
  - p11_qg_skill
---

# Server Tools

## Spec
```yaml
kind: server_tools
pillar: P04
llm_function: TOOL
max_bytes: 4096
naming: p04_server_tools_{{name}}.md + .yaml
core: true
```

## What It Is
A server tool is a reusable capability with structured phases, trigger conditions, and lifecycle management. It defines a specific workflow that can be executed repeatedly across different contexts. Server tools are NOT agents (P02, which define identity/persona) nor system_prompts (P03, which define communication style). A server tool answers "what phases execute to achieve this capability?" while agents answer "who am I?" and prompts answer "how do I communicate?"

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
| agent_invoked | crew.use_tool("analyze") | Programmatic call from agent |

## Quality Gates
| Gate | Validation | Failure Impact |
|------|------------|----------------|
| H01_phases_defined | phases array not empty | Cannot execute workflow |
| H02_trigger_valid | trigger_type in allowed values | Cannot activate tool |
| H03_input_schema | Valid JSON schema format | Runtime parameter errors |
| H04_output_format | Defined output structure | Unpredictable results |

## Usage Examples
```yaml
# User-invocable tool (slash command)
trigger_type: user_invocable
slash_command: "/monitor"
phases: [discover, analyze, report]

# Agent-only tool (programmatic)
trigger_type: agent_only
invoke_pattern: "crew.use_tool('backup')"
phases: [load, transform, analyze, export]

# Event-driven tool
trigger_type: event_driven
event_pattern: "file_change:*.log"
phases: [detect, parse, analyze, notify]
```

## Anti-Patterns
| Anti-Pattern | Why Wrong | Correct Approach |
|--------------|-----------|------------------|
| Single-phase tool | Not reusable, just a function | Use action_prompt for one-off tasks |
| No trigger definition | Cannot be activated | Define clear trigger conditions |
| Agent identity in tool | Mixing concerns | Use agent for identity, tool for capability |
| Hard-coded parameters | Not reusable | Use input_schema for parameterization |

## Integration Points
- **F2 BECOME**: Tools are loaded by agents to extend capabilities
- **F3 INJECT**: Tools can inject domain-specific knowledge
- **F5 CALL**: Tools orchestrate tool usage across phases
- **Handoffs**: Tools can be passed between nuclei for specialized execution
- **Memory**: Tools can persist state between phases via memory_scope

Server tools enable modular, reusable workflow definition that bridges the gap between simple prompts and complex multi-agent systems.
## Production Reference: OpenClaude Bundled Server Tools
OpenClaude ships ~18 bundled server tools as battle-tested implementations:

| Tool | Trigger | Pattern | CEX Equivalent |
|-------|---------|---------|----------------|
| /monitor | slash_command | 3-parallel-agent review | p04_server_tools_monitor |
| /backup | slash_command | adversarial verification | p04_server_tools_backup |
| /audit | agent_invoked | 9-section summarization | p04_server_tools_audit |
| /schedule | slash_command | recurring cron schedule | p04_server_tools_schedule (future) |
| /diagnose | slash_command | diagnostic investigation | n/a (Anthropic-specific) |

**Key architectural insight**: Tools are defined as prompt text with frontmatter,
not as code. The tool body IS the prompt injected when the tool triggers. This
maps directly to CEX's tool-as-artifact model.

**Parallel dispatch pattern** (from /monitor):
- Phase 1: Identify changes (system logs)
- Phase 2: Dispatch 3 agents concurrently, each with the full log + specialized focus
- Phase 3: Aggregate findings and fix issues directly
This pattern generalizes: any tool can dispatch parallel sub-agents with typed foci.

**Analysis scratchpad pattern** (from /audit):
- <analysis> tags create a private drafting space
- Forces structured thinking before output
- Scratchpad is stripped from final result
- Improves quality without consuming permanent context

## New Tool Patterns Discovered
| Pattern | Description | Example |
|---------|-------------|---------|
| Adversarial tool | Agent explicitly tries to BREAK the implementation | p04_server_tools_backup |
| Parallel review | Multiple focused agents analyze same log concurrently | p04_server_tools_monitor |
| Scratchpad tool | <analysis> block for private reasoning, stripped from output | p04_server_tools_audit |
| Background extract | Runs silently after N turns, extracts persistent memories | p04_server_tools_memory_extract |
| Rationalization counter | Lists excuses the agent will generate, pre-emptively counters | p04_server_tools_backup |
```

core

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_hook]] | sibling | 0.70 |
| [[p01_kc_steps]] | sibling | 0.68 |
| [[p01_kc_supabase_mcp]] | sibling | 0.62 |
| [[p01_kc_skill]] | sibling | 0.56 |
| [[p01_kc_retriever_config]] | sibling | 0.56 |
| [[skill-builder]] | related | 0.36 |
| [[bld_knowledge_card_skill]] | sibling | 0.34 |
| [[p01_kc_workflow]] | sibling | 0.32 |
| [[p03_ins_skill_builder]] | upstream | 0.30 |
| [[p11_qg_skill]] | downstream | 0.29 |
