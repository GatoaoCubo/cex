---
id: p12_wf_visual_frontend_marketing
kind: workflow
pillar: P12
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
title: Visual Frontend + Marketing Production Workflows
steps_count: 18
execution: mode_branching_sequential
agent_nodes: [n02-visual-marketing-hub, n07-orchestrator]
timeout: 5400000
retry_policy: per_step_with_mode_awareness
depends_on: []
signals: [visual_complete, copy_complete, dual_complete, workflow_error]
domain: visual_frontend_engineering_and_copywriting
quality: null
tags: [workflow, visual-frontend, marketing, html, tailwind, copywriting, N02, component, landing_page]
tldr: 6 dual-role workflows — 3 visual (component, landing page, responsive), 2 copy (campaign, email), 1 dual (integrated page) — mode-aware execution.
density_score: 0.96
---

# Visual Frontend + Marketing Production Workflows

## Overview

Six operational workflows for dual-role N02. Mode detection → specialized workflow execution.
Each produces committed, compiled artifacts with mode-appropriate quality gates.
Executes on `n02-visual-marketing-hub` (claude-sonnet-4-6 + opus fallback).

## Mode Detection & Routing

```
INPUT: intent→detect-mode→route-workflow

VISUAL MODE: component, html, tailwind, responsive, design, css, layout
COPY MODE: copy, ad, headline, email, campaign, brand_voice
DUAL MODE: landing page + copy, integrated page, visual + persuasive

WORKFLOW ROUTING:
- detect_mode(intent) returns: VISUAL | COPY | DUAL
- route to appropriate workflow
- apply mode-specific quality gates
- use mode-appropriate tools (browser MCP vs readability check)
```

---

## VISUAL MODE Workflows

### Workflow V1: Build HTML Component

**Goal**: Create production-ready HTML component with Tailwind CSS and shadcn/ui patterns
**Input required**: Component type, styling requirements, functionality specs, accessibility level
**Output**: Complete component file with HTML, styling, and documentation

#### Steps

```
Step 1: COMPONENT SPEC [n02-visual-marketing-hub]
  - Input: component type (button, form, card, navbar, etc.)
  - Action: Define component API, props, variants, accessibility requirements
  - Output: component_spec_{mission}.md
  - Signal: spec_complete

Step 2: HTML STRUCTURE [n02-visual-marketing-hub]
  - Action: Generate semantic HTML5 markup with proper ARIA labels
  - Apply: WCAG AA compliance, keyboard navigation support
  - Output: component_html_{mission}.md
  - Signal: html_complete

Step 3: TAILWIND STYLING [n02-visual-marketing-hub]
  - Action: Apply utility classes, design tokens, responsive variants
  - Ensure: zero hardcoded hex, mobile-first approach, dark mode support
  - Output: component_styled_{mission}.md
  - Signal: styling_complete

Step 4: VALIDATE + COMPILE [n02-visual-marketing-hub]
  - Validate: W3C HTML validator, Lighthouse audit, accessibility check
  - Compile: python _tools/cex_compile.py
  - Commit: git commit -m "[N02] component — {mission}"
  - Signal: visual_complete
```

### Workflow V2: Build Landing Page

**Goal**: Create complete responsive landing page with multiple sections
**Input required**: Page purpose, sections needed, design style, responsive requirements
**Output**: Full HTML page with optimized performance and accessibility

#### Steps

```
Step 1: PAGE ARCHITECTURE [n02-visual-marketing-hub]
  - Input: page purpose, required sections (hero, features, testimonials, etc.)
  - Action: Define page structure, layout pattern (F/Z), breakpoint strategy
  - Output: page_architecture_{mission}.md
  - Signal: architecture_complete

Step 2: HTML GENERATION [n02-visual-marketing-hub]
  - Action: Generate complete HTML page with semantic structure
  - Include: proper heading hierarchy, meta tags, accessibility features
  - Output: landing_page_html_{mission}.md
  - Signal: html_complete

Step 3: RESPONSIVE IMPLEMENTATION [n02-visual-marketing-hub]
  - Action: Apply mobile-first responsive classes, test breakpoints
  - Ensure: touch-friendly interactions, readable typography scaling
  - Output: responsive_optimized_{mission}.md
  - Signal: responsive_complete

Step 4: PERFORMANCE + COMPILE [n02-visual-marketing-hub]
  - Validate: Lighthouse score >= 90, W3C validation, contrast check
  - Optimize: lazy loading, proper image sizing, minimal CSS
  - Compile + Commit: git commit -m "[N02] landing page — {mission}"
  - Signal: visual_complete
```

---

## COPY MODE Workflows

### Workflow C1: Ad Campaign

**Goal**: Produce complete ad creative set for one campaign (Facebook/Google/LinkedIn)
**Input required**: Product name, audience segment, key benefit, budget range, campaign objective
**Output**: Campaign brief + 3 ad variants per format (image/video/carousel) + copy deck

### Steps

