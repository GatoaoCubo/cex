---
kind: config
id: bld_config_tts_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for tts_provider production
quality: 8.6
title: "Config Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, config]
tldr: "Naming, paths, limits for tts_provider production"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
p04_tts_{{name}}.md (e.g., p04_tts_azure.md, p04_tts_google.md)  

## Paths  
/artifacts/tts/{{name}}/  
/config/tts/{{name}}.yaml  

## Limits  
max_bytes: 4096  
max_turns: 5  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null
