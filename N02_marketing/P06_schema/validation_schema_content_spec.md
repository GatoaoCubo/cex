---
id: validation_schema_content_spec
kind: validation_schema
pillar: P06
nucleus: n02
title: "Content Format Validation Schema"
version: 1.0.0
quality: 9.0
tags: [validation_schema, content_spec, format_rules, character_limits, P06, n02_marketing]
domain: content-validation
status: active
density_score: 1.0
related:
  - ex_response_format_ad_copy
  - p03_pt_marketing_task_execution
  - brand_voice_templates
  - n02_tool_copy_analyzer
  - ad_copy_template
  - ex_prompt_template_aida
  - tpl_content_distribution_plan
  - p01_kc_ayrshare_api
  - landing_page_template
  - p03_sp_marketing_nucleus
---

# Content Format Validation Schema

## Purpose

Every piece of copy N02 generates MUST pass this schema before leaving the pipeline.
Character limits are not suggestions. Tone rules are not preferences. They are gates.
Bad copy that ships is worse than no copy at all.

## Platform Character Limits

| Platform | Asset Type | Headline | Body | CTA | Hashtags |
|----------|-----------|---------|------|-----|---------|
| Instagram | Post | 125 (above fold) | 2200 max | N/A | 30 max |
| Instagram | Story | N/A | 250 max | 25 (button label) | 10 |
| Instagram | Reel | 150 | 2200 | N/A | 30 |
| LinkedIn | Post | 150 | 3000 | N/A | 5 recommended |
| LinkedIn | Article | 150 | 120000 | N/A | 5 max |
| LinkedIn | Ad | 150 | 600 | 25 | N/A |
| X (Twitter) | Post | N/A | 280 | N/A | 2 recommended |
| Meta Ads | Headline | 40 | 125 | 25 | N/A |
| Meta Ads | Carousel | 40 per card | 125 | 25 | N/A |
| Email | Subject | 50 (40 mobile) | unlimited | 45 (button) | N/A |
| TikTok | Caption | N/A | 2200 | N/A | 30 max |
| YouTube | Title | 100 (70 visible) | unlimited | N/A | 15 max |

## Tone Rule Matrix

| Brand Voice | Allowed Patterns | Blocked Patterns |
|------------|-----------------|-----------------|
| `bold` | Direct imperatives, strong verbs, short punchy sentences | Passive constructions, qualifiers ("might", "could"), apologies |
| `conversational` | First-person plural, questions, contractions | Jargon, corporate-speak, passive voice |
| `professional` | Third-person or formal second, credentials, data citations | Slang, emoji overuse, exclamation marks |
| `playful` | Wordplay, alliteration, pop culture refs, emoji | Dry statistics, legal disclaimers as primary content |
| `authoritative` | Definitive statements, industry statistics, expert quotes | Hedging, uncertainty language, "we believe" |
| `empathetic` | Validation language, pain-point mirroring, second person warm | Prescriptive commands, statistics without context |

## CTA Requirements

```yaml
cta_rules:
  required_when:
    - campaign_goal: [conversion, consideration]
  format:
    - verb_first: true               # "Get", "Start", "Discover" -- not "Our product lets you..."
    - max_words: 5                   # "Start your free trial today" = OK; longer = truncate
    - no_passive: true
    - urgency_alignment: true        # if urgency_trigger=deadline -> CTA includes time signal
  forbidden_ctas:
    - "Click here"
    - "Learn more" (standalone, no context)
    - "Submit"
    - "Buy now" (unless ecommerce with explicit product)
  recommended_patterns:
    awareness: ["Discover [benefit]", "See how [outcome]", "Meet [product]"]
    consideration: ["Get the [resource]", "Watch the [demo]", "Read the [case study]"]
    conversion: ["Start [trial/free/today]", "Claim your [offer]", "Book a [demo/call]"]
    retention: ["Unlock [feature]", "Upgrade to [tier]", "Renew and [benefit]"]
```

## Brand Voice Compliance Rules

```yaml
voice_compliance:
  readability_target: "Flesch-Kincaid grade 8 or below for B2C; 10 or below for B2B"
  sentence_length_max: 25 words (soft limit)
  paragraph_length_max: 3 sentences for social; 5 for email
  active_voice_ratio: "> 80% of sentences"
  emoji_rules:
    playful: 1-3 per post, thematically relevant
    conversational: 0-2 per post
    professional: 0-1 per post (decorative only)
    bold: 0-1 per post
    authoritative: 0 (never)
    empathetic: 0-2 per post
  forbidden_phrases:
    - "game-changer"
    - "revolutionary"
    - "world-class"
    - "synergy"
    - "leverage" (as noun)
    - "solutions" (standalone)
    - "seamlessly"
    - "cutting-edge"
```

## Validation Output Schema

```yaml
validation_result:
  passed: boolean
  score: float (0.0-1.0)
  violations:
    - field: string
      rule: string
      severity: error|warning
      detail: string
      suggestion: string
  platform_compliance:
    - channel: string
      format: string
      compliant: boolean
      overages: {field: chars_over}
  tone_score: float (0.0-1.0)
  cta_present: boolean
  cta_compliant: boolean
```

## Downstream Consumers

- `workflow_campaign_pipeline.md` -- validation gate at F7 GOVERN step
- `content_filter_n02.md` -- reads this schema for automated filtering
- `ab_test_config_n02.md` -- validates each variant before registering test
- `self_improvement_loop_n02.md` -- uses violation patterns as learning signal

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ex_response_format_ad_copy]] | upstream | 0.33 |
| [[p03_pt_marketing_task_execution]] | upstream | 0.24 |
| [[brand_voice_templates]] | upstream | 0.23 |
| [[n02_tool_copy_analyzer]] | upstream | 0.23 |
| [[ad_copy_template]] | upstream | 0.23 |
| [[ex_prompt_template_aida]] | upstream | 0.22 |
| [[tpl_content_distribution_plan]] | upstream | 0.22 |
| [[p01_kc_ayrshare_api]] | upstream | 0.22 |
| [[landing_page_template]] | upstream | 0.19 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.19 |
