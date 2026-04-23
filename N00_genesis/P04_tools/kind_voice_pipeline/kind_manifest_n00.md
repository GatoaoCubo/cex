---
id: n00_voice_pipeline_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Voice Pipeline -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, voice_pipeline, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_voice_pipeline
  - bld_schema_tts_provider
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_action_paradigm
  - bld_schema_search_strategy
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_multimodal_prompt
  - bld_schema_stt_provider
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A voice_pipeline is an end-to-end voice agent architecture definition that specifies the complete STT -> LLM -> TTS loop with latency targets, interruption handling, and turn-taking protocol. It orchestrates stt_provider, the core LLM nucleus, and tts_provider into a coherent real-time voice interaction system. The output is a deployable voice agent specification that enables natural spoken conversations with AI agents.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `voice_pipeline` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| stt_provider_id | string | yes | Reference to stt_provider artifact for transcription |
| tts_provider_id | string | yes | Reference to tts_provider artifact for synthesis |
| nucleus_id | string | yes | LLM nucleus handling the conversation (n01-n07) |
| target_latency_ms | integer | yes | End-to-end response latency target |

## When to use
- When building a real-time voice assistant using any CEX nucleus as the LLM brain
- When deploying an AI customer service agent that requires voice input/output
- When the product requires a spoken interface backed by CEX's knowledge system

## Builder
`archetypes/builders/voice_pipeline-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind voice_pipeline --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: vp_cex_voice_assistant
kind: voice_pipeline
pillar: P04
nucleus: n04
title: "CEX Voice Knowledge Assistant"
version: 1.0
quality: null
---
stt_provider_id: stt_openai_whisper_v3
tts_provider_id: tts_elevenlabs_rachel
nucleus_id: n04
target_latency_ms: 800
```

## Related kinds
- `stt_provider` (P04) -- STT backend configured in this pipeline
- `tts_provider` (P04) -- TTS backend configured in this pipeline
- `audio_tool` (P04) -- audio processing tool used within the pipeline
- `multi_modal_config` (P04) -- configuration governing audio encoding in the pipeline

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_voice_pipeline]] | downstream | 0.49 |
| [[bld_schema_tts_provider]] | downstream | 0.44 |
| [[bld_schema_reranker_config]] | downstream | 0.42 |
| [[bld_schema_usage_report]] | downstream | 0.41 |
| [[bld_schema_action_paradigm]] | downstream | 0.41 |
| [[bld_schema_search_strategy]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
| [[bld_schema_stt_provider]] | downstream | 0.40 |
