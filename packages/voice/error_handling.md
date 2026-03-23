# Voice Agent — Error Handling

**Type**: ERROR_HANDLING | **Version**: 1.0.0

## Error Categories

### Audio Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| No microphone detected | Hardware disconnected or permission denied | Display error message; suggest checking system audio settings |
| Recording timeout | No speech detected within 15s window | Play 400Hz beep; return to chat silently |
| Audio too quiet | Microphone gain too low | Prompt user to speak louder; adjust gain if possible |
| Audio clipping | Microphone too close or volume too high | Log warning; Whisper handles mild clipping gracefully |

### STT Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Whisper model not loaded | First run or model file missing | Auto-download model on first use; show progress |
| Transcription empty | Background noise only, no speech | Play 400Hz timeout beep; return to chat |
| Language mismatch | Non-Portuguese speech detected | Default to PT-BR; accept result and let Claude interpret |
| Whisper timeout | Audio too long or system overloaded | Truncate to 15s and retry once |

### Intent Parsing Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Intent unclear | Ambiguous transcription | TTS: "Nao entendi. Repita."; re-enter listen mode |
| Multiple intents detected | User gave compound command | Execute first intent; queue remainder |
| Exit command in mid-sentence | False positive exit detection | Check if exit word is standalone (not embedded in phrase) |

### TTS Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| Edge TTS unavailable | Network issue or service down | Fallback: print text response without voice |
| ElevenLabs quota exceeded | Monthly API limit reached | Fallback to Edge TTS automatically |
| Audio playback failed | Speaker unavailable or busy | Print text response; log audio error |

### System Errors

| Error | Cause | Recovery |
|-------|-------|----------|
| MCP server crash | Unhandled exception in server.py | Auto-restart MCP server; log crash details |
| Config missing | .env not found or incomplete | Use defaults: PT-BR, 15s, Edge TTS |
| Permission denied | OS blocks microphone access | Display system-specific instructions to grant access |

## Retry Policy

| Phase | Max Retries | Strategy |
|-------|-------------|----------|
| Audio capture | 1 | Re-trigger recording on silence timeout |
| STT transcription | 1 | Retry with same audio buffer |
| Intent parsing | 2 | Ask user to repeat ("Nao entendi. Repita.") |
| TTS output | 0 | Fallback to text immediately |
| MCP server | 1 | Auto-restart on crash |

## Graceful Degradation

```
Full mode:    Voice in -> STT -> Claude -> TTS -> Voice out
Fallback 1:   Voice in -> STT -> Claude -> Text out (TTS fails)
Fallback 2:   Text in  -> Claude -> Text out (STT fails)
```

---

*Voice Agent v7.0.0 — ATLAS — 2026-03-05*
