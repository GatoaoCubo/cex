---
kind: architecture
id: bld_architecture_embedding_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of embedding_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Embedding Config"
version: "1.0.0"
author: n03_builder
tags: [embedding_config, builder, examples]
tldr: "Golden and anti-examples for embedding config construction, demonstrating ideal structure and common pitfalls."
domain: "embedding config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| model_id | Embedding model identifier (e.g. `nomic-embed-text`, `text-embedding-3-small`) | embedding-config-builder | required |
| provider | Hosting provider: ollama, openai, cohere, huggingface | embedding-config-builder | required |
| dimensions | Output vector dimensionality (e.g. 768, 1536, 3072) | embedding-config-builder | required |
| chunk_size | Max tokens per text chunk before splitting | embedding-config-builder | required |
| chunk_overlap | Token overlap between adjacent chunks for context continuity | embedding-config-builder | required |
| distance_metric | Similarity function: cosine, dot_product, euclidean | embedding-config-builder | required |
| tokenizer | Tokenizer used for chunk boundary calculation | embedding-config-builder | required |
| batch_size | Number of texts vectorized per API call | embedding-config-builder | optional |
| normalize | Whether to L2-normalize output vectors (true/false) | embedding-config-builder | required |
| cost_per_1k_tokens | Pricing reference for budget planning | embedding-config-builder | optional |
| metadata | config id, version, pillar, scope, author, created date | embedding-config-builder | required |
## Dependency Graph
```
rag_source (P01) --informs--> embedding_config (source characteristics shape chunk_size)
embedding_config --consumed_by--> knowledge_index (P10) (index uses model + dimensions + metric)
embedding_config --consumed_by--> retriever (P02) (retriever needs vector params to query index)
knowledge_card (P01) --independent-- embedding_config (KC distills knowledge; config vectorizes it)
signal (P12) --independent-- embedding_config (config is static spec, not runtime event)
workflow (P12) --independent-- embedding_config (workflow orchestrates; config parameterizes)
```
| From | To | Type | Data |
|------|----|------|------|
| rag_source | embedding_config | data_flow | source size and language inform chunk_size and tokenizer |
| embedding_config | knowledge_index | consumed_by | model_id, dimensions, distance_metric for index construction |
| embedding_config | retriever | consumed_by | vector params needed to query and rank results |
## Boundary Table
| embedding_config IS | embedding_config IS NOT |
|--------------------|------------------------|
| A model configuration: which embedding model, with what parameters | A knowledge_card — KC distills and stores domain knowledge |
| Specifies vectorization: chunk size, overlap, distance metric | A rag_source — rag_source points to an external indexable source |
| Infrastructure spec: bridges raw text to searchable vector index | A knowledge_index (P10) — knowledge_index configures the search index structure |
| Defines how text becomes vectors, not what text to embed | A glossary_entry — glossary defines domain terms |
| Includes cost and normalization for production deployment | A context_doc — context_doc provides background knowledge |
| Consumed by both the indexer and the retriever | A few_shot_example — examples demonstrate input/output patterns |
| Static spec set once per scope or model change | A retriever — retriever executes queries using this config |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Source | rag_source | External text sources whose characteristics inform chunking strategy |
| Model | model_id, provider, dimensions, tokenizer | Define which embedding model produces the vectors |
| Chunking | chunk_size, chunk_overlap | Control how raw text is split before vectorization |
| Similarity | distance_metric, normalize | Determine how vector similarity is computed at query time |
| Performance | batch_size, cost_per_1k_tokens | Tune throughput and track cost for production use |
| Identity | metadata | Record config id, version, scope, and authoring context |
