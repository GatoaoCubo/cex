---
kind: output_template
id: bld_output_template_multi_modal_config
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} for multi_modal_config production
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Multi Modal Config"
version: "1.0.0"
author: n03_builder
tags: [multi_modal_config, builder, examples]
tldr: "Golden and anti-examples for multi modal config construction, demonstrating ideal structure and common pitfalls."
domain: "multi modal config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_multi_modal_config
  - bld_knowledge_card_multi_modal_config
  - bld_schema_multi_modal_config
  - bld_instruction_multi_modal_config
  - p03_sp_multi_modal_config_builder
  - multi-modal-config-builder
  - p10_lr_multi_modal_config_builder
  - bld_config_multi_modal_config
  - bld_collaboration_multi_modal_config
  - bld_architecture_multi_modal_config
---

# Output Template: multi_modal_config
```yaml
---
id: p04_mmc_{{capability_slug}}
kind: multi_modal_config
pillar: P04
title: "{{Capability Name}} Multi-Modal Config"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{builder_name}}"
supported_modalities: [{{image}}, {{audio}}, {{text}}]
image_max_resolution: "{{WxH}}"
image_format: [png, jpg, webp]
audio_format: [mp3, wav]
audio_max_duration_s: {{seconds}}
video_max_duration_s: {{seconds}}
preprocessing: [{{resize}}, {{compress}}]
routing_model:
  image: {{vision_model}}
  audio: {{audio_model}}
  text: {{text_model}}
token_cost_estimate:
  image: {{tokens_per_image}}
  audio: {{tokens_per_minute}}
domain: {{domain_name}}
quality: null
tags: [multi_modal_config, {{tag1}}, {{tag2}}]
tldr: "{{Dense <=160ch config summary}}"
---

# {{Capability Name}} Multi-Modal Config

## Supported Modalities
| Modality | Formats | Max Size/Duration | Tokens/Unit |
|----------|---------|-------------------|-------------|
| Image | {{formats}} | {{resolution}} | {{cost}} |
| Audio | {{formats}} | {{duration}}s | {{cost}} |
| Video | {{formats}} | {{duration}}s | {{cost}} |

## Preprocessing Pipeline
| Step | Modality | Action | Purpose |
|------|----------|--------|---------|
| 1 | Image | {{resize to WxH}} | Reduce token cost |
| 2 | Audio | {{transcribe via Whisper}} | Convert to text |
| 3 | Video | {{extract keyframes}} | Reduce to images |

## Routing Map
| Modality | Model | Reason |
|----------|-------|--------|
| Image | {{model}} | {{native vision support}} |
| Audio | {{model}} | {{transcription capability}} |
| Text | {{model}} | {{default text processing}} |

## Token Cost Estimates
| Modality | Cost | Notes |
|----------|------|-------|
| Image (1024px) | ~750 tokens | {{scaling notes}} |
| Image (2048px) | ~1500 tokens | {{scaling notes}} |
| Audio (1min) | ~300 tokens (transcribed) | {{after Whisper}} |

## Fallback Chain
1. IF model lacks native {{modality}} → {{fallback action}}
2. IF format unsupported → {{conversion step}}
3. IF over budget → {{preprocessing reduction}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_multi_modal_config]] | upstream | 0.65 |
| [[bld_knowledge_card_multi_modal_config]] | upstream | 0.58 |
| [[bld_schema_multi_modal_config]] | downstream | 0.50 |
| [[bld_instruction_multi_modal_config]] | upstream | 0.46 |
| [[p03_sp_multi_modal_config_builder]] | upstream | 0.44 |
| [[multi-modal-config-builder]] | upstream | 0.44 |
| [[p10_lr_multi_modal_config_builder]] | downstream | 0.44 |
| [[bld_config_multi_modal_config]] | downstream | 0.41 |
| [[bld_collaboration_multi_modal_config]] | downstream | 0.41 |
| [[bld_architecture_multi_modal_config]] | downstream | 0.40 |
