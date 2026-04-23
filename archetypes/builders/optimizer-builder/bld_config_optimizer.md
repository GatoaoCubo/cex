---
kind: config
id: bld_config_optimizer
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for optimizer production
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
quality: 9.1
title: "Config Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_ins_optimizer
  - bld_config_quality_gate
  - bld_schema_optimizer
  - p11_qg_optimizer
  - bld_knowledge_card_optimizer
  - bld_memory_optimizer
  - bld_output_template_optimizer
  - bld_config_unit_eval
  - bld_config_retriever_config
  - bld_config_memory_scope
---
# Config: optimizer Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_opt_{target_slug}.md | p11_opt_kc_latency.md |
| Builder dir | kebab-case | optimizer-builder/ |
| Fields | snake_case | density_score, measured_at |
| Slug chars | [a-z][a-z0-9_]+ | no hyphens, no uppercase |
Rule: id MUST equal filename stem.
Rule: target_slug derived from target field — spaces to underscores, lowercase.
## File Paths
1. Output: cex/P11_feedback/examples/p11_opt_{target_slug}.md
2. Compiled: cex/P11_feedback/compiled/p11_opt_{target_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
## Threshold Ordering Rules
| metric.direction | Ordering |
|-----------------|----------|
| minimize | trigger < target < critical |
| maximize | trigger > target > critical |
## Frequency Enum (valid values only)
continuous, hourly, daily, weekly, monthly
## Action Type Enum (valid values only)
tune, prune, scale, replace, restructure
## Risk Level Enum (valid values only)
low, medium, high
## Improvement History
1. list of {date: YYYY-MM-DD, value: float}
2. minimum 0 entries at creation
3. append on each optimization cycle
## Automated Flag
1. true: system executes action without human approval
2. false: system flags, human approves before execution

## Metadata

```yaml
id: bld_config_optimizer
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-optimizer.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | upstream | 0.35 |
| [[bld_config_quality_gate]] | sibling | 0.33 |
| [[bld_schema_optimizer]] | upstream | 0.33 |
| [[p11_qg_optimizer]] | downstream | 0.32 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.31 |
| [[bld_memory_optimizer]] | downstream | 0.30 |
| [[bld_output_template_optimizer]] | upstream | 0.29 |
| [[bld_config_unit_eval]] | sibling | 0.29 |
| [[bld_config_retriever_config]] | sibling | 0.29 |
| [[bld_config_memory_scope]] | sibling | 0.29 |
