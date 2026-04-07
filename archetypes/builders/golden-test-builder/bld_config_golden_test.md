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
