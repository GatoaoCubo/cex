---
id: p10_dtc_design_token_contract
kind: input_schema
pillar: P10
title: Design Token Contract — 3-Layer Architecture
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend_marketing
target_artifact: design_system
token_layers: [primitives, semantic_codexa, component_level]
color_palette: codexa_green_accent
font_stack: [geist_variable, inter, jetbrains_mono]
validation_rules: [zero_hardcoded_hex, consistent_spacing, proper_hierarchy]
domain: visual_frontend_engineering
quality: 9.1
tags: [input_schema, design_tokens, codexa, visual-system, color, typography, spacing, N02]
tldr: 3-layer design token contract — primitives (:root), semantic (CODEXA), component — zero hardcoded hex colors, consistent spacing, #50C878 accent.
density_score: 0.96
---

# Design Token Contract — 3-Layer Architecture

## Purpose

Defines the mandatory 3-layer design token architecture for all N02 visual output.
Ensures consistent styling, maintainable code, and zero hardcoded values across components and pages.

## 3-Layer Token Architecture

### Layer 1: Primitives (:root level)

Base tokens that define the foundation. Never reference these directly in components.

```css
:root {
  /* Color Primitives */
  --white: #ffffff;
  --black: #000000;
  --gray-50: #f9fafb;
  --gray-100: #f3f4f6;
  --gray-200: #e5e7eb;
  --gray-300: #d1d5db;
  --gray-400: #9ca3af;
  --gray-500: #6b7280;
  --gray-600: #4b5563;
  --gray-700: #374151;
  --gray-800: #1f2937;
  --gray-900: #111827;
  --gray-950: #030712;
  
  /* CODEXA Brand Primitives */
  --codexa-green-50: #f0fdf4;
  --codexa-green-100: #dcfce7;
  --codexa-green-200: #bbf7d0;
  --codexa-green-300: #86efac;
  --codexa-green-400: #4ade80;
  --codexa-green-500: #50C878; /* Primary accent */
  --codexa-green-600: #16a34a;
  --codexa-green-700: #15803d;
  --codexa-green-800: #166534;
  --codexa-green-900: #14532d;
  
  /* Spacing Primitives */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  --space-12: 3rem;    /* 48px */
  --space-16: 4rem;    /* 64px */
  --space-20: 5rem;    /* 80px */
  --space-24: 6rem;    /* 96px */
  
  /* Typography Primitives */
  --font-size-xs: 0.75rem;   /* 12px */
  --font-size-sm: 0.875rem;  /* 14px */
  --font-size-base: 1rem;    /* 16px */
  --font-size-lg: 1.125rem;  /* 18px */
  --font-size-xl: 1.25rem;   /* 20px */
  --font-size-2xl: 1.5rem;   /* 24px */
  --font-size-3xl: 1.875rem; /* 30px */
  --font-size-4xl: 2.25rem;  /* 36px */
  --font-size-5xl: 3rem;     /* 48px */
  --font-size-6xl: 3.75rem;  /* 60px */
  
  /* Border Radius Primitives */
  --radius-sm: 0.125rem;  /* 2px */
  --radius: 0.25rem;      /* 4px */
  --radius-md: 0.375rem;  /* 6px */
  --radius-lg: 0.5rem;    /* 8px */
  --radius-xl: 0.75rem;   /* 12px */
  --radius-2xl: 1rem;     /* 16px */
  --radius-full: 9999px;
}
```

### Layer 2: Semantic CODEXA Tokens

Business-meaningful tokens that reference primitives. Reference these in components.

```css
.codexa-theme {
  /* Surface Colors */
  --codexa-surface-50: var(--gray-50);
  --codexa-surface-100: var(--gray-100);
  --codexa-surface-200: var(--gray-200);
  --codexa-surface-500: var(--gray-500);
  --codexa-surface-800: var(--gray-800);
  --codexa-surface-900: var(--gray-900);
  
  /* Text Hierarchy */
  --codexa-text-primary: var(--gray-900);
  --codexa-text-secondary: var(--gray-600);
  --codexa-text-tertiary: var(--gray-500);
  --codexa-text-inverse: var(--white);
  
  /* Interactive Elements */
  --codexa-accent: var(--codexa-green-500);      /* #50C878 */
  --codexa-accent-hover: var(--codexa-green-600);
  --codexa-accent-active: var(--codexa-green-700);
  --codexa-accent-subtle: var(--codexa-green-50);
  
  /* Border & Outline */
  --codexa-border-default: var(--gray-200);
  --codexa-border-subtle: var(--gray-100);
  --codexa-border-emphasis: var(--gray-300);
  
  /* Status Colors */
  --codexa-success: var(--codexa-green-500);
  --codexa-success-bg: var(--codexa-green-50);
  --codexa-warning: #f59e0b;
  --codexa-warning-bg: #fef3c7;
  --codexa-error: #ef4444;
  --codexa-error-bg: #fef2f2;
}

/* Dark Mode Semantic Overrides */
.dark .codexa-theme {
  --codexa-surface-50: var(--gray-950);
  --codexa-surface-100: var(--gray-900);
  --codexa-surface-200: var(--gray-800);
  --codexa-surface-500: var(--gray-400);
  --codexa-surface-800: var(--gray-200);
  --codexa-surface-900: var(--gray-100);
  
  --codexa-text-primary: var(--gray-100);
  --codexa-text-secondary: var(--gray-400);
  --codexa-text-tertiary: var(--gray-500);
  --codexa-text-inverse: var(--gray-900);
  
  --codexa-border-default: var(--gray-700);
  --codexa-border-subtle: var(--gray-800);
  --codexa-border-emphasis: var(--gray-600);
}
```

