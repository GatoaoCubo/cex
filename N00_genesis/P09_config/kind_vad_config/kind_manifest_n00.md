---
id: n00_vad_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "VAD Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, vad_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_vad_config
  - bld_schema_reranker_config
  - vad-config-builder
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_playground_config
  - bld_schema_thinking_config
  - bld_schema_dataset_card
  - bld_schema_bugloop
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A vad_config (Voice Activity Detection config) defines the sensitivity and timing parameters for detecting when a user is speaking versus silent in a realtime voice session. Proper VAD configuration prevents the agent from interrupting the user mid-sentence (too aggressive) or failing to detect speech end (too passive), making voice interactions feel natural and responsive.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `vad_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| mode | enum | yes | server_vad \| semantic_vad \| manual |
| threshold | float | yes | Speech detection threshold (0.0-1.0, higher=less sensitive) |
| silence_duration_ms | integer | yes | Silence duration to trigger end-of-speech |
| prefix_padding_ms | integer | no | Audio to include before detected speech onset |
| noise_reduction | boolean | no | Enable background noise filtering |
| interrupt_enabled | boolean | yes | Allow user to interrupt agent mid-response |
| interrupt_threshold | float | no | Threshold for interruption detection |

## When to use
- Tuning voice session behavior for noisy environments (call center, open office)
- Configuring semantic VAD for languages with longer pause patterns (e.g. PT-BR)
- Setting conservative VAD for medical transcription where false positives are costly

## Builder
`archetypes/builders/vad_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind vad_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: vad_config_support_ptbr
kind: vad_config
pillar: P09
nucleus: n02
title: "PT-BR Support VAD Config"
version: 1.0
quality: null
---
mode: server_vad
threshold: 0.5
silence_duration_ms: 800
prefix_padding_ms: 300
noise_reduction: true
interrupt_enabled: true
interrupt_threshold: 0.7
```

## Related kinds
- `realtime_session` (P09) -- the session config that references this VAD config
- `prosody_config` (P09) -- voice personality settings paired with VAD
- `transport_config` (P09) -- audio transport layer that VAD processes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_vad_config]] | upstream | 0.50 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[vad-config-builder]] | related | 0.38 |
| [[bld_schema_usage_report]] | upstream | 0.38 |
| [[bld_schema_integration_guide]] | upstream | 0.37 |
| [[bld_schema_sandbox_spec]] | upstream | 0.37 |
| [[bld_schema_playground_config]] | upstream | 0.37 |
| [[bld_schema_thinking_config]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.37 |
| [[bld_schema_bugloop]] | downstream | 0.36 |
