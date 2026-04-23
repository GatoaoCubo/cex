---
kind: config
id: bld_config_lifecycle_rule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for lifecycle_rule production
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
title: "Config Lifecycle Rule"
version: "1.0.0"
author: n03_builder
tags: [lifecycle_rule, builder, examples]
tldr: "Golden and anti-examples for lifecycle rule construction, demonstrating ideal structure and common pitfalls."
domain: "lifecycle rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_quality_gate
  - bld_tools_lifecycle_rule
  - bld_schema_lifecycle_rule
  - bld_config_validation_schema
  - bld_config_retriever_config
  - bld_config_memory_scope
  - bld_config_runtime_rule
  - bld_config_prompt_version
  - bld_config_output_validator
  - bld_collaboration_lifecycle_rule
---
# Config: lifecycle_rule Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_lc_{rule_slug}.yaml | p11_lc_kc_freshness.yaml |
| Builder dir | kebab-case | lifecycle-rule-builder/ |
| Fields | snake_case | freshness_days, review_cycle |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P11_feedback/examples/p11_lc_{rule_slug}.yaml
2. Compiled: cex/P11_feedback/compiled/p11_lc_{rule_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
## Freshness Ranges by Domain Volatility
| Volatility | freshness_days | Example domains |
|------------|---------------|-----------------|
| High | 30-60 | model_card (pricing changes), scraper (site structure) |
| Medium | 60-120 | knowledge_card (domain facts), agent (capabilities) |
| Low | 120-365 | law (architectural rules), pattern (design patterns) |
| Stable | 365+ | interface (contracts), type_def (schemas) |
## Review Cycle Selection
| Artifact churn rate | Recommended cycle |
|--------------------|-------------------|
| Daily updates | weekly |
| Weekly updates | monthly |
| Monthly updates | quarterly |
| Rarely changes | yearly |

## Metadata

```yaml
id: bld_config_lifecycle_rule
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-lifecycle-rule.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_quality_gate]] | sibling | 0.33 |
| [[bld_tools_lifecycle_rule]] | upstream | 0.31 |
| [[bld_schema_lifecycle_rule]] | upstream | 0.27 |
| [[bld_config_validation_schema]] | sibling | 0.27 |
| [[bld_config_retriever_config]] | sibling | 0.27 |
| [[bld_config_memory_scope]] | sibling | 0.27 |
| [[bld_config_runtime_rule]] | sibling | 0.26 |
| [[bld_config_prompt_version]] | sibling | 0.26 |
| [[bld_config_output_validator]] | sibling | 0.26 |
| [[bld_collaboration_lifecycle_rule]] | downstream | 0.25 |
