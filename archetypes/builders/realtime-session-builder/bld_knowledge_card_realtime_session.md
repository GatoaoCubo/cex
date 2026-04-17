---
kind: knowledge_card
id: bld_knowledge_card_realtime_session
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for realtime_session production
quality: 9.2
title: "Knowledge Card: Realtime Session (LLM Streaming)"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, knowledge_card, openai_realtime, gemini_live, webrtc, vad]
tldr: "LLM realtime session domain: providers, transport, VAD, barge-in, ephemeral auth, latency budgets, lifecycle events."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

## Domain Overview

`realtime_session` artifacts configure LLM bidirectional audio+text streaming sessions.
Unlike traditional WebRTC video conferencing, the primary use case is voice-interactive
AI agents: the user speaks, an LLM responds in real-time audio, and the session manages
turn-taking, interruption, and tool calls mid-stream.

Key providers: OpenAI Realtime API (WebSocket + WebRTC, `gpt-4o-realtime-preview-*`),
Gemini Live (`gemini-2.0-flash-exp`, WebSocket/gRPC), Anthropic streaming (SSE/WebSocket).
Integration platforms: LiveKit Agents, Daily Bots, Vapi, Retell AI, Twilio Voice Media Streams.

## Provider / Model Pairs

| Provider | Realtime Model | Transport | Audio Format | Notes |
|----------|---------------|-----------|--------------|-------|
| OpenAI | gpt-4o-realtime-preview-2024-12-17 | websocket, webrtc | pcm16@24kHz (WS), opus@48kHz (WebRTC) | Ephemeral token: POST /v1/realtime/sessions |
| OpenAI | gpt-4o-mini-realtime-preview-2024-12-17 | websocket | pcm16@24kHz | Lower latency, smaller model |
| Google | gemini-2.0-flash-exp | websocket, grpc_bidi | pcm16@16kHz | semantic_vad; no server_vad |
| Custom | any | websocket, grpc_bidi | pcm16 or opus | Use provider: custom + document endpoint |

## Key Concepts

| Concept | Definition | Source |
|---------|------------|--------|
| server_vad | Server-side voice activity detection: threshold, prefix_padding_ms, silence_duration_ms | OpenAI Realtime API docs |
| semantic_vad | Content-aware turn detection (Gemini Live); uses LLM understanding of speech end | Google Gemini Live docs |
| Barge-in / Interruption | Client speaks while model is responding; triggers response.cancel + audio flush | OpenAI Realtime events spec |
| Ephemeral token | 60s client_secret minted server-side via POST /v1/realtime/sessions; never ship API key to browser | OpenAI security model |
| conversation.item | Persistent message in session context; user/assistant/function_call/function_call_output | OpenAI Realtime API |
| response.audio.delta | Streaming audio chunk event; latency measured from speech_stopped to first delta | OpenAI Realtime events |
| ICE/DTLS setup | WebRTC peer connection establishment; adds 200-500ms before first audio | RFC 8829, RFC 5764 |
| DTLS-SRTP | Encrypted media transport for WebRTC audio streams | RFC 5764 |
| Codec-transport lock | WebRTC requires opus@48kHz; WebSocket requires pcm16@24kHz or g711_ulaw | OpenAI API constraints |
| Tool mid-stream | LLM calls a function during live response; handled via response.function_call_arguments.done event | OpenAI Realtime tool use |

## Lifecycle Events (MUST handle all 7)

| Event | When | Handler |
|-------|------|---------|
| session.created | After WebSocket connect + auth | Store session.id, initialize state |
| session.updated | After session.update sent | Confirm config applied |
| conversation.item.created | After user/assistant turn | Update conversation history |
| response.created | Model starts responding | Set inflightResponseId |
| response.audio.delta | Audio chunk streaming | Decode + play immediately |
| response.done | Full response complete | Clear inflightResponseId |
| error | Protocol/auth/rate-limit error | Log, reconnect if retriable |

## Latency Budgets

| Stage | Target | Measurement | Provider |
|-------|--------|-------------|----------|
| WebRTC ICE/DTLS setup | <= 500 ms | pc.iceConnectionState timings | OpenAI WebRTC |
| First response.audio.delta | <= 300 ms after speech_stopped | server_vad speech_stopped -> first delta | OpenAI WebSocket |
| End-to-end perceived | <= 800 ms | mic capture ts -> speaker playback ts | All |
| Gemini first chunk | <= 500 ms | grpc_bidi first audio frame | Gemini Live |

## Industry Standards

- WebRTC (IETF RFC 8829) -- peer connection, SDP, ICE
- DTLS-SRTP (RFC 5764) -- encrypted media over WebRTC
- RTP/RTCP (RFC 3550) -- realtime transport + feedback
- ICE (RFC 5245) -- NAT traversal
- SDP (RFC 4566) -- session description
- SIP (RFC 3261) -- session initiation (telephony, Twilio)

## Common Patterns

1. **WebSocket + server_vad**: Default for OpenAI; pcm16@24kHz; simplest setup
2. **WebRTC + opus**: For browser integration; lower bandwidth; adds ICE latency
3. **gRPC bidi**: For Gemini Live server-to-server; highest throughput
4. **Ephemeral token pattern**: Server mints 60s token, browser uses it for connection
5. **State resume**: On disconnect, replay conversation.item list + re-send response.create
6. **Tool mid-stream**: On function_call_arguments.done, execute, return function_call_output item, resume

## Pitfalls

- Using generic `gpt-4o` model (not realtime-capable) -- silent streaming failure
- Shipping raw API key to browser -- security incident; use ephemeral tokens
- Omitting barge-in handler -- model speaks over user indefinitely
- Wrong codec for transport -- pcm16 on WebRTC causes decode silence
- `turn_detection: none` without manual response.create trigger -- model never responds
- Not handling `error` event -- reconnect loop never triggered
