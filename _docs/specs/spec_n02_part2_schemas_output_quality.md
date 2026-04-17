---
id: spec_n02_part2
kind: constraint_spec
pillar: P06
title: Spec N02 Part 2 -- Schemas Output Quality Orchestration
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: frontend-visual-engineering
quality_target: 9.0
status: EXECUTED
scope: N02_marketing
depends_on: spec_n02_visual_frontend_engineer
tags: [spec, n02, schemas, output, quality-gates, html, tailwind, a11y]
tldr: Waves 3-4 do N02 -- schemas visuais, output templates HTML, quality gates, orchestration.
density_score: 0.95
quality: 9.0
updated: "2026-04-07"
---

# Spec N02 Part 2 -- Schemas, Output, Quality, Orchestration

## PRE-REQUISITOS COMPLETOS

- [x] Part 1 identidade (agent dual-role, system_prompt, agent_card)
- [x] Wave 2 KCs (10 novos via SHAKA, 104KB)
- [x] Boot/config (n02.cmd, .mcp-n02.json, seed)

---

## WAVE 3A: SCHEMAS (P06) -- 5 CREATE em N02/P06_schema/

### 3.1 html_output_schema.yaml
Valida todo HTML output do N02.
DOCTYPE html, lang attribute, meta viewport, meta charset utf-8.
Semantic elements: header, main, footer obrigatorios.
Heading hierarchy: h1 unico, h2-h6 sem saltos.
Tailwind CDN link ou build. Nenhum style inline arbitrario.
Alt em toda img. Role/aria em elementos interativos.
Mobile viewport: width=device-width, initial-scale=1.

