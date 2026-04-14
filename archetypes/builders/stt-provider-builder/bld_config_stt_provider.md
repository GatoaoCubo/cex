---
kind: config
id: bld_config_stt_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for stt_provider production
quality: 8.6
title: "Config Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, config]
tldr: "Naming, paths, limits for stt_provider production"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p04_stt_{{name}}.md`  
Examples: `p04_stt_azure.md`, `p04_stt_google.md`  
{{name}}: lowercase, alphanumeric, hyphens allowed  

## Paths  
Artifacts: `/artifacts/p04/stt/{{name}}/`  
Subdirectories: `models/`, `logs/`, `tests/`  

## Limits  
max_bytes: 4096  
max_turns: 10  
effort_level: medium  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
