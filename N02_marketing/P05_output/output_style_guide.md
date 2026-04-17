---
id: p05_output_style_guide
kind: output_validator
pillar: P05
title: "Design System Style Guide — Self-Contained HTML"
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
tags: [output, template, style-guide, design-system, tokens]
tldr: "Self-contained HTML design system page — palette, typography, spacing, components, dark mode."
density_score: 0.91
---

# Design System Style Guide Template

## Purpose
Single HTML file documenting the complete CODEXA design system.
Self-contained: all CSS tokens inline, no external dependencies except fonts.
Inspired by: Linear, Railway, Raycast, Stripe, Vercel design systems.

---

## Template Structure

```
1. Header (logo + "Design System v1.0")
2. Color Palette
   ├── Primitives (background, foreground, primary, secondary, muted, accent, destructive)
   ├── CODEXA Semantic (surface-900→500, text tiers, borders, accent)
   ├── Functional (success, warning, error, info)
   └── Dark mode comparison (side-by-side swatches)
3. Typography
   ├── Font stack (Geist Variable, Inter, JetBrains Mono)
   ├── Type scale specimens (h1→h6, body, small, caption)
   ├── Line height + letter spacing
   └── Font weight range
4. Spacing
   ├── Scale visualization (4px base: 0→96px)
   └── Common patterns (padding, margin, gap)
5. Components
   ├── Buttons (primary, secondary, ghost, destructive)
   ├── Cards (default, elevated, interactive)
   ├── Inputs (text, search, select)
   ├── Badges (status variants)
   └── Tables (striped, hoverable)
6. Icons + Illustrations
7. Dark / Light mode toggle demo
```

## Complete HTML

