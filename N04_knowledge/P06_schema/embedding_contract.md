---
id: p06_schema_embedding
kind: schema
pillar: P06
title: "Embedding Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [schema, n04, embedding, vector, chunking, rag, similarity]
tldr: "Embedding config: model, dimensions, chunking strategy (fixed/semantic/sentence), similarity threshold, index type."
density_score: 0.93
---

# Embedding Contract

## Model Options

| Model | Provider | Dimensions | Cost | Quality |
|-------|----------|-----------|------|---------|
| text-embedding-3-small | OpenAI | 1536 | Low | Good |
| text-embedding-3-large | OpenAI | 3072 | Medium | Best |
| embed-english-v3.0 | Cohere | 1024 | Low | Good |
| gecko | Google | 768 | Free (quota) | Good |

## Chunking Strategy

| Strategy | Chunk Size | Overlap | Best For |
|----------|-----------|---------|----------|
| Fixed | 500 tokens | 50 | General KCs |
| Semantic | By H2 section | Headers | Structured KCs with clear sections |
| Sentence-window | 1 sentence + 2 context | Full sentence | QA retrieval |

## Similarity Threshold

| Score | Interpretation | Action |
|-------|---------------|--------|
| >= 0.85 | Strong match | Include in prompt |
| 0.70-0.84 | Relevant | Include if budget allows |
| < 0.70 | Weak | Exclude |

## Selection Criteria

| Requirement | Model Choice | Chunking | Threshold |
|-------------|--------------|----------|-----------|
| Cost-sensitive prototype | gecko | fixed | 0.70 |
| Production RAG system | text-embedding-3-large | semantic | 0.75 |
| QA over docs | text-embedding-3-small | sentence-window | 0.80 |
| Large knowledge base | embed-english-v3.0 | fixed | 0.70 |

## Default Config
```yaml
model: text-embedding-3-small
dimensions: 1536
chunking: semantic
chunk_max_tokens: 500
overlap_tokens: 50
similarity_threshold: 0.70
index_type: ivfflat
distance_metric: cosine
```