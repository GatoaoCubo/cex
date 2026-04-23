---
kind: schema
id: bld_schema_embedding_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for embedding_config
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_chunk_strategy
  - bld_schema_embedder_provider
  - bld_schema_retriever_config
  - bld_schema_constraint_spec
  - bld_schema_agent_card
  - bld_schema_effort_profile
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_smoke_eval
---

# Schema: embedding_config
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_emb_{model}) | YES | - | Namespace compliance |
| kind | literal "embedding_config" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| model_name | string | YES | - | Embedding model identifier |
| provider | string | YES | - | Model provider (ollama, openai, cohere, voyager) |
| dimensions | integer | YES | - | Vector dimensions (e.g. 768, 1024, 1536) |
| chunk_size | integer | YES | - | Tokens per chunk |
| overlap | integer | REC | 0 | Token overlap between chunks |
| tokenizer | string | REC | - | Tokenizer used (cl100k_base, etc.) |
| distance_metric | enum (cosine, euclidean, dot_product) | REC | "cosine" | Similarity function |
| batch_size | integer | REC | 32 | Vectors per batch call |
| normalize | boolean | REC | true | L2 normalize vectors |
| max_tokens | integer | REC | - | Model max input tokens |
| cost_per_1m_tokens | float or null | REC | null | USD per 1M tokens (null if free/local) |
| domain | string | YES | - | Domain this config serves |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "embedding" |
| tldr | string <= 160ch | YES | - | Dense summary |
## ID Pattern
Regex: `^p01_emb_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Model` — model name, provider, and key specs
2. `## Chunking` — chunk_size, overlap, and tokenizer strategy
3. `## Performance` — latency, throughput, and cost characteristics
4. `## Integration` — how to use this config in the RAG pipeline
## Constraints
- max_bytes: 512 (body only)
- naming: p01_emb_{model_slug}.yaml
- machine_format: yaml
- id == filename stem
- dimensions MUST be positive integer
- chunk_size MUST be positive integer
- distance_metric MUST be one of: cosine, euclidean, dot_product
- quality: null always
- embedding_config is CONFIGURATION — no index logic (that is knowledge_index P10)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_chunk_strategy]] | sibling | 0.63 |
| [[bld_schema_embedder_provider]] | sibling | 0.62 |
| [[bld_schema_retriever_config]] | sibling | 0.62 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_agent_card]] | sibling | 0.61 |
| [[bld_schema_effort_profile]] | sibling | 0.61 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_unit_eval]] | sibling | 0.60 |
| [[bld_schema_golden_test]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
