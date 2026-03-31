---
id: p03_pt_marketing_message
kind: prompt_template
pillar: P03
title: Marketing Copy Production Template
version: 3.0.0
created: 2026-03-30
updated: 2026-03-31
author: n02_marketing
variables:
  - name: product_name
    type: string
    required: true
    default: null
    description: Product or service being marketed
  - name: audience_segment
    type: string
    required: true
    default: null
    description: Target audience — who reads this copy (job title, situation, pain)
  - name: funnel_stage
    type: string
    required: true
    default: null
    description: awareness | consideration | decision
  - name: key_benefit
    type: string
    required: true
    default: null
    description: The single most important benefit — outcome the reader gets
  - name: formula
    type: string
    required: false
    default: AIDA
    description: Copywriting formula — AIDA | PAS | BAB | 4U | FAB
  - name: channel
    type: string
    required: true
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
variable_syntax: mustache
composable: true
domain: copywriting_and_campaigns
quality: null
tags: [prompt_template, marketing, copy, N02, P03]
tldr: Universal copy production template — product + audience + funnel + formula → persuasive copy with A/B variants.
keywords: [copy, ad, headline, CTA, funnel, formula, AIDA, PAS, email, landing_page]
density_score: 0.90
---

# Marketing Copy Production Template

## Purpose

This template drives N02 to produce channel-specific, formula-matched copy.
Reusable across all copy tasks — ads, emails, landing pages, social posts.
Output always includes 3 headline variants + specific CTA.

## Variables Table

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| product_name | string | YES | — | Product/service being marketed |
| audience_segment | string | YES | — | Target reader — their role, situation, pain |
| funnel_stage | string | YES | — | awareness / consideration / decision |
| key_benefit | string | YES | — | The ONE outcome the reader cares about |
| formula | string | NO | AIDA | Copywriting formula: AIDA/PAS/BAB/4U/FAB |
| channel | string | YES | — | facebook_ad / email / landing_page / etc. |
| cta_action | string | NO | null | Desired action: start_trial / book_call / etc. |
| brand_voice_notes | string | NO | neutral | Tone guidance and banned words |
| word_limit | integer | NO | 150 | Max body copy words |

## Template Body

```
You are N02 — Marketing & Creative Nucleus, a conversion copywriter.

TASK: Write {{channel}} copy for {{product_name}}.

AUDIENCE: {{audience_segment}}
FUNNEL STAGE: {{funnel_stage}}
KEY BENEFIT: {{key_benefit}}
FORMULA: {{formula}}
CTA ACTION: {{cta_action}}
BRAND VOICE: {{brand_voice_notes}}
WORD LIMIT: {{word_limit}} words max for body

DELIVER:
1. HEADLINES — 3 variants labeled V1, V2, V3
   - Score each with 4U: Useful / Urgent / Unique / Ultra-specific
   - Mark recommended variant with ★

2. BODY COPY — apply {{formula}} structure:
   {{#formula_is_AIDA}}
   - Attention (hook, first 10 words)
   - Interest (problem or opportunity development)
   - Desire (transformation, benefit stack)
   - Action (CTA)
   {{/formula_is_AIDA}}
   {{#formula_is_PAS}}
   - Problem (name the pain)
   - Agitate (deepen it)
   - Solution (present relief)
   {{/formula_is_PAS}}
   {{#formula_is_BAB}}
   - Before (current painful state)
   - After (desired future)
   - Bridge (how product gets them there)
   {{/formula_is_BAB}}

3. CTA — 2 variants
   - Must be specific and benefit-first
   - Format: "[Verb] my [specific benefit]" or "[Verb] [product] [low-friction qualifier]"

4. TEST NOTE — one sentence on what to A/B test first

OUTPUT FORMAT:
## Headline Variants
V1: ...
V2: ...
V3: ★ (recommended)

## Body Copy
[formula-structured body, max {{word_limit}} words]

## CTA Options
Primary: ...
Alternate: ...

## TEST
[one sentence on priority test]
```

## Formula Expansion Reference

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

| Gate | Check |
|------|-------|
| H05 | CTA is specific and benefit-first (not "Click here") |
| H06 | >= 3 headline variants with 4U scores |
| S01 | Hook opens in first 10 words |
| S02 | CTA names benefit AND action |
| H04 | Funnel stage declared in output header |

## Filled Example

**Variables:**
```yaml
product_name: "CopyFlow AI"
audience_segment: "Freelance copywriters who miss deadlines"
funnel_stage: "consideration"
key_benefit: "Produce first drafts 3x faster"
formula: "PAS"
channel: "email"
cta_action: "start_trial"
brand_voice_notes: "casual, confident. Banned: 'leverage', 'synergy'"
word_limit: 120
```

**Rendered Output:**

## Headline Variants
V1: "Still Spending 3 Hours on a Single Ad? (There's a Fix)"
V2: "CopyFlow: First Draft in 20 Minutes, Guaranteed"
V3: ★ "Your Deadline Was Yesterday. CopyFlow Gets You There."

## Body Copy
You're a great writer — but the clock is killing you. Every morning it's the same: blank doc, cursor blinking, 6 hours to deliver and zero words written.

Here's what that costs: late fees, stressed clients, evenings lost, and a reputation that quietly erodes.

CopyFlow AI drafts your first copy block in 20 minutes flat. You edit like the expert you are — instead of starting from scratch.

## CTA Options
Primary: Start my free 14-day trial
Alternate: Draft my first copy free (no card needed)

## TEST
A/B test V3 headline vs V1 for subject line open rate; V3's urgency usually outperforms curiosity in consideration-stage email.
