---
kind: knowledge_card
id: bld_knowledge_card_audio_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for audio_tool production — audio processing tool specification
sources: OpenAI Whisper docs, ElevenLabs API, Google Speech-to-Text, Azure Cognitive Speech, Deepgram docs, AssemblyAI docs
quality: 9.1
title: "Knowledge Card Audio Tool"
version: "1.0.0"
author: n03_builder
tags: [audio_tool, builder, examples]
tldr: "Golden and anti-examples for audio tool construction, demonstrating ideal structure and common pitfalls."
domain: "audio tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_audio_tool_builder
  - bld_instruction_audio_tool
  - bld_config_audio_tool
  - p10_lr_audio_tool_builder
  - bld_examples_audio_tool
  - bld_schema_audio_tool
  - p01_kc_audio_tool
  - bld_collaboration_audio_tool
  - audio-tool-builder
  - p04_audio_tool_NAME
---

# Domain Knowledge: audio_tool
## Executive Summary
Audio tools process audio signals: converting speech to text (STT), generating speech from text (TTS), or analyzing audio features (speaker diarization, emotion, language detection). They are direction-specific, model-bound, format-constrained, and language-scoped. Audio tools are NOT notifiers (message delivery), NOT vision_tools (image/video), NOT cli_tools (terminal executables).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Directions | input (STT), output (TTS), analysis, bidirectional |
| Standard sample_rate | 16000 Hz (STT), 22050/44100 Hz (TTS) |
| Max body | 2048 bytes |
| Language codes | BCP-47 (en, pt-BR, es, fr, de, ja, zh, ko, it, nl) |
## Direction Reference
| Direction | Meaning | Input | Output |
|-----------|---------|-------|--------|
| input | Speech-to-text (STT) | audio bytes | text string |
| output | Text-to-speech (TTS) | text string | audio bytes |
| analysis | Feature extraction | audio bytes | structured JSON |
| bidirectional | STT + TTS both | audio or text | text or audio |
## Model Reference
| Model ID | Provider | Direction | Notes |
|----------|----------|-----------|-------|
| whisper_large_v3 | OpenAI | input | Best multilingual accuracy, 99 languages |
| whisper_large_v3_turbo | OpenAI | input | 8x faster, slight accuracy trade-off |
| tts_1 | OpenAI | output | Low latency, 6 voices |
| tts_1_hd | OpenAI | output | High fidelity, 6 voices |
| eleven_multilingual_v2 | ElevenLabs | output | 29 languages, voice cloning |
| eleven_turbo_v2_5 | ElevenLabs | output | Ultra-low latency (<400ms) |
| google_chirp | Google | input | 100+ languages, Chirp architecture |
| google_chirp_2 | Google | input | Next-gen, better noise robustness |
| azure_neural_hd | Azure | output | 140+ voices, SSML support |
| azure_whisper | Azure | input | Whisper-based Azure deployment |
| deepgram_nova_2 | Deepgram | input | <300ms latency, streaming |
| deepgram_nova_2_medical | Deepgram | input | Medical vocabulary specialization |
| assemblyai_best | AssemblyAI | input | Best accuracy, speaker diarization |
| assemblyai_nano | AssemblyAI | input | Fast + cheap, lower accuracy |
## Format Compatibility
| Format | STT Input | TTS Output | Notes |
|--------|-----------|------------|-------|
| mp3 | yes | yes | Most common; lossy compression |
| wav | yes | yes | Lossless PCM; best STT accuracy |
| ogg | yes | yes | Open format; good web compatibility |
| flac | yes | no | Lossless compressed; STT only |
| webm | yes | no | Browser MediaRecorder default |
| m4a | yes | no | Apple ecosystem; AAC codec |
| aac | yes | yes | Efficient lossy compression |
| pcm | yes | yes | Raw samples; lowest latency |
## Patterns
- **STT**: audio → 16kHz normalize → model → text + timestamps
- **TTS**: text → SSML optional → model → audio bytes
- **Streaming**: chunked audio → partial transcripts (Deepgram/AssemblyAI WebSocket)
## Anti-Patterns
| Anti-Pattern | Why |
|---|---|
| GPT-4o as audio model id | LLM, not audio model |
| direction: "stt" | Enum: input/output/analysis/bidirectional |
| languages: ["English"] | Must use BCP-47: "en" |
| formats: ["audio/*"] | Must be explicit enum members |
| No sample_rate | STT accuracy varies 16kHz vs 44.1kHz |
## Application
1. Determine direction (STT/TTS/analysis)
2. Select models matching direction + language + latency
3. Specify formats, languages (BCP-47), streaming, sample_rate
4. Validate: id pattern, kind, direction enum, model names

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_audio_tool_builder]] | downstream | 0.54 |
| [[bld_instruction_audio_tool]] | downstream | 0.53 |
| [[bld_config_audio_tool]] | downstream | 0.53 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.52 |
| [[bld_examples_audio_tool]] | downstream | 0.50 |
| [[bld_schema_audio_tool]] | downstream | 0.49 |
| [[p01_kc_audio_tool]] | sibling | 0.49 |
| [[bld_collaboration_audio_tool]] | downstream | 0.49 |
| [[audio-tool-builder]] | downstream | 0.49 |
| [[p04_audio_tool_NAME]] | downstream | 0.43 |
