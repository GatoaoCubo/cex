---
id: p01_kc_color_theory_applied
kind: knowledge_card
pillar: P01
title: "Color Theory Applied"
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.0
tags: [knowledge, frontend, color, ui, accessibility, wcag]
tldr: "HSL color model, 60-30-10 rule, WCAG contrast compliance, semantic color systems, and dark mode implementation patterns"
density_score: 0.88
---

# Color Theory Applied

## Quick Reference

```yaml
color_model: HSL # Hue Saturation Lightness
composition_rule: "60-30-10" # 60% neutral, 30% primary, 10% accent
wcag_contrast:
  AA: "4.5:1" # minimum
  AAA: "7:1" # enhanced
semantic_colors:
  success: "#22c55e"
  warning: "#f59e0b" 
  error: "#ef4444"
  info: "#3b82f6"
codexa_accent: "#50C878" # signature green
surface_scale: "900-500" # dark to light
css_pattern: "var(--color-name)"
dark_mode_rule: "invert_lightness_preserve_hue"
```

## Key Concepts

**HSL Color Model**: Hue (0-360°), Saturation (0-100%), Lightness (0-100%). Superior to RGB/HEX for systematic color generation. Easy lightness manipulation for variants.

**60-30-10 Composition Rule**: 60% neutral/background colors, 30% primary brand colors, 10% accent colors for highlights. Maintains visual hierarchy and prevents color overwhelm.

**WCAG Contrast Compliance**: AA standard requires 4.5:1 contrast ratio for normal text, 3:1 for large text. AAA enhanced standard requires 7:1 for normal text, 4.5:1 for large text.

**Semantic Color System**: Consistent color meanings across interface. Success (green), Warning (amber), Error (red), Info (blue). Users build mental models around these associations.

**Surface Scale Architecture**: Systematic grayscale from surface-900 (darkest) to surface-500 (lightest). Provides consistent elevation and depth hierarchy.

**Dark Mode Implementation**: Invert lightness values while preserving hue and saturation. Maintains brand recognition while reducing eye strain in low-light environments.

## Patterns

**CSS Custom Properties Pattern**: Define colors as CSS variables `--color-primary-500`, `--color-surface-800`. Enables theme switching and systematic color management across components.

**Shade Generation Pattern**: Base color + HSL manipulation. Generate lighter shades by increasing lightness, darker by decreasing. Maintain consistent saturation for brand cohesion.

**Contextual Color Selection**: Use semantic colors for state communication, neutral colors for content hierarchy, accent colors sparingly for calls-to-action and interactive elements.

## Golden Rules

**Contrast First**: Always validate contrast ratios before shipping. Use tools like WebAIM Contrast Checker. Accessibility is non-negotiable for inclusive design.

**Systematic Over Custom**: Build color systems, not ad-hoc selections. Define palettes with mathematical relationships rather than arbitrary color choices.

**Test in Context**: Colors behave differently on various backgrounds and in different lighting conditions. Test color combinations in actual usage scenarios, not isolation.

## References

- WCAG 2.1 Color Contrast Guidelines
- Material Design Color System
- Tailwind CSS Color Palette Architecture
- HSL Color Model Specification