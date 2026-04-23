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
agent_groups: [n02-visual-marketing-hub, n07-orchestrator]
timeout: 5400000
retry_policy: per_step_with_mode_awareness
depends_on: []
signals: [visual_complete, copy_complete, dual_complete, workflow_error]
domain: visual_frontend_engineering_and_copywriting
quality: 9.1
tags: [workflow, visual-frontend, marketing, html, tailwind, copywriting, N02, component, landing_page]
tldr: 6 dual-role workflows — 3 visual (component, landing page, responsive), 2 copy (campaign, email), 1 dual (integrated page) — mode-aware execution.
density_score: 0.96
related:
  - p12_dr_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p03_ap_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p07_sr_visual_frontend_marketing
  - p11_qg_visual_frontend_marketing
  - p03_pt_visual_frontend_marketing
  - landing-page-builder
  - spec_n02_visual_frontend_engineer
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

**Goal**: Produce complete ad creative set for one campaign
**Input required**: Product name, audience segment, key benefit, campaign objective
**Output**: Campaign brief + 3 ad variants per platform with A/B headlines and CTAs

#### Steps

```
Step 1: BRIEF + HEADLINES [n02-visual-marketing-hub]
  - Action: Write campaign brief + generate 10 headline variants with 4U scoring
  - Select: Top 3 headlines for each platform (FB, Google, LinkedIn)
  - Output: campaign_brief_{mission}.md
  - Signal: brief_complete

Step 2: AD COPY [n02-visual-marketing-hub]
  - Action: Write full ad copy (hook + body + CTA) for each format — 3 A/B variants
  - Apply: AIDA/PAS formula per platform best practices
  - Output: ad_copy_{mission}.md
  - Signal: copy_complete

Step 3: COMPILE + COMMIT [n02-visual-marketing-hub]
  - Validate: CTA specificity, readability check, A/B variant count
  - Compile + Commit: git commit -m "[N02] ad campaign copy — {mission}"
  - Signal: copy_complete
```

### Workflow C2: Email Sequence

**Goal**: Produce 5-email sequence with subject lines and body copy
**Input required**: Audience, goal type, product/offer
**Output**: Complete email sequence with A/B subject line variants

#### Steps

```
Step 1: SEQUENCE PLAN + COPY [n02-visual-marketing-hub]
  - Action: Map email sequence strategy + write all 5 emails
  - Include: subject line variants, preview text, body copy, CTAs
  - Apply: Formula-based copy per email purpose
  - Output: email_sequence_{mission}.md
  - Signal: copy_complete

Step 2: COMPILE + COMMIT [n02-visual-marketing-hub]  
  - Validate: readability, CTA specificity, funnel stage flow
  - Compile + Commit: git commit -m "[N02] email sequence — {mission}"
  - Signal: copy_complete
```

---

## DUAL MODE Workflow

### Workflow D1: Integrated Landing Page (Visual + Copy)

**Goal**: Build complete landing page where copy and visual work together seamlessly
**Input required**: Product, audience, funnel stage, copy formula, design style
**Output**: Full HTML page with embedded persuasive copy using proper visual hierarchy

#### Steps

```
Step 1: DUAL PLANNING [n02-visual-marketing-hub]
  - Action: Plan copy formula integration with visual hierarchy
  - Define: how PAS/AIDA structure maps to F/Z-pattern layout
  - Output: dual_plan_{mission}.md
  - Signal: plan_complete

Step 2: COPY GENERATION [n02-visual-marketing-hub]
  - Action: Write persuasive copy following chosen formula
  - Include: 3 headline variants, benefit blocks, CTAs
  - Output: copy_content_{mission}.md
  - Signal: copy_ready

Step 3: VISUAL INTEGRATION [n02-visual-marketing-hub]
  - Action: Build HTML page with copy embedded in semantic tags
  - Ensure: headlines in h1-h6, CTAs as button components, responsive flow
  - Apply: Tailwind styling that enhances copy readability
  - Output: integrated_page_{mission}.md
  - Depends on: Step 2
  - Signal: visual_ready

Step 4: DUAL VALIDATION + COMPILE [n02-visual-marketing-hub]
  - Validate: BOTH visual gates (Lighthouse >= 90) AND copy gates (readability, CTA)
  - Test: copy-visual integration quality, hierarchy supporting persuasion
  - Compile + Commit: git commit -m "[N02] integrated landing page — {mission}"
  - Signal: dual_complete
```

---

## Error Handling

### Mode-Aware Error Handling

**VISUAL Mode Failures**:
- **Lighthouse < 90**: optimize images, minify CSS, retry once
- **W3C validation errors**: fix HTML structure, retry with corrected markup  
- **Accessibility failures**: add ARIA labels, improve contrast, fix keyboard nav
- **Responsive failures**: adjust breakpoints, test on multiple devices

**COPY Mode Failures**:
- **Quality gate fails** (score < 8.0): return to copy step, apply F6 retry, max 2 revisions
- **Readability fails** (Flesch < target): simplify sentences, remove jargon, retry
- **CTA too generic**: rewrite with benefit-first template, retry

**DUAL Mode Failures**:
- **Copy-visual mismatch**: realign visual hierarchy with copy structure
- **Integration quality low**: improve semantic HTML for copy elements
- **Either dimension fails**: apply mode-specific fixes above

**Universal Failures**:
- **Step fails completely**: retry once with revised prompt; if still fail, signal `workflow_error` to N07
- **MCP unavailable**: proceed with local tools; browser MCP → manual validation, markitdown → formula-based KC
- **Model upgrade needed**: switch to Opus for complex HTML tasks automatically

## Signals

| Signal | Emitter | Meaning |
|--------|---------|---------|
| **visual_complete** | n02-visual-marketing-hub | HTML/CSS deliverable saved, Lighthouse validated, compiled, committed |
| **copy_complete** | n02-visual-marketing-hub | Copy deliverable saved, readability checked, compiled, committed |
| **dual_complete** | n02-visual-marketing-hub | Integrated page saved, both visual AND copy gates passed, committed |
| **workflow_error** | n02-visual-marketing-hub | Unrecoverable failure in any mode, escalate to N07 |
| **mode_detected** | n02-visual-marketing-hub | Workflow routing complete, mode identified for execution |

## Quality Gate Integration

- **VISUAL workflows**: Must pass V01-V09 gates (Lighthouse, W3C, a11y, responsive, tokens)
- **COPY workflows**: Must pass C01-C05 gates (funnel stage, CTA, headlines, readability, hook)  
- **DUAL workflows**: Must pass ALL visual + copy gates + integration quality checks (SD01-SD03)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_dr_visual_frontend_marketing]] | related | 0.56 |
| [[p08_ac_visual_frontend_marketing]] | upstream | 0.53 |
| [[p03_ap_visual_frontend_marketing]] | upstream | 0.53 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.48 |
| [[p03_sp_visual_frontend_marketing]] | upstream | 0.44 |
| [[p07_sr_visual_frontend_marketing]] | upstream | 0.39 |
| [[p11_qg_visual_frontend_marketing]] | upstream | 0.36 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.36 |
| [[landing-page-builder]] | upstream | 0.31 |
| [[spec_n02_visual_frontend_engineer]] | upstream | 0.31 |
