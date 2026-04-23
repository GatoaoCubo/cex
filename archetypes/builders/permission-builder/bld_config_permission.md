---
kind: config
id: bld_config_permission
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for permission production
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
title: "Config Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_permission
  - p03_ins_permission
  - bld_knowledge_card_permission
  - bld_memory_permission
  - bld_tools_permission
  - p03_sp_permission_builder
  - bld_examples_permission
  - permission-builder
  - p11_qg_permission
  - p09_perm_{{SCOPE_SLUG}}
---
# Config: permission Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p09_perm_{scope_slug}.md | p09_perm_pool_access.md |
| Builder dir | kebab-case | permission-builder/ |
| Fields | snake_case | deny_list, allow_list |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P09_config/examples/p09_perm_{scope_slug}.md
2. Compiled: cex/P09_config/compiled/p09_perm_{scope_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 3072 bytes
2. Density: >= 0.80
## Access Level Matrix
| Level | Meaning | Enum values |
|-------|---------|------------|
| read | View resource content | allow, deny, conditional |
| write | Modify resource content | allow, deny, conditional |
| execute | Run resource as action | allow, deny, conditional |
## Precedence Rule
deny_list ALWAYS overrides allow_list (no exceptions).

## Metadata

```yaml
id: bld_config_permission
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-permission.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_permission]] | upstream | 0.50 |
| [[p03_ins_permission]] | upstream | 0.42 |
| [[bld_knowledge_card_permission]] | upstream | 0.41 |
| [[bld_memory_permission]] | downstream | 0.40 |
| [[bld_tools_permission]] | upstream | 0.38 |
| [[p03_sp_permission_builder]] | upstream | 0.38 |
| [[bld_examples_permission]] | upstream | 0.36 |
| [[permission-builder]] | related | 0.36 |
| [[p11_qg_permission]] | downstream | 0.35 |
| [[p09_perm_{{SCOPE_SLUG}}]] | related | 0.33 |
