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
- Output: cex/P10_memory/examples/p10_bi_{index_slug}.md
- Compiled: cex/P10_memory/compiled/p10_bi_{index_slug}.yaml
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Density: >= 0.80
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
