# Voice Agent | Instructions v7.0

## Quick Start

```
/v
```

This plays a beep, listens for ONE voice command, executes it, responds via TTS, then returns control.

## How It Works (v7.0 - Beep-Only)

```
1. /v called
2. BEEP (800Hz) - recording starts immediately (NO TTS greeting)
3. Claude listens (15s max, no wake word needed)
4. User speaks freely: "liste os arquivos"
5. BEEP (1200Hz) - recording ended
6. Whisper transcribes
7. Claude executes the command
8. Claude speaks response: "5 arquivos encontrados"
9. Control returns to chat
10. User types /v for next command
```

## Key Differences from v6.0

- **NO TTS greeting** - beep replaces "Pode falar."
- **NO wake word** - speak directly after beep
- **Beep feedback** - audio cues replace voice prompts during listening
- **Manual control** - user types /v for each command

## Exit Commands

Say any of: parar, sair, exit, quit, stop, tchau

## MCP Tools Used

```python
mcp__voice__speak("text")           # TTS for responses only
mcp__voice__listen_start()          # Start recording (auto-beeps)
mcp__voice__listen_poll(session_id) # Check status
```

## Filter Results

| Result | Meaning |
|--------|---------|
| `VOICE_COMMAND: {text}` | Valid command - execute it |
| `NOISE_FILTERED` | Background noise - say "Nao entendi. Repita." |
| `INVALID_COMMAND` | Unclear speech - say "Nao entendi. Repita." |
| `EXIT_VOICE_LOOP` | Exit command - say "Ate logo" |
| `NO_SPEECH_DETECTED` | Timeout - return to chat silently |

## Response Guidelines

- Keep TTS responses to 1-2 sentences
- Confirm actions: "Feito", "3 arquivos"
- User cannot see screen - be descriptive
- On unclear input: "Nao entendi. Repita por favor."

## Feedback Signals

| Signal | Meaning |
|--------|---------|
| BEEP 800Hz | Recording started - speak now |
| BEEP 1200Hz | Recording ended - processing |
| BEEP 400Hz | Timeout - no speech detected |

## Configuration

Edit `.env` or `voice/config.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `WAKE_WORD_ENABLED` | false | NO wake word in v7.0 |
| `STT_LANGUAGE` | pt | Language code |
| `STT_MAX_DURATION` | 15 | Recording duration (seconds) |
| `EDGE_VOICE` | pt-BR-FranciscaNeural | TTS voice |

---

**Version**: 7.0.0
**Updated**: 2025-11-30
**Architecture**: Beep-only feedback, single capture per /v
