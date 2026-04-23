---
kind: config
id: bld_config_consolidation_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for consolidation_policy production
quality: 8.7
title: "Config: consolidation_policy-builder"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, config]
tldr: "Naming convention p10_cp_*, pillar P10, max 6144 bytes, stored in P10_memory/ or agent-specific subdirectory"
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_config_procedural_memory
  - bld_config_memory_architecture
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_model_registry
  - bld_config_diff_strategy
  - bld_config_usage_quota
---

## Naming Convention
Pattern: `p10_cp_[a-z][a-z0-9_]+`
Examples:
- `p10_cp_customer_support_pro`
- `p10_cp_research_agent_enterprise`
- `p10_cp_minimal_ttl_only`

## Paths
Artifacts stored in pillar directory:
`P10_memory/policies/`

Or co-located with parent memory_architecture:
`N0{x}_*/memory/p10_cp_*.md`

## Limits
- max_bytes: 6144
- max_turns: null (static policy spec)
- effort_level: 4 (high -- requires reading parent memory_architecture first)
- quality_floor: 8.0
- quality_target: 9.0

## Hooks
- pre_build: read parent memory_architecture artifact to determine active layers + tier
- post_build: `python _tools/cex_compile.py {path}`
- on_quality_fail: check domain accuracy first (D04 contamination is most common failure)
- on_error: verify consolidation_async: true is set and no OS/GC terminology present

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_procedural_memory]] | sibling | 0.49 |
| [[bld_config_memory_architecture]] | sibling | 0.38 |
| [[bld_config_search_strategy]] | sibling | 0.35 |
| [[bld_config_transport_config]] | sibling | 0.34 |
| [[bld_config_sales_playbook]] | sibling | 0.34 |
| [[bld_config_partner_listing]] | sibling | 0.33 |
| [[bld_config_planning_strategy]] | sibling | 0.33 |
| [[bld_config_model_registry]] | sibling | 0.33 |
| [[bld_config_diff_strategy]] | sibling | 0.32 |
| [[bld_config_usage_quota]] | sibling | 0.32 |
