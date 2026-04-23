---
kind: output_template
id: bld_output_template_prosody_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for prosody_config production
quality: 8.8
title: "Output Template Prosody Config"
version: "1.1.0"
author: n03_hybrid_review2
tags: [prosody_config, builder, output_template, ssml]
tldr: "Two-shape template: SSML emission or provider-native emission"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
related:
  - bld_instruction_prosody_config
  - bld_examples_prosody_config
  - hybrid_review2_n03
  - bld_knowledge_card_prosody_config
  - bld_schema_prosody_config
  - bld_output_template_tts_provider
  - p09_qg_prosody_config
  - bld_config_prosody_config
  - p04_fn_cf_elevenlabs_tts
  - p03_sp_prosody_config_builder
---

## Shape A -- SSML emission (Azure/Google/AWS/IBM)
```yaml
---
id: p09_prs_{{slug}}
kind: prosody_config
pillar: P09
version: 1.0.0
quality: null
emission: ssml
language: {{bcp47}}
---
baseline:
  pitch: "{{baseline_pitch|+0%}}"
  rate: "{{baseline_rate|100%}}"
  volume: "{{baseline_volume|medium}}"
emotions:
  {{emotion_name}}:
    ssml: |
      <prosody pitch="{{pitch_delta}}" rate="{{rate_delta}}" volume="{{volume_level}}">
        <break time="{{break_ms}}ms"/>
        <emphasis level="{{emphasis_level}}">{{text}}</emphasis>
      </prosody>
target_providers: [{{providers_csv}}]
```

## Shape B -- Provider-native emission (ElevenLabs/PlayHT/Cartesia/Hume)
```yaml
---
id: p09_prs_{{slug}}
kind: prosody_config
pillar: P09
version: 1.0.0
quality: null
emission: {{elevenlabs|playht|cartesia|hume}}
language: {{bcp47}}
---
provider: {{provider}}
model_id: {{model_id}}
# ElevenLabs shape
voice_settings:
  stability: {{0.0-1.0}}
  similarity_boost: {{0.0-1.0}}
  style: {{0.0-1.0}}
  use_speaker_boost: {{true|false}}
# Cartesia shape (use instead of voice_settings)
text_template: "[{{emotion_tag}}] {{text}} [pause:{{ms}}ms]"
speed: {{slow|normal|fast}}
# PlayHT shape
emotion: {{female_happy|male_sad|...}}
speed: {{0.5-2.0}}
target_providers: [{{providers_csv}}]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_prosody_config]] | upstream | 0.59 |
| [[bld_examples_prosody_config]] | downstream | 0.56 |
| [[hybrid_review2_n03]] | downstream | 0.47 |
| [[bld_knowledge_card_prosody_config]] | upstream | 0.45 |
| [[bld_schema_prosody_config]] | downstream | 0.27 |
| [[bld_output_template_tts_provider]] | sibling | 0.25 |
| [[p09_qg_prosody_config]] | downstream | 0.23 |
| [[bld_config_prosody_config]] | downstream | 0.22 |
| [[p04_fn_cf_elevenlabs_tts]] | upstream | 0.19 |
| [[p03_sp_prosody_config_builder]] | upstream | 0.17 |
