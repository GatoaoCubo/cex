---
id: p03_pt_visual_frontend_marketing
kind: prompt_template
pillar: P03
title: Visual Frontend + Marketing Production Template
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
variables:
  # Universal Variables
  - name: mode
    type: string
    required: true
    default: null
    description: VISUAL | COPY | DUAL
  - name: product_name
    type: string
    required: true
    default: null
    description: Product or service being marketed or built
    
  # Copy Mode Variables
  - name: audience_segment
    type: string
    required: false
    default: null
    description: Target audience — who reads this copy (job title, situation, pain)
  - name: funnel_stage
    type: string
    required: false
    default: null
    description: awareness | consideration | decision
  - name: key_benefit
    type: string
    required: false
    default: null
    description: The single most important benefit — outcome the reader gets
  - name: formula
    type: string
    required: false
    default: AIDA
    description: Copywriting formula — AIDA | PAS | BAB | 4U | FAB
  - name: channel
    type: string
    required: false
    default: null
    description: Where copy will appear — facebook_ad | google_ad | email | landing_page | linkedin | instagram
  - name: cta_action
    type: string
    required: false
    default: null
    description: Desired action after reading — start_trial | book_call | download | buy | subscribe
  - name: brand_voice_notes
    type: string
    required: false
    default: neutral
    description: Tone notes — casual, professional, bold, empathetic; banned words if any
  - name: word_limit
    type: integer
    required: false
    default: 150
    description: Maximum word count for the body copy
    
  # Visual Mode Variables
  - name: component_type
    type: string
    required: false
    default: null
    description: landing_page | hero_section | form | card | button | navigation | dashboard | email_template
  - name: layout_pattern
    type: string
    required: false
    default: f_pattern
    description: f_pattern | z_pattern | grid | single_column | two_column
  - name: color_scheme
    type: string
    required: false
    default: codexa
    description: codexa | neutral | brand | custom (uses CODEXA design tokens)
  - name: responsive_breakpoints
    type: string
    required: false
    default: mobile_first
    description: mobile_first | desktop_down | tablet_focus
  - name: dark_mode
    type: boolean
    required: false
    default: true
    description: Include dark mode support
  - name: accessibility_level
    type: string
    required: false
    default: AA
    description: WCAG level — A | AA | AAA
  - name: animation_level
    type: string
    required: false
    default: subtle
    description: none | subtle | moderate | rich (Framer Motion patterns)
variable_syntax: mustache
composable: true
domain: visual_frontend_engineering_and_copywriting
quality: 9.2
tags: [prompt_template, visual-frontend, marketing, html, tailwind, copy, N02, P03]
tldr: Dual-mode template — generates production HTML/CSS with Tailwind + shadcn/ui OR persuasive copy with formulas, based on mode selection.
keywords: [html, frontend, tailwind, component, responsive, a11y, copy, ad, headline, CTA, funnel, formula, AIDA, PAS, landing_page]
density_score: 0.96
related:
  - p03_ap_visual_frontend_marketing
  - p08_ac_visual_frontend_marketing
  - p12_dr_visual_frontend_marketing
  - p03_sp_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - p12_wf_visual_frontend_marketing
  - p07_sr_visual_frontend_marketing
  - p11_qg_visual_frontend_marketing
  - spec_n02_visual_frontend_engineer
  - spec_n02_part2
---

# Visual Frontend + Marketing Production Template

## Purpose

This dual-mode template drives N02 to produce either:
- **VISUAL MODE**: Production HTML/CSS with Tailwind + shadcn/ui components
- **COPY MODE**: Formula-matched persuasive copy with A/B variants  
- **DUAL MODE**: Integrated pages where copy is embedded in visual hierarchy

Reusable across all visual and copy tasks — components, landing pages, ads, emails.

## Variables Table

### Universal Variables
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| mode | string | YES | — | VISUAL / COPY / DUAL |
| product_name | string | YES | — | Product/service being built or marketed |

### Copy Mode Variables (when mode = COPY or DUAL)
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| audience_segment | string | YES* | — | Target reader — their role, situation, pain |
| funnel_stage | string | YES* | — | awareness / consideration / decision |
| key_benefit | string | YES* | — | The ONE outcome the reader cares about |
| formula | string | NO | AIDA | Copywriting formula: AIDA/PAS/BAB/4U/FAB |
| channel | string | YES* | — | facebook_ad / email / landing_page / etc. |
| cta_action | string | NO | null | Desired action: start_trial / book_call / etc. |
| brand_voice_notes | string | NO | neutral | Tone guidance and banned words |
| word_limit | integer | NO | 150 | Max body copy words |

