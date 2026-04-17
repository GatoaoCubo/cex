---
id: ex_multi_modal_config_photo_video_narration
kind: multi_modal_config
pillar: P03
title: "Example Multi Modal Config: Photo Video Narration"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: photo_video_editing_with_narration
quality: null
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
  - BRAND_TONE
  - BRAND_TTS_VOICE_ID
tags: [multi_modal_config, photo, video, narration, n02]
tldr: "Configuration for combining stills, motion, captions, and voiceover into branded short-form content."
density_score: 0.9
---

# Config

```yaml
input_modalities:
  - image
  - video
  - script
output_modalities:
  - edited_video
  - voiceover_audio
  - subtitles
style:
  voice: "{{BRAND_VOICE}}"
  tone: "{{BRAND_TONE}}"
  pacing: medium
voiceover:
  voice_id: "{{BRAND_TTS_VOICE_ID}}"
  max_words: 180
editing:
  aspect_ratios: ["9:16", "1:1", "16:9"]
  caption_mode: burned_in
  cut_style: quick_clear
```

