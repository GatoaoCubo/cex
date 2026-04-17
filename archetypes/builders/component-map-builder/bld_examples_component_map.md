---
pillar: P00
id: bld_examples_component_map
kind: examples
parent: component-map-builder
version: 1.0.0
quality: 9.1
title: "Examples Component Map"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# Examples — component-map-builder
## Golden Example
INPUT: "Map the CEX brain infrastructure components and connections"
OUTPUT (complete, 19+ fields):
```yaml
id: p08_cmap_brain_infrastructure
kind: component_map
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "infrastructure"
quality: null
tags: [component-map, brain, infrastructure, search, knowledge]
tldr: "Structured inventory of Brain search infrastructure: BM25, FAISS, Ollama, and 1957 pool artifacts"
scope: "CEX Brain search infrastructure — indexing, embedding, retrieval"
component_count: 6
connection_count: 8
components:
  - {name: "BM25 Index", role: "keyword search", owner: "knowledge-engine", status: "active"}
  - {name: "FAISS Index", role: "vector similarity search", owner: "knowledge-engine", status: "active"}
  - {name: "Ollama", role: "local embedding generation", owner: "system", status: "active"}
  - {name: "Pool", role: "artifact storage (1957 items)", owner: "system", status: "active"}
  - {name: "brain_query API", role: "hybrid search endpoint", owner: "knowledge-engine", status: "active"}
  - {name: "build_indexes_ollama.py", role: "index rebuilder", owner: "knowledge-engine", status: "active"}
connections:
  - {from: "Pool", to: "build_indexes_ollama.py", type: "data_flow"}
  - {from: "build_indexes_ollama.py", to: "BM25 Index", type: "produces"}
  - {from: "build_indexes_ollama.py", to: "FAISS Index", type: "produces"}
  - {from: "Ollama", to: "build_indexes_ollama.py", type: "dependency"}
  - {from: "brain_query API", to: "BM25 Index", type: "data_flow"}
  - {from: "brain_query API", to: "FAISS Index", type: "data_flow"}
  - {from: "agent_groups", to: "brain_query API", type: "data_flow"}
  - {from: "Ollama", to: "brain_query API", type: "dependency"}
keywords: [brain, search, bm25, faiss, ollama, knowledge, retrieval]
## Scope
CEX Brain search infrastructure: all components involved in indexing, embedding, and retrieving knowledge artifacts. Excludes individual artifact content, agent_group internals, and API deployment.
## Components
| Component | Role | Owner | Status | Version |
|-----------|------|-------|--------|---------|
| BM25 Index | Keyword search (lexical) | knowledge-engine | active | - |
| FAISS Index | Vector similarity (semantic) | knowledge-engine | active | 140MB gitignored |
| Ollama | Local embedding (nomic-embed-text) | system | active | auto-start |
| Pool | Artifact storage | system | active | 1957 items |
| brain_query API | Hybrid search endpoint | knowledge-engine | active | ~88% accuracy |
| build_indexes_ollama.py | Index rebuilder | knowledge-engine | active | ~20 min full rebuild |
## Connections
| From | To | Type | Data | Direction |
|------|-----|------|------|-----------|
| Pool | build_indexes_ollama.py | data_flow | raw artifacts | unidirectional |
| build_indexes_ollama.py | BM25 Index | produces | keyword index | unidirectional |
| build_indexes_ollama.py | FAISS Index | produces | vector index | unidirectional |
| Ollama | build_indexes_ollama.py | dependency | embeddings | unidirectional |
| brain_query API | BM25 Index | data_flow | keyword results | unidirectional |
| brain_query API | FAISS Index | data_flow | vector results | unidirectional |
| agent_groups | brain_query API | data_flow | search queries | unidirectional |
| Ollama | brain_query API | dependency | runtime embeddings | unidirectional |
## Interfaces
| Boundary | Components | Contract | Status |
|----------|-----------|----------|--------|
| Search API | brain_query <-> agent_groups | MCP tool call, returns ranked results | active |
| Embedding | Ollama <-> indexer/API | nomic-embed-text model, 768d vectors | active |
## Dependencies
| Component | Depends On | Failure Impact |
|-----------|-----------|---------------|
| FAISS Index | Ollama | fallback to BM25-only (~50% accuracy) |
| brain_query API | BM25 + FAISS | no search if both down |
