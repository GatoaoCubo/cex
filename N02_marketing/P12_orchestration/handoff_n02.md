---
quality: 8.4
quality: 7.7
id: handoff_n02
kind: handoff
8f: F8_collaborate
nucleus: n02
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_handoff.md
overrides:
  tone: seductive, emotional, conversion-oriented
  voice: second-person direct / brand-first
  sin_lens: LUXURIA CRIATIVA
  required_fields:
    - brand_voice_anchor
    - emotional_tone
    - cta_intent
    - campaign_brief
    - success_metrics
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with brand voice samples
max_revisions: 2
escalation_target: n07
version: 1.0.0
tags: [mirror, n02, marketing, creative, hermes_assimilation, campaign_brief, handoff, P12]
tldr: "N02 handoff template: campaign brief + brand voice contract + success metrics for downstream nuclei"
created: "2026-04-18"
updated: "2026-04-18"
author: n02_marketing
related:
  - p03_sp_marketing_nucleus
  - cross_nucleus_handoffs
  - p02_nd_n02.md
  - n02_self_review_2026-04-02
  - n02_kc_campaign
  - p11_qg_marketing_artifacts
  - n02_leverage_map_v2_verification
  - p08_ac_n02
  - p12_wf_marketing_pipeline
  - p12_wf_visual_frontend_marketing
density_score: 1.0
---

## N02 Override: Marketing Handoff

N00 handoff passes task context between agents. N02 extends to a
**campaign brief contract** -- everything a downstream nucleus needs to produce
on-brand, conversion-ready work without a single clarifying question.

## Required Sections (N02 additions)

### Campaign Brief
| Field | Value |
|-------|-------|
| Campaign name | {{campaign_slug}} |
| Phase | pre-launch / launch / nurture / re-engagement |
| Target segment | {{segment_from_user_model_n02}} |
| Buying stage | awareness / consideration / decision / loyalty |
| Channel | {{platform_from_messaging_gateway_n02}} |
| Deadline | {{ISO_DATE}} |

### Brand Voice Contract
| Dimension | Value |
|-----------|-------|
| Register | warm / bold / playful |
| Voice anchor | {{brand_voice_one_line}} |
| Emotional tone | {{primary_emotion}} |
| Forbidden words | See personality_n02 anti-patterns |
| CTA intent | {{desired_action}} |

### Success Metrics
| Metric | Target | Tracking |
|--------|--------|---------|
| Open rate (email) | >{{X}}% | Campaign tool |
| CTR | >{{Y}}% | UTM tracking |
| Conversion | >{{Z}}% | Landing page |
| A/B winner | Declared at {{N}} sends | Statistical sig |

## Downstream Instructions
All nuclei receiving this handoff MUST:
1. Load `personality_n02.md` before generating any copy
2. Produce Variant A + Variant B per `skill_n02.md`
3. Validate against anti-patterns before returning output
4. Signal N02 on completion with quality score + winning variant ID

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_marketing_nucleus]] | upstream | 0.31 |
| [[cross_nucleus_handoffs]] | related | 0.31 |
| [[p02_nd_n02.md]] | upstream | 0.30 |
| [[n02_self_review_2026-04-02]] | upstream | 0.29 |
| [[n02_kc_campaign]] | upstream | 0.28 |
| [[p11_qg_marketing_artifacts]] | upstream | 0.27 |
| [[n02_leverage_map_v2_verification]] | upstream | 0.26 |
| [[p08_ac_n02]] | upstream | 0.26 |
| [[p12_wf_marketing_pipeline]] | related | 0.25 |
| [[p12_wf_visual_frontend_marketing]] | related | 0.23 |
