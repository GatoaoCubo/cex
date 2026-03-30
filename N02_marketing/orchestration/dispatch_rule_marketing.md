---
id: p12_dr_marketing
kind: dispatch_rule
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: n02_marketing
domain: copywriting_and_campaigns
quality: null
tags: [dispatch_rule, marketing, N02, routing]
tldr: Route to N02 when the task requires copy, ads, headlines, CTAs, email sequences, landing pages, or brand voice.
scope: marketing_and_creative
keywords: [copy, copywriting, ad, ads, headline, CTA, call_to_action, campaign, landing_page, email_sequence, brand_voice, social_media, anuncio, campanha, copy, redacao, texto_publicitario, slogan]
agent_node: n02-marketing-hub
model: claude-sonnet-4-6
cli: claude
priority: 7
confidence_threshold: 0.70
fallback: n07-orchestrator
---

# Marketing Dispatch Rule

## Purpose

Routes copywriting and creative marketing tasks to N02 (Marketing & Creative Nucleus).
N02 is the only nucleus that writes persuasive content — ads, emails, landing pages,
brand voice, social media copy, and campaign briefs.

## Trigger Conditions

### Route to N02 when request contains:

| Category | English Keywords | Portuguese Keywords |
|----------|-----------------|---------------------|
| Copy writing | copy, copywriting, ad copy, write ad | copy, redação, texto publicitário |
| Advertising | ad, ads, advertisement, banner ad | anuncio, anúncio, publicidade |
| Headlines | headline, subject line, title, hook | titulo, manchete, assunto de email |
| CTAs | CTA, call to action, button text | botão, chamada para ação |
| Campaigns | campaign, campaign brief, creative brief | campanha, briefing |
| Email | email sequence, nurture, cold email, welcome email | sequência de email, email marketing |
| Landing Pages | landing page, hero section, above the fold | página de destino, LP |
| Brand | brand voice, tone of voice, messaging | voz da marca, tom de voz |
| Social | social media post, caption, Instagram, LinkedIn | post, legenda, redes sociais |
| Strategy | creative strategy, messaging strategy | estratégia criativa |

### Do NOT route to N02:

| Task | Route To |
|------|----------|
| A/B test statistical analysis | N04 |
| Ad platform setup (Meta, Google) | N05 |
| Market research with large doc sets | N01 |
| Sales pricing strategy | N06 |
| Code for tracking or analytics | N05 |
| Legal review of copy claims | Human |

## Keyword Rationale

Keywords cover: direct copy requests, channel-specific writing (email/social/ads),
structural elements (headline/CTA/hook), and strategic inputs (brief/brand voice).
Portuguese variants included for bilingual CEX operation.

## Routing Logic

```
IF task.keywords ∩ dispatch_keywords != ∅ AND confidence >= 0.70:
    route → n02-marketing-hub (claude, sonnet, anthropic_max)
ELIF confidence < 0.70:
    request clarification → ask "is this a copy/creative task?"
ELIF n02-marketing-hub unavailable:
    escalate → n07-orchestrator
```

## Fallback Policy

If `n02-marketing-hub` is unavailable: escalate to `n07-orchestrator` with task description.
N07 will either retry N02 or provide manual handoff instructions.
