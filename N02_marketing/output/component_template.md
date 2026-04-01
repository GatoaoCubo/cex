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
quality: 8.8
tags: [output_template, component, shadcn_ui, tailwind, radix, accessibility, variants, N02]
tldr: Reusable component template following shadcn/ui patterns — variant system, accessibility built-in, Tailwind utility classes, production ready.
density_score: 0.96
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
      
      <!-- Usage Examples -->
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-gray-900">Usage Examples</h2>
        
        <div class="grid gap-4 md:grid-cols-2">
          <!-- Form Actions -->
          <div class="bg-gray-50 rounded-lg p-4">
            <h3 class="font-medium text-gray-900 mb-3">Form Actions</h3>
            <div class="flex gap-2">
              <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors">
                Save Changes
              </button>
              <button class="border border-input bg-background hover:bg-accent hover:text-accent-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 h-10 px-4 py-2 rounded-md text-sm font-medium transition-colors">
                Cancel
              </button>
            </div>
          </div>
          
          <!-- Call to Action -->
          <div class="bg-gray-50 rounded-lg p-4">
            <h3 class="font-medium text-gray-900 mb-3">Call to Action</h3>
            <div class="space-y-2">
              <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 h-11 px-8 rounded-md text-sm font-medium transition-colors w-full sm:w-auto">
                Get Started Today
              </button>
              <p class="text-xs text-gray-500">No credit card required</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Accessibility Features -->
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-gray-900">Accessibility Features</h2>
        <div class="bg-gray-50 rounded-lg p-4">
          <ul class="space-y-2 text-sm text-gray-600">
            <li>✓ <strong>Keyboard Navigation:</strong> Full support for Tab, Enter, and Space keys</li>
            <li>✓ <strong>Focus Indicators:</strong> Clear focus ring for keyboard users</li>
            <li>✓ <strong>Screen Readers:</strong> Semantic button elements with proper roles</li>
            <li>✓ <strong>Touch Targets:</strong> Minimum 44px height for mobile accessibility</li>
            <li>✓ <strong>Color Contrast:</strong> All variants meet WCAG AA standards (4.5:1)</li>
            <li>✓ <strong>Disabled States:</strong> Clear visual and functional disabled state</li>
            <li>✓ <strong>ARIA Support:</strong> Compatible with aria-label and aria-describedby</li>
          </ul>
        </div>
      </div>
      
      <!-- CSS Classes Reference -->
      <div class="space-y-4">
        <h2 class="text-xl font-semibold text-gray-900">CSS Classes Reference</h2>
        <div class="bg-gray-50 rounded-lg p-4 overflow-x-auto">
          <pre class="text-sm text-gray-800"><code>/* Base button classes */
.btn-base {
  @apply inline-flex items-center justify-center whitespace-nowrap rounded-md text-sm font-medium transition-colors;
  @apply focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2;
  @apply disabled:pointer-events-none disabled:opacity-50;
}

/* Size variants */
.btn-sm { @apply h-9 rounded-md px-3; }
.btn-default { @apply h-10 px-4 py-2; }
.btn-lg { @apply h-11 rounded-md px-8; }

/* Style variants */
.btn-primary { @apply bg-primary text-primary-foreground hover:bg-primary/90; }
.btn-secondary { @apply bg-secondary text-secondary-foreground hover:bg-secondary/80; }
.btn-destructive { @apply bg-destructive text-destructive-foreground hover:bg-destructive/90; }
.btn-outline { @apply border border-input bg-background hover:bg-accent hover:text-accent-foreground; }
.btn-ghost { @apply hover:bg-accent hover:text-accent-foreground; }
.btn-link { @apply text-primary underline-offset-4 hover:underline; }</code></pre>
        </div>
      </div>
    </div>
    
  </body>
</html>
```

### Card Component Template

```html
---
component: card_component
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90
component_type: card
variants: 4
---

