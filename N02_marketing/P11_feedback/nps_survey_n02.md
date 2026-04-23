---
id: nps_survey_n02
kind: nps_survey
pillar: P11
nucleus: n02
title: "Audience Satisfaction NPS Survey -- N02 Marketing"
version: 1.0.0
quality: 9.0
tags: [nps_survey, audience_satisfaction, brand_sentiment, retention, P11, n02_marketing]
domain: campaign-feedback
status: active
density_score: 1.0
related:
  - bld_schema_tagline
  - n06_schema_brand_config
  - bld_schema_model_registry
  - bld_instruction_nps_survey
  - kc_nps_survey
  - bld_schema_experiment_tracker
  - bld_schema_nps_survey
  - nps-survey-builder
  - bld_schema_optimizer
  - bld_knowledge_card_nps_survey
---

# Audience Satisfaction NPS Survey

## Purpose

CTR and CVR measure what audiences DO. NPS measures what they FEEL.
Both signals are necessary. A high-CTR campaign that destroys brand trust
is a net loss. NPS catches what performance metrics miss: the emotional
residue that either compounds loyalty or accelerates churn.

## Core NPS Question

> "How likely are you to recommend [Brand/Product/Content] to a colleague or friend?"
> Scale: 0 (not at all likely) to 10 (extremely likely)

**Scoring:**
- **Promoters (9-10)**: Loyal, will amplify brand
- **Passives (7-8)**: Satisfied but switchable
- **Detractors (0-6)**: At risk, potentially vocal

**Formula:** NPS = % Promoters - % Detractors
**Target:** >= 40 (good), >= 60 (excellent), >= 70 (world-class)

## Survey Configuration Schema

```yaml
nps_survey:
  id: "nps_{campaign_id}_{wave}"
  trigger:
    type: post_purchase|post_content|post_campaign|periodic|behavioral
    delay_after_trigger_hours: 24    # minimum respect window
    max_surveys_per_user_per_month: 1
  channel: email|in_app|sms|linkedin_message
  language: string

  questions:
    primary:
      text: "How likely are you to recommend [brand] to a colleague?"
      type: nps_scale_0_10
    follow_up_promoter:
      condition: score >= 9
      text: "What made you give us that score? What do you value most?"
      type: open_text
      max_chars: 500
    follow_up_passive:
      condition: score in [7,8]
      text: "What would make you an even bigger fan?"
      type: open_text
      max_chars: 500
    follow_up_detractor:
      condition: score <= 6
      text: "We're sorry to hear that. What went wrong?"
      type: open_text
      max_chars: 500
    optional_segment:
      text: "What best describes you?"
      type: single_choice
      options: ["Founder/CEO", "Marketing Lead", "Developer", "Other"]

  design:
    estimated_completion_seconds: 45
    mobile_first: true
    brand_voice_applied: true
    skip_allowed: true
```

## Response Collection Schema

```yaml
nps_response:
  survey_id: string
  respondent_id: string (anonymized)
  cohort_id: string (from cohort_analysis_n02.md)
  channel_acquired: string
  campaign_id: string (nullable)
  score: integer (0-10)
  category: promoter|passive|detractor
  follow_up_text: string (nullable)
  submitted_at: ISO 8601 datetime
  icp_segment: string (nullable)
```

## Aggregation & Reporting

```yaml
nps_report:
  period: string
  campaign_id: string (nullable, for campaign-specific reports)
  sample_size: integer
  response_rate: float
  nps_score: float                    # -100 to +100
  promoter_pct: float
  passive_pct: float
  detractor_pct: float
  trend:
    vs_previous_period: float
    vs_industry_benchmark: float      # marketing software avg NPS: ~41
  qualitative_themes:
    promoter_themes: array[string]    # extracted from follow-up text
    detractor_themes: array[string]
  segment_breakdown:
    by_icp_segment: {segment: nps_score}
    by_channel: {channel: nps_score}
    by_campaign: {campaign_id: nps_score}
```

## Industry Benchmarks

| Category | NPS Benchmark |
|---------|--------------|
| B2B SaaS | 30-40 |
| Marketing Agency | 25-35 |
| Content Media | 35-50 |
| E-commerce | 45-60 |
| Enterprise Software | 20-30 |

## Copy Implications from NPS Data

| NPS Signal | Copy Action |
|-----------|------------|
| Promoter theme: "saves time" | Lead all TOFU with time-savings hook |
| Detractor theme: "too promotional" | Reduce direct-response frequency; increase value content |
| Passive theme: "good but generic" | Personalization lift: segment-specific copy |
| Score drop post-campaign | Campaign fatigue signal: reduce frequency or refresh creative |
| High NPS low CVR | Trust is there; friction is somewhere else -- test CTA and landing page |

## Closed-Loop Actions

```yaml
auto_actions:
  detractor:
    if score <= 4:
      trigger: customer_success_alert         # human review
    if score in [5,6]:
      trigger: retention_sequence_email        # automated nurture
  promoter:
    if score >= 9:
      trigger: referral_ask_sequence           # harvesting advocacy
    if score >= 10:
      trigger: testimonial_request_email       # social proof capture
```

## Integration

- Feeds into: `cohort_analysis_n02.md` (satisfaction by cohort)
- Feeds into: `self_improvement_loop_n02.md` (brand sentiment signal)
- Triggers: `workflow_campaign_pipeline.md` (post-campaign measurement step)
- Referenced by: `customer_segment_n02.md` (segment satisfaction profiling)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_tagline]] | upstream | 0.31 |
| [[n06_schema_brand_config]] | upstream | 0.30 |
| [[bld_schema_model_registry]] | upstream | 0.29 |
| [[bld_instruction_nps_survey]] | upstream | 0.29 |
| [[kc_nps_survey]] | upstream | 0.29 |
| [[bld_schema_experiment_tracker]] | upstream | 0.28 |
| [[bld_schema_nps_survey]] | upstream | 0.28 |
| [[nps-survey-builder]] | related | 0.27 |
| [[bld_schema_optimizer]] | upstream | 0.26 |
| [[bld_knowledge_card_nps_survey]] | upstream | 0.25 |
