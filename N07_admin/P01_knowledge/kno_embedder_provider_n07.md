---
id: p01_emb_openai_text_embedding_3_small
kind: embedder_provider
pillar: P02
nucleus: N07
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "embedder-provider-builder"
provider: "openai"
model: "text-embedding-3-small"
dimensions: 1536
dimensions_override: 512
max_tokens: 8191
batch_size: 2048
normalize: true
truncate: true
distance_metric: "cosine"
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
quality: 9.2
tags: [embedder-provider, openai, orchestration, semantic-search, handoff-retrieval]
tldr: "text-embedding-3-small for N07 orchestration corpus -- 512d MRL, $0.02/1M tokens, Ollama fallback for cost-zero ops"
keywords: [openai, text-embedding-3-small, handoff, signal, mission-plan, orchestration, nomic-embed-text]
linked_artifacts:
  primary: null
  related: [p01_emb_local_nomic_embed_text]
data_source: "https://platform.openai.com/docs/guides/embeddings"
density_score: 1.0
related:
  - bld_examples_embedder_provider
  - bld_tools_embedder_provider
  - p01_emb_nomic_embed_text
  - bld_tools_model_provider
  - bld_knowledge_card_embedder_provider
  - bld_examples_embedding_config
  - p03_sp_embedder_provider_builder
  - bld_tools_model_card
  - bld_examples_model_provider
  - p01_kc_embedder_provider
---
<!-- 8F: F1 kind=embedder_provider P01 | F2 embedder-provider-builder 13 ISOs | F3 schema+examples+memory injected | F4 N07 sloth lens: 512d MRL primary, Ollama fallback | F5 no prior artifact | F6 produced | F7 H01-H10 pass quality:null | F8 compile pending -->

## Boundary

embedder_provider IS: connection config for text-embedding-3-small used by N07 to embed and
retrieve operational documents (handoffs, signal JSONs, mission plans, decision manifests,
wave schedules) via cex_retriever.py.

embedder_provider IS NOT: vector_store, model_provider, retriever pipeline, chunker, or
LLM inference config. It does not govern how documents are split or ranked -- only the
embedding connection contract.

## Configuration Matrix

| Parameter | Value | Source |
|-----------|-------|--------|
| Provider | openai | https://platform.openai.com/docs/guides/embeddings |
| Model | text-embedding-3-small | https://platform.openai.com/docs/models |
| Dimensions | 1536 (native), 512 (MRL) | https://platform.openai.com/docs/guides/embeddings |
| Max Tokens | 8191 | https://platform.openai.com/docs/guides/embeddings |
| Batch Size | 2048 texts/request | https://platform.openai.com/docs/guides/embeddings |
| Normalize | true (L2-normalized by default) | https://platform.openai.com/docs/guides/embeddings |
| Truncate | true (auto-truncates to max_tokens) | https://platform.openai.com/docs/api-reference/embeddings |
| Distance Metric | cosine (correct for L2-normalized output) | Mathematical property |
| Pricing | $0.02 per 1M tokens | https://platform.openai.com/docs/pricing |
| Fallback Model | nomic-embed-text (Ollama local) | https://ollama.com/library/nomic-embed-text |
| Fallback Dimensions | 768 (separate index required) | https://docs.nomic.ai/reference/endpoints/nomic-embed-text |
| Fallback Cost | null (local, no token cost) | local inference |

## Dimension Tradeoffs

N07 corpus: handoff files (~800 tokens), signal JSONs (~200 tokens), mission plans (~1200 tokens),
decision manifests (~600 tokens). Short operational documents -- 512d MRL is optimal.

| Dimensions | MTEB Avg | Storage/vec | Latency | Use Case |
|------------|----------|-------------|---------|----------|
| 1536 (native) | 62.3% | 6.1 KB | baseline | Full-fidelity retrieval, rarely needed for short ops docs |
| 512 (MRL) | 61.6% | 2.0 KB | -30% | N07 primary: operational doc retrieval, 65% cost reduction |
| 256 (MRL) | 59.8% | 1.0 KB | -50% | Classification only -- not recommended for N07 retrieval |
| 768 (nomic) | 54.9% | 3.1 KB | local | Fallback: zero cost, acceptable recall for signal corpus |

