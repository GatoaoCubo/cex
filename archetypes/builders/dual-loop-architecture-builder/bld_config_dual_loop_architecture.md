---
kind: config
id: bld_config_dual_loop_architecture
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for dual_loop_architecture production
quality: null
title: "Config Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, config]
tldr: "Naming, paths, limits for dual_loop_architecture production"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p08_dl_{{name}}.md`  
Examples: `p08_dl_initial.md`, `p08_dl_refined.md`  

## Paths  
Base: `/artifacts/p08/dl/{{name}}/`  
Subpaths: `/drafts/`, `/reviews/`, `/final/`  

## Limits  
max_bytes: 5120  
max_turns: 10  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
