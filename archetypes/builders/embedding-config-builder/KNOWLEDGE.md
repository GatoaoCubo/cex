---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for embedding_config production
sources: [MTEB benchmark, OpenAI embeddings docs, Ollama model library, FAISS docs]
---

# Domain Knowledge: embedding_config

## Foundational Concept
Embedding configs define how text is converted to vectors for semantic search.
Rooted in dense retrieval research (Karpukhin et al. 2020 DPR), the MTEB benchmark
for model comparison, and production RAG patterns. In CEX, embedding_configs sit in
the spec layer of P01 — they define MODEL parameters, not index or pipeline logic.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| OpenAI Embeddings API | Model, dimensions, pricing | model_name, dimensions, cost |
| Ollama Model Library | Local model specs, quantization | provider, model_name (local) |
| MTEB Benchmark | Model quality ranking by task | Model selection guidance |
| FAISS Documentation | Index types, distance metrics | distance_metric field |
| LangChain Text Splitters | Chunking strategies, overlap | chunk_size, overlap fields |

## Key Patterns
- Dimensions determine vector space richness (768 baseline, 1536 high-fidelity)
- Chunk size balances granularity vs context (256-512 for retrieval, 1024+ for summarization)
- Overlap prevents information loss at chunk boundaries (10-20% of chunk_size)
- Cosine similarity is the default metric (normalize=true required)
- Local models (Ollama) trade quality for zero cost and privacy
- Batch size affects throughput: larger batches = fewer API calls = lower latency
- Normalization is required for cosine similarity (skip only for dot_product)

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| provider | CEX uses Ollama locally, API remotely | LangChain embeddings class |
| cost_per_1m_tokens | Budget tracking for API models | OpenAI pricing page |
| normalize | Explicit control for distance metric | FAISS IndexFlatIP vs IndexFlatL2 |
| overlap | Chunk boundary handling | LangChain chunk_overlap |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT embedding_config |
|------|------------|-------------------------------|
| brain_index (P10) | Search index configuration (BM25, FAISS) | brain_index CONFIGURES the index; embedding_config CONFIGURES the model |
| rag_source (P01) | External source pointer with URL | rag_source POINTS to data; embedding_config VECTORIZES data |
| knowledge_card (P01) | Dense research fact | KC IS content; embedding_config PROCESSES content |
| context_doc (P01) | Domain background | context_doc PROVIDES context; embedding_config ENCODES context |

## References
- Karpukhin et al. Dense Passage Retrieval (2020) — Foundation of dense embeddings
- Muennighoff et al. MTEB: Massive Text Embedding Benchmark (2022)
- OpenAI Embeddings Guide — text-embedding-3-small/large specs
- Ollama Model Library — nomic-embed-text, mxbai-embed-large