### Visual Mode Variables (when mode = VISUAL or DUAL)  
| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| component_type | string | YES* | — | landing_page / hero_section / form / card / button / etc. |
| layout_pattern | string | NO | f_pattern | f_pattern / z_pattern / grid / single_column |
| color_scheme | string | NO | codexa | codexa / neutral / brand / custom |
| responsive_breakpoints | string | NO | mobile_first | mobile_first / desktop_down / tablet_focus |
| dark_mode | boolean | NO | true | Include dark mode support |
| accessibility_level | string | NO | AA | WCAG level — A / AA / AAA |
| animation_level | string | NO | subtle | none / subtle / moderate / rich |

*Required when mode includes that dimension

## Template Bodies

### VISUAL Mode Template
```
You are N02 — Visual Frontend Engineer + Marketing Nucleus.

MODE: VISUAL
TASK: Build {{component_type}} for {{product_name}}.

VISUAL SPECS:
- COMPONENT TYPE: {{component_type}}
- LAYOUT PATTERN: {{layout_pattern}}
- COLOR SCHEME: {{color_scheme}}
- RESPONSIVE: {{responsive_breakpoints}}
- DARK MODE: {{dark_mode}}
- ACCESSIBILITY: WCAG {{accessibility_level}}
- ANIMATION: {{animation_level}}

REQUIREMENTS:
✅ Semantic HTML5 structure
✅ Tailwind CSS utilities only (NO hardcoded hex)
✅ shadcn/ui component patterns where applicable
✅ WCAG {{accessibility_level}} compliance (4.5:1+ contrast)
✅ Mobile-first responsive design
✅ Dark mode with proper tokens
✅ Lighthouse performance target: 90+

DELIVER:
1. HTML STRUCTURE — complete semantic markup
2. TAILWIND CLASSES — utility-first styling
3. COMPONENT PROPS — if applicable (shadcn/ui patterns)
4. ACCESSIBILITY FEATURES — ARIA labels, focus states
5. RESPONSIVE BEHAVIOR — sm:, md:, lg: breakpoints
6. DARK MODE VARIANTS — dark: prefix classes
7. TEST NOTES — visual validation checklist

OUTPUT FORMAT:
```html
---
component: {{component_type}}
responsive: true
a11y_compliant: true
dark_mode: {{dark_mode}}
lighthouse_target: 90+
---

<!DOCTYPE html>
<html lang="en" class="h-full">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{product_name}}</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="min-h-screen bg-background text-foreground">
    <!-- Component implementation -->
  </body>
</html>
```

## Visual Test Checklist
- [ ] W3C HTML validation passed
- [ ] Lighthouse score >= 90
- [ ] Contrast ratio >= 4.5:1
- [ ] Responsive on mobile/tablet/desktop
- [ ] Dark mode toggle works
- [ ] Keyboard navigation functional
```

### COPY Mode Template
```
You are N02 — Visual Frontend Engineer + Marketing Nucleus.

MODE: COPY
TASK: Write {{channel}} copy for {{product_name}}.

COPY SPECS:
- AUDIENCE: {{audience_segment}}
- FUNNEL STAGE: {{funnel_stage}}
- KEY BENEFIT: {{key_benefit}}
- FORMULA: {{formula}}
- CTA ACTION: {{cta_action}}
- BRAND VOICE: {{brand_voice_notes}}
- WORD LIMIT: {{word_limit}} words max for body

DELIVER:
1. HEADLINES — 3 variants labeled V1, V2, V3
   - Score each with 4U: Useful / Urgent / Unique / Ultra-specific
   - Mark recommended variant with ★

2. BODY COPY — apply {{formula}} structure
3. CTA — 2 variants (specific + benefit-first)
4. TEST NOTE — priority A/B test recommendation

OUTPUT FORMAT:
## Headline Variants
V1: ...
V2: ...
V3: ★ (recommended)

## Body Copy
[{{formula}}-structured body, max {{word_limit}} words]

## CTA Options
Primary: ...
Alternate: ...

## TEST
[copy optimization guidance]
```

