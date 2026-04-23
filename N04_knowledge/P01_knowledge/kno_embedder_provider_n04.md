---
id: kno_embedder_provider_n04
kind: embedder_provider
pillar: P02
nucleus: n04
title: N04 Embedder Provider
version: "1.0.0"
quality: 9.1
tags: [embedder_provider, n04, rag, embeddings, knowledge_gluttony]
provider: openai
model: text-embedding-3-large
dimensions: 3072
dimensions_override: 1024
max_tokens: 8191
batch_size: 96
normalize: true
truncate: end
distance_metric: cosine
matryoshka: true
sparse_support: false
api_key_env: OPENAI_API_KEY
api_base_url: https://api.openai.com/v1
domain: rag_indexing
tldr: "High-fidelity dense embedder for N04 retrieval, graph augmentation, and memory recall."
density_score: 1.0
related:
  - bld_collaboration_knowledge_graph
  - p01_kc_embedder_provider
  - bld_examples_embedder_provider
  - p01_emb_openai_text_embedding_3_small
  - bld_collaboration_embedder_provider
  - p03_sp_embedder_provider_builder
  - agent_card_n04
  - bld_memory_embedder_provider
  - p03_ins_embedder_provider
  - bld_collaboration_vector_store
---
<!-- 8F: F1=embedder_provider/P01 F2=embedder-provider-builder F3=nucleus_def_n04+P01/P10 schema+kc_embedder_provider+N04 configs F4=template-first OpenAI dense retrieval profile for knowledge-hungry N04
     F5=shell,apply_patch,cex_compile F6=author markdown artifact F7=frontmatter+ascii+line-count+self-check F8=N04_knowledge/P01_knowledge/kno_embedder_provider_n04.md -->
# Overview
N04 needs an embedder that rewards breadth without collapsing precision.
Knowledge Gluttony means indexing more domains, more entity variants, and more relation hints, but every extra chunk only helps if its vector remains comparable across the whole corpus.
`text-embedding-3-large` is the default hungry profile because it preserves nuance for multilingual technical markdown, taxonomy labels, memory summaries, and graph node descriptions.
The provider profile favors recall first, then reranking and graph traversal for discipline.

## Boundary
`embedder_provider` IS the contract for text-to-vector conversion.
`embedder_provider` IS NOT the vector backend, retriever policy, or graph schema.
N04 uses this artifact to keep chunk embeddings, entity embeddings, and memory embeddings aligned under one semantic geometry.

## Configuration Matrix
| Parameter | Value | Why it serves Knowledge Gluttony |
|-----------|-------|----------------------------------|
| Provider | `openai` | stable API and broad ecosystem coverage |
| Model | `text-embedding-3-large` | richer semantic capacity than smaller dense options |
| Native dimensions | `3072` | preserves detail for long-tail domain distinctions |
| Reduced dimensions | `1024` | supports lower-cost side indexes without model drift |
| Max tokens | `8191` | lets N04 keep semantically complete chunks |
| Batch size | `96` texts/request | balances throughput and provider headroom |
| Normalize | `true` | keeps cosine space stable across mixed corpora |
| Truncate | `end` | preserves leading taxonomy and title context |
| Distance metric | `cosine` | aligns with normalized vectors and mixed-length chunks |
| Sparse support | `false` | dense provider; lexical recall handled elsewhere |
| API key env | `OPENAI_API_KEY` | explicit auth boundary |
| Base URL | `https://api.openai.com/v1` | standard endpoint for shared tooling |

## Why This Model
N04 indexes repository markdown, schema notes, memory summaries, runtime configs, and graph node descriptions.
These materials are dense, domain-heavy, and often short enough that subtle phrasing matters.
A hungry knowledge nucleus benefits more from semantic resolution than from absolute token thrift.
The large profile is therefore the primary index embedder, while dimension reduction remains available for secondary caches.

