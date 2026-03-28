---
kind: examples
id: bld_examples_audio_tool
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of audio_tool artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: audio-tool-builder
## Golden Example
INPUT: "Create a speech-to-text tool using Whisper and Deepgram for transcription"
OUTPUT:
```yaml
id: p04_audio_speech_transcription
kind: audio_tool
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "EDISON"
name: "Speech Transcription Tool"
direction: input
models:
  - whisper_large_v3
  - deepgram_nova_2
formats: [mp3, wav, ogg, flac, webm, m4a]
languages: [en, pt-BR, es, fr, de, ja, zh]
quality: null
tags: [audio_tool, stt, transcription, whisper, deepgram, P04]
tldr: "STT tool: Whisper + Deepgram Nova-2, 7 languages, 6 formats, word timestamps, streaming"
description: "Speech-to-text transcription tool supporting Whisper large-v3 and Deepgram Nova-2 with word-level timestamps and streaming."
sample_rate: 16000
max_duration: 600
streaming: true
word_timestamps: true
provider: openai
```
## Overview
Transcribes audio input to text using Whisper large-v3 (OpenAI) or Deepgram Nova-2.
Used by voice interfaces, meeting recorders, and content pipelines requiring accurate multilingual transcription.
## Direction
Input (STT): audio bytes received -> format detected -> model selected -> transcription returned as text with optional word-level timestamps.
Streaming mode: audio chunks pushed in real-time, partial transcripts emitted as SSE events.
## Models
| Model | Provider | Accuracy | Latency | Cost |
|-------|----------|----------|---------|------|
| whisper_large_v3 | OpenAI | high | medium (2-8s) | $0.006/min |
| deepgram_nova_2 | Deepgram | high | low (<1s) | $0.0043/min |
## Formats
| Format | Input | Output | Notes |
|--------|-------|--------|-------|
| mp3 | yes | - | lossy, common upload format |
| wav | yes | - | lossless PCM, highest accuracy |
| ogg | yes | - | open format, good for web |
| flac | yes | - | lossless compressed |
| webm | yes | - | browser MediaRecorder default |
| m4a | yes | - | Apple ecosystem format |
## Languages
| Code | Language | Whisper | Deepgram |
|------|----------|---------|---------|
| en | English | high | high |
| pt-BR | Portuguese (Brazil) | high | medium |
| es | Spanish | high | medium |
| fr | French | high | medium |
| de | German | high | medium |
| ja | Japanese | medium | low |
| zh | Chinese (Mandarin) | medium | low |
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_audio_ pattern (H02 pass)
- kind: audio_tool (H04 pass)
- direction: input — valid enum (H06 pass)
- models list matches ## Models entries exactly (H07 pass)
- formats all within allowed enum (H08 pass)
- languages use BCP-47 codes (H09 pass)
- all 5 required body sections present (H10 pass)
- streaming: true declared (S04 pass)
- word_timestamps declared (S05 pass)
- tldr: 71 chars <= 160 (S01 pass)
- tags: 6 items, includes "audio_tool" (S02 pass)
## Anti-Example
INPUT: "Create audio tool for text to speech"
BAD OUTPUT:
```yaml
id: tts-tool
kind: tool
pillar: tools
name: TTS
models: [GPT-4o]
quality: 9.0
tags: [tts]
```
Converts text to audio.
## Models
GPT-4o: does text to speech
FAILURES:
1. id: "tts-tool" has hyphens and no `p04_audio_` prefix -> H02 FAIL
2. kind: "tool" not "audio_tool" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. Missing required fields: direction, formats, languages, version, created, updated, author, tldr -> H06 FAIL
6. tags: only 1 item, missing "audio_tool" -> S02 FAIL
7. direction not declared — caller cannot determine STT vs TTS vs analysis -> H06 FAIL
8. models: ["GPT-4o"] — GPT-4o is not an audio model; wrong model name -> H07 FAIL
9. formats not specified — consumer cannot send correct audio format -> H08 FAIL
10. languages not specified — multilingual support unknown -> H09 FAIL
11. Body missing ## Direction, ## Formats, ## Languages sections -> H10 FAIL
