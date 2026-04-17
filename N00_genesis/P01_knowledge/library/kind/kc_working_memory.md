---
id: p01_kc_working_memory
kind: knowledge_card
type: kind
pillar: P10
title: "Working Memory -- Deep Knowledge for working_memory"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: working_memory
quality: null
tags: [working_memory, P10, INJECT, kind-kc, agent-memory, task-state]
tldr: "working_memory holds active task state in typed slots with capacity limits and task-scoped expiry. NOT episodic (past) or entity (persistent facts)."
when_to_use: "Building, reviewing, or reasoning about working_memory artifacts"
keywords: [working_memory, task_state, context_slots, agent_memory, ephemeral, baddeley]
feeds_kinds: [working_memory]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
---

# Working Memory

## Spec
```yaml
kind: working_memory
pillar: P10
llm_function: INJECT
max_bytes: 2048
naming: p10_wm_{task_scope}.md
core: true
```

## What It Is
Working memory (cognitive origin: Baddeley & Hitch, 1974) holds short-term, limited-capacity state
for an agent's active task execution. It stores intermediate results, retry counts, current step,
and accumulated context that the task needs during execution but does not need to persist afterward.

NOT episodic_memory (past interaction history). NOT entity_memory (persistent facts about entities).
NOT session_state (full session context). NOT prospective_memory (future scheduled actions).

## Cross-Framework Map
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| LangChain | ConversationBufferWindowMemory | Buffer window = capacity_limit |
| LangGraph | AgentState dict | context_slots per node |
| DSPy | Typed Predict state | Typed context_slots |
| AutoGPT | Scratch memory | working_memory + expiry: on_complete |
| MemGPT | In-context scratchpad | Main context window subset |

## Key Parameters
| Parameter | Type | Typical | Notes |
|-----------|------|---------|-------|
| task_id | string | required | Binds memory to a specific task instance |
| owner | string | required | Agent/nucleus that owns this memory |
| context_slots | map[string, typed_value] | required | Named slots for task state |
| capacity_limit | int | 10 | Max active slots; evict oldest on overflow |
| expiry | enum | on_complete | on_complete, ttl_minutes, manual |
| initial_state | map | {} | Pre-loaded state at task start |

## Slot Types
| State Type | Slot Type | Example |
|-----------|-----------|---------|
| Current step | string | "step": "extract_entities" |
| Retry counter | int | "retry_count": 2 |
| Intermediate results | list | "results": ["item1"] |
| Confidence score | float | "avg_confidence": 0.87 |
| Completion flag | bool | "is_complete": false |
| Complex data | json | "parsed_output": {...} |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| Step tracking | Multi-step task | string slot "current_step" |
| Error accumulation | Retry with backoff | int slot "error_count" + threshold |
| Buffer window | Conversation continuation | list slot "last_n_turns" + capacity_limit |
| Confidence tracking | Quality-gated output | float slot "min_confidence" + threshold |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No task_id | Multiple tasks share memory state | Always bind to task_id |
| expiry: never | Memory leaks accumulate across tasks | Use on_complete for task-scoped memory |
| Slots without types | Type errors corrupt task logic | Declare type for each slot |
| Storing past interactions | Mixes working with episodic memory | Past episodes -> episodic_memory |

## Integration Graph
```
task_definition --> [working_memory] --> agent (reads during execution)
                          |
                   episodic_memory (completed task logged)
                   entity_memory (entities extracted stored)
                   session_state (session-level context)
```

## Decision Tree
- IF state needed only during task execution -> working_memory (expiry: on_complete)
- IF state spans multiple sessions -> entity_memory or episodic_memory
- IF state is agent persona/capabilities -> agent_card, NOT working_memory
- IF state tracks future actions -> prospective_memory, NOT working_memory
