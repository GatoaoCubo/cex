---
id: p04_client_groq_whisper
name: groq_whisper_client
description: "API client for Groq audio transcription via whisper-large-v3 — used by WhatsApp monitor for voice messages"
base_url: "https://api.groq.com/openai/v1"
auth_method: api_key
endpoints:
  - path: /audio/transcriptions
    method: POST
    content_type: multipart/form-data
lp: P04
type: client
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: edison
domain: audio-transcription
quality: 9.0
tags: [client, groq, whisper, transcription, audio, whatsapp]
---

# Groq Whisper Client — Audio Transcription

## Purpose
Unidirectional API client that sends audio files (OGG/MP3) to Groq's whisper-large-v3 model for transcription. Integrated into the CODEXA WhatsApp Monitor daemon for real-time voice message processing.

## Endpoint
```
POST https://api.groq.com/openai/v1/audio/transcriptions
Authorization: Bearer $GROQ_API_KEY
Content-Type: multipart/form-data
```

## Request
```python
requests.post(
    "https://api.groq.com/openai/v1/audio/transcriptions",
    headers={"Authorization": "Bearer " + GROQ_KEY},
    files={"file": (filename, file_bytes, "audio/ogg")},
    data={"model": "whisper-large-v3", "language": "pt"},
    timeout=30,
)
```

## Configuration
- **Auth**: `GROQ_API_KEY` env var (fallback: reads from `.env` file)
- **Model**: `whisper-large-v3` (Portuguese language default)
- **Timeout**: 30 seconds
- **Formats**: OGG (WhatsApp native), MP3

## Integration
Used by `records/framework/whatsapp/wa_monitor.py` — polls WhatsApp bridge every 5s, detects audio messages, transcribes via Groq, logs transcript and writes signal file for CODEXA wake-on-message pattern.
