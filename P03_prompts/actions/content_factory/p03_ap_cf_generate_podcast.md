---
id: p03_ap_cf_generate_podcast
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate Podcast Episode Script"
action: "Generate a podcast episode script with segments, talking points, and show notes from a topic"
input_required:
  - "topic: string — episode subject"
  - "duration_minutes: integer — target episode length (5-60)"
  - "format: enum — solo, interview, panel, storytelling"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Complete podcast script with intro, segments, transitions, outro, and distribution metadata"
purpose: "Automate podcast scripting so episodes can be recorded with minimal preparation"
steps_count: 4
timeout: "90s"
edge_cases:
  - "format=interview but no guest defined — generate generic guest question framework"
  - "duration under 5 min — format as 'micro-episode' with single segment"
  - "Topic too niche — add context-setting intro segment for general audience"
constraints:
  - "Do NOT generate audio files — output is text script only"
  - "Do NOT include specific guest names unless provided in input"
  - "Word count must approximate duration (150 words/minute spoken)"
domain: "content_factory"
quality: null
tags: [action_prompt, content_factory, podcast, audio, script]
tldr: "Generate podcast episode script (segments + talking points + show notes) from topic and duration for recording"
density_score: 0.91
---

## Context
Podcasts are a growing content factory channel. This prompt generates the complete episode
script — structured into timed segments with talking points and transitions — so the host
can record with minimal preparation. Show notes are included for distribution platforms.
Purpose: reduce episode preparation time from hours to minutes.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| topic | string | Free text, 3-100 chars | YES |
| duration_minutes | integer | 5-60 | YES |
| format | enum | solo, interview, panel, storytelling | YES |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Calculate word budget from duration (150 words/min) and plan segment count
2. Generate episode structure: intro (10%), body segments (75%), outro + CTA (15%)
3. Write each segment: title, talking points (3-5), key quotes, transition line
4. Compile show notes: episode summary, timestamps, links placeholders, CTA

## Output
Format: Markdown
Structure:
```markdown
# {{Episode Title}}
**Duração**: {{duration}} min | **Formato**: {{format}}

## Intro [00:00 - {{end}}]
{{intro script with hook}}

## Segmento 1: {{title}} [{{start}} - {{end}}]
**Pontos**:
- {{talking_point_1}}
- {{talking_point_2}}
**Transição**: {{transition_line}}

## Outro + CTA [{{start}} - {{end}}]
{{outro script}}

---
## Show Notes
- {{summary}}
- Timestamps: {{list}}
- Links: {{REF_1}}, {{REF_2}}
```

## Validation
- Total script word count within ±15% of duration × 150 words/min
- Every segment has timing marks, talking points, and transition
- Show notes include summary, timestamps, and CTA
- Edge case: interview format includes question framework
- Brand voice from brand_config applied to intro and outro

## References
- wf_cf_promote (episode promotion workflow)
- brand_config.yaml (host persona, show identity)
