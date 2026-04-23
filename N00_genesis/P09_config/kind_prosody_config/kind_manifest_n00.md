---
id: n00_prosody_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Prosody Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, prosody_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_prosody_config
  - bld_schema_voice_pipeline
  - bld_schema_reranker_config
  - bld_schema_tts_provider
  - bld_schema_vad_config
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A prosody_config defines voice personality and emotion settings for text-to-speech and voice AI integrations: speaking rate, pitch, emotional tone, accent, and pause patterns. It enables CEX voice interfaces to match brand personality and deliver contextually appropriate vocal characteristics for different interaction types (calm support, energetic sales, clinical healthcare).

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `prosody_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| voice_id | string | yes | TTS provider voice identifier |
| language | string | yes | BCP-47 language tag (e.g. pt-BR, en-US) |
| speaking_rate | float | yes | Rate multiplier (0.5=slow, 1.0=normal, 2.0=fast) |
| pitch_semitones | integer | no | Pitch adjustment (-12 to +12 semitones) |
| emotion | enum | no | neutral \| calm \| energetic \| empathetic \| professional |
| pause_ms | integer | no | Pause duration after sentences (ms) |
| ssml_enabled | boolean | no | Whether to parse SSML markup in output |

## When to use
- Configuring voice output for a CEX-powered customer support agent
- Setting up brand-consistent voice personality for a marketing campaign voice bot
- Adapting prosody for different interaction contexts (sales vs. support vs. alerts)

## Builder
`archetypes/builders/prosody_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind prosody_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: prosody_support_ptbr
kind: prosody_config
pillar: P09
nucleus: n02
title: "PT-BR Support Voice Config"
version: 1.0
quality: null
---
voice_id: pt-BR-Wavenet-A
language: pt-BR
speaking_rate: 0.95
emotion: empathetic
pause_ms: 300
ssml_enabled: true
```

## Related kinds
- `vad_config` (P09) -- voice activity detection that pairs with prosody in realtime voice sessions
- `realtime_session` (P09) -- the session config that references prosody settings
- `transport_config` (P09) -- network layer for streaming voice audio

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_prosody_config]] | upstream | 0.42 |
| [[bld_schema_voice_pipeline]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.39 |
| [[bld_schema_tts_provider]] | upstream | 0.38 |
| [[bld_schema_vad_config]] | upstream | 0.38 |
| [[bld_schema_dataset_card]] | upstream | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.37 |
| [[bld_schema_sandbox_spec]] | upstream | 0.37 |
| [[bld_schema_sandbox_config]] | upstream | 0.37 |
