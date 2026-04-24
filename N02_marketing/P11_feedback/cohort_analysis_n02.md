---
id: cohort_analysis_n02
kind: cohort_analysis
8f: F4_reason
pillar: P07
nucleus: n02
title: "Campaign Audience Cohort Analysis"
version: 1.0.0
quality: 9.0
tags: [cohort_analysis, audience_segmentation, campaign_performance, P11, n02_marketing]
domain: audience-intelligence
status: active
density_score: 1.0
related:
  - cohort-analysis-builder
  - kc_cohort_analysis
  - bld_instruction_cohort_analysis
  - p10_mem_cohort_analysis_builder
  - bld_knowledge_card_cohort_analysis
  - p03_sp_cohort_analysis_builder
  - bld_schema_cohort_analysis
  - bld_output_template_cohort_analysis
  - leverage_map_v2_n06_verification
  - bld_examples_cohort_analysis
---

# Campaign Audience Cohort Analysis

## Purpose

Not all audiences respond to the same copy. Cohort analysis answers:
WHO is converting, WHEN they convert, and WHY certain segments disengage.
Without this, N02 produces copy that averages across segments -- and average
copy converts no one.

## Cohort Definition

A cohort is a group of audience members who share a defining characteristic
observed at the same point in time.

### Cohort Types

| Type | Defining Characteristic | Use |
|------|------------------------|-----|
| `acquisition_cohort` | First exposure to brand content | Funnel stage tracking |
| `campaign_cohort` | First exposed in specific campaign | Campaign attribution |
| `channel_cohort` | Acquired via specific platform | Channel ROI |
| `segment_cohort` | ICP-segment membership | Message-market fit |
| `behavioral_cohort` | Triggered by action (click, save, comment) | Retargeting precision |
| `temporal_cohort` | Active in specific time window | Seasonality effects |

## Cohort Schema

```yaml
cohort:
  id: "cohort_{type}_{date}_{label}"
  type: acquisition|campaign|channel|segment|behavioral|temporal
  label: string                         # human-readable: "LinkedIn leads Q1 2026"
  definition_criteria: string           # machine-readable filter
  cohort_date: ISO 8601 date            # when cohort was defined
  size: integer                         # member count at definition
  platform_source: instagram|linkedin|x|meta|email|organic
  campaign_id: string (nullable)
  icp_segment: string (nullable)        # maps to customer_segment_n02.md
```

## Retention Curve Schema

```yaml
retention_data:
  cohort_id: string
  measurement_unit: day|week|month
  periods:
    - period: 0
      retained_count: integer           # = cohort size (period 0 = 100%)
      retention_rate: 1.0
    - period: 1
      retained_count: integer
      retention_rate: float
    # ... continues per period
  churn_events:
    - period: integer
      churn_trigger: string             # inferred or tagged reason
      recovery_action: string           # retargeting sequence to trigger
```

## Engagement Funnel per Cohort

```
AWARENESS    -> content reach, impressions
CONSIDERATION -> profile visits, link clicks, saves
CONVERSION   -> form fills, purchases, sign-ups
RETENTION    -> repeat engagement, subscription renewal
ADVOCACY     -> shares, tags, referrals
```

Track each cohort's distribution across funnel stages per campaign week.
Expected shape: narrow funnel (high attrition AWARENESS->CONSIDERATION is normal).
Alert when attrition is STEEPER than benchmark at CONSIDERATION->CONVERSION.

## Benchmarks

| Cohort Stage | Expected Drop | Alert Threshold |
|-------------|--------------|----------------|
| Awareness -> Consideration | 90-95% drop | < 2% CTR |
| Consideration -> Conversion | 80-90% drop | < 1% CVR |
| Conversion -> Retention | 40-60% drop | < 40% 30-day retention |
| Retention -> Advocacy | 70-80% drop | NPS < 40 |

## Analysis Queries

```yaml
standard_analyses:
  - name: "Best performing cohort by CVR"
    group_by: [cohort_type, platform_source]
    metric: conversion_rate
    filter: impressions >= 500

  - name: "Cohort decay rate comparison"
    group_by: [icp_segment]
    metric: retention_rate
    period: week_4
    comparison: vs_campaign_average

  - name: "Channel-specific BOFU cohort quality"
    group_by: [platform_source]
    filter: funnel_stage == BOFU
    metric: [conversion_rate, cost_per_acquisition]

  - name: "Lookalike audience lift"
    group_by: [is_lookalike]
    metric: [ctr, cvr]
    hypothesis_test: true
```

## Copy Implication Rules

| Cohort Insight | Copy Action |
|---------------|------------|
| High engagement, low conversion | MOFU copy: add social proof, reduce friction |
| Low initial engagement | TOFU hook test: switch hook_type in ab_test_config |
| High early churn | Retention sequence: urgency + value reminder |
| Advocacy-stage cohort | Referral ask copy: social proof + reward |
| Segment A >> Segment B | Invest more creative budget in Segment A ICP |

## Integration

- Consumes: `customer_segment_n02.md` (ICP definitions)
- Consumes: `nps_survey_n02.md` (retention signal)
- Feeds into: `self_improvement_loop_n02.md` (segment performance signals)
- Feeds into: `ab_test_config_n02.md` (audience split design)
- Referenced by: `workflow_campaign_pipeline.md` (post-campaign analysis step)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[cohort-analysis-builder]] | related | 0.44 |
| [[kc_cohort_analysis]] | upstream | 0.43 |
| [[bld_instruction_cohort_analysis]] | upstream | 0.42 |
| [[p10_mem_cohort_analysis_builder]] | downstream | 0.39 |
| [[bld_knowledge_card_cohort_analysis]] | upstream | 0.39 |
| [[p03_sp_cohort_analysis_builder]] | upstream | 0.39 |
| [[bld_schema_cohort_analysis]] | upstream | 0.30 |
| [[bld_output_template_cohort_analysis]] | upstream | 0.30 |
| [[leverage_map_v2_n06_verification]] | upstream | 0.30 |
| [[bld_examples_cohort_analysis]] | related | 0.29 |
