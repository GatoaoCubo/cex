---
id: p01_kc_embedding_config
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Embedding Config — Deep Knowledge for embedding_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: embedding_config
quality: 9.1
tags: [embedding_config, p01, GOVERN, kind-kc]
tldr: "Specifies which vector model encodes text into embeddings — dimensions, normalization, and distance metric"
when_to_use: "Building, reviewing, or reasoning about embedding_config artifacts"
keywords: [embedding, vector-model, dimensions, similarity]
feeds_kinds: [embedding_config]
density_score: null
related:
  - p01_emb_openai_text_embedding_3_small
  - bld_knowledge_card_embedding_config
  - bld_architecture_embedding_config
  - p01_kc_vector_embedding_model_selection
  - bld_collaboration_embedding_config
  - p01_kc_embedder_provider
  - bld_examples_embedding_config
  - embedding-config-builder
  - p03_sp_embedding_config_builder
  - p03_sp_embedder_provider_builder
---

# Embedding Config

## Spec
```yaml
kind: embedding_config
pillar: P01
llm_function: GOVERN
max_bytes: 512
naming: p01_emb_{{model}}.yaml
core: false
```

## What It Is
An embedding_config defines which vector model converts text into dense numerical representations for similarity search. It specifies model name, dimensions, chunk size compatibility, and distance metric. It is NOT a knowledge_index (P10, which configures the vector store/index itself) nor a chunk_strategy (which defines how text is split before encoding). The embedding_config sits between chunking and indexing — it governs the encoding step.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `Embeddings` (OpenAIEmbeddings, HuggingFaceEmbeddings) | Abstract base; `.embed_documents()` / `.embed_query()` |
| LlamaIndex | `BaseEmbedding` / `OpenAIEmbedding` | Registered via `Settings.embed_model` |
| CrewAI | Delegated to LangChain embeddings | No native embedding class |
| DSPy | `dspy.ColBERTv2` / `dspy.Embedder` | ColBERT for retrieval; Embedder for general |
| Haystack | `SentenceTransformersDocumentEmbedder` | Separate document vs query embedders |
| OpenAI | `text-embedding-3-small/large` | Matryoshka: truncate dimensions for cost savings |
| Anthropic | Voyager (via partnership) | No native embedding API; recommends Voyage AI |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| model_name | string | required | Larger models = better recall but higher latency/cost |
| dimensions | int | model-dependent | Lower dims = faster search but reduced precision |
| chunk_size | int | 512 | Must align with chunk_strategy; mismatch degrades quality |
| distance_metric | enum | cosine | Cosine for normalized; L2 for unnormalized; dot for speed |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Matryoshka truncation | Cost-sensitive, moderate recall | text-embedding-3-large at 256 dims (vs 3072 full) |
| Local model | Privacy/offline requirement | nomic-embed-text via Ollama, 768 dims |
| Asymmetric embedding | Query != document style | E5: prefix "query:" vs "passage:" |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Mismatched dimensions vs index | Insertion fails or silent truncation | Align embedding dims with vector store config |
| Switching models without re-indexing | Cosine similarity becomes meaningless | Re-embed all documents when changing models |
| Ignoring normalization | L2 distance skewed by vector magnitude | Use cosine or normalize before indexing |

## Integration Graph
```
[chunk_strategy] --> [embedding_config] --> [knowledge_index (P10)]
                          |
                   [retriever_config]
```

## Decision Tree
- IF privacy-critical or offline THEN local model (nomic, BGE)
- IF cost-sensitive with moderate quality THEN text-embedding-3-small or Matryoshka
- IF maximum retrieval quality THEN text-embedding-3-large full dims or Cohere embed-v3
- DEFAULT: text-embedding-3-small, 1536 dims, cosine

## Quality Criteria
- GOOD: Model specified with dimensions and distance metric
- GREAT: Benchmarked on domain data; dimensions justified; chunk_size aligned with chunk_strategy
- FAIL: No dimensions specified; model/index dimension mismatch; no distance metric

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.52 |
| [[bld_knowledge_card_embedding_config]] | sibling | 0.48 |
| [[bld_architecture_embedding_config]] | downstream | 0.46 |
| [[p01_kc_vector_embedding_model_selection]] | sibling | 0.45 |
| [[bld_collaboration_embedding_config]] | downstream | 0.44 |
| [[p01_kc_embedder_provider]] | sibling | 0.44 |
| [[bld_examples_embedding_config]] | downstream | 0.43 |
| [[embedding-config-builder]] | related | 0.42 |
| [[p03_sp_embedding_config_builder]] | downstream | 0.41 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.41 |
