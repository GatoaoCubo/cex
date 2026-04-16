---
kind: instruction
id: bld_instruction_memory_architecture
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for memory_architecture
quality: 8.9
title: "Instruction: memory_architecture-builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, instruction]
tldr: "8F production process for LLM agent memory architecture: load schema, define layers, specify backends, map eviction policy, add tier matrix"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Phase 1: RESEARCH

1. Identify the agent type and primary use case (customer support, research, coding, etc.).
2. Determine which memory layers are required: working (always), episodic (if multi-session),
   semantic (if fact-heavy), procedural (if skill-driven).
3. Map the agent's target commercial tier (free/pro/enterprise) against the tier matrix
   in bld_knowledge_card_memory_architecture.md.
4. Review reference architectures: MemGPT/Letta for hierarchical design, Zep for
   temporal graphs, mem0 for selective extraction, Cognee for knowledge graphs.
5. Identify storage constraints: vector DB provider, graph DB availability, KV store limits.
6. Check bld_schema_memory_architecture.md for required frontmatter and body structure.

## Phase 2: COMPOSE

1. Write frontmatter per bld_schema_memory_architecture.md (all required fields, quality: null).
2. Write Overview section: agent type, memory goals, which layers are active and why.
3. Write Memory Layer Definitions table:
   - Columns: Layer | Backend | Retention | Tier Required | Notes
   - Row per active layer with concrete backend (e.g., "pgvector", "Neo4j", "Redis").
4. Write Storage Backends section: one subsection per active layer with backend config.
5. Write Read Pipeline: step-by-step retrieval flow from query to context injection.
6. Write Write Pipeline: step-by-step extraction/classification/storage after generation.
7. Write Eviction Policy: per-layer strategy (LRU, LFU, TTL, importance score).
8. Write Commercial Tier Matrix: FREE vs. PRO vs. ENTERPRISE feature differences.
9. Write Integration Points: cross-reference consolidation_policy and procedural_memory kinds.

## Phase 3: VALIDATE

- [ ] Schema compliance: all required frontmatter fields present, ID matches pattern.
- [ ] Domain accuracy: all content describes LLM agent memory, not hardware memory.
- [ ] Layer completeness: working layer present; other layers justified or excluded.
- [ ] Tier matrix present: FREE/PRO/ENTERPRISE differentiation explicit.
- [ ] Industry references: at least one system cited (MemGPT, Zep, mem0, Cognee, LangMem).
- [ ] Eviction policy specified: no layer left with unbounded retention.
- [ ] quality: null in frontmatter (never self-score).
- [ ] No Unicode characters in body (ASCII only per ascii-code-rule.md).
