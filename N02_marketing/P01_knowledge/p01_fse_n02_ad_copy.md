---
id: p01_fse_n02_ad_copy
kind: few_shot_example
8f: F3_inject
pillar: P01
nucleus: N02
title: "Few-Shot Example -- N02 Ad Copy via 8F Pipeline"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: few-shot-example-builder
domain: marketing
difficulty: medium
edge_case: false
format: "8F pipeline trace + input/output pairs for paid ad copy"
quality: 9.1
tags: [few-shot, ad-copy, marketing, 8f-pipeline, n02, creative_lust]
tldr: "4 input/output pairs teaching N02 how to run the 8F pipeline for paid ad copy: brief -> angles -> variants -> quality gate."
keywords: [ad-copy, paid-ads, linkedin, instagram, 8f, campaign, cta, funnel]
density_score: 1.0
related:
  - n02_tool_copy_analyzer
  - p03_sp_marketing_nucleus
  - ex_response_format_ad_copy
  - p03_pt_marketing_task_execution
  - p08_ac_n02
  - ad_copy_template
  - p03_ap_visual_frontend_marketing
  - p02_agent_visual_frontend_marketing
  - ex_agent_copywriter
  - p07_sr_visual_frontend_marketing
---
<!-- 8F TRACE
F1 CONSTRAIN: kind=few_shot_example, pillar=P01, max_bytes=5120, naming=p01_fse_{topic}.md
F2 BECOME: few-shot-example-builder (13 ISOs loaded). Sin lens: Creative Lust.
F3 INJECT: kno_few_shot_example_n02 + kc_campaign + input_schema_campaign_brief + quality_gate_marketing. Match: 82%
F4 REASON: 4 examples, easy->hard arc, domain=paid ad copy, formats: LinkedIn+Instagram+Email+Multi-platform
F5 CALL: Read+Write+compile ready. 1 similar artifact (kno_few_shot_example_n02.md).
F6 PRODUCE: 4 input/output pairs, each with 8F trace header and variant pack
F7 GOVERN: frontmatter complete, id=p01_fse_n02_ad_copy, tags>=3, input non-empty x4, output non-empty x4, no self-scoring
F8 COLLABORATE: compiled via cex_compile.py
-->

## Explanation

N02's 8F pipeline transforms a marketing brief into seductive, testable ad copy.
These 4 examples calibrate easy (one platform, clear brief) through hard (multi-platform
retargeting with restricted vocabulary). Each output shows the exact structured form:
angles declared first, copy variants second, quality metadata last.

The sin lens is active on every example: output must make the reader WANT, not just KNOW.

---

## Example 1 (easy) -- LinkedIn B2B, MOFU, single platform

**Input brief**
```yaml
task: create_3_linkedin_ad_variants
audience: b2b_saas_founders
funnel_stage: mofu
offer: ai_agent_platform
promise: ship agents 10x faster than coding from scratch
proof:
  stat: "customers shipped first agent in under 2 hours"
  basis: "median across 47 beta customers"
constraints:
  max_chars: 240
  tone: direct_confident
  cta: start_free_trial
  banned: [hype_adjectives, passive_voice]
```

**8F trace (abbreviated)**
```
F1: kind=prompt_template/P03, pillar=P03, constraint=240 chars, tone=direct_confident
F2: N02 loaded. Creative Lust lens active -- desire before logic.
F3: kc_campaign (MOFU stage = differentiate+prove), brand_config, copy_analyzer
F4: angles -> pain_to_proof, aspiration, objection_break
F6: 3 variants, each = angle + copy + CTA
F7: proof present x3, CTA present x3, no hype, brand match = pass
```

**Output**
```yaml
variants:
  - angle: pain_to_proof
    copy: "Most agent builds stall at integration hell. Our customers bypass it. Median time to first live agent: under 2 hours. 47 teams confirmed it. Start your free trial."
    cta: "Start free trial"

  - angle: aspiration
    copy: "The best AI teams are not writing more code. They are composing agents from typed infrastructure. First one ships in hours. Start your free trial and see the gap."
    cta: "Start free trial"

  - angle: objection_break
    copy: "If you think agent development is weeks of plumbing, you are pricing the wrong stack. 47 teams shipped in under 2 hours each. Start your free trial before the next sprint."
    cta: "Start free trial"

quality_check:
  proof_present: true
  cta_count: 1 per variant
  hype_words: 0
  stage_alignment: mofu (differentiate + prove)
```

