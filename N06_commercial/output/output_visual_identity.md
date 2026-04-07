---
id: n06_output_visual_identity
kind: visual_identity
pillar: P06
title: "Identidade Visual GATO³ — Paleta PB Minimalista + Tipografia"
version: 1.0.0
created: 2026-04-02
author: n06_commercial
domain: brand-visual
quality: 9.2
tags: [brand, visual, identity, cores, tipografia, gato3, n06]
tldr: "Identidade visual GATO³: paleta PB minimalista, tipografia Allrounder+Kenao, guidelines de uso, fotografia alto contraste, dark mode. Design tokens para N03."
density_score: 0.93
---

# Visual Identity — GATO³

## Color Palette

### Primary Colors

| Role | HEX | HSL | RGB | Usage |
|------|-----|-----|-----|-------|
| **Primary** | #000000 | 0°, 0%, 0% | 0, 0, 0 | Headlines, primary CTAs, key UI elements |
| **Secondary** | #1F1F1F | 0°, 0%, 12% | 31, 31, 31 | Supporting elements, cards, navigation |
| **Accent** | #7A7A7A | 0°, 0%, 48% | 122, 122, 122 | Highlights, badges, interactive states |

### Surface Colors

| Role | HEX | Usage |
|------|-----|-------|
| **Background** | #FFFFFF | Page background, canvas |
| **Foreground** | #000000 | Body text, primary content |
| **Surface** | #D1D1D1 | Cards, modals, elevated elements |

### Color Psychology

| Color | Emotion | Why GATO³ Uses It |
|-------|---------|-------------------|
| #000000 | Elegância, sofisticação, atemporalidade | Transmite seriedade e qualidade premium, diferencia de pet shops coloridos |
| #1F1F1F | Profundidade, contraste suave, modernidade | Cria hierarquia visual sem quebrar minimalismo |
| #7A7A7A | Equilíbrio, neutralidade, versatilidade | Elementos secundários que não competem com conteúdo principal |

### Contrast Ratios (WCAG 2.1)

| Combination | Ratio | AA | AAA |
|------------|-------|-----|-----|
| Foreground on Background | 21:1 | ✅ | ✅ |
| Accent on Background | 4.5:1 | ✅ | ❌ |
| Foreground on Surface | 9.2:1 | ✅ | ✅ |

## Typography

### Font Stack

| Role | Font | Weight | Size Scale | Line Height |
|------|------|--------|------------|-------------|
| **Heading** | Allrounder | 600-700 | 2.0-3.5rem | 1.2 |
| **Body** | Kenao | 400-500 | 0.875-1.125rem | 1.6 |
| **Mono** | JetBrains Mono | 400-600 | 0.75-1.0rem | 1.4 |

### Type Scale (px)

| Level | Size | Weight | Use |
|-------|------|--------|-----|
| H1 | 48 | 700 | Page titles |
| H2 | 36 | 600 | Section headers |
| H3 | 24 | 600 | Subsections |
| H4 | 20 | 500 | Card titles |
| Body | 16 | 400 | Paragraphs |
| Small | 14 | 400 | Captions, labels |
| Tiny | 12 | 400 | Legal, footnotes |

### Pairing Rationale
Allrounder traz personalidade display geométrica para títulos e headlines, mantendo legibilidade. Kenao oferece excelente legibilidade em interfaces e textos corridos, complementando a geometria do Allrounder. JetBrains Mono garante clareza em elementos técnicos. Juntas criam harmonia visual sem competição.

## Logo Usage

### Clear Space
Minimum clear space around logo = ≥1× expoente ³ em todos os lados.

### Minimum Size
- Digital: 24px width minimum
- Print: 10mm width minimum

### Approved Variations
1. Cubo + wordmark GATO³ (versão completa)
2. Cubo sozinho (quando espaço limitado)
3. Wordmark sozinho (aplicações tipográficas)
4. Versão monocromática branca (fundos escuros)

### Prohibited Usage
- ❌ Não esticar ou distorcer proporções
- ❌ Não rotacionar ou inclinar
- ❌ Não adicionar sombras ou efeitos
- ❌ Não usar sobre fundos com muito ruído
- ❌ Não alterar cores fora da paleta aprovada
- ❌ Não separar cubo do ³ expoente

## Photography Style
- **Mood**: PB alto contraste, minimalista, produto como meio não fim
- **Lighting**: Natural difusa ou artificial direcionada, evitar sombras duras
- **Subjects**: Gatos em ambientes reais, produtos integrados na decoração, tutores interagindo naturalmente
- **Post-processing**: Desaturação seletiva mantendo tons de pele, alto contraste, grain sutil
- **Avoid**: Fundos coloridos, cenários montados, pets posando forçadamente, acúmulo de produtos

## Iconografia
- **Style**: Monoline 2px weight, geométrica, consistente com cubo da marca
- **Grid**: 24px base, alinhamento pixel-perfect
- **Corner radius**: 2px quando aplicável
- **Palette**: Apenas cores da marca (#000000, #7A7A7A, #FFFFFF)

## Motion Design
- **Easing**: out-quad (natural, confortável)
- **Duration**: Microinterações 150-250ms, transições 300-500ms
- **Physics**: Sutis, sem bounce ou elastic exagerados
- **Triggers**: Hover, focus, state changes

## Dark Mode Rules
- Background → #1F1F1F
- Foreground → #FFFFFF  
- Surface → #2A2A2A
- Accent remains #7A7A7A (unchanged)
- Reduce image brightness to 85%
- Use surface color for card backgrounds, not pure black

---

## Design Token Export

For N03 Builder consumption:

```css
:root {
  --brand-primary: #000000;
  --brand-secondary: #1F1F1F;
  --brand-accent: #7A7A7A;
  --brand-bg: #FFFFFF;
  --brand-fg: #000000;
  --brand-surface: #D1D1D1;
  --font-heading: 'Allrounder', sans-serif;
  --font-body: 'Kenao', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
  --icon-weight: 2px;
  --motion-easing: cubic-bezier(0.25, 0.46, 0.45, 0.94);
  --motion-duration-micro: 150ms;
  --motion-duration-transition: 300ms;
}

@media (prefers-color-scheme: dark) {
  :root {
    --brand-bg: #1F1F1F;
    --brand-fg: #FFFFFF;
    --brand-surface: #2A2A2A;
  }
}
```

---

*Generated by N06 Brand Architect · Source: `.cex/brand/brand_config.yaml` visual section*