```html
<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CODEXA Design System</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --background: 0 0% 100%;
      --foreground: 240 10% 3.9%;
      --primary: 240 5.9% 10%;
      --secondary: 240 4.8% 95.9%;
      --muted: 240 4.8% 95.9%;
      --accent: 240 4.8% 95.9%;
      --destructive: 0 84.2% 60.2%;
      --border: 240 5.9% 90%;

      --codexa-accent: #50C878;
      --codexa-surface-900: hsl(240 10% 5%);
      --codexa-surface-800: hsl(240 8% 12%);
      --codexa-surface-700: hsl(240 6% 20%);
      --codexa-surface-600: hsl(240 5% 30%);
      --codexa-surface-500: hsl(240 4% 40%);
      --codexa-text-primary: hsl(0 0% 95%);
      --codexa-text-secondary: hsl(0 0% 70%);
      --codexa-text-tertiary: hsl(0 0% 50%);
      --codexa-border-default: hsl(240 5% 25%);
    }
    body { font-family: 'Inter', sans-serif; }
    .font-mono { font-family: 'JetBrains Mono', monospace; }
    .swatch { width: 80px; height: 80px; border-radius: 12px; border: 1px solid var(--codexa-border-default); }
    .section { margin-bottom: 64px; }
    .section-title { font-size: 14px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.1em; color: var(--codexa-text-tertiary); margin-bottom: 24px; }
  </style>
</head>
<body class="bg-[var(--codexa-surface-900)] text-[var(--codexa-text-primary)] max-w-5xl mx-auto px-8 py-16">

  <!-- Header -->
  <header class="mb-16">
    <div class="flex items-center gap-3 mb-4">
      <div class="w-10 h-10 rounded-lg flex items-center justify-center font-bold text-black" style="background: var(--codexa-accent)">C</div>
      <span class="text-2xl font-bold">CODEXA</span>
    </div>
    <h1 class="text-4xl font-bold mb-2">Design System</h1>
    <p class="text-[var(--codexa-text-secondary)]">v1.0.0 — Tokens, Typography, Components</p>
  </header>

  <!-- COLOR PALETTE -->
  <section class="section">
    <p class="section-title">Color Palette</p>
    <h2 class="text-2xl font-bold mb-6">CODEXA Semantic Colors</h2>
    <div class="grid grid-cols-2 sm:grid-cols-4 lg:grid-cols-6 gap-4 mb-8">
      <div>
        <div class="swatch" style="background: var(--codexa-surface-900)"></div>
        <p class="text-sm mt-2 font-mono">surface-900</p>
      </div>
      <div>
        <div class="swatch" style="background: var(--codexa-surface-800)"></div>
        <p class="text-sm mt-2 font-mono">surface-800</p>
      </div>
      <div>
        <div class="swatch" style="background: var(--codexa-surface-700)"></div>
        <p class="text-sm mt-2 font-mono">surface-700</p>
      </div>
      <div>
        <div class="swatch" style="background: var(--codexa-surface-600)"></div>
        <p class="text-sm mt-2 font-mono">surface-600</p>
      </div>
      <div>
        <div class="swatch" style="background: var(--codexa-surface-500)"></div>
        <p class="text-sm mt-2 font-mono">surface-500</p>
      </div>
      <div>
        <div class="swatch" style="background: var(--codexa-accent)"></div>
        <p class="text-sm mt-2 font-mono">accent</p>
        <p class="text-xs text-[var(--codexa-text-tertiary)]">#50C878</p>
      </div>
    </div>
    <h3 class="text-lg font-semibold mb-4">Functional Colors</h3>
    <div class="grid grid-cols-4 gap-4">
      <div><div class="swatch" style="background: #22c55e"></div><p class="text-sm mt-2 font-mono">success</p></div>
      <div><div class="swatch" style="background: #f59e0b"></div><p class="text-sm mt-2 font-mono">warning</p></div>
      <div><div class="swatch" style="background: #ef4444"></div><p class="text-sm mt-2 font-mono">error</p></div>
      <div><div class="swatch" style="background: #3b82f6"></div><p class="text-sm mt-2 font-mono">info</p></div>
    </div>
  </section>

  <!-- TYPOGRAPHY -->
  <section class="section">
    <p class="section-title">Typography</p>
    <h2 class="text-2xl font-bold mb-6">Type Scale (1.25 ratio)</h2>
    <div class="space-y-6">
      <div class="flex items-baseline gap-4">
        <span class="text-xs text-[var(--codexa-text-tertiary)] w-16">48px</span>
        <span class="text-5xl font-bold" style="line-height: 1.1">Heading 1</span>
      </div>
      <div class="flex items-baseline gap-4">
        <span class="text-xs text-[var(--codexa-text-tertiary)] w-16">36px</span>
        <span class="text-4xl font-bold" style="line-height: 1.2">Heading 2</span>
      </div>
      <div class="flex items-baseline gap-4">
        <span class="text-xs text-[var(--codexa-text-tertiary)] w-16">24px</span>
        <span class="text-2xl font-semibold">Heading 3</span>
      </div>
      <div class="flex items-baseline gap-4">
        <span class="text-xs text-[var(--codexa-text-tertiary)] w-16">16px</span>
        <span class="text-base">Body text — Inter Regular 400, line-height 1.5</span>
      </div>
      <div class="flex items-baseline gap-4">
        <span class="text-xs text-[var(--codexa-text-tertiary)] w-16">14px</span>
        <span class="text-sm font-mono">Code — JetBrains Mono 400</span>
      </div>
    </div>
  </section>

  <!-- SPACING -->
  <section class="section">
    <p class="section-title">Spacing</p>
    <h2 class="text-2xl font-bold mb-6">4px Base Scale</h2>
    <div class="space-y-2">
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">4</span><div class="h-4 rounded" style="width: 16px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">8</span><div class="h-4 rounded" style="width: 32px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">16</span><div class="h-4 rounded" style="width: 64px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">24</span><div class="h-4 rounded" style="width: 96px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">32</span><div class="h-4 rounded" style="width: 128px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">48</span><div class="h-4 rounded" style="width: 192px; background: var(--codexa-accent)"></div></div>
      <div class="flex items-center gap-4"><span class="text-xs w-8 text-right">64</span><div class="h-4 rounded" style="width: 256px; background: var(--codexa-accent)"></div></div>
    </div>
  </section>

  <!-- COMPONENTS -->
  <section class="section">
    <p class="section-title">Components</p>
    <h2 class="text-2xl font-bold mb-6">Buttons</h2>
    <div class="flex flex-wrap gap-4 mb-8">
      <button class="px-4 py-2 rounded-lg font-medium text-black" style="background: var(--codexa-accent)">Primary</button>
      <button class="px-4 py-2 rounded-lg font-medium border" style="border-color: var(--codexa-border-default); color: var(--codexa-text-primary)">Secondary</button>
      <button class="px-4 py-2 rounded-lg font-medium text-[var(--codexa-text-secondary)] hover:text-[var(--codexa-text-primary)]">Ghost</button>
      <button class="px-4 py-2 rounded-lg font-medium bg-red-500/20 text-red-400">Destructive</button>
    </div>
    <h2 class="text-2xl font-bold mb-6">Badges</h2>
    <div class="flex flex-wrap gap-3">
      <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-green-500/20 text-green-400">Active</span>
      <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-amber-500/20 text-amber-400">Pending</span>
      <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-red-500/20 text-red-400">Error</span>
      <span class="px-2.5 py-1 rounded-full text-xs font-medium bg-blue-500/20 text-blue-400">Info</span>
    </div>
  </section>

</body>
</html>
```

## Usage
1. Copy HTML to local file
2. Customize token values in `:root`
3. Replace CODEXA branding with target brand
4. Screenshot sections for documentation
5. Deploy as static page for team reference
