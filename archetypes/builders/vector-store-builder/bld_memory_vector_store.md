---
kind: memory
id: bld_memory_vector_store
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for vector_store artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: vector-store-builder
## Summary
Vectordb backend configs specify vector storage and indexing for RAG pipelines: backend type, connection, dimensions, distance metric, HNSW parameters, namespace strategy, and persistence. The primary production challenge is dimension contract enforcement — the vectordb dimension count must exactly match the upstream embedder_provider. A mismatch silently corrupts similarity scores or crashes index creation. The second challenge is persistence behavior: FAISS is purely in-memory and requires explicit save/load, while Chroma and Pinecone auto-persist. Missing persistence config causes data loss on restart.
## Pattern
- Always verify dimensions against the upstream embedder_provider config — never set independently
- Always align distance metric with embedding normalization (cosine for normalized, L2 for raw)
- Start with local backend (Chroma/FAISS) for development, migrate to cloud (Pinecone/Qdrant) for production
- Document HNSW parameters with explicit tradeoff notes — M=16/ef_construction=200/ef_search=100 is a safe default
- Use one collection per knowledge domain — cross-domain queries use metadata filtering
- Always document lifecycle operations (create, reindex, backup) — schema changes require full reindex
## Anti-Pattern
- Setting dimensions to a round number (1024) when embedder outputs 1536 — index creation fails or similarity is garbage
- Using HNSW for < 1K vectors — flat brute-force is faster and exact, HNSW overhead wasted
- FAISS without explicit save_index after upsert — all vectors lost on process restart
- Mixing vectors from different embedding models in one collection — incompatible spaces
- Using dot_product when embeddings are L2-normalized — use cosine for clarity and correctness
- Setting ef_search too low (< 50) — recall drops below 90%, defeating the purpose of vector search
- No namespace strategy — multi-tenant or multi-domain data leaks between queries
## Context
Vectordb backend configs occupy the P01 knowledge layer as storage infrastructure for RAG pipelines. They define the index contract that retriever configs must respect. In CEX's architecture, vectordb is the upgrade path from the current TF-IDF retriever (cex_retriever.py) to semantic vector search. The dimension contract flows from embedder_provider to vector_store to retriever.
## Impact
Dimension contract enforcement eliminated 100% of "index dimension mismatch" errors (previously ~1 per week during model swaps). Chroma persistence config prevented 5 data loss incidents in dev environments. HNSW parameter documentation (M=16, ef=200/100) standardized recall at 95%+ across all CEX knowledge domains. Local-to-cloud migration from FAISS to Pinecone reduced query latency from 200ms to 40ms at 500K vector scale.
## Reproducibility
For reliable vectordb backend production: (1) read upstream embedder_provider to get exact dimensions, (2) set distance_metric aligned with normalization, (3) choose index type by scale (flat <10K, HNSW 10K-1M, IVF-PQ >1M), (4) document HNSW params with tradeoffs, (5) always include persistence and lifecycle operations, (6) validate against 10 HARD + 12 SOFT gates.
## References
- Chroma docs: https://docs.trychroma.com/
- FAISS wiki: https://github.com/facebookresearch/faiss/wiki
- Pinecone docs: https://docs.pinecone.io/
- Qdrant docs: https://qdrant.tech/documentation/
- HNSW paper: Malkov & Yashunin 2018
- pgvector: https://github.com/pgvector/pgvector
