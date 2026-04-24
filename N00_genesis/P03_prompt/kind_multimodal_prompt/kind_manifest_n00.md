---
id: n00_multimodal_prompt_manifest
kind: knowledge_card
8f: F3_inject
pillar: P03
nucleus: n00
title: "Multimodal Prompt -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, multimodal_prompt, p03, n00, archetype, template]
density_score: 0.99
related:
  - bld_schema_multimodal_prompt
  - bld_schema_reranker_config
  - kc_multimodal_prompt
  - bld_knowledge_card_multi_modal_config
  - p03_sp_multimodal_prompt_builder
  - bld_schema_integration_guide
  - bld_schema_sandbox_spec
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A multimodal_prompt is a cross-modal prompt pattern that combines vision, audio, and text inputs into a single coherent LLM invocation. It specifies how different modalities are encoded, prioritized, and referenced within the prompt context, and what kind of cross-modal reasoning the model should apply. The output is a structured prompt envelope that enables models like Claude or GPT-4V to reason across image, audio, and text simultaneously.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `multimodal_prompt` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| modalities | list | yes | Active modalities: text, image, audio, video |
| encoding_rules | map | yes | Per-modality encoding format (base64, url, file_path) |
| cross_modal_instruction | string | yes | How to relate modalities in reasoning |
| fallback_text_only | boolean | no | Whether to degrade gracefully if modality unavailable |

## When to use
- When the LLM task requires reasoning across image + text (e.g., screenshot analysis, document OCR)
- When building voice-enabled agents that combine STT output with text prompts
- When a pipeline ingests documents, images, or audio and the prompt must reference all modalities

## Builder
`archetypes/builders/multimodal_prompt-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind multimodal_prompt --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: mmp_screenshot_to_bug_report
kind: multimodal_prompt
pillar: P03
nucleus: n05
title: "Screenshot to Bug Report"
version: 1.0
quality: null
---
modalities: [image, text]
encoding_rules:
  image: base64
  text: utf8
cross_modal_instruction: "Analyze the screenshot. Identify UI errors. Reference specific elements."
fallback_text_only: true
```

## Related kinds
- `vision_tool` (P04) -- tool that captures or preprocesses images before multimodal_prompt
- `audio_tool` (P04) -- tool that processes audio before it enters the multimodal_prompt
- `multi_modal_config` (P04) -- configuration layer for input format and resolution settings
- `prompt_template` (P03) -- base template that multimodal_prompt extends with modal slots

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_multimodal_prompt]] | downstream | 0.50 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[kc_multimodal_prompt]] | sibling | 0.38 |
| [[bld_knowledge_card_multi_modal_config]] | sibling | 0.37 |
| [[p03_sp_multimodal_prompt_builder]] | related | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_sandbox_spec]] | downstream | 0.36 |
| [[bld_schema_benchmark_suite]] | downstream | 0.36 |
| [[bld_schema_voice_pipeline]] | downstream | 0.36 |
| [[bld_schema_usage_report]] | downstream | 0.36 |
