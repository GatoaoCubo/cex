---
id: p04_mcp_organization_brain
name: organization-brain
description: "Hybrid RAG retrieval server — BM25 keyword + FAISS vector search with Ollama embeddings"
transport: stdio
tools_provided: [brain_query, brain_prime, brain_list, brain_status, smart_context]
resources_provided: [pool_index]
pillar: P04
kind: mcp_server
8f: F5_call
version: 1.0.0
created: 2026-03-24
author: builder_agent
domain: knowledge-retrieval
quality: 9.1
tags: [mcp, brain, rag, bm25, faiss, ollama, search]
updated: "2026-04-07"
title: "Mcp Server Codexa Brain"
density_score: 0.92
tldr: "Defines mcp server for mcp server codexa brain, with validation gates and integration points."
related:
  - p10_bi_organization_brain
  - p04_plug_brain_search
  - p01_rs_brain_faiss_index
  - p07_se_brain_query
  - p01_emb_nomic_embed_text
  - bld_examples_instruction
  - bld_examples_component_map
  - bld_memory_mcp_server
  - bld_examples_smoke_eval
  - mcp-server-builder
---

# Brain MCP Server

## Name
1. Name: organization-brain
2. Role: Central knowledge retrieval for all organization agent_groups

## Transport
1. Transport: stdio (via `python -m organization_brain.server`)
2. Auth: none (local only)
3. Timeout: 30s per query

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
1. Start: `python -m organization_brain.server` (cwd: src/)
2. Required env: `organization_ROOT`, `PYTHONPATH`
3. Fallback: Ollama down = BM25 keyword-only (~50% accuracy vs ~88% hybrid)
4. Index rebuild: `python build_indexes_ollama.py --scope all` (~20 min)
5. Model: nomic-embed-text (768d), chunk 2048, overlap 128

## Debugging
1. Check: `curl http://localhost:11434/api/tags` (Ollama running?)
2. Verify: FAISS index exists in `src/indexes/` (~140MB)
3. Test: `brain_status(verbose=true)` for cache/model state
4. Common: "model not found" = run `ollama pull nomic-embed-text`

## Metadata

```yaml
id: p04_mcp_organization_brain
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p04-mcp-organization-brain.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_bi_organization_brain]] | downstream | 0.42 |
| [[p04_plug_brain_search]] | related | 0.40 |
| [[p01_rs_brain_faiss_index]] | related | 0.38 |
| [[p07_se_brain_query]] | downstream | 0.32 |
| [[p01_emb_nomic_embed_text]] | upstream | 0.31 |
| [[bld_examples_instruction]] | downstream | 0.28 |
| [[bld_examples_component_map]] | related | 0.28 |
| [[bld_memory_mcp_server]] | downstream | 0.26 |
| [[bld_examples_smoke_eval]] | downstream | 0.26 |
| [[mcp-server-builder]] | related | 0.25 |
