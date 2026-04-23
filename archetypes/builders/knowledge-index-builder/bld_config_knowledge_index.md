---
kind: config
id: bld_config_knowledge_index
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for knowledge_index production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: high
max_turns: 25
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: global
quality: 9.0
title: "Config Knowledge Index"
version: "1.0.0"
author: n03_builder
tags: [knowledge_index, builder, examples]
tldr: "Golden and anti-examples for knowledge index construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge index construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_knowledge_index
  - bld_examples_knowledge_index
  - p11_qg_knowledge_index
  - bld_tools_knowledge_index
  - bld_config_runtime_state
  - knowledge-index-builder
  - bld_config_quality_gate
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_instruction_knowledge_index
---
# Config: knowledge_index Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p10_bi_{index_slug}.md | p10_bi_knowledge_pool.md |
| Builder dir | kebab-case | knowledge-index-builder/ |
| Fields | snake_case | rebuild_schedule, freshness_max_days |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P10_memory/examples/p10_bi_{index_slug}.md
2. Compiled: cex/P10_memory/compiled/p10_bi_{index_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Density: >= 0.80
## Algorithm Reference
| Algorithm | Best for | Latency | Accuracy |
|-----------|----------|---------|----------|
| bm25 | Exact keyword matching | Low | High precision |
| faiss | Semantic similarity | Medium | High recall |
| hybrid | Balanced search | Medium | Best F1 |
## Rebuild Reference
| Schedule | Frequency | Use case |
|----------|-----------|----------|
| on_change | Per document change | Small, critical corpus |
| hourly | Every hour | Active, frequently updated |
| daily | Once per day | Standard knowledge pool |
| weekly | Once per week | Stable, rarely changing |
| manual | On demand only | Static reference data |

## Metadata

```yaml
id: bld_config_knowledge_index
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-knowledge-index.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_knowledge_index]] | upstream | 0.31 |
| [[bld_examples_knowledge_index]] | upstream | 0.31 |
| [[p11_qg_knowledge_index]] | downstream | 0.29 |
| [[bld_tools_knowledge_index]] | upstream | 0.29 |
| [[bld_config_runtime_state]] | sibling | 0.29 |
| [[knowledge-index-builder]] | downstream | 0.27 |
| [[bld_config_quality_gate]] | sibling | 0.27 |
| [[bld_config_retriever_config]] | sibling | 0.26 |
| [[bld_config_memory_scope]] | sibling | 0.26 |
| [[bld_instruction_knowledge_index]] | upstream | 0.26 |
