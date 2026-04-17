---
kind: collaboration
id: bld_collaboration_stt_provider
pillar: P12
llm_function: COLLABORATE
purpose: How stt_provider-builder works in crews with other builders
quality: 8.9
title: "Collaboration Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, collaboration]
tldr: "How stt_provider-builder works in crews with other builders"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Configures and integrates STT provider APIs, ensuring compatibility with system interfaces and handling credential management.  

## Receives From  
| Builder       | What                  | Format   |  
|---------------|-----------------------|----------|  
| config_manager| Provider credentials  | JSON     |  
| audio_engine  | Audio format specs    | YAML     |  
| test_suite    | Sample audio files    | WAV      |  

## Produces For  
| Builder       | What                  | Format       |  
|---------------|-----------------------|--------------|  
| voice_pipeline| STT integration code  | Python module|  
| config_manager| Provider config files | JSON         |  
| test_suite    | Integration test logs | TXT          |  

## Boundary  
Does NOT handle voice_pipeline end-to-end processing (handled by voice_pipeline builder) or VAD sensitivity thresholds (handled by vad_config builder).
