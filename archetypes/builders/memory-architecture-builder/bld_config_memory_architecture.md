---
kind: config
id: bld_config_memory_architecture
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for memory_architecture production
quality: null
title: "Config Memory Architecture"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_architecture, builder, config]
tldr: "Naming, paths, limits for memory_architecture production"
domain: "memory_architecture construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention  
Pattern: p10_marc_{{name}}.md  
Examples:  
- p10_marc_example.md  
- p10_marc_core.md  

## Paths  
Artifacts stored in:  
`/opt/cex/memory_architecture/{{name}}/`  
Subdirectories:  
- `configs/`  
- `models/`  
- `logs/`  

## Limits  
- max_bytes: 5120  
- max_turns: 100  
- effort_level: 3  

## Hooks  
- pre_build: null  
- post_build: null  
- on_error: null  
- on_quality_fail: null
