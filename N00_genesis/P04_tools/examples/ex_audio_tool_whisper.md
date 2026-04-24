---
id: p04_audio_whisper
kind: audio_tool
8f: F5_call
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Whisper Speech-to-Text"
direction: input
models:
  - whisper-1
  - whisper-large-v3
formats:
  - mp3
  - wav
  - ogg
  - m4a
  - webm
languages:
  - en
  - pt
  - es
quality: 9.0
tags: [audio_tool, whisper, stt, transcription]
tldr: "Whisper STT tool for transcribing audio to text, supporting 50+ languages via OpenAI API"
description: "Transcribes audio files to text using OpenAI Whisper with word-level timestamps"
sample_rate: 16000
max_duration: 600
streaming: false
word_timestamps: true
voice_id: null
provider: "OpenAI"
domain: "tool integration"
title: "Audio Tool Whisper"
density_score: 0.96
related:
  - bld_examples_audio_tool
  - bld_knowledge_card_audio_tool
  - audio-tool-builder
  - p01_kc_audio_tool
  - p04_audio_tool_NAME
  - p03_sp_audio_tool_builder
  - bld_knowledge_card_multi_modal_config
  - p10_lr_audio_tool_builder
  - p01_kc_multi_modal_config
  - p04_api_client_groq_whisper
---

# Whisper Speech-to-Text

## Overview
Transcribes audio files to text using OpenAI's Whisper model. Used by agents that process voice messages, meeting recordings, or audio content for downstream text analysis.

## Direction
Audio input -> Whisper model -> Text output with timestamps.
Audio file (mp3/wav/ogg) -> whisper-1 API -> `{"text": "...", "segments": [...]}`.
No streaming — full file must be uploaded before transcription begins.

## Models
| Model | Provider | Accuracy | Latency | Cost |
|-------|----------|----------|---------|------|
| whisper-1 | OpenAI | high | 1-5s | $0.006/min |
| whisper-large-v3 | local/HF | high | 5-30s | free (GPU required) |

## Formats
| Format | Input | Output | Notes |
|--------|-------|--------|-------|
| mp3 | yes | - | Most common, good compression |
| wav | yes | - | Lossless, larger files |
| ogg | yes | - | WhatsApp voice messages |
| m4a | yes | - | iOS recordings |
| webm | yes | - | Browser recordings |

## Languages
| Code | Language | whisper-1 | whisper-large-v3 |
|------|----------|-----------|-------------------|
| en | English | high | high |
| pt | Portuguese | high | high |
| es | Spanish | high | high |

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `audio tool`
- **Artifact ID**: `p04_audio_whisper`
- **Tags**: [audio_tool, whisper, stt, transcription]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `audio tool` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_audio_tool]] | downstream | 0.52 |
| [[bld_knowledge_card_audio_tool]] | upstream | 0.41 |
| [[audio-tool-builder]] | related | 0.41 |
| [[p01_kc_audio_tool]] | related | 0.41 |
| [[p04_audio_tool_NAME]] | sibling | 0.41 |
| [[p03_sp_audio_tool_builder]] | related | 0.35 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.35 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.34 |
| [[p01_kc_multi_modal_config]] | related | 0.34 |
| [[p04_api_client_groq_whisper]] | related | 0.34 |
