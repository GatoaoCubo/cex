---
kind: config
id: bld_config_realtime_session
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for realtime_session production
quality: null
title: "Config Realtime Session"
version: "1.0.0"
author: wave1_builder_gen
tags: [realtime_session, builder, config]
tldr: "Naming, paths, limits for realtime_session production"
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p09_rs_{{name}}.md`  
Examples: `p09_rs_user123.md`, `p09_rs_projectX.md`  

## Paths  
Base: `/artifacts/p09/rs/{{session_id}}/`  
Examples:  
- Logs: `/artifacts/p09/rs/sess456/logs/`  
- Outputs: `/artifacts/p09/rs/sess456/outputs/`  

## Limits  
max_bytes: 4096  
max_turns: 20  
effort_level: 5  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
