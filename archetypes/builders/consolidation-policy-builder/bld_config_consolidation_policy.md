---
kind: config
id: bld_config_consolidation_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for consolidation_policy production
quality: null
title: "Config Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, config]
tldr: "Naming, paths, limits for consolidation_policy production"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention  
Pattern: `p10_cp_{{name}}.md`  
Examples: `p10_cp_security.md`, `p10_cp_compliance.md`  

## Paths  
Policies: `/cex/policies/p10/consolidation/`  
Artifacts: `/cex/artifacts/p10/consolidation/`  

## Limits  
max_bytes: 4096, max_turns: 10, effort_level: 3  

## Hooks  
pre_build: null, post_build: null, on_error: null, on_quality_fail: null
