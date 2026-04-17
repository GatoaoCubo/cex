---
kind: config
id: bld_config_sandbox_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sandbox_config production
quality: 8.6
title: "Config Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, config]
tldr: "Naming, paths, limits for sandbox_config production"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p09_sb_{{name}}.yaml`  
Examples: `p09_sb_example.yaml`, `p09_sb_test.yaml`  

## Paths  
Artifacts stored in: `/sandboxes/p09/{{name}}/artifacts`  

## Limits  
max_bytes: 2048  
max_turns: 10  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
