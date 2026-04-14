---
kind: examples
id: bld_examples_realtime_session
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of realtime_session artifacts (LLM streaming, not video conf)
quality: 9.1
title: "Examples: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, examples, openai_realtime, websocket, webrtc]
tldr: "Golden example: OpenAI WebSocket realtime session. Anti-examples: generic model, missing VAD, raw API key."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Golden Example: OpenAI Realtime API via WebSocket

```yaml
---
kind: realtime_session
id: p04_rs_support_voicebot
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: websocket
version: "1.0.0"
created: 2026-04-13
updated: 2026-04-13
quality: null
tags: [realtime_session, openai, websocket, vad, support]
tldr: "Customer support voicebot: OpenAI Realtime WebSocket, server_vad, pcm16@24kHz, barge-in."
---
```

### Session Config

```json
{
  "model": "gpt-4o-realtime-preview-2024-12-17",
  "modalities": ["audio", "text"],
  "voice": "alloy",
  "instructions": "You are a customer support agent for Acme Corp. Be concise.",
  "input_audio_format": "pcm16",
  "output_audio_format": "pcm16",
  "input_audio_transcription": {"model": "whisper-1"},
  "turn_detection": {
    "type": "server_vad",
    "threshold": 0.5,
    "prefix_padding_ms": 300,
    "silence_duration_ms": 500
  },
  "tools": [],
  "tool_choice": "auto",
  "temperature": 0.8,
  "max_response_output_tokens": 1024
}
```

### Why it passes

- Provider + model pinned to realtime-capable version ✓
- Transport `websocket` paired with `pcm16` codec ✓
- `server_vad` with explicit threshold, padding, silence_ms ✓
- `quality: null` in frontmatter ✓
- ID matches `^p04_rs_[a-z0-9_]{3,48}\.md$` ✓

---

## Anti-Example 1: Generic model ID (H04 fail)

```yaml
---
kind: realtime_session
id: p04_rs_chat_agent
pillar: P04
provider: openai
model: gpt-4o
transport: websocket
quality: null
---
```

### Why it fails

`model: gpt-4o` is the chat-completion model. It does NOT support the Realtime API.
Must use `gpt-4o-realtime-preview-2024-12-17` or a pinned realtime-capable version.
**Gate**: H04 -- `model` must be a realtime-capable pinned version.

---

## Anti-Example 2: Missing VAD and barge-in (H07 + H08 fail)

```yaml
---
kind: realtime_session
id: p04_rs_demo
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: websocket
quality: null
---
```

```json
{
  "model": "gpt-4o-realtime-preview-2024-12-17",
  "modalities": ["audio"],
  "voice": "alloy"
}
```

### Why it fails

No `turn_detection` field -> H07 FAIL. No interruption policy -> H08 FAIL.
Without VAD, the server never knows when the user stopped speaking.
Without barge-in handling, the model keeps speaking over the user.

---

## Anti-Example 3: Raw API key exposed (H09 fail)

```yaml
---
kind: realtime_session
id: p04_rs_insecure
pillar: P04
provider: openai
model: gpt-4o-realtime-preview-2024-12-17
transport: webrtc
quality: null
---
```

```js
const pc = new RTCPeerConnection();
// WRONG: api_key shipped to browser
const ws = new WebSocket("wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview",
  ["realtime", `openai-insecure-api-key-${process.env.OPENAI_API_KEY}`]);
```

### Why it fails

Raw `OPENAI_API_KEY` is exposed in the browser. **Gate**: H09 -- API key MUST NOT appear
in artifact. Instead: mint ephemeral token server-side via `POST /v1/realtime/sessions`
(60s TTL), pass `client_secret.value` to browser only.

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P07 |
| Domain | realtime_session construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
