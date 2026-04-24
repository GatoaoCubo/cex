---
id: p01_kc_typography_web
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Typography Web"
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.1
tags: [knowledge, frontend]
tldr: "Typography Web patterns and best practices"
density_score: 0.88
updated: "2026-04-07"
related:
  - n02_kc_typography_web
  - kc_visual_hierarchy_principles
  - p05_output_social_card
  - n06_output_pricing_page
  - p10_dtc_design_token_contract
  - n06_output_visual_identity
  - p05_output_email_template
  - n02_kc_email_html_responsive
  - p05_output_visual_report
  - p05_output_style_guide
---

# Typography Web

## Quick Reference

```yaml
font_stacks:
  headings: "Geist Variable, system-ui, sans-serif"
  body: "Inter, -apple-system, BlinkMacSystemFont, sans-serif"
  code: "JetBrains Mono, Menlo, Monaco, monospace"
scale: 1.25  # major third
line_heights:
  body: 1.5
  headings: 1.2
letter_spacing:
  headings: "-0.02em"
  body: "0"
loading: "font-display: swap"
```

## Key Concepts

**Variable Fonts**: Single font file containing multiple weights/widths via axes (wght, wdth, slnt). Reduces HTTP requests and enables fluid typography scaling.

**Font Loading Strategy**: font-display: swap prevents invisible text during font download (FOIT). System font fallbacks ensure immediate text rendering.

**Type Scale**: Mathematical progression using ratios (1.25 major third) creates consistent visual hierarchy. Base size typically 16px, scaling up for headings.

**Line Height**: Relative units maintain proportional spacing. 1.5 for body text ensures readability, 1.2 for headings prevents excessive whitespace.

**Letter Spacing**: Negative values (-0.02em) on headings compensate for optical spacing at larger sizes. Body text typically uses default (0).

**Font Pairing**: Contrast between serif/sans-serif or different font personalities. Geist Variable (geometric sans) + Inter (humanist sans) provides subtle contrast.

## Patterns

**Progressive Enhancement**:
```css
@font-face {
  font-family: 'Inter';
  src: url('inter.woff2') format('woff2');
  font-display: swap;
  font-weight: 100 900;
}
```

**Fluid Typography**:
```css
h1 {
  font-size: clamp(2rem, 4vw, 4rem);
  line-height: 1.2;
  letter-spacing: -0.02em;
}
```

**System Font Stack**:
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
```

## Golden Rules

**Always provide fallbacks**: System fonts ensure immediate rendering while web fonts load. Never rely solely on web fonts without fallback stacks.

**Optimize for performance**: Use font-display: swap, preload critical fonts, subset font files to reduce payload. Variable fonts reduce total file size.

**Maintain consistency**: Establish type scale, stick to 2-3 font families maximum. Use consistent line-heights and letter-spacing across similar elements.

## References

- Variable Fonts Guide: web.dev/variable-fonts
- Font Loading: developer.mozilla.org/en-US/docs/Web/CSS/@font-face
- Type Scale Calculator: type-scale.com

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_typography_web`
- **Tags**: [knowledge, frontend]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_kc_typography_web]] | sibling | 0.70 |
| [[kc_visual_hierarchy_principles]] | sibling | 0.32 |
| [[p05_output_social_card]] | downstream | 0.31 |
| [[n06_output_pricing_page]] | downstream | 0.28 |
| [[p10_dtc_design_token_contract]] | downstream | 0.27 |
| [[n06_output_visual_identity]] | downstream | 0.24 |
| [[p05_output_email_template]] | downstream | 0.23 |
| [[n02_kc_email_html_responsive]] | sibling | 0.22 |
| [[p05_output_visual_report]] | downstream | 0.21 |
| [[p05_output_style_guide]] | downstream | 0.20 |
