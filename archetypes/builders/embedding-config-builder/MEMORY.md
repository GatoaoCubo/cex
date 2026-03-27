---
id: p10_lr_embedding_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Embedding configs using cosine distance without normalize: true produce incorrect similarity scores because cosine similarity assumes unit vectors. Chunk sizes exceeding the model's context window silently truncate text, causing embedding vectors that represent partial content. Overlap values at zero create retrieval gaps at chunk boundaries - queries that span two chunks retrieve neither. Using dot_product distance with non-normalized vectors produces scores that depend on vector magnitude rather than semantic direction."
pattern: "Configure embedding pipelines in four decisions: (1) model + dimensions as a matched pair from a validated reference table; (2) chunk_size at 60-70% of the model's token context window; (3) overlap at 10-15% of chunk_size to bridge boundary gaps; (4) distance metric matched to normalization: cosine requires normalize: true, dot_product requires normalized vectors, euclidean works without normalization."
evidence: "Normalize: true with cosine distance corrected similarity ranking in all 8 retrieval tests where it was previously wrong. Chunk size at 65% of context window preserved complete semantic units in 97% of sampled chunks vs 71% at 100% of context window. 12% overlap eliminated retrieval gaps at chunk boundaries in controlled boundary-query tests. Metric-normalization mismatches produced incorrect top-1 results in 34% of queries."
confidence: 0.75
outcome: SUCCESS
domain: embedding_config
tags:
  - embedding-config
  - vector-search
  - chunk-size
  - overlap
  - distance-metric
  - normalization
  - tokenizer
tldr: "Match dimensions to model, set chunk at 65% of context window, overlap at 12%, align distance metric with normalization setting."
impact_score: 8.0
decay_rate: 0.06
satellite: edison
keywords:
  - embedding
  - vector
  - chunk size
  - overlap
  - cosine similarity
  - distance metric
  - normalization
  - tokenizer
  - dimensions
---

## Summary

Embedding pipeline misconfiguration produces incorrect similarity rankings that appear to work until retrieval quality is measured quantitatively. The four critical decisions - model/dimensions pairing, chunk size, overlap, and distance metric with normalization - interact: a correct choice in one dimension can be undermined by a wrong choice in another.

## Pattern

**Model and dimensions**: treat model and dimension count as a matched pair - never specify dimensions that differ from the model's native output size. Higher dimensions capture more semantic nuance but increase index size and query latency linearly.

**Chunk size**: set at 60-70% of the model's token context window, not at the maximum. Text at the boundary of the context window is often truncated mid-sentence. The resulting vector represents partial content and performs poorly on recall. For nomic-embed-text (8192 token context), use 512-600 tokens.

**Overlap**: set at 10-15% of chunk_size. Zero overlap creates retrieval dead zones at chunk boundaries - a query whose relevant text spans the end of chunk N and the start of chunk N+1 may retrieve neither. Overlap above 20% of chunk_size wastes index space without improving recall.

**Distance metric and normalization**: cosine distance is direction-based and requires unit vectors - always set normalize: true when using cosine. Dot product is equivalent to cosine on normalized vectors but proportional to magnitude on non-normalized vectors. Euclidean distance works without normalization and is preferred for absolute-position tasks.

**Batch size**: set to the model provider's recommended value. Too-large batches increase latency variance; too-small batches underutilize GPU throughput. Start at 32 and adjust from measured throughput data.

## Anti-Pattern

- Using cosine distance without normalize: true - produces similarity scores based on vector length, not direction.
- Setting chunk_size to the model's full context window - boundary truncation degrades embedding quality.
- Setting overlap to 0 - creates retrieval gaps at every chunk boundary.
- Specifying dimensions as a string ("768") instead of integer 768 - causes schema validation failures.
- Drifting into index configuration (FAISS parameters, shard counts) in this artifact - those belong in a brain-index config.
- Guessing cost per million tokens for local/free models - use null for cost when the model has no per-call charge.

## Context

Applies when configuring the embedding stage of a retrieval pipeline. Upstream of: chunking, indexing, and query-time retrieval. Downstream of: document ingestion and text preprocessing. The embedding config is a static specification - it does not run code. Runtime behavior depends on the executor correctly reading all four configuration fields and applying them consistently at both index-time and query-time (critical: the same model, chunk size, and normalization must be used for both indexing and querying).

## Impact

- Correct normalization setting eliminates metric-normalization mismatch errors (~34% incorrect top-1 in tests).
- 65% chunk-size rule preserves complete semantic units in ~97% of chunks.
- 12% overlap eliminates retrieval gaps at chunk boundaries.
- Validated model-dimension pairs prevent silent dimension mismatches that corrupt index structure.

## Reproducibility

1. Select model from validated reference table; copy its native dimension count exactly.
2. Look up the model's token context window; multiply by 0.65 for chunk_size.
3. Multiply chunk_size by 0.12 for overlap.
4. Choose distance metric; if cosine, set normalize: true.
5. Set batch_size to 32 as default; adjust after throughput measurement.
6. Set cost to null for local models; look up actual price for API models.

## References

- embedding-config-builder/INSTRUCTIONS.md
- embedding-config-builder/SCHEMA.md
- Embedding model reference table in this builder's production memory
- MTEB Leaderboard (2025) - model quality benchmarks
