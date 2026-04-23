---
kind: config
id: bld_config_router
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
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
title: "Config Router"
version: "1.0.0"
author: n03_builder
tags: [router, builder, examples]
tldr: "Golden and anti-examples for router construction, demonstrating ideal structure and common pitfalls."
domain: "router construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_router
  - bld_schema_router
  - p11_qg_router
  - bld_examples_router
  - p03_ins_router
  - p03_sp_router_builder
  - bld_config_memory_scope
  - bld_memory_router
  - router-builder
  - bld_architecture_router
---
# Config: router Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_router_{slug}.md` | `p02_router_agent_group_task.md` |
| Builder directory | kebab-case | `router-builder/` |
| Frontmatter fields | snake_case | `routes_count`, `fallback_route` |
| Router slug | snake_case, lowercase | `agent_group_task`, `api_gateway` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P02_model/examples/p02_router_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_router_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80
## Load Balance Enum
| Value | When to use |
|-------|-------------|
| priority | Routes have clear priority ordering (default) |
| weighted | Traffic should be distributed by weight percentage |
| round_robin | Equal distribution across equivalent destinations |
| none | Single best match only, no distribution |
## Confidence Threshold Guidelines
| Range | Meaning | Use case |
|-------|---------|----------|
| 0.9-1.0 | Very high confidence required | Critical/admin routes |
| 0.7-0.9 | Standard confidence | Most production routes |
| 0.5-0.7 | Loose matching | Exploratory or catch-all routes |
| < 0.5 | Not recommended | Too many false positives |
## Route Table Requirements
- Minimum 2 routes per router (1-route routers are dispatch_rules)
- Each pattern must be unique across the table
- Priority range: 1-100 (higher = preferred)
- Confidence_min per route can override global confidence_threshold

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_router]] | upstream | 0.46 |
| [[bld_schema_router]] | upstream | 0.41 |
| [[p11_qg_router]] | downstream | 0.40 |
| [[bld_examples_router]] | upstream | 0.39 |
| [[p03_ins_router]] | upstream | 0.38 |
| [[p03_sp_router_builder]] | upstream | 0.36 |
| [[bld_config_memory_scope]] | sibling | 0.35 |
| [[bld_memory_router]] | downstream | 0.35 |
| [[router-builder]] | upstream | 0.34 |
| [[bld_architecture_router]] | upstream | 0.33 |
