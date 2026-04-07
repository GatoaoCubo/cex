---
id: p03_pt_commercial_nucleus
kind: prompt_template
pillar: P03
title: Commercial Nucleus Prompt Templates
version: 3.1.0
created: 2026-03-30
updated: 2026-04-07
author: n06_commercial
quality: 9.1
tags: [prompt_template, commercial, N06, pricing, courses, funnels, brand]
tldr: "7 prompt templates for N06 commercial outputs: pricing page, course outline, sales page, upsell sequence, brand-aligned copy. All parametric with {{variables}}."
density_score: 0.93
linked_artifacts:
  primary: p03_sp_commercial_nucleus
  related: [p01_kc_commercial_nucleus, p01_kc_brand_monetization_models, n06_output_pricing_page]
variables:
  - name: product_name
    type: string
    required: true
    default: null
    description: Name of the digital product or course.
  - name: target_audience
    type: string
    required: true
    default: null
    description: Specific audience segment (e.g., "freelance designers earning R$3-5k/month").
  - name: transformation
    type: string
    required: true
    default: null
    description: Measurable outcome the buyer achieves (e.g., "land their first R$10k client in 90 days").
  - name: price_range
    type: string
    required: false
    default: null
    description: Optional price anchor or range to inform tier design.
  - name: platform
    type: string
    required: false
    default: Hotmart
    description: Deployment platform (Hotmart, Kiwify, Kajabi, Teachable).
  - name: traffic_source
    type: string
    required: false
    default: null
    description: Where traffic enters the funnel (Instagram, YouTube, Google, cold email).
  - name: audience_size
    type: string
    required: false
    default: null
    description: Estimated reachable audience size for revenue model projections.
variable_syntax: mustache
composable: true
domain: commercial-monetization
quality: 8.9
tags: [prompt_template, commercial, N06, pricing, course, funnel, upsell, revenue-model]
tldr: Five reusable N06 templates — Pricing Strategy, Course Outline, Funnel Build, Upsell Sequence, and Revenue Model.
density_score: 0.91
---

# Commercial Nucleus Prompt Templates

Four reusable templates for N06 core tasks. Each template is composable — use individually or chain for a full product launch.

---

## Template 1: Pricing Strategy

**Use when**: You need to price a digital product or course.

```
Design a 3-tier pricing strategy for {{product_name}}.

TARGET AUDIENCE: {{target_audience}}
TRANSFORMATION: {{transformation}}
PLATFORM: {{platform}}
{{#price_range}}PRICE ANCHOR: {{price_range}}{{/price_range}}

Deliverables:
1. Transformation Value Assessment — quantify what the outcome is worth to the buyer
2. 3-Tier Pricing Table (Basic / Pro / VIP) with:
   - Price per tier
   - Inclusions per tier
   - Psychological rationale for each price point
3. Revenue Model — 3 scenarios (conservative / realistic / optimistic):
   - Units × Price × Conversion Rate = Revenue
4. Recommended launch price with written rationale (2-3 sentences)
5. Payment plan option (installments) if applicable

Apply value-based pricing. Anchor to transformation, not production cost.
```

---

## Template 2: Course Outline

**Use when**: You need to structure a course curriculum.

```
Build a course outline for {{product_name}}.

TARGET AUDIENCE: {{target_audience}}
TRANSFORMATION: {{transformation}}
PLATFORM: {{platform}}

Deliverables:
1. Transformation Arc:
   - BEFORE: [student situation, pain, frustration at start]
   - JOURNEY: [module milestones — what shifts at each module]
   - AFTER: [specific outcome, skill, status, or income gained]

2. Module Structure (4-8 modules):
   For each module:
   - Module title (outcome-focused, not topic-focused)
   - 3-5 lesson titles
   - Estimated duration
   - What the student can DO after this module

3. Pricing Tier Recommendation:
   - Justify based on transformation depth and delivery mode
   - Recommend platform tier (Hotmart Standard / Plus / VIP)

4. Upsell Path:
   - What is the logical next product after completing this course?
```

---

## Template 3: Funnel Build

**Use when**: You need a complete sales funnel for a product.

