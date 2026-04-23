---
kind: knowledge_card
id: bld_knowledge_card_embedding_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for embedding_config production — vector model configuration
sources: MTEB benchmark, OpenAI embeddings, Ollama model library, DPR (Karpukhin 2020)
quality: 9.1
title: "Knowledge Card Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_embedding_config_builder
  - p01_kc_embedding_config
  - bld_examples_embedding_config
  - p03_sp_embedding_config_builder
  - p01_emb_openai_text_embedding_3_small
  - p01_emb_nomic_embed_text
  - p01_kc_vector_embedding_model_selection
  - bld_instruction_embedding_config
  - p01_kc_embedder_provider
  - p06_schema_embedding
---

# Domain Knowledge: embedding_config
## Executive Summary
Embedding configs define how text is converted to vectors for semantic search: model selection, dimensions, chunk size, overlap, distance metric, and normalization. They sit in the spec layer — defining MODEL parameters, not index structure (knowledge_index) or data sources (rag_source). The choice of embedding model determines retrieval quality, cost, and latency.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge) |
| Frontmatter fields | 20+ |
| Quality gates | 8 HARD + 8 SOFT |
| Default distance metric | cosine (requires normalize=true) |
| Chunk size range | 256-512 (retrieval), 1024+ (summarization) |
| Overlap | 10-20% of chunk_size |
| Key providers | OpenAI, Ollama (local), Cohere, Voyage |
## Patterns
- **Model selection by trade-off**:
| Model | Dimensions | Cost | Quality (MTEB) | Use case |
|-------|-----------|------|----------------|----------|
| text-embedding-3-small | 1536 | $0.02/1M | Good | Budget production |
| text-embedding-3-large | 3072 | $0.13/1M | Best (API) | High-fidelity retrieval |
| nomic-embed-text | 768 | Free (local) | Good | Privacy, zero cost |
| mxbai-embed-large | 1024 | Free (local) | Better (local) | Quality local option |
- **Chunk size balances granularity vs context**: smaller chunks = more precise retrieval but less context per result
- **Overlap prevents boundary loss**: 10-20% overlap ensures information at chunk edges is captured in adjacent chunks
- **Normalization**: required for cosine similarity; skip only when using dot_product distance
- **Batch processing**: larger batches = fewer API calls = lower latency; balance against memory constraints
- **Cost awareness**: track cost_per_1M_tokens; local models (Ollama) trade quality for zero cost
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No chunk overlap | Information at boundaries is lost; queries miss relevant content |
| Cosine without normalization | Distance calculations are incorrect; results unreliable |
| chunk_size > context_window | Chunks truncated silently; information loss |
| Mixing distance metrics | Index built with cosine, searched with dot_product = wrong ranking |
| Over-dimensioned model for simple task | Wastes compute and storage; 768-dim sufficient for most retrieval |
| No cost tracking | API embedding costs accumulate unnoticed |
## Application
1. Select provider: API (OpenAI, Cohere) for quality or local (Ollama) for cost/privacy
2. Choose model: match dimensions and quality to retrieval requirements
3. Set chunk_size: 256-512 for retrieval, 1024+ for summarization
4. Set overlap: 10-20% of chunk_size
5. Configure distance metric: cosine (default, normalize=true) or dot_product
6. Validate: chunks fit model context window, normalization matches distance metric
## References
- Karpukhin et al. 2020: Dense Passage Retrieval (DPR) — foundation of dense embeddings
- Muennighoff et al. 2022: MTEB — Massive Text Embedding Benchmark
- OpenAI: text-embedding-3-small/large specifications
- Ollama: nomic-embed-text, mxbai-embed-large model library

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_embedding_config_builder]] | downstream | 0.48 |
| [[p01_kc_embedding_config]] | sibling | 0.45 |
| [[bld_examples_embedding_config]] | downstream | 0.45 |
| [[p03_sp_embedding_config_builder]] | downstream | 0.44 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.44 |
| [[p01_emb_nomic_embed_text]] | related | 0.43 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.42 |
| [[bld_instruction_embedding_config]] | downstream | 0.39 |
| [[p01_kc_embedder_provider]] | sibling | 0.39 |
| [[p06_schema_embedding]] | downstream | 0.37 |
