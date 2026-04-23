---
kind: config
id: bld_config_e2e_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for e2e_eval production
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
title: "Config E2E Eval"
version: "1.0.0"
author: n03_builder
tags: [e2e_eval, builder, examples]
tldr: "Golden and anti-examples for e2e eval construction, demonstrating ideal structure and common pitfalls."
domain: "e2e eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_output_template_e2e_eval
  - e2e-eval-builder
  - bld_config_retriever_config
  - bld_config_quality_gate
  - bld_schema_e2e_eval
  - bld_tools_e2e_eval
  - bld_config_unit_eval
  - bld_config_memory_scope
  - bld_config_validation_schema
  - bld_config_prompt_version
---
# Config: e2e_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_e2e_{pipeline_slug}.md | p07_e2e_research_to_kc.md |
| Compiled | p07_e2e_{pipeline_slug}.yaml | p07_e2e_research_to_kc.yaml |
| Builder dir | kebab-case | e2e-eval-builder/ |
| Fields | snake_case | data_fixtures, expected_output |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P07_evals/p07_e2e_{pipeline_slug}.md
2. Compiled: cex/P07_evals/compiled/p07_e2e_{pipeline_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
3. Timeout: default 300s, max 600s for complex pipelines
## Pipeline Policy
1. Minimum 2 stages per e2e_eval (otherwise use unit_eval)
2. Stages must form connected flow (output_n feeds input_n+1)
3. Data fixtures required for reproducibility
4. Cleanup mandatory (tests must not pollute state)

## Metadata

```yaml
id: bld_config_e2e_eval
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-e2e-eval.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | e2e eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_e2e_eval]] | upstream | 0.45 |
| [[e2e-eval-builder]] | upstream | 0.39 |
| [[bld_config_retriever_config]] | sibling | 0.37 |
| [[bld_config_quality_gate]] | sibling | 0.37 |
| [[bld_schema_e2e_eval]] | upstream | 0.36 |
| [[bld_tools_e2e_eval]] | upstream | 0.35 |
| [[bld_config_unit_eval]] | sibling | 0.35 |
| [[bld_config_memory_scope]] | sibling | 0.34 |
| [[bld_config_validation_schema]] | sibling | 0.33 |
| [[bld_config_prompt_version]] | sibling | 0.33 |
