---
kind: knowledge_card
id: bld_knowledge_card_episodic_memory
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for episodic_memory production
sources: Tulving (1972) episodic memory theory, MemGPT (Packer et al. 2023), Zep memory, LangChain ConversationSummaryBufferMemory
quality: 8.4
title: "Knowledge Card Episodic Memory"
version: "1.0.0"
author: n03_builder
tags: [episodic_memory, builder, knowledge_card]
tldr: "Episodic memory stores temporally-indexed past interaction episodes for LLM agents, enabling autobiographical recall grounded in Tulving (1972)."
domain: "episodic memory construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_knowledge_card_memory_architecture
  - atom_22_memory_taxonomy
  - bld_output_template_memory_architecture
  - memory-architecture-builder
  - bld_knowledge_card_entity_memory
  - p01_kc_memory_scope
  - bld_knowledge_card_consolidation_policy
  - p03_sp_memory_architecture_builder
  - bld_knowledge_card_memory_scope
  - p01_kc_memory_persistence
---

# Domain Knowledge: episodic_memory

## Executive Summary
Episodic memory (Tulving, 1972) stores temporally indexed autobiographical events -- what happened, when, and in what context. In LLM agent systems, episodic memory holds past interaction episodes: the conversation context, task performed, outcome, and key observations. Agents retrieve relevant past episodes to inject context and avoid repeating mistakes.

## Cognitive Science Foundation
| Tulving's Memory Types | CEX P10 Equivalent |
|-----------------------|--------------------|
| Episodic (what happened) | episodic_memory |
| Semantic (facts, concepts) | entity_memory, knowledge_card |
| Procedural (skills, how-to) | skill, instruction |

## LLM Implementation Patterns
| Pattern | Framework | Notes |
|---------|-----------|-------|
| ConversationSummaryBufferMemory | LangChain | Buffers N turns, summarizes older episodes |
| MemGPT external context | MemGPT (2023) | Manages main + archival context with paging |
| Zep temporal memory | Zep | Server-side episode store with NLP extraction |
| LangGraph conversation state | LangGraph | Per-thread episode history in graph state |
| Mem0 memory layer | Mem0 | Hybrid entity + episodic with graph links |

## Retrieval Methods
| Method | Mechanism | When to Use |
|--------|-----------|-------------|
| Recency | Return most recent N episodes | Conversational continuity |
| Relevance | Embedding similarity search | Domain-specific context recall |
| Hybrid | Recency + relevance score fusion | General-purpose agents |
| Temporal | Episodes from similar time window | Seasonal or cycle-aware tasks |

## Episode Schema Best Practices
| Field | Type | Why Required |
|-------|------|-------------|
| timestamp | datetime | Temporal indexing -- the core of episodic memory |
| context | string | What was happening when this episode occurred |
| task | string | What the agent was doing |
| outcome | string | What happened / result |
| retrieval_keys | list[string] | Enable future retrieval by topic/entity |
| confidence | float | Reliability of the stored episode |

## Decay Policy Options
| Policy | Mechanism | Use Case |
|--------|-----------|----------|
| Time decay | Episodes expire after N days | General agents |
| Count limit | Prune oldest when count > max | Fixed-size stores |
| Relevance decay | Remove episodes never retrieved | Dense knowledge domains |
| Hybrid | Time + relevance combined | Production agents |

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No timestamp field | Cannot do temporal retrieval or decay |
| Unlimited episode_count | Retrieval latency grows unbounded |
| No decay policy | Stale episodes corrupt context |
| Mixing entity facts with episodes | Entity facts are timeless; episodes are temporal |
| No retrieval keys | Full semantic scan required for every query |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_memory_architecture]] | sibling | 0.43 |
| [[atom_22_memory_taxonomy]] | sibling | 0.37 |
| [[bld_output_template_memory_architecture]] | downstream | 0.29 |
| [[memory-architecture-builder]] | downstream | 0.28 |
| [[bld_knowledge_card_entity_memory]] | sibling | 0.27 |
| [[p01_kc_memory_scope]] | sibling | 0.26 |
| [[bld_knowledge_card_consolidation_policy]] | sibling | 0.25 |
| [[p03_sp_memory_architecture_builder]] | downstream | 0.25 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.25 |
| [[p01_kc_memory_persistence]] | sibling | 0.25 |
