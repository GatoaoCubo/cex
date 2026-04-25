---
kind: tools
id: bld_tools_query_optimizer
pillar: P04
llm_function: CALL
purpose: Tools available for query_optimizer production
quality: null
title: "Query Optimizer Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, tools]
tldr: "Tool registry for query optimizer builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for query rewriting, expansion, and multi-hop decomposition rules for rag retrieval."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_query_optimizer
---

# Tools: query-optimizer-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 | ACTIVE |
| cex_retriever.py | Find similar optimizers | Phase 1 | ACTIVE |
| cex_doctor.py | Health check | Phase 3 | ACTIVE |
| cex_query.py | TF-IDF builder discovery | Phase 1 | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions |
| LlamaIndex docs | docs.llamaindex.ai | Query engine patterns |
| HyDE paper | arxiv.org/abs/2212.10496 | Hypothetical Document Embeddings |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| DENIED | (none) | -- |

## CEX Pipeline Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | query optimizer construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
