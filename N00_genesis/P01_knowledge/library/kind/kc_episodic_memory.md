---
id: p01_kc_episodic_memory
kind: knowledge_card
type: kind
pillar: P10
title: "Episodic Memory -- Deep Knowledge for episodic_memory"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: episodic_memory
quality: 8.8
tags: [episodic_memory, P10, INJECT, kind-kc, agent-memory, interaction-history]
tldr: "episodic_memory stores temporally-indexed past interaction episodes (Tulving 1972) for LLM agent recall. NOT working_memory (current task) or entity_memory (persistent facts)."
when_to_use: "Building, reviewing, or reasoning about episodic_memory artifacts"
keywords: [episodic_memory, interaction_history, agent_memory, tulving, memgpt, zep, autobiographical]
feeds_kinds: [episodic_memory]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
---

# Episodic Memory

## Spec
```yaml
kind: episodic_memory
pillar: P10
llm_function: INJECT
max_bytes: 3072
naming: p10_em_{scope}.md
core: true
```

## What It Is
Episodic memory (Tulving, 1972) stores temporally indexed autobiographical events -- what happened,
when, and in what context. In LLM agents, episodic_memory holds past interaction episodes:
the prompt received, task performed, outcome, and key observations.

NOT working_memory (current task state). NOT entity_memory (persistent entity facts).
NOT prospective_memory (future scheduled actions). NOT knowledge_card (factual domain knowledge).

## Cross-Framework Map
| Framework | Equivalent | Notes |
|-----------|-----------|-------|
| LangChain | ConversationSummaryBufferMemory | Buffers N turns, summarizes older episodes |
| MemGPT (2023) | External archival context | Paged storage + recall API |
| Zep | Temporal memory server | Server-side episode store with NLP extraction |
| LangGraph | Per-thread conversation state | Episode history in graph state |
| Mem0 | Hybrid episodic layer | Combines episode + entity with graph links |

## Key Parameters
| Parameter | Type | Typical | Notes |
|-----------|------|---------|-------|
| owner | string | required | Agent/nucleus that owns this memory |
| scope | string | required | Conversation or task scope |
| retrieval_method | enum | hybrid | recency, relevance, hybrid, temporal |
| max_episodes | int | 50 | Max episodes before eviction |
| summary_threshold | int | 20 | Episodes to retain before summarizing older |
| eviction_policy | enum | lru | lru, oldest_first, relevance_weighted |
| compression | bool | true | Summarize older episodes to save context |

## Episode Schema
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string | YES | Unique episode identifier |
| timestamp | datetime | YES | When it happened |
| agent_id | string | YES | Which agent was involved |
| input_summary | string | YES | Brief summary of input/prompt |
| output_summary | string | YES | Brief summary of response |
| outcome | enum | YES | success, failure, partial |
| key_observations | list | REC | What was learned |
| entities_mentioned | list | REC | Named entities (link to entity_memory) |

## Retrieval Patterns
| Method | Mechanism | Use When |
|--------|-----------|---------|
| Recency | Return most recent N | Conversational continuity |
| Relevance | Embedding similarity | Domain-specific recall |
| Hybrid | Recency + relevance fusion | General-purpose agents |
| Temporal | Same time window prev period | Seasonal or cycle-aware |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| Conversation buffer | Multi-turn chat agent | max_episodes: 20, retrieval: recency |
| Task historian | Agent that learns from past runs | max_episodes: 100, retrieval: relevance |
| Compressed history | Long-running agent | compression: true, summary_threshold: 20 |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No eviction policy | Memory grows unbounded, context overflows | Set max_episodes + eviction_policy |
| Storing facts as episodes | Entity facts decay/change incorrectly | Facts -> entity_memory |
| No compression | Long history exhausts context window | Enable compression |
| Same memory for all agents | Cross-agent contamination | Scope per agent_id |

## Integration Graph
```
interaction (agent run) --> [episodic_memory] <-- retrieval (F3 INJECT)
                                 |
                          entity_memory (extracted entities)
                          working_memory (active task -> episode on complete)
                          knowledge_index (episode vectors)
```
