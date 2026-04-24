---
id: schedule_n02
kind: schedule
8f: F8_collaborate
nucleus: n02
pillar: P12
mirrors: N00_genesis/P12_orchestration/templates/tpl_schedule.md
overrides:
  tone: seductive, emotional, conversion-oriented
  voice: second-person direct / brand-first
  sin_lens: LUXURIA CRIATIVA
  required_fields:
    - brand_voice_anchor
    - emotional_tone
    - cta_intent
    - campaign_phase
    - cadence_type
  quality_threshold: 9.0
  density_target: 0.85
  example_corpus: 3+ examples with brand voice samples
nl_spec: "campaign calendar with pre-launch, launch, and nurture phases"
version: 1.0.0
quality: 8.4
tags: [mirror, n02, marketing, creative, hermes_assimilation, campaign_calendar, cadence, P12]
tldr: "N02 campaign schedule: pre-launch heat, launch surge, and nurture cadence orchestrated as conversion arcs"
created: "2026-04-18"
updated: "2026-04-18"
author: n02_marketing
related:
  - n02_kc_campaign
  - landing_page_template
  - email_sequence_template
  - n02_kc_email_sequence
  - p07_sr_5d_marketing
  - p11_qg_marketing_artifacts
  - p03_sp_marketing_nucleus
  - p08_ac_n02
  - p01_kc_marketing_best_practices
  - schedule_instagram_content_plan
density_score: 1.0
---

## N02 Override: Campaign Calendar

N00 defines cron-based recurring tasks. N02 extends to **campaign cadence arcs** --
time-sequenced conversion events with phase-specific tone shifts.

## Campaign Phases

| Phase | Duration | Goal | Dominant Register | Frequency |
|-------|----------|------|------------------|-----------|
| Pre-launch | T-14 to T-3 | Build desire + FOMO | Warm | 3x/week |
| Launch | T-0 to T+3 | Convert NOW | Bold | Daily + urgency bursts |
| Nurture | T+4 to T+30 | Retain + upsell | Warm | 2x/week |
| Re-engagement | T+31+ | Win back lapsed | Bold or Playful | 1x/week |

## Cadence Templates

### Pre-Launch (14 days)
```yaml
T-14: Teaser -- "Something is coming. You'll want to be first."
T-10: Pain reveal -- Lead with the problem we're solving
T-7:  Social proof -- Early testimonial or waitlist count
T-3:  Final warning -- "Doors open in 72 hours. Are you in?"
```

### Launch (4 days)
```yaml
T+0: Open -- Full offer reveal, bold register, hard CTA
T+1: Objection handler -- FAQ framed as desire amplifiers
T+2: Scarcity signal -- Honest urgency (spots, deadline, bonus)
T+3: Last call -- "This closes at midnight."
```

### Nurture (ongoing)
```yaml
cron: "0 10 * * 2,4"   # Tue + Thu 10am brand timezone
format: value-first email -> soft CTA
goal: next-tier conversion or referral activation
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_kc_campaign]] | upstream | 0.31 |
| [[landing_page_template]] | upstream | 0.24 |
| [[email_sequence_template]] | upstream | 0.22 |
| [[n02_kc_email_sequence]] | upstream | 0.20 |
| [[p07_sr_5d_marketing]] | upstream | 0.20 |
| [[p11_qg_marketing_artifacts]] | upstream | 0.19 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.18 |
| [[p08_ac_n02]] | upstream | 0.18 |
| [[p01_kc_marketing_best_practices]] | upstream | 0.17 |
| [[schedule_instagram_content_plan]] | sibling | 0.17 |
