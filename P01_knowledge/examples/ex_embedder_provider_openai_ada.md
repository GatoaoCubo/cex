---
id: p01_emb_openai_text_embedding_3_small
kind: embedder_provider
pillar: P01
title: "Example — OpenAI text-embedding-3-small Provider"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
provider: openai
model: text-embedding-3-small
dimensions: 1536
max_tokens: 8191
batch_size: 100
normalize: true
api_key_env: OPENAI_API_KEY
domain: embedder_provider
quality: 9.1
tags: [embedder-provider, openai, text-embedding-3, vector, rag]
tldr: "OpenAI text-embedding-3-small config — 1536 dims (reducible to 256), $0.02/1M tokens, 8191 max input, L2-normalized."
when_to_use: "Default cloud embedder for CEX RAG when OpenAI API is available and cost is acceptable"
keywords: [openai, embedding, text-embedding-3-small, vector, rag]
density_score: null
---

# Embedder Provider: OpenAI text-embedding-3-small

## Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| provider | openai | Widely available, strong MTEB scores |
| model | text-embedding-3-small | Best cost/quality ratio in OpenAI lineup |
| dimensions | 1536 | Native output; reducible to 256/512/1024 via `dimensions` param |
| max_tokens | 8191 | Model hard limit per chunk |
| batch_size | 100 | Stays within rate limits; ~2s per batch |
| normalize | true | L2-normalize for cosine similarity |
| api_key_env | OPENAI_API_KEY | Env var, never hardcoded |

## Dimension Reduction (Matryoshka)
| Dimensions | Index Size (10K docs) | MTEB Score | Use Case |
|------------|----------------------|------------|----------|
| 1536 | ~58 MB | 62.3 | Production quality |
| 1024 | ~39 MB | 61.8 | Balanced |
| 512 | ~19 MB | 60.9 | Memory-constrained |
| 256 | ~10 MB | 59.2 | Mobile/edge |

## Pricing
| Metric | Value |
|--------|-------|
| Cost per 1M tokens | $0.02 |
| Cost per 10K documents (~500 tokens avg) | $0.10 |
| Full CEX reindex (~2184 docs) | ~$0.02 |

## API Call
```python
from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=["chunk text here"],
    dimensions=1536  # or 256/512/1024
)
vector = response.data[0].embedding
```

## Comparison to Alternatives
| Model | Provider | Dims | Cost/1M | MTEB | Local |
|-------|----------|------|---------|------|-------|
| **text-embedding-3-small** | **openai** | **1536** | **$0.02** | **62.3** | **no** |
| text-embedding-3-large | openai | 3072 | $0.13 | 64.6 | no |
| embed-english-v3.0 | cohere | 1024 | $0.10 | 64.5 | no |
| voyage-3 | voyage | 1024 | $0.06 | 67.1 | no |
| nomic-embed-text | ollama | 768 | $0 | 62.4 | yes |

## Boundary
embedder_provider IS: connection config for an embedding API with model, dimensions, and batching.
embedder_provider IS NOT: a vector store config (vector_store), a chunk strategy, or a retriever pipeline.
