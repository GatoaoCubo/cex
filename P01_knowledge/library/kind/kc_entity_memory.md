---
id: p01_kc_entity_memory
kind: knowledge_card
type: kind
pillar: P10
title: "Entity Memory — Deep Knowledge for entity_memory"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: entity_memory
quality: 9.1
tags: [entity_memory, P10, INJECT, kind-kc]
tldr: "entity_memory stores current atomic facts about a named entity (project, system, person) with confidence scores, source attribution, and TTL — representing present state, not event history."
when_to_use: "Building, reviewing, or reasoning about entity_memory artifacts"
keywords: [entity_facts, knowledge_graph, working_memory]
feeds_kinds: [entity_memory]
density_score: null
aliases: ["entity store", "fact store", "knowledge graph entry", "entity facts", "named entity memory"]
user_says: ["remember this entity", "lembrar essa entidade", "store facts about this project", "save what we know about X", "track this entity"]
long_tails: ["I need to store current facts about a project so the AI remembers next session", "track what we know about this customer with confidence scores", "create a persistent fact store for named entities like people and systems", "remember key attributes about this project across sessions"]
cross_provider:
  langchain: "ConversationEntityMemory"
  llamaindex: "AgentWorkflow state dict"
  crewai: "Memory (entity scope)"
  dspy: "History type (implicit)"
  openai: "Thread messages + file_search"
  anthropic: "cache_control ephemeral"
  haystack: "n/a (custom via DocumentStore)"
---

# Entity Memory

## Spec
```yaml
kind: entity_memory
pillar: P10
llm_function: INJECT
max_bytes: 2048
naming: p10_entity.md
core: true
```

## What It Is
An entity_memory stores current atomic facts about a named entity — a project, system, person, or resource — each fact carrying confidence and source. It represents present state (what is true now), NOT a history log (what happened over time), NOT a learning_record (which tracks agent performance patterns across sessions).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ConversationEntityMemory` | Extracts and stores entity facts from conversation |
| LlamaIndex | `AgentWorkflow` state dict | Entities stored in workflow state between steps |
| CrewAI | `Memory` (entity scope) | Structured entity facts in CrewAI Memory system |
| DSPy | `History` type | Conversation history can encode entity state implicitly |
| Haystack | N/A | No native entity memory; custom via DocumentStore |
| OpenAI | `Thread` messages + `file_search` | Entity facts surfaced via file_search on persistent Thread |
| Anthropic | `cache_control` ephemeral | Entity context cached with `cache_control` for session |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| entity_type | string | required | project/system/person — drives fact schema |
| facts | list[Fact] | required | {attribute, value, confidence, source} — max 10 |
| updated | ISO date | required | Last refresh — stale without this |
| ttl_days | int | 30 | Lower = fresher; null = permanent (use for stable arch facts) |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Project entity | Current state of ongoing project | `organization-core: {api_version: v2, tests: 273, phase: 3}` |
| System entity | Technical facts about infrastructure | `railway: {region: us-east, pg: v17, ssl: required}` |
| Person entity | Facts about collaborators | `user: {expertise: python, timezone: BRT, pref: terse}` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Entity as event log | Appending events instead of updating facts bloats memory | Entity memory = current state only; use learning_record for history |
| No TTL | Stale facts accumulate and actively mislead agents | Always set `ttl_days` or mark stable facts explicitly |
| Fact overload | >20 facts per entity = unmanageable, high noise | Keep top 10 most decision-relevant facts; prune on update |

## Integration Graph
```
rag_source, context_doc --> [entity_memory] --> knowledge_index, agent_card
                                    |
                               chunk_strategy, retriever_config, learning_record
```

## Decision Tree
- IF fact changes frequently (daily) THEN `ttl_days: 7`
- IF fact is architectural/structural THEN `ttl_days: 90` or null
- IF fact is personal preference THEN user entity, `confidence: high`
- DEFAULT: project entity, `ttl_days: 30`, top 10 facts, source attributed

## Quality Criteria
- GOOD: entity_type, facts list, updated timestamp, ttl_days all present
- GREAT: confidence scores per fact, source attribution, update trigger defined
- FAIL: entity used as event log, no TTL, >20 facts, missing updated timestamp
