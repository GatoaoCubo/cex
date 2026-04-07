---
kind: architecture
id: bld_architecture_memory_scope
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of memory_scope — inventory, dependencies, and architectural position
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| memory_types | List of memory kinds used (episodic, semantic, procedural) | memory_scope | required |
| backend | Storage engine (file, sqlite, redis, faiss) | memory_scope | required |
| ttl | Time-to-live per memory entry | memory_scope | required |
| scope | Isolation boundary (agent, session, global) | memory_scope | optional |
| eviction_policy | What happens when memory is full (LRU, FIFO, score) | memory_scope | optional |
| session_state | Runtime state that feeds into memory | P10 | upstream |
| learning_record | Patterns extracted from memory | P10 | downstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| memory_types | memory_scope | produces | List of memory kinds used (episodic, semantic, procedural) |
| backend | memory_scope | produces | Storage engine (file, sqlite, redis, faiss) |
| ttl | memory_scope | produces | Time-to-live per memory entry |
| scope | memory_scope | produces | Isolation boundary (agent, session, global) |
| eviction_policy | memory_scope | produces | What happens when memory is full (LRU, FIFO, score) |
| session_state | P10 | depends | Runtime state that feeds into memory |
| learning_record | P10 | depends | Patterns extracted from memory |
## Boundary Table
| memory_scope IS | memory_scope IS NOT |
|-------------|----------------|
| Memory scope config — which memory types an agent uses, backends, TTL, and isolation boundaries | session_state (P10 |
| Not session_state | session_state (P10 |
| Not runtime state) | runtime state) |
| Not knowledge_index | knowledge_index (P10 |
| Not search index) | search index) |
| Not learning_record | learning_record (P10 |
| Not pattern storage) | pattern storage) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | memory_types, backend, ttl | Define the artifact's core parameters |
| optional | scope, eviction_policy | Extend with recommended fields |
| external | session_state, learning_record | Upstream/downstream connections |
