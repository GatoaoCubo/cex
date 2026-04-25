---
id: p01_ex_memory_persistence
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Dual Persistence: SQLite + Chroma for LLM Agent Memory"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [memory, sqlite, chroma, vector-search, persistence, hybrid-search]
tldr: "SQLite (FTS5) + Chroma (vectors) together provide hybrid search with 10x token savings via 3-layer progressive disclosure"
when_to_use: "Design persistent memory for LLM agents with keyword + local semantic search"
keywords: [sqlite, chroma, fts5, vector-embedding, dual-persistence]
long_tails:
  - "How to combine SQLite and Chroma for LLM agent memory"
  - "What is the difference between contentSessionId and memorySessionId"
axioms:
  - "ALWAYS use contentSessionId for observations (stable)"
  - "NEVER use memorySessionId for FK — it starts NULL"
linked_artifacts:
  primary: p01_kc_memory_session_compression
  related: [p01_kc_memory_worker_service, p01_kc_memory_privacy_controls]
density_score: null
data_source: "https://github.com/thedotmack/claude-mem"
related:
  - p01_kc_memory_session_compression
  - bld_examples_vector_store
  - p10_ax_session_compression
  - bld_collaboration_search_tool
  - retriever-builder
  - search-tool-builder
  - bld_knowledge_card_knowledge_index
  - bld_knowledge_card_search_tool
  - p01_kc_bm25_search
---

## TL;DR

SQLite stores structured data (sessions, observations, summaries) with FTS5 for keyword search. Chroma adds vector embeddings for semantic search. Combined: hybrid search with 3-layer progressive disclosure that reduces token consumption by 10x.

## Core Concept

LLM agent memory requires two types of search: exact keyword (FTS5/SQLite) and semantic similarity (Chroma/vectors). Neither solves it alone. The dual persistence pattern separates structured storage (SQLite) from semantic index (Chroma), connected by a 3-layer MCP workflow: search (IDs, ~50 tokens) -> timeline (context, ~200 tokens) -> get_observations (details, ~1000 tokens).

## Architecture

```
SQLite (~/.claude-mem/claude-mem.db)
  sessions | sdk_sessions | observations (FTS5) | summaries
                    |
                    +--- hybrid search ---+
                    |                     |
              keyword match        semantic similarity
              (FTS5/BM25)          (Chroma embeddings)
                    |                     |
                    +--- 3-layer MCP -----+
              search → timeline → get_observations
```

| Table | Key Fields | Function |
|-------|-----------|----------|
| sdk_sessions | content_session_id, memory_session_id | Session tracking |
| observations | memory_session_id, tool_name, title | Raw data with FTS5 |
| summaries | content_session_id, summary | Compressed narrative |

## Patterns

| Trigger | Action |
|---------|--------|
| Exact search by tool name | FTS5 on tool_name field |
| Search by similar concept | Chroma semantic search |
| Limited context window | 3-layer progressive disclosure |
| New session needs history | Inject summaries + observations |
| Two session IDs available | contentSessionId for FK, memorySessionId for resume |

## Anti-Patterns

- Using only SQLite without Chroma (loses semantic search)
- Using only Chroma without SQLite (loses structured queries)
- Loading all observations at once (blows token budget)
- Using memorySessionId as FK (starts NULL, unstable)
- Ignoring FTS5 and using LIKE queries (10-100x slower)

## References

- source: https://github.com/thedotmack/claude-mem
- related: p01_kc_memory_session_compression
- related: p01_kc_memory_worker_service
- related: p01_kc_memory_privacy_controls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_memory_session_compression]] | sibling | 0.25 |
| [[bld_examples_vector_store]] | downstream | 0.20 |
| [[p10_ax_session_compression]] | downstream | 0.20 |
| [[bld_collaboration_search_tool]] | downstream | 0.19 |
| [[retriever-builder]] | downstream | 0.18 |
| [[search-tool-builder]] | downstream | 0.17 |
| [[bld_knowledge_card_knowledge_index]] | sibling | 0.16 |
| [[bld_knowledge_card_search_tool]] | sibling | 0.15 |
| [[p01_kc_bm25_search]] | sibling | 0.15 |
