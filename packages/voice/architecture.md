# Voice Agent — Architecture

**Type**: ARCHITECTURE | **Version**: 1.0.0

## System Architecture (v7.0 — Beep-Only)

```
+---------------------------------------------------------------+
|                    VOICE AGENT v7.0                            |
+---------------------------------------------------------------+
|                                                                |
|  +-----------+    +-----------+    +-----------+               |
|  |  /v CMD   | -> | RECORDER  | -> |  WHISPER  |              |
|  | (trigger) |    | (15s max) |    |   (STT)   |              |
|  +-----------+    +-----------+    +-----------+               |
|                                          |                     |
|                                          v                     |
|                                   +-----------+                |
|                                   |  INTENT   |                |
|                                   |  PARSER   |                |
|                                   +-----------+                |
|                                    |         |                 |
|                              Clear?|    Unclear?               |
|                                    v         v                 |
|                             +-----------+ +-----------+        |
|                             | EXECUTOR  | |  RETRY    |        |
|                             | (Claude)  | | LISTENER  |        |
|                             +-----------+ +-----------+        |
|                                    |                           |
|                                    v                           |
|                             +-----------+                      |
|                             |   TTS     |                      |
|                             | (EdgeTTS) |                      |
|                             +-----------+                      |
|                                    |                           |
|                              [Return to chat]                  |
+---------------------------------------------------------------+
```

## Component Breakdown

### 1. Trigger Layer

| Component | Purpose |
|-----------|---------|
| `/v` command | Activates single-capture voice mode |
| Beep 800Hz | Signals recording start |
| Beep 1200Hz | Signals recording end |
| Beep 400Hz | Signals timeout (no speech) |

### 2. Audio Capture

| Component | Purpose |
|-----------|---------|
| Recorder | Captures microphone audio for up to 15 seconds |
| Noise Filter | Removes background noise (wake word disabled in v7.0) |
| Silence Detector | Ends recording on 2s silence gap |

### 3. Speech-to-Text (STT)

| Component | Purpose |
|-----------|---------|
| Whisper | OpenAI Whisper for PT-BR transcription |
| Language Config | `STT_LANGUAGE=pt` for Brazilian Portuguese |
| Duration Limit | `STT_MAX_DURATION=15` seconds |

### 4. Intent Parser

| Component | Purpose |
|-----------|---------|
| Claude LLM | Interprets transcription as desire/intent |
| Exit Detection | Recognizes: parar, sair, exit, quit, stop, tchau |
| Clarity Check | Routes to retry if intent unclear |

### 5. Text-to-Speech (TTS)

| Component | Purpose |
|-----------|---------|
| Edge TTS | Primary: `pt-BR-FranciscaNeural` voice |
| ElevenLabs | Optional: Higher quality with API key |

## Data Flow

```
User speaks -> Microphone -> WAV buffer -> Whisper STT
    -> Text transcript -> Claude intent parser
    -> Command execution -> Response text
    -> Edge TTS -> Speaker output -> Return to chat
```

## File Map

| File | Layer | Purpose |
|------|-------|---------|
| `server.py` | MCP | Voice command MCP server |
| `stt.py` | STT | Speech-to-text with beep feedback |
| `tts.py` | TTS | Text-to-speech response |
| `voice_filter.py` | Audio | Noise filtering |
| `config.py` | Config | Centralized settings |

---

*Voice Agent v7.0.0 — ATLAS — 2026-03-05*
