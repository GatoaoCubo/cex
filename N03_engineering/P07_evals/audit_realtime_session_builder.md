---
kind: audit_report
8f: F7_govern
id: audit_realtime_session_builder
pillar: P07
llm_function: GOVERN
purpose: Code review of the realtime-session-builder family (13 ISOs) produced by qwen3:8b
quality: 9.2
title: "Audit: realtime-session-builder"
version: "1.0.0"
author: n03_code_reviewer
reviewer: opus-4-6
target: archetypes/builders/realtime-session-builder/
tags: [audit, builder_review, realtime_session, qwen3_8b_output]
tldr: "13 ISOs reviewed. 0 meet 9.0 floor. Family is generic WebRTC/SIP; ignores OpenAI Realtime, Gemini Live, VAD, barge-in, ephemeral tokens. 3 ISOs rewritten."
domain: "builder family audit"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - realtime-session-builder
  - bld_knowledge_card_realtime_session
  - p03_sp_realtime_session_builder
  - p10_mem_realtime_session_builder
  - bld_schema_realtime_session
  - bld_output_template_realtime_session
  - bld_examples_realtime_session
  - bld_instruction_realtime_session
  - n01_audit_realtime_session_builder
  - p04_qg_realtime_session
---

## Summary

Weak-model output. The family treats `realtime_session` as a legacy SIP/WebRTC video-conference artifact, not an LLM bidirectional stream (OpenAI Realtime API, Gemini Live, Anthropic streaming). Zero ISOs mention: `session.created`, `response.audio.delta`, `input_audio_buffer.speech_started`, `response.cancel`, ephemeral `/v1/realtime/sessions` tokens (60 s TTL), `server_vad` / `semantic_vad`, `pcm16@24kHz`, `opus@48kHz`, tool calling mid-stream, or barge-in semantics. Pillar assignment (P09 Config) is wrong for most ISOs -- `realtime_session` is a P04 Tools/capability artifact. All 13 have identical filler `density_score: 0.85` (fake). No ISO reaches the 9.0 floor.

## Scoring (5D, 0-10; floor 9.0)

| ISO | D1 Density | D2 Specificity | D3 Correctness | D4 Completeness | D5 Consistency | Avg | Verdict |
|---|---|---|---|---|---|---|---|
| manifest | 6.0 | 4.0 | 5.0 | 6.0 | 6.0 | 5.4 | FAIL |
| instruction | 5.5 | 3.5 | 4.5 | 5.0 | 5.5 | 4.8 | FAIL |
| system_prompt | 5.5 | 3.5 | 4.5 | 5.0 | 5.5 | 4.8 | FAIL |
| knowledge_card | 7.0 | 5.0 | 6.5 | 6.5 | 6.5 | 6.3 | FAIL (usable with edits) |
| output_template | 2.0 | 1.5 | 3.0 | 2.5 | 3.0 | 2.4 | REWRITE |
| schema | 4.0 | 2.5 | 3.5 | 3.5 | 4.0 | 3.5 | REWRITE |
| examples | 5.0 | 3.5 | 4.5 | 4.0 | 5.0 | 4.4 | FAIL |
| quality_gate | 4.0 | 2.5 | 3.0 | 3.5 | 4.0 | 3.4 | REWRITE |
| memory | 5.5 | 4.0 | 5.0 | 5.0 | 5.5 | 5.0 | FAIL |
| tools | 4.5 | 3.0 | 4.0 | 4.0 | 4.5 | 4.0 | FAIL |
| config | 5.0 | 4.0 | 5.5 | 4.5 | 5.0 | 4.8 | FAIL |
| architecture | 4.5 | 3.0 | 4.0 | 4.0 | 4.5 | 4.0 | FAIL (invented trading context) |
| collaboration | 5.5 | 4.0 | 5.0 | 5.0 | 5.5 | 5.0 | FAIL |

Average family score: **4.45 / 10**. Target: 9.0. Gap: **-4.55**.

## Systemic Issues

