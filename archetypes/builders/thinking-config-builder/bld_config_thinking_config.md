---
kind: config
id: bld_config_thinking_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for thinking_config production
quality: null
title: "Config Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, config]
tldr: "Naming, paths, limits for thinking_config production"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p09_thk_{{name}}.yaml`  
Examples: `p09_thk_report.yaml`, `p09_thk_analysis.yaml`  

## Paths  
Artifacts stored in: `/artifacts/p09/{{name}}/`  

## Limits  
max_bytes: 2048  
max_turns: 5  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
