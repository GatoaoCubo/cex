---
id: workflow_campaign_pipeline
kind: workflow
pillar: P12
nucleus: n02
title: "End-to-End Campaign Workflow Pipeline"
version: 1.0.0
quality: 8.9
tags: [workflow, campaign_pipeline, brief_to_publish, orchestration, P12, n02_marketing]
domain: campaign-orchestration
status: active
density_score: 1.0
related:
  - p12_wf_marketing_pipeline
  - n02_kc_campaign
  - p12_wf_content_factory_v1
  - p03_ch_brief_to_multiformat
  - n02_tool_copy_analyzer
  - p12_wf_cf_promote
  - p08_ac_n02
  - p03_sp_marketing_nucleus
  - p04_rp_marketing_nucleus
  - p11_qg_marketing_artifacts
---

# End-to-End Campaign Workflow Pipeline

## Purpose

A campaign without a pipeline is an idea. This workflow converts brief input
into deployed, measured creative -- with no steps skipped, no decisions deferred,
and no quality gates bypassed. Creative Lust demands COMPLETION, not just output.

## Pipeline Overview

```
BRIEF INPUT
    |
    v
F1: CONSTRAIN -- validate brief against input_schema_campaign_brief.md
    |
    v
F2: STRATEGIZE -- map brief to funnel stage, content pillars, hook framework
    |
    v
F3: RESEARCH -- load brand_config, audience KCs, competitor intel, past campaign signals
    |
    v
F4: PLAN -- copy variants, A/B structure, scheduling calendar
    |
    v
F5: CREATE -- generate copy assets via action_prompt_n02_copy.md
    |
    v
F6: VALIDATE -- run each asset through validation_schema_content_spec.md
    |         (if fail: regenerate, max 3 attempts)
    |
    v
F7: REVIEW -- optional human review gate (configurable; default: skip for autonomous)
    |
    v
F8: DISTRIBUTE -- publish via social_publisher_n02.md + api_reference_social_apis.md
    |
    v
F9: MEASURE -- collect performance signals (CTR, CVR, engagement)
    |
    v
F10: ANALYZE -- cohort_analysis + ab_test evaluation
    |
    v
F11: EVOLVE -- feed signals into self_improvement_loop_n02.md
    |
    v
F12: ARCHIVE -- store campaign artifacts, commit to repo, signal n07
```

## Stage Definitions

### F1 CONSTRAIN -- Brief Validation

```yaml
inputs:
  - campaign_brief (raw)
outputs:
  - validated_brief (compliant with input_schema_campaign_brief.md)
  - campaign_id (auto-generated)
error_handling:
  - BRIEF_001..005: return error, request correction
gate: all required fields present + validation rules pass
```

### F2 STRATEGIZE -- Intent Resolution

```yaml
inputs:
  - validated_brief
logic:
  - map campaign_goal -> funnel_stage (TOFU/MOFU/BOFU)
  - select hook_framework based on funnel_stage + brand_voice
  - identify content_pillars relevant to this campaign
  - set urgency_trigger if not in brief
outputs:
  - strategy_doc (funnel_stage, hook_type, content_pillar[s], urgency_trigger)
```

### F3 RESEARCH -- Context Assembly

```yaml
load_in_sequence:
  1. .cex/brand/brand_config.yaml (brand voice, colors, values)
  2. N02_marketing/P02_model/customer_segment_n02.md (ICP for target_audience)
  3. N02_marketing/P01_knowledge/kc_marketing_vocabulary.md (controlled vocabulary)
  4. N01_intelligence/ competitor KCs if campaign_goal == awareness
  5. Past campaign signals from self_improvement_loop_n02.md (rulebook)
  6. Platform specs from api_reference_social_apis.md (for each channel in brief)
```

### F4 PLAN -- Production Blueprint

```yaml
outputs:
  - copy_plan:
      assets_count: integer
      variants_count: integer (2 if a_b_testing else 1)
      formats: array (per channel)
      scheduling_calendar: [{asset_id, channel, publish_datetime}]
      ab_test_config: ab_test object (nullable)
gate: plan reviewed and locked before F5 (no scope creep mid-execution)
```