```
Step 1: BRIEF [n02-marketing-hub]
  - Input: product/audience/goal from handoff
  - Action: Write campaign brief (objective, audience, key message, channels, KPIs)
  - Output: campaign_brief_{mission}.md
  - Signal: brief_complete

Step 2: AUDIENCE [n02-marketing-hub]
  - Input: campaign brief
  - Action: Define 3 audience segments with pain points and desire statements
  - Output: audience_profile_{mission}.md
  - Signal: audience_complete

Step 3: HEADLINES [n02-marketing-hub]
  - Input: audience profiles + key benefit
  - Action: Generate 10 headline variants per segment (score with 4U formula)
  - Top 3 per segment advance; output: headlines_{mission}.md
  - Signal: headlines_complete

Step 4: AD COPY [n02-marketing-hub]
  - Input: top headlines + audience profiles
  - Action: Write full ad copy (hook + body + CTA) for each format — 3 A/B variants
  - Output: ad_copy_{mission}.md
  - Depends on: Steps 2, 3
  - Signal: copy_complete

Step 5: COMPILE + COMMIT [n02-marketing-hub]
  - Action: Compile all artifacts, git add + commit, write signal
  - Command: git commit -m "[N02] ad campaign copy — {mission}"
  - Signal: marketing_copy_complete
```

---

## Workflow 2: Landing Page Copy

**Goal**: Produce full landing page copy for a product or offer
**Input required**: Product, audience, offer, primary CTA, optional testimonials
**Output**: Complete LP copy file with all sections

### Steps

```
Step 1: RESEARCH [n02-marketing-hub]
  - Action: If markitdown/fetch available, pull competitor LP for teardown
  - Output: competitor_notes_{mission}.md (optional)
  - Fallback: proceed from KC formulas if no web access

Step 2: HERO SECTION [n02-marketing-hub]
  - Action: Write headline (10 variants, top 3 selected) + subhead + hero CTA
  - Apply: 4U formula scoring; select variant with highest score
  - Output: lp_hero_{mission}.md

Step 3: BODY COPY [n02-marketing-hub]
  - Sections to write:
    a. Problem/Agitate block (PAS formula — 150 words)
    b. Solution intro (2 sentences, transformation language)
    c. Benefits block (FAB format — 5–7 bullets)
    d. Social proof section (3 testimonial slots with [NAME] [COMPANY] placeholders)
    e. Objection-busting FAQ (5 questions, direct answers)
    f. Final CTA section (urgency + benefit restatement + button copy)
  - Output: lp_body_{mission}.md

Step 4: COMPILE + COMMIT [n02-marketing-hub]
  - Merge hero + body into lp_complete_{mission}.md
  - Run readability check (target Flesch >= 60)
  - Compile: python _tools/cex_compile.py
  - Commit: git commit -m "[N02] landing page copy — {mission}"
  - Signal: marketing_copy_complete
```

---

## Workflow 3: Email Sequence

**Goal**: Produce a 5-email nurture or cold outreach sequence
**Input required**: Audience, goal (nurture/cold/cart/re-engagement), product/offer
**Output**: 5 emails with subject lines, preview text, and body copy

### Steps

```
Step 1: SEQUENCE PLAN [n02-marketing-hub]
  - Input: goal type (nurture | cold | cart | re-engagement)
  - Action: Select skeleton from KC, map each email to objective
  - Output: email_plan_{mission}.md
  - Signal: plan_complete

Step 2: EMAIL COPY [n02-marketing-hub]
  - For each email (1–5):
    - Write subject line (3 variants, select best by curiosity gap)
    - Write preview text (40–90 chars)
    - Write email body (formula-matched per email type)
    - Write CTA (specific + benefit-first)
  - Output: email_sequence_{mission}.md
  - Depends on: Step 1
  - Signal: copy_complete

Step 3: COMPILE + COMMIT [n02-marketing-hub]
  - Compile sequence file
  - Commit: git commit -m "[N02] email sequence — {mission}"
  - Signal: marketing_copy_complete
```

---

---

## Workflow 4: Brand Voice Card

**Goal**: Define and document a brand's writing voice for consistent copy production
**Input required**: Brand name, brand description, 2–3 copy samples (or NONE), target tone description
**Output**: Brand voice card with tone scores, signature phrases, banned words, persona anchor

### Steps

```
Step 1: VOICE EXTRACT [n02-marketing-hub]
  - If samples provided: analyze tone, vocabulary, energy, person dimensions
  - If no samples: build from target tone description alone
  - Score each dimension 1–5: Formal↔Casual, Technical↔Plain, 3rd↔1st, Calm↔Bold
  - Output: voice_dimensions_{mission}.md

Step 2: VOICE CARD [n02-marketing-hub]
  - Write: 5 signature phrases the brand says
  - Write: 5 banned words/phrases the brand never says
  - Write: persona anchor (brand as a person: age, job, how they talk)
  - Write: 3 before/after examples showing voice applied to weak copy
  - Write: voice flex rules (when voice can adapt, when it must hold)
  - Output: brand_voice_card_{mission}.md

Step 3: COMPILE + COMMIT [n02-marketing-hub]
  - Compile voice card
  - Commit: git commit -m "[N02] brand voice card — {mission}"
  - Signal: marketing_copy_complete
```

---

## Error Handling

- **Step fails**: retry once with revised prompt; if still fail, signal `marketing_copy_error` to N07
- **Quality gate fails** (score < 8.0): return to copy step, apply F6 retry, max 2 revisions
- **MCP unavailable**: proceed with formula-based approach from KC; note in output
- **No brand voice card**: write in neutral professional tone; flag "[BRAND VOICE CARD RECOMMENDED]" at top

## Signals

| Signal | Emitter | Meaning |
|--------|---------|---------|
| marketing_copy_complete | n02-marketing-hub | All deliverables saved, compiled, committed |
| marketing_copy_error | n02-marketing-hub | Unrecoverable failure, escalate to N07 |
