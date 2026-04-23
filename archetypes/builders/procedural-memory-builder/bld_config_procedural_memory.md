---
kind: config
id: bld_config_procedural_memory
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for procedural_memory production
quality: 8.7
title: "Config: procedural_memory-builder"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, config]
tldr: "Naming convention p10_pm_*, pillar P10, max 6144 bytes, stored in P10_memory/ or agent-specific subdirectory"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_config_consolidation_policy
  - bld_config_memory_architecture
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_agent_computer_interface
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_model_registry
  - bld_config_diff_strategy
---

## Naming Convention
Pattern: `p10_pm_[a-z][a-z0-9_]+`
Examples:
- `p10_pm_coding_assistant_pro`
- `p10_pm_research_agent_enterprise`
- `p10_pm_empty_free_tier`

## Paths
Artifacts stored in pillar directory:
`P10_memory/skills/`

Or co-located with agent:
`N0{x}_*/memory/p10_pm_*.md`

## Limits
- max_bytes: 6144
- max_turns: null (static skill library spec)
- effort_level: 4 (high -- requires reading memory_architecture + consolidation_policy first)
- quality_floor: 8.0
- quality_target: 9.0

## Hooks
- pre_build: read parent memory_architecture (for tier) and consolidation_policy (for TTL)
- post_build: `python _tools/cex_compile.py {path}`
- on_quality_fail: check domain accuracy (D04: robotics/hardware contamination is common)
- on_error: verify skill_format and tier fields present, no motor schema terminology

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_consolidation_policy]] | sibling | 0.54 |
| [[bld_config_memory_architecture]] | sibling | 0.42 |
| [[bld_config_search_strategy]] | sibling | 0.37 |
| [[bld_config_transport_config]] | sibling | 0.36 |
| [[bld_config_sales_playbook]] | sibling | 0.36 |
| [[bld_config_agent_computer_interface]] | sibling | 0.35 |
| [[bld_config_partner_listing]] | sibling | 0.34 |
| [[bld_config_planning_strategy]] | sibling | 0.34 |
| [[bld_config_model_registry]] | sibling | 0.34 |
| [[bld_config_diff_strategy]] | sibling | 0.34 |
