---
id: p01_vdb_faiss
kind: vector_store
pillar: P02
nucleus: n07
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: vector-store-builder
backend: faiss
connection:
  host: "localhost"
  port: null
  api_key_env: null
  tls: false
  database: null
collection: "n07_orchestration"
dimensions: 1536
distance_metric: cosine
index_type: ivf
hnsw:
  M: null
  ef_construction: null
  ef_search: null
ivf:
  nlist: 64
  nprobe: 8
  quantizer: flat
max_vectors: 10000
metadata_filtering: true
metadata_schema:
  nucleus: string
  mission: string
  wave: integer
  timestamp: string
  kind: string
8f: F1_constrain
  quality_score: float
persistence: manual
namespace_strategy: "index_per_document_type"
cloud_region: null
pricing: null
domain: vector_storage
quality: 8.8
tags: [vector-store, faiss, ivf, local, n07, orchestration]
tldr: "FAISS IVFFlat -- local, 4 indexes by doc type, 1536d cosine, manual persist to .cex/vectorstore/n07/"
keywords: [faiss, vectordb, ivf, local, orchestration, n07]
linked_artifacts:
  primary: null
  related: [p01_emb_openai_text_embedding_3_small]
data_source: "https://github.com/facebookresearch/faiss/wiki"
related:
  - p01_kc_knowledge_index
  - bld_memory_vector_store
  - knowledge-index-builder
  - bld_knowledge_card_vector_store
  - bld_collaboration_knowledge_index
  - p03_sp_vector_store_builder
  - p01_kc_vector_store
  - p03_ins_vector_store
  - bld_collaboration_embedding_config
  - bld_examples_instruction
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=vector_store, pillar=P01, max_bytes=4096, naming=p01_vdb_faiss.yaml
F2 BECOME: vector-store-builder (13 ISOs). Identity: storage+indexing config for RAG
F3 INJECT: bld_schema + bld_examples (Chroma golden) + bld_memory (FAISS persistence critical)
F4 REASON: FAISS IVFFlat chosen -- corpus 2K-5K docs fits in RAM, zero cost, no network dep.
           Sloth lens: simplest backend that satisfies N07 search SLA. No Qdrant/Pinecone.
           4 indexes by doc type: handoffs, signals, plans, decisions.
           nlist=64 (sqrt(5000)), nprobe=8 (12.5% of nlist) -- good recall/speed tradeoff.
           Dimensions 1536 for text-embedding-3-small; 768 fallback documented.
F5 CALL: compile tool ready
F6 PRODUCE: 1 artifact, body <= 4096 bytes
F7 GOVERN: quality: null, H01-H10 pass
F8 COLLABORATE: saved, compiled
-->

## Boundary

vector_store IS: FAISS IVFFlat index configuration for N07 orchestration corpus (handoffs,
signals, mission plans, decision manifests). Storage and indexing layer only.

vector_store IS NOT: embedder_provider (no model config), retriever (no query pipeline),
agent (no identity), model_provider (no LLM routing).

## Backend Matrix

| Parameter | Value | Source |
|-----------|-------|--------|
| Backend | faiss 1.8.x | https://github.com/facebookresearch/faiss |
| Index Type | IndexIVFFlat (IVFFlat) | https://github.com/facebookresearch/faiss/wiki/Faiss-indexes |
| Host | in-process (no server) | https://github.com/facebookresearch/faiss/wiki |
| Auth | none (local file) | https://github.com/facebookresearch/faiss/wiki |
| Dimensions | 1536 (text-embedding-3-small) | Upstream: p01_emb_openai_text_embedding_3_small |
| Distance Metric | cosine (L2-normalized embeddings) | https://github.com/facebookresearch/faiss/wiki/MetricType |
| Max Vectors | 10000 per index | Corpus estimate: 2K-5K docs per type |
| Persistence | manual (index.write_index / read_index) | https://github.com/facebookresearch/faiss/wiki/Index-IO |
| Metadata Filtering | external (SQLite sidecar, .cex/vectorstore/n07/meta.db) | https://github.com/facebookresearch/faiss/wiki |

## Index Configuration

FAISS IVFFlat uses an inverted file structure: nlist centroids partition the space,
nprobe centroids are searched at query time. No HNSW parameters apply.

| Parameter | Value | Effect |
|-----------|-------|--------|
| nlist | 64 | Voronoi cells. sqrt(5000) rule. More cells = faster search, less recall |
| nprobe | 8 | Cells searched per query. 8/64 = 12.5%. Recall ~95% at this ratio |
| quantizer | IndexFlatL2 | Exact centroid search. Required for IVFFlat (no PQ compression) |
| train_size | >= 64 * 39 = 2496 | IVFFlat requires >= 39 * nlist vectors to train. Must pre-train |