---

## Example 2 (medium) -- Instagram D2C, TOFU, visual-first

**Input brief**
```yaml
task: create_2_instagram_caption_variants
audience: fashion_conscious_women_25_35
funnel_stage: tofu
offer: sustainable_streetwear_brand
promise: look good without the guilt trip
proof:
  visual: hero_product_image_attached
  social: "12,000 orders shipped carbon-neutral"
constraints:
  max_chars: 150
  tone: warm_irreverent
  cta: link_in_bio
  banned: [climate_doom_language, corporate_speak]
```

**8F trace (abbreviated)**
```
F1: kind=prompt_template/P03, pillar=P03, constraint=150 chars, tone=warm_irreverent
F2: N02 loaded. Short-form Instagram = hook dominates. Desire before explanation.
F3: kc_campaign (TOFU = educate, frame), brand_config, kc_visual_hierarchy_principles
F4: angles -> identity_mirror, proof_by_number
F6: 2 variants, warm_irreverent voice, emoji allowed
F7: hook in first line, no doom language, CTA present = pass
```

**Output**
```yaml
variants:
  - angle: identity_mirror
    copy: "Streetwear that does not cost the planet a favor. 12,000 orders shipped. All carbon-neutral. Link in bio."
    cta: "Link in bio"

  - angle: proof_by_number
    copy: "12,000 orders. Zero carbon guilt. Your next fit is here. Link in bio."
    cta: "Link in bio"

quality_check:
  proof_present: true
  cta_count: 1 per variant
  doom_language: 0
  hook_position: line_1
```

---

## Example 3 (medium-hard) -- Email subject line A/B batch, BOFU

**Input brief**
```yaml
task: create_5_email_subject_line_variants
audience: free_tier_saas_users_30_days_active
funnel_stage: bofu
offer: pro_plan_upgrade
promise: unlock team collaboration + advanced analytics
proof:
  stat: "Pro users retain 41% longer"
  basis: "internal cohort data Q1"
constraints:
  max_chars: 50
  tone: friendly_urgent
  cta: implicit_in_subject
  banned: [spam_triggers, ALL_CAPS, excessive_punctuation]
  test_hypothesis: "urgency vs. curiosity vs. social_proof"
```

**8F trace (abbreviated)**
```
F1: kind=prompt_template/P03, constraint=50 chars, test_hypothesis present
F2: N02. BOFU = remove risk, close. Email subject = first filter.
F3: kc_email_sequence (subject line patterns), campaign quality gate
F4: 3 hypothesis angles (urgency, curiosity, social_proof) + 2 hybrid
F6: 5 variants mapped to hypothesis angles
F7: no spam triggers, no ALL_CAPS, CTA implicit, < 50 chars x5 = pass
```

**Output**
```yaml
variants:
  - angle: urgency
    subject: "Your 30-day trial ends soon -- here is what you lose"
    chars: 48
    hypothesis: urgency

  - angle: curiosity
    subject: "What Pro users see that free users miss"
    chars: 38
    hypothesis: curiosity

  - angle: social_proof
    subject: "Pro users stay 41% longer. Here is why."
    chars: 38
    hypothesis: social_proof

  - angle: hybrid_urgency_proof
    subject: "41% retention lift. Your upgrade window closes Friday."
    chars: 51
    note: "1 char over limit -- trim: remove 'lift'"
    chars_fixed: 50

  - angle: hybrid_curiosity_proof
    subject: "Why do Pro users stay? One number explains it."
    chars: 46
    hypothesis: curiosity_plus_proof

quality_check:
  spam_trigger_words: 0
  ALL_CAPS: false
  char_limit_pass: 4 of 5 (1 flagged with fix)
  stage_alignment: bofu
```

---

## Example 4 (hard) -- Multi-platform retargeting, restricted vocabulary

