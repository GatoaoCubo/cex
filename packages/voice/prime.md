# Voice Agent | PRIME

## PURPOSE

**VOICE_AGENT**: Accessibility-first voice interface for CODEXA. Enables hands-free interaction with Claude Code.

**Provides**: Voice-to-text | Text-to-speech | Noise filtering

**Philosophy**: Simple, reliable, one command at a time. User speaks "desires", Claude orchestrates.

**Activation**: `/v`

## ARCHITECTURE (v7.0 - Beep-Only UX)

```
+-------------------------------------------------------------+
|                      /v FLOW (v7.0)                          |
+-------------------------------------------------------------+
|                                                              |
|  1. User types /v                                            |
|         |                                                    |
|         v                                                    |
|  2. BEEP (800Hz) - recording starts immediately              |
|         |                                                    |
|         v                                                    |
|  3. User speaks freely (15s window, no wake word)            |
|         |                                                    |
|         v                                                    |
|  4. BEEP (1200Hz) - recording ended                          |
|         |                                                    |
|         v                                                    |
|  5. Whisper transcribes                                      |
|         |                                                    |
|         v                                                    |
|  6. Claude interprets as "desire/intent"                     |
|         |                                                    |
|         +--- Clear? -> Execute, speak response               |
|         |                                                    |
|         +--- Unclear? -> "Nao entendi. Repita."              |
|                         +-> Listen again                     |
|                                                              |
|  7. Return to chat (user types /v for next command)          |
|                                                              |
+-------------------------------------------------------------+
```

## KEY FILES

| File | Purpose |
|------|---------|
| `voice/server.py` | MCP server |
| `voice/stt.py` | Speech-to-text |
| `voice/tts.py` | Text-to-speech |
| `voice/voice_filter.py` | Noise filter (wake word disabled) |
| `voice/config.py` | Configuration |

## INSTRUCTIONS FOR AI

### When /v is called:

1. **NO TTS greeting** - just start listening immediately
2. **Start listening**: `mcp__voice__listen_start(max_duration=15, initial_timeout=5)`
   - BEEP plays automatically when recording starts
3. **Poll until done**: Keep calling `mcp__voice__listen_poll(session_id)`
4. **Handle result**:
   - `VOICE_COMMAND: {text}` -> Execute user's intent, speak short response
   - `NOISE_FILTERED` or `INVALID_COMMAND` -> Speak "Nao entendi. Repita." and listen again
   - `EXIT_VOICE_LOOP` -> Speak "Ate logo", stop
   - `NO_SPEECH_DETECTED` -> Return to chat silently
5. **Return to chat**

### Response Rules

- Keep TTS to 1-2 sentences
- Confirm actions: "Feito", "3 arquivos"
- User cannot see screen - be descriptive
- On unclear input: "Nao entendi. Repita por favor."

## FEEDBACK SIGNALS

| Signal | Meaning |
|--------|---------|
| BEEP 800Hz | Recording started - speak now |
| BEEP 1200Hz | Recording ended - processing |
| BEEP 400Hz | Timeout - no speech detected |

## EXIT COMMANDS

parar, sair, exit, quit, stop, tchau

## CONFIGURATION

```bash
# In .env (v7.0 defaults)
WAKE_WORD_ENABLED=false   # No wake word needed
STT_LANGUAGE=pt
STT_MAX_DURATION=15
EDGE_VOICE=pt-BR-FranciscaNeural
```

---

**Version**: 7.0.0
**Created**: 2025-11-27
**Updated**: 2025-11-30
**Agent Type**: Voice Interface
**Architecture**: Beep-only feedback, single capture per /v
**Dependencies**: sounddevice, edge-tts, ElevenLabs API
