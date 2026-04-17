---
id: kno_vector_store_n04
kind: vector_store
pillar: P01
nucleus: n04
title: N04 Vector Store
version: "1.0.0"
quality: null
tags: [vector_store, n04, qdrant, retrieval, knowledge_gluttony]
backend: qdrant
connection:
  host: localhost
  port: 6333
  api_key_env: null
  tls: false
  database: null
collection: n04_knowledge
dimensions: 3072
distance_metric: cosine
index_type: hnsw
hnsw:
  M: 32
  ef_construction: 256
  ef_search: 128
max_vectors: null
metadata_filtering: true
metadata_schema:
  pillar: keyword
  kind: keyword
  nucleus: keyword
  source_path: keyword
  freshness_days: integer
  tags: keyword_array
persistence: auto
namespace_strategy: pillar_then_kind_then_scope
cloud_region: null
pricing: null
domain: vector_storage
tldr: "Qdrant HNSW store for high-recall N04 semantic search with disciplined metadata filtering."
---
<!-- 8F: F1=vector_store/P01 F2=vector-store-builder F3=nucleus_def_n04+kc_vector_store+N04 env/path config+knowledge lifecycle KC F4=template-first local-first Qdrant profile for dense hungry retrieval
     F5=shell,apply_patch,cex_compile F6=author markdown artifact F7=frontmatter+metric-dimension coherence+ascii+self-check F8=N04_knowledge/P01_knowledge/kno_vector_store_n04.md -->
# Overview
N04 needs a store that can keep many dense vectors without giving up filter discipline.
Knowledge Gluttony pushes toward broad ingestion, but a hungry index becomes noisy if pillar, kind, and freshness boundaries cannot be enforced cheaply at query time.
Qdrant with HNSW is the default backend because it supports strong metadata filtering, straightforward local deployment, and predictable hybrid retrieval growth.

## Boundary
`vector_store` defines where vectors live and how they are indexed.
It does not choose the embedding model or the retrieval orchestration policy.
This artifact assumes embeddings come from `kno_embedder_provider_n04` and are queried by N04 retrieval flows.

## Backend Matrix
| Parameter | Value | Why it serves Knowledge Gluttony |
|-----------|-------|----------------------------------|
| Backend | `qdrant` | scales from local prototyping to larger persistent deployments |
| Version posture | `1.x current stable track` | mature HNSW and filter semantics |
| Host | `localhost:6333` | fast local loop for repository-native indexing |
| Auth | `none by default` | local-first test mode; can add API key later |
| Dimensions | `3072` | matches canonical embedder for maximum semantic detail |
| Distance metric | `cosine` | aligned with normalized dense vectors |
| Index type | `hnsw` | strong recall-speed tradeoff for rich technical corpora |
| Max vectors | `unbounded practical by storage` | no premature cap on knowledge appetite |
| Persistence | `auto` | restart-safe local durability |
| Metadata filtering | `true` | lets N04 search greedily, then narrow precisely |

## Why Qdrant
| Need | Qdrant fit |
|------|------------|
| local-first experimentation | single service, low operational overhead |
| rich filters | payload filters by pillar, kind, tags, freshness |
| HNSW tuning | explicit control over build and search breadth |
| future hybrid search | good posture for dense plus metadata plus rerank |
| graph sidecar use | can hold node description vectors separately |

## Index Configuration
| Parameter | Value | Effect |
|-----------|-------|--------|
| `M` | `32` | denser graph, better recall for semantically close technical artifacts |
| `ef_construction` | `256` | slower build, stronger neighbor quality during indexing |
| `ef_search` | `128` | higher query breadth, fewer missed long-tail matches |

Scale guidance:
- `< 100K` vectors: keep `ef_search=96` for fast interactive queries.
- `100K-5M` vectors: use the stated defaults as the balanced profile.
- `> 5M` vectors: increase `ef_search` selectively for audit and analysis queries.

## Collection Design
| Collection | Purpose | Notes |
|------------|---------|-------|
| `n04_knowledge` | canonical artifact vectors | source of truth for repository knowledge |
| `n04_memory` | learning and runtime memory vectors | same model family for direct comparability |
| `n04_graph_nodes` | node descriptions and summaries | supports graph plus vector joins |
| `n04_staging` | re-embed and migration workspace | never mix with canonical reads |

## Namespace Strategy
1. Partition first by collection scope: `knowledge`, `memory`, `graph_nodes`, `staging`.
2. Filter second by `pillar`, `kind`, and `nucleus` before broad semantic expansion.
3. Keep migration runs in `staging` until dimension and metadata checks pass.
4. Store source paths so retrieval can point back to exact repository evidence.
5. Carry freshness metadata so stale but semantically strong items can be downweighted.

## Lifecycle Operations
1. **Create**: define collection with `3072` dimensions, cosine metric, and HNSW enabled.
2. **Reindex**: rebuild the target collection after chunking or embedding family changes.
3. **Backup**: snapshot persistent storage before bulk deletes or namespace merges.
4. **Restore**: recover snapshots into a new collection, then swap readers after validation.

## Query Posture
| Query type | Filter strategy | Search posture |
|------------|-----------------|----------------|
| exact task routing | filter by `kind` and `nucleus` first | moderate `top_k`, low rerank cost |
| broad knowledge sweep | filter by `pillar` only | higher `top_k`, rerank aggressively |
| memory recall | search `n04_memory` with freshness bias | weight recency and score |
| graph augmentation | query `n04_graph_nodes` from entity seed | join vector hits with graph walk |

## Anti-Patterns
1. Mixing `3072` and reduced vectors inside one collection creates invalid neighborhoods.
2. Using semantic search without metadata filters causes cross-pillar contamination.
3. Reusing the canonical collection during model migration hides drift until retrieval quality drops.
4. Storing every transient log line as a vector inflates cost and weakens signal density.
5. Using low `ef_search` for audit workloads saves milliseconds but loses the rare evidence N04 wants.

## References
1. `archetypes/builders/vector-store-builder/bld_instruction_vector_store.md`
2. `P01_knowledge/library/kind/kc_vector_store.md`
3. `N04_knowledge/P09_config/con_env_config_n04.md`
4. `N04_knowledge/P01_knowledge/knowledge_card_knowledge.md`

## Properties
| Property | Value |
|----------|-------|
| Kind | `vector_store` |
| Pillar | `P01` |
| Nucleus | `n04` |
| Backend | `qdrant` |
| Collection | `n04_knowledge` |
| Dimensions | `3072` |
| Metric | `cosine` |
| Index type | `hnsw` |
| Metadata filtering | `true` |
| Persistence | `auto` |
