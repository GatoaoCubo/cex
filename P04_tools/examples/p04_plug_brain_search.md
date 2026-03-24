---
id: p04_plug_brain_search
name: brain_search_plugin
description: "Extensible search plugin combining BM25 keyword and FAISS semantic search with auto-index rebuild"
extension_points:
  - keyword_search
  - vector_search
  - index_builder
dependencies:
  - ollama (nomic-embed-text)
  - faiss-cpu
  - sentence-transformers
lp: P04
type: plugin
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: knowledge-retrieval
quality: 9.0
tags: [plugin, search, bm25, faiss, vector, semantic, ollama]
---

# Brain Search Plugin — Hybrid Retrieval Engine

## Purpose
Core search plugin for codexa-brain MCP server. Provides two search strategies that combine for hybrid retrieval: BM25 keyword matching (~50% accuracy alone) and FAISS vector search with Ollama embeddings (~88% hybrid accuracy).

## Architecture
```
query -> [BM25 keyword search] -> ranked results (fast, ~5ms)
      -> [FAISS vector search] -> ranked results (slower, ~150ms)
      -> [score fusion] -> hybrid ranked output
```

## Components

### keyword_search
- Pre-built BM25 index over all CODEXA knowledge artifacts
- Build: `python build_keyword_index.py --scope all`
- Scopes: agents, workflows, prompts, all
- Fast path: ~50ms per query

### vector_search
- FAISS index with `nomic-embed-text` embeddings via Ollama
- Index size: ~140MB (gitignored, rebuild on fresh clone)
- Model loading: ~23s first load, cached after
- Build: `python build_indexes_ollama.py --scope all` (~20 min)

### index_builder
- Chunks markdown files into ~512 token segments
- Extracts metadata (frontmatter, headers, paths)
- Generates embeddings via local Ollama instance
- Stores in FAISS flat index (L2 distance)

## Degradation
| Condition | Mode | Accuracy |
|-----------|------|----------|
| Ollama + FAISS available | hybrid | ~88% |
| Ollama down | keyword-only | ~50% |
| No pre-built index | unavailable | error with build instructions |

## Extension