### DUAL Mode Template  
```
You are N02 — Visual Frontend Engineer + Marketing Nucleus.

MODE: DUAL (Visual + Copy Integration)
TASK: Build {{component_type}} with integrated {{formula}} copy for {{product_name}}.

INTEGRATION SPECS:
- VISUAL: {{component_type}} with {{layout_pattern}} layout
- COPY: {{formula}} structure for {{funnel_stage}} audience
- HIERARCHY: Embed headlines in proper h1-h6 tags
- BUTTONS: Transform CTAs into styled components

DELIVER:
1. INTEGRATED HTML — copy embedded in visual hierarchy
2. HEADLINE VARIANTS — 3 variants as actual h1/h2 tags  
3. STYLED CTAs — button components with hover states
4. RESPONSIVE COPY — text scales with breakpoints
5. DUAL TEST NOTES — both visual and copy optimization

OUTPUT FORMAT:
```html
---
page: {{component_type}}_{{formula}}
copy_formula: {{formula}}
funnel_stage: {{funnel_stage}}
responsive: true
a11y_compliant: true
lighthouse_target: 90+
---

<!DOCTYPE html>
<!-- Complete page with integrated copy + visual -->
</html>
```

## Test Checklist (Dual)
VISUAL: [W3C, Lighthouse, contrast, responsive]
COPY: [headlines, CTA effectiveness, funnel alignment]
```

## Pattern Expansion Reference

### Visual Component Patterns

When `{{component_type}}` = landing_page:
```html
<main class="min-h-screen bg-background">
  <section class="container mx-auto px-4 py-16"> <!-- Hero -->
    <div class="grid gap-8 lg:grid-cols-2"> <!-- F-pattern layout -->
      <div class="space-y-6">
        <h1 class="text-4xl font-bold tracking-tight text-foreground lg:text-5xl">
          <!-- Primary headline -->
        </h1>
        <p class="text-xl text-muted-foreground">
          <!-- Subheadline -->
        </p>
        <button class="bg-primary text-primary-foreground hover:bg-primary/90 px-6 py-3 rounded-md font-medium">
          <!-- Primary CTA -->
        </button>
      </div>
      <div class="lg:order-first"> <!-- Visual element --> </div>
    </div>
  </section>
  <!-- Additional sections: features, testimonials, pricing, FAQ -->
</main>
```

When `{{component_type}}` = form:
```html
<form class="space-y-6 bg-card p-6 rounded-lg border border-border">
  <div class="space-y-2">
    <label for="email" class="text-sm font-medium text-foreground">
      Email
    </label>
    <input 
      type="email" 
      id="email" 
      class="w-full px-3 py-2 border border-input bg-background text-foreground rounded-md focus:ring-2 focus:ring-primary focus:border-transparent"
      required
    >
  </div>
  <button type="submit" class="w-full bg-primary text-primary-foreground hover:bg-primary/90 py-2 rounded-md font-medium">
    <!-- Submit CTA -->
  </button>
</form>
```

### Copy Formula Reference

When `{{formula}}` = AIDA, expand body structure as:
```
ATTENTION: [Bold claim or question — reader's desire or fear, 1 sentence]
INTEREST: [Develop the problem or opportunity — why it matters now, 2–3 sentences]
DESIRE: [Transformation — what life looks like after the solution, benefit stack, 2–3 sentences]
ACTION: [CTA — specific + benefit-first, 1 sentence]
```

When `{{formula}}` = PAS, expand body structure as:
```
PROBLEM: [Name exact pain — reader already feels this, 1–2 sentences]
AGITATE: [Deepen pain — consequences, missed opportunities, cost of inaction, 2–3 sentences]
SOLUTION: [Present product as relief — not features, transformation, 2–3 sentences]
```

When `{{formula}}` = BAB, expand body structure as:
```
BEFORE: [Current painful state — reader's reality right now, 1–2 sentences]
AFTER: [Desired future state — what they want, vivid and specific, 1–2 sentences]
BRIDGE: [Your product/service as the mechanism from Before to After, 2–3 sentences]
```

## Quality Gates Applied

