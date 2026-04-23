# P10 Memory — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| Mem0 | Memory layer | User memory, agent memory, organization memory, memory types (episodic, semantic, procedural), memory search, memory update, memory decay, graph memory |
| Zep | Long-term memory | Memory enrichment, fact extraction, temporal awareness, entity extraction, session memory, perpetual memory, relevance scoring, memory summaries |
| Letta (MemGPT) | Memory management | Core memory (persona + human), archival memory (unlimited, searchable), recall memory (conversation search), memory editing, memory hierarchy, inner thoughts |
| LangGraph Persistence | State persistence | Checkpoints, threads, cross-thread memory (Store), state snapshots, namespace/key storage, checkpoint metadata, resume/replay |
| LangChain Memory Types | Conversation memory | ConversationBufferMemory, ConversationSummaryMemory, ConversationSummaryBufferMemory, EntityMemory, VectorStoreMemory, ConversationTokenBufferMemory |
| Motif | Interaction patterns | Activity tracking, interaction sequences, behavioral patterns, session analysis |
| Redis | Cache/state store | Key-value store, TTL-based expiry, pub/sub, sorted sets (for rankings), hash maps (structured state), streams (append-only log) |
| Conversation Window Mgmt | Token optimization | Sliding window, token budgets, summarization-on-overflow, compression, priority-based retention, context truncation strategies |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Session/Conversation State | LangChain (BufferMemory), LangGraph (thread checkpoints), Letta (recall memory), Redis (session store), Zep (session memory) | Ephemeral state for current conversation, discarded or archived after session ends | 5 |
| Long-term / Persistent Memory | Mem0 (user/agent memory), Zep (perpetual memory), Letta (archival memory), LangGraph (Store cross-thread), LangChain (VectorStoreMemory) | Persists across sessions. Accumulated knowledge about users, entities, preferences | 5 |
| Memory Summary / Compression | LangChain (SummaryMemory, SummaryBufferMemory), Letta (archival compression), Zep (memory summaries), Conversation Window Mgmt (summarize-on-overflow) | Condensing older memories into summaries to fit context windows while retaining key information | 4 |
| Entity Memory | LangChain (EntityMemory), Zep (entity extraction), Mem0 (graph memory entities), Letta (core memory persona/human) | Tracking specific entities (people, tools, concepts) and their attributes across conversations | 4 |
| Semantic Search over Memory | Mem0 (memory search), Zep (relevance scoring), LangChain (VectorStoreMemory), Letta (archival search), LangGraph (Store with embeddings) | Vector-based retrieval of relevant memories given a query | 5 |
| Learning Record / Fact | Mem0 (episodic memory), Zep (fact extraction), Letta (archival memory entries) | Discrete learned facts or experiences stored for future reference | 3 |
| Memory Decay / TTL | Mem0 (memory decay), Redis (TTL), Zep (temporal awareness), Conversation Window Mgmt (priority retention) | Time-based or usage-based degradation of memory relevance | 4 |
| Runtime State | LangGraph (state checkpoints), Redis (key-value state), Motif (activity tracking) | Mutable state accumulated during execution (routing decisions, counters, flags) | 3 |
| Memory Index / Search Config | Mem0 (search config), LangChain (VectorStoreMemory retriever config), Zep (relevance scoring params) | Configuration for how memories are indexed and retrieved (embedding model, similarity threshold, top_k) | 3 |
| Memory Hierarchy | Letta (core > recall > archival), Mem0 (short-term > long-term), LangChain (buffer > summary > vector), Conversation Window Mgmt (priority tiers) | Tiered memory system where different levels trade off access speed for capacity | 4 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| runtime_state | Runtime State | 80% | Good match to LangGraph checkpoints and Redis state. Gap: industry runtime state includes checkpoint versioning (LangGraph thread_ts) for replay/rollback. CEX is current-snapshot only. |
| knowledge_index | Memory Index / Semantic Search | 85% | Strong match. CEX knowledge_index (BM25 + FAISS) aligns with Mem0/Zep/LangChain vector search. Gap: industry indexes support multi-modal (text + image embeddings) and cross-namespace search. |
| learning_record | Learning Record / Fact | 80% | Good match to Mem0 episodic memory and Zep fact extraction. Gap: industry learning records carry confidence scores and temporal decay (Mem0 decay, Zep temporal awareness). CEX records are static. |
| session_state | Session/Conversation State | 85% | Excellent match. Maps directly to LangChain BufferMemory, LangGraph thread state, Redis sessions. Gap: industry session state supports multiple serialization formats and checkpoint branching. |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| memory_summary | Every major memory framework implements summarization/compression as a distinct operation. When context windows fill up, older memories are condensed into summaries. Distinct from learning_record (records specific facts/outcomes) and session_state (ephemeral snapshot). A memory_summary is a compressed representation of many interactions. | LangChain (SummaryMemory, SummaryBufferMemory), Letta (archival compression), Zep (memory summaries), Conversation Window Mgmt (summarize-on-overflow) | high |
| entity_memory | Tracking entities (users, tools, concepts) and their evolving attributes is a first-class concept across frameworks. Distinct from learning_record (captures what happened) and knowledge_index (search infrastructure). Entity memory answers "what do I know about X?" with structured, updateable facts. | LangChain (EntityMemory), Zep (entity extraction), Mem0 (graph memory entities), Letta (core memory persona/human blocks) | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| learning_record | KEEP (add decay metadata) | Industry strongly favors temporal decay and confidence scoring on learned facts (Mem0 decay, Zep temporal awareness). Consider adding optional `confidence` and `last_accessed` fields to schema. |
| session_state | KEEP (clarify ephemerality) | Well-scoped. Boundary should emphasize: session_state is NEVER promoted to long-term storage. For persistent cross-session data, use learning_record or entity_memory. |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| runtime_state | LangGraph checkpoints, Redis key-value state, Motif activity tracking, Letta inner-thought state |
| knowledge_index | Mem0 memory search config, LangChain VectorStoreMemory retriever, Zep relevance scoring, FAISS/BM25 hybrid |
| learning_record | Mem0 episodic memory, Zep fact extraction, Letta archival memory entries |
| session_state | LangChain ConversationBufferMemory, LangGraph thread state, Redis session store, Zep session memory |

## 7. Summary
Current: 4 kinds → Proposed: 6 kinds (+memory_summary, +entity_memory) | Coverage: ~82% → ~92%

Key insight: The memory landscape universally implements a **tiered hierarchy** (session → summary → long-term → archival) where **summarization** is an explicit transformation step, not just a byproduct. CEX currently has session_state (tier 1) and learning_record (tier 3) but lacks the compression layer between them. Adding memory_summary fills this gap. Entity memory is the other universal pattern — every framework from LangChain to Mem0 to Zep treats "what do I know about entity X?" as a distinct query type requiring structured, updateable storage separate from general learning records.
