---
id: p03_pt_cf_slide_deck
kind: prompt_template
pillar: P03
title: "Content Factory — Slide Deck Template"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
variables:
  - name: BRAND_NAME
    type: string
    required: true
    default: null
    description: "Company or brand name"
  - name: BRAND_VOICE
    type: string
    required: true
    default: null
    description: "Brand tone descriptor"
  - name: CONTENT_TOPIC
    type: string
    required: true
    default: null
    description: "Presentation subject"
  - name: CONTENT_PRESENTATION_TITLE
    type: string
    required: true
    default: null
    description: "Title of the presentation"
  - name: CONTENT_SLIDES_COUNT
    type: integer
    required: false
    default: 12
    description: "Target number of slides"
  - name: CONTENT_KEY_POINTS
    type: list
    required: true
    default: null
    description: "3-6 key points to cover"
  - name: TARGET_AUDIENCE
    type: string
    required: true
    default: null
    description: "Audience persona and context"
  - name: CONTENT_CTA
    type: string
    required: true
    default: null
    description: "Closing call-to-action"
  - name: CONTENT_VISUAL_STYLE
    type: string
    required: false
    default: "minimal-dark"
    description: "Visual direction — minimal-dark, corporate-light, bold-colorful, editorial"
variable_syntax: mustache
composable: true
domain: content_factory
quality: 9.1
tags: [prompt_template, slides, presentation, deck, content_factory, P03]
tldr: "Reusable mold for generating slide deck content with titles, bullets, speaker notes, and visual cues"
keywords: [slide deck, presentation, slides, marp, speaker notes, content factory]
density_score: 0.90
---

# Slide Deck Template

## Purpose
Generates structured slide deck content from a presentation brief. Each slide includes a title, bullet points, speaker notes, and visual direction cues. Output is formatted for Marp (Markdown to PPTX/PDF/HTML) compilation in the Content Factory pipeline. Also usable as input for Canva presentation creation.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| BRAND_NAME | string | yes | — | Company or brand name |
| BRAND_VOICE | string | yes | — | Tone descriptor |
| CONTENT_TOPIC | string | yes | — | Subject |
| CONTENT_PRESENTATION_TITLE | string | yes | — | Presentation title |
| CONTENT_SLIDES_COUNT | integer | no | 12 | Slide count |
| CONTENT_KEY_POINTS | list | yes | — | Key points |
| TARGET_AUDIENCE | string | yes | — | Audience persona |
| CONTENT_CTA | string | yes | — | Closing CTA |
| CONTENT_VISUAL_STYLE | string | no | minimal-dark | Visual style |

## Template Body

```
You are a presentation designer for {{BRAND_NAME}}. Write in a {{BRAND_VOICE}} tone.

TITLE: {{CONTENT_PRESENTATION_TITLE}}
TOPIC: {{CONTENT_TOPIC}}
AUDIENCE: {{TARGET_AUDIENCE}}
SLIDES: {{CONTENT_SLIDES_COUNT}}
STYLE: {{CONTENT_VISUAL_STYLE}}

Create a slide deck covering:
{{CONTENT_KEY_POINTS}}

## OUTPUT FORMAT (Marp-compatible Markdown)

---
marp: true
theme: {{CONTENT_VISUAL_STYLE}}
paginate: true
---

### Slide 1 — Title Slide
# {{CONTENT_PRESENTATION_TITLE}}
**{{BRAND_NAME}}**
[VISUAL: brand logo + {{CONTENT_VISUAL_STYLE}} background]

<!-- speaker notes: Introduce yourself. Set context for {{TARGET_AUDIENCE}}. -->

---

### Slide 2 — Agenda
- Point 1
- Point 2
- ...

<!-- speaker notes: Preview what the audience will learn. -->

---

### Slides 3 to N-2 — Content Slides
For EACH item in {{CONTENT_KEY_POINTS}}:

#### Slide [N]: [Key Point Title]
- Bullet 1 (max 8 words)
- Bullet 2 (max 8 words)
- Bullet 3 (max 8 words)
[VISUAL: suggested diagram, chart, or image description]

<!-- speaker notes: 2-3 sentences expanding on the key point. Include data or example. -->

---

### Slide N-1 — Summary
## Key Takeaways
- [Recap point 1]
- [Recap point 2]
- [Recap point 3]

---

### Slide N — CTA
## {{CONTENT_CTA}}
[VISUAL: contact info, QR code, or next step graphic]

<!-- speaker notes: Deliver {{CONTENT_CTA}} clearly. Repeat the link/action. -->

## CONSTRAINTS
- Exactly {{CONTENT_SLIDES_COUNT}} slides (+/- 1)
- Max 3 bullets per content slide, max 8 words per bullet
- Every slide has speaker notes (2-3 sentences)
- Every content slide has a [VISUAL] cue
- Use Marp --- separators between slides
- Match {{BRAND_VOICE}} and {{CONTENT_VISUAL_STYLE}} throughout
```

## Quality Gates

| Gate | Status | Notes |
|------|--------|-------|
| H01 | PASS | id matches ^p03_pt_[a-z][a-z0-9_]+$ |
| H02 | PASS | All required frontmatter fields present |
| H03 | PASS | All {{vars}} in body exist in variables list |
| H04 | PASS | All variables in list appear in template body |
| H05 | PASS | File size < 8192 bytes |
| H06 | PASS | variable_syntax is mustache consistently |

## Examples

### Example 1: 12-slide investor pitch
Variables:
```yaml
BRAND_NAME: "NeuralShip"
BRAND_VOICE: "confident-data-driven"
CONTENT_TOPIC: "AI-powered logistics optimization"
CONTENT_PRESENTATION_TITLE: "NeuralShip — Series A Pitch"
CONTENT_SLIDES_COUNT: 12
CONTENT_KEY_POINTS:
  - "The $400B logistics inefficiency problem"
  - "How our AI reduces delivery time by 35%"
  - "Unit economics and path to profitability"
  - "Team and competitive moat"
TARGET_AUDIENCE: "Series A VCs with logistics portfolio interest"
CONTENT_CTA: "Let's schedule a deep dive — neural@ship.com"
CONTENT_VISUAL_STYLE: "minimal-dark"
```
