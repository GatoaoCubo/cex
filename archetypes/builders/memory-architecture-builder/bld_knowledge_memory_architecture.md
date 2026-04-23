---
kind: knowledge_card
id: bld_knowledge_card_memory_architecture
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for memory_architecture production
quality: 9.2
title: "Knowledge Card: memory_architecture Builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, knowledge_card, llm_agent_memory, memgpt, letta]
tldr: "LLM agent memory architecture: hierarchical working/episodic/semantic/procedural layers, MemGPT/Letta pipeline, Zep/mem0/Cognee backends, tier-differentiated PRO/ENTERPRISE features"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.91
related:
  - memory-architecture-builder
  - bld_output_template_memory_architecture
  - p03_sp_memory_architecture_builder
  - p01_kc_memory_scope
  - atom_22_memory_taxonomy
  - consolidation-policy-builder
  - bld_knowledge_card_consolidation_policy
  - bld_knowledge_card_memory_scope
  - bld_collaboration_memory_type
  - bld_instruction_memory_architecture
---

## Domain Overview

Memory architecture in LLM agents defines how systems store, retrieve, and manage
context across sessions. Unlike hardware memory, agent memory is about *information
persistence* -- keeping what matters, forgetting what does not, and surfacing the right
facts at generation time. The field is shaped by MemGPT/Letta (Packer 2023) which
introduced virtual context management with paging between in-context (working) and
external (persistent) memory tiers.

Modern agent memory systems layer four types: working (active context window),
episodic (interaction history), semantic (extracted facts/entities), and procedural
(skills, workflows, tool usage patterns). Production systems combine vector stores,
knowledge graphs, and key-value backends to serve each layer at appropriate latency.

## Key Concepts

| Concept | Definition | Source |
|---------|-----------|--------|
| Virtual Context Management | Paging memory in/out of the fixed LLM context window | MemGPT/Letta (Packer 2023) |
| Working Memory | Active in-context window: system prompt + recent messages | MemGPT architecture |
| Episodic Memory | Interaction history: conversation logs, session summaries | LangMem, Zep |
| Semantic Memory | Extracted facts, entities, relationships in persistent store | mem0, Cognee |
| Procedural Memory | Skills, SOPs, learned workflows stored outside context | Voyager (Wang 2023) |
| Temporal Knowledge Graph | Time-aware graph capturing evolving entity relationships | Zep (2024) |
| Selective Memory Extraction | LLM-driven extraction of facts worth retaining | mem0 (2024) |
| Sleep-Time Consolidation | Offline processing to promote and merge memories | MemGPT consolidation pipeline |
| Memory Hierarchy | Ordered tiers by recency/importance: L1 context -> L2 episodic -> L3 semantic | CEX P10 |
| Context Assembly | Retrieval + ranking + injection of memories into prompt at inference | RAG + reranker |

## Industry References

| System | Architecture | Key Contribution |
|--------|-------------|-----------------|
| MemGPT / Letta (Packer 2023) | Hierarchical: core + archival + recall | First formalized LLM OS with paging |
| Zep (2024) | Temporal knowledge graph | Entity tracking with time-awareness |
| mem0 (2024) | Selective extraction + vector store | Automatic memory from conversation |
| Cognee (2024) | Knowledge graph + ACL | Structured semantic memory with access control |
| LangMem | 4-layer: working/episodic/semantic/procedural | LangGraph-native memory framework |
| OpenAI Memory (2024) | Cross-session fact retention | Selective user-fact storage |
| Claude Projects | Cross-conversation context files | Document-based persistent context |
| A-MEM (2024) | Zettelkasten-inspired interconnected notes | Note-linking for associative retrieval |

## Memory Layer Matrix

| Layer | Storage | Retrieval | Retention | Use Case |
|-------|---------|-----------|-----------|---------|
| Working | In-context | Immediate | Session-only | Active reasoning |
| Episodic | Vector DB | Semantic search | Configurable TTL | Conversation recall |
| Semantic | Graph + KV | Entity lookup | Persistent | Fact/entity queries |
| Procedural | KV / file | Exact match | Persistent | Skill execution |

## Commercial Tier Differentiation

| Feature | Free | PRO | ENTERPRISE |
|---------|------|-----|------------|
| Working memory | Context window only | Extended paging | Multi-agent shared |
| Episodic memory | None | Last 30 sessions | Unlimited + searchable |
| Semantic memory | None | Auto-extraction | Knowledge graph |
| Procedural memory | None | Skill library | Versioned + team-shared |
| Consolidation | None | Basic TTL | Sleep-time + compliance |
| Retention policy | N/A | 90 days | Custom + data residency |

## Common Patterns

1. **Hierarchical paging**: Virtual context management with in/out of context window.
2. **Dual-memory read/write**: Separate pipelines for reading into context vs. writing after generation.
3. **Importance scoring**: Weight memories by recency, frequency, and relevance before eviction.
4. **Async consolidation**: Background jobs promote episodic -> semantic during idle periods.
5. **Multi-modal memory**: Store text + embeddings + structured metadata per memory unit.

## Pitfalls

- Storing everything leads to noise and context bloat at retrieval time.
- Missing temporal metadata makes time-sensitive fact updates impossible.
- No eviction policy causes unbounded storage growth in long-running agents.
- Flat memory (no hierarchy) forces full-scan retrieval, breaking latency budgets.
- Conflating episodic (what happened) with semantic (what is true) creates stale fact errors.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[memory-architecture-builder]] | downstream | 0.59 |
| [[bld_output_template_memory_architecture]] | downstream | 0.51 |
| [[p03_sp_memory_architecture_builder]] | downstream | 0.49 |
| [[p01_kc_memory_scope]] | sibling | 0.47 |
| [[atom_22_memory_taxonomy]] | sibling | 0.45 |
| [[consolidation-policy-builder]] | downstream | 0.45 |
| [[bld_knowledge_card_consolidation_policy]] | sibling | 0.44 |
| [[bld_knowledge_card_memory_scope]] | sibling | 0.39 |
| [[bld_collaboration_memory_type]] | downstream | 0.39 |
| [[bld_instruction_memory_architecture]] | downstream | 0.37 |
