---
kind: tools
id: bld_tools_vector_store
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for vector_store production
quality: 9.0
title: "Tools Vector Store"
version: "1.0.0"
author: n03_builder
tags: [vector_store, builder, examples]
tldr: "Golden and anti-examples for vector store construction, demonstrating ideal structure and common pitfalls."
domain: "vector store construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_model_provider
  - bld_tools_embedder_provider
  - bld_tools_model_card
  - bld_memory_vector_store
  - bld_sp_tools_software_project
  - bld_knowledge_card_vector_store
  - bld_tools_client
  - bld_tools_response_format
  - bld_tools_search_tool
  - bld_tools_function_def
---

# Tools: vector-store-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing vector_store configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
| cex_retriever.py | TF-IDF search for similar vector configs | Phase 1 (find references) | ACTIVE |
| cex_compile.py | Compile .md to .yaml | Phase 4 (post-save) | ACTIVE |
| validate_artifact.py | Validate any artifact kind via builder gates | Phase 3 | [PLANNED] |
## Data Sources (APIs and Docs)
| Source | URL | Data |
|--------|-----|------|
| Pinecone docs | https://docs.pinecone.io/ | Serverless, pods, namespaces |
| Pinecone pricing | https://www.pinecone.io/pricing/ | Per-vector and per-query costs |
| pgvector | https://github.com/pgvector/pgvector | PostgreSQL extension, ivfflat/hnsw |
| Chroma docs | https://docs.trychroma.com/ | Collections, persistence, filtering |
| FAISS wiki | https://github.com/facebookresearch/faiss/wiki | IndexFlatL2, HNSW, IVF-PQ |
| Qdrant docs | https://qdrant.tech/documentation/ | Collections, filtering, hybrid search |
| Weaviate docs | https://weaviate.io/developers/weaviate | Schema, modules, vectorizers |
| Milvus docs | https://milvus.io/docs | Collections, partitions, index types |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation (until validate_artifact.py exists)
Manually check each QUALITY_GATES gate against produced artifact.
All 10 HARD gates must pass. SOFT gates contribute to score.
## SDK References
| Backend | SDK | Install |
|---------|-----|---------|
| Pinecone | `pinecone-client` | `pip install pinecone-client` |
| pgvector | `psycopg2` + SQL | `pip install psycopg2-binary` |
| Chroma | `chromadb` | `pip install chromadb` |
| FAISS | `faiss-cpu` / `faiss-gpu` | `pip install faiss-cpu` |
| Qdrant | `qdrant-client` | `pip install qdrant-client` |
| Weaviate | `weaviate-client` | `pip install weaviate-client` |
| Milvus | `pymilvus` | `pip install pymilvus` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_model_provider]] | sibling | 0.46 |
| [[bld_tools_embedder_provider]] | sibling | 0.44 |
| [[bld_tools_model_card]] | sibling | 0.43 |
| [[bld_memory_vector_store]] | downstream | 0.37 |
| [[bld_sp_tools_software_project]] | sibling | 0.36 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.35 |
| [[bld_tools_client]] | sibling | 0.35 |
| [[bld_tools_response_format]] | sibling | 0.35 |
| [[bld_tools_search_tool]] | sibling | 0.33 |
| [[bld_tools_function_def]] | sibling | 0.32 |
