---
kind: examples
id: bld_examples_embedder_provider
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of embedder_provider artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Embedder Provider"
version: "1.0.0"
author: n03_builder
tags: [embedder_provider, builder, examples]
tldr: "Golden and anti-examples for embedder provider construction, demonstrating ideal structure and common pitfalls."
domain: "embedder provider construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: embedder-provider-builder
## Golden Example
INPUT: "Configure OpenAI text-embedding-3-small for semantic search"
OUTPUT:
```yaml
id: p01_emb_openai_text_embedding_3_small
kind: embedder_provider
pillar: P01
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
provider: "openai"
model: "text-embedding-3-small"
dimensions: 1536
dimensions_override: null
max_tokens: 8191
batch_size: 2048
normalize: true
truncate: true
distance_metric: cosine
matryoshka: true
sparse_support: false
api_key_env: "OPENAI_API_KEY"
api_base_url: null
pricing:
  per_1m_tokens: 0.02
  per_request: null
  currency: USD
mteb_score: 62.3
domain: embedding
quality: null
tags: [embedder-provider, openai, text-embedding-3, semantic-search]
tldr: "text-embedding-3-small — openai, 1536d (MRL to 512), $0.02/1M tokens, best cost/quality for semantic search"
keywords: [openai, text-embedding-3-small, semantic-search, matryoshka]
linked_artifacts:
  primary: null
  related: [p01_emb_openai_text_embedding_3_large]
data_source: "https://platform.openai.com/docs/guides/embeddings"
## Boundary
embedder_provider IS: connection config for text-embedding-3-small (dimensions, normalization, batch limits).
embedder_provider IS NOT: vector_store, model_provider, retriever, chunker.
## Configuration Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | openai | https://platform.openai.com/docs/guides/embeddings |
| Model | text-embedding-3-small | https://platform.openai.com/docs/models |
| Dimensions | 1536 (native), 512 (reduced) | https://platform.openai.com/docs/guides/embeddings |
| Max Tokens | 8191 | https://platform.openai.com/docs/guides/embeddings |
| Batch Size | 2048 texts/request | https://platform.openai.com/docs/guides/embeddings |
| Normalize | true (L2-normalized by default) | https://platform.openai.com/docs/guides/embeddings |
| Truncate | true (auto-truncates to max_tokens) | https://platform.openai.com/docs/api-reference/embeddings |
| Distance Metric | cosine (normalized vectors) | Mathematical property |
| Pricing | $0.02 per 1M tokens | https://platform.openai.com/docs/pricing |
## Dimension Tradeoffs
| Dimensions | MTEB Avg | Storage/vec | Latency | Use Case |
|------------|----------|-------------|---------|----------|
| 1536 (native) | 62.3% | 6.1 KB | baseline | High-accuracy semantic search |
| 512 (MRL) | 61.6% | 2.0 KB | -30% | Cost-optimized search, large corpora |
| 256 (MRL) | 59.8% | 1.0 KB | -50% | Classification, clustering |
## Integration Pattern
```python
from openai import OpenAI
client = OpenAI()  # uses OPENAI_API_KEY env var
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=["query text"],
    dimensions=1536  # or 512 for MRL reduction
)
vector = response.data[0].embedding  # len == dimensions
```
## Anti-Patterns
1. Mixing text-embedding-3-small with text-embedding-ada-002 in the same index — incompatible vector spaces
2. Setting dimensions=512 without matryoshka support verification — produces zero-padded garbage
3. Exceeding 8191 tokens without truncation — API silently truncates, losing document tail
4. Using dot_product distance with normalized vectors — cosine is correct for L2-normalized output
## References
- embeddings: https://platform.openai.com/docs/guides/embeddings
- models: https://platform.openai.com/docs/models
- pricing: https://platform.openai.com/docs/pricing
```
WHY THIS IS GOLDEN:
- Every Configuration row has Source URL (never `-`)
- Dimensions are exact integers from official docs
- normalize is boolean, not string
- Pricing concrete: $0.02/1M tokens
- quality: null
- Matryoshka tradeoff table with concrete MTEB scores
- Integration code uses environment variable, not hardcoded key
## Anti-Example
INPUT: "Configure Cohere embeddings"
BAD OUTPUT:
```yaml
id: cohere_embedder
kind: embedder
provider: Cohere
dimensions: "1024"
normalize: "yes"
api_key: "sk-abc123..."
quality: 9.0
Cohere offers excellent embeddings. Their model is one of the best
for semantic search. Simply call the API with your text.
```
FAILURES:
1. id: no `p01_emb_` prefix — H02 FAIL
2. kind: "embedder" not "embedder_provider" — H04 FAIL
3. provider: uppercase — H07 FAIL
4. dimensions: string not integer — H08 FAIL
5. normalize: string "yes" not boolean — H09 FAIL
6. api_key: hardcoded secret — SECURITY VIOLATION
7. quality: self-assigned 9.0 — H05 FAIL
8. Body: marketing prose, no Configuration Matrix — S07 FAIL
9. No Source URLs in body — density FAIL
