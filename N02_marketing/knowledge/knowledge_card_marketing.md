---
id: p01_kc_visual_frontend_marketing
kind: knowledge_card
pillar: P01
title: Visual Frontend Engineering + Marketing — Dual Knowledge Card
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n02_visual_frontend_marketing
domain: visual_frontend_engineering_and_copywriting
quality: null
tags: [knowledge_card, visual-frontend, marketing, html, tailwind, copywriting, campaigns, N02]
tldr: Dual-role knowledge — 10 frontend KCs (Tailwind, shadcn, a11y, responsive, typography, tokens) + copywriting formulas — for N02 Visual Frontend Engineer.
when_to_use: Load before any visual, copy, or dual-mode task. Reference frontend KCs for HTML generation, copy formulas for persuasion, integration patterns for dual work.
keywords: [html, frontend, tailwind, shadcn, responsive, a11y, copywriting, AIDA, PAS, headline, CTA, funnel, landing page, component, visual hierarchy]
long_tails:
  - How to build responsive landing page with Tailwind CSS
  - How to integrate persuasive copy into visual hierarchy
  - WCAG AA accessibility compliance with shadcn/ui components
  - Mobile-first responsive design patterns with Tailwind
  - How to write high-converting headlines embedded in semantic HTML
  - Design token architecture for consistent styling
