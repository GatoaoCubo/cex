# Voice Agent — Tools and APIs

**Type**: TOOLS_AND_APIS | **Version**: 1.0.0

## Core Voice Stack

| Component | Technology | Config |
|-----------|-----------|--------|
| STT Engine | OpenAI Whisper (local) | `STT_LANGUAGE=pt`, `STT_MAX_DURATION=15` |
| TTS Primary | Edge TTS | `EDGE_VOICE=pt-BR-FranciscaNeural` |
| TTS Premium | ElevenLabs | `ELEVENLABS_API_KEY` (optional) |
| Audio I/O | System microphone + speaker | OS-level permissions required |

## MCP Server

| Endpoint | Purpose |
|----------|---------|
| `server.py` | Voice command MCP server — exposes voice tools to Claude Code |

## Voice Files

| File | Purpose | Location |
|------|---------|----------|
| `server.py` | MCP server for voice commands | `voice/server.py` |
| `stt.py` | Speech-to-text with beep feedback | `voice/stt.py` |
| `tts.py` | Text-to-speech for responses | `voice/tts.py` |
| `voice_filter.py` | Noise filtering (wake word disabled) | `voice/voice_filter.py` |
| `config.py` | Centralized configuration | `voice/config.py` |

## Audio Feedback Signals

| Signal | Frequency | Meaning |
|--------|-----------|---------|
| Start beep | 800Hz | Recording started — speak now |
| End beep | 1200Hz | Recording ended — processing |
| Timeout beep | 400Hz | No speech detected |

## Claude Code Tools (Available via Voice)

All standard Claude Code tools are accessible through voice commands:

| Tool | Voice Example |
|------|--------------|
| Read | "Le o arquivo config ponto py" |
| Write | "Cria um arquivo teste ponto md" |
| Bash | "Roda git status" |
| Grep | "Procura por TODO no codigo" |
| Glob | "Lista todos os arquivos markdown" |

## Environment Variables

| Variable | Default | Purpose |
|----------|---------|---------|
| `WAKE_WORD_ENABLED` | `false` | No wake word in v7.0 |
| `STT_LANGUAGE` | `pt` | Whisper language |
| `STT_MAX_DURATION` | `15` | Max recording seconds |
| `EDGE_VOICE` | `pt-BR-FranciscaNeural` | TTS voice selection |
| `ELEVENLABS_API_KEY` | (none) | Optional premium TTS |

## Integration

| Agent/System | Relationship |
|-------------|-------------|
| Claude Code | Voice is I/O layer — all tools accessible |
| ATLAS satellite | Voice agent runs under ATLAS (execution) |
| `/v` command | User-facing trigger |

---

*Voice Agent v7.0.0 — ATLAS — 2026-03-05*