### Visual Mode Gates
| Gate | Check |
|------|-------|
| V01 | Lighthouse Performance >= 90 |
| V02 | WCAG AA accessibility compliance (4.5:1+ contrast) |
| V03 | W3C HTML validation (0 errors) |
| V04 | Mobile-first responsive design functional |
| V05 | Dark mode implementation present |
| V06 | Zero hardcoded hex colors (#HEXCODE prohibited) |
| V07 | Semantic HTML5 structure used |
| V08 | Tailwind utility classes only |

### Copy Mode Gates
| Gate | Check |
|------|-------|
| C01 | CTA is specific and benefit-first (not "Click here") |
| C02 | >= 3 headline variants with 4U scores |
| C03 | Hook opens in first 10 words |
| C04 | CTA names benefit AND action |
| C05 | Funnel stage declared in output header |
| C06 | Formula structure properly applied |

### Dual Mode Gates
| Gate | Check |
|------|-------|
| D01 | All Visual gates (V01-V08) passed |
| D02 | All Copy gates (C01-C06) passed |
| D03 | Copy properly integrated into visual hierarchy |
| D04 | Headlines use semantic h1-h6 tags |
| D05 | CTAs become styled button components |

## Filled Examples

### VISUAL Mode Example

**Variables:**
```yaml
mode: "VISUAL"
product_name: "CopyFlow AI"
component_type: "hero_section"
layout_pattern: "f_pattern"
color_scheme: "codexa"
responsive_breakpoints: "mobile_first"
dark_mode: true
accessibility_level: "AA"
animation_level: "subtle"
```

**Rendered Output:**
```html
---
component: hero_section
responsive: true
a11y_compliant: true
dark_mode: true
lighthouse_target: 90+
---

<section class="container mx-auto px-4 py-16">
  <div class="grid gap-8 lg:grid-cols-2">
    <div class="space-y-6">
      <h1 class="text-4xl font-bold tracking-tight text-foreground lg:text-5xl">
        CopyFlow AI
      </h1>
      <p class="text-xl text-muted-foreground">
        Draft faster. Write better. Meet deadlines.
      </p>
      <button class="bg-primary text-primary-foreground hover:bg-primary/90 px-6 py-3 rounded-md font-medium transition-colors">
        Start Free Trial
      </button>
    </div>
  </div>
</section>
```

### DUAL Mode Example

**Variables:**
```yaml
mode: "DUAL"
product_name: "CopyFlow AI"
component_type: "landing_page"
audience_segment: "Freelance copywriters who miss deadlines"
funnel_stage: "consideration"
key_benefit: "Produce first drafts 3x faster"
formula: "PAS"
layout_pattern: "f_pattern"
color_scheme: "codexa"
```

**Rendered Output:**
```html
---
page: landing_page_PAS
copy_formula: PAS
funnel_stage: consideration
responsive: true
a11y_compliant: true
lighthouse_target: 90+
---

<main class="min-h-screen bg-background">
  <section class="container mx-auto px-4 py-16">
    <div class="grid gap-8 lg:grid-cols-2">
      <div class="space-y-6">
        <!-- PROBLEM: Embedded in headline -->
        <h1 class="text-4xl font-bold tracking-tight text-foreground lg:text-5xl">
          Your Deadline Was Yesterday. CopyFlow Gets You There.
        </h1>
        <!-- AGITATE: Subheadline -->
        <p class="text-xl text-muted-foreground">
          Late fees. Stressed clients. Evenings lost. Your reputation quietly eroding.
        </p>
        <!-- SOLUTION: Body text -->
        <p class="text-lg text-foreground">
          CopyFlow AI drafts your first copy block in 20 minutes flat. 
          You edit like the expert you are — instead of starting from scratch.
        </p>
        <!-- ACTION: Styled CTA -->
        <button class="bg-primary text-primary-foreground hover:bg-primary/90 px-6 py-3 rounded-md font-medium transition-colors">
          Start My Free 14-Day Trial
        </button>
      </div>
    </div>
  </section>
</main>
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ap_visual_frontend_marketing]] | related | 0.59 |
| [[p08_ac_visual_frontend_marketing]] | downstream | 0.55 |
| [[p12_dr_visual_frontend_marketing]] | downstream | 0.53 |
| [[p03_sp_visual_frontend_marketing]] | related | 0.52 |
| [[p02_agent_visual_frontend_marketing]] | upstream | 0.50 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.47 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.44 |
| [[p11_qg_visual_frontend_marketing]] | downstream | 0.42 |
| [[spec_n02_visual_frontend_engineer]] | downstream | 0.34 |
| [[spec_n02_part2]] | downstream | 0.34 |
