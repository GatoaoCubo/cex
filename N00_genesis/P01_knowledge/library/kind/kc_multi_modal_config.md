---
id: p01_kc_multi_modal_config
kind: knowledge_card
type: kind
pillar: P04
title: "Multi-Modal Config — Deep Knowledge for multi_modal_config"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n04_knowledge
domain: multi_modal_config
quality: 9.1
tags: [multi_modal_config, P04, CONSTRAIN, kind-kc]
tldr: "multi_modal_config defines input format, resolution, encoding, and routing rules for multi-modal LLM interactions — images, audio, video, and documents."
when_to_use: "Building, reviewing, or reasoning about multi_modal_config artifacts"
keywords: [multi_modal, image, audio, video, vision, modality, routing]
feeds_kinds: [multi_modal_config]
density_score: null
related:
  - bld_knowledge_card_multi_modal_config
  - bld_output_template_multi_modal_config
  - p10_lr_multi_modal_config_builder
  - kc_multimodal_prompt
  - multi-modal-config-builder
  - p01_kc_vision_tool
  - p03_sp_multi_modal_config_builder
  - bld_schema_multi_modal_config
  - bld_instruction_multi_modal_config
  - bld_architecture_multi_modal_config
---

# Multi-Modal Config

## Spec
```yaml
kind: multi_modal_config
pillar: P04
llm_function: CONSTRAIN
max_bytes: 2048
naming: p04_mmc_{{capability}}.yaml
core: false
```

## What It Is
A multi_modal_config is the configuration spec for processing non-text inputs in LLM pipelines — defining supported modalities (image, audio, video, document), format constraints, resolution/quality limits, preprocessing steps, token cost estimates, and routing rules for which model handles which modality. It is NOT a vision_tool (P04, which performs image analysis), NOT an audio_tool (P04, which processes audio), NOT a model_card (P02, which describes model capabilities).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| OpenAI | Vision API (`gpt-4o`), Whisper, DALL-E | Image input via URL/base64; audio via Whisper transcription |
| Anthropic | Vision in Claude (`image` content blocks) | Base64/URL images, PDF support, up to 20 images per turn |
| Google | Gemini multimodal (`inline_data`, `file_data`) | Native image/audio/video/PDF in single API call |
| LangChain | `HumanMessage` with `image_url` content | Multi-part messages with text + image blocks |
| LlamaIndex | `ImageNode`, `MultiModalVectorStoreIndex` | Separate embedding for images in retrieval |
| CrewAI | Tool-based (vision_tool, audio_tool) | Multimodal via tool delegation, not native |
| Hugging Face | `pipeline("image-to-text")`, `pipeline("audio-classification")` | Task-specific pipelines per modality |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| supported_modalities | list | [image, text] | More = flexible but complex routing |
| image_max_resolution | string | 2048x2048 | Higher = better detail but more tokens (up to 1500/image) |
| image_format | list | [png, jpg, webp, gif] | Broader = more compatible but larger payloads |
| audio_format | list | [mp3, wav, m4a] | wav=lossless but large; mp3=compressed |
| audio_max_duration_s | int | 600 | Longer = more content but higher latency/cost |
| video_max_duration_s | int | 60 | Video is token-expensive; limit aggressively |
| preprocessing | list | [] | resize/compress/transcribe — reduces cost but loses detail |
| routing_model | map | {} | Which model handles which modality |
| token_cost_estimate | map | {} | Per-modality token costs for budget planning |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Image-first | Document analysis, screenshot processing | max_res=2048, format=[png,jpg], preprocess=none |
| Audio transcription | Voice input, podcast processing | audio → Whisper → text, then LLM processes text |
| Video keyframes | Video understanding without full processing | Extract 1 frame/5s, process as image sequence |
| Modality routing | Different models for different inputs | images→claude, audio→whisper, text→any |
| Cost-aware preprocessing | High volume, budget-constrained | Resize images to 1024px, compress audio to 64kbps |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Max resolution always | 4K images = 2000+ tokens each, burns budget | Resize to task-appropriate resolution (768px for classification) |
| No format validation | Unsupported format → API error at runtime | Validate format before API call; convert if needed |
| Audio without transcription fallback | Model doesn't support native audio → failure | Always have whisper/transcription fallback |
| Ignoring token costs | 10 images = 15K tokens, blows context budget | Estimate per-image cost; integrate with context_window_config |

## Integration Graph
```
vision_tool, audio_tool --> [multi_modal_config] --> agent_card, context_window_config
                                     |
                               model_card, model_provider, function_def
```

## Decision Tree
- IF images only THEN simple config: supported=[image], route to vision-capable model
- IF audio input THEN add transcription step: audio→whisper→text→LLM
- IF video input THEN keyframe extraction: 1 frame/5s, process as images
- IF mixed modalities THEN routing map: each modality → best model
- IF cost-constrained THEN aggressive preprocessing: resize, compress, limit count
- DEFAULT: image+text, max_resolution=1024, png/jpg, route to claude/gpt-4o

## Quality Criteria
- GOOD: supported_modalities, format constraints, resolution limits all present
- GREAT: routing map, token cost estimates, preprocessing pipeline, fallback chain
- FAIL: no format validation, no resolution limits, no routing, ignore token costs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_multi_modal_config]] | sibling | 0.71 |
| [[bld_output_template_multi_modal_config]] | downstream | 0.61 |
| [[p10_lr_multi_modal_config_builder]] | downstream | 0.53 |
| [[kc_multimodal_prompt]] | sibling | 0.46 |
| [[multi-modal-config-builder]] | related | 0.45 |
| [[p01_kc_vision_tool]] | sibling | 0.42 |
| [[p03_sp_multi_modal_config_builder]] | upstream | 0.41 |
| [[bld_schema_multi_modal_config]] | downstream | 0.40 |
| [[bld_instruction_multi_modal_config]] | upstream | 0.39 |
| [[bld_architecture_multi_modal_config]] | downstream | 0.38 |
