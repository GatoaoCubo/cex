---
id: p04_api_client_groq_whisper
kind: api_client
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
---

# Client: Groq Whisper

## Connection
- Base URL: https://api.groq.com/openai/v1
- Auth: Bearer token (GROQ_API_KEY env var)
- Timeout: 30s

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