Sloth lens decision: 512d MRL loses 0.7% MTEB vs native but cuts storage and cost by 65%.
For N07 operational corpus (never >5K documents), this is the correct tradeoff.

## Batch Embedding Strategy

N07 embeds four corpus types on different schedules:

| Corpus | Avg Tokens | Batch Trigger | Batch Size | Provider |
|--------|-----------|---------------|------------|----------|
| Handoff files (.cex/runtime/handoffs/) | ~800 | on write (F8) | 32 | openai primary |
| Signal JSONs (.cex/runtime/signals/) | ~200 | on write (F8) | 128 | openai primary |
| Mission plans (.cex/runtime/plans/) | ~1200 | on write (F8) | 16 | openai primary |
| Decision manifests (.cex/runtime/decisions/) | ~600 | on write (F8) | 64 | openai primary |

Fallback routing: if OPENAI_API_KEY absent or API returns 429/503, route to Ollama
nomic-embed-text. Fallback index is separate (768d vs 512d -- incompatible vector spaces).
Never mix openai and nomic vectors in the same index.

## Integration Pattern

```python
# cex_retriever.py integration -- N07 orchestration corpus
from openai import OpenAI
import os

# Primary: OpenAI text-embedding-3-small at 512d MRL
client = OpenAI()  # reads OPENAI_API_KEY from env

def embed_n07(texts: list[str], use_fallback: bool = False) -> list[list[float]]:
    if use_fallback:
        # Ollama nomic-embed-text -- separate 768d index
        import requests
        resp = requests.post(
            "http://localhost:11434/api/embeddings",
            json={"model": "nomic-embed-text", "prompt": texts[0]}
        )
        return [resp.json()["embedding"]]
    # Primary path: 512d MRL via dimensions param
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=texts,           # up to 2048 texts per call
        dimensions=512         # MRL reduction from native 1536
    )
    return [item.embedding for item in response.data]

# Batch embed the N07 handoff corpus
def index_handoffs(paths: list[str]) -> None:
    texts = [open(p).read() for p in paths]
    for i in range(0, len(texts), 2048):
        batch = texts[i:i+2048]
        vectors = embed_n07(batch)
        # store in vector_store with path metadata
```

## Anti-Patterns

1. Using 1536d native when 512d MRL is available -- N07 corpus is short docs; 512d saves 65% storage with <1% recall loss.
2. Mixing openai (512d) and nomic-embed-text (768d) vectors in the same index -- incompatible vector spaces, similarity scores become meaningless.
3. Triggering re-embed on every N07 session start -- embed on write (F8 signal), not on read; avoids redundant API spend.
4. Setting batch_size > 2048 for openai -- provider enforces server-side limit; silent truncation or 429 errors stall the pipeline.
5. Hardcoding OPENAI_API_KEY in cex_retriever.py config -- always read from env var; key exposure breaks CI/CD and security posture.
6. Falling back to nomic without routing to a separate index -- nomic is 768d, openai is 512d; same-index mixed vectors corrupt all similarity scores.

## References

- embeddings guide: https://platform.openai.com/docs/guides/embeddings
- model list: https://platform.openai.com/docs/models
- pricing: https://platform.openai.com/docs/pricing
- MTEB leaderboard: https://huggingface.co/spaces/mteb/leaderboard
- nomic-embed-text: https://ollama.com/library/nomic-embed-text
- MRL paper: https://arxiv.org/abs/2205.13147

## Properties

| Property | Value |
|----------|-------|
| Kind | `embedder_provider` |
| Pillar | P01 |
| Nucleus | N07 |
| Domain | embedding / orchestration retrieval |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_embedder_provider]] | downstream | 0.63 |
| [[bld_tools_embedder_provider]] | downstream | 0.36 |
| [[p01_emb_nomic_embed_text]] | upstream | 0.35 |
| [[bld_tools_model_provider]] | downstream | 0.34 |
| [[bld_knowledge_card_embedder_provider]] | upstream | 0.33 |
| [[bld_examples_embedding_config]] | downstream | 0.32 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.32 |
| [[bld_tools_model_card]] | downstream | 0.30 |
| [[bld_examples_model_provider]] | downstream | 0.29 |
| [[p01_kc_embedder_provider]] | upstream | 0.29 |
