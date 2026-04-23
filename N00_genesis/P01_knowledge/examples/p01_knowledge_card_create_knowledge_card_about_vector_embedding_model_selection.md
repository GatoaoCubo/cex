---
id: p01_kc_vector_embedding_model_selection
kind: knowledge_card
pillar: P01
title: "Vector Embedding Model Selection Criteria"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "builder"
domain: vector_search
quality: 9.1
tags: [vector-embeddings, model-selection, retrieval, similarity-search, knowledge]
tldr: "Model selection depends on domain match, dimension trade-offs (384-1536), and retrieval task: text-embedding-3-small for speed, text-embedding-ada-002 for cost, sentence-transformers for offline"
when_to_use: "When choosing embedding model for RAG, semantic search, or similarity tasks"
keywords: [embedding-model, vector-search, similarity, retrieval, dimensions]
long_tails:
  - Which embedding model for semantic search in technical documentation
  - How to choose between OpenAI and sentence-transformers embeddings
  - Embedding dimension impact on retrieval accuracy vs speed
axioms:
  - ALWAYS benchmark on your specific domain before production deployment
  - NEVER use embeddings trained on different language than your content
  - IF retrieval latency > 100ms THEN use models with <= 512 dimensions
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 0.89
data_source: "https://openai.com/blog/new-embedding-models, https://huggingface.co/spaces/mteb/leaderboard"
related:
  - p01_emb_openai_text_embedding_3_small
  - p06_schema_embedding
  - p01_kc_embedder_provider
  - bld_knowledge_card_embedding_config
  - p01_kc_embedding_config
  - bld_collaboration_embedding_config
  - n01_emb_text_embedding_4
  - bld_examples_embedder_provider
  - p01_gl_embedding
  - embedding-config-builder
---
# Vector Embedding Model Selection Criteria

## Quick Reference
```yaml
topic: embedding_model_selection
scope: Model choice for semantic retrieval tasks
owner: vector_search_engineer
criticality: high
```

## Key Concepts
- **Dimension Trade-off**: Higher dimensions (1536) = better accuracy, lower speed; 384-512 dimensions balance both
- **Domain Specialization**: Models trained on code (CodeBERT), legal (LegalBERT), or general web text show 15-30% accuracy difference
- **Retrieval Metrics**: Recall@10 measures relevance; latency measured as embedding_time + search_time
- **Context Window**: OpenAI text-embedding-3 handles 8192 tokens; sentence-transformers typically 512 tokens max

## Strategy Phases
1. **Benchmark**: Test top 3 models on 100+ query-document pairs from your domain
2. **Measure**: Record Recall@10, MRR@10, embedding latency, storage size per vector
3. **Cost Analysis**: OpenAI pricing vs local inference costs (GPU memory, compute time)
4. **Scale Test**: Evaluate performance with your expected vector database size (1M+ documents)
5. **Deploy**: Start with proven model, A/B test improvements using retrieval metrics

## Golden Rules
- CHOOSE text-embedding-3-small for general English text with speed priority
- EVALUATE sentence-transformers/all-MiniLM-L6-v2 for cost-sensitive offline deployments
- BENCHMARK domain-specific models (e.g., SciBERT for papers) against general models
- MONITOR retrieval quality degradation when switching models in production

## Flow
```text
[Content Type] -> [Domain Analysis] -> [Candidate Models]
                                           |
                    [Benchmark Suite] -> [Metrics Collection]
                                           |
                    [Cost vs Quality] -> [Model Selection] -> [Deploy]
```

## Comparativo
| Model | Dimensions | Recall@10 | Latency | Cost | Best For |
|-------|------------|-----------|---------|------|----------|
| text-embedding-3-large | 3072 | 0.94 | 45ms | $0.13/1M | High accuracy retrieval |
| text-embedding-3-small | 1536 | 0.89 | 22ms | $0.02/1M | Balanced speed/quality |
| text-embedding-ada-002 | 1536 | 0.85 | 28ms | $0.10/1M | Legacy compatibility |
| all-MiniLM-L6-v2 | 384 | 0.82 | 8ms | Free | Local/offline deployment |
| E5-large-v2 | 1024 | 0.90 | 35ms | Free | Open source production |

## References
- OpenAI Embedding Models: https://openai.com/blog/new-embedding-models
- MTEB Leaderboard: https://huggingface.co/spaces/mteb/leaderboard
- Related: p01_kc_rag_fundamentals (retrieval pipeline context)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.45 |
| [[p06_schema_embedding]] | downstream | 0.40 |
| [[p01_kc_embedder_provider]] | sibling | 0.39 |
| [[bld_knowledge_card_embedding_config]] | sibling | 0.39 |
| [[p01_kc_embedding_config]] | sibling | 0.37 |
| [[bld_collaboration_embedding_config]] | downstream | 0.35 |
| [[n01_emb_text_embedding_4]] | related | 0.34 |
| [[bld_examples_embedder_provider]] | downstream | 0.34 |
| [[p01_gl_embedding]] | related | 0.32 |
| [[embedding-config-builder]] | related | 0.32 |
