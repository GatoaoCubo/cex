---
kind: schema
id: bld_schema_realtime_session
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema for realtime_session (LLM bidirectional streaming) -- SINGLE SOURCE OF TRUTH
quality: 9.2
title: "Schema Realtime Session"
version: "1.1.0"
author: n03_rewrite
tags: [realtime_session, builder, schema, openai_realtime, webrtc, vad]
tldr: "Schema for LLM realtime sessions: provider, transport, VAD, codec, interruption policy, tool mid-stream, ephemeral auth."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_instruction_realtime_session
  - p03_sp_realtime_session_builder
  - bld_output_template_realtime_session
  - bld_knowledge_card_realtime_session
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_quickstart_guide
  - p04_qg_realtime_session
  - bld_schema_api_reference
  - bld_schema_integration_guide
---

## ID Pattern

`^p04_rs_[a-z0-9_]{3,48}\.md$`   (e.g. `p04_rs_support_voicebot.md`)

## Frontmatter (REQUIRED)

| Field | Type | Required | Allowed / Example | Notes |
|---|---|---|---|---|
| id | string | yes | `p04_rs_*` | Matches ID pattern |
| kind | const | yes | `realtime_session` | |
| pillar | const | yes | `P04` | Tools / capabilities pillar |
| provider | enum | yes | `openai` \| `gemini` \| `anthropic` \| `custom` | |
| model | string | yes | `gpt-4o-realtime-preview-2024-12-17` | Provider-pinned version |
| transport | enum | yes | `webrtc` \| `websocket` \| `grpc_bidi` | |
| version | semver | yes | `1.0.0` | |
| created | ISO8601 | yes | `2026-04-13` | |
| updated | ISO8601 | yes | `2026-04-13` | |
| quality | null | yes | `null` | Peer review assigns |
| tags | array | yes | `[realtime_session, openai, webrtc]` | lowercase |
| tldr | string | yes | <=140 chars | |

## Body Structure (REQUIRED sections, in order)

1. **Session Goal** — one paragraph, what the agent does on this stream.
2. **Transport & Codec**
   - `transport`: webrtc | websocket | grpc_bidi
   - `input_audio_format`: `pcm16` (24 kHz LE mono) | `opus` (48 kHz WebRTC)
   - `output_audio_format`: same set
3. **Turn Detection (VAD)** — pick ONE:
   - `server_vad` (default; threshold 0.0-1.0, prefix_padding_ms, silence_duration_ms)
   - `semantic_vad` (Gemini Live; uses content signals)
   - `none` (manual: client issues `response.create`)
4. **Interruption Policy (barge-in)**
   - Trigger event: `input_audio_buffer.speech_started`
   - Action: emit `response.cancel` + flush client audio queue
   - Truncate server transcript via `conversation.item.truncate`
5. **Tool Calling Mid-Stream**
   - Tool schemas (JSON Schema draft-07), `tool_choice` in {auto, none, required, {type:function,name:X}}
   - Handling: on `response.function_call_arguments.done` -> execute -> `conversation.item.create` with function_call_output -> `response.create`
6. **Session Lifecycle Events** — must handle: `session.created`, `session.updated`, `conversation.item.created`, `response.created`, `response.audio.delta`, `response.done`, `error`.
7. **Authentication** — ephemeral client_secret from `POST /v1/realtime/sessions` (60 s TTL). API key NEVER on client.
8. **Reconnect & State** — resume token or `conversation.item.create` replay; max retries + backoff table.
9. **Latency Budget** — table with target ms for ICE/DTLS, first audio chunk, end-to-end.
10. **Observability** — logged event types, PII redaction policy, sample rate.

## Constraints (HARD)

- `provider` + `model` must be a known pair (see kc_realtime_session.md table).
- If `transport: webrtc` then `input_audio_format in {opus, pcm16}`; if `websocket` then `pcm16` or `g711_ulaw`.
- `turn_detection.type: none` REQUIRES a documented manual `response.create` trigger (client event or wake-word).
- An interruption policy section is MANDATORY even if `turn_detection: none`.
- `max_response_output_tokens` in `[1, 4096]` or `"inf"`.
- Tool names: `^[a-zA-Z_][a-zA-Z0-9_]{0,63}$`; unique per session.
- Ephemeral token mint endpoint documented; raw API key MUST NOT appear in artifact.

## Constraints (SOFT)

- Latency budget table SHOULD target first audio delta <= 300 ms from speech_stopped.
- SHOULD declare reconnect strategy (retries, backoff) even if trivial.
- SHOULD include a PII redaction note if transcripts are persisted.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_realtime_session]] | upstream | 0.52 |
| [[p03_sp_realtime_session_builder]] | upstream | 0.50 |
| [[bld_output_template_realtime_session]] | upstream | 0.49 |
| [[bld_knowledge_card_realtime_session]] | upstream | 0.47 |
| [[bld_schema_reranker_config]] | sibling | 0.41 |
| [[bld_schema_usage_report]] | sibling | 0.39 |
| [[bld_schema_quickstart_guide]] | sibling | 0.38 |
| [[p04_qg_realtime_session]] | downstream | 0.38 |
| [[bld_schema_api_reference]] | sibling | 0.38 |
| [[bld_schema_integration_guide]] | sibling | 0.38 |
