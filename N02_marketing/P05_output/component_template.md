---
id: p09_ct_component_template
kind: output_validator
pillar: P09
title: Component Template — shadcn/ui Style Patterns
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend_marketing
template_type: component
output_format: html_component_with_variants
component_patterns: [button, card, form, input, dialog, dropdown, navigation, table]
styling_approach: utility_first_tailwind
variant_system: compound_variants
accessibility: wcag_aa_radix_primitives
performance: lighthouse_90_plus
reusability: high
domain: visual_frontend_engineering
quality: 9.1
tags: [output_template, component, shadcn_ui, tailwind, radix, accessibility, variants, N02]
tldr: Reusable component template following shadcn/ui patterns — variant system, accessibility built-in, Tailwind utility classes, production ready.
density_score: 0.96
related:
  - p09_lpt_landing_page_template
  - p10_hos_html_output_visual_frontend
  - p05_output_style_guide
  - p03_pt_visual_frontend_marketing
  - kc_tailwind_patterns
  - p01_kc_tailwind_patterns
  - landing_page_petshop_crm
  - n06_output_pricing_page
  - bld_examples_landing_page
  - p05_output_dashboard_ui
---

# Component Template — shadcn/ui Style Patterns

## Purpose

Template for generating reusable, accessible components following shadcn/ui design patterns. Each component includes multiple variants, built-in accessibility, and consistent styling via design tokens.

## Base Component Template

### Universal Component Structure

```html
---
component: {component_name}
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
component_type: {button|card|form|input|dialog|dropdown|navigation|table}
variants: {variant_count}
---

<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{Component Name} - Component Library</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              border: '#e5e7eb',
              input: '#e5e7eb',
              ring: '#50C878',
              background: '#ffffff',
              foreground: '#111827',
              primary: {
                DEFAULT: '#50C878',
                foreground: '#ffffff',
              },
              secondary: {
                DEFAULT: '#f3f4f6',
                foreground: '#111827',
              },
              destructive: {
                DEFAULT: '#ef4444',
                foreground: '#ffffff',
              },
              muted: {
                DEFAULT: '#f3f4f6',
                foreground: '#6b7280',
              },
              accent: {
                DEFAULT: '#f3f4f6',
                foreground: '#111827',
              },
              popover: {
                DEFAULT: '#ffffff',
                foreground: '#111827',
              },
              card: {
                DEFAULT: '#ffffff',
                foreground: '#111827',
              },
            },
            borderRadius: {
              lg: '0.5rem',
              md: '0.375rem',
              sm: '0.125rem',
            },
          }
        },
        darkMode: 'class',
      }
    </script>
  </head>
  
  <body class="min-h-screen bg-background p-8">
    
    <!-- Component Showcase -->
    <div class="max-w-4xl mx-auto space-y-8">
      
      <!-- Header -->
      <div class="space-y-2">
        <h1 class="text-3xl font-bold text-foreground">{Component Name}</h1>
        <p class="text-muted-foreground">{component_description}</p>
      </div>
      
      <!-- Variants Showcase -->
      <div class="grid gap-8">
        {component_variants}
      </div>
      
      <!-- Usage Examples -->
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-foreground">Usage Examples</h2>
        <div class="grid gap-4 md:grid-cols-2">
          {usage_examples}
        </div>
      </div>
      
      <!-- Accessibility Features -->
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-foreground">Accessibility Features</h2>
        <div class="bg-muted rounded-lg p-4">
          <ul class="space-y-2 text-sm text-muted-foreground">
            {accessibility_features}
          </ul>
        </div>
      </div>
      
    </div>
    
  </body>
</html>
```

## Component Pattern Examples

### Button Component Template

