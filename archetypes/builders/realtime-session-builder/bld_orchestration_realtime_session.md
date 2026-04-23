---
kind: collaboration
id: bld_collaboration_realtime_session
pillar: P12
llm_function: COLLABORATE
purpose: How realtime_session-builder works in crews with other builders
quality: 9.0
title: "Collaboration: realtime-session-builder"
version: "1.1.0"
author: n01_audit
tags: [realtime_session, builder, collaboration, P12]
tldr: "Crew role: session layer between model_provider (upstream) and voice_pipeline/vad_config (sibling). Produces session JSON for frontend clients."
domain: "realtime_session construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_collaboration_voice_pipeline
  - p03_sp_realtime_session_builder
  - p03_sp_voice_pipeline_builder
  - realtime-session-builder
  - bld_collaboration_stt_provider
  - bld_architecture_realtime_session
  - bld_collaboration_audio_tool
  - bld_architecture_voice_pipeline
  - bld_memory_voice_pipeline
  - bld_collaboration_session_backend
---

## Crew Role

Produces the session-layer configuration that sits between the LLM provider
(OpenAI Realtime API, Gemini Live) and the client audio stack. Handles session
initialization, VAD, barge-in, tool mid-stream, and lifecycle events.
Does NOT process audio signals (audio_tool), manage offline STT/NLU/TTS pipelines
(voice_pipeline), or handle server infrastructure (session_backend).

## Receives From

| Builder | What | Format | When |
|---------|------|--------|------|
| model_provider | Provider endpoint, auth mechanism, model ID | YAML | F1 CONSTRAIN |
| voice_pipeline | Codec requirements (pcm16 vs opus), VAD hints | YAML | F3 INJECT |
| vad_config | VAD threshold tuning, silence_duration_ms | YAML | F3 INJECT |
| system_prompt | Agent instructions for session.instructions field | YAML/MD | F3 INJECT |
| env_config | OPENAI_API_KEY (server-side only; for ephemeral mint) | ENV | F5 CALL |

## Produces For

| Builder | What | Format |
|---------|------|--------|
| session_backend | Session config JSON for WebSocket/WebRTC connection | JSON |
| agent (P02) | Session ID + lifecycle events for agent orchestration | JSON events |
| session_state | Conversation items for state persistence + resume | JSON |
| monitoring (trace_config) | Event log types, PII redaction policy | YAML |

## Boundary

Does NOT produce:
- `voice_pipeline` artifacts (offline STT/NLU/TTS) -- route to voice-pipeline-builder
- `stt_provider` configs (standalone STT) -- route to stt-provider-builder
- `tts_provider` configs (standalone TTS) -- route to tts-provider-builder
- `vad_config` (standalone VAD tuning) -- route to vad-config-builder
- `session_backend` (server infrastructure) -- route to session-backend-builder
- `audio_tool` (signal processing) -- route to audio-tool-builder

## Properties

| Property | Value |
|----------|-------|
| Kind | `collaboration` |
| Pillar | P12 |
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
| [[bld_collaboration_voice_pipeline]] | sibling | 0.41 |
| [[p03_sp_realtime_session_builder]] | upstream | 0.40 |
| [[p03_sp_voice_pipeline_builder]] | upstream | 0.36 |
| [[realtime-session-builder]] | upstream | 0.36 |
| [[bld_collaboration_stt_provider]] | sibling | 0.35 |
| [[bld_architecture_realtime_session]] | upstream | 0.34 |
| [[bld_collaboration_audio_tool]] | sibling | 0.33 |
| [[bld_architecture_voice_pipeline]] | upstream | 0.31 |
| [[bld_memory_voice_pipeline]] | upstream | 0.31 |
| [[bld_collaboration_session_backend]] | sibling | 0.30 |
