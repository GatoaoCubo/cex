---
id: n00_audio_tool_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "Audio Tool -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, audio_tool, p04, n00, archetype, template]
density_score: 1.0
related:
  - p01_kc_audio_tool
  - bld_schema_audio_tool
  - audio-tool-builder
  - p04_audio_tool_NAME
  - p03_sp_audio_tool_builder
  - p04_audio_whisper
  - bld_schema_tts_provider
  - bld_schema_stt_provider
  - bld_knowledge_card_audio_tool
  - bld_examples_audio_tool
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An audio_tool provides agents with speech-to-text transcription, text-to-speech synthesis, and audio analysis capabilities, abstracting provider APIs (Whisper, ElevenLabs, AssemblyAI) into a unified tool interface. It handles audio format conversion, chunking for long files, and confidence scoring for transcription quality. The output is a structured tool module that agents call to process or generate audio content.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `audio_tool` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| capabilities | list | yes | Supported operations: stt, tts, analysis, diarization |
| provider | string | yes | Backend provider: whisper, elevenlabs, assemblyai, azure |
| supported_formats | list | yes | Input/output audio formats: mp3, wav, ogg, flac |
| language_support | list | no | ISO language codes supported |

## When to use
- When building voice-enabled agents that need STT or TTS integration
- When processing meeting recordings, podcasts, or customer call audio
- When a voice_pipeline requires a discrete audio processing component

## Builder
`archetypes/builders/audio_tool-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind audio_tool --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: at_whisper_stt_en
kind: audio_tool
pillar: P04
nucleus: n05
title: "Whisper STT Tool (English)"
version: 1.0
quality: null
---
capabilities: [stt, diarization]
provider: whisper
supported_formats: [mp3, wav, m4a, ogg]
language_support: [en, pt, es]
```

## Related kinds
- `stt_provider` (P04) -- provider-specific STT configuration used by audio_tool
- `tts_provider` (P04) -- provider-specific TTS configuration used by audio_tool
- `voice_pipeline` (P04) -- end-to-end voice architecture that chains audio_tools
- `multimodal_prompt` (P03) -- prompt that receives audio_tool transcription output

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_audio_tool]] | sibling | 0.48 |
| [[bld_schema_audio_tool]] | downstream | 0.46 |
| [[audio-tool-builder]] | related | 0.44 |
| [[p04_audio_tool_NAME]] | related | 0.44 |
| [[p03_sp_audio_tool_builder]] | related | 0.43 |
| [[p04_audio_whisper]] | related | 0.42 |
| [[bld_schema_tts_provider]] | downstream | 0.42 |
| [[bld_schema_stt_provider]] | downstream | 0.42 |
| [[bld_knowledge_card_audio_tool]] | sibling | 0.41 |
| [[bld_examples_audio_tool]] | downstream | 0.41 |
