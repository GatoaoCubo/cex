---
id: p04_fn_cf_elevenlabs_tts
kind: function_def
8f: F6_produce
pillar: P04
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
name: elevenlabs_text_to_speech
description: "Generate narration audio from text via ElevenLabs API. Call when the Content Factory needs voiceover for videos, lessons, or podcasts. Supports PT-BR and EN voices with emotion control."
parameters:
  type: object
  properties:
    text:
      type: string
      description: "Text to convert to speech. Max 5000 characters per call. Supports SSML tags for pauses and emphasis."
    voice_id:
      type: string
      description: "ElevenLabs voice ID. Use list_voices to discover available voices."
    language:
      type: string
      description: "Output language"
      enum: [pt-BR, en-US, en-GB, es-ES, fr-FR, de-DE]
    model_id:
      type: string
      description: "TTS model to use"
      enum: [eleven_multilingual_v2, eleven_turbo_v2_5, eleven_monolingual_v1]
    stability:
      type: number
      description: "Voice stability 0.0-1.0. Lower = more expressive, higher = more consistent."
    similarity_boost:
      type: number
      description: "Voice similarity 0.0-1.0. Higher = closer to original voice sample."
    style:
      type: number
      description: "Style exaggeration 0.0-1.0. Higher = more dramatic delivery."
    output_format:
      type: string
      description: "Audio output format"
      enum: [mp3_44100_128, mp3_44100_192, pcm_16000, pcm_24000, pcm_44100]
  required: [text, voice_id]
returns:
  type: object
  description: "Generated audio file metadata"
  properties:
    audio_url:
      type: string
      description: "URL to download the generated audio file"
    duration_seconds:
      type: number
      description: "Audio duration in seconds"
    characters_used:
      type: integer
      description: "Characters consumed from quota"
    format:
      type: string
      description: "Output audio format"
provider_compat: [openai, anthropic, gemini]
strict: false
domain: content_factory
quality: 9.0
tags: [function_def, elevenlabs, tts, audio, narration, content_factory]
tldr: "LLM-callable function to generate voiceover audio via ElevenLabs TTS — PT-BR/EN with emotion control"
examples:
  - input: {"text": "Bem-vindos ao modulo 3...", "voice_id": "pNInz6obpgDQGcFmaJgB", "language": "pt-BR", "model_id": "eleven_multilingual_v2"}
    output: {"audio_url": "https://api.elevenlabs.io/audio/abc123.mp3", "duration_seconds": 12.5, "characters_used": 280, "format": "mp3_44100_128"}
error_types: [text_too_long, voice_not_found, quota_exceeded, invalid_model, rate_limited]
density_score: 0.94
related:
  - p01_kc_elevenlabs_tts
  - bld_schema_research_pipeline
  - bld_schema_voice_pipeline
  - bld_schema_validation_schema
  - bld_schema_prosody_config
  - bld_schema_social_publisher
  - bld_schema_model_registry
  - bld_schema_dataset_card
  - p03_ch_content_pipeline
  - n06_schema_brand_config
---

# ElevenLabs Text-to-Speech Function

## Overview
Generates natural-sounding narration audio from text using ElevenLabs API. The LLM calls this when the Content Factory pipeline needs voiceover for video scripts, lesson narrations, or podcast intros. Supports multilingual output (PT-BR primary) with fine-grained control over voice expressiveness.

## Parameters

### text
Type: string | Required: yes
The narration text. Max 5000 characters. Supports SSML: `<break time="500ms"/>` for pauses, `<emphasis>` for stress. Split longer scripts into multiple calls.

### voice_id
Type: string | Required: yes
ElevenLabs voice identifier. Common IDs: `pNInz6obpgDQGcFmaJgB` (Adam), `21m00Tcm4TlvDq8ikWAM` (Rachel). Use list_voices endpoint to discover all.

### language
Type: string (enum) | Required: no | Default: pt-BR
Target language. Model `eleven_multilingual_v2` required for non-English.

### model_id
Type: string (enum) | Required: no | Default: eleven_multilingual_v2
TTS model. `eleven_multilingual_v2` for multi-language, `eleven_turbo_v2_5` for fast English.

### stability / similarity_boost / style
Type: number (0.0-1.0) | Required: no
Voice control knobs. Recommended starting point: stability=0.5, similarity_boost=0.75, style=0.3.

### output_format
Type: string (enum) | Required: no | Default: mp3_44100_128
Audio format. Use `pcm_44100` for video assembly (FFmpeg), `mp3_44100_192` for standalone distribution.

## Returns
Type: object with `audio_url`, `duration_seconds`, `characters_used`, `format`.

## Examples

### Example 1: PT-BR lesson narration
```json
{"text": "Neste modulo, voce vai aprender a construir agentes autonomos com ferramentas e memoria.", "voice_id": "pNInz6obpgDQGcFmaJgB", "language": "pt-BR", "stability": 0.6, "similarity_boost": 0.8}
```

### Example 2: English video hook with dramatic delivery
```json
{"text": "You're losing 2 hours of focus every morning. And you don't even know it.", "voice_id": "21m00Tcm4TlvDq8ikWAM", "language": "en-US", "model_id": "eleven_turbo_v2_5", "style": 0.7, "output_format": "pcm_44100"}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_elevenlabs_tts]] | upstream | 0.33 |
| [[bld_schema_research_pipeline]] | downstream | 0.26 |
| [[bld_schema_voice_pipeline]] | downstream | 0.26 |
| [[bld_schema_validation_schema]] | downstream | 0.24 |
| [[bld_schema_prosody_config]] | downstream | 0.24 |
| [[bld_schema_social_publisher]] | downstream | 0.24 |
| [[bld_schema_model_registry]] | downstream | 0.24 |
| [[bld_schema_dataset_card]] | downstream | 0.23 |
| [[p03_ch_content_pipeline]] | upstream | 0.23 |
| [[n06_schema_brand_config]] | downstream | 0.23 |
