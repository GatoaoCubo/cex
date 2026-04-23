---
kind: knowledge_card
id: bld_knowledge_card_embedder_provider
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for embedder_provider production — atomic searchable facts
sources: embedder-provider-builder SCHEMA + MANIFEST, MTEB leaderboard, provider docs
quality: 9.1
title: "Knowledge Card Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_memory_embedder_provider
  - p03_ins_embedder_provider
  - p03_sp_embedder_provider_builder
  - p11_qg_embedder_provider
  - bld_examples_embedder_provider
  - bld_config_embedder_provider
  - bld_schema_embedder_provider
  - bld_knowledge_card_model_provider
  - p01_kc_embedder_provider
  - p01_emb_openai_text_embedding_3_small
---

# Domain Knowledge: embedder_provider
## Executive Summary
Embedder provider configs are infrastructure artifacts for RAG pipelines — they encode the connection spec between your application and an embedding model API. Each config captures provider, model ID, dimensions, normalization behavior, batch limits, max tokens, authentication, and pricing. The dimension count is a hard contract: downstream vector indices must match exactly. Normalization determines which distance metric to use. These configs differ from vector_store (which stores vectors), model_provider (which routes LLM calls), and retriever (which orchestrates search).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 (knowledge infrastructure) |
| Kind | `embedder_provider` (exact literal) |
| ID pattern | `p01_emb_{provider}_{model_slug}` |
| Required frontmatter | 20+ fields |
| Quality gates | 10 HARD + 12 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.85 |
| Quality field | always `null` |
| Domain field | always `embedding` |
| Key booleans | normalize, matryoshka, sparse_support, truncate |
| Provider enum | openai, cohere, voyage, jina, nomic, local, huggingface, other |
## Patterns
| Pattern | Application |
|---------|-------------|
| Dimension contract | Exact integer from official docs; vectordb index must match |
| Normalization explicitness | Always boolean true/false; determines distance metric choice |
| Matryoshka reduction | Reduce dimensions via MRL for 60-70% storage savings with <2% quality loss |
| Environment variable auth | api_key_env points to env var name, never contains the key itself |
| Batch size safety margin | Set to 80% of provider limit to avoid 429 errors under load |
| MTEB task-specific scoring | Cite retrieval or STS score, not aggregate — aggregate hides weaknesses |
| Local fallback | Configure sentence-transformers as fallback when cloud API is unavailable |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Dimensions from blog post | Third-party sources often cite wrong or outdated values |
| Different models for docs vs queries | Incompatible vector spaces produce meaningless similarity |
| Hardcoded API key in config | Security violation; breaks in CI/CD and rotation |
| batch_size: 999999 | Provider enforces limits server-side; causes 429 or silent failure |
| normalize: "yes" | Must be boolean true/false; string breaks validation |
| Mixing embedding models in one index | Dimensions and vector spaces are model-specific |
| Ignoring max_tokens | Documents silently truncated, losing trailing content |
| Using dot_product on normalized vectors | Equivalent to cosine but less readable; use cosine explicitly |
## Application
1. Set `id: p01_emb_{provider}_{model_slug}` — must equal filename stem
2. Populate all required frontmatter fields; set `quality: null`
3. Set `dimensions` from official provider documentation (integer, exact)
4. Set `normalize: true/false` from provider default behavior
5. Set `distance_metric` aligned with normalization (cosine if normalized)
6. Write `## Configuration Matrix` with Value + Source URL per row
7. Write `## Dimension Tradeoffs` if model supports matryoshka
8. Validate: body <= 4096 bytes, all configs sourced, 10 HARD + 12 SOFT gates
## References
- MTEB leaderboard: https://huggingface.co/spaces/mteb/leaderboard
- OpenAI embeddings: https://platform.openai.com/docs/guides/embeddings
- Cohere embed: https://docs.cohere.com/docs/models#embed
- Matryoshka Representation Learning: Kusupati et al. 2022
- Sentence-Transformers: https://www.sbert.net/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_embedder_provider]] | downstream | 0.55 |
| [[p03_ins_embedder_provider]] | downstream | 0.54 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.51 |
| [[p11_qg_embedder_provider]] | downstream | 0.49 |
| [[bld_examples_embedder_provider]] | downstream | 0.47 |
| [[bld_config_embedder_provider]] | downstream | 0.46 |
| [[bld_schema_embedder_provider]] | downstream | 0.42 |
| [[bld_knowledge_card_model_provider]] | sibling | 0.41 |
| [[p01_kc_embedder_provider]] | sibling | 0.39 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.37 |
