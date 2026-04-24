---
id: p01_kc_visual_hierarchy
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Visual Hierarchy in Web Design"
version: 1.0.0
created: 2026-03-30
author: n02_visual_frontend
domain: frontend
quality: 9.0
tags: [visual-hierarchy, web-design, ux, layout, typography, contrast]
tldr: "Size, color, contrast, spacing, and position guide user attention. F-pattern for text, Z-pattern for landing pages."
when_to_use: "When designing web layouts or reviewing UI for attention flow"
keywords: [visual-hierarchy, f-pattern, z-pattern, whitespace, typography]
density_score: 0.92
updated: "2026-04-07"
related:
  - p02_agent_visual_frontend_marketing
  - p01_kc_qa_validation
  - p01_kc_context_scoping
  - p01_kc_spawn_patterns
  - p01_kc_input_hydration
  - p01_kc_workflow_orchestration
  - kc_visual_hierarchy_principles
  - p01_kc_output_formatting
  - p03_ap_visual_frontend_marketing
  - p01_kc_pattern_extraction
---

# Visual Hierarchy in Web Design

## Core Tools

| Tool | Effect | Example |
|------|--------|---------|
| Size | Larger = more important | H1 > H2 > body text |
| Color/Contrast | High contrast attracts eye first | Dark CTA on light background |
| Position | Top-left → bottom-right (LTR cultures) | Logo top-left, CTA above fold |
| Whitespace | Isolation = emphasis | Hero section with generous padding |
| Typography weight | Bold > regular > light | Bold headline, regular body |
| Repetition | Consistent patterns create scannable rhythm | Card grids, list items |

## Reading Patterns

| Pattern | When | Layout |
|---------|------|--------|
| F-pattern | Text-heavy pages (articles, search results) | Important content in first 2 lines + left column |
| Z-pattern | Minimal pages (landing, hero) | Logo (top-left) → CTA (top-right) → content (bottom-left) → action (bottom-right) |
| Gutenberg | Balanced layouts | Primary optical area (top-left) → terminal area (bottom-right) |

## Anti-Pattern
Everything emphasized = nothing emphasized. If all text is bold, bold loses meaning.

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_visual_hierarchy`
- **Tags**: [visual-hierarchy, web-design, ux, layout, typography, contrast]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_visual_frontend_marketing]] | downstream | 0.20 |
| [[p01_kc_qa_validation]] | sibling | 0.20 |
| [[p01_kc_context_scoping]] | sibling | 0.20 |
| [[p01_kc_spawn_patterns]] | sibling | 0.20 |
| [[p01_kc_input_hydration]] | sibling | 0.19 |
| [[p01_kc_workflow_orchestration]] | sibling | 0.19 |
| [[kc_visual_hierarchy_principles]] | sibling | 0.18 |
| [[p01_kc_output_formatting]] | sibling | 0.18 |
| [[p03_ap_visual_frontend_marketing]] | downstream | 0.18 |
| [[p01_kc_pattern_extraction]] | sibling | 0.17 |
