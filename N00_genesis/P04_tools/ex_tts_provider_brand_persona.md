---
id: ex_tts_provider_brand_persona
kind: tts_provider
pillar: P04
title: "Example TTS Provider: Brand Persona Voice"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: brand_persona_chat
quality: 8.7
brand_placeholders:
  - BRAND_NAME
  - BRAND_PERSONA_NAME
  - BRAND_VOICE
  - BRAND_TTS_VOICE_ID
tags: [tts_provider, voice, audio, brand-persona, n02]
tldr: "Provider contract for converting brand persona text into consistent spoken audio."
density_score: 0.88
related:
  - bld_instruction_tts_provider
  - bld_collaboration_model_provider
  - p01_kc_elevenlabs_tts
  - model-provider-builder
  - bld_collaboration_tts_provider
  - p03_sp_tts_provider_builder
  - voice-pipeline-builder
  - bld_architecture_stt_provider
  - bld_output_template_tts_provider
  - bld_knowledge_card_tts_provider
---

# Purpose

Map `{{BRAND_PERSONA_NAME}}` text output to a stable TTS voice profile using `{{BRAND_TTS_VOICE_ID}}`.

## Provider Contract

```yaml
provider: "{{TTS_PROVIDER_NAME}}"
voice_id: "{{BRAND_TTS_VOICE_ID}}"
input:
  text: string
  tone: "{{BRAND_VOICE}}"
  pace: medium
  language: auto
output:
  audio_format: mp3
  sample_rate_hz: 44100
  max_duration_seconds: 120
retry_policy:
  attempts: 2
  fallback_voice_id: "{{FALLBACK_VOICE_ID}}"
```

## Selection Rules

- Favor clarity over dramatic performance.
- Keep cadence aligned with `{{BRAND_VOICE}}`.
- Reject voices that distort product names or CTA phrases.

## New Brand Variables

- `FALLBACK_VOICE_ID`: backup voice when the primary provider fails.
- `TTS_PROVIDER_NAME`: vendor label used for routing and billing.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_tts_provider]] | upstream | 0.23 |
| [[bld_collaboration_model_provider]] | upstream | 0.23 |
| [[p01_kc_elevenlabs_tts]] | upstream | 0.22 |
| [[model-provider-builder]] | upstream | 0.21 |
| [[bld_collaboration_tts_provider]] | downstream | 0.21 |
| [[p03_sp_tts_provider_builder]] | upstream | 0.20 |
| [[voice-pipeline-builder]] | related | 0.20 |
| [[bld_architecture_stt_provider]] | downstream | 0.20 |
| [[bld_output_template_tts_provider]] | downstream | 0.19 |
| [[bld_knowledge_card_tts_provider]] | upstream | 0.19 |
