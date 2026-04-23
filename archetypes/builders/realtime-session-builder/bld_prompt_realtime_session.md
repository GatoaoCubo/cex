---
kind: instruction
id: bld_instruction_realtime_session
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for realtime_session
quality: 9.1
title: "Instruction: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, instruction, vad, barge_in, ephemeral_token]
tldr: "Production process: pick provider+model pair, match codec to transport, configure VAD, wire barge-in, mint ephemeral token."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_output_template_realtime_session
  - bld_schema_realtime_session
  - p03_sp_realtime_session_builder
  - bld_knowledge_card_realtime_session
  - p04_qg_realtime_session
  - p10_mem_realtime_session_builder
  - realtime-session-builder
  - bld_examples_realtime_session
  - audit_realtime_session_builder
  - atom_29_voice_realtime
---

## Phase 1: RESEARCH

1. Identify provider + model pair: must be realtime-capable
   (e.g., `openai` + `gpt-4o-realtime-preview-2024-12-17`; `gemini` + `gemini-2.0-flash-exp`)
   -- consult bld_knowledge_card_realtime_session.md provider table
2. Choose transport: `webrtc` (browser, opus), `websocket` (server or browser, pcm16),
   `grpc_bidi` (server-to-server, Gemini)
3. Verify codec-transport pairing: webrtc -> opus@48kHz; websocket -> pcm16@24kHz or g711_ulaw
4. Confirm VAD strategy for use case: `server_vad` (default), `semantic_vad` (Gemini only),
   `none` (requires manual `response.create` trigger)
5. Define latency budget: first audio delta target (recommend <= 300 ms after speech_stopped)
6. Identify tools the model may call mid-stream (JSON Schema definitions required)

## Phase 2: COMPOSE

1. Read `bld_schema_realtime_session.md` -- assign `id` matching `^p04_rs_[a-z0-9_]{3,48}\.md$`
2. Read `bld_output_template_realtime_session.md` -- follow exact frontmatter + JSON structure
3. Write session config JSON: `model`, `modalities`, `voice`, `input_audio_format`,
   `output_audio_format`, `turn_detection`, `tools`, `tool_choice`, `max_response_output_tokens`
4. Configure `turn_detection`:
   - `server_vad`: set `threshold` (0.5 default), `prefix_padding_ms` (300), `silence_duration_ms` (500)
   - `none`: document the manual `response.create` trigger event or wake-word
5. Write ephemeral token mint flow: `POST /v1/realtime/sessions` + 60s TTL note + NEVER ship raw key
6. Write interruption handler: `input_audio_buffer.speech_started` -> `response.cancel`
   + `audioPlayer.flush()` + `conversation.item.truncate`
7. Build latency budget table: ICE/DTLS setup, first audio delta, end-to-end perceived
8. Document all 7 lifecycle events and their handlers
9. Write reconnect strategy: max retries, backoff table, state resume via conversation.item.create

## Phase 3: VALIDATE

- [ ] `id` matches schema pattern: `^p04_rs_[a-z0-9_]{3,48}\.md$` (H02)
- [ ] `provider` + `model` are realtime-capable pair -- not generic chat model (H04)
- [ ] `transport` in {webrtc, websocket, grpc_bidi} (H05)
- [ ] Codec matches transport: opus for webrtc, pcm16/g711_ulaw for websocket (H06)
- [ ] `turn_detection.type` specified; if server_vad then threshold+padding+silence_ms set (H07)
- [ ] Barge-in handler present: speech_started -> response.cancel + flush (H08)
- [ ] No raw API key in body; ephemeral token mint endpoint documented (H09)
- [ ] Latency budget table present with first-audio-delta target (H10)
- [ ] `quality: null` in frontmatter (H05-variant)
- [ ] All 7 lifecycle events handled

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | realtime_session construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_realtime_session]] | downstream | 0.57 |
| [[bld_schema_realtime_session]] | downstream | 0.57 |
| [[p03_sp_realtime_session_builder]] | related | 0.55 |
| [[bld_knowledge_card_realtime_session]] | upstream | 0.52 |
| [[p04_qg_realtime_session]] | downstream | 0.48 |
| [[p10_mem_realtime_session_builder]] | downstream | 0.46 |
| [[realtime-session-builder]] | downstream | 0.43 |
| [[bld_examples_realtime_session]] | downstream | 0.42 |
| [[audit_realtime_session_builder]] | downstream | 0.39 |
| [[atom_29_voice_realtime]] | upstream | 0.30 |
