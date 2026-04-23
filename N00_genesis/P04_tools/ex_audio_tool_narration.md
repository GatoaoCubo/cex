---
id: ex_audio_tool_narration
kind: audio_tool
pillar: P04
title: "Example Audio Tool: Narration"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: photo_video_editing_with_narration
quality: 8.7
brand_placeholders:
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_TTS_VOICE_ID
tags: [audio_tool, narration, voiceover, n02]
tldr: "Audio tool contract for script cleanup, narration generation, loudness normalization, and subtitle timing."
density_score: 0.88
related:
  - bld_schema_model_registry
  - bld_schema_tagline
  - bld_schema_experiment_tracker
  - n06_schema_brand_config
  - bld_schema_multimodal_prompt
  - bld_schema_handoff_protocol
  - bld_schema_voice_pipeline
  - bld_schema_training_method
  - bld_schema_landing_page
  - bld_schema_model_architecture
---

# Pipeline

1. Normalize the source script.
2. Generate narration in the target voice.
3. Trim silence and normalize loudness.
4. Export subtitle timing cues.

## Output Contract

```yaml
script_clean: string
audio_url: string
duration_seconds: number
subtitle_cues:
  - start:
    end:
    text:
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | downstream | 0.25 |
| [[bld_schema_tagline]] | downstream | 0.24 |
| [[bld_schema_experiment_tracker]] | downstream | 0.24 |
| [[n06_schema_brand_config]] | downstream | 0.23 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.20 |
| [[bld_schema_handoff_protocol]] | downstream | 0.19 |
| [[bld_schema_voice_pipeline]] | downstream | 0.19 |
| [[bld_schema_training_method]] | downstream | 0.19 |
| [[bld_schema_landing_page]] | downstream | 0.18 |
| [[bld_schema_model_architecture]] | downstream | 0.18 |
