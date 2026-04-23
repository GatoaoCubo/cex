---
kind: config
id: bld_config_smoke_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for smoke_eval production
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
title: "Config Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - smoke-eval-builder
  - bld_knowledge_card_smoke_eval
  - bld_output_template_smoke_eval
  - bld_memory_smoke_eval
  - p03_sp_smoke_eval_builder
  - bld_tools_smoke_eval
  - bld_collaboration_smoke_eval
  - bld_config_retriever_config
  - bld_config_quality_gate
  - p07_se_{{SCOPE_SLUG}}
---
# Config: smoke_eval Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_se_{scope_slug}.md | p07_se_brain_mcp.md |
| Builder dir | kebab-case | smoke-eval-builder/ |
| Fields | snake_case | critical_path, fast_fail |
Rule: id MUST equal filename stem.
## File Paths
- Output: cex/P07_evals/p07_se_{scope_slug}.md
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes (smaller than unit_eval)
2. Density: >= 0.80
3. Timeout: MUST be <= 30 seconds (non-negotiable)
## Fast-Fail Policy
1. fast_fail: always true (smoke tests abort on first failure)
2. No partial pass — either all checks pass or test fails
3. On failure: log which check failed, suggest remediation

## Metadata

```yaml
id: bld_config_smoke_eval
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-smoke-eval.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | smoke eval construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[smoke-eval-builder]] | upstream | 0.43 |
| [[bld_knowledge_card_smoke_eval]] | upstream | 0.42 |
| [[bld_output_template_smoke_eval]] | upstream | 0.40 |
| [[bld_memory_smoke_eval]] | downstream | 0.40 |
| [[p03_sp_smoke_eval_builder]] | upstream | 0.40 |
| [[bld_tools_smoke_eval]] | upstream | 0.39 |
| [[bld_collaboration_smoke_eval]] | upstream | 0.39 |
| [[bld_config_retriever_config]] | sibling | 0.38 |
| [[bld_config_quality_gate]] | sibling | 0.36 |
| [[p07_se_{{SCOPE_SLUG}}]] | upstream | 0.36 |