axioms:
  - ALWAYS use design tokens, NEVER hardcode hex colors (#HEXCODE prohibited)
  - ALWAYS build mobile-first responsive with proper breakpoints
  - ALWAYS target Lighthouse 90+ performance and WCAG AA accessibility
  - ALWAYS identify funnel stage before writing copy
  - ALWAYS lead with reader's desire, not product features
  - NEVER use vague CTAs — specificity increases conversion
linked_artifacts:
  primary: p02_agent_visual_frontend_marketing
  related: [p03_sp_visual_frontend_marketing, p03_pt_visual_frontend_marketing]
  frontend_kcs: [kc_tailwind_patterns, kc_shadcn_radix_patterns, kc_accessibility_a11y, kc_responsive_layouts, kc_typography_web, kc_color_theory_applied, kc_visual_hierarchy, kc_css_animation_micro, kc_email_html_responsive, kc_html_component_library]
density_score: 0.96
data_source: internal_distillation_and_frontend_kcs
---

# Visual Frontend Engineering + Marketing — Dual Knowledge Card

## Quick Reference

```yaml
# Dual-Role Configuration
domain: visual_frontend_engineering_and_copywriting
nucleus: N02
model: claude-sonnet-4-6 (+ claude-opus-4-6 fallback for HTML-heavy)
cli: claude (Anthropic subscription)
mcps: [markitdown, puppeteer_browser]

# Visual Frontend Capabilities
frontend_stack: [tailwind_css, shadcn_ui, radix_primitives, html5_semantic]
design_tokens: [primitives, semantic_codexa, component_level]
typography: [geist_variable, inter, jetbrains_mono]
responsive: [mobile_first, sm_640px, md_768px, lg_1024px, xl_1280px, 2xl_1536px]
accessibility: [wcag_aa_minimum, 4.5_contrast_ratio, semantic_markup]
performance: [lighthouse_90_plus, w3c_valid, lazy_loading]

# Copywriting Capabilities  
copy_formulas: [AIDA, PAS, BAB, 4U, FAB]
funnel_stages: [awareness, consideration, decision]
channels: [ads, email, landing_page, social, brand, components]

# Dual Integration
modes: [VISUAL, COPY, DUAL]
integration: [copy_in_hierarchy, semantic_headlines, styled_ctas]
```

## Frontend Knowledge Base (10 Core KCs)

### Design & Layout KCs
- **`kc_tailwind_patterns`**: Utility-first patterns, JIT mode, configuration strategies
- **`kc_visual_hierarchy`**: F/Z-pattern layouts, typography scale, whitespace, focal points
- **`kc_responsive_layouts`**: Mobile-first breakpoints, fluid grids, container queries
- **`kc_typography_web`**: 3-font system (Geist+Inter+JBMono), hierarchy, readability

### Component & Styling KCs
- **`kc_shadcn_radix_patterns`**: Component composition, variant patterns, accessibility built-in
- **`kc_html_component_library`**: Semantic markup, reusable patterns, API design
- **`kc_color_theory_applied`**: CODEXA palette, contrast ratios, dark mode tokens
- **`kc_css_animation_micro`**: Framer Motion patterns, hover states, transitions

### Accessibility & Performance KCs
- **`kc_accessibility_a11y`**: WCAG AA compliance, ARIA labels, keyboard navigation
- **`kc_email_html_responsive`**: Inline CSS, client compatibility, responsive email templates

### Frontend Integration Patterns
```
Copy → Visual Integration:
1. Headlines → Semantic h1-h6 tags with Tailwind typography classes
2. CTAs → Button components with hover/focus states
3. Body copy → Proper p tags with responsive text scaling
4. Lists → ul/ol with Tailwind list styling
5. Forms → shadcn/ui form components with validation styling
```

## Visual Frontend Patterns

### Tailwind Design Token Usage
```css
/* NEVER use hardcoded colors */
❌ style="color: #50C878"
✅ class="text-codexa-accent"

/* Design token layers */
:root { --background: white; --foreground: black; } /* Primitives */
.codexa { --codexa-accent: #50C878; --codexa-surface-900: ...; } /* Semantic */
.sidebar { --sidebar-background: var(--codexa-surface-900); } /* Component */
```

### Responsive Patterns (Mobile-First)
```html
<!-- Base styles for mobile, then add breakpoints -->
<div class="grid gap-4 p-4 sm:gap-6 sm:p-6 lg:grid-cols-2 lg:gap-8">
  <div class="space-y-4">
    <!-- Content scales with device -->
    <h1 class="text-2xl font-bold sm:text-3xl lg:text-4xl">Mobile-First Headline</h1>
  </div>
</div>
```

### Accessibility Essentials
```html
<!-- Semantic structure with ARIA -->
<button 
  class="bg-primary text-primary-foreground hover:bg-primary/90 focus:ring-2 focus:ring-primary focus:ring-offset-2"
  aria-label="Start your free trial"
>
  Get Started
</button>

<!-- Form accessibility -->
<label for="email" class="text-sm font-medium">Email</label>
<input 
  id="email" 
  type="email" 
  class="border-input bg-background focus:ring-2 focus:ring-primary"
  required
  aria-describedby="email-error"
>
```

### Component Composition (shadcn/ui Style)
```typescript
// Button variants
const buttonVariants = {
  variant: {
    default: "bg-primary text-primary-foreground hover:bg-primary/90",
    destructive: "bg-destructive text-destructive-foreground hover:bg-destructive/90",
    outline: "border border-input hover:bg-accent hover:text-accent-foreground",
  },
  size: {
    default: "h-10 px-4 py-2",
    sm: "h-9 rounded-md px-3",
    lg: "h-11 rounded-md px-8",
  }
}
```

## DUAL Mode Integration Strategies

### Copy-to-Visual Mapping
| Copy Element | HTML Implementation | Tailwind Classes |
|-------------|-------------------|------------------|
| **Headlines** | h1, h2, h3 tags | `text-3xl font-bold tracking-tight` |
| **Subheadlines** | p with emphasis | `text-xl text-muted-foreground` |
| **CTAs** | button elements | `bg-primary text-primary-foreground hover:bg-primary/90` |
| **Body copy** | p tags in prose | `prose prose-gray dark:prose-invert` |
| **Bullet lists** | ul with icons | `space-y-2 text-sm` |

### Visual Formula Integration
```html
<!-- AIDA structure in HTML -->
<section class="container mx-auto px-4 py-16">
  <!-- ATTENTION: Hero headline -->
  <h1 class="text-4xl font-bold tracking-tight lg:text-5xl">
    Stop Losing Leads to Weak Landing Pages
  </h1>
  
  <!-- INTEREST: Problem development -->
  <p class="mt-6 text-xl text-muted-foreground">
    Every visitor that bounces is revenue walking out the door...
  </p>
  
  <!-- DESIRE: Benefit stack -->
  <div class="mt-12 grid gap-8 lg:grid-cols-3">
    <!-- Benefits in card layout -->
  </div>
  
  <!-- ACTION: CTA section -->
  <div class="mt-16 text-center">
    <button class="bg-primary text-primary-foreground hover:bg-primary/90 px-8 py-4 rounded-lg text-lg font-medium">
      Build My High-Converting Page
    </button>
  </div>
</section>
```

## Copywriting Formulas

### AIDA — Awareness → Interest → Desire → Action
Use for: cold traffic ads, email subject lines, landing page above-the-fold
```
A — Hook that grabs attention (bold claim, question, surprising stat)
I — Build interest with the problem or opportunity
D — Create desire with transformation story or benefit stack
A — CTA with single clear next step
```

### PAS — Problem → Agitate → Solution
Use for: Facebook ads, cold email, sales pages targeting pain-aware audiences
```
P — Name the exact pain point the reader already feels
A — Deepen it: consequences, missed opportunities, future if nothing changes
S — Present your solution as the relief
```

### BAB — Before → After → Bridge
Use for: testimonials structure, case study copy, social proof sections
```
Before: Reader's current state (problem, frustration, limitation)
After: Desired future state (what life looks like after solving it)
Bridge: Your product/service as the mechanism to cross
```

### 4U Headline Formula
Use for: all headlines. Score each dimension 1–3, aim for total >= 8.
```
Useful — Does it promise a benefit?
Urgent — Does it create time pressure or consequence for inaction?
Unique — Could only your offer say this?
Ultra-specific — Does it name a number, name, or concrete outcome?
```

### FAB — Features → Advantages → Benefits
Use for: product description copy, email body, landing page benefit section
```
Feature: What it IS (e.g., "AI-powered headline scorer")
Advantage: What it DOES (e.g., "scores 10 variants in 3 seconds")
Benefit: What it MEANS for reader (e.g., "you ship copy 2x faster")
```

## Headline Patterns (High CTR)

| Pattern | Example |
|---------|---------|
| Number + Outcome | "7 Headlines That Doubled Our Conversion Rate" |
| How to [Outcome] Without [Pain] | "How to Launch Ads Without Wasting Budget" |
| The [Secret/Method/System] | "The 3-Word CTA That Gets More Clicks" |
| Question with implied answer | "Still Writing Weak CTAs? This Changes Everything." |
| Specific result + timeframe | "Get 3x More Leads in 30 Days" |

## CTA Patterns

| Weak (Banned) | Strong (Use) | Why |
|---------------|-------------|-----|
| Click here | Get my free audit | Specific benefit |
| Learn more | See how it works (2 min) | Specificity + low friction |
| Submit | Yes, send my guide | First-person + desire |
| Buy now | Start my 14-day trial | Framing as start, not spend |
| Sign up | Join 4,000+ marketers | Social proof embedded |

## Funnel Stage Matrix

| Stage | Awareness | Consideration | Decision |
|-------|-----------|---------------|----------|
| Reader knows | Has a problem | Has a solution category | Has your brand |
| Goal | Stop the scroll | Build preference | Remove final objection |
| Formula | AIDA / hook | BAB / comparison | Offer + urgency |
| CTA | Soft (learn more) | Medium (see demo) | Hard (buy / start) |
| Tone | Curious, bold | Educational, credible | Confident, urgent |

## Brand Voice — 4 Dimensions

```
1. TONE: formal ←——→ casual (e.g., "We help" vs "Let's fix this")
2. VOCABULARY: technical ←——→ plain (e.g., "ROI optimization" vs "more sales")
3. PERSON: third-person ←——→ first-person (e.g., "the company" vs "we/you")
4. ENERGY: calm ←——→ bold (e.g., "reliable solution" vs "this changes everything")
```
For each client/product: score each dimension 1–5. Document 3 banned words + 3 signature phrases.

## Email Sequence Skeletons

### Cold Outreach (5-email)
1. Hook email — problem statement + social proof hook (no pitch)
2. Value email — one insight/tip relevant to their problem (no pitch)
3. Case study email — BAB story of a similar client
4. Offer email — clear pitch with CTA
5. Breakup email — creates urgency via absence ("Last email...")

### Nurture / Welcome (3-email)
1. Welcome — deliver promised lead magnet + brand story
2. Quick win — teach one thing they can apply today
3. Invitation — offer next step (trial, call, product)

## Production Flows

### VISUAL Mode Flow
```text
[Component intent] → [shadcn/ui pattern selection] → [HTML structure]
→ [Tailwind styling] → [Responsive breakpoints] → [A11y implementation]
→ [Dark mode variants] → [Lighthouse validation >= 90] → [Publish]
```

### COPY Mode Flow
```text
[Audience pain/desire] → [Formula selection] → [Hook draft]
→ [Body with FAB/BAB] → [CTA specificity check] → [A/B variants]
→ [Readability score >= 60] → [Brand voice match] → [Publish]
```

### DUAL Mode Flow
```text
[Product + audience] → [Mode detection] → [Copy formula + layout pattern]
→ [Copy generation] → [Visual hierarchy mapping] → [HTML implementation]
→ [Semantic integration] → [Responsive styling] → [Dual validation]
→ [Lighthouse + readability] → [Publish integrated page]
```

## Mode Detection Rules
```python
def select_mode(intent):
    visual_keywords = ["build", "create", "html", "component", "responsive", "design"]
    copy_keywords = ["write", "copy", "ad", "email", "headline", "campaign"]
    
    has_visual = any(kw in intent.lower() for kw in visual_keywords)
    has_copy = any(kw in intent.lower() for kw in copy_keywords)
    
    if has_visual and has_copy:
        return "DUAL"  # Integrated page with copy + visual
    elif has_visual:
        return "VISUAL"  # Component, layout, styling
    elif has_copy:
        return "COPY"  # Headlines, ads, email sequences
    else:
        return "UNCLEAR"  # Ask for clarification
```

## Ad Copy Character Limits (Platform Reference)

| Platform | Headline | Primary Text | Description |
|----------|---------|-------------|-------------|
| Facebook/Instagram | 40 chars | 125 chars | 30 chars |
| Google Search | 30 chars × 3 | — | 90 chars × 2 |
| LinkedIn | — | 150 chars | — |
| Twitter/X | — | 280 chars | — |

## Psychological Triggers (use 1 per piece)

| Trigger | Application | Example |
|---------|------------|---------|
| Specificity | Numbers beat vague claims | "Saves 3 hours" not "saves time" |
| Social proof | Volume or authority | "Used by 12,000 marketers" |
| Loss aversion | Frame as avoiding cost | "Stop losing leads to weak CTAs" |
| Urgency | Deadline or scarcity | "Closes Friday" / "Only 3 spots left" |
| Curiosity gap | Promise + withhold | "The one word that doubled our CTR" |
| Identity shift | Become who they want to be | "Write like a pro. Ship like a machine." |

## Readability Targets

| Audience | Flesch Score | Avg Sentence | Passive Voice |
|----------|-------------|-------------|--------------|
| B2C (consumer) | >= 65 | <= 14 words | < 5% |
| B2B (professional) | >= 50 | <= 18 words | < 10% |
| Executive/C-suite | >= 40 | <= 20 words | < 15% |

## Golden Rules

### Visual Frontend Rules
- **ALWAYS**: Use design tokens, NEVER hardcode hex colors (#HEXCODE prohibited)
- **ALWAYS**: Build mobile-first with proper breakpoints (sm:, md:, lg:, xl:, 2xl:)
- **ALWAYS**: Target Lighthouse 90+ performance and WCAG AA accessibility  
- **ALWAYS**: Use semantic HTML5 elements (header, main, section, article, aside)
- **NEVER**: Output invalid HTML — validate with W3C before delivery
- **ENSURE**: Dark mode support with proper token mapping
- **VERIFY**: Contrast ratios >= 4.5:1 for all text-background combinations

### Copywriting Rules
- **ALWAYS**: Identify funnel stage → select formula → write hook first → benefit stack → CTA → TEST note
- **NEVER**: Start with the product. Start with the reader's desire or pain.
- **ENSURE**: Every CTA names the specific action AND the specific benefit
- **PRODUCE**: Minimum 3 headline variants on every task — label V1, V2, V3; mark ★ recommended
- **VERIFY**: Flesch score before delivery; fix if below threshold for audience type

### DUAL Mode Integration Rules
- **ALWAYS**: Map copy structure to visual hierarchy (PAS → F-pattern, AIDA → Z-pattern)
- **ALWAYS**: Convert headlines to semantic h1-h6 tags, CTAs to button components
- **NEVER**: Use styled divs for headlines — proper semantic markup required
- **ENSURE**: Visual flow supports copy persuasion (F/Z-pattern aligned with formula)
- **VERIFY**: Both visual gates (Lighthouse) AND copy gates (readability) pass

### Universal Quality Standards
- **Lighthouse Performance**: >= 90 (VISUAL and DUAL modes)
- **WCAG Accessibility**: >= AA compliance (4.5:1 contrast minimum)
- **Copy Readability**: Flesch >= 60 (B2C) or >= 50 (B2B)
- **CTA Specificity**: Must name benefit + action (not "Click here" or "Learn more")
- **A/B Variant Count**: Minimum 3 headline variants for testing
- **Responsive Behavior**: Mobile-first approach, touch-friendly interactions
