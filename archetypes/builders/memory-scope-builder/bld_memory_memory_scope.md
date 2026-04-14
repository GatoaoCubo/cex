---
id: p10_lr_memory_scope_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "memory_scope artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from CrewAI MemoryScope, Mastra memory, Mem0, LangChain ConversationBufferMemory, LlamaIndex ChatMemoryBuffer documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: memory_scope
tags: [memory-scope, P02, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [memory scope, ephemeral, session-scoped, long-term, shared]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Memory Scope"
density_score: 0.90
llm_function: INJECT
---
## Summary
Memory scope config — which memory types an agent uses, backends, TTL, and isolation boundaries. The difference between a useful memory_scope and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Memory Types, Backend Config, Lifecycle.
Body budget: 2048 bytes max.
## Anti-Pattern
1. No TTL: Memory grows unbounded, stale facts pollute context
2. No scope isolation: Agent A reads Agent B's private memory, causing confusion
3. Storing raw conversations: Token waste; store distilled facts, not transcripts
4. No eviction policy: Full memory store silently drops new entries or crashes
## Context
The 2048-byte body limit keeps memory_scope artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_memory_scope_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-memory-scope-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | memory_scope |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
