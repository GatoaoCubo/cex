---
id: p10_rs_conversation
kind: runtime_state
pillar: P10
title: "Runtime State: Conversation Context Manager"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
agent: "conversation-manager"
persistence: "session"
domain: "conversation"
quality: 9.1
tags: [runtime-state, conversation, context, session]
tldr: "Session-scoped runtime state for conversation context: turn tracking, topic detection, memory promotion, and context window budget."
routing_mode: "rule_based"
priority_count: 4
update_frequency: "per_task"
fallback_agent: "gateway-agent"
density_score: 1.0
constraint_count: 3
linked_artifacts:
  primary: "mental-model-builder"
  related: [session-state-builder, context-doc-builder]
related:
  - ex_context_session_memory
  - bld_memory_session_state
  - bld_knowledge_card_memory_benchmark
  - p01_kc_memory_scope
  - p01_kc_memory_persistence
  - p01_kc_session_backend
  - bld_knowledge_card_memory_architecture
  - bld_knowledge_card_memory_scope
  - kc_model_context_protocol
  - p01_kc_entity_memory
---
## Agent Context
Conversation context manager tracks per-session state for multi-turn interactions. Maintains turn history, active topic, accumulated facts, and context window budget. State is session-scoped — destroyed on session end, with key facts promoted to persistent memory before teardown.
## Routing Rules
| Rule | Condition | Action | Confidence |
|------|-----------|--------|------------|
| topic_switch | user intent diverges from active_topic | update active_topic, archive previous context | 0.85 |
| memory_promote | fact repeated 3+ times or user says "remember" | write to persistent memory file | 0.95 |
| budget_exceeded | token_count > 80% of context_window | trigger compaction: summarize oldest turns | 0.99 |
| fallback_route | confidence < 0.5 on all routing rules | escalate to gateway-agent for re-routing | 1.00 |
## Decision Tree
```text
new_user_message
  ├── same_topic (intent matches active_topic) -> append to turn history
  ├── new_topic (intent diverges) -> archive context, switch active_topic
  ├── memory_request ("remember X") -> promote to persistent memory
  └── ambiguous (confidence < 0.5) -> ask clarifying question
```
## Priorities
1. **Context budget** — never exceed context window; compact proactively at 80%
2. **Turn coherence** — maintain topic thread; don't lose context on topic switch
3. **Memory promotion** — persist valuable facts before session teardown
4. **Latency** — state updates must complete in < 100ms to avoid blocking response
## Heuristics
| Heuristic | When | Confidence |
|-----------|------|------------|
| 3-turn topic stability | Same topic for 3+ turns = committed topic | 0.90 |
| Recency bias | Last 5 turns weighted 3x vs older turns in relevance | 0.85 |
| Explicit > implicit | User-stated facts override inferred facts | 0.95 |
## Constraints
1. Session state must not exceed 50KB serialized — enforce via compaction
2. Never persist PII to memory without explicit user consent
3. Context compaction must preserve all user-stated facts (explicit memory requests)
## State Transitions
| Trigger | From | To | Condition |
|---------|------|----|-----------|
| session_start | idle | active | user sends first message |
| topic_switch | active | active | intent divergence detected |
| budget_exceeded | active | compacting | token_count > 80% window |
| compaction_done | compacting | active | summary replaces old turns |
| session_end | active | teardown | user closes or timeout |
| teardown_done | teardown | idle | promoted facts saved |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ex_context_session_memory]] | upstream | 0.34 |
| [[bld_memory_session_state]] | related | 0.28 |
| [[bld_knowledge_card_memory_benchmark]] | upstream | 0.27 |
| [[p01_kc_memory_scope]] | upstream | 0.25 |
| [[p01_kc_memory_persistence]] | upstream | 0.25 |
| [[p01_kc_session_backend]] | related | 0.25 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.24 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.24 |
| [[kc_model_context_protocol]] | upstream | 0.24 |
| [[p01_kc_entity_memory]] | related | 0.24 |
