---
id: p04_api_client_groq_whisper
kind: api_client
8f: F5_call
name: groq_whisper
base_url: "https://api.groq.com/openai/v1"
auth_method: api_key
endpoints:
  - method: POST
    path: /audio/transcriptions
pillar: P04
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [client, groq, whisper, transcription, audio]
updated: "2026-04-07"
domain: "tool integration"
title: "Api Client Groq Whisper"
density_score: 0.92
tldr: "Defines api client for api client groq whisper, with validation gates and integration points."
related:
  - p04_audio_whisper
  - audio-tool-builder
  - p04_audio_tool_NAME
  - p01_kc_audio_tool
  - bld_knowledge_card_multi_modal_config
  - api-client-builder
  - p01_kc_multi_modal_config
  - bld_tools_model_provider
  - p10_lr_audio_tool_builder
  - bld_knowledge_card_audio_tool
---

# Client: Groq Whisper

## Connection
1. Base URL: https://api.groq.com/openai/v1
2. Auth: Bearer token (GROQ_API_KEY env var)
3. Timeout: 30s

## Operations
| Method | Endpoint | Purpose |
|--------|----------|---------|
| POST | /audio/transcriptions | Transcribe audio to text |

## Contract
```yaml
request:
  file: binary (OGG/MP3/WAV, max 25MB)
  model: "whisper-large-v3-turbo"
  language: "pt" (optional)
response:
  text: string (transcribed content)
```

## Usage
```python
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
result = client.audio.transcriptions.create(
    file=open("audio.ogg", "rb"),
    model="whisper-large-v3-turbo"
)
print(result.text)
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `api_client` |
| Pillar | P04 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_audio_whisper]] | related | 0.40 |
| [[audio-tool-builder]] | related | 0.31 |
| [[p04_audio_tool_NAME]] | related | 0.27 |
| [[p01_kc_audio_tool]] | related | 0.26 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.26 |
| [[api-client-builder]] | related | 0.24 |
| [[p01_kc_multi_modal_config]] | related | 0.24 |
| [[bld_tools_model_provider]] | related | 0.23 |
| [[p10_lr_audio_tool_builder]] | downstream | 0.23 |
| [[bld_knowledge_card_audio_tool]] | upstream | 0.23 |
