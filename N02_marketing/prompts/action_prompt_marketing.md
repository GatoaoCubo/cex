---
id: p03_ap_generate_marketing_strategy
kind: action_prompt
pillar: P03
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n02_marketing
title: N02 Action Prompts — Marketing Copy Quick Execution
action: Execute copy task directly with minimal input
input_required:
  - "task_type: string — which copy task to run"
  - "product: string — product or service name"
  - "audience: string — target audience description"
output_expected: Completed copy deliverable with A/B variants and TEST note
purpose: Quick-execution prompts for the 5 most common N02 tasks — no template wiring needed, paste and run.
steps_count: 5
timeout: 60s
edge_cases:
  - "No brand voice provided — use neutral professional tone"
  - "No funnel stage specified — ask before writing or default to consideration"
  - "Copy exceeds word limit — trim benefits block first, keep hook and CTA intact"
constraints:
  - NEVER write generic CTAs — always specific + benefit-first
  - ALWAYS produce 3 headline variants minimum
  - NEVER skip funnel stage identification
domain: copywriting_and_campaigns
quality: null
tags: [action_prompt, marketing, copy, N02, quick_execution]
tldr: 5 ready-to-run N02 action prompts — ad copy, headline, landing page hero, email, brand voice card.
density_score: 0.91
---

# N02 Action Prompts — Marketing Copy Quick Execution

## Context

Five copy tasks run most often in N02. These action prompts are pre-wired — paste the
relevant prompt into the N02 system, fill the `[BRACKETS]`, and get a complete deliverable.
No template setup needed. Each follows 8F pipeline internally.

---

## Action 1: Write Facebook/Instagram Ad

**Use when**: Need a paid social ad with hook, body, and CTA.

```
TASK: Write a Facebook/Instagram ad.
PRODUCT: [product name and one-sentence description]
AUDIENCE: [who they are, their pain or desire]
FUNNEL STAGE: [awareness | consideration | decision]
KEY BENEFIT: [the ONE outcome they get]
BRAND VOICE: [casual/professional/bold — and 1–2 banned words if any]

DELIVER:
- 3 headline variants (V1, V2, V3 with 4U scores, mark ★ recommended)
- Primary text (hook + PAS or AIDA body, 90–125 words)
- CTA button text (2 options, specific + benefit-first)
- TEST note (what to A/B test first)
```

---

## Action 2: Optimize Headlines (10 Variants)

**Use when**: Need multiple headline options for an ad, email subject, or landing page.

```
TASK: Generate 10 headline variants and score them.
PRODUCT: [name]
AUDIENCE: [description]
FUNNEL STAGE: [awareness | consideration | decision]
KEY BENEFIT: [single outcome]

DELIVER:
- 10 headline variants using these formulas:
  - 2× AIDA hook
  - 2× PAS opener
  - 2× 4U scored
  - 2× Number + Outcome
  - 2× "How to [benefit] without [pain]"
- Score each variant: Useful/Urgent/Unique/Ultra-specific (1–3 each, max 12)
- Top 3 ranked by score
- TEST: which to test first and why
```

---

## Action 3: Landing Page Hero Section

**Use when**: Need the above-the-fold section of a landing page.

```
TASK: Write landing page hero section.
PRODUCT: [name + what it does in one sentence]
AUDIENCE: [who lands on this page, what brought them here]
OFFER: [what they get — trial, demo, download, purchase]
KEY BENEFIT: [the transformation they care about]
BRAND VOICE: [tone notes]

DELIVER:
- 3 headline variants (scored, ★ recommended)
- Subheadline (1 sentence, expands headline with specificity)
- Hero body (2–3 sentences, desire-building, no features yet)
- Primary CTA (specific + benefit-first)
- Secondary CTA (lower commitment — "See how it works")
- Social proof hook (1 line: "Join X companies/people who...")
- TEST note
```

---

## Action 4: Cold Email (5-Email Sequence)

**Use when**: Need a B2B cold outreach or B2C nurture sequence.

```
TASK: Write a 5-email sequence.
TYPE: [cold_outreach | nurture | cart_abandonment | re-engagement]
PRODUCT: [name]
AUDIENCE: [description — role, company type, pain]
GOAL: [desired action at end of sequence]
BRAND VOICE: [tone]

DELIVER for each email (1–5):
- Subject line (3 variants, mark ★ recommended)
- Preview text (40–90 chars)
- Body copy (formula-matched per email type from KC)
- CTA (specific)
- Email purpose label (hook / value / social_proof / offer / breakup)
```

---

## Action 5: Brand Voice Card

**Use when**: Need to define or document a brand's writing voice.

```
TASK: Create a brand voice card.
BRAND: [brand name]
DESCRIPTION: [what they do, who they serve, 1–2 sentences]
KNOWN EXAMPLES: [paste 2–3 samples of existing copy if available, or write NONE]
TARGET TONE: [describe in plain words — e.g., "warm but authoritative, like a smart friend"]

DELIVER:
- Tone dimension scores (Formal←→Casual, Technical←→Plain, 3rd←→1st person, Calm←→Bold) each on 1–5 scale
- 5 signature phrases the brand would say
- 5 banned words/phrases the brand would never say
- Persona anchor (describe the brand as if it were a person: age, job, how they talk)
- 3 before/after examples: [weak copy] → [brand voice copy]
- Usage rules (2–3 sentences on when voice can flex and when it must hold firm)
```

---

## Validation

| Check | Rule |
|-------|------|
| CTA specificity | Not "Click here" / "Learn more" — must name benefit |
| Headline variants | Minimum 3 per task |
| Funnel stage | Declared in every deliverable |
| A/B TEST note | Required at end of every output |
| Word limits | Respected per channel (social < 150, email < 250 body, LP hero < 100 subhead) |

## Edge Cases

| Situation | Action |
|-----------|--------|
| No brand voice provided | Write in neutral professional tone; flag "[BRAND VOICE CARD RECOMMENDED]" |
| No funnel stage specified | Default to consideration; note assumption at top of output |
| Copy exceeds word limit | Trim benefits block; keep hook and CTA intact |
| Conflicting CTAs requested | Pick ONE; note the choice and reason |
