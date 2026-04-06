---
kind: tools
id: bld_tools_vectordb_backend
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for vectordb_backend production
---

# Tools: vectordb-backend-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing vectordb_backend configs in pool | Phase 1 (check duplicates) | CONDITIONAL |
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