### Layer 3: Component-Level Tokens

Component-specific tokens that reference semantic layer. Use for reusable patterns.

```css
/* Button Component Tokens */
.button-tokens {
  --button-primary-bg: var(--codexa-accent);
  --button-primary-text: var(--white);
  --button-primary-hover: var(--codexa-accent-hover);
  --button-primary-active: var(--codexa-accent-active);
  
  --button-secondary-bg: var(--codexa-surface-100);
  --button-secondary-text: var(--codexa-text-primary);
  --button-secondary-hover: var(--codexa-surface-200);
  
  --button-padding-sm: var(--space-2) var(--space-3);
  --button-padding-md: var(--space-3) var(--space-4);
  --button-padding-lg: var(--space-4) var(--space-6);
  
  --button-radius: var(--radius);
}

/* Card Component Tokens */
.card-tokens {
  --card-bg: var(--white);
  --card-border: var(--codexa-border-default);
  --card-text: var(--codexa-text-primary);
  --card-text-muted: var(--codexa-text-secondary);
  --card-padding: var(--space-6);
  --card-radius: var(--radius-lg);
  --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.dark .card-tokens {
  --card-bg: var(--gray-900);
  --card-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
}

/* Form Component Tokens */
.form-tokens {
  --form-input-bg: var(--white);
  --form-input-border: var(--codexa-border-default);
  --form-input-border-focus: var(--codexa-accent);
  --form-input-text: var(--codexa-text-primary);
  --form-input-placeholder: var(--codexa-text-tertiary);
  --form-input-radius: var(--radius);
  --form-input-padding: var(--space-3);
  
  --form-label-text: var(--codexa-text-secondary);
  --form-label-size: var(--font-size-sm);
  --form-label-weight: 500;
}

/* Navigation Component Tokens */
.nav-tokens {
  --nav-bg: var(--white);
  --nav-border: var(--codexa-border-subtle);
  --nav-text: var(--codexa-text-primary);
  --nav-text-hover: var(--codexa-accent);
  --nav-text-active: var(--codexa-accent);
  --nav-padding: var(--space-4) var(--space-6);
}
```

## Tailwind CSS Integration

### Custom Tailwind Config

```javascript
// tailwind.config.js
module.exports = {
  theme: {
    extend: {
      colors: {
        // Map to semantic tokens
        background: 'var(--codexa-surface-50)',
        foreground: 'var(--codexa-text-primary)',
        
        primary: {
          DEFAULT: 'var(--codexa-accent)',
          foreground: 'var(--white)',
          hover: 'var(--codexa-accent-hover)',
        },
        
        secondary: {
          DEFAULT: 'var(--codexa-surface-200)',
          foreground: 'var(--codexa-text-primary)',
        },
        
        muted: {
          DEFAULT: 'var(--codexa-surface-100)',
          foreground: 'var(--codexa-text-secondary)',
        },
        
        accent: {
          DEFAULT: 'var(--codexa-accent)',
          foreground: 'var(--white)',
        },
        
        border: 'var(--codexa-border-default)',
        ring: 'var(--codexa-accent)',
      },
      
      fontFamily: {
        sans: ['Geist Variable', 'Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'Monaco', 'Consolas', 'monospace'],
      },
      
      spacing: {
        // Map to spacing primitives
        '18': 'var(--space-18)', // 4.5rem / 72px
        '88': 'var(--space-88)', // 22rem / 352px
      },
      
      borderRadius: {
        // Map to radius primitives
        'lg': 'var(--radius-lg)',
        'xl': 'var(--radius-xl)',
      }
    }
  },
  
  darkMode: 'class', // Enable dark mode via .dark class
}
```

