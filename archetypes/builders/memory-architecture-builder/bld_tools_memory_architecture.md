---
kind: tools
id: bld_tools_memory_architecture
pillar: P04
llm_function: CALL
purpose: Tools available for memory_architecture production
quality: 9.0
title: "Tools: memory_architecture-builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, tools]
tldr: "CEX tools for memory_architecture production: compile, score, retriever, doctor, query. External: pgvector, Neo4j, Redis, mem0, Zep."
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_tools_consolidation_policy
  - memory-architecture-builder
  - p03_sp_memory_architecture_builder
  - bld_tools_procedural_memory
  - bld_knowledge_card_memory_architecture
  - bld_collaboration_memory_type
  - bld_instruction_memory_architecture
  - bld_output_template_memory_architecture
  - bld_manifest_memory_type
  - p01_kc_memory_scope
---

## CEX Production Tools

| Tool | Purpose | When |
|------|---------|------|
| `python _tools/cex_compile.py {path}` | Compile .md to .yaml + validate frontmatter | After every write |
| `python _tools/cex_score.py --apply {path}` | Score artifact against quality gate | After compile |
| `python _tools/cex_retriever.py {query}` | Find similar memory_architecture artifacts | Before writing (Template-First) |
| `python _tools/cex_doctor.py` | Health check on builder ISOs | After batch edits |
| `python _tools/cex_query.py memory_architecture` | Discover related kinds and builders | F1 CONSTRAIN |

## External Reference Systems

| System | Type | Purpose in Production |
|--------|------|----------------------|
| pgvector (PostgreSQL) | Vector store | Episodic memory backend (dev/prod) |
| Pinecone / Weaviate | Managed vector store | Episodic + semantic (cloud-only) |
| Neo4j | Graph DB | Semantic memory with entity relationships |
| Redis | KV store | Procedural memory + working memory overflow |
| mem0 SDK | Memory framework | Automated extraction + storage |
| Zep SDK | Memory framework | Temporal knowledge graph backend |
| LangMem | Memory framework | LangGraph-native 4-layer memory |

## Validation Checklist (run before commit)

- [ ] `grep -i "DRAM\|DDR\|SRAM\|CXL\|cache coherence\|nanosecond" {file}` returns nothing
- [ ] `layers` field present and non-empty
- [ ] Commercial Tier Matrix section present in body
- [ ] At least one system cited (MemGPT, Zep, mem0, Cognee, LangMem)
- [ ] `quality: null` in frontmatter

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_consolidation_policy]] | sibling | 0.48 |
| [[memory-architecture-builder]] | downstream | 0.44 |
| [[p03_sp_memory_architecture_builder]] | upstream | 0.41 |
| [[bld_tools_procedural_memory]] | sibling | 0.41 |
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.39 |
| [[bld_collaboration_memory_type]] | downstream | 0.36 |
| [[bld_instruction_memory_architecture]] | upstream | 0.35 |
| [[bld_output_template_memory_architecture]] | downstream | 0.34 |
| [[bld_manifest_memory_type]] | upstream | 0.34 |
| [[p01_kc_memory_scope]] | upstream | 0.32 |
