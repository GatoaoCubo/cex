---
id: p03_ap_cf_generate_presentation
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n02_marketing"
title: "Generate Presentation Deck from Topic"
action: "Generate a slide-by-slide presentation with content, speaker notes, and visual layout directions from a topic"
input_required:
  - "topic: string — presentation subject"
  - "slides_count: integer — target number of slides (5-30)"
  - "audience: string — who will watch the presentation"
  - "format: enum — keynote, workshop, pitch, webinar"
  - "brand_config: object — {{BRAND_*}} variables"
output_expected: "Slide deck structure with per-slide content, speaker notes, layout type, and Canva template mapping"
purpose: "Produce presentation-ready slide content that maps directly to Canva templates for instant design"
steps_count: 4
timeout: "90s"
edge_cases:
  - "slides_count over 30 — split into multi-part presentation with bridge slides"
  - "format=pitch with no product defined — extract from brand_config.product"
  - "No audience specified — infer from format (pitch=investors, workshop=practitioners)"
constraints:
  - "Do NOT generate actual slide images — output text + layout directions for Canva"
  - "Max 6 bullet points per slide, max 8 words per bullet"
  - "Speaker notes 50-150 words per slide"
domain: "content_factory"
quality: 9.1
tags: [action_prompt, content_factory, presentation, slides, canva]
tldr: "Generate slide-by-slide presentation (content + speaker notes + layout) from topic for Canva template mapping"
density_score: 0.92
---

## Context
Presentations are high-frequency content factory outputs — used for webinars, pitches,
workshops, and social carousel repurposing. This prompt produces the textual structure
that maps to Canva brand templates for instant visual production.
Purpose: decouple content creation from design, enabling parallel production.

## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| topic | string | Free text, 3-100 chars | YES |
| slides_count | integer | 5-30 | YES |
| audience | string | Viewer profile | YES |
| format | enum | keynote, workshop, pitch, webinar | YES |
| brand_config | object | {{BRAND_*}} YAML variables | YES |

## Execution
1. Plan slide arc: opening hook → problem → solution → evidence → CTA
2. Assign layout type per slide (title, content, quote, chart_placeholder, image_placeholder, cta)
3. Write per-slide: headline (≤8 words), bullets (≤6), speaker notes (50-150 words)
4. Map each slide to Canva template type and generate presentation metadata

## Output
Format: YAML + Markdown
Structure:
```yaml
presentation:
  title: "{{title}}"
  format: "{{format}}"
  slides:
    - id: 1
      layout: "title"
      headline: "{{headline}}"
      bullets: []
      speaker_notes: "{{notes}}"
      canva_template: "brand_title_slide"
    - id: 2
      layout: "content"
      headline: "{{headline}}"
      bullets: ["{{b1}}", "{{b2}}"]
      speaker_notes: "{{notes}}"
      canva_template: "brand_content_slide"
```

## Validation
- Slide count matches slides_count input
- No slide exceeds 6 bullets or 8 words per bullet
- Speaker notes present for every slide (50-150 words)
- Slide arc follows opening → body → CTA structure
- Edge case: 30+ slides flagged with split recommendation

## References
- Canva Business API (template mapping)
- wf_cf_promote (social carousel repurposing)
