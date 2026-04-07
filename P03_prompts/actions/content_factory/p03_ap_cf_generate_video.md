---
id: p03_ap_cf_generate_video
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate Video Script and Production Brief"
action: "Generate a video script with scenes, narration, and visual directions from a topic and duration target"
input_required:
  - "topic: string — video subject"
  - "duration_seconds: integer — target video length (30-600)"
  - "style: enum — talking_head, screencast, animation, mixed"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Scene-by-scene script with narration text, visual cues, timing marks, and YouTube metadata"
purpose: "Produce publish-ready video scripts that feed into YouTube upload workflow with zero manual editing"
steps_count: 4
timeout: "90s"
edge_cases:
  - "Duration under 30s — format as YouTube Short with vertical framing notes"
  - "Duration over 600s — split into parts with end-screen cross-references"
  - "Style=animation without visual assets — output storyboard descriptions for Canva"
constraints:
  - "Do NOT generate actual video files — output is script + directions only"
  - "Do NOT include copyrighted music suggestions — use 'royalty-free' placeholder"
  - "Narration word count must match duration (avg 150 words/minute)"
domain: "content_factory"
quality: 9.1
tags: [action_prompt, content_factory, video, youtube, script]
tldr: "Generate scene-by-scene video script with narration, visual cues, and YouTube metadata from topic and duration"
density_score: 0.93
---

## Context
Content Factory generates video content at scale. This action prompt produces the textual
foundation — script, scene directions, and metadata — that feeds into the YouTube publish
workflow. The output is designed for direct use without manual script editing.
Purpose: automate the most time-consuming part of video production (scripting).

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| topic | string | Free text, 3-100 chars | YES |
| duration_seconds | integer | 30-600 | YES |
| style | enum | talking_head, screencast, animation, mixed | YES |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Calculate target word count from duration (150 words/min) and plan scene count
2. Generate hook (first 5s), body scenes, and CTA (last 10s) with timing marks
3. For each scene: write narration text + visual direction + on-screen text suggestions
4. Compile YouTube metadata: title (≤60 chars), description, tags, thumbnail text suggestion

## Output
Format: Markdown with YAML metadata block
Structure:
```yaml
video:
  title: "{{title}}"
  duration_target: {{seconds}}
  scenes:
    - id: 1
      timestamp: "00:00-00:05"
      narration: "{{hook text}}"
      visual: "{{camera/screen direction}}"
      on_screen: "{{text overlay}}"
  youtube_meta:
    title: "{{≤60 chars}}"
    description: "{{2-3 paragraphs}}"
    tags: ["{{tag1}}", "{{tag2}}"]
    thumbnail_text: "{{3-5 words}}"
```

## Validation
- Total narration word count within ±10% of duration × 2.5 words/sec
- Every scene has narration + visual direction (no empty fields)
- YouTube title ≤ 60 characters
- Edge case: duration < 30s formatted as Short with vertical notes
- Brand voice consistent across all narration text

## References
- wf_cf_publish_youtube (downstream workflow)
- Canva API (thumbnail generation)
