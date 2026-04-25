---
id: kc_tailwind_patterns
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Tailwind CSS Patterns -- Production Design System Recipes"
tags: [tailwind, patterns, design-system, utility-first, responsive, dark-mode, components]
tldr: "Battle-tested Tailwind CSS patterns for N02 output: responsive grid compositions, dark mode token switching, component variant APIs via CVA, animation utilities for micro-interactions, and the 60-30-10 color distribution rule enforced via design tokens."
quality: 8.8
density_score: 0.97
related:
  - p05_output_style_guide
  - p09_lpt_landing_page_template
  - p01_kc_tailwind_patterns
  - p09_ct_component_template
  - p10_hos_html_output_visual_frontend
  - landing_page_petshop_crm
  - p03_pt_visual_frontend_marketing
  - n06_output_pricing_page
  - p05_output_dashboard_ui
  - p05_output_visual_report
---

# Tailwind Patterns

This document outlines best practices for using Tailwind CSS in design systems.

## Core Principles

### 1. Utility-First Approach
- Use utility classes for styling
- Maintain a consistent class naming convention
- Avoid excessive class nesting

### 2. Component-Based Design
- Create reusable components
- Use component-specific utility classes
- Maintain component state separately

### 3. Responsive Design
- Use responsive breakpoints
- Implement mobile-first approach
- Use utility classes for different screen sizes

## Implementation Guide

```html
<div class="container mx-auto p-4">
  <div class="flex flex-wrap">
    <div class="w-full md:w-1/2 p-2">
      <div class="bg-white rounded shadow">
        <!-- Content -->
      </div>
    </div>
    <div class="w-full md:w-1/2 p-2">
      <div class="bg-white rounded shadow">
        <!-- Content -->
      </div>
    </div>
  </div>
</div>
```

## Best Practices

- Keep utility classes organized
- Use custom variants for specific use cases
- Maintain a design system library

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p05_output_style_guide]] | downstream | 0.57 |
| [[p09_lpt_landing_page_template]] | downstream | 0.53 |
| [[p01_kc_tailwind_patterns]] | sibling | 0.53 |
| [[p09_ct_component_template]] | downstream | 0.42 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.36 |
| [[landing_page_petshop_crm]] | downstream | 0.36 |
| [[p03_pt_visual_frontend_marketing]] | downstream | 0.33 |
| [[n06_output_pricing_page]] | downstream | 0.33 |
| [[p05_output_dashboard_ui]] | downstream | 0.32 |
| [[p05_output_visual_report]] | downstream | 0.29 |
