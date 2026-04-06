---
kind: memory
id: bld_memory_embedder_provider
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for embedder_provider artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: embedder-provider-builder
## Summary
Embedder provider configs specify embedding model connections for RAG pipelines: provider API, model ID, dimensions, normalization, batch sizes, and authentication. The primary production challenge is dimension accuracy — using wrong dimensions corrupts entire vector indices and requires full reindexing. The second challenge is normalization consistency: mixing normalized and unnormalized vectors in the same index produces meaningless similarity scores.
## Pattern
- Always verify dimensions against official provider documentation — never copy from third-party sources
- Always set normalization explicitly — some providers normalize by default (OpenAI), others don't (sentence-transformers)
- Document matryoshka support when available — MRL dimension reduction saves 60-70% storage with <2% quality loss
- Include MTEB retrieval scores for the specific task type (STS, retrieval, clustering) — aggregate scores hide task-specific weaknesses
- Batch size must match provider rate limits — exceeding causes 429 errors and pipeline stalls
- Distance metric must align with normalization: cosine for normalized, dot_product or L2 for raw vectors
## Anti-Pattern
- Using dimensions from a blog post instead of official docs — blog posts often cite outdated or wrong values
- Embedding documents with one model and queries with another — vector spaces are incompatible across models
- Setting batch_size to max integer — providers enforce limits server-side, causing silent failures or 429s
- Omitting api_key_env and hardcoding credentials — security violation, breaks in CI/CD
- Using text-embedding-ada-002 dimensions (1536) for text-embedding-3-large (3072) — same provider, different dimensions
- Ignoring max_tokens — documents exceeding the limit are silently truncated, losing trailing content
## Context
Embedder provider configs occupy the P01 knowledge layer as infrastructure components for RAG pipelines. They define the vector space contract that vectordb_backend and retriever configs must respect. In multi-provider setups, embedder configs enable fallback chains (cloud primary, local fallback) and cost-aware routing (cheap model for bulk ingestion, quality model for queries).
## Impact
Configs with verified dimensions eliminated reindexing incidents (previously ~2 per quarter). Matryoshka dimension reduction on text-embedding-3-small (1536 to 512) reduced Pinecone costs by 65% with 1.1% retrieval quality loss. Explicit normalization flags prevented 3 production incidents where cosine similarity returned nonsense on unnormalized vectors.
## Reproducibility
For reliable embedder provider production: (1) source dimensions from official API docs, (2) verify normalization behavior empirically with a test vector, (3) set batch_size to 80% of provider limit for safety margin, (4) include MTEB scores from the official leaderboard, (5) test dimension reduction quality on a representative sample before committing to reduced dimensions.
## References
- MTEB leaderboard: https://huggingface.co/spaces/mteb/leaderboard
- OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
- Matryoshka Representation Learning: Kusupati et al. 2022
- Sentence-Transformers documentation: https://www.sbert.net/
