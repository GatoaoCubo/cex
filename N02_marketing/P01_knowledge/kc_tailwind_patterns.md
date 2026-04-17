---
id: kc_tailwind_patterns
kind: knowledge_card
pillar: P01
title: Tailwind Patterns
tags: [tailwind, patterns, design]
quality: 8.8
density_score: 0.97
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
