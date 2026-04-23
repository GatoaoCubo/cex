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
related:
  - bld_collaboration_voice_pipeline
  - bld_collaboration_realtime_session
  - p03_sp_voice_pipeline_builder
  - bld_collaboration_model_provider
  - bld_architecture_stt_provider
  - stt-provider-builder
  - bld_collaboration_audio_tool
  - p03_sp_stt_provider_builder
  - bld_memory_voice_pipeline
  - bld_collaboration_tts_provider
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_voice_pipeline]] | sibling | 0.43 |
| [[bld_collaboration_realtime_session]] | sibling | 0.34 |
| [[p03_sp_voice_pipeline_builder]] | upstream | 0.29 |
| [[bld_collaboration_model_provider]] | sibling | 0.29 |
| [[bld_architecture_stt_provider]] | upstream | 0.28 |
| [[stt-provider-builder]] | upstream | 0.27 |
| [[bld_collaboration_audio_tool]] | sibling | 0.27 |
| [[p03_sp_stt_provider_builder]] | upstream | 0.27 |
| [[bld_memory_voice_pipeline]] | upstream | 0.26 |
| [[bld_collaboration_tts_provider]] | sibling | 0.26 |
