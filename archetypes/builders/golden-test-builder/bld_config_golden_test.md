---
kind: config
id: bld_config_golden_test
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for golden_test production
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
title: "Config Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_quality_gate
  - bld_output_template_golden_test
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_output_validator
  - bld_config_validation_schema
  - bld_config_prompt_version
  - p10_lr_golden_test_builder
  - bld_config_hook_config
  - bld_config_handoff_protocol
---
# Config: golden_test Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_gt_{case_slug}.md | p07_gt_kc_prompt_caching.md |
| Builder dir | kebab-case | golden-test-builder/ |
| Fields | snake_case | quality_threshold, target_kind |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P07_evals/examples/p07_gt_{case_slug}.md
2. Compiled: cex/P07_evals/compiled/p07_gt_{case_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
3. Golden output: no truncation (complete artifact required)
## Quality Threshold Policy
1. quality_threshold minimum: 9.5 (non-negotiable)
2. Reviewer approval required before golden status
3. Producer CANNOT self-approve as reviewer

## Metadata

```yaml
id: bld_config_golden_test
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-golden-test.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | golden test construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_quality_gate]] | sibling | 0.39 |
| [[bld_output_template_golden_test]] | upstream | 0.39 |
| [[bld_config_retriever_config]] | sibling | 0.39 |
| [[bld_config_memory_scope]] | sibling | 0.36 |
| [[bld_config_output_validator]] | sibling | 0.35 |
| [[bld_config_validation_schema]] | sibling | 0.35 |
| [[bld_config_prompt_version]] | sibling | 0.35 |
| [[p10_lr_golden_test_builder]] | downstream | 0.34 |
| [[bld_config_hook_config]] | sibling | 0.33 |
| [[bld_config_handoff_protocol]] | sibling | 0.33 |
