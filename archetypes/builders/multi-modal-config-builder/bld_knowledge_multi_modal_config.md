---
kind: knowledge_card
id: bld_knowledge_card_multi_modal_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for multi_modal_config production
sources: kc_multi_modal_config.md, provider documentation, multi-modal best forctices
quality: 9.0
title: "Knowledge Card Multi Modal Config"
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
  - bld_output_template_multi_modal_config
  - p10_lr_multi_modal_config_builder
  - multi-modal-config-builder
  - kc_multimodal_prompt
  - p04_audio_whisper
  - bld_instruction_multi_modal_config
  - p01_kc_audio_tool
  - p03_sp_audio_tool_builder
  - p03_sp_multi_modal_config_builder
---

# Domain Knowledge: multi_modal_config
## Executive Summary
Multi-modal configs define processing rules for non-text LLM inputs — images, audio, video, documents. They specify format constraints, resolution limits, preprocessing pipelines, model routing, and token cost estimates. Critical for vision-capable agents, document processrs, and any pipeline handling non-text data.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (Tools) |
| LLM Function | CONSTRAIN |
| Max bytes | 2048 |
| Naming | p04_mmc_{capability}.yaml |
| Core | false |
| Modalities | image, audio, video, document, text |
## Provider Multi-Modal Support
| Provider | Image | Audio | Video | PDF |
|----------|-------|-------|-------|-----|
| OpenAI (GPT-4o) | URL/base64 | Whisper | — | — |
| Anthropic (Claude) | base64/URL | — | — | Yes (20 pages) |
| Google (Gemini) | inline/file | native | native | Yes |
| LangChain | HumanMessage image_url | tool-based | — | loader |
## Token Cost Reference
| Input | Approximate Tokens |
|-------|--------------------|
| Image 768px | ~400 |
| Image 1024px | ~750 |
| Image 2048px | ~1500 |
| Audio 1min (transcribed) | ~300 |
| PDF page | ~1200 |
## Patterns
- **Image-first**: document/screenshot analysis — resize, process as images
- **Audio transcription**: voice → Whisper → text → LLM
- **Video keyframes**: extract 1 frame/5s, process as image sequence
- **Modality routing**: images→claude, audio→whisper, text→any
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Max resolution always | 4K = 2000+ tokens each |
| No format validation | API error at runtime |
| No transcription fallback | Model can't handle audio |
| Ignore token costs | Budget blown by images |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_multi_modal_config]] | sibling | 0.70 |
| [[bld_output_template_multi_modal_config]] | downstream | 0.54 |
| [[p10_lr_multi_modal_config_builder]] | downstream | 0.51 |
| [[multi-modal-config-builder]] | downstream | 0.40 |
| [[kc_multimodal_prompt]] | sibling | 0.38 |
| [[p04_audio_whisper]] | downstream | 0.34 |
| [[bld_instruction_multi_modal_config]] | downstream | 0.34 |
| [[p01_kc_audio_tool]] | sibling | 0.34 |
| [[p03_sp_audio_tool_builder]] | downstream | 0.33 |
| [[p03_sp_multi_modal_config_builder]] | downstream | 0.33 |
