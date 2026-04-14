---
kind: collaboration
id: bld_collaboration_prosody_config
pillar: P12
llm_function: COLLABORATE
purpose: How prosody_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, collaboration]
tldr: "How prosody_config-builder works in crews with other builders"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Configures prosody and emotion parameters for voice synthesis, ensuring alignment with emotional tone and speech rhythm requirements.  

## Receives From  
| Builder       | What                  | Format  |  
|---------------|-----------------------|---------|  
| emotion_profile | Emotional state definitions | JSON    |  
| prosody_rules   | Speech pattern guidelines   | YAML    |  
| voice_characteristics | Pitch, pace, and tone attributes | JSON  |  

## Produces For  
| Builder           | What                    | Format  |  
|-------------------|-------------------------|---------|  
| prosody_config    | Final prosody configuration | JSON    |  
| emotion_mapping   | Emotion-to-prosody parameter mappings | YAML  |  
| validation_report | Compliance check against rules | Markdown |  

## Boundary  
Does NOT handle TTS provider integrations (handled by `tts_provider_builder`) or agent persona definitions (handled by `agent_profile_builder`). Emotion state generation is excluded; only mapping and configuration are scoped.
