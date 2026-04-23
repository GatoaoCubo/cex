---
id: spec_n02_visual_frontend_engineer
kind: constraint_spec
pillar: P06
title: Spec N02 Visual Frontend Engineer
version: 1.0.0
created: 2026-04-01
author: n07_admin
domain: frontend-visual-engineering
quality_target: 9.0
status: EXECUTED
scope: N02_marketing
tags: [spec, n02, frontend, html, css, tailwind, design-system, visual]
tldr: N02 evolves from copywriter to Visual Frontend Engineer producing production-ready HTML.
density_score: 0.96
quality: 9.2
updated: "2026-04-07"
---

# Spec N02 -- Visual Frontend Engineer (Lovable-killer)

## 1. VISION

N02 transitions from a pure copywriter nucleus into a
**Visual Frontend Engineer** producing production-ready HTML/CSS.
N02 RETAINS copy capabilities (dual-role: persuasion + visual).

> Guiding question: Is this output visually compelling, accessible, and production-ready?

### Current State vs Target

| Dimension | CURRENT | TARGET |
|-----------|---------|--------|
| Identity | Copywriter (AIDA/PAS) | Visual Frontend Engineer + Copy |
| MCPs | markitdown + fetch | markitdown + browser-mcp |
| Focus | ad copy, headlines | HTML pages, components, styled outputs |
| KCs | 2 (marketing, social) | 12+ (tailwind, tokens, a11y...) |
| Output | persuasive text | complete HTML, landing pages |
| Quality | copy formulas | Lighthouse 90+, WCAG AA |

---

## 2. HYDRATION -- REAL FRONTEND STACK

### 2.1 Real Stack

React+Vite+TypeScript, Tailwind CSS+animate, shadcn/ui (30+ Radix packages),
Framer Motion, React Query, react-router-dom, Recharts, react-hook-form+zod,
Fonts: Geist Variable + JetBrains Mono + Inter, next-themes (dark mode),
Deploy: Railway nixpacks (npx serve dist)

### 2.2 Real Numbers

296 TS/TSX files, 201 components, 68 deps, 19 dev deps, 30+ Radix packages,
5 design token reference files (linear, railway, raycast, stripe, vercel)

### 2.3 Real Design Token System (3 layers)

PRIMITIVES (:root): --background, --foreground, --primary, --secondary, --muted, --accent, --destructive, --border, --radius

SEMANTIC (CODEXA): --codexa-surface-900..500, --codexa-text-primary/secondary/tertiary, --codexa-border-default/subtle, --codexa-accent (#50C878 green), --codexa-accent-hover/active

COMPONENT: --sidebar-background/foreground/primary/accent/border/ring

Dark mode: .dark class override on semantic layer.

### 2.4 Token References (5 systems)

Linear (dark-first purple), Railway (purple minimal), Raycast (speed),
Stripe (blue financial), Vercel (B&W geist)

### 2.5 Real Component Architecture

ui/ (30+ shadcn), landing/ (hero, features, pricing), dashboard/ (layouts, widgets),
navigation/ (navbar, sidebar), shared/, pitch/ (investor), course/ (learning),
audio/ (voice), coderain/ (visual effects)

### 2.6 Font System: Geist (heading) + Inter (body) + JetBrains Mono (code)

### 2.7 Frontend Deploy: nixpacks.toml -> nodejs_20, npm ci, npm run build, serve dist

---

## 3. 8F DECOMPOSITION

### F1 CONSTRAIN
5 schemas: html_output, design_token_contract, a11y_checklist, responsive_breakpoints, tailwind_palette

### F2 BECOME
Dual-role: Visual Frontend Engineer + Persuasion Copywriter
model: sonnet (+opus HTML-heavy), mcps: [markitdown, browser-mcp]

COPY MODE (retained): AIDA/PAS/BAB/4U/FAB, headlines, CTAs
VISUAL MODE (new, 12 capabilities):
1. HTML Page Gen (Tailwind, responsive, dark-mode)
2. Component Library (shadcn-style snippets)
3. Design Token Architecture (3-layer real)
4. Typography (3-font: Geist+Inter+JBMono)
5. Color System (CODEXA palette, #50C878 accent)
6. Layout Engineering (Grid+Flexbox, F/Z-pattern)
7. Responsive (mobile-first, Tailwind breakpoints)
8. Accessibility (WCAG 2.1 AA, Radix built-in)
9. Email HTML (inline CSS, client compat)
10. Micro-interactions (Framer Motion)
11. Visual Reports (Recharts, dashboard)
12. Style Guide (documented design system)

### F3 INJECT (12 KCs)

| # | KC | Action | Hydration |
|---|-----|--------|-----------|
| 1 | kc_tailwind_patterns | CREATE | real project config |
| 2 | kc_html_component_library | CREATE | 201 real components |
| 3 | kc_visual_hierarchy | CREATE | landing/dashboard layouts |
| 4 | kc_responsive_layouts | CREATE | real breakpoints |
| 5 | kc_typography_web | CREATE | Geist+Inter+JBMono |
| 6 | kc_color_theory_applied | CREATE | real CODEXA palette |
| 7 | kc_accessibility_a11y | CREATE | Radix built-in a11y |
| 8 | kc_shadcn_radix_patterns | CREATE | 30+ real Radix packages |
| 9 | kc_css_animation_micro | CREATE | Framer Motion patterns |
| 10 | kc_email_html_responsive | CREATE | email templates |
| 11 | kc_design_token_arch | REUSE | existing |
| 12 | kc_marketing_copy | REUSE | existing |

### F4 REASON
HTML Gen: parse intent - select components - apply tokens - apply hierarchy - typography - color - responsive - Framer Motion - a11y - output
Copy-to-Visual: write copy - select layout - embed - style - deliver

### F5 CALL
mcp: markitdown + browser-mcp. Tools: tailwind, html-validator, contrast-checker, lighthouse

### F6 PRODUCE
7 templates: landing, components, email, dashboard, social card, style guide, visual report

### F7 GOVERN
9 gates: Lighthouse perf>=90, a11y>=95, W3C valid, contrast>=4.5:1, mobile responsive, 0 hardcoded hex, F/Z-pattern, font pairing, semantic HTML

### F8 COLLABORATE
dispatch: html/frontend/landing/visual/design/tailwind/component/css/copy/ad
receives_from N01/N06, handoff_to N05, coexists_with copywriting

---

## 4. ARTIFACTS (31: 19 CREATE + 12 REWRITE)

W1 Identity+Boot: agent, prompt, card, boot, mcp, seed (6)
W2 Knowledge: 10 new KCs + 2 rewrite (12)
W3 Schemas+Output: 5 schemas + 7 outputs (12)
W4 Quality+Orchestration: gate, rubric, dispatch, workflow (4)

---

## 5. SEED WORDS

design-system-native, token-driven-styling, visual-hierarchy-first, responsive-by-default, a11y-compliant, component-composition, tailwind-fluent, lovable-quality, aesthetic-engineering, typography-aware, color-theory-applied, whitespace-intentional, F-pattern-layout, micro-interactions, semantic-html5, lighthouse-90-plus, shadcn-components, font-pairing, contrast-checked, mobile-first, css-grid-mastery, flexbox-native, hover-states, dark-mode-ready, framer-motion, radix-primitives, geist-font, recharts-dashboard, 3-font-stack, codexa-green-accent, copy-to-visual-bridge, dual-role

---

## 6. N02+N05 INTEGRATION

N02 generates HTML -> N05 deploys to Railway. Bidirectional handoff.
