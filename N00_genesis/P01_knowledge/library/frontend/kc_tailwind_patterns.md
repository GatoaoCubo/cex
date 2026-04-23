---
id: p01_kc_tailwind_patterns
kind: knowledge_card
pillar: P01
title: "Tailwind CSS Patterns & Configuration"
version: 1.0.0
created: 2026-04-01
author: builder
domain: frontend
quality: 9.0
tags: [knowledge, frontend, tailwind, css, utility-first]
tldr: "Tailwind utility-first patterns, JIT mode, responsive design, and configuration strategies"
density_score: 0.88
related:
  - kc_tailwind_patterns
  - p10_hos_html_output_visual_frontend
  - p09_lpt_landing_page_template
  - p05_output_style_guide
  - landing_page_petshop_crm
  - p09_ct_component_template
  - p05_output_visual_report
  - bld_examples_landing_page
  - p03_pt_visual_frontend_marketing
  - p05_output_dashboard_ui
---

# Tailwind CSS Patterns & Configuration

## Utility-First Philosophy

**Core Principle**: Compose styles from single-purpose utility classes rather than writing custom CSS.

```html
<!-- Traditional CSS approach -->
<div class="card">
  <h2 class="card-title">Title</h2>
</div>

<!-- Utility-first approach -->
<div class="bg-white rounded-lg shadow-md p-6">
  <h2 class="text-xl font-bold text-gray-900">Title</h2>
</div>
```

**Benefits**: Faster development, consistent spacing, no CSS bloat, easier maintenance.

## Configuration Patterns

### tailwind.config.js Extend Strategy

```js
module.exports = {
  content: ['./src/**/*.{js,ts,jsx,tsx,html}'],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f0f9ff',
          500: '#3b82f6',
          900: '#1e3a8a'
        },
        accent: '#50C878'
      },
      spacing: {
        '18': '4.5rem',
        '88': '22rem'
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['Fira Code', 'monospace']
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography')
  ]
}
```

### JIT Mode & Arbitrary Values

```html
<!-- Arbitrary values with JIT -->
<div class="bg-[#50C878] w-[350px] top-[117px]">
  <p class="text-[14px] leading-[1.2]">Custom sizing</p>
</div>
```

## Responsive Design Patterns

### Mobile-First Breakpoints

```html
<!-- sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px -->
<div class="w-full md:w-1/2 lg:w-1/3 xl:w-1/4">
  <img class="object-cover h-48 md:h-64 lg:h-48" src="image.jpg" alt="">
</div>
```

### Dark Mode Variant

```html
<div class="bg-white dark:bg-gray-900">
  <h1 class="text-gray-900 dark:text-white">
    Adapts to system preference
  </h1>
</div>
```

## Component Extraction with @apply

```css
/* When you need to extract repeated patterns */
.btn-primary {
  @apply px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2;
}

.card {
  @apply bg-white rounded-lg shadow-md p-6 border border-gray-200;
}
```

## Plugin System

### Custom Plugin Example

```js
const plugin = require('tailwindcss/plugin')

module.exports = {
  plugins: [
    plugin(function({ addUtilities }) {
      addUtilities({
        '.writing-vertical': {
          'writing-mode': 'vertical-lr'
        },
        '.text-shadow': {
          'text-shadow': '0 2px 4px rgba(0,0,0,0.1)'
        }
      })
    })
  ]
}
```

## Performance Optimization

### Content Configuration

```js
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx}',
    './components/**/*.{js,ts,jsx,tsx}',
    './app/**/*.{js,ts,jsx,tsx}'
  ],
  // Safelist classes that are generated dynamically
  safelist: [
    'text-red-500',
    'bg-green-500',
    {
      pattern: /bg-(red|green|blue)-(100|200|300)/,
      variants: ['hover', 'focus']
    }
  ]
}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_tailwind_patterns]] | sibling | 0.52 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.50 |
| [[p09_lpt_landing_page_template]] | downstream | 0.50 |
| [[p05_output_style_guide]] | downstream | 0.49 |
| [[landing_page_petshop_crm]] | downstream | 0.47 |
| [[p09_ct_component_template]] | downstream | 0.47 |
| [[p05_output_visual_report]] | downstream | 0.42 |
| [[bld_examples_landing_page]] | related | 0.40 |
| [[p03_pt_visual_frontend_marketing]] | downstream | 0.37 |
| [[p05_output_dashboard_ui]] | downstream | 0.35 |