### 3.2 design_token_contract.yaml
3-layer token system baseado no index.css real:
Layer 1 PRIMITIVES: --background, --foreground, --primary, --secondary, --muted, --accent, --destructive, --border, --radius. Valores HSL.
Layer 2 SEMANTIC: --codexa-surface-900..500, --codexa-text-primary/secondary/tertiary, --codexa-border-default/subtle, --codexa-accent (#50C878). Referencia primitives.
Layer 3 COMPONENT: --sidebar-*, --card-*, --button-*. Referencia semantics.
Rule: 0 hex hardcoded em components. Dark mode: .dark class no semantic layer only.

### 3.3 a11y_checklist.yaml
WCAG 2.1 AA minimum baseado em kc_accessibility_a11y:
Perceivable: alt text, captions, contrast >= 4.5:1 (text), >= 3:1 (large text).
Operable: keyboard nav (tab order), focus-visible, skip-to-content, no keyboard traps.
Understandable: form labels, error messages, consistent nav, language attribute.
Robust: valid HTML, ARIA roles correct, heading hierarchy, semantic elements.
Touch targets: min 48x48px. prefers-reduced-motion: respect.

### 3.4 responsive_breakpoints.yaml
Mobile-first breakpoints (Tailwind defaults):
base: 0-639px (mobile), sm: 640px, md: 768px, lg: 1024px, xl: 1280px, 2xl: 1536px.
Max content width: 1280px (max-w-7xl).
Fluid typography: clamp(1rem, 2.5vw, 1.25rem) body, clamp(1.5rem, 4vw, 3rem) h1.
Grid: 1col mobile, 2col md, 3col lg, 4col xl.
Touch targets: 48px min on mobile. Spacing scale: 4px base.

### 3.5 tailwind_palette_contract.yaml
Palette restrita ao design system. Cores permitidas: primary, secondary, accent, muted, destructive, background, foreground, border.
CODEXA extras: surface-900..500, codexa-accent(#50C878), codexa-accent-hover, codexa-accent-active.
60-30-10 rule enforced: 60% background, 30% secondary/muted, 10% accent.
Dark mode: inverted lightness, same hue. Forbidden: arbitrary hex in className.

---

## WAVE 3B: OUTPUT TEMPLATES (P05) -- 7 CREATE em N02/P05_output/

### 3.6 output_landing_page.md
Template HTML completo para landing pages.
Estrutura: hero (headline+subhead+CTA+visual) > features grid (3-6 items) > social proof (testimonials) > pricing (2-3 tiers) > FAQ accordion > final CTA > footer.
Inclui: Tailwind CDN, design tokens, dark mode toggle, responsive (mobile-first), Geist+Inter fonts, meta tags SEO, og:image.
Variantes: SaaS, e-commerce, infoproduto.

### 3.7 output_component_library.md
Catalogo de componentes HTML reutilizaveis baseado em kc_html_component_library.
Cada componente: nome, HTML semantico, Tailwind classes, responsive, dark mode, a11y.
Componentes: hero (5 variants), navbar (3), feature grid (4), pricing table, testimonial card, FAQ accordion, footer (3), CTA block (3), stat counter, login form, dashboard sidebar+main.
Padrao: copy-paste ready, Tailwind CDN compatible.

### 3.8 output_email_template.md
Template email HTML responsivo baseado em kc_email_html_responsive.
Table-based layout (Outlook compat), inline CSS, max-width 600px.
Variantes: welcome, transactional, marketing, cart abandonment.
Inclui: MSO conditionals, dark mode hacks, web-safe font stacks, image fallbacks.
Testado: Gmail, Outlook, Apple Mail, Yahoo.

### 3.9 output_dashboard_ui.md
Template dashboard com sidebar + main content.
Inclui: nav sidebar (collapsible), top bar (search+avatar+notifications), content area (cards grid), data table (sortable), chart placeholder (Recharts-compatible), stat cards (4-grid), responsive (sidebar->drawer on mobile).
Design tokens: surface-900 sidebar, surface-800 content, codexa-accent highlights.

### 3.10 output_social_card.md
Template HTML/SVG para cards de redes sociais.
Formatos: og:image (1200x630), Instagram (1080x1080), LinkedIn (1200x627), X/Twitter (1200x675).
Inclui: gradient backgrounds, typography hierarchy, logo placement, CTA text.
Renderizavel como screenshot via browser-mcp.

### 3.11 output_style_guide.md
Design system documentado como HTML page.
Secoes: color palette (swatches + tokens), typography (font stack + scale + specimens), spacing (scale visual), components (live examples), icons, dark mode comparison.
Baseado nos 5 design token references (Linear, Railway, Raycast, Stripe, Vercel).
Self-contained HTML com todos tokens CSS inline.

### 3.12 output_visual_report.md
Template para reports longos com visual profissional.
Estrutura: cover (titulo+data+logo) > executive summary > sections com headers hierarquicos > data tables styled > chart placeholders > conclusions > appendix.
Typography: Geist headings, Inter body, JetBrains Mono code blocks.
Print-friendly: @media print com page-break-before.

---

## WAVE 4A: QUALITY GATES (P07) -- 2 REWRITE

### 4.1 quality_gate_marketing.md

| Gate | Threshold | Required |
|------|-----------|----------|
| lighthouse_perf | >= 90 | yes |
| lighthouse_a11y | >= 95 | yes |
| w3c_valid | 0 HTML errors | yes |
| contrast_ratio | >= 4.5:1 text | yes |
| mobile_responsive | 320-1280px | yes |
| zero_hardcoded_hex | 0 hex in components | yes |
| visual_hierarchy | F/Z-pattern | no |
| font_pairing | heading+body distinct | yes |
| semantic_html | h1-h6 order correct | yes |
| dark_mode | .dark renders OK | yes |
| touch_targets | >= 48x48px mobile | yes |
| reduced_motion | respected | no |

### 4.2 scoring_rubric_marketing.md
Dual scoring: COPY (hook 0-3, CTA 0-3, formula 0-2, audience 0-2) + VISUAL (layout 0-3, color 0-2, typography 0-2, responsive 0-2, a11y 0-1). Final: average normalized to 10. Min 8.0 publish, 9.0 golden.

---

## WAVE 4B: ORCHESTRATION (P12) -- 2 REWRITE

### 4.3 dispatch_rule_marketing.md
keywords: html, frontend, landing, visual, design, tailwind, component, css, responsive, email, dashboard, copy, ad, headline, campanha, CTA, brand.
receives_from: [N01, N06], handoff_to: [N05(deploy)], coexists_with: copywriting.
model: sonnet (default), opus (HTML-heavy). mcps: [markitdown, browser-mcp].

### 4.4 workflow_marketing.md
COPY workflow: brief > audience > formula (AIDA/PAS/BAB) > write > A/B > score > deliver.
VISUAL workflow: intent > page type > components (KC library) > tokens (3-layer) > typography (3-font) > color (60-30-10) > responsive > animations > a11y > lighthouse > deliver HTML.
BRIDGE: write copy > select layout > embed in components > style tokens > deliver page.

---

## ARTEFATOS PART 2 (16 total: 12 CREATE + 4 REWRITE)

W3A Schemas: 5 CREATE (html_output, design_token, a11y, responsive, tailwind_palette)
W3B Output: 7 CREATE (landing, components, email, dashboard, social, style_guide, report)
W4A Quality: 2 REWRITE (quality_gate 12 gates, scoring_rubric dual)
W4B Orch: 2 REWRITE (dispatch_rule, workflow copy+visual+bridge)
