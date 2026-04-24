---
id: n00_stt_provider_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "STT Provider -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, stt_provider, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_stt_provider
  - bld_schema_voice_pipeline
  - bld_schema_tts_provider
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_api_reference
  - bld_schema_multimodal_prompt
  - bld_schema_search_strategy
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An stt_provider is a speech-to-text provider integration that specifies the configuration, authentication, and API contract for a specific STT backend (OpenAI Whisper, AssemblyAI, Azure Speech, Deepgram). It abstracts provider-specific API details so the audio_tool can swap providers without code changes. The output is a provider configuration artifact consumed by audio_tool to route transcription requests to the correct backend.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `stt_provider` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider_name | string | yes | openai_whisper, assemblyai, azure_speech, deepgram |
| api_endpoint | string | yes | Base API URL for transcription requests |
| auth_method | string | yes | api_key, oauth2, or azure_key |
| word_error_rate | float | no | Expected WER for benchmark reference |

## When to use
- When configuring which STT backend the audio_tool or voice_pipeline uses
- When swapping transcription providers for cost or quality reasons
- When building a multi-provider fallback chain for speech transcription in the voice_pipeline

## Builder
`archetypes/builders/stt_provider-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind stt_provider --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: stt_openai_whisper_v3
kind: stt_provider
pillar: P04
nucleus: n05
title: "OpenAI Whisper v3 STT Provider"
version: 1.0
quality: null
---
provider_name: openai_whisper
api_endpoint: "https://api.openai.com/v1/audio/transcriptions"
auth_method: api_key
word_error_rate: 0.05
```

## Related kinds
- `audio_tool` (P04) -- tool that uses stt_provider for transcription operations
- `tts_provider` (P04) -- counterpart provider for text-to-speech synthesis
- `voice_pipeline` (P04) -- end-to-end voice architecture that references stt_provider
- `multi_modal_config` (P04) -- configuration that routes audio inputs to the correct stt_provider

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_stt_provider]] | downstream | 0.45 |
| [[bld_schema_voice_pipeline]] | downstream | 0.41 |
| [[bld_schema_tts_provider]] | downstream | 0.40 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_integration_guide]] | downstream | 0.39 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_api_reference]] | downstream | 0.38 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.38 |
| [[bld_schema_search_strategy]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.38 |
