---
id: n00_realtime_session_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Realtime Session -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, realtime_session, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_vad_config
  - bld_schema_tts_provider
  - bld_schema_voice_pipeline
  - bld_schema_integration_guide
  - bld_schema_thinking_config
  - bld_schema_sandbox_spec
  - bld_schema_realtime_session
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A realtime_session defines the configuration for a live, bidirectional session between a user and a CEX agent: WebSocket or WebRTC transport, audio/text modalities, turn-taking protocol, interruption handling, and session lifecycle management. It enables voice-first and low-latency interactive experiences built on the OpenAI Realtime API or equivalent.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `realtime_session` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable session config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| modalities | list | yes | Input/output modalities: text, audio |
| transport | enum | yes | websocket \| webrtc \| sse |
| turn_detection | enum | yes | server_vad \| client_vad \| push_to_talk |
| interruption_handling | enum | yes | allow \| buffer \| block |
| max_session_duration_s | integer | yes | Session timeout in seconds |
| audio_format | enum | no | pcm16 \| g711_ulaw \| opus |
| sample_rate_hz | integer | no | Audio sample rate (default 24000) |
| prosody_config_ref | string | no | Reference to prosody_config for voice settings |

## When to use
- Building a real-time voice assistant powered by a CEX nucleus
- Configuring low-latency text streaming sessions for interactive use
- Setting up WebRTC-based browser voice interfaces for CEX demonstrations

## Builder
`archetypes/builders/realtime_session-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind realtime_session --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: realtime_voice_support
kind: realtime_session
pillar: P09
nucleus: n02
title: "Voice Support Realtime Session"
version: 1.0
quality: null
---
modalities: [audio, text]
transport: websocket
turn_detection: server_vad
interruption_handling: allow
max_session_duration_s: 1800
audio_format: pcm16
sample_rate_hz: 24000
prosody_config_ref: prosody_support_ptbr
```

## Related kinds
- `prosody_config` (P09) -- voice personality settings for this session
- `vad_config` (P09) -- voice activity detection config for turn_detection
- `transport_config` (P09) -- network transport layer underpinning the session

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_multimodal_prompt]] | upstream | 0.42 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[bld_schema_vad_config]] | upstream | 0.41 |
| [[bld_schema_tts_provider]] | upstream | 0.40 |
| [[bld_schema_voice_pipeline]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_thinking_config]] | upstream | 0.39 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
| [[bld_schema_realtime_session]] | upstream | 0.39 |
