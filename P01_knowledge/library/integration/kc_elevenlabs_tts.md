---
id: p01_kc_elevenlabs_tts
kind: knowledge_card
type: domain
pillar: P01
title: "ElevenLabs TTS — Voice Synthesis for Content Factory"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: n04_knowledge
domain: elevenlabs_tts
quality: 9.1
tags: [elevenlabs, tts, voice, audio, content-factory, integration, INJECT]
tldr: "REST API for text-to-speech with multilingual models, voice cloning, and streaming — optimized for PT-BR narration"
when_to_use: "When any nucleus needs to generate spoken audio from text — narrations, podcasts, voiceovers"
keywords: [elevenlabs, tts, text-to-speech, voice-cloning, multilingual, streaming]
feeds_kinds: [api_client, audio_tool, workflow, dag]
linked_artifacts: [kc_ffmpeg_patterns, kc_youtube_api, kc_canva_connect_api]
density_score: null
---

# ElevenLabs TTS

## Quick Reference
```yaml
base_url: https://api.elevenlabs.io/v1
auth: xi-api-key header
models:
  - eleven_multilingual_v2    # Best quality, 29 languages, PT-BR excellent. ~300ms latency.
  - eleven_turbo_v2_5         # 32 languages, ~200ms latency. Slightly lower quality.
  - eleven_monolingual_v1     # English only, legacy.
  - eleven_flash_v2_5         # Fastest, ~75ms. Good for real-time.
rate_limit: 100 concurrent requests (paid), 2 concurrent (free)
output_format: mp3_44100_128 (default), pcm_16000, pcm_22050, pcm_24000, pcm_44100, ulaw_8000
```

## Core Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/text-to-speech/{voice_id}` | POST | Generate audio from text (returns audio bytes) |
| `/text-to-speech/{voice_id}/stream` | POST | Stream audio chunks (chunked transfer) |
| `/voices` | GET | List available voices |
| `/voices/{voice_id}` | GET | Get voice details |
| `/voices/add` | POST | Add cloned voice from audio samples |
| `/voice-generation/generate-voice` | POST | Generate random voice from description |
| `/user/subscription` | GET | Check quota remaining |
| `/history` | GET | List generated audio history |
| `/models` | GET | List available models |

## PT-BR Voices (Built-in, No Cloning Needed)

| Voice ID | Name | Style | Best For |
|----------|------|-------|----------|
| `EXAVITQu4vr4xnSDxMaL` | Sarah | Warm, conversational | Narration, courses |
| `onwK4e9ZLuTAKqWW03F9` | Daniel | Authoritative, clear | Business, tutorials |
| `TX3LPaxmHKxFdv7VOQHJ` | Liam | Young, energetic | Social content |
| `pFZP5JQG7iQjIQuC4Bku` | Lily | Soft, friendly | Podcasts, stories |

Note: multilingual_v2 auto-detects PT-BR from input text. No language parameter needed.

## Generate 5-Minute Narration Example

```python
import httpx

headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}

# ~750 words = ~5 min narration at normal speed
text = """Neste episódio, vamos explorar como a inteligência artificial
está transformando a criação de conteúdo digital..."""  # full script here

resp = httpx.post(
    "https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL",
    headers=headers,
    json={
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,        # 0=variable, 1=monotone. 0.5 is natural.
            "similarity_boost": 0.75, # 0=creative, 1=exact clone. 0.75 for consistency.
            "style": 0.3,            # 0=neutral, 1=exaggerated. Keep low for narration.
            "use_speaker_boost": True # Enhances clarity. Costs ~10% more chars.
        },
        "output_format": "mp3_44100_128"
    },
    timeout=120  # Long texts take time to synthesize
)

with open("narration.mp3", "wb") as f:
    f.write(resp.content)
```

## Streaming (for real-time playback)

```python
with httpx.stream("POST", f"{base_url}/text-to-speech/{voice_id}/stream",
    headers=headers,
    json={"text": text, "model_id": "eleven_turbo_v2_5"}
) as response:
    for chunk in response.iter_bytes(chunk_size=4096):
        audio_player.write(chunk)  # play as it arrives
```

## Voice Cloning

```python
files = [
    ("files", ("sample1.mp3", open("sample1.mp3", "rb"), "audio/mpeg")),
    ("files", ("sample2.mp3", open("sample2.mp3", "rb"), "audio/mpeg")),
]
data = {"name": "My Custom Voice", "description": "Brand narrator"}
resp = httpx.post(f"{base_url}/voices/add",
    headers={"xi-api-key": ELEVENLABS_API_KEY},
    data=data, files=files
)
custom_voice_id = resp.json()["voice_id"]
```

Requirements: 1-25 audio samples, each 1-10 min. Clean audio, single speaker, minimal background noise. Total recommended: 3-5 min of diverse speech.

## Pricing (per character)

| Plan | Characters/mo | Cost | Per 1K chars |
|------|--------------|------|-------------|
| Free | 10,000 | $0 | — |
| Starter | 30,000 | $5/mo | $0.17 |
| Creator | 100,000 | $22/mo | $0.22 |
| Pro | 500,000 | $99/mo | $0.20 |
| Scale | 2,000,000 | $330/mo | $0.17 |

A 5-minute narration (~750 words, ~4,500 chars) costs approximately $0.75-$1.00 on Creator plan.

## Gotchas

- **Character count includes spaces and punctuation.** A 1000-word text is ~6,000 chars, not ~5,000.
- **Multilingual_v2 is not turbo.** Expect 2-5x slower than turbo for the same text. Use turbo for drafts, multilingual for final.
- **Voice stability < 0.3 causes wild variation** between generations. Keep at 0.4-0.6 for consistent narration.
- **Max text per request: 5,000 chars.** For longer content, split into chunks and concatenate audio with FFmpeg.
- **Speaker boost doubles clarity but costs ~10% more characters.** Worth it for final exports, skip for drafts.
- **Cloned voices require Professional Voice License for commercial use.** Built-in voices are licensed for all commercial use on paid plans.
- **Rate limit errors (429)** return after ~10s. Implement exponential backoff starting at 1s.

## Docs
- API Reference: https://elevenlabs.io/docs/api-reference
- Voice Settings Guide: https://elevenlabs.io/docs/voice-lab/voice-settings
- Python SDK: `pip install elevenlabs` — wraps all endpoints with typed models
