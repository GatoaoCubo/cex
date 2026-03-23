# ADW-100: Voice Interaction Workflow | Voice Agent

> **Version**: 1.0.0 | **Agent**: voice_agent | **Type**: Agentic Developer Workflow

---

## IDENTITY

**Purpose**: Voice-based interaction with Claude Code
**Domain**: Speech-to-text, text-to-speech, voice commands
**Output**: Transcribed text, spoken responses, voice loop

---

## TRIGGER

```yaml
triggers:
  - command: /voice
  - command: /voice-start
  - command: /voice-stop
  - tool: mcp__voice__listen
  - tool: mcp__voice__speak
```

---

## WORKFLOW PHASES

### Phase 1: CAPTURE (user speech)

```yaml
phase: capture
objective: Record and transcribe user speech
actions:
  - Start audio recording
  - Detect speech activity
  - Stop on silence or max duration
  - Send to Whisper API for transcription

outputs:
  - transcript: Transcribed text
  - confidence: Transcription confidence
  - duration: Recording length
```

**Tools**:
- `mcp__voice__listen_start()` - Non-blocking start
- `mcp__voice__listen_poll()` - Check status
- `mcp__voice__listen()` - Blocking (legacy)

### Phase 2: PROCESS (Claude response)

```yaml
phase: process
objective: Generate response to user input
actions:
  - Parse transcribed text
  - Route to appropriate handler:
    - Command detection
    - Question answering
    - Task execution

outputs:
  - response_text: Claude's response
  - action_taken: What was done
```

### Phase 3: SPEAK (TTS response)

```yaml
phase: speak
objective: Convert response to speech
actions:
  - Select TTS provider (Edge TTS / ElevenLabs)
  - Generate audio from response text
  - Play audio to user

outputs:
  - audio_played: Boolean
  - duration: Playback length
```

**Tool**: `mcp__voice__speak({ text: "response" })`

### Phase 4: LOOP (continuous mode)

```yaml
phase: loop
objective: Maintain continuous voice conversation
actions:
  - After speaking, listen for next input
  - Repeat capture -> process -> speak
  - Exit on "stop" or "exit" command

outputs:
  - session_duration: Total conversation time
  - turns: Number of exchanges
```

**Tool**: `mcp__voice__start_voice_loop()`

---

## EXECUTION MODES

### Single Command

```javascript
// Listen once, respond, done
mcp__voice__listen()
// Process transcript
mcp__voice__speak("Response here")
```

### Non-blocking (Recommended)

```javascript
// Start recording in background
const session = mcp__voice__listen_start()

// Poll for completion
while (true) {
  const status = mcp__voice__listen_poll(session.session_id)
  if (status.status === "done") {
    // Process transcript
    break
  }
  // Continue other work
}
```

### Continuous Loop

```javascript
// Start voice loop with greeting
mcp__voice__start_voice_loop({
  greeting: "Voice mode activated. Speak your command."
})

// Loops until user says "exit" or "stop"
```

---

## QUALITY GATES

```yaml
quality_gates:
  transcription:
    - confidence > 0.7
    - no timeout (speech detected)

  tts:
    - audio plays successfully
    - response < 500 chars (for speed)
```

---

## CONFIGURATION

```json
{
  "language": "pt",
  "max_duration": 15,
  "initial_timeout": 3,
  "tts_provider": "edge-tts",
  "voice": "pt-BR-FranciscaNeural",
  "speed": 1.0
}
```

---

## ERROR HANDLING

| Error | Response |
|-------|----------|
| No speech detected | "Nao ouvi nada. Tente novamente." |
| Transcription failed | "Desculpe, nao consegui entender." |
| TTS failed | Fall back to text response |

---

## ACCESSIBILITY

Voice agent enables:
- Hands-free coding assistance
- Accessibility for users with mobility issues
- Faster interaction for quick commands

---

## INTEGRATION

**Upstream**: User microphone input
**Downstream**: Claude Code commands, other agents

---

**Created by**: voice_agent v1.0.0
**Last Updated**: 2025-11-30
