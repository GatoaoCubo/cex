---
id: p01_kc_slide_generation
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CSV-Driven Slide Generation Pipeline with Design Tokens and Emotion Arcs"
version: 1.0.0
created: 2026-03-26
updated: 2026-03-26
author: builder_agent
domain: content_generation
quality: 9.1
tags: [slides, html-generation, design-tokens, chart-js, emotion-arc, csv-pipeline, presentation]
tldr: "Pipeline generates HTML slides via 8 CSVs (strategy, layout, color, typography) with Chart.js, design tokens and Duarte Sparkline emotion arcs"
when_to_use: "Generate data-driven HTML presentations with engagement strategy based on emotion arcs"
keywords: [slide-generation, design-tokens, chart-js, sparkline, csv-pipeline, duarte-method]
long_tails:
  - "How to automatically generate HTML slides from CSV data"
  - "How to apply emotion arcs in presentations to maintain engagement"
axioms:
  - "ALWAYS use design tokens (var(--x)) — NEVER hardcoded hex"
  - "ALWAYS use Chart.js for data — NEVER CSS-only bars"
  - "NEVER put more than 1 main message per slide"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_function_become]
density_score: null
data_source: "https://www.duarte.com/resources/books/resonate/"
related:
  - kc_webinar_script
  - bld_output_template_pitch_deck
  - p03_sp_pitch_deck_builder
  - bld_instruction_pitch_deck
  - p05_qg_pitch_deck
  - p01_kc_marp_cli
  - bld_collaboration_pitch_deck
  - bld_tools_pitch_deck
  - p03_sp_webinar_script_builder
  - p01_kc_brand_propagation_arch
---

## Summary

CSV-driven pipeline that generates HTML slides with design tokens, Chart.js and emotion arcs (Duarte Sparkline).
8 CSVs control strategy (15 deck structures), layout (25 variants), typography, color, backgrounds, copy (25 formulas like PAS/AIDA/FAB), charts (25 Chart.js types) and CSS animations.
BM25 contextual search selects components by deck position and previous emotion.
Token validator (slide-token-validator.py) rejects any hardcoded hex in the final HTML.

## Spec

| CSV | Content | Count |
|-----|---------|-------|
| slide-strategies | Deck structures + emotion arcs + sparkline beats | 15 |
| slide-layouts | Layout variants + component + animations | 25 |
| slide-layout-logic | Goal -> Layout + break_pattern flag | -- |
| slide-typography | Content type -> Typography scale | -- |
| slide-color-logic | Emotion -> Color treatment | -- |
| slide-backgrounds | Slide type -> Image category (Pexels/Unsplash) | -- |
| slide-copy | Copywriting formulas (PAS, AIDA, FAB) | 25 |
| slide-charts | Chart.js types with config | 25 |

Pipeline por slide: layout-logic → typography → color-logic → backgrounds → animations → HTML.
Duarte Sparkline calcula break patterns em 1/3 e 2/3 do deck, alternando "What Is" (frustration) com "What Could Be" (hope).
Design system persistido em MASTER.md (global) + pages/*.md (overrides por pagina).
Retrieval: page-specific override → fallback MASTER — garante consistencia visual.

## Patterns

| Trigger | Action |
|---------|--------|
| New deck requested | BM25 search in slide-strategies.csv for structure + emotion arc |
| Slide at position 1/3 or 2/3 | Activate break_pattern flag (invert emotion) |
| Quantitative data in slide | Chart.js with tokens (borderColor: var(--x)) |
| Brand customization | Persist design system: MASTER.md + page overrides |
| Search for specific component | Contextual search: --position N --prev-emotion X |

## Anti-Patterns

- Hardcoded hex (#FF6B6B) in HTML -- token validator rejects
- CSS-only bars for data -- always Chart.js via CDN
- Slide without navigation (keyboard arrows, click, progress bar)
- Monotonous deck without emotion arc -- audience disengages
- Slide with multiple messages (cognitive overload)

## Code

<!-- lang: python | purpose: contextual slide search with BM25 -->
```bash
# Basic search: finds deck strategy
python scripts/search-slides.py "investor pitch"

# Contextual search: considers position and previous emotion
python scripts/search-slides.py "problem slide" \
  --context --position 2 --total 9

# Domain-specific search
python scripts/search-slides.py "revenue growth" -d chart
```

```css
/* Design tokens — source of truth */
background: var(--slide-bg);
color: var(--color-primary);
font-family: var(--typography-font-heading);

/* Chart.js com tokens */
borderColor: var(--color-primary);
```

## References

- source: https://www.duarte.com/resources/books/resonate/
- source: https://www.chartjs.org/docs/latest/
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_webinar_script]] | sibling | 0.44 |
| [[bld_output_template_pitch_deck]] | downstream | 0.39 |
| [[p03_sp_pitch_deck_builder]] | downstream | 0.36 |
| [[bld_instruction_pitch_deck]] | downstream | 0.34 |
| [[p05_qg_pitch_deck]] | downstream | 0.30 |
| [[p01_kc_marp_cli]] | sibling | 0.29 |
| [[bld_collaboration_pitch_deck]] | downstream | 0.28 |
| [[bld_tools_pitch_deck]] | downstream | 0.26 |
| [[p03_sp_webinar_script_builder]] | downstream | 0.25 |
| [[p01_kc_brand_propagation_arch]] | sibling | 0.23 |
