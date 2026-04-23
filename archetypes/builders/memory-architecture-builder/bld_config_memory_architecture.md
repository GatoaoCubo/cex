---
kind: config
id: bld_config_memory_architecture
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for memory_architecture production
quality: 8.7
title: "Config: memory_architecture-builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, config]
tldr: "Naming convention p10_marc_*, pillar P10, max 8192 bytes, stored in P10_memory/ or agent-specific subdirectory"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_config_planning_strategy
  - bld_config_procedural_memory
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_agent_computer_interface
  - bld_config_consolidation_policy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_repo_map
---

## Naming Convention
Pattern: `p10_marc_[a-z][a-z0-9_]+`
Examples:
- `p10_marc_customer_support_v1`
- `p10_marc_research_agent_full`
- `p10_marc_minimal_working_only`

## Paths
Artifacts stored in pillar directory:
`P10_memory/architectures/`

Or agent-specific subdirectory:
`N0{x}_*/memory/p10_marc_*.md`

## Limits
- max_bytes: 8192
- max_turns: null (no limit -- architecture artifacts are static specs)
- effort_level: 4 (high -- architecture requires domain research + tier planning)
- quality_floor: 8.0
- quality_target: 9.0

## Hooks
- pre_build: verify agent type and target tier are known before building
- post_build: `python _tools/cex_compile.py {path}`
- on_quality_fail: rebuild knowledge_card + system_prompt first (domain accuracy is root cause)
- on_error: check for hardware memory terminology (D04 defect) and remove

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_planning_strategy]] | sibling | 0.38 |
| [[bld_config_procedural_memory]] | sibling | 0.37 |
| [[bld_config_search_strategy]] | sibling | 0.36 |
| [[bld_config_transport_config]] | sibling | 0.35 |
| [[bld_config_sales_playbook]] | sibling | 0.35 |
| [[bld_config_agent_computer_interface]] | sibling | 0.35 |
| [[bld_config_consolidation_policy]] | sibling | 0.34 |
| [[bld_config_partner_listing]] | sibling | 0.34 |
| [[bld_config_diff_strategy]] | sibling | 0.34 |
| [[bld_config_repo_map]] | sibling | 0.33 |
