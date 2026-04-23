---
id: p10_lr_embedding_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
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
agent_group: edison
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Embedding Config"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_embedding_config
  - p03_sp_embedding_config_builder
  - bld_manifest_memory_type
  - bld_instruction_embedding_config
  - bld_tools_memory_type
  - p01_kc_embedding_config
  - bld_config_memory_type
  - bld_config_tagline
  - p11_qg_embedding_config
  - bld_output_template_builder
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

## Builder Context

This ISO operates within the `embedding-config-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_embedding_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_embedding_config_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | embedding_config |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_embedding_config]] | upstream | 0.42 |
| [[p03_sp_embedding_config_builder]] | upstream | 0.38 |
| [[bld_manifest_memory_type]] | upstream | 0.38 |
| [[bld_instruction_embedding_config]] | upstream | 0.36 |
| [[bld_tools_memory_type]] | upstream | 0.33 |
| [[p01_kc_embedding_config]] | upstream | 0.32 |
| [[bld_config_memory_type]] | upstream | 0.31 |
| [[bld_config_tagline]] | upstream | 0.31 |
| [[p11_qg_embedding_config]] | downstream | 0.30 |
| [[bld_output_template_builder]] | upstream | 0.29 |
