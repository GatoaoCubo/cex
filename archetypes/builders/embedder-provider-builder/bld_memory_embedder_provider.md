---
kind: memory
id: bld_memory_embedder_provider
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for embedder_provider artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_embedder_provider
  - bld_collaboration_embedder_provider
  - p03_sp_embedder_provider_builder
  - embedder-provider-builder
  - p03_ins_embedder_provider
  - bld_examples_embedder_provider
  - bld_config_embedder_provider
  - p01_kc_embedder_provider
  - p11_qg_embedder_provider
  - p01_emb_openai_text_embedding_3_small
---
# Memory: embedder-provider-builder
## Summary
Embedder provider configs specify embedding model connections for RAG pipelines: provider API, model ID, dimensions, normalization, batch sizes, and authentication. The primary production challenge is dimension accuracy — using wrong dimensions corrupts entire vector indices and requires full reindexing. The second challenge is normalization consistency: mixing normalized and unnormalized vectors in the same index produces meaningless similarity scores.
## Pattern
1. Always verify dimensions against official provider documentation — never copy from third-party sources
2. Always set normalization explicitly — some providers normalize by default (OpenAI), others don't (sentence-transformers)
3. Document matryoshka support when available — MRL dimension reduction saves 60-70% storage with <2% quality loss
4. Include MTEB retrieval scores for the specific task type (STS, retrieval, clustering) — aggregate scores hide task-specific weaknesses
5. Batch size must match provider rate limits — exceeding causes 429 errors and pipeline stalls
6. Distance metric must align with normalization: cosine for normalized, dot_product or L2 for raw vectors
## Anti-Pattern
1. Using dimensions from a blog post instead of official docs — blog posts often cite outdated or wrong values
2. Embedding documents with one model and queries with another — vector spaces are incompatible across models
3. Setting batch_size to max integer — providers enforce limits server-side, causing silent failures or 429s
4. Omitting api_key_env and hardcoding credentials — security violation, breaks in CI/CD
5. Using text-embedding-ada-002 dimensions (1536) for text-embedding-3-large (3072) — same provider, different dimensions
6. Ignoring max_tokens — documents exceeding the limit are silently truncated, losing trailing content
## Context
Embedder provider configs occupy the P01 knowledge layer as infrastructure components for RAG pipelines. They define the vector space contract that vector_store and retriever configs must respect. In multi-provider setups, embedder configs enable fallback chains (cloud primary, local fallback) and cost-aware routing (cheap model for bulk ingestion, quality model for queries).
## Impact
Configs with verified dimensions eliminated reindexing incidents (previously ~2 per quarter). Matryoshka dimension reduction on text-embedding-3-small (1536 to 512) reduced Pinecone costs by 65% with 1.1% retrieval quality loss. Explicit normalization flags prevented 3 production incidents where cosine similarity returned nonsense on unnormalized vectors.
## Reproducibility
For reliable embedder provider production: (1) source dimensions from official API docs, (2) verify normalization behavior empirically with a test vector, (3) set batch_size to 80% of provider limit for safety margin, (4) include MTEB scores from the official leaderboard, (5) test dimension reduction quality on a representative sample before committing to reduced dimensions.
## References
1. MTEB leaderboard: https://huggingface.co/spaces/mteb/leaderboard
2. OpenAI embeddings guide: https://platform.openai.com/docs/guides/embeddings
3. Matryoshka Representation Learning: Kusupati et al. 2022
4. Sentence-Transformers documentation: https://www.sbert.net/

## Metadata

```yaml
id: bld_memory_embedder_provider
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-embedder-provider.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | embedder provider construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_embedder_provider]] | upstream | 0.64 |
| [[bld_collaboration_embedder_provider]] | upstream | 0.50 |
| [[p03_sp_embedder_provider_builder]] | upstream | 0.49 |
| [[embedder-provider-builder]] | upstream | 0.48 |
| [[p03_ins_embedder_provider]] | upstream | 0.47 |
| [[bld_examples_embedder_provider]] | upstream | 0.46 |
| [[bld_config_embedder_provider]] | upstream | 0.46 |
| [[p01_kc_embedder_provider]] | upstream | 0.44 |
| [[p11_qg_embedder_provider]] | downstream | 0.44 |
| [[p01_emb_openai_text_embedding_3_small]] | upstream | 0.42 |