```html
---
component: button_component
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
component_type: button
variants: 6
---

<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Button Component - CODEXA Design System</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              primary: { DEFAULT: '#50C878', foreground: '#ffffff' },
              secondary: { DEFAULT: '#f3f4f6', foreground: '#111827' },
              destructive: { DEFAULT: '#ef4444', foreground: '#ffffff' },
              outline: { DEFAULT: 'transparent', foreground: '#111827' },
              ghost: { DEFAULT: 'transparent', foreground: '#111827' },
              link: { DEFAULT: 'transparent', foreground: '#50C878' },
              border: '#e5e7eb',
              ring: '#50C878',
            }
          }
        },
        darkMode: 'class',
      }
    </script>
  </head>
  
  <body class="min-h-screen bg-white p-8">
    
    <div class="max-w-4xl mx-auto space-y-8">
      
      <!-- Header -->
      <div class="space-y-2">
        <h1 class="text-3xl font-bold text-gray-900">Button Component</h1>
        <p class="text-gray-600">Accessible button component with multiple variants and sizes.</p>
      </div>
      
      <!-- Button Variants -->
      <div class="space-y-6">
        
        <!-- Default Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Default (Primary)</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-9 px-3 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Small
            </button>
            <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Default
            </button>
            <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-11 px-8 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Large
            </button>
          </div>
        </div>
        
        <!-- Secondary Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Secondary</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="bg-secondary text-secondary-foreground hover:bg-secondary/80 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-9 px-3 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Small
            </button>
            <button class="bg-secondary text-secondary-foreground hover:bg-secondary/80 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Default
            </button>
            <button class="bg-secondary text-secondary-foreground hover:bg-secondary/80 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-11 px-8 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Large
            </button>
          </div>
        </div>
        
        <!-- Destructive Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Destructive</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="bg-destructive text-destructive-foreground hover:bg-destructive/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Delete Account
            </button>
            <button class="bg-destructive text-destructive-foreground hover:bg-destructive/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none" disabled>
              Disabled
            </button>
          </div>
        </div>
        
        <!-- Outline Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Outline</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="border border-input bg-background hover:bg-accent hover:text-accent-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Outline Button
            </button>
          </div>
        </div>
        
        <!-- Ghost Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Ghost</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="hover:bg-accent hover:text-accent-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Ghost Button
            </button>
          </div>
        </div>
        
        <!-- Link Variant -->
        <div class="space-y-3">
          <h3 class="text-lg font-medium text-gray-900">Link</h3>
          <div class="flex items-center gap-4 flex-wrap">
            <button class="text-primary underline-offset-4 hover:underline focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 text-sm font-medium transition-colors disabled:opacity-50 disabled:pointer-events-none">
              Link Button
            </button>
          </div>
        </div>
      </div>
      
    </div>
    
  </body>
</html>
```

## Anti-Patterns

### What NOT to Do

| ❌ Anti-Pattern | ✅ Correct Approach | Why |
|----------------|-------------------|-----|
| `<div onclick="">` buttons | `<button type="button">` | Screen readers need semantic button elements |
| Custom CSS animations | `transition-colors` utility | Hardware acceleration + consistency |
| Fixed pixel heights `h-[32px]` | Relative heights `h-10` | Better scaling across screen sizes |
| Hardcoded colors `bg-blue-500` | Design tokens `bg-primary` | Brand consistency + dark mode support |
| Missing focus styles | `focus:ring-2` classes | Keyboard accessibility requirement |
| Single size components | Multiple size variants | Different contexts need different scales |
| Inline styles `style=""` | Utility classes | Better performance + maintainability |
| Generic onClick handlers | Specific semantic actions | Better UX + screen reader context |

### Implementation Mistakes

- **Missing aria-labels on icon-only buttons** → Always provide accessible text
- **Using divs for interactive elements** → Use semantic HTML (button, input, select)
- **Skipping disabled states** → Every interactive component needs disabled styling
- **Ignoring touch targets** → Minimum 44px height for mobile accessibility
- **Breaking keyboard navigation** → Test Tab, Enter, Space, Arrow keys
- **Hardcoding brand colors** → Use design tokens for theme consistency

## Accessibility Standards

### Universal A11y Requirements

Every component must include:

```html
<!-- 1. Proper semantic markup -->
<button type="button" role="button">Click me</button>

<!-- 2. Focus management -->
<button class="focus:ring-2 focus:ring-ring focus:ring-offset-2">Focusable</button>

<!-- 3. ARIA labels when needed -->
<button aria-label="Close dialog">×</button>

<!-- 4. Form associations -->
<label for="username">Username</label>
<input id="username" aria-describedby="username-help">
<div id="username-help">Enter your username</div>

<!-- 5. Error announcements -->
<div role="alert" aria-live="polite">
  Error message here
</div>

<!-- 6. Touch targets (44px minimum) -->
<button class="h-11 px-4">Touch-friendly</button>

<!-- 7. Color contrast compliance -->
<!-- All text must have 4.5:1 contrast ratio minimum -->
```

## Performance Optimization

### Optimized Component Loading

```html
<!-- Minimal DOM for fast rendering -->
<button class="btn-primary">
  <!-- Simple structure -->
</button>

<!-- CSS-only animations -->
<button class="transition-colors hover:bg-primary/90">
  <!-- Hardware-accelerated transitions -->
</button>

<!-- Efficient class composition -->
<div class="flex items-center space-x-2">
  <!-- Utility classes for minimal CSS -->
</div>
```

### Component Integration

```bash
# Validation pipeline for components
lighthouse component.html --only=performance,accessibility
w3c-validator component.html
npm run test:component

# Integration with CEX system
python _tools/cex_compile.py component.md
python _tools/cex_doctor.py --component
```

This template ensures every component generated by N02 is production-ready, accessible, and follows modern design system patterns.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_lpt_landing_page_template]] | sibling | 0.66 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.58 |
| [[p05_output_style_guide]] | sibling | 0.52 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.51 |
| [[kc_tailwind_patterns]] | upstream | 0.45 |
| [[p01_kc_tailwind_patterns]] | upstream | 0.39 |
| [[landing_page_petshop_crm]] | upstream | 0.37 |
| [[n06_output_pricing_page]] | upstream | 0.36 |
| [[bld_examples_landing_page]] | upstream | 0.35 |
| [[p05_output_dashboard_ui]] | sibling | 0.35 |