```
Build a complete sales funnel for {{product_name}}.

TARGET AUDIENCE: {{target_audience}}
TRANSFORMATION: {{transformation}}
TRAFFIC SOURCE: {{traffic_source}}
PLATFORM: {{platform}}

Deliverables:

TOFU (Top of Funnel):
- 3 ad hooks / post headlines targeting the specific pain of {{target_audience}}
- CTA for each hook (lead magnet name, opt-in page headline)
- Expected conversion benchmark: [X%]

MOFU (Middle of Funnel):
- Lead magnet title + 3-bullet value proposition
- 3-email nurture sequence:
  - Email 1 (day 0): Deliver + educate
  - Email 2 (day 2): Deepen pain + introduce mechanism
  - Email 3 (day 4): Transition to offer

BOFU (Bottom of Funnel):
- Sales page headline (outcome-specific)
- VSL outline (hook → problem → mechanism → proof → offer → CTA)
- Guarantee framing
- Primary CTA text

POST-PURCHASE:
- Order bump: [name, price, one-sentence value prop]
- OTO1: [name, price, take rate estimate]
- Downsell: [fallback if OTO declined]
```

---

## Template 4: Upsell Sequence

**Use when**: You need to maximize LTV after the first sale.

```
Design a complete upsell sequence for buyers of {{product_name}}.

TARGET AUDIENCE: {{target_audience}} who just purchased
BASE PRICE: {{price_range}}

Deliverables:

1. ORDER BUMP (shown at checkout):
   - Product name
   - Price (15-30% of base price)
   - One-sentence value: "Add X to your order and get Y faster"
   - Expected take rate: [%]

2. OTO1 (shown immediately after purchase):
   - Product name + transformation
   - Price (50-100% of base price)
   - Pitch: what does this unlock that the base product doesn't?
   - Urgency element
   - Expected take rate: [%]

3. OTO2 (shown after OTO1 decline or accept):
   - Done-for-you / implementation layer
   - Price (2-3x base price)
   - Expected take rate: [%]

4. DOWNSELL (shown after OTO1 decline):
   - Stripped-down version OR payment plan version
   - Price (30-40% of OTO1)
   - Expected conversion of declinees: [%]

5. LTV PROJECTION:
   - AOV = Base + (Bump × take%) + (OTO1 × take%) + (OTO2 × take%)
   - LTV = AOV × [repeat purchase or subscription factor]
```

---

---

## Template 5: Revenue Model

**Use when**: You need to project revenue scenarios before a launch or pricing decision.

```
Build a revenue model for {{product_name}}.

TARGET AUDIENCE: {{target_audience}}
TRANSFORMATION: {{transformation}}
BASE PRICE: {{price_range}}
PLATFORM: {{platform}}
{{#audience_size}}REACHABLE AUDIENCE: {{audience_size}}{{/audience_size}}

Deliverables:

1. UNIT ECONOMICS (per sale):
   - Base price
   - Order bump price + take rate → contribution
   - OTO1 price + take rate → contribution
   - OTO2 price + take rate → contribution
   - AOV = Base + (Bump × %) + (OTO1 × %) + (OTO2 × %)

2. REVENUE SCENARIOS:
   | Scenario | Sales | AOV | Revenue |
   |----------|-------|-----|---------|
   | Conservative | [X] | [AOV] | [R$] |
   | Realistic | [X] | [AOV] | [R$] |
   | Optimistic | [X] | [AOV] | [R$] |

3. FUNNEL MATH (show conversion chain):
   Audience → TOFU reach ([X%]) → MOFU opt-ins ([X%]) → BOFU clicks ([X%]) → Sales ([X%]) = [N] buyers

4. LTV PROJECTION:
   - LTV = AOV × Purchase Frequency × Customer Lifespan
   - Target: LTV >= 3x AOV

5. CAC CEILING:
   - Max acceptable CAC = 30% of AOV = R$[X]
   - Required ROAS to break even: [X]x
```

---

## Composability

These templates chain naturally for a product launch:

```
Template 2 (Course Outline) → Template 1 (Pricing Strategy) → Template 5 (Revenue Model) → Template 3 (Funnel Build) → Template 4 (Upsell Sequence)
```

Run in sequence or dispatch to N06 via grid for parallel execution.
