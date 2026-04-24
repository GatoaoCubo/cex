---
id: n04_ec_knowledge
kind: embedding_config
8f: F3_inject
pillar: P01_knowledge
version: 3.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge_nucleus
title: "N04 Embedding Model Configuration"
models_count: 2
default_model_id: google-text-embedding-004
quality: 9.1
tags: [embedding, config, n04, knowledge, rag, p01, google]
tldr: "Specifies the embedding model configurations for N04, establishing 'google/text-embedding-004' as the primary model and 'jinaai/jina-embeddings-v2-base-en' as the secondary."
density_score: 0.91
related:
  - p03_sp_embedding_config_builder
  - p03_ins_embedder_provider
  - p01_kc_embedding_config
  - p03_sp_embedder_provider_builder
  - p01_kc_embedder_provider
  - p01_gl_embedding
  - bld_collaboration_model_provider
  - p01_emb_openai_text_embedding_3_small
  - bld_instruction_embedding_config
  - n01_emb_text_embedding_4
---

# N04 Embedding Model Configuration

## 1. Overview
This document specifies the configurations for the embedding models used by the N04 Knowledge Nucleus. The choice of embedding model is critical for the performance of semantic search and the overall RAG pipeline. This configuration defines a primary, high-performance model from Google and a secondary, high-performance open-source model.

---

## 2. Primary Model: `google/text-embedding-004`

- **Provider**: Google
- **Dimensions**: `768`
- **Distance Metric**: `Cosine Similarity`
- **Normalize**: `True`
- **Cost**: Managed via Google Cloud subscription.
- **Use Case**: **Default for all CEX ingestions.** As the latest generation of Google's embedding models, it provides state-of-the-art performance tailored for the Gemini family of models. Its native integration within the Google ecosystem makes it the canonical choice.

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **`model_id`** | `google/text-embedding-004` | SOTA performance and native integration with the CEX Gemini-based architecture. |
| **`provider`** | `Google` | The official provider of the model via Vertex AI API. |
| **`dimensions`** | `768` | Standard, effective dimension size. |
| **`distance_metric`**| `cosine` | Industry standard for comparing normalized vectors. |
| **`normalize`** | `true` | Required for accurate cosine similarity and efficient search. |

---

## 3. Secondary Model: `jinaai/jina-embeddings-v2-base-en`

- **Provider**: Hugging Face / Self-Hosted
- **Dimensions**: `768`
- **Distance Metric**: `Cosine Similarity`
- **Normalize**: `True`
- **License**: Apache 2.0
- **Use Case**: **Batch processing, offline environments, or for tasks requiring an open-source, auditable model.** Jina v2 is a top-performing open-source model with a large context length, making it a powerful and flexible alternative.

| Parameter | Value | Rationale |
| :--- | :--- | :--- |
| **`model_id`** | `jinaai/jina-embeddings-v2-base-en`| Best-in-class open-source model with a permissive license and excellent performance. |
| **`provider`** | `HuggingFace` | Can be accessed via API or hosted locally for private data contexts. |
| **`dimensions`** | `768` | Standard dimension size, matching the primary model for easier interchangeability. |
| **`distance_metric`**| `cosine` | Standard for comparing normalized vectors. |
| **`normalize`** | `true` | Ensures vectors are on the unit sphere for comparison. |

## 4. Selection & Routing Logic
The `embedding_apis` MCP will route requests based on the following logic:
1.  **Default**: All standard ingestion workflows will use the **Primary Model** (`google/text-embedding-004`).
2.  **Explicit Request**: An agent can explicitly request the **Secondary Model** for a specific task by providing a `use_secondary_model: true` flag in its request.
3.  **Private Data Context**: If an ingestion source is flagged as `private: true`, the system will automatically use the self-hosted instance of the **Secondary Model** to ensure data does not leave the CEX environment.

## 5. Integration
This configuration is a direct dependency of the **Generate Embeddings** step in the `WF-01: RAG Ingestion & Indexing` workflow. The chosen model's output vector size (`dimensions`) dictates the schema of the target `vector_db` MCP. Any change to the dimensionality of the default model requires a full re-indexing of the knowledge base.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_embedding_config_builder]] | related | 0.34 |
| [[p03_ins_embedder_provider]] | related | 0.32 |
| [[p01_kc_embedding_config]] | related | 0.32 |
| [[p03_sp_embedder_provider_builder]] | related | 0.32 |
| [[p01_kc_embedder_provider]] | related | 0.30 |
| [[p01_gl_embedding]] | related | 0.30 |
| [[bld_collaboration_model_provider]] | related | 0.30 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.30 |
| [[bld_instruction_embedding_config]] | related | 0.29 |
| [[n01_emb_text_embedding_4]] | sibling | 0.29 |