Scale guidance:
- < 1K vectors per index: use IndexFlatIP (brute-force, exact, no training required)
- 1K-10K vectors: IVFFlat with nlist=64, nprobe=8 (this config)
- > 10K vectors: IVFPQx8 for compressed storage, or migrate to Qdrant

**Dimensions fallback:** If embedder is local (768d, e.g. all-MiniLM-L6-v2), rebuild
indexes with dimensions=768. Never mix dimension configs within one index file.

## Namespace Strategy

Four separate FAISS index files, one per N07 document type:

| Collection | Index File | Document Types Included |
|-----------|-----------|------------------------|
| n07_handoffs | .cex/vectorstore/n07/handoffs.index | handoff .md files in .cex/runtime/handoffs/ |
| n07_signals | .cex/vectorstore/n07/signals.index | signal JSON files in .cex/runtime/signals/ |
| n07_plans | .cex/vectorstore/n07/plans.index | mission plan .md files in .cex/runtime/plans/ |
| n07_decisions | .cex/vectorstore/n07/decisions.index | decision_manifest.yaml and decision records |

Rules:
- One index per document type -- cross-type queries use metadata sidecar filtering
- Metadata sidecar (SQLite) maps vector ID -> {nucleus, mission, wave, timestamp, kind, quality_score}
- Never store raw document text in FAISS -- use sidecar or separate document store

## Lifecycle Operations

1. **Train + Create**: Load >= 2496 vectors, call `index.train(vectors)`, then `index.add(vectors)`.
   Use `faiss.IndexFlatL2` as quantizer, wrap with `faiss.IndexIVFFlat(quantizer, 1536, 64)`.

2. **Incremental update**: IVFFlat does not support delete. Append-only: call `index.add(new_vectors)`
   after each new document batch. Sidecar SQLite is append-compatible.

3. **Reindex (full rebuild)**: Triggered by (a) embedder model change, (b) nlist tuning,
   (c) corpus growth past 10K. Re-embed all docs, re-train, re-add, save, replace files.

4. **Backup**: Copy `.cex/vectorstore/n07/*.index` + `meta.db` to `.cex/vectorstore/n07/backup/YYYYMMDD/`.

5. **Restore**: Replace `.cex/vectorstore/n07/` contents from backup directory, reload index
   via `faiss.read_index(path)` at next process start.

6. **Persistence at write time**: Call `faiss.write_index(index, path)` after every add batch.
   FAISS is in-memory -- any omitted write loses all appended vectors on process exit.

## Anti-Patterns

1. Omitting `faiss.write_index()` after upsert -- FAISS is purely in-memory; all new vectors
   lost on process restart. Must persist explicitly after every batch add.

2. Querying before training -- IndexIVFFlat raises `AssertionError: Index not trained`.
   Train with >= nlist * 39 representative vectors before the first add().

3. Setting nprobe = nlist (nprobe=64) -- degrades to brute-force, eliminates IVF speed benefit.
   Target nprobe = 10-15% of nlist for the recall/speed tradeoff.

4. Mixing 1536-dim and 768-dim vectors in the same index file -- FAISS silently accepts mismatched
   dimensions if quantizer was created with wrong d; similarity scores become garbage.

5. Storing all N07 doc types in one index -- cross-type noise contaminates results. Use one index
   per document type with metadata sidecar for cross-type joins.

## References

- FAISS wiki: https://github.com/facebookresearch/faiss/wiki
- FAISS index types: https://github.com/facebookresearch/faiss/wiki/Faiss-indexes
- Index I/O: https://github.com/facebookresearch/faiss/wiki/Index-IO,-cloning-and-hyper-parameter-tuning
- IVF guidelines: https://github.com/facebookresearch/faiss/wiki/Guidelines-to-choose-an-index
- MetricType: https://github.com/facebookresearch/faiss/wiki/MetricType

## Properties

| Property | Value |
|----------|-------|
| Kind | `vector_store` |
| Pillar | P01 |
| Nucleus | N07 |
| Backend | FAISS IVFFlat |
| Domain | vector_storage |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_knowledge_index]] | downstream | 0.40 |
| [[bld_memory_vector_store]] | downstream | 0.40 |
| [[knowledge-index-builder]] | downstream | 0.39 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.38 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.34 |
| [[p03_sp_vector_store_builder]] | downstream | 0.32 |
| [[p01_kc_vector_store]] | upstream | 0.30 |
| [[p03_ins_vector_store]] | downstream | 0.30 |
| [[bld_collaboration_embedding_config]] | downstream | 0.30 |
| [[bld_examples_instruction]] | downstream | 0.30 |
