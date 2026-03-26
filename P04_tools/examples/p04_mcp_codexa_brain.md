---
id: p04_mcp_codexa_brain
name: codexa-brain
description: "Hybrid RAG retrieval server — BM25 keyword + FAISS vector search with Ollama embeddings"
transport: stdio
tools_provided: [brain_query, brain_prime, brain_list, brain_status, smart_context]
resources_provided: [pool_index]
pillar: P04
kind: mcp_server
version: 1.0.0
created: 2026-03-24
author: edison
domain: knowledge-retrieval
quality: 9.5
tags: [mcp, brain, rag, bm25, faiss, ollama, search]
---

# Brain MCP Server

## Name
- Name: codexa-brain
- Role: Central knowledge retrieval for all CODEXA satellites

## Transport
- Transport: stdio (via `python -m codexa_brain.server`)
- Auth: none (local only)
- Timeout: 30s per query

## Tools Provided
| Tool | Purpose |
|------|---------|
| brain_query(question, scope, k) | Semantic search, returns ranked chunks with scores |
| brain_prime(entity, depth) | Executive summary at minimal/standard/deep depth |
| brain_list(scope, format) | List entities by category (agents, workflows, all) |
| brain_status(verbose) | Health: model state, cache hits, uptime |
| smart_context(query, agent) | Unified nav: semantic + file structure |

## Resources Provided
| Resource | Shape |
|----------|-------|
| pool_index | json (agent/workflow/prompt counts) |

## Integration Notes
- Start: `python -m codexa_brain.server` (cwd: src/)
- Required env: `CODEXA_ROOT`, `PYTHONPATH`
- Fallback: Ollama down = BM25 keyword-only (~50% accuracy vs ~88% hybrid)
- Index rebuild: `python build_indexes_ollama.py --scope all` (~20 min)
- Model: nomic-embed-text (768d), chunk 2048, overlap 128

## Debugging
1. Check: `curl http://localhost:11434/api/tags` (Ollama running?)
2. Verify: FAISS index exists in `src/indexes/` (~140MB)
3. Test: `brain_status(verbose=true)` for cache/model state
4. Common: "model not found" = run `ollama pull nomic-embed-text`
