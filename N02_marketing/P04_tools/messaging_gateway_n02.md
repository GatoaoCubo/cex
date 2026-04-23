---
id: messaging_gateway_n02
kind: messaging_gateway
nucleus: n02
pillar: P04
mirrors: N00_genesis/P04_tools/tpl_messaging_gateway.md
overrides:
  tone: seductive, emotional, conversion-oriented
  voice: second-person direct / brand-first
  sin_lens: LUXURIA CRIATIVA
  required_fields:
    - brand_voice_anchor
    - emotional_tone
    - cta_intent
    - campaign_type
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with brand voice samples
version: 1.0.0
quality: 8.2
tags: [mirror, n02, marketing, creative, hermes_assimilation, messaging, dm_campaigns, P04]
tldr: "N02 messaging gateway: DM broadcast campaigns via Telegram, Discord communities, WhatsApp click-to-chat"
created: "2026-04-18"
updated: "2026-04-18"
author: n02_marketing
related:
  - ex_response_format_ad_copy
  - n02_kc_campaign
  - p03_sp_marketing_nucleus
  - n02_leverage_map_v2_verification
  - p07_sr_5d_marketing
  - n02_self_review_2026-04-02
  - p08_ac_n02
  - p03_sp_brand_nucleus
  - n02_tool_copy_analyzer
  - p02_nd_n02.md
density_score: 1.0
---

## N02 Override: DM Campaign Gateway

N00 defines platform transport and security. N02 extends to **campaign delivery** --
the gateway as a conversion channel, not just a messaging pipe.

## Campaign Platform Matrix

| Platform | Mode | Campaign Type | N02 Use Case |
|----------|------|--------------|--------------|
| Telegram | broadcast + bot | Pre-launch drip, flash sale alerts | High-frequency warm leads |
| Discord | community + role-based | Community nurture, exclusive drops | Brand loyalists, superfans |
| WhatsApp | click-to-chat | Decision-stage CTA, abandoned cart | High-intent buyers |

## Message Templates (N02 Required)

### Telegram Broadcast
```
Subject: {{hook_under_12_words}}
Body: {{pain_line}} + {{desire_line}} + {{cta_link}}
Max: 320 chars (no truncation on mobile)
```

### Discord Community Post
```
Channel: #{{campaign_channel}}
Role ping: @{{segment_role}}
Format: embed with image + 2-line copy + button CTA
```

### WhatsApp Click-to-Chat
```
Pre-fill message: "{{opener_question_that_feels_personal}}"
CTA button label: {{action_verb}} (max 20 chars)
```

## Brand Voice Rules for DM
- Never open with "Hi" -- open with the pain or the promise
- One CTA per message, no exceptions
- Urgency must be real (deadline, stock, access window)
- Emoji only if brand register is playful; never for B2B segments

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ex_response_format_ad_copy]] | downstream | 0.25 |
| [[n02_kc_campaign]] | upstream | 0.23 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.23 |
| [[n02_leverage_map_v2_verification]] | upstream | 0.23 |
| [[p07_sr_5d_marketing]] | downstream | 0.23 |
| [[n02_self_review_2026-04-02]] | downstream | 0.22 |
| [[p08_ac_n02]] | downstream | 0.22 |
| [[p03_sp_brand_nucleus]] | upstream | 0.21 |
| [[n02_tool_copy_analyzer]] | related | 0.21 |
| [[p02_nd_n02.md]] | upstream | 0.21 |
