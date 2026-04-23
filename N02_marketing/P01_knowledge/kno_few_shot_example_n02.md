---
id: kno_few_shot_example_n02
kind: few_shot_example
pillar: P01
nucleus: N02
title: "N02 Marketing Few Shot Example"
version: "1.0.0"
quality: 9.1
tags: [few_shot_example, marketing, prompting, copy, creative_lust, n02]
density_score: 0.99
related:
  - n02_tool_copy_analyzer
  - p07_sr_5d_marketing
  - p03_sp_marketing_nucleus
  - ad_copy_template
  - p08_ac_n02
  - landing_page_template
  - p01_kc_conversion_copywriting_frameworks
  - ex_prompt_template_aida
  - p03_ap_visual_frontend_marketing
  - ex_agent_copywriter
---
<!-- 8F: F1=few_shot_example/P01 F2=few-shot-example-builder F3=nucleus_def_n02+kc_campaign+ab_testing_framework+N02_memory+P01_schema F4=example_for_marketing_prompt_input_output_shape F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P01_knowledge/kno_few_shot_example_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | few_shot_example |
| Pillar | P01 |
| Nucleus | N02 |
| Teaching target | input and output shape for campaign copy generation |
| Creative Lust lens | show how desire, proof, and CTA align in one compact example |
| Difficulty | medium |

## Why This Example Exists

N02 prompts often fail when the model receives a vague brief.
This example teaches the model to convert a structured marketing request into output that is seductive, specific, and operational.
It demonstrates:

1. audience naming
2. pain articulation
3. proof grounding
4. funnel-stage alignment
5. CTA discipline

## Canonical Input

```yaml
input:
  task: create_3_linkedin_ad_variants
  audience: b2b_saas_founders
  funnel_stage: mofu
  offer: conversion_audit
  promise: reduce wasted paid traffic
  proof:
    stat: "23 percent lift in qualified demos"
    basis: "last 6 campaign audits"
  constraints:
    max_chars: 240
    tone: sharp_confident
    cta: book_audit
    banned: [empty_hype, vague_superlatives]
```

## Canonical Output

```yaml
output:
  variant_1:
    angle: pain_to_proof
    copy: "Paid traffic is not expensive. Waste is. We found 23 percent more qualified demos hiding inside underperforming funnels. Book the audit and see where your pipeline leaks first."
    cta: "Book the audit"
  variant_2:
    angle: aspiration_with_evidence
    copy: "The best SaaS teams do not buy more clicks. They turn intent into demos. Our last 6 audits surfaced a 23 percent lift in qualified demand. Book the audit before next spend goes live."
    cta: "Book the audit"
  variant_3:
    angle: objection_breaker
    copy: "If your traffic volume is fine but demos stay soft, the problem is probably not reach. It is conversion friction. Our recent audits uncovered a 23 percent lift opportunity. Book the audit now."
    cta: "Book the audit"
```

## Format Lessons

| Lesson | What the model should learn |
|--------|-----------------------------|
| structured input | a good brief names audience, stage, offer, proof, and constraints |
| structured output | each variant needs an angle, a copy block, and a CTA |
| proof discipline | numeric evidence sits inside the argument, not as an afterthought |
| tone discipline | sharp and confident does not mean manipulative |
| CTA discipline | one clear action per variant |

## Explanation

This example is not about dazzling style alone.
It teaches controlled seduction.
Each output variant preserves one persuasion logic:

| Variant | Logic |
|---------|-------|
| 1 | pain -> proof -> action |
| 2 | aspiration -> credibility -> urgency |
| 3 | objection -> diagnosis -> invitation |

## Why It Fits N02 Memory

The example also reinforces patterns visible in current N02 memory:

| Memory signal | Reflected here |
|---------------|----------------|
| benefit-specific language wins | every variant names an outcome |
| generic CTA loses | each CTA is action specific |
| proof near headline improves trust | proof sits in the body before the CTA |
| vague hype is blocked | no "best ever" filler |

## Edge Cases Covered

| Edge case | Handling |
|-----------|----------|
| short character limit | copy stays compressed but still specific |
| B2B audience skepticism | evidence appears early |
| MOFU stage | copy assumes awareness but not final commitment |
| same CTA across variants | angles vary while action remains stable |

## Variation Ideas

| Variation | What changes |
|-----------|--------------|
| tofu version | replace audit CTA with softer learn-more CTA |
| bofu version | add guarantee and deadline pressure |
| ecommerce version | shift proof from demos to revenue or AOV lift |
| email version | allow longer narrative arc |

## Prompting Rules Derived From This Example

1. Always request at least one proof source or proof placeholder.
2. Name the funnel stage explicitly.
3. Force one CTA family for the batch unless testing CTA itself.
4. Keep banned-language controls in the input.
5. Return angles, not just lines of copy.

## Anti-Patterns

| Anti-pattern | Failure |
|--------------|---------|
| input says "write good ads" | no strategy anchor |
| output has only raw copy lines | hard to compare or test |
| proof omitted | copy sounds inflated |
| multiple CTAs in one line | action diffuses |
| stage omitted | voice drifts between awareness and close |

## Reusable Skeleton

```yaml
few_shot_skeleton:
  input:
    task: artifact_request
    audience: segment
    funnel_stage: tofu_or_mofu_or_bofu
    offer: named_offer
    proof: stat_or_testimonial
    constraints: explicit_limits
  output:
    variant_n:
      angle: persuasion_logic
      copy: final_line
      cta: action
```

## Properties

| Property | Value |
|----------|-------|
| Best use | campaign prompt grounding |
| Output style | structured YAML-like variant pack |
| Main teaching | desire plus proof plus CTA |
| Risk prevented | flashy but untestable responses |
| Save path | N02_marketing/P01_knowledge/kno_few_shot_example_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_tool_copy_analyzer]] | downstream | 0.31 |
| [[p07_sr_5d_marketing]] | downstream | 0.29 |
| [[p03_sp_marketing_nucleus]] | downstream | 0.27 |
| [[ad_copy_template]] | downstream | 0.27 |
| [[p08_ac_n02]] | downstream | 0.26 |
| [[landing_page_template]] | downstream | 0.25 |
| [[p01_kc_conversion_copywriting_frameworks]] | related | 0.24 |
| [[ex_prompt_template_aida]] | downstream | 0.23 |
| [[p03_ap_visual_frontend_marketing]] | downstream | 0.22 |
| [[ex_agent_copywriter]] | downstream | 0.22 |
