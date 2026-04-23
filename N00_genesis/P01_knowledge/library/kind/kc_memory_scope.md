---
id: p01_kc_memory_scope
kind: knowledge_card
type: kind
pillar: P02
title: "Memory Scope — Deep Knowledge for memory_scope"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: memory_scope
quality: 9.1
tags: [memory_scope, p02, INJECT, kind-kc]
tldr: "Agent memory configuration — defines which memory types, backends, and TTLs an agent uses for persistence across sessions"
when_to_use: "Building, reviewing, or reasoning about memory_scope artifacts"
keywords: [memory, persistence, scope, ttl, session-state]
feeds_kinds: [memory_scope]
density_score: null
aliases: ["memory config", "memory settings", "persistence config", "memory policy", "agent memory definition"]
user_says: ["configure memory", "configurar memoria", "set up persistence", "define what the agent remembers", "how long should it remember"]
long_tails: ["I need to define what this agent remembers and for how long", "configure memory types and TTL policies for my agent", "set up tiered memory with hot session buffer and cold archive", "define which memory backends and expiration policies my agent uses"]
cross_provider:
  langchain: "ConversationBufferMemory / VectorStoreMemory"
  llamaindex: "ChatMemoryBuffer / storage context"
  crewai: "memory=True on Crew (auto-managed)"
  dspy: "n/a (state managed externally)"
  openai: "Assistants thread history (automatic)"
  anthropic: "File-based MEMORY.md system"
  haystack: "ChatMessageStore"
related:
  - memory-scope-builder
  - bld_knowledge_card_memory_scope
  - bld_examples_memory_scope
  - bld_collaboration_memory_type
  - bld_collaboration_memory_scope
  - bld_architecture_memory_scope
  - p10_lr_memory_scope_builder
  - bld_knowledge_card_memory_architecture
  - atom_22_memory_taxonomy
  - memory-architecture-builder
---

# Memory Scope

## Spec
```yaml
kind: memory_scope
pillar: P02
llm_function: INJECT
max_bytes: 2048
naming: p02_memscope.md
core: false
```

## What It Is
A memory_scope defines what memory an agent has access to, how it persists, and when it expires. It specifies memory types (episodic, semantic, procedural), storage backends (files, vector stores, databases), and TTL (time-to-live) policies. It is NOT session_state (P10, which tracks volatile in-session data) nor a knowledge_card (which stores static facts). Memory scope answers "what does this agent remember and for how long?" — session state answers "what is happening right now?"

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `ConversationBufferMemory` / `VectorStoreMemory` | Multiple memory types; pluggable backends |
| LlamaIndex | `ChatMemoryBuffer` / storage context | Memory attached to chat engine or agent |
| CrewAI | `memory=True` on Crew | Short-term, long-term, entity memory auto-managed |
| DSPy | No built-in memory | State managed externally; examples cached |
| Haystack | `ChatMessageStore` | Conversation memory via store interface |
| OpenAI | Assistants thread history | Automatic conversation memory per thread |
| Anthropic | No native memory | organization implements via file-based MEMORY.md system |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| memory_types | list | [episodic] | More types = richer recall but higher storage/token cost |
| backend | enum | file | Vector store = semantic search; file = simple; DB = scalable |
| ttl | duration | session | Longer TTL = more context but stale memories accumulate |
| max_entries | int | 100 | Higher = more recall but slower retrieval and token cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Session-only memory | Stateless tasks, no continuity needed | Chat assistant with conversation buffer, cleared on exit |
| Persistent file memory | Cross-session learning, single user | organization MEMORY.md — user prefs, feedback, project state |
| Vector-backed memory | Large memory pool, semantic search needed | FAISS index of past interactions for similar-case retrieval |
| Tiered memory | Balance cost and recall | Hot (session buffer) → warm (file) → cold (vector archive) |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Unlimited memory without TTL | Token cost grows unbounded; stale memories mislead | Set TTL; consolidate old memories periodically |
| Memorizing everything | Low-value memories dilute high-value ones | Filter: only save surprising, non-obvious, reusable facts |
| No memory consolidation | Duplicates accumulate; retrieval quality drops | Periodic dedup + merge of related memories |

## Integration Graph
```
[agent, boot_config] --> [memory_scope] --> [session_state (P10), knowledge_index (P10)]
                              |
                       [knowledge_card, context_doc]
```

## Decision Tree
- IF task is stateless (no cross-session needs) THEN session buffer only
- IF single user needs cross-session learning THEN file-based persistent memory
- IF large-scale memory with semantic search THEN vector-backed memory
- IF tracking volatile in-session data THEN session_state (P10), not memory_scope
- DEFAULT: file-based persistent memory with monthly consolidation

## Quality Criteria
- GOOD: Memory types specified; backend defined; TTL set; max_entries bounded
- GREAT: Consolidation strategy defined; tested memory retrieval quality; tiered storage with clear promotion rules
- FAIL: No TTL (unbounded growth); memorizes everything; no backend specified; confused with session_state

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-scope-builder]] | related | 0.51 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.51 |
| [[bld_examples_memory_scope]] | downstream | 0.49 |
| [[bld_collaboration_memory_type]] | downstream | 0.47 |
| [[bld_collaboration_memory_scope]] | downstream | 0.45 |
| [[bld_architecture_memory_scope]] | downstream | 0.43 |
| [[p10_lr_memory_scope_builder]] | downstream | 0.42 |
| [[bld_knowledge_card_memory_architecture]] | sibling | 0.41 |
| [[atom_22_memory_taxonomy]] | sibling | 0.40 |
| [[memory-architecture-builder]] | downstream | 0.40 |