## Dimension Tradeoffs
| Dimensions | Recall posture | Storage posture | Latency posture | Recommended use |
|------------|----------------|-----------------|-----------------|-----------------|
| `3072` | maximum semantic appetite | highest footprint | baseline | canonical knowledge and memory index |
| `2048` | high recall with modest loss | lower than native | slightly faster | graph node sidecar embeddings |
| `1024` | balanced | medium | faster | experimentation, local mirrors, previews |
| `512` | selective | compact | fastest | coarse routing only, not canonical search |

## Corpus Fit
| Corpus slice | Embedding goal | Notes |
|-------------|----------------|-------|
| knowledge artifacts | preserve domain distinctions | prioritize taxonomic and architectural nuance |
| memory artifacts | recall decisions and lessons | temporal context matters more than phrasing exactness |
| graph nodes | support hybrid graph plus vector retrieval | entity descriptions should live in same vector family |
| schema docs | cluster related constraints | helps route tasks to the right builder quickly |
| configs | identify operational adjacency | useful for cross-artifact retrieval, not exact matching |

## Integration Pattern
```python
from openai import OpenAI

client = OpenAI()

def embed_texts(texts, dimensions=3072):
    response = client.embeddings.create(
        model="text-embedding-3-large",
        input=texts,
        dimensions=dimensions,
    )
    return [item.embedding for item in response.data]
```

## Retrieval Heuristics
1. Embed titles plus body for short artifacts where naming carries routing signal.
2. Keep chunk headers attached because N04 artifacts compress heavy meaning into section names.
3. Use `3072` for canonical storage whenever a corpus may feed memory or graph enrichment later.
4. Use `1024` only for derivative indexes, never by mixing inside the primary namespace.
5. Re-embed the entire namespace on model family change, not incrementally.

## Anti-Patterns
1. Mixing `text-embedding-3-large` and unrelated legacy vectors in one collection causes false neighborhoods.
2. Downshifting dimensions per document instead of per index breaks similarity consistency.
3. Embedding raw boilerplate headings without body context inflates low-value hubs.
4. Treating embeddings as a substitute for taxonomy weakens controllability.
5. Using one giant chunk to capture "everything known" creates vague vectors and shallow recall.

## Operational Notes
| Concern | N04 stance |
|---------|------------|
| cost pressure | reduce dimensions in derivative indexes before changing model family |
| freshness | re-embed after chunking strategy changes or metadata packing changes |
| multilingual content | keep language markers in chunk metadata, not in vector families |
| graph alignment | reuse same model for entity descriptions and source chunks |
| memory alignment | runtime and learning artifacts should stay in same vector geometry |

## References
1. `archetypes/builders/embedder-provider-builder/bld_instruction_embedder_provider.md`
2. `P01_knowledge/library/kind/kc_embedder_provider.md`
3. `N04_knowledge/architecture/nucleus_def_n04.md`
4. `N04_knowledge/P09_config/con_env_config_n04.md`

## Properties
| Property | Value |
|----------|-------|
| Kind | `embedder_provider` |
| Pillar | `P01` |
| Nucleus | `n04` |
| Model family | `text-embedding-3` |
| Canonical dimensions | `3072` |
| Reduced profile | `1024` |
| Metric | `cosine` |
| Primary optimization | recall under dense technical corpora |
| Memory compatibility | yes |
| Graph compatibility | yes |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_knowledge_graph]] | downstream | 0.37 |
| [[p01_kc_embedder_provider]] | upstream | 0.35 |
| [[bld_examples_embedder_provider]] | downstream | 0.34 |
| [[p01_emb_openai_text_embedding_3_small]] | sibling | 0.31 |
| [[bld_collaboration_embedder_provider]] | related | 0.30 |
| [[p03_sp_embedder_provider_builder]] | downstream | 0.29 |
| [[agent_card_n04]] | upstream | 0.29 |
| [[bld_memory_embedder_provider]] | downstream | 0.28 |
| [[p03_ins_embedder_provider]] | downstream | 0.28 |
| [[bld_collaboration_vector_store]] | related | 0.28 |
