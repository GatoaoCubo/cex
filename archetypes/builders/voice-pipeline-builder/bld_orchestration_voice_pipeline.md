---
kind: collaboration
id: bld_collaboration_voice_pipeline
pillar: P12
llm_function: COLLABORATE
purpose: How voice_pipeline-builder works in crews with other builders
quality: 8.9
title: "Collaboration Voice Pipeline"
version: "1.0.0"
author: wave1_builder_gen
tags: [voice_pipeline, builder, collaboration]
tldr: "How voice_pipeline-builder works in crews with other builders"
domain: "voice_pipeline construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_stt_provider
  - p03_sp_voice_pipeline_builder
  - bld_collaboration_tts_provider
  - bld_collaboration_realtime_session
  - bld_memory_voice_pipeline
  - p11_qg_voice_pipeline
  - voice-pipeline-builder
  - bld_collaboration_audio_tool
  - p01_kc_audio_tool
  - p03_sp_tts_provider_builder
---

## Crew Role  
Orchestrates end-to-end voice pipeline workflows, integrating STT/TTS components, managing data flow, and ensuring compatibility between providers.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| STT Provider  | Transcribed text      | JSON        |  
| TTS Provider  | Audio output          | WAV         |  
| Config Manager| Pipeline settings     | YAML        |  
| User Interface| Customization requests| JSON        |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| TTS Provider  | Text to synthesize    | JSON        |  
| STT Provider  | Audio to transcribe   | WAV         |  
| Monitoring    | Pipeline metrics      | Log         |  
| User Interface| Pipeline status       | Dashboard   |  

## Boundary  
Does NOT implement STT/TTS algorithms (handled by stt_provider/tts_provider builders), manage
infrastructure configuration (handled by env_config/sandbox_config builders), or define session
state (handled by realtime_session builder).

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
| Domain | voice_pipeline construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_stt_provider]] | sibling | 0.44 |
| [[p03_sp_voice_pipeline_builder]] | upstream | 0.41 |
| [[bld_collaboration_tts_provider]] | sibling | 0.38 |
| [[bld_collaboration_realtime_session]] | sibling | 0.38 |
| [[bld_memory_voice_pipeline]] | upstream | 0.38 |
| [[p11_qg_voice_pipeline]] | upstream | 0.36 |
| [[voice-pipeline-builder]] | upstream | 0.34 |
| [[bld_collaboration_audio_tool]] | sibling | 0.34 |
| [[p01_kc_audio_tool]] | upstream | 0.34 |
| [[p03_sp_tts_provider_builder]] | upstream | 0.33 |
