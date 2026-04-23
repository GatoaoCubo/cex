---
id: n00_multi_modal_config_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Multi Modal Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, multi_modal_config, p04, n00, archetype, template]
density_score: 1.0
related:
  - p01_kc_multi_modal_config
  - bld_schema_multi_modal_config
  - bld_knowledge_card_multi_modal_config
  - multi-modal-config-builder
  - bld_architecture_multi_modal_config
  - bld_output_template_multi_modal_config
  - bld_schema_multimodal_prompt
  - bld_collaboration_multi_modal_config
  - bld_schema_voice_pipeline
  - bld_schema_reranker_config
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A multi_modal_config specifies input format requirements, resolution constraints, encoding standards, and routing rules for multi-modal LLM inputs. It defines how images, audio, and documents should be preprocessed before being sent to the model, and which provider endpoint handles each modality. The output is a configuration layer that standardizes multi-modal preprocessing across all agents and ensures models receive properly formatted inputs.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `multi_modal_config` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| supported_modalities | list | yes | Active modalities: image, audio, video, document |
| image_config | map | no | max_resolution, encoding (base64/url), format |
| audio_config | map | no | sample_rate, format, max_duration_seconds |
| routing_rules | map | no | Modality -> provider endpoint mapping |

## When to use
- When configuring a multi-modal LLM pipeline that processes images, audio, or video
- When standardizing how different modalities are encoded before injection into the model context
- When the multimodal_prompt artifact needs a companion configuration for its input processing

## Builder
`archetypes/builders/multi_modal_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind multi_modal_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mmc_claude_vision_standard
kind: multi_modal_config
pillar: P04
nucleus: n03
title: "Claude Vision Standard Config"
version: 1.0
quality: null
---
supported_modalities: [image, document]
image_config:
  max_resolution: "1568x1568"
  encoding: base64
  format: [jpeg, png, webp, gif]
routing_rules:
  image: anthropic_claude_sonnet
  document: anthropic_claude_sonnet
```

## Related kinds
- `multimodal_prompt` (P03) -- prompt template that multi_modal_config preprocesses inputs for
- `vision_tool` (P04) -- image analysis tool that uses multi_modal_config encoding rules
- `audio_tool` (P04) -- audio tool that uses multi_modal_config audio encoding settings
- `context_window_config` (P03) -- token budget allocation that multi_modal_config must respect

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_multi_modal_config]] | sibling | 0.43 |
| [[bld_schema_multi_modal_config]] | downstream | 0.42 |
| [[bld_knowledge_card_multi_modal_config]] | sibling | 0.40 |
| [[multi-modal-config-builder]] | related | 0.39 |
| [[bld_architecture_multi_modal_config]] | downstream | 0.37 |
| [[bld_output_template_multi_modal_config]] | downstream | 0.36 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.36 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.35 |
| [[bld_schema_voice_pipeline]] | downstream | 0.35 |
| [[bld_schema_reranker_config]] | downstream | 0.34 |
