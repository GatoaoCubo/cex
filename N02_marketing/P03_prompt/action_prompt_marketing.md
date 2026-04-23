---
id: p03_ap_visual_frontend_marketing
kind: action_prompt
pillar: P03
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
title: N02 Action Prompts — Visual Frontend + Marketing Quick Execution
action: Execute visual or copy task directly with minimal input
input_required:
  - "mode: string — VISUAL | COPY | DUAL"
  - "task_type: string — which specific task to run"
  - "product: string — product or service name"
output_expected: Production HTML/CSS with Tailwind OR copy deliverable with A/B variants OR integrated page
purpose: Ready-to-run action prompts for dual-role N02 — 6 visual tasks + 4 copy tasks, no template setup needed.
steps_count: 10
timeout: 90s
edge_cases:
  - "No color scheme specified — default to CODEXA tokens"
  - "No accessibility level — default to WCAG AA"
  - "No brand voice provided — use neutral professional tone"
  - "No funnel stage specified — default to consideration"
  - "HTML exceeds complexity — break into smaller components"
constraints:
  - VISUAL: NEVER use hardcoded hex colors, ALWAYS target Lighthouse 90+, ALWAYS include dark mode
  - COPY: NEVER write generic CTAs, ALWAYS produce 3 headline variants minimum
  - DUAL: NEVER skip integration between copy and visual hierarchy
domain: visual_frontend_engineering_and_copywriting
quality: 9.1
tags: [action_prompt, visual-frontend, marketing, html, tailwind, copy, N02, quick_execution]
tldr: 10 ready-to-run N02 action prompts — 6 visual (landing page, components, responsive) + 4 copy (ads, headlines, emails) + dual integration.
density_score: 0.96
related:
  - p02_agent_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p03_pt_visual_frontend_marketing
  - p07_sr_visual_frontend_marketing
  - p11_qg_visual_frontend_marketing
  - landing-page-builder
  - spec_n02_part2
---

# N02 Action Prompts — Visual Frontend + Marketing Quick Execution

## Context

Ten tasks run most often in dual-role N02. These action prompts are pre-wired — paste the
relevant prompt, fill the `[BRACKETS]`, and get a complete deliverable.
No template setup needed. Each follows 8F pipeline internally with visual gates OR copy gates.

---

## VISUAL MODE Actions

### Action V1: Build Complete Landing Page

**Use when**: Need a full production landing page with multiple sections.

```
MODE: VISUAL
TASK: Build a complete landing page with Tailwind CSS.
PRODUCT: [name + what it does]
LAYOUT: [f_pattern | z_pattern | single_column]
SECTIONS: [hero, features, testimonials, pricing, faq, cta_final — select which to include]
COLOR_SCHEME: [codexa | neutral | brand]
CTA_ACTION: [start_trial | book_demo | download | buy]

DELIVER:
- Complete HTML page with semantic structure
- Mobile-first responsive design (sm:, md:, lg: breakpoints)
- Dark mode implementation with proper tokens
- WCAG AA accessibility compliance
- Tailwind utility classes only (zero hardcoded hex)
- Lighthouse performance optimization
- Component breakdown (which shadcn/ui patterns used)
- TEST: visual validation checklist
```

### Action V2: Create shadcn/ui Component

**Use when**: Need a reusable component following shadcn/ui patterns.

```
MODE: VISUAL
TASK: Create a [button | card | form | dialog | dropdown | input] component.
COMPONENT_TYPE: [specify type]
VARIANT_COUNT: [how many style variants needed]
PROPS: [list any specific props or configuration]
ACCESSIBILITY: [basic | enhanced — keyboard nav, screen reader]

DELIVER:
- Base component HTML with Tailwind classes
- All variants (primary, secondary, destructive, etc.)
- Proper ARIA labels and accessibility features
- Hover, focus, and active states
- Dark mode variants
- Usage examples (3 different contexts)
- Component API documentation
- TEST: accessibility and visual QA checklist
```

### Action V3: Make Component/Page Responsive

**Use when**: Need to add responsive behavior to existing design.

```
MODE: VISUAL
TASK: Add responsive design to existing HTML.
EXISTING_HTML: [paste current HTML or describe component]
BREAKPOINTS: [which breakpoints to target: sm | md | lg | xl | 2xl]
PRIORITY: [mobile_first | desktop_down]
LAYOUT_CHANGES: [describe how layout should adapt]

DELIVER:
- Responsive HTML with Tailwind breakpoint classes
- Mobile-first methodology applied
- Typography scaling across devices
- Navigation patterns for mobile (hamburger, drawer, etc.)
- Image optimization and lazy loading
- Touch-friendly interactions on mobile
- Responsive testing checklist
- TEST: cross-device validation steps
```

---

## COPY MODE Actions

### Action C1: Optimize Headlines (10 Variants)

**Use when**: Need multiple headline options for landing page, ad, or email.

```
MODE: COPY
TASK: Generate 10 headline variants and score them.
PRODUCT: [name]
AUDIENCE: [description]
FUNNEL_STAGE: [awareness | consideration | decision]
KEY_BENEFIT: [single outcome]

DELIVER:
- 10 headline variants using these formulas:
  - 2× AIDA hook
  - 2× PAS opener  
  - 2× 4U scored
  - 2× Number + Outcome
  - 2× "How to [benefit] without [pain]"
- Score each: Useful/Urgent/Unique/Ultra-specific (1–3 each)
- Top 3 ranked by total score
- TEST: which to A/B test first and why
```

