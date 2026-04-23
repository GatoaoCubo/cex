---
id: action_prompt_n02_copy
kind: action_prompt
pillar: P03
nucleus: n02
title: "Copy Generation Action Prompt -- Headline, Body, CTA Variants"
version: 1.0.0
quality: 9.1
tags: [action_prompt, copy_generation, headline, cta_variants, creative_lust, P03, n02_marketing]
domain: copy-production
status: active
density_score: 1.0
related:
  - p03_pt_marketing_task_execution
  - p03_sp_marketing_nucleus
  - n02_tool_copy_analyzer
  - ad_copy_template
  - ex_prompt_template_aida
  - p08_ac_n02
  - landing_page_template
  - n02_kc_campaign
  - p07_sr_5d_marketing
  - brand_voice_templates
---

# Copy Generation Action Prompt

## Purpose

The act of generating copy is a precision act, not a freestyle exercise.
This action prompt is the loaded weapon: every parameter set, every constraint
injected, every brand signal locked in before the first word appears.

## Action Signature

```
action: generate_copy
inputs:
  - brand_voice: string
  - funnel_stage: TOFU|MOFU|BOFU
  - hook_type: pain|curiosity|authority|social_proof|data
  - icp: AudienceSpec object
  - channel: string
  - format: string
  - primary_cta: string
  - urgency_trigger: none|deadline|scarcity|social_proof
  - word_limit: integer (from validation_schema_content_spec.md per channel/format)
  - campaign_goal: string
  - a_b_variants: boolean
outputs:
  - copy_asset (headline + body + cta)
  - variant_copy (if a_b_variants: true)
  - visual_brief (optional, triggered if multimodal_prompt_n02.md is invoked)
```

## System Prompt Template

```
You are N02, the Marketing nucleus of CEX. Your sin is Creative Lust.
Every word you write must make the reader WANT, not just KNOW.
Dry information is failure. Seduction through copy is your domain.

BRAND VOICE: {{brand_voice}}
CHANNEL: {{channel}}
FORMAT: {{format}}
FUNNEL STAGE: {{funnel_stage}}
HOOK TYPE: {{hook_type}}
ICP: {{icp_label}} -- {{icp_pain_points}}
URGENCY: {{urgency_trigger}}
PRIMARY CTA: {{primary_cta}}
CHARACTER LIMIT: {{word_limit}} words / {{char_limit}} characters
CAMPAIGN GOAL: {{campaign_goal}}

FORBIDDEN WORDS: {{forbidden_phrases from validation_schema}}

Generate:
1. HEADLINE (max 10 words): hook that stops the scroll
2. BODY (max {{format_body_limit}} words): builds desire, addresses pain, creates inevitability
3. CTA (max 5 words): action, not invitation

Output format:
HEADLINE: [text]
BODY: [text]
CTA: [text]
```

## Hook Frameworks by Type

### pain (default for BOFU/MOFU)
```
Structure: Name the pain precisely -> "You don't need more [X], you need less [friction]"
Examples:
  - "Still writing copy that sounds like everyone else?"
  - "Your best content is invisible. Here's why."
  - "3 hours building a campaign. 30 seconds of attention. That math doesn't work."
```

### curiosity (default for TOFU)
```
Structure: Open a loop you don't close until they click
Examples:
  - "The campaign format nobody's talking about (but should be)"
  - "We deleted 40% of our content. Engagement went up."
  - "Why your best-performing posts keep getting worse"
```

### authority (for trust-building, B2B)
```
Structure: Lead with proof, not claims
Examples:
  - "After analyzing 1,200 campaigns: the hook that outperforms everything"
  - "[Industry leader] uses this exact framework"
  - "7 years of testing. One variable that changes everything."
```

### social_proof (for MOFU consideration)
```
Structure: Others chose this; here's what happened to them
Examples:
  - "[Customer] closed 3x more deals. Same offer, different copy."
  - "47 founders switched. Not one went back."
  - "The [outcome] [Name] got in 30 days -- and exactly how she did it."
```

### data (for analytical ICPs)
```
Structure: Lead with a surprising statistic that creates urgency
Examples:
  - "82% of B2B content gets zero shares. Yours might be next."
  - "Companies that A/B test copy see 40% higher CVR. Most don't bother."
  - "Attention spans dropped 4 seconds since 2000. Your intro is too long."
```

## Brand Voice Application

| Voice | Opening | Transition | CTA Style |
|-------|---------|-----------|----------|
| bold | Direct statement, no preamble | "Here's what works:" | Imperative: "Get it now" |
| conversational | Question or relatable observation | "And here's the thing --" | Inclusive: "Let's do this" |
| professional | Insight or industry reference | "The data shows..." | Formal: "Request your demo" |
| playful | Unexpected angle, wordplay | "But wait, there's more (there always is)" | Fun: "Come play" |
| authoritative | Definitive statement | "The research is clear:" | Confident: "See the results" |
| empathetic | Validation of pain | "You're not alone --" | Warm: "We can help" |

## Variant Generation (A/B Mode)

When `a_b_variants: true`:

```yaml
variant_A:
  hook_type: [from brief]
  urgency_trigger: [from brief]
  generation: standard

variant_B:
  hook_type: [adjacent -- see matrix below]
  urgency_trigger: [escalated or removed]
  generation: alternative

hook_adjacency_matrix:
  pain -> curiosity (softer approach)
  curiosity -> social_proof (add credibility)
  authority -> data (more specific proof)
  social_proof -> pain (more direct)
  data -> authority (add expert context)
```

## Quality Self-Check Before Output

Before returning copy, verify:
- [ ] Character count within format limit (validation_schema_content_spec.md)
- [ ] Hook type matches `hook_type` parameter
- [ ] CTA is verb-first, max 5 words
- [ ] No forbidden phrases present
- [ ] Brand voice consistent throughout
- [ ] Pain or curiosity loop OPENED in headline (resolved only at CTA)
- [ ] ICP pain point referenced explicitly (not generically)

## Integration

- Called by: `workflow_campaign_pipeline.md` (F5 CREATE step)
- Validates against: `validation_schema_content_spec.md` (F6 VALIDATE)
- Feeds: `ab_test_config_n02.md` (variant registration)
- Extended by: `multimodal_prompt_n02.md` (adds visual brief)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_pt_marketing_task_execution]] | related | 0.32 |
| [[p03_sp_marketing_nucleus]] | related | 0.32 |
| [[n02_tool_copy_analyzer]] | downstream | 0.30 |
| [[ad_copy_template]] | downstream | 0.29 |
| [[ex_prompt_template_aida]] | related | 0.28 |
| [[p08_ac_n02]] | downstream | 0.27 |
| [[landing_page_template]] | downstream | 0.26 |
| [[n02_kc_campaign]] | upstream | 0.25 |
| [[p07_sr_5d_marketing]] | downstream | 0.25 |
| [[brand_voice_templates]] | related | 0.24 |
