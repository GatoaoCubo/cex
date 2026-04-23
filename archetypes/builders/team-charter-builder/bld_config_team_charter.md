---
kind: config
id: bld_config_team_charter
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for team_charter production
quality: 8.6
title: "Config Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, config, governance]
tldr: "Naming, paths, limits for team_charter production"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_code_of_conduct
  - bld_config_transport_config
  - bld_collaboration_team_charter
  - bld_config_search_strategy
  - bld_config_visual_workflow
  - bld_config_sales_playbook
  - bld_config_prompt_technique
  - p03_sp_team_charter_builder
  - bld_config_healthcare_vertical
  - bld_config_graph_rag_config
---

## Naming Convention
Pattern: `p12_tc_{{mission_slug}}_v{{n}}.md`
Examples: `p12_tc_brand_launch_v1.md`, `p12_tc_rag_pipeline_v2.md`, `p12_tc_overnight_evolve_v1.md`

## Paths
Artifacts stored in: `P12_orchestration/charters/{{mission_slug}}/`
Archive path: `.cex/runtime/decisions/archive/tc_{{charter_id}}_{{date}}.md`

## Limits
max_bytes: 4096
max_turns: 3
effort_level: 2

## Hooks
pre_build: "Read GDP decision manifest (.cex/runtime/decisions/decision_manifest.yaml)"
post_build: "python _tools/cex_compile.py {path}"
on_error: "Write partial draft, flag missing fields, escalate to N07"
on_quality_fail: "Retry F6 once; if still < 8.0, output partial with TODO markers"

## Version Policy
- v1: initial charter (first GDP session)
- v2+: charter amended after mid-mission scope change (requires user approval)
- Amendments MUST preserve original budget ceiling and deadline UNLESS user explicitly overrides.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_code_of_conduct]] | sibling | 0.29 |
| [[bld_config_transport_config]] | sibling | 0.29 |
| [[bld_collaboration_team_charter]] | downstream | 0.29 |
| [[bld_config_search_strategy]] | sibling | 0.28 |
| [[bld_config_visual_workflow]] | sibling | 0.27 |
| [[bld_config_sales_playbook]] | sibling | 0.27 |
| [[bld_config_prompt_technique]] | sibling | 0.27 |
| [[p03_sp_team_charter_builder]] | upstream | 0.27 |
| [[bld_config_healthcare_vertical]] | sibling | 0.27 |
| [[bld_config_graph_rag_config]] | sibling | 0.27 |
