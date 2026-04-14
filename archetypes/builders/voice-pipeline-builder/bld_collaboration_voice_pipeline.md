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
