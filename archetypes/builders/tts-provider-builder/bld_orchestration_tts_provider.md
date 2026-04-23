---
kind: collaboration
id: bld_collaboration_tts_provider
pillar: P12
llm_function: COLLABORATE
purpose: How tts_provider-builder works in crews with other builders
quality: 8.9
title: "Collaboration Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, collaboration]
tldr: "How tts_provider-builder works in crews with other builders"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_tts_provider_builder
  - bld_collaboration_voice_pipeline
  - tts-provider-builder
  - voice-pipeline-builder
  - bld_instruction_tts_provider
  - bld_collaboration_prosody_config
  - kc_tts_provider
  - bld_collaboration_vad_config
  - bld_collaboration_sso_config
  - p10_lr_tts_provider_builder
---

## Crew Role  
Manages integration with external TTS APIs, ensuring compatibility, configuration management, and error handling for text-to-speech synthesis.  

## Receives From  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| API_Manager   | API credentials       | JSON       |  
| Config_Reader | Provider-specific settings | YAML     |  
| Text_Handler  | Text input for synthesis | Plain text |  

## Produces For  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| File_Exporter | TTS output files      | WAV/MP3    |  
| Error_Handler | Error logs            | JSON       |  
| Config_Validator | Configuration validation results | YAML |  

## Boundary  
Does NOT handle voice pipeline architecture (voice_pipeline_builder) or prosody configuration (prosody_configurator). Voice pipeline design and personality tuning are managed by dedicated components.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_tts_provider_builder]] | upstream | 0.34 |
| [[bld_collaboration_voice_pipeline]] | sibling | 0.33 |
| [[tts-provider-builder]] | upstream | 0.32 |
| [[voice-pipeline-builder]] | upstream | 0.30 |
| [[bld_instruction_tts_provider]] | upstream | 0.27 |
| [[bld_collaboration_prosody_config]] | sibling | 0.26 |
| [[kc_tts_provider]] | upstream | 0.26 |
| [[bld_collaboration_vad_config]] | sibling | 0.26 |
| [[bld_collaboration_sso_config]] | sibling | 0.24 |
| [[p10_lr_tts_provider_builder]] | upstream | 0.24 |
