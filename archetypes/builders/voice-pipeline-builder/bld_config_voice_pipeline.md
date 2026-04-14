---
kind: config
id: bld_config_voice_pipeline
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for voice_pipeline production
quality: 8.8
title: "Config Voice Pipeline"
version: "1.0.0"
author: wave1_builder_gen
tags: [voice_pipeline, builder, config]
tldr: "Naming, paths, limits for voice_pipeline production"
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Naming Convention  
Pattern: `p04_vp_{{name}}.md`  
Examples: `p04_vp_speech.md`, `p04_vp_tts.md`  

## Paths  
Base: `/artifacts/p04/vp/{{name}}/`  
Audio: `{{base}}/audio/`  
Logs: `{{base}}/logs/`  
Metadata: `{{base}}/meta/`  

## Limits  
max_bytes: 5120  
max_turns: 10  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
