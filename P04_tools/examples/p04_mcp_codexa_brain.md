---
id: p04_mcp_codexa_brain
name: codexa-brain
description: "MCP server providing RAG-style retrieval for the CODEXA knowledge base — hybrid search BM25+FAISS with Ollama embeddings"
transport: stdio
tools_provided:
  - brain_prime
  - brain_query
  - brain_list
  - brain_status
  - smart_context
resources_provided:
  - pool_index
lp: P04
type: mcp_server
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: knowledge-retrieval
quality: 9.0
tags: [mcp, brain, search, rag, bm25, faiss, ollama]
---

# Brain MCP Server — Hybrid Knowledge Retrieval

## Purpose
codexa-brain is the central MCP server for CODEXA knowledge retrieval. Reduces context consumption from ~50k tokens to ~400 tokens per prime operation via executive summaries and semantic search.

## Architecture
- **Transport**: stdio (launched via `python -m codexa_brain.server`)
- **Search Strategy**: Hybrid — BM25 keyword index + FAISS vector search with `nomic-embed-text` via Ollama
- **Fallback**: Auto-degrades to keyword-only (~50% accuracy) when Ollama/model unavailable
- **Warmup**: Background thread pre-loads SentenceTransformer model on boot (~23s saved on first query)
- **Cache**: LRU query cache (100 entries) with hit rate tracking

## Tools

### brain_prime(entity, depth)
Executive summary of any CODEXA entity. Depths: minimal (~150 tokens), standard (~400), deep (~800).

### brain_query(question, scope, k)
Semantic search across knowledge base. Returns ranked chunks with scores and sources. Pre-built BM25 index required (~50ms fast path).

### brain_list(scope, format)
Lists entities by category (agents, workflows, prompts, all). Format: names or summary.

### brain_status(verbose)
Health check — server status, model loading state, query count, uptime, cache hit rate.

### smart_context(query, agent, include_files, include_knowledge)
Unified navigation combining semantic search + file structure. Returns knowledge matches, domains, and suggested commands.

## Configuration
```json
{
  "codexa-brain": {
    "type": "stdio",
    "command": "python",
    "args": ["-m", "codexa_brain.server"],
    "cwd": "records/core/brain/mcp-codexa-brain/src",
    "env": {
      "PYTHONPATH": "records/core/brain/mcp-codexa-brain/src",
      "CODEXA_ROOT": "."
    }
  }
}
```

## Metrics
| Metric | Value |
|--------|-------|
| Tools exposed | 5 (prime, query, list, status, smart_context) |
| Query latency (keyword) | ~50ms |
| Query latency (hybrid) | ~200ms |
| Model warmup | ~23s (background, non-blocking) |
| Cache capacity | 100 entries LRU |
| Index rebuild | ~20 min (build_indexes_ollama.py) |
