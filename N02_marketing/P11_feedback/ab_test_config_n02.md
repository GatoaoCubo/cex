---
id: ab_test_config_n02
kind: ab_test_config
pillar: P11
nucleus: n02
title: "A/B Test Configuration -- Copy Variant Testing"
version: 1.0.0
quality: null
tags: [ab_test_config, copy_variants, conversion_optimization, P11, n02_marketing]
domain: performance-creative
status: active
---

# A/B Test Configuration -- Copy Variant Testing

## Purpose

Gut feelings don't scale. A/B testing turns creative intuition into data.
This config governs how N02 structures, deploys, and concludes copy experiments.

## Test Taxonomy

| Test Type | What Varies | Use When |
|-----------|------------|---------|
| `headline_test` | Hook, first line, subject line | CTR optimization |
| `cta_test` | CTA verb, phrasing, urgency | Conversion rate optimization |
| `tone_test` | Brand voice variant | New audience, new platform |
| `format_test` | Content format (post vs. carousel vs. reel) | Content_format selection |
| `length_test` | Copy length (short vs. long-form) | Engagement vs. click optimization |
| `hook_test` | Hook type (pain|curiosity|data|social_proof|authority) | TOFU awareness campaigns |
| `urgency_test` | Urgency trigger present vs. absent | MOFU/BOFU conversion lift |

## Test Configuration Schema

```yaml
ab_test:
  id: "test_{campaign_id}_{sequence}"
  type: headline_test|cta_test|tone_test|format_test|length_test|hook_test|urgency_test
  hypothesis: string               # "Adding scarcity to CTA increases conversion by 15%"
  campaign_id: string
  platform: instagram|linkedin|x|meta|email
  primary_metric: ctr|conversion_rate|engagement_rate|cpa
  secondary_metrics: array[string]

  traffic_split:
    control: 0.50                  # proportion of audience (0.0-1.0)
    treatment: 0.50                # must sum to 1.0

  sample_size:
    min_impressions_per_variant: 1000
    min_conversions_per_variant: 50  # for conversion tests
    confidence_level: 0.95
    power: 0.80

  runtime:
    start_date: string
    max_days: 14                   # hard stop even if undecided
    early_stop_threshold: 0.99    # stop if significance exceeds this

  variants:
    control:
      label: "A"
      description: string
      copy_asset_id: string
      copy_snapshot: string        # full copy text at test registration
    treatment:
      label: "B"
      description: string
      copy_asset_id: string
      copy_snapshot: string

  winner_rule: significance|practical_significance|hybrid
  winner_min_lift: 0.10           # minimum meaningful improvement (10%)
```

## Variant Generation Protocol

When `a_b_testing: true` in campaign brief:

```yaml
variant_generation:
  generate_count: 2                # default 2 variants (A/B); max 4 (A/B/C/D)
  isolation_principle: change_one_variable   # never test 2 variables simultaneously
  naming_convention: "{test_type}_{date}_{variant_letter}"

  auto_variants:
    headline_test:
      A: pain-point-first hook
      B: curiosity-gap hook
    cta_test:
      A: action verb + benefit ("Get more clients")
      B: action verb + urgency ("Get more clients before Friday")
    tone_test:
      A: brand_voice from brief
      B: adjacent tone (bold -> conversational)
```

## Statistical Evaluation Rules

```python
# Winner declaration logic

def declare_winner(test_result):
    p_value = test_result["p_value"]
    lift = test_result["relative_lift"]
    impressions = test_result["total_impressions"]

    if p_value < 0.05 and lift > 0.10 and impressions >= 2000:
        return "treatment_wins"
    elif p_value < 0.05 and lift < -0.10:
        return "control_wins"
    elif test_result["days_running"] >= 14:
        return "inconclusive"     # time-boxed termination
    else:
        return "continue"
```

## Results Schema

```yaml
ab_test_result:
  test_id: string
  status: running|concluded|inconclusive|stopped_early
  winner: control|treatment|none
  confidence: float
  relative_lift: float            # (treatment - control) / control
  absolute_lift: float
  control_metric: float
  treatment_metric: float
  impressions:
    control: integer
    treatment: integer
  learning:
    summary: string               # plain language: "Scarcity CTA lifted CVR 18% on LinkedIn"
    promote_to_rulebook: boolean
    hypothesis_confirmed: boolean
```

## Exclusion Rules (Do Not Test)

- Brand identity elements (logo, brand name spelling)
- Legal disclaimer copy
- Accessibility text (alt text, ARIA labels)
- Competitor mentions
- Price points without legal/finance sign-off

## Integration

- Feeds into: `self_improvement_loop_n02.md` (winner rules -> rulebook)
- Triggered by: `workflow_campaign_pipeline.md` (when `a_b_testing: true`)
- Validated by: `validation_schema_content_spec.md` (both variants must pass)
- Audience data from: `cohort_analysis_n02.md` (segment performance context)
