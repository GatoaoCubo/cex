---
id: user_model_n02
kind: user_model
8f: F2_become
nucleus: n02
pillar: P10
mirrors: N00_genesis/P10_memory/tpl_user_model.md
overrides:
  tone: seductive, emotional, conversion-oriented
  voice: second-person direct / brand-first
  sin_lens: LUXURIA CRIATIVA
  required_fields:
    - brand_voice_anchor
    - emotional_tone
    - cta_intent
    - buying_stage
    - pain_points
    - aspirations
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with brand voice samples
version: 1.0.0
quality: 8.2
tags: [mirror, n02, marketing, creative, hermes_assimilation, buyer_persona, P10]
tldr: "N02 buyer persona model: maps pains, aspirations, and buying stage to conversion moments"
created: "2026-04-18"
updated: "2026-04-18"
author: n02_marketing
related:
  - p07_sr_5d_marketing
  - p03_sp_marketing_nucleus
  - landing_page_template
  - p08_ac_n02
  - n02_marketing
  - n02_tool_copy_analyzer
  - p04_rp_marketing_nucleus
  - ex_prompt_template_aida
  - p12_wf_visual_frontend_marketing
  - email_sequence_template
density_score: 1.0
---

## N02 Override: Buyer Persona

N00 tracks preferences and working style. N02 extends this to **buying psychology** --
what makes the buyer move from curious to committed.

## Required Collections (N02 additions)

### buying_stage
| Stage | Signal | N02 Response |
|-------|--------|--------------|
| Awareness | First touch, broad search | Hook-first content, no hard sell |
| Consideration | Comparing options | Social proof, benefit framing |
| Decision | Price/feature check | Urgency + clear CTA |
| Loyalty | Repeat buyer | Exclusive access, community belonging |

### pain_points
| Pain | Emotional Weight | Copy Angle |
|------|-----------------|------------|
| {{pain_1}} | high / medium / low | {{angle_1}} |
| {{pain_2}} | high / medium / low | {{angle_2}} |

### aspirations
| Aspiration | Desire Language | CTA Hook |
|------------|----------------|----------|
| {{aspiration_1}} | {{desire_phrase_1}} | {{cta_hook_1}} |
| {{aspiration_2}} | {{desire_phrase_2}} | {{cta_hook_2}} |

## Brand Voice Anchor
`{{brand_voice_one_line}}` — the North Star phrase that all copy returns to.

## Emotional Tone Map
| Touchpoint | Tone | Example Line |
|------------|------|-------------|
| First ad | curiosity + desire | "You already know this isn't enough." |
| Landing page | confidence + urgency | "Every day you wait costs you." |
| Email nurture | warmth + exclusivity | "This was made for people like you." |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_5d_marketing]] | upstream | 0.29 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.27 |
| [[landing_page_template]] | upstream | 0.24 |
| [[p08_ac_n02]] | upstream | 0.24 |
| [[n02_marketing]] | upstream | 0.23 |
| [[n02_tool_copy_analyzer]] | upstream | 0.21 |
| [[p04_rp_marketing_nucleus]] | upstream | 0.21 |
| [[ex_prompt_template_aida]] | upstream | 0.21 |
| [[p12_wf_visual_frontend_marketing]] | downstream | 0.21 |
| [[email_sequence_template]] | upstream | 0.21 |
