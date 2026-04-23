---
id: p04_audio_tool_NAME
kind: audio_tool
pillar: P04
version: 1.0.0
title: "Template — Audio Tool"
tags: [template, audio, tool, tts, stt, transcription]
tldr: "Configures an audio processing tool: TTS, STT, or transcription. Defines provider, model, language, format, and quality thresholds."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.96
related:
  - bld_knowledge_card_audio_tool
  - p01_kc_audio_tool
  - bld_examples_audio_tool
  - p04_audio_whisper
  - audio-tool-builder
  - bld_schema_audio_tool
  - bld_collaboration_audio_tool
  - stt-provider-builder
  - bld_knowledge_card_stt_provider
  - bld_schema_tts_provider
---

# Audio Tool: [NAME]

## Purpose
[WHAT audio task this tool handles — transcription, synthesis, or analysis]

## Configuration
```yaml
provider: [openai | elevenlabs | whisper | deepgram]
model: [whisper-large-v3 | tts-1-hd | nova-2]
mode: [transcribe | synthesize | analyze]
language: [en | pt-BR | auto-detect]
format: [mp3 | wav | ogg | flac]
sample_rate: [16000 | 22050 | 44100]
max_duration_s: [60 | 300 | 3600]
```

## Capabilities

| Capability | Supported | Notes |
|------------|-----------|-------|
| Transcription (STT) | [yes\|no] | [Accuracy target: WER < 5%] |
| Synthesis (TTS) | [yes\|no] | [Voice: alloy, echo, fable, onyx] |
| Speaker diarization | [yes\|no] | [Max speakers: N] |
| Timestamp alignment | [yes\|no] | [Word-level or segment-level] |
| Streaming | [yes\|no] | [Latency target: <500ms] |

## Error Handling
- **Audio too long**: Split at silence boundaries, process chunks
- **Bad format**: Convert to WAV 16kHz mono before processing
- **Low quality audio**: Warn + proceed with lower confidence threshold
- **Provider timeout**: Retry 2x with exponential backoff

## Quality Gate
- [ ] Provider and model specified
- [ ] Language explicitly set (no silent default)
- [ ] Max duration defined (prevents runaway costs)
- [ ] Error handling for common failures

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_audio_tool]] | upstream | 0.41 |
| [[p01_kc_audio_tool]] | related | 0.41 |
| [[bld_examples_audio_tool]] | downstream | 0.39 |
| [[p04_audio_whisper]] | sibling | 0.38 |
| [[audio-tool-builder]] | related | 0.36 |
| [[bld_schema_audio_tool]] | downstream | 0.35 |
| [[bld_collaboration_audio_tool]] | downstream | 0.35 |
| [[stt-provider-builder]] | related | 0.33 |
| [[bld_knowledge_card_stt_provider]] | upstream | 0.32 |
| [[bld_schema_tts_provider]] | downstream | 0.31 |
