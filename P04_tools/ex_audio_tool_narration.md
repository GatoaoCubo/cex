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
quality: null
brand_placeholders:
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_TTS_VOICE_ID
tags: [audio_tool, narration, voiceover, n02]
tldr: "Audio tool contract for script cleanup, narration generation, loudness normalization, and subtitle timing."
density_score: 0.88
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

