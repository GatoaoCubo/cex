---
id: p01_kc_runtime_state
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P10
title: "Runtime State — Deep Knowledge for runtime_state"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: runtime_state
quality: 9.1
tags: [runtime_state, P10, INJECT, kind-kc]
tldr: "Accumulated variable state built during execution that persists between sessions — routing decisions, active task queue, counters"
when_to_use: "Building, reviewing, or reasoning about runtime_state artifacts"
keywords: [state, routing, persistence]
feeds_kinds: [runtime_state]
density_score: null
aliases: ["persistent state", "agent state", "runtime variables", "accumulated state", "cross-session state"]
user_says: ["save runtime state", "salvar estado do agente", "persist agent decisions", "keep track of routing", "store counters across sessions"]
long_tails: ["I need to persist routing decisions and counters across agent sessions", "store accumulated state that survives between runs", "track the agent's task queue and progress across multiple sessions", "save mutable state like retry counts and routing choices persistently"]
cross_provider:
  langchain: "RunnableConfig metadata + custom persistence"
  llamaindex: "AgentWorkflow state dict (ctx.data)"
  crewai: "Flow state object (@start/@listen)"
  dspy: "dspy.settings + module instance variables"
  openai: "Thread metadata dict"
  anthropic: "Custom YAML injected into system prompt"
  haystack: "Pipeline metadata + component state"
related:
  - bld_memory_runtime_state
  - runtime-state-builder
  - bld_architecture_runtime_state
  - bld_collaboration_session_state
  - p01_kc_session_state
  - bld_knowledge_card_runtime_state
  - session-state-builder
  - bld_architecture_session_state
  - p03_ins_runtime_state
  - p03_sp_session_state_builder
---

# Runtime State

## Spec
```yaml
kind: runtime_state
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_rs_{{agent}}.yaml
core: true
```

## What It Is
Runtime state is the mutable YAML accumulator for an agent's in-flight decisions, routing choices, counters, and task queue that builds up during execution and persists across sessions. It reflects what the agent is currently doing and has decided, not who it is. It is NOT mental_model (P02 — fixed identity, never mutated at runtime) nor session_state (ephemeral — discarded at session end; runtime_state survives).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `RunnableConfig` metadata + custom persistence | Config carries run-scoped state; persist between runs via external store |
| LlamaIndex | `AgentWorkflow` state dict | `ctx.data` in Workflow persists across steps within a run |
| CrewAI | `Flow` state object | `@start`/`@listen` methods read/write Flow state; persisted in YAML |
| DSPy | `dspy.settings` + module instance variables | Module-level state persists within program lifecycle |
| Haystack | Pipeline metadata + component state | No native cross-run state; use external YAML file |
| OpenAI | Thread metadata dict | Thread-level metadata carries routing decisions across messages |
| Anthropic | Custom YAML injected into system prompt | State read from file at session start, written at session end |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| agent | string | required | One file per agent; prevents state collision |
| task_queue | list | [] | Longer queue = more context injected; trim completed tasks |
| routing_decisions | map | {} | Capture keyword → agent_group mappings made this run |
| counters | map | {} | Track attempt counts, retry limits, batch progress |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Checkpoint-before-write | Before mutating state, write checkpoint | `cp p10_rs_atlas.yaml p10_rs_atlas.bak.yaml` |
| Queue-drain pattern | Clear completed items after commit | `task_queue: [pending_items_only]` after each batch |
| Merge-on-conflict | Two agent_groups write same state file | Read → merge → write; use timestamp as tiebreaker |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Storing identity in runtime state | mental_model becomes mutable; routing breaks | Keep identity in P02 mental_model; only decisions/counters in runtime_state |
| Never clearing completed tasks | State grows unbounded; context overflow | Drain queue on commit; archive completed items |
| Injecting full runtime_state into every prompt | Token waste; irrelevant fields injected | Selective injection: only fields relevant to current task |

## Integration Graph
```
[mental_model] --> [runtime_state] --> [action_prompt]
[session_state] ----^         |
                         [checkpoint]
```

## Decision Tree
- IF agent is stateless one-shot THEN skip runtime_state (use session_state only)
- IF agent runs multiple sessions THEN write p10_rs_{{agent}}.yaml at end of each session
- IF state file >3072 bytes THEN archive old entries, trim to active task queue only
- DEFAULT: One runtime_state file per agent; inject at session start; write at session end

## Quality Criteria
- GOOD: Has agent name, task_queue, routing_decisions, counters; under 3072 bytes; YAML parseable
- GREAT: Checkpoint backup present; completed tasks drained; only active fields injected
- FAIL: Mixes agent identity with runtime data; unbounded growth; >3072 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_runtime_state]] | related | 0.43 |
| [[runtime-state-builder]] | related | 0.42 |
| [[bld_architecture_runtime_state]] | upstream | 0.39 |
| [[bld_collaboration_session_state]] | related | 0.39 |
| [[p01_kc_session_state]] | sibling | 0.38 |
| [[bld_knowledge_card_runtime_state]] | sibling | 0.35 |
| [[session-state-builder]] | related | 0.35 |
| [[bld_architecture_session_state]] | upstream | 0.34 |
| [[p03_ins_runtime_state]] | related | 0.34 |
| [[p03_sp_session_state_builder]] | upstream | 0.34 |