### F5 CREATE -- Copy Generation

```yaml
invokes: action_prompt_n02_copy.md
for_each_asset in copy_plan:
  - inject: brand_voice, ICP, hook_type, CTA, channel, format
  - generate: headline + body + CTA (+ visual brief if multimodal_prompt used)
  - store: draft_copy object with asset_id
max_generation_time_per_asset: 30 seconds
```

### F6 VALIDATE -- Quality Gate

```yaml
invokes: validation_schema_content_spec.md
for_each_draft_copy:
  - check: character limits per platform/format
  - check: tone compliance (brand_voice rules)
  - check: CTA present (if campaign_goal requires)
  - check: forbidden_phrases absent
  - score: 0.0-1.0
  threshold: 0.80 minimum to proceed
retry: max 3 regeneration attempts per asset
on_failure_after_3: flag for human review, pause this asset
```

### F7 REVIEW -- Human Gate (Configurable)

```yaml
default: skip (autonomous mode)
enable_when:
  - campaign budget_usd > 10000
  - is_regulated_industry: true
  - explicit user request
review_interface: handoff to user with preview + approve/reject per asset
timeout: 24 hours (auto-approve if no response and auto_approve: true)
```

### F8 DISTRIBUTE -- Publishing

```yaml
invokes: social_publisher_n02.md
for_each_approved_asset:
  - route to platform API (api_reference_social_apis.md)
  - respect rate_limits per platform
  - log: published_at, platform_post_id, asset_id
  - handle errors: queue failed, retry with backoff
scheduling: honor scheduling_calendar from F4
```

### F9 MEASURE -- Signal Collection

```yaml
collect_after: 24h, 72h, 7d, end_date
signals_per_asset:
  - impressions, clicks, ctr, conversions, cvr
  - engagement_rate, save_rate, share_rate
  - platform_post_id as join key
store_in: performance_signal objects (cohort_analysis_n02.md schema)
```

### F10 ANALYZE -- Post-Campaign Intelligence

```yaml
invoke_sequence:
  1. cohort_analysis_n02.md -- segment breakdown
  2. ab_test_config_n02.md -- winner declaration (if a_b_testing)
  3. nps_survey_n02.md -- trigger survey for conversion cohort
outputs:
  - campaign_summary_report (performance by asset, by channel, by segment)
  - winner_copy (if A/B concluded)
```

### F11 EVOLVE -- Learning Integration

```yaml
invokes: self_improvement_loop_n02.md
with: campaign_summary_report + performance_signals
produces:
  - new_rule_candidates (high performers)
  - failure_archive_entries (low performers)
gate: campaign must have >= 500 impressions total to generate rules
```

### F12 ARCHIVE -- Completion

```yaml
actions:
  - compile all artifacts: python _tools/cex_compile.py N02_marketing/
  - git commit: "[N02] campaign {campaign_id} complete -- {nps_score} NPS, {avg_cvr}% CVR"
  - signal: write_signal('n02', 'campaign_complete', score)
  - archive: move campaign artifacts to N02_marketing/P12_orchestration/archive/
```

## Pipeline Configuration

```yaml
pipeline_config:
  autonomous_mode: true             # runs F1-F12 without human gates
  human_gate_at: F7                 # configurable; null to disable
  max_retries_per_asset: 3
  auto_approve_timeout_hours: 24
  measure_periods_days: [1, 3, 7]
  evolve_min_impressions: 500
  archive_on_complete: true
  commit_on_complete: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_marketing_pipeline]] | sibling | 0.29 |
| [[n02_kc_campaign]] | upstream | 0.27 |
| [[p12_wf_content_factory_v1]] | sibling | 0.25 |
| [[p03_ch_brief_to_multiformat]] | upstream | 0.24 |
| [[n02_tool_copy_analyzer]] | upstream | 0.23 |
| [[p12_wf_cf_promote]] | sibling | 0.22 |
| [[p08_ac_n02]] | upstream | 0.21 |
| [[p03_sp_marketing_nucleus]] | upstream | 0.21 |
| [[p04_rp_marketing_nucleus]] | upstream | 0.21 |
| [[p11_qg_marketing_artifacts]] | upstream | 0.20 |
