---
id: n01_emb_text_embedding_4
kind: embedding_config
pillar: P01
title: "Embedding Config for N01 RAG"
version: "1.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
model_name: "text-embedding-004"
provider: "Google"
dimensions: 768
chunk_size: 512
chunk_overlap: 64
quality: 9.1
tags: [embedding, config, n01, rag, memory, vector]
tldr: "Specifies the text-embedding-004 model with 768 dimensions for N01's RAG knowledge base."
density_score: 0.99
related:
  - p01_kc_rag_chunking_strategies
  - p01_kc_vector_embedding_model_selection
  - p01_emb_openai_text_embedding_3_small
  - p01_emb_nomic_embed_text
  - bld_instruction_embedding_config
  - p06_schema_embedding
  - bld_knowledge_card_embedding_config
  - n04_rc_knowledge
  - p01_gl_embedding
  - bld_knowledge_card_chunk_strategy
---

## Purpose
This document defines the standard vector embedding model and chunking strategy for all documents ingested into the **N01 Intelligence Nucleus** knowledge base. This configuration is critical for the performance and accuracy of its Retrieval-Augmented Generation (RAG) capabilities.

## Model Rationale

| Attribute | Value | Justification |
|-----------|-------|---------------|
| **Model** | `text-embedding-004` | State-of-the-art on MTEB benchmark |
| **Provider** | Google | Native integration with `gemini-2.5-pro` |
| **Dimensions** | 768 | Rich semantic representation, efficient search |
| **Context Length** | 8,192 tokens | Handles long documents without truncation |
| **Performance** | Top 3 on MTEB | Proven accuracy on diverse text types |
| **Compatibility** | Gemini ecosystem | Reduces API latency, shared tokenization |

## Chunking Strategy
- **Chunk Size**: `512 tokens`
- **Overlap**: `64 tokens`
- **Reasoning**: A chunk size of 512 tokens is chosen as an optimal balance between two competing needs:
    1.  **Contextual Richness**: Chunks must be large enough to contain complete semantic units (paragraphs, concepts).
    2.  **Vector Specificity**: Chunks must be small enough so that the resulting vector accurately represents a specific piece of information.
- The 64-token overlap ensures that semantic context is not lost at the boundaries between chunks, improving the retriever's ability to find relevant passages that span across chunk divisions.

## Performance Benchmarks

| Metric | Target | Validation Method |
|--------|--------|-------------------|
| Embedding latency | < 200ms per chunk | `time.time()` around embed call |
| Retrieval accuracy | > 85% @ k=5 | Manual eval on 50 test queries |
| Vector similarity | > 0.7 for duplicates | Cosine similarity on known pairs |
| Memory usage | < 2GB for 10K docs | `psutil.memory_info()` |
| Index build time | < 5min for 1K docs | End-to-end pipeline timing |

**Validation Commands:**
```bash
python _tools/embedding_benchmark.py --config n01_emb_text_embedding_4
python _tools/rag_accuracy_test.py --threshold 0.85
```

## Usage Guidelines

**When to Use:**
- Research papers and academic documents (optimal for technical content)
- Market intelligence reports (handles domain-specific terminology)
- Competitor analysis documents (preserves comparative context)
- Long-form industry whitepapers (maintains semantic coherence)

**When NOT to Use:**
- Real-time data feeds (embedding latency unsuitable)
- Documents under 200 tokens (overhead exceeds benefit)
- Highly structured data like spreadsheets (use database indexing instead)
- Code repositories (use specialized code embeddings)

**Implementation Example:**
```python
config = {
    "model": "text-embedding-004",
    "chunk_size": 512,
    "chunk_overlap": 64,
    "max_retries": 3
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_rag_chunking_strategies]] | related | 0.35 |
| [[p01_kc_vector_embedding_model_selection]] | related | 0.34 |
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.34 |
| [[p01_emb_nomic_embed_text]] | sibling | 0.32 |
| [[bld_instruction_embedding_config]] | downstream | 0.32 |
| [[p06_schema_embedding]] | downstream | 0.32 |
| [[bld_knowledge_card_embedding_config]] | related | 0.31 |
| [[n04_rc_knowledge]] | related | 0.31 |
| [[p01_gl_embedding]] | related | 0.31 |
| [[bld_knowledge_card_chunk_strategy]] | related | 0.30 |
