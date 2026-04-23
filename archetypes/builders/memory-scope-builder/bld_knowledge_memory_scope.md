---
kind: knowledge_card
id: bld_knowledge_card_memory_scope
pillar: P02
llm_function: INJECT
purpose: Domain knowledge for memory_scope production
sources: CrewAI memory architecture, Mem0 long-term memory, Mastra agent memory, conversation memory patterns, episodic vs semantic memory research
quality: 9.0
title: "Knowledge Card Memory Scope"
version: "1.0.0"
author: n03_builder
tags: [memory_scope, builder, examples]
tldr: "Golden and anti-examples for memory scope construction, demonstrating ideal structure and common pitfalls."
domain: "memory scope construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_memory_scope_builder
  - p01_kc_memory_scope
  - memory-scope-builder
  - bld_examples_memory_scope
  - bld_collaboration_memory_scope
  - bld_collaboration_memory_type
  - p03_sp_memory_scope_builder
  - memory-architecture-builder
  - atom_22_memory_taxonomy
  - bld_knowledge_card_memory_architecture
---

# Domain Knowledge: memory_scope
## Executive Summary
Memory scope config — which memory types an agent uses, backends, TTL, and isolation boundaries. Produced as P02 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P02 |
| llm_function | INJECT |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Ephemeral | In-memory buffer cleared on session end | Short conversations, stateless tools |
| Session-scoped | Persists within session, cleared on restart | Multi-turn conversations, task context |
| Long-term | Persists across sessions with TTL | User preferences, learned patterns, facts |
| Shared | Accessible by multiple agents with ACL | Team knowledge, cross-agent context |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No TTL | Memory grows unbounded, stale facts pollute context |
| No scope isolation | Agent A reads Agent B's private memory, causing confusion |
| Storing raw conversations | Token waste; store distilled facts, not transcripts |
| No eviction policy | Full memory store silently drops new entries or crashes |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p02_memscope_[a-z][a-z0-9_]+$`
## References
- CrewAI MemoryScope, Mastra memory, Mem0, LangChain ConversationBufferMemory, LlamaIndex ChatMemoryBuffer
- CrewAI memory architecture, Mem0 long-term memory, Mastra agent memory, conversation memory patterns, episodic vs semantic memory research

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_memory_scope_builder]] | downstream | 0.59 |
| [[p01_kc_memory_scope]] | sibling | 0.52 |
| [[memory-scope-builder]] | related | 0.49 |
| [[bld_examples_memory_scope]] | downstream | 0.45 |
| [[bld_collaboration_memory_scope]] | downstream | 0.43 |
| [[bld_collaboration_memory_type]] | downstream | 0.43 |
| [[p03_sp_memory_scope_builder]] | related | 0.38 |
| [[memory-architecture-builder]] | downstream | 0.37 |
| [[atom_22_memory_taxonomy]] | sibling | 0.35 |
| [[bld_knowledge_card_memory_architecture]] | sibling | 0.35 |