### Usage in HTML

```html
<!-- CORRECT: Using Tailwind classes that map to tokens -->
<div class="bg-background text-foreground border border-border rounded-lg p-6">
  <h2 class="text-lg font-medium text-foreground">Card Title</h2>
  <p class="text-muted-foreground mt-2">Card description content</p>
  
  <button class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2 mt-4 px-4 py-2 rounded-md">
    Action Button
  </button>
</div>

<!-- INCORRECT: Hardcoded values -->
<div style="background: #ffffff; color: #111827; border: 1px solid #e5e7eb;">
  <!-- This breaks the design system -->
</div>

<!-- INCORRECT: No dark mode consideration -->
<div class="bg-white text-gray-900">
  <!-- Missing dark: variants -->
</div>
```

## Font Stack Implementation

### 3-Font System

```css
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap');

.font-tokens {
  /* Headings: Geist Variable */
  --font-heading: 'Geist Variable', 'Inter', system-ui, sans-serif;
  
  /* Body text: Inter */
  --font-body: 'Inter', system-ui, sans-serif;
  
  /* Code/monospace: JetBrains Mono */
  --font-mono: 'JetBrains Mono', 'Monaco', 'Consolas', monospace;
  
  /* Font weights */
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
}
```

### Typography Scale Usage

```html
<!-- Heading hierarchy with proper font usage -->
<h1 class="font-sans text-4xl font-bold tracking-tight">
  Main headline (Geist Variable via font-sans)
</h1>

<h2 class="font-sans text-2xl font-semibold">
  Section heading
</h2>

<p class="font-sans text-base text-muted-foreground">
  Body paragraph text (Inter via font-sans)
</p>

<code class="font-mono text-sm bg-muted px-2 py-1 rounded">
  Code snippet (JetBrains Mono)
</code>
```

## Validation Rules

### Mandatory Checks

| Rule | Description | Validation |
|------|-------------|------------|
| **Zero hardcoded hex** | No #HEXCODE values in code | Automated scan for # colors |
| **Token reference only** | Only use defined token names | Verify against token list |
| **Dark mode coverage** | Every color has dark variant | Visual dark mode test |
| **Contrast compliance** | All combinations >= 4.5:1 | Contrast ratio calculator |
| **Spacing consistency** | Use spacing scale only | Check against space-* classes |
| **Font stack adherence** | Only use 3 approved fonts | Font family audit |

### Common Violations

```html
<!-- VIOLATIONS -->
❌ style="color: #50C878"              <!-- Hardcoded hex -->
❌ class="bg-green-500"                <!-- Direct color class -->
❌ style="padding: 15px"               <!-- Off-scale spacing -->
❌ style="font-family: Arial"          <!-- Non-approved font -->
❌ class="text-green-500"              <!-- No dark mode variant -->

<!-- CORRECT USAGE -->
✅ class="text-primary"                <!-- Semantic token -->
✅ class="bg-accent hover:bg-accent/90" <!-- Token + interaction -->
✅ class="p-4"                         <!-- Scale-compliant spacing -->
✅ class="font-sans"                   <!-- Approved font stack -->
✅ class="text-primary dark:text-primary-dark" <!-- Dark mode ready -->
```

## Component Example: Button with Token Usage

```html
<!-- Button component using all 3 token layers -->
<button class="
  // Layer 3: Component tokens via Tailwind classes
  bg-primary text-primary-foreground 
  hover:bg-primary/90 
  focus:ring-2 focus:ring-primary focus:ring-offset-2
  
  // Layer 2: Semantic spacing and typography
  px-4 py-2 
  text-sm font-medium
  
  // Layer 1: Primitive radius
  rounded-md
  
  // Interaction states
  transition-colors
  disabled:opacity-50 disabled:cursor-not-allowed
  
  // Dark mode (automatic via token system)
  dark:ring-offset-background
">
  Button Text
</button>
```

This button automatically adapts to:
- Light/dark themes (via token system)
- Brand color changes (modify --codexa-accent)
- Spacing scale updates (modify space tokens)
- Typography changes (modify font tokens)

## Integration with CEX Quality Gates

N02 output validation includes token compliance:

```bash
# Automated token validation
python _tools/validate_tokens.py component.html
# Checks: hardcoded colors, off-scale spacing, unapproved fonts

# Visual validation
lighthouse component.html --only=accessibility
# Checks: contrast ratios, color combinations

# Design system audit
python _tools/design_system_audit.py N02_marketing/
# Checks: token usage consistency across all components
```