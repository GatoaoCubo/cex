---
id: p01_kc_session_state
kind: knowledge_card
type: kind
pillar: P10
title: "Session State — Deep Knowledge for session_state"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: session_state
quality: 9.1
tags: [session_state, P10, INJECT, kind-kc]
tldr: "Ephemeral per-session snapshot of current task, inputs, and intermediate outputs — discarded on session end"
when_to_use: "Building, reviewing, or reasoning about session_state artifacts"
keywords: [ephemeral, snapshot, session]
feeds_kinds: [session_state]
density_score: null
aliases: ["session snapshot", "ephemeral state", "run state", "current session", "in-flight state"]
user_says: ["save current session", "salvar sessao atual", "track session progress", "checkpoint this run", "what step am I on"]
long_tails: ["I need to track the current task and step progress within this session", "save an ephemeral snapshot so I can resume if the agent crashes", "create a session checkpoint with current inputs and intermediate outputs", "track which step I'm on in a multi-step session for crash recovery"]
cross_provider:
  langchain: "BaseChatMessageHistory (in-memory)"
  llamaindex: "ChatEngine session context"
  crewai: "Flow ephemeral state (@start data)"
  dspy: "Module forward() local variables"
  openai: "Thread messages array (single session)"
  anthropic: "messages array within single API call chain"
  haystack: "Pipeline.run() input/output dict"
---

# Session State

## Spec
```yaml
kind: session_state
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_ss_{{session}}.yaml
core: false
```

## What It Is
Session state is an ephemeral YAML snapshot of a single execution session — the current task, active inputs, intermediate outputs, and step progress. It is written at session start, updated during execution, and discarded (or promoted to learning_record if score >= 7.0) at session end. It is NOT runtime_state (which persists across sessions) nor learning_record (which accumulates evidence over time — session_state does not accumulate).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseChatMessageHistory` (in-memory) | In-memory history is session-scoped; cleared on new chat |
| LlamaIndex | `ChatEngine` session context | Session context persists within one chat engine lifecycle |
| CrewAI | `Flow` ephemeral state (`@start` initial data) | Flow state is session-scoped unless explicitly persisted |
| DSPy | Module forward() local variables | Run context exists only within a single .forward() call chain |
| Haystack | `Pipeline.run()` input/output dict | Each run() call is isolated; outputs not automatically persisted |
| OpenAI | Thread messages array (single session) | Thread = one session; create new thread for new session |
| Anthropic | `messages` array within a single API call chain | Messages list is per-invocation; no cross-session persistence |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| session_id | string | uuid | Unique per run; enables audit trail |
| current_task | string | required | Single active task; prevents scope creep |
| step | int | 0 | Track progress; resume from last step on retry |
| outputs | map | {} | Intermediate results; cleared on session end |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Step-indexed progress | Long multi-step tasks with retry risk | `step: 3, total_steps: 8` — resume from step 3 on crash |
| Promote-on-success | Session with score >= 7.0 | On session end: if score >= 7.0 → write learning_record |
| Minimal injection | Only inject fields needed for current step | Load full state but pass only `current_task` + `step` to LLM |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Persisting session_state as runtime_state | Ephemeral data pollutes persistent state; stale tasks accumulate | Promote intentionally at session end; never auto-persist |
| Large outputs stored in session_state | YAML grows beyond 3072 bytes; injection overhead | Store large outputs as separate files; reference by path |
| Sharing session_state across concurrent sessions | Race conditions; fields overwritten by parallel agents | One file per session_id; never share between concurrent runs |

## Integration Graph
```
[handoff] --> [session_state] --> [action_prompt]
                    |
          [learning_record] (on score >= 7.0)
          [discarded] (on score < 7.0)
```

## Decision Tree
- IF session starts THEN create p10_ss_{{session_id}}.yaml with current_task + step=0
- IF session completes with score >= 7.0 THEN promote to learning_record
- IF session ends (any outcome) THEN delete session_state file
- DEFAULT: Never persist session_state across sessions without explicit promotion

## Quality Criteria
- GOOD: Has session_id, current_task, step, timestamp; under 3072 bytes; YAML parseable
- GREAT: Step-indexed progress; output references by path not inline; clear session boundaries
- FAIL: Persisted after session end; mixed with runtime_state; outputs stored inline bloating file
