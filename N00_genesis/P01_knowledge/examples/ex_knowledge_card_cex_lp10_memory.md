---
id: p01_kc_cex_lp10_memory
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP10 Memory — Working Memory and State for LLM Agents"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp10, memory, runtime-state, knowledge-index, learning-record, session]
tldr: "P10 defines 4 types of operational memory: runtime_state, knowledge_index, learning_record, session_state"
when_to_use: "Understand how LLM agents manage state and memory across sessions"
keywords: [memory, runtime-state, knowledge-index, learning-record, session-state]
long_tails:
  - "How to manage working memory in LLM agents"
  - "What is the difference between knowledge P01 and memory P10 in CEX"
axioms:
  - "ALWAYS distinguish P01 (what it KNOWS) from P10 (what it REMEMBERS)"
  - "NEVER persist session_state beyond the session"
linked_artifacts:
  primary: p01_kc_cex_lp09_config
  related: [p01_kc_cex_lp01_knowledge]
density_score: 1.0
data_source: "https://arxiv.org/abs/2304.03442"
related:
  - p01_kc_cex_function_inject
  - p01_kc_lp10_memory
  - bld_architecture_session_state
  - bld_architecture_runtime_state
  - p01_kc_cex_lp01_knowledge
  - bld_architecture_memory_scope
  - p03_sp_memory_scope_builder
  - memory-scope-builder
  - runtime-state-builder
  - bld_architecture_learning_record
---

## Quick Reference

topic: P10 Memory | scope: agent state management | criticality: high
types: 4 | function: INJECT | layer: runtime + content

## Key Concepts

- P10 is the agent's notebook (operational memory)
- P01 = what I STUDIED (external, validated, persistent)
- P10 = what I EXPERIENCED (internal, accumulated, sessional)
- runtime_state stores decisions and routing across sessions
- knowledge_index configures semantic search (BM25 + FAISS)
- learning_record registers what worked and what failed
- session_state is an ephemeral snapshot (dies with the session)
- LangChain separates Memory (P10) from Document (P01)
- LlamaIndex separates StorageContext (P10) from Node (P01)
- MemGPT demonstrates autonomous memory management
- P10 consumes P01: memory references knowledge
- P10 feeds P03: session context informs prompt
- P10 is governed by P09: retention and cleanup rules
- Dominant function: INJECT (memory injected as context)
- runtime_state max 3072 bytes (persistent across sessions)
- session_state is NOT core (ephemeral, disposable)
- knowledge_index is NOT embedding_config (P01) nor rag_source

## Phases

1. Define which states persist across sessions (runtime)
2. Configure knowledge_index with BM25 + FAISS for search
3. Start learning_record to capture patterns
4. Create session_state for active session snapshot
5. Implement retention rules via P09 (decay, archive)
6. Feed P03 with relevant session context

## Golden Rules

- ALWAYS separate P01 (knowledge) from P10 (memory)
- NEVER treat session_state as persistent (ephemeral)
- ALWAYS register learning_record after critical execution
- NEVER duplicate knowledge (P01) as runtime_state (P10)
- ALWAYS compress memory before context overflow

## Comparativo

| Type | Persistence | Layer | Example |
|------|------------|-------|---------|
| runtime_state | Across sessions | runtime | Routing decisions, counters |
| knowledge_index | Permanent | runtime | BM25 config, FAISS params |
| learning_record | Permanent | content | Success/failure patterns |
| session_state | Ephemeral | runtime | Current task snapshot |

## Flow

```
[P10: Memory Layer]
         |
    +----+----+----+
    |    |    |    |
   rs   bi   lr   ss
    |    |    |    |
    v    v    v    v
 [INJECT into context]
    |         |
    v         v
 persiste   efemero
    |         |
    +----+----+
         |
         v
  [P03 prompt enriched]
         |
         v
  [P01 knowledge referenced]
```

## References

- source: https://arxiv.org/abs/2304.03442
- source: https://arxiv.org/abs/2310.08560
- related: p01_kc_cex_lp09_config
- related: p01_kc_cex_lp01_knowledge


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_inject]] | sibling | 0.38 |
| [[p01_kc_lp10_memory]] | sibling | 0.33 |
| [[bld_architecture_session_state]] | downstream | 0.28 |
| [[bld_architecture_runtime_state]] | downstream | 0.27 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.27 |
| [[bld_architecture_memory_scope]] | downstream | 0.26 |
| [[p03_sp_memory_scope_builder]] | downstream | 0.25 |
| [[memory-scope-builder]] | downstream | 0.24 |
| [[runtime-state-builder]] | downstream | 0.23 |
| [[bld_architecture_learning_record]] | downstream | 0.23 |
