---
kind: collaboration
id: bld_collaboration_vad_config
pillar: P12
llm_function: COLLABORATE
purpose: How vad_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, collaboration]
tldr: "How vad_config-builder works in crews with other builders"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - kc_vad_config
  - bld_collaboration_tts_provider
  - vad-config-builder
  - bld_architecture_vad_config
  - bld_collaboration_stt_provider
  - p03_sp_vad_config_builder
  - bld_instruction_vad_config
  - bld_knowledge_card_vad_config
  - voice-pipeline-builder
  - bld_collaboration_sso_config
---

## Crew Role  
Specializes in crafting and validating Voice Activity Detection (VAD) configurations, ensuring optimal silence/voice thresholds, sensitivity, and language-specific tuning for downstream processing.  

## Receives From  
| Builder         | What                          | Format      |  
|-----------------|-------------------------------|-------------|  
| voice_pipeline_builder | Audio sample rate, language | JSON        |  
| stt_provider_builder   | Sensitivity thresholds      | YAML        |  
| user_input      | Use case (e.g., noisy env)    | Structured  |  

## Produces For  
| Builder         | What                          | Format      |  
|-----------------|-------------------------------|-------------|  
| voice_pipeline_builder | VAD config file             | JSON        |  
| validation_team | Configuration validation report | CSV         |  
| deployment_team | Summary of applied settings   | Markdown    |  

## Boundary  
Does NOT handle full voice pipeline architecture (voice_pipeline_builder) or transcription provider integration (stt_provider_builder). Those are managed by dedicated builders.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_vad_config]] | upstream | 0.35 |
| [[bld_collaboration_tts_provider]] | sibling | 0.34 |
| [[vad-config-builder]] | upstream | 0.33 |
| [[bld_architecture_vad_config]] | upstream | 0.27 |
| [[bld_collaboration_stt_provider]] | sibling | 0.26 |
| [[p03_sp_vad_config_builder]] | upstream | 0.26 |
| [[bld_instruction_vad_config]] | upstream | 0.22 |
| [[bld_knowledge_card_vad_config]] | upstream | 0.22 |
| [[voice-pipeline-builder]] | upstream | 0.22 |
| [[bld_collaboration_sso_config]] | sibling | 0.22 |