### Action C2: Write Facebook/Instagram Ad

**Use when**: Need paid social ad with hook, body, and CTA.

```
MODE: COPY
TASK: Write Facebook/Instagram ad.
PRODUCT: [product name and description]
AUDIENCE: [who they are, pain/desire]
FUNNEL_STAGE: [awareness | consideration | decision]
KEY_BENEFIT: [the ONE outcome they get]
BRAND_VOICE: [casual/professional/bold + banned words]

DELIVER:
- 3 headline variants (V1, V2, V3 with 4U scores, ★ recommended)
- Primary text (hook + PAS/AIDA body, 90–125 words)
- CTA button text (2 options, specific + benefit-first)
- Character count validation
- TEST note (what to A/B test first)
```

---

## DUAL MODE Actions

### Action D1: Build Landing Page with Integrated Copy

**Use when**: Need complete page where copy and visual work together.

```
MODE: DUAL
TASK: Build landing page with integrated persuasive copy.
PRODUCT: [name + description]
AUDIENCE: [target visitor description]
FUNNEL_STAGE: [awareness | consideration | decision]
COPY_FORMULA: [AIDA | PAS | BAB]
LAYOUT_PATTERN: [f_pattern | z_pattern]
KEY_BENEFIT: [transformation they want]

DELIVER:
- Complete HTML page with embedded copy structure
- Headlines as proper h1-h6 semantic tags
- Copy formulas applied in visual hierarchy
- CTAs as styled button components with hover states
- F/Z-pattern layout supporting copy flow
- Responsive text scaling
- Dark mode for both visual and copy readability
- DUAL TEST: both copy variants and visual elements
```

### Action D2: Convert Copy to Styled HTML Component

**Use when**: Have existing copy that needs visual implementation.

```
MODE: DUAL
TASK: Convert plain text copy into styled HTML component.
EXISTING_COPY: [paste the copy text]
COMPONENT_TYPE: [hero | card | email | ad_creative]
COPY_HIERARCHY: [which parts are headlines vs body vs CTA]
BRAND_TOKENS: [which design system to apply]

DELIVER:
- HTML structure with copy embedded in semantic tags
- Tailwind styling that enhances readability
- Typography hierarchy supporting copy formula
- Visual emphasis on key copy elements (bolding, sizing)
- CTA transformation into button components
- Mobile-optimized copy display
- Copy-visual integration assessment
- TEST: readability and conversion optimization
```

---

## Validation Checklists

### VISUAL Mode Validation
| Check | Rule |
|-------|------|
| HTML validation | W3C validator passes (0 errors) |
| Lighthouse score | Performance >= 90 |
| Accessibility | WCAG AA compliance (4.5:1+ contrast) |
| Responsive design | Mobile-first breakpoints working |
| Color tokens | Zero hardcoded hex colors (#HEXCODE prohibited) |
| Dark mode | Proper dark: variants implemented |
| Semantic markup | Proper HTML5 structure used |

### COPY Mode Validation
| Check | Rule |
|-------|------|
| CTA specificity | Not "Click here" / "Learn more" — must name benefit |
| Headline variants | Minimum 3 per task |
| Funnel stage | Declared in every deliverable |
| A/B TEST note | Required at end of every output |
| Word limits | Respected per channel |
| Hook placement | First 10 words create curiosity/urgency |

### DUAL Mode Validation
| Check | Rule |
|-------|------|
| All visual checks | V1-V7 must pass |
| All copy checks | C1-C6 must pass |
| Integration quality | Copy embedded in proper visual hierarchy |
| Semantic headlines | Headlines use h1-h6 tags, not just styling |
| CTA components | CTAs become button elements with hover states |

---

## Edge Cases & Troubleshooting

### VISUAL Mode Edge Cases
| Situation | Action |
|-----------|--------|
| No color scheme specified | Default to CODEXA design tokens |
| Component too complex | Break into smaller sub-components |
| Accessibility requirements unclear | Default to WCAG AA minimum |
| No layout pattern specified | Use F-pattern for landing pages, grid for dashboards |
| Browser compatibility needed | Use Tailwind utilities (broad support) |

### COPY Mode Edge Cases
| Situation | Action |
|-----------|--------|
| No brand voice provided | Write in neutral professional; flag "[BRAND VOICE CARD RECOMMENDED]" |
| No funnel stage specified | Default to consideration; note assumption at output top |
| Copy exceeds word limit | Trim benefits block; keep hook and CTA intact |
| Conflicting CTAs requested | Pick ONE; note choice and reason |
| B2B vs B2C tone conflict | B2B aims Flesch >= 50, B2C aims Flesch >= 65 |

### DUAL Mode Edge Cases
| Situation | Action |
|-----------|--------|
| Copy and visual style mismatch | Adapt visual hierarchy to support copy flow |
| Technical content in casual design | Balance: professional typography with accessible styling |
| Long copy in mobile layout | Implement progressive disclosure, accordion patterns |
| Multiple CTAs needed | Use primary/secondary visual hierarchy, test separately |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.53 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.50 |
| [[p12_dr_visual_frontend_marketing]] | downstream | 0.49 |
| [[p03_sp_visual_frontend_marketing]] | related | 0.49 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.47 |
| [[p03_pt_visual_frontend_marketing]] | related | 0.47 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.43 |
| [[p11_qg_visual_frontend_marketing]] | downstream | 0.37 |
| [[landing-page-builder]] | downstream | 0.34 |
| [[spec_n02_part2]] | downstream | 0.32 |
