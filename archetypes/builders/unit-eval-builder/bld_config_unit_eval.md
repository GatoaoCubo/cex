---
kind: config
id: bld_config_unit_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for unit_eval production
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
title: "Config Unit Eval"
version: "1.0.0"
author: n03_builder
tags: [unit_eval, builder, examples]
tldr: "Golden and anti-examples for unit eval construction, demonstrating ideal structure and common pitfalls."
domain: "unit eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
# Config: unit_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_ue_{target_slug}.md | p07_ue_kc_yaml_parse.md |
| Compiled | p07_ue_{target_slug}.yaml | p07_ue_kc_yaml_parse.yaml |
| Builder dir | kebab-case | unit-eval-builder/ |
| Fields | snake_case | target_kind, expected_output |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P07_evals/p07_ue_{target_slug}.md
2. Compiled: cex/P07_evals/compiled/p07_ue_{target_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
3. Timeout: default 60s, max 300s for unit scope
## Assertion Policy
1. Minimum 1 assertion per unit_eval
2. Each assertion MUST reference a gate_ref from target builder
3. Severity must be HARD or SOFT (no costm levels)

## Metadata

```yaml
id: bld_config_unit_eval
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-unit-eval.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | unit eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
