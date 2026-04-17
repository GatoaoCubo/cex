---
kind: config
id: bld_config_vad_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for vad_config production
quality: 8.6
title: "Config Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, config]
tldr: "Naming, paths, limits for vad_config production"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: p09_vad_{{name}}.yaml  
Examples:  
- p09_vad_speech.yaml  
- p09_vad_noise.yaml  

## Paths  
/artifacts/p09/vad/{{name}}/  

## Limits  
- max_bytes: 2048  
- max_turns: 10  
- effort_level: 3  

## Hooks  
- pre_build: null  
- post_build: null  
- on_error: null  
- on_quality_fail: null