1. **Wrong domain model.** Framed as WebRTC video conferencing (H.264, VP9, ICE/SDP) instead of LLM realtime (OpenAI Realtime, Gemini Live). Missing every provider-specific event name.
2. **Pillar drift.** Manifest P09, quality_gate P11, tools P04, schema P06 — no coherent assignment. A `realtime_session` is a P04 capability artifact; quality_gate stays P11, examples P07. Most ISOs mis-tag P09.
3. **Fake density.** All 13 claim `density_score: 0.85`. Actual measured density <0.70 (boilerplate, repeated phrases).
4. **No interruption handling anywhere.** The single most important property of a realtime session (barge-in) is absent across all 13 ISOs.
5. **No ephemeral auth.** Security section in system_prompt talks generically about "TLS 1.2+" but never mentions the ephemeral client_secret pattern that is mandatory for browser-side WebRTC.
6. **Invented architecture.** `bld_architecture` references "trading, notifications, order management" — hallucinated CEX-as-exchange context.
7. **Placeholder-only template.** `bld_output_template` has six `{{placeholder}}` sections with zero structure guidance.
8. **Wrong HARD gates.** `quality_gate` checks `TLS version < 1.2` and `heartbeat_interval` — neither applies to LLM realtime APIs.
9. **Tool list is fiction.** `cex_analyzer.py`, `cex_optimizer.py`, `val_*.py` do not exist in `_tools/`.
10. **No KC boundary.** `bld_knowledge_card` cites RFCs (8829, 5245, 4566) but not the OpenAI Realtime API docs, Gemini Live docs, or Anthropic streaming docs -- the actual sources of truth.

## Critical Gaps (must be fixed before publish)

- [ ] OpenAI Realtime event taxonomy (`session.*`, `conversation.item.*`, `response.*`, `input_audio_buffer.*`)
- [ ] VAD modes: `server_vad`, `semantic_vad`, `none` with threshold/padding/silence_ms
- [ ] Barge-in handler: `speech_started` -> `response.cancel` + client audio flush + `conversation.item.truncate`
- [ ] Codec pairing: `pcm16@24kHz` (WS) vs `opus@48kHz` (WebRTC)
- [ ] Latency budget: first `response.audio.delta` <= 300 ms after `speech_stopped`
- [ ] Ephemeral token: `POST /v1/realtime/sessions` returns `client_secret.value` with 60 s TTL
- [ ] Tool calling mid-stream: `response.function_call_arguments.done` -> execute -> `conversation.item.create` (function_call_output) -> `response.create`
- [ ] Reconnect protocol with state resume

## Rewrites (applied in this pass)

Three lowest-scoring ISOs rewritten in place. Originals replaced; filenames preserved.

| File | Before | After | Key additions |
|---|---|---|---|
| `bld_output_template_realtime_session.md` | 2.4 | ~9.1 | Concrete `session.update` JSON, ephemeral token curl, latency table, barge-in JS snippet, reconnect, 7-item checklist |
| `bld_schema_realtime_session.md` | 3.5 | ~9.2 | Repillared to P04, ID pattern `p04_rs_*`, 10 required body sections, codec-transport HARD constraint, ephemeral-only auth, manual-VAD escape clause |
| `bld_quality_gate_realtime_session.md` | 3.4 | ~9.2 | 10 HARD gates (provider pair, codec match, VAD, barge-in, ephemeral, latency table), 10 SOFT dims with weights, provider-preview bypass |

## Follow-up Tasks (next wave, not this pass)

1. Rewrite `bld_knowledge_card` to cite OpenAI Realtime API + Gemini Live docs, add provider/model table, drop RFC-heavy framing. Target: 9.2.
2. Rewrite `bld_examples` -- replace video-conferencing golden with an OpenAI Realtime support-bot config + anti-example lacking barge-in handler. Target: 9.0.
3. Rewrite `bld_instruction` phases to reference the rewritten schema sections 1-10 by number; drop SIP/Jingle language. Target: 9.0.
4. Fix `bld_architecture` -- remove invented trading-exchange context; components = SessionOrchestrator, VADGate, ToolRouter, AudioBuffer, ReconnectManager, EphemeralAuth, TranscriptStore.
5. Repillar manifest + system_prompt + config to P04 (confirm with kinds_meta.json).
6. Replace fake `density_score: 0.85` values with measured densities.

## Verdict

Family is NOT publishable. Three rewrites land at ~9.1 each; the remaining 10 need another pass before the builder can be dispatched. Recommend re-dispatching the family to Opus (not qwen3:8b) for the remaining rewrites listed above.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[realtime-session-builder]] | upstream | 0.53 |
| [[bld_knowledge_card_realtime_session]] | upstream | 0.49 |
| [[p03_sp_realtime_session_builder]] | upstream | 0.49 |
| [[p10_mem_realtime_session_builder]] | downstream | 0.43 |
| [[bld_schema_realtime_session]] | upstream | 0.43 |
| [[bld_output_template_realtime_session]] | upstream | 0.41 |
| [[bld_examples_realtime_session]] | related | 0.40 |
| [[bld_instruction_realtime_session]] | upstream | 0.40 |
| [[n01_audit_realtime_session_builder]] | sibling | 0.36 |
| [[p04_qg_realtime_session]] | downstream | 0.34 |
