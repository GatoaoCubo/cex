---
id: p03_constraint_cf_presentation
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "n01_intelligence"
name: "Content Factory Presentation Format Constraints"
constraint_type: "format_rules"
pattern: "multi_rule_set"
quality: null
tags: [constraint_spec, content-factory, presentation, slides, canva]
tldr: "Presentation constraints: 10-30 slides, 3-5 bullets/slide, speaker notes, PPTX+PDF+GSlides export"
description: "Governs all presentation outputs from dag_cf_presentation for clarity and brand consistency"
provider_compat: "canva, google_slides, powerpoint"
fallback: "Manual design review if automated validation unavailable"
temperature_override: "0.4"
max_tokens: "2048"
---

## Overview

Constrains all presentation artifacts produced by the Content Factory presentation pipeline (dag_cf_presentation). Ensures every deck meets professional presentation standards with clear visual hierarchy, brand consistency, and multi-format export. Applied at quality_check node before export.

## Constraint Definition

### Structure Rules
| Element | Min | Target | Max |
|---------|-----|--------|-----|
| total_slides | 10 | 20 | 30 |
| bullets_per_slide | 2 | 3 | 5 |
| words_per_bullet | 5 | 8 | 15 |
| words_per_slide | 15 | 30 | 50 |
| speaker_notes_words | 50 | 150 | 300 |

### MUST Rules
- Deck MUST include: title slide, agenda/overview, content slides, summary/CTA slide
- Title slide MUST show: presentation title, subtitle, author/brand, date
- Every content slide MUST have speaker notes (min 50 words)
- Visual slides (charts, diagrams) MUST have alt text for accessibility
- Brand template MUST be applied: logo placement, color palette, fonts
- Slide numbering MUST appear on all slides except title
- Export MUST produce: PPTX, PDF, Google Slides link

### MUST NOT Rules
- MUST NOT exceed 5 bullet points per slide
- MUST NOT use full sentences as bullets (max 15 words per bullet)
- MUST NOT have text-only slides for more than 3 consecutive slides
- MUST NOT use fonts outside the brand-approved set
- MUST NOT have slides without visual hierarchy (title + body distinction)

### Slide Types
| Type | Frequency | Description |
|------|-----------|-------------|
| title | 1 per deck | Opening with title, subtitle, brand |
| agenda | 1 per deck | Section overview with navigation |
| content | 60-70% | Key points with bullets + visual |
| visual | 20-30% | Chart, diagram, or image-dominant |
| divider | per section | Section transition with section title |
| cta | 1 per deck | Closing with call-to-action |

### Export Formats
| Format | Engine | Spec |
|--------|--------|------|
| PPTX | Canva/python-pptx | 16:9, embedded fonts, editable |
| PDF | Export from PPTX | Flattened, non-editable, print-ready |
| Google Slides | API upload | Shared link, view or edit permissions |

### Quality Metrics
| Metric | Min | Target | Max |
|--------|-----|--------|-----|
| visual_slide_ratio | 20% | 30% | 50% |
| avg_words_per_slide | 15 | 30 | 50 |
| slides_with_notes | 90% | 100% | 100% |

## Provider Compatibility

| Provider | Support | Method |
|----------|---------|--------|
| Canva | native | Template-based design with brand kit |
| python-pptx | native | Programmatic slide generation |
| Google Slides | native | API-driven creation and sharing |
| PowerPoint | native | PPTX direct export |

## Integration

- Consumed by: dag_cf_presentation (quality_check node)
- Validates outputs from: assemble_deck node
- Cross-references: brand_config.yaml (palette, fonts, logo placement)
- Feeds: quality_gate node in dag_cf_master for final approval
