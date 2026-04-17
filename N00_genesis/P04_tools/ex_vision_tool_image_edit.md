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
quality: null
brand_placeholders:
  - BRAND_NAME
  - BRAND_VOICE
tags: [vision_tool, image-edit, creative, n02]
tldr: "Vision editing contract for preparing branded images and frame selections before narration and publishing."
density_score: 0.87
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

