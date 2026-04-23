---
id: ex_vision_tool_image_edit
kind: vision_tool
pillar: P04
title: "Example Vision Tool: Image Edit for Brand Content"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: photo_video_editing_with_narration
quality: 8.7
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
tags: [vision_tool, image-edit, creative, n02]
tldr: "Vision editing contract for preparing branded images and frame selections before narration and publishing."
density_score: 0.87
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - n06_schema_brand_config
  - bld_schema_tagline
  - bld_schema_training_method
  - bld_schema_multimodal_prompt
  - bld_schema_model_architecture
  - bld_schema_dataset_card
  - bld_schema_retriever_config
  - bld_schema_handoff_protocol
---

# Tasks

- clean_background
- crop_for_channel
- add_safe_text_area
- select_best_frame
- generate_alt_text

## Input Schema

```yaml
asset_url: string
channel: string
creative_goal: string
brand_voice: "{{BRAND_VOICE}}"
```

## Output Schema

```yaml
edited_asset_url: string
thumbnail_url: string
alt_text: string
notes: string
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | downstream | 0.59 |
| [[bld_schema_experiment_tracker]] | downstream | 0.52 |
| [[n06_schema_brand_config]] | downstream | 0.51 |
| [[bld_schema_tagline]] | downstream | 0.48 |
| [[bld_schema_training_method]] | downstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.41 |
| [[bld_schema_model_architecture]] | downstream | 0.41 |
| [[bld_schema_dataset_card]] | downstream | 0.39 |
| [[bld_schema_retriever_config]] | downstream | 0.39 |
| [[bld_schema_handoff_protocol]] | downstream | 0.38 |
