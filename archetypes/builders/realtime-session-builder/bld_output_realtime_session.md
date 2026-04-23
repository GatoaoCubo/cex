---
kind: output_template
id: bld_output_template_realtime_session
pillar: P05
llm_function: PRODUCE
purpose: Concrete template for realtime_session (OpenAI Realtime / Gemini Live / Anthropic streaming)
quality: 9.1
title: "Output Template Realtime Session"
version: "1.1.0"
author: n03_rewrite
tags: [realtime_session, builder, output_template, webrtc, openai_realtime, gemini_live]
tldr: "Template producing a concrete LLM realtime session config: transport, VAD, codec, interruption, tools, ephemeral token."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_realtime_session
  - bld_schema_realtime_session
  - p03_sp_realtime_session_builder
  - bld_knowledge_card_realtime_session
  - p10_mem_realtime_session_builder
  - realtime-session-builder
  - bld_examples_realtime_session
  - p04_qg_realtime_session
  - audit_realtime_session_builder
  - atom_29_voice_realtime
---

## Artifact Frontmatter (emit verbatim)

```yaml
---
kind: realtime_session
id: {{id}}                         # e.g. p04_rs_support_voicebot
pillar: P04
provider: {{provider}}             # openai | gemini | anthropic
model: {{model}}                   # gpt-4o-realtime-preview | gemini-2.0-flash-exp
transport: {{transport}}           # webrtc | websocket | grpc_bidi
version: "1.0.0"
created: {{created_at}}
updated: {{updated_at}}
quality: null
tags: [realtime_session, {{provider}}, {{transport}}]
tldr: "{{one_line_purpose}}"
---
```

## Session Config (the core payload)

```json
{
  "model": "{{model}}",
  "modalities": ["audio", "text"],
  "voice": "{{voice}}",
  "instructions": "{{system_prompt_ref}}",
  "input_audio_format": "pcm16",
  "output_audio_format": "pcm16",
  "input_audio_transcription": {"model": "whisper-1"},
  "turn_detection": {
    "type": "server_vad",
    "threshold": 0.5,
    "prefix_padding_ms": 300,
    "silence_duration_ms": 500
  },
  "tools": {{tool_schemas_json}},
  "tool_choice": "auto",
  "temperature": 0.8,
  "max_response_output_tokens": {{max_tokens}}
}
```

## Ephemeral Token Minting (server-side, 60s TTL)

```bash
curl -X POST https://api.openai.com/v1/realtime/sessions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"{{model}}","voice":"{{voice}}"}'
# -> returns client_secret.value (use in browser; expires in 60s)
```

## Latency Budget (MUST populate)

| Stage | Budget | Measured via |
|---|---|---|
| WebRTC ICE/DTLS setup | <= 500 ms | `pc.iceConnectionState` timings |
| First `response.audio.delta` | <= 300 ms after user stops speaking | server_vad `speech_stopped` -> first delta |
| End-to-end perceived latency | <= 800 ms | mic capture ts -> speaker playback ts |

## Interruption (Barge-in) Handler

```js
// On input_audio_buffer.speech_started while response is in-flight:
if (inflightResponseId) {
  dc.send(JSON.stringify({type: "response.cancel"}));
  audioPlayer.flush();   // drop queued output chunks
}
```

## Reconnect / State Persistence

- Store last `conversation.item.id` + unacked user audio in `{{state_store}}`.
- On reconnect: mint new ephemeral token, replay items via `conversation.item.create`, resume with `response.create`.

## Checklist (fill all; no `{{placeholder}}` may remain)

- [ ] `{{provider}}`, {{model}}, {{transport}}, `{{voice}}` resolved
- [ ] `turn_detection` chosen: `server_vad` (default) | `none` (manual `response.create`) | `semantic_vad` (Gemini)
- [ ] Codec pair set: `pcm16@24kHz` (OpenAI WS) or `opus@48kHz` (WebRTC)
- [ ] Tool schemas inlined (JSON Schema draft-07, names unique)
- [ ] Ephemeral token mint endpoint documented (never ship API key to client)
- [ ] Barge-in handler wired to `input_audio_buffer.speech_started`
- [ ] Reconnect strategy (max 3 retries, exponential backoff 500/1500/4500 ms)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_realtime_session]] | upstream | 0.61 |
| [[bld_schema_realtime_session]] | downstream | 0.55 |
| [[p03_sp_realtime_session_builder]] | upstream | 0.53 |
| [[bld_knowledge_card_realtime_session]] | upstream | 0.53 |
| [[p10_mem_realtime_session_builder]] | downstream | 0.46 |
| [[realtime-session-builder]] | upstream | 0.42 |
| [[bld_examples_realtime_session]] | downstream | 0.42 |
| [[p04_qg_realtime_session]] | downstream | 0.41 |
| [[audit_realtime_session_builder]] | downstream | 0.40 |
| [[atom_29_voice_realtime]] | upstream | 0.33 |