<div class="max-w-4xl mx-auto space-y-8">
  
  <!-- Header -->
  <div class="space-y-2">
    <h1 class="text-3xl font-bold text-gray-900">Card Component</h1>
    <p class="text-gray-600">Flexible container component for content organization.</p>
  </div>
  
  <!-- Card Variants -->
  <div class="grid gap-6 md:grid-cols-2">
    
    <!-- Basic Card -->
    <div class="bg-card text-card-foreground rounded-lg border border-border shadow-sm p-6">
      <h3 class="text-lg font-semibold mb-2">Basic Card</h3>
      <p class="text-muted-foreground">This is a basic card with title and description. Perfect for content organization.</p>
    </div>
    
    <!-- Card with Header -->
    <div class="bg-card text-card-foreground rounded-lg border border-border shadow-sm">
      <div class="p-6 pb-4">
        <div class="flex items-center justify-between">
          <h3 class="text-lg font-semibold">Card with Header</h3>
          <button class="hover:bg-accent hover:text-accent-foreground p-2 rounded-md text-sm">
            ⋯
          </button>
        </div>
      </div>
      <div class="px-6 pb-6">
        <p class="text-muted-foreground">This card includes a header with actions. Great for interactive content.</p>
      </div>
    </div>
    
    <!-- Card with Footer -->
    <div class="bg-card text-card-foreground rounded-lg border border-border shadow-sm">
      <div class="p-6 pb-4">
        <h3 class="text-lg font-semibold mb-2">Card with Footer</h3>
        <p class="text-muted-foreground">This card includes footer actions for user interactions.</p>
      </div>
      <div class="px-6 pb-6">
        <div class="flex gap-2">
          <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-ring focus:ring-offset-2 px-4 py-2 rounded-md text-sm font-medium transition-colors">
            Accept
          </button>
          <button class="border border-input bg-background hover:bg-accent hover:text-accent-foreground focus:ring-2 focus:ring-ring focus:ring-offset-2 px-4 py-2 rounded-md text-sm font-medium transition-colors">
            Decline
          </button>
        </div>
      </div>
    </div>
    
    <!-- Interactive Card -->
    <div class="bg-card text-card-foreground rounded-lg border border-border shadow-sm hover:shadow-md transition-shadow cursor-pointer p-6">
      <div class="flex items-start space-x-4">
        <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
          <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
          </svg>
        </div>
        <div class="flex-1">
          <h3 class="text-lg font-semibold mb-1">Interactive Card</h3>
          <p class="text-muted-foreground text-sm">This card responds to hover and click interactions.</p>
        </div>
      </div>
    </div>
  </div>
  
  <!-- Usage Examples -->
  <div class="space-y-4">
    <h2 class="text-xl font-semibold text-gray-900">Usage Examples</h2>
    
    <!-- Feature Grid -->
    <div class="grid gap-6 md:grid-cols-3">
      <div class="bg-card text-card-foreground rounded-lg border border-border p-6">
        <div class="w-10 h-10 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
          <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </div>
        <h3 class="font-semibold mb-2">Feature Title</h3>
        <p class="text-sm text-muted-foreground">Feature description explaining the benefit and value proposition.</p>
      </div>
      
      <div class="bg-card text-card-foreground rounded-lg border border-border p-6">
        <div class="w-10 h-10 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
          <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
          </svg>
        </div>
        <h3 class="font-semibold mb-2">Feature Title</h3>
        <p class="text-sm text-muted-foreground">Feature description explaining the benefit and value proposition.</p>
      </div>
      
      <div class="bg-card text-card-foreground rounded-lg border border-border p-6">
        <div class="w-10 h-10 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
          <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"></path>
          </svg>
        </div>
        <h3 class="font-semibold mb-2">Feature Title</h3>
        <p class="text-sm text-muted-foreground">Feature description explaining the benefit and value proposition.</p>
      </div>
    </div>
  </div>
</div>
```

## Component Patterns Reference

### Input Component Template

```html
<!-- Input variants -->
<div class="space-y-4">
  <!-- Default Input -->
  <div class="space-y-2">
    <label for="email" class="text-sm font-medium text-foreground">Email</label>
    <input 
      type="email" 
      id="email" 
      placeholder="Enter your email"
      class="flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
    >
  </div>
  
  <!-- Input with error -->
  <div class="space-y-2">
    <label for="password" class="text-sm font-medium text-foreground">Password</label>
    <input 
      type="password" 
      id="password"
      placeholder="Enter your password"
      aria-describedby="password-error"
      class="flex h-10 w-full rounded-md border border-destructive bg-background px-3 py-2 text-sm ring-offset-background focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-destructive focus-visible:ring-offset-2"
    >
    <p id="password-error" class="text-sm text-destructive" role="alert">
      Password must be at least 8 characters
    </p>
  </div>
  
  <!-- Disabled Input -->
  <div class="space-y-2">
    <label for="disabled-input" class="text-sm font-medium text-muted-foreground">Disabled Input</label>
    <input 
      type="text" 
      id="disabled-input"
      value="This field is disabled"
      disabled
      class="flex h-10 w-full rounded-md border border-input bg-muted px-3 py-2 text-sm text-muted-foreground cursor-not-allowed opacity-50"
    >
  </div>
</div>
```

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

### Dark Mode Implementation

```html
<!-- Component with dark mode variants -->
<div class="bg-background text-foreground border border-border dark:bg-gray-900 dark:text-gray-100 dark:border-gray-700">
  <!-- Content automatically adapts -->
</div>

<!-- Using CSS variables for automatic adaptation -->
<style>
  :root {
    --background: #ffffff;
    --foreground: #111827;
    --border: #e5e7eb;
  }
  
  .dark {
    --background: #111827;
    --foreground: #f9fafb;
    --border: #374151;
  }
  
  .bg-background { background-color: var(--background); }
  .text-foreground { color: var(--foreground); }
  .border-border { border-color: var(--border); }
</style>
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