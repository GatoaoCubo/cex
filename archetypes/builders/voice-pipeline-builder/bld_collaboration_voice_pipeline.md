---
kind: collaboration
id: bld_collaboration_voice_pipeline
pillar: P12
llm_function: COLLABORATE
purpose: How voice_pipeline-builder works in crews with other builders
quality: null
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
Does NOT implement STT/TTS algorithms (handled by providers), manage infrastructure (handled by DevOps), or enforce security policies (handled by Security team).
