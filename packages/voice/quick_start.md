# Voice Agent | Quick Start

**Version**: 2.0.0 | **Updated**: 2025-12-09 | **Type**: Voice Interface

---

## Overview

Voice Agent enables hands-free interaction with CODEXA through speech recognition and text-to-speech. It serves as the accessibility layer for all agents, allowing voice commands to trigger workflows.

**Core Mission**: Make CODEXA accessible through voice interaction.

---

## Quick Commands

```bash
# Start voice mode (single capture)
/v

# Start continuous voice session
/vstart

# Stop voice session
/vstop

# Check voice status
/vstatus

# Voice GUI interface
/vgui
```

---

## Voice Modes

### 1. Single Capture (/v)
```
User speaks -> Transcribed -> Processed -> Response (text)
```
Best for: Quick commands, short queries

### 2. Continuous Session (/vstart)
```
User speaks -> Response -> User speaks -> Response -> ...
     ^                                           |
     +------------- Loop until /vstop -----------+
```
Best for: Extended conversations, hands-free work

### 3. GUI Mode (/vgui)
```
Visual interface + Voice input
- See transcription in real-time
- Visual feedback for listening state
- Manual override available
```

---

## Voice Commands to Agent Routing

| Voice Command | Routed To | Example |
|---------------|-----------|---------|
| "criar anuncio..." | anuncio_agent | "criar anuncio para fone bluetooth" |
| "pesquisar..." | pesquisa_agent | "pesquisar concorrentes de skincare" |
| "ajuda com..." | mentor_agent | "ajuda com precificacao" |
| "criar marca..." | marca_agent | "criar marca para pet shop" |
| "foto de produto..." | photo_agent | "foto de produto para oculos" |

### Trigger Keywords

```yaml
anuncio_agent: ["anuncio", "listing", "criar copy", "marketplace"]
pesquisa_agent: ["pesquisar", "analisar", "concorrentes", "mercado"]
mentor_agent: ["ajuda", "duvida", "como fazer", "ensinar"]
marca_agent: ["marca", "branding", "identidade", "logo"]
photo_agent: ["foto", "imagem", "produto visual"]
video_agent: ["video", "reels", "shorts", "youtube"]
```

---

## Technical Architecture

```
+--------------+     +--------------+     +--------------+
|  Microphone  | --> |  STT Engine  | --> |  Intent      |
|  (system)    |     |  (Whisper)   |     |  Parser      |
+--------------+     +--------------+     +--------------+
                                                 |
                                                 v
+--------------+     +--------------+     +--------------+
|  Speaker     | <-- |  TTS Engine  | <-- |  Response    |
|  (system)    |     |  (ElevenLabs)|     |  Generator   |
+--------------+     +--------------+     +--------------+
```

### Session Flow

```
1. listen_start()    -> Start recording (non-blocking)
2. listen_poll(id)   -> Check if recording complete
3. [transcription]   -> Get text from audio
4. intent_parse()    -> Determine target agent
5. route_to_agent()  -> Execute with appropriate agent
6. speak(response)   -> TTS output
```

---

## Configuration

### Voice Settings

```json
{
  "stt": {
    "engine": "whisper",
    "language": "pt-BR",
    "model": "base"
  },
  "tts": {
    "engine": "elevenlabs",
    "voice_id": "your-voice-id",
    "language": "pt-BR"
  },
  "session": {
    "timeout_seconds": 30,
    "max_recording_seconds": 60,
    "auto_punctuation": true
  }
}
```

### Language Support

| Language | STT | TTS | Status |
|----------|-----|-----|--------|
| Portuguese (BR) | yes | yes | Primary |
| English | yes | yes | Supported |
| Spanish | yes | partial | Partial |

---

## Integration Examples

### Example 1: Voice-Triggered Listing

```
User: "Criar anuncio para fone bluetooth gamer"

Voice Agent:
1. Transcribe -> "Criar anuncio para fone bluetooth gamer"
2. Parse intent -> anuncio_agent
3. Extract product -> "fone bluetooth gamer"
4. Route -> anuncio_agent with context
5. Receive output -> listing content
6. Speak summary -> "Anuncio criado com titulo..."
```

### Example 2: Voice Q&A with Mentor

```
User: "Como melhorar a taxa de conversao?"

Voice Agent:
1. Transcribe -> "Como melhorar a taxa de conversao?"
2. Parse intent -> mentor_agent (question)
3. Route -> mentor_agent
4. Receive answer -> detailed response
5. Speak answer -> TTS output
```

---

## Troubleshooting

### Common Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| No transcription | Mic not detected | Check system permissions |
| Poor accuracy | Background noise | Use noise cancellation |
| TTS not working | API key missing | Configure elevenlabs key |
| Session timeout | Long pause | Increase timeout_seconds |

### Debug Mode

```bash
/vstatus  # Check current session state

# Output:
Voice Status:
- Session: active
- Recording: false
- Last transcription: "criar anuncio..."
- Engine: whisper (pt-BR)
```

---

## Accessibility Features

- **Hands-free operation**: Full CODEXA control via voice
- **Screen reader compatible**: Works with assistive tech
- **Customizable TTS**: Adjust speed, voice, volume
- **Fallback to text**: Always available as backup

---

## Related Resources

- **Commands**: `/v`, `/vstart`, `/vstop`, `/vstatus`, `/vgui`
- **Config**: `data/voice_config.yaml`
- **Architecture**: `architecture.md`
- **Instructions**: `instructions.md`

---

**Your voice, your command.**