**Input brief**
```yaml
task: create_retargeting_copy_pack
audience: website_visitors_no_purchase_72h
funnel_stage: bofu
offer: limited_cohort_enrollment
promise: last 3 seats in live coaching cohort
proof:
  stat: "87% of graduates hit revenue goal within 90 days"
  testimonial: "I closed my first 5-figure deal in week 3. -- Ana S."
constraints:
  platforms: [instagram_story, linkedin_sponsored, email_drip]
  max_chars:
    instagram_story: 80
    linkedin_sponsored: 300
    email_drip: 60_char_subject_200_char_preview
  tone: warm_scarce
  cta: secure_my_seat
  banned: [fake_scarcity, income_claims_unsubstantiated, pressure_manipulation]
  legal_note: "87% stat must include basis in email only, not in ad copy"
```

**8F trace (abbreviated)**
```
F1: kind=prompt_template/P03, 3 platforms, different char limits, legal constraint
F2: N02. Multi-platform = one brief, adapted output per channel. Legal constraints active.
F3: kc_campaign, kc_email_sequence, brand_config, quality_gate (legal flag: stat basis email-only)
F4: unified angle = authentic_scarcity + peer_proof; adapt per channel length
F6: 3 platform packs, each with legal compliance note
F7: no fake_scarcity, stat basis in email only, warm_scarce tone consistent = pass
```

**Output**
```yaml
instagram_story:
  copy: "3 seats left. Ana closed her first 5-figure deal in week 3. Secure yours."
  cta: "Secure my seat"
  chars: 74

linkedin_sponsored:
  copy: "87% of our graduates hit their revenue goal within 90 days. We have 3 seats left in the next live cohort. Ana closed her first 5-figure deal in week 3. If you have been on the list, now is the time. Secure my seat."
  cta: "Secure my seat"
  chars: 213
  note: "Stat basis omitted per legal constraint (not substantiated in ad format)"

email_drip:
  subject: "3 seats left -- Ana's story (and yours?)"
  subject_chars: 41
  preview: "87% of graduates hit revenue goal in 90 days (Q1 cohort data). Ana closed her first 5-figure deal in week 3. You are next."
  preview_chars: 122
  note: "Stat basis included in preview (email format approved for disclosure)"

quality_check:
  fake_scarcity: false (3 seats confirmed real)
  income_claim_unsubstantiated: false (stat + testimonial both present)
  legal_compliance: pass (stat basis in email only)
  platform_char_limits: all within limits
  tone_consistency: warm_scarce across all 3 platforms
```

---

## Format Lessons

| Lesson | What the model learns |
|--------|-----------------------|
| Declare angles before copy | Angle names make A/B testing trackable |
| Include quality_check block | Self-govern before delivery; surface failures early |
| Adapt per platform, not per angle | Brief defines desire; channel defines length + format |
| Legal constraints are copy constraints | Never omit banned/legal from the brief |
| Proof discipline | Every variant carries evidence -- never decoration |

## Prompting Rules Derived From These Examples

1. Every brief must include: audience, funnel_stage, offer, promise, proof, constraints.
2. Declare test_hypothesis when running A/B -- angles need names, not just copy.
3. Include platform-specific char limits explicitly; let the model adapt.
4. Legal constraints belong in the brief `banned` or `legal_note` field.
5. Output format: angle + copy + cta + quality_check per variant.
6. For multi-platform: one brief, per-channel adaptation section.

## Anti-Patterns

| Anti-pattern | Failure |
|-------------|---------|
| No proof in brief | Copy inflates -> trust gap |
| No angle declared | Copy is not testable; cannot iterate |
| Single variant only | A/B testing is impossible |
| Char limits omitted | Copy goes over; platform truncates; CTA lost |
| Legal constraints undeclared | Compliance failure in publish stage |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_tool_copy_analyzer]] | downstream | 0.33 |
| [[p03_sp_marketing_nucleus]] | downstream | 0.29 |
| [[ex_response_format_ad_copy]] | downstream | 0.27 |
| [[p03_pt_marketing_task_execution]] | downstream | 0.26 |
| [[p08_ac_n02]] | downstream | 0.25 |
| [[ad_copy_template]] | downstream | 0.25 |
| [[p03_ap_visual_frontend_marketing]] | downstream | 0.24 |
| [[p02_agent_visual_frontend_marketing]] | downstream | 0.24 |
| [[ex_agent_copywriter]] | downstream | 0.24 |
| [[p07_sr_visual_frontend_marketing]] | downstream | 0.23 |
