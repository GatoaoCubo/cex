---
kind: config
id: bld_config_realtime_session
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for realtime_session production
quality: 8.7
title: "Config: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, config]
tldr: "Naming, paths, limits for realtime_session production (kind lives in P04, artifacts use p04_rs_ prefix)."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_repo_map
  - bld_config_ab_test_config
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_usage_quota
  - bld_config_agent_computer_interface
  - bld_config_data_residency
---

## Naming Convention
Pattern: `p04_rs_{{name}}.md`
Examples: `p04_rs_support_voicebot.md`, `p04_rs_demo_agent.md`
Regex: `^p04_rs_[a-z0-9_]{3,48}\.md$`

Note: Kind `realtime_session` lives in pillar P04 (Tools/Capabilities).
The `bld_config` ISO itself lives in P09 (Config) as it defines production settings.

## Paths
Artifacts: `P04_tools/realtime_session/p04_rs_{{name}}.md`
Builder ISOs: `archetypes/builders/realtime-session-builder/`

## Limits
max_bytes: 5120
max_turns: 20
effort_level: 5

## Hooks
pre_build: null
post_build: python _tools/cex_compile.py {path}
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.46 |
| [[bld_config_transport_config]] | sibling | 0.46 |
| [[bld_config_diff_strategy]] | sibling | 0.45 |
| [[bld_config_repo_map]] | sibling | 0.44 |
| [[bld_config_ab_test_config]] | sibling | 0.44 |
| [[bld_config_pricing_page]] | sibling | 0.44 |
| [[bld_config_sales_playbook]] | sibling | 0.44 |
| [[bld_config_usage_quota]] | sibling | 0.44 |
| [[bld_config_agent_computer_interface]] | sibling | 0.43 |
| [[bld_config_data_residency]] | sibling | 0.43 |
