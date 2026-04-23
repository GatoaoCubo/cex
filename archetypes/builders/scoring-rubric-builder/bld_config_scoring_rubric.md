---
kind: config
id: bld_config_scoring_rubric
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for scoring_rubric production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_quality_gate
  - bld_config_memory_scope
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_config_validation_schema
  - bld_config_hook_config
  - bld_tools_scoring_rubric
  - bld_config_handoff_protocol
  - bld_config_constraint_spec
---
# Config: scoring_rubric Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_sr_{framework_slug}.md | p07_sr_5d_knowledge_card.md |
| Builder dir | kebab-case | scoring-rubric-builder/ |
| Fields | snake_case | dimensions_count, threshold_golden |
| Framework names | descriptive slug | 5d, 12lp, kc_quality |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P07_evals/examples/p07_sr_{framework_slug}.md
2. Compiled: cex/P07_evals/compiled/p07_sr_{framework_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 5120 bytes
2. Density: >= 0.80
3. Dimensions: >= 3 (no upper limit, but 3-8 recommended)
## Weight Policy
1. All dimension weights MUST sum to exactly 100%
2. Integer percentages preferred (25%, 20%, 15%)
3. No dimension below 5% (too small to matter)
4. No dimension above 40% (avoid single-dimension dominance)

## Metadata

```yaml
id: bld_config_scoring_rubric
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-scoring-rubric.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | scoring rubric construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.41 |
| [[bld_config_quality_gate]] | sibling | 0.40 |
| [[bld_config_memory_scope]] | sibling | 0.38 |
| [[bld_config_prompt_version]] | sibling | 0.36 |
| [[bld_config_output_validator]] | sibling | 0.36 |
| [[bld_config_validation_schema]] | sibling | 0.35 |
| [[bld_config_hook_config]] | sibling | 0.35 |
| [[bld_tools_scoring_rubric]] | upstream | 0.34 |
| [[bld_config_handoff_protocol]] | sibling | 0.34 |
| [[bld_config_constraint_spec]] | sibling | 0.34 |
