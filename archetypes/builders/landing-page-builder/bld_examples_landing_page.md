---
id: bld_examples_landing_page
kind: examples
pillar: P01
builder: landing-page-builder
version: 1.0.0
quality: 9.1
title: "Examples Landing Page"
author: n03_builder
tags: [landing_page, builder, examples]
tldr: "Golden and anti-examples for landing page construction, demonstrating ideal structure and common pitfalls."
domain: "landing page construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# Examples: Landing Page Builder

## Example 1: SaaS Product (HTML + Tailwind)

**Input**: "Create a landing page for CodeForge, an AI testing tool for developers"

**Output sketch** (abbreviated — real output is complete HTML):
```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>CodeForge — Tests First. Code Fearless.</title>
  <meta name="description" content="AI that writes tests before you write code. Ship faster with confidence.">
  <meta property="og:title" content="CodeForge — Tests First. Code Fearless.">
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
</head>
<body class="bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100">
  <!-- HERO -->
  <section id="hero" aria-label="Hero" class="min-h-screen flex items-center">
    <div class="max-w-7xl mx-auto px-4 text-center">
      <h1 class="text-5xl md:text-7xl font-bold">Tests First. Code Fearless.</h1>
      <p class="mt-6 text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto">
        AI that writes your tests before you write code. Ship 3x faster with full coverage.
      </p>
      <a href="#pricing" data-track="hero-cta"
         class="mt-8 inline-block px-8 py-4 bg-blue-600 text-white rounded-lg text-lg font-semibold hover:bg-blue-700 transition">
        Start Free Trial
      </a>
    </div>
  </section>
  <!-- ... 11 more sections ... -->
</body>
</html>
```

## Example 2: Infoproduct/Curso (PT-BR)

**Input**: "Create landing page for AI automation course, R$497, 8 modules"

**Section order** (infoproduct template):
HERO (transformation) > PROBLEMA (dor do manual) > TRANSFORMACAO (antes/depois) >
MODULOS (8 cards) > DEPOIMENTOS > GARANTIA (7 dias) > PRICING (R$497 ou 12x) >
FAQ > CTA FINAL > FOOTER

## Anti-Example
```html
<!-- BAD: Not a landing page, just a wireframe -->
<div>
  <h1>Title here</h1>
  <p>Description here</p>
  <button>CTA</button>
</div>
<!-- Missing: responsive, dark mode, SEO, a11y, sections, styling, EVERYTHING -->
```

## Exemplar Requirements

1. Score 9.0+ to qualify as few-shot reference
2. Demonstrate ideal structure for this artifact kind
3. Populate all frontmatter fields with realistic values
4. Use domain-specific content not generic placeholders
5. Enable retrieval via tags and TF-IDF matching

## Properties

| Property | Value |
|----------|-------|
| Kind | `examples` |
| Pillar | P01 |
| Domain | landing page construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
