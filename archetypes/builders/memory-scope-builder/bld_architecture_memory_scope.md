---
kind: architecture
id: bld_architecture_memory_scope
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of memory_scope — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Memory Scope"
version: "1.0.0"
author: n03_builder
tags: [memory_scope, builder, examples]
tldr: "Golden and anti-examples for memory scope construction, demonstrating ideal structure and common pitfalls."
domain: "memory scope construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - memory-scope-builder
  - p03_sp_memory_scope_builder
  - p01_kc_memory_scope
  - bld_examples_memory_scope
  - p10_lr_memory_scope_builder
  - bld_collaboration_memory_scope
  - bld_instruction_memory_scope
  - bld_output_template_memory_scope
  - bld_collaboration_memory_type
  - bld_tools_memory_scope
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

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_memory_scope
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-memory-scope.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-scope-builder]] | upstream | 0.66 |
| [[p03_sp_memory_scope_builder]] | upstream | 0.61 |
| [[p01_kc_memory_scope]] | upstream | 0.52 |
| [[bld_examples_memory_scope]] | upstream | 0.50 |
| [[p10_lr_memory_scope_builder]] | downstream | 0.48 |
| [[bld_collaboration_memory_scope]] | downstream | 0.45 |
| [[bld_instruction_memory_scope]] | upstream | 0.41 |
| [[bld_output_template_memory_scope]] | upstream | 0.38 |
| [[bld_collaboration_memory_type]] | downstream | 0.37 |
| [[bld_tools_memory_scope]] | upstream | 0.36 |
