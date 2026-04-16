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
