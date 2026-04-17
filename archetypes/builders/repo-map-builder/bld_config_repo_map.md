---
kind: config
id: bld_config_repo_map
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for repo_map production
quality: 8.6
title: "Config Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, config]
tldr: "Naming, paths, limits for repo_map production"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p01_rm_{{name}}.md`  
Examples:  
- `p01_rm_projectA.md`  
- `p01_rm_dataScience.md`  

## Paths  
- Root: `/repo_maps/`  
- Per Pillar: `/repo_maps/P01/{{name}}/`  

## Limits  
- max_bytes: 5120  
- max_turns: 10  
- effort_level: 3  

## Hooks  
- pre_build: null  
- post_build: null  
- on_error: null  
- on_quality_fail: null
