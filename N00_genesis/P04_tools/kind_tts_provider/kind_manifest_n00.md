---
id: n00_tts_provider_manifest
kind: knowledge_card
8f: F3_inject
pillar: P04
nucleus: n00
title: "TTS Provider -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, tts_provider, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_tts_provider
  - bld_schema_voice_pipeline
  - bld_schema_reranker_config
  - bld_schema_stt_provider
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_examples_tts_provider
  - bld_schema_usage_report
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A tts_provider is a text-to-speech provider integration that specifies the configuration, voice selection, audio format, and API contract for a specific TTS backend (ElevenLabs, OpenAI TTS, Azure Speech, Google TTS). It abstracts provider-specific synthesis APIs so the audio_tool can generate speech from text without provider lock-in. The output is a provider configuration artifact consumed by audio_tool to route synthesis requests to the correct backend.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `tts_provider` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| provider_name | string | yes | elevenlabs, openai_tts, azure_speech, google_tts |
| api_endpoint | string | yes | Base API URL for synthesis requests |
| voice_id | string | yes | Default voice identifier for synthesis |
| output_format | string | yes | Audio output format: mp3, wav, ogg |

## When to use
- When configuring which TTS backend the audio_tool or voice_pipeline uses for synthesis
- When building voice response agents that require natural-sounding speech output
- When the voice_pipeline needs a provider swap for cost, quality, or language support reasons

## Builder
`archetypes/builders/tts_provider-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind tts_provider --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: tts_elevenlabs_rachel
kind: tts_provider
pillar: P04
nucleus: n05
title: "ElevenLabs Rachel TTS Provider"
version: 1.0
quality: null
---
provider_name: elevenlabs
api_endpoint: "https://api.elevenlabs.io/v1/text-to-speech"
voice_id: "21m00Tcm4TlvDq8ikWAM"
output_format: mp3
```

## Related kinds
- `audio_tool` (P04) -- tool that uses tts_provider for speech synthesis operations
- `stt_provider` (P04) -- counterpart provider for speech-to-text transcription
- `voice_pipeline` (P04) -- end-to-end voice architecture that references tts_provider
- `multi_modal_config` (P04) -- configuration that routes text-to-speech to the correct tts_provider

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_tts_provider]] | downstream | 0.47 |
| [[bld_schema_voice_pipeline]] | downstream | 0.41 |
| [[bld_schema_reranker_config]] | downstream | 0.39 |
| [[bld_schema_stt_provider]] | downstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.38 |
| [[bld_examples_tts_provider]] | downstream | 0.38 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
