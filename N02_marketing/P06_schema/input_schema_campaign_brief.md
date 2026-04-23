---
id: input_schema_campaign_brief
kind: input_schema
pillar: P06
nucleus: n02
title: "Campaign Brief Input Schema"
version: 1.0.0
quality: 9.0
tags: [input_schema, campaign_brief, brand_contract, P06, n02_marketing]
domain: campaign-intake
status: active
density_score: 1.0
related:
  - n06_schema_brand_config
  - p06_is_marketing_data_model
  - bld_schema_model_registry
  - bld_schema_multimodal_prompt
  - bld_schema_training_method
  - bld_schema_tagline
  - bld_schema_experiment_tracker
  - bld_schema_validation_schema
  - bld_schema_input_schema
  - p06_is_brand_data_model
---

# Campaign Brief Input Schema

## Purpose

Canonical contract between brief-giver and N02. Every campaign begins here.
No schema compliance = no execution. Zero ambiguity. Zero wasted creative cycles.

## Required Fields

| Field | Type | Constraints | Description |
|-------|------|-------------|-------------|
| `brand_name` | string | max 100 chars, non-empty | Legal or trade brand identifier |
| `campaign_goal` | enum | `awareness\|consideration\|conversion\|retention\|advocacy` | Primary funnel objective |
| `target_audience` | object | see AudienceSpec | ICP definition |
| `channels` | array[enum] | min 1; `instagram\|linkedin\|x\|meta\|email\|tiktok\|youtube\|search` | Distribution surfaces |
| `content_formats` | array[enum] | min 1; `post\|story\|reel\|carousel\|email\|ad_creative\|long_form\|short_form` | Asset types required |
| `budget_usd` | number | > 0, nullable | Total campaign budget (null = organic only) |
| `start_date` | string | ISO 8601 date | Campaign activation date |
| `end_date` | string | ISO 8601 date, after start | Campaign close date |
| `brand_voice` | enum | `professional\|conversational\|playful\|authoritative\|empathetic\|bold` | Tone of voice |
| `primary_cta` | string | max 80 chars | Single conversion action to drive |

## Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `campaign_id` | string | auto-generated | Internal tracking identifier |
| `tagline` | string | null | Campaign-level headline constraint |
| `competitor_avoid` | array[string] | [] | Brand names to not reference |
| `content_pillar` | string | null | Strategic content pillar this campaign supports |
| `funnel_stage` | enum | derived from `campaign_goal` | `TOFU\|MOFU\|BOFU` |
| `urgency_trigger` | enum | `none\|deadline\|scarcity\|social_proof` | Persuasion mechanism |
| `retargeting_window_days` | integer | 30 | Attribution window for paid |
| `a_b_testing` | boolean | false | Whether to generate variant sets |
| `language` | string | `pt-BR\|en-US\|es-ES` | Output language |
| `reference_assets` | array[url] | [] | Brand inspiration / style references |

## AudienceSpec Object

```yaml
audience:
  icp_label: string          # e.g. "Mid-market SaaS CMO"
  age_range: [min, max]      # integers 13-99
  pain_points: array[string] # jobs-to-be-done framing
  psychographics: string     # lifestyle, values, aspirations
  platform_behavior: string  # how they consume content on channel
  lookalike_source: string   # nullable -- seed audience identifier
```

## Validation Rules

```yaml
rules:
  - end_date > start_date
  - if campaign_goal == conversion: primary_cta is required and non-empty
  - if a_b_testing == true: content_formats must include at least 2 items
  - if budget_usd > 0: at least one paid channel (meta|x|linkedin|search) in channels
  - brand_voice must be consistent with existing brand_config.yaml if present
```

## Example (Minimum Valid Brief)

```yaml
brand_name: "Gato3"
campaign_goal: conversion
target_audience:
  icp_label: "Startup founder, 28-45, tech-savvy"
  pain_points: ["too many tools", "no time to build brand", "generic AI output"]
channels: [instagram, linkedin]
content_formats: [post, carousel]
budget_usd: null
start_date: "2026-05-01"
end_date: "2026-05-31"
brand_voice: bold
primary_cta: "Start your free trial"
```

## Downstream Consumers

- `validation_schema_content_spec.md` -- validates output against brief constraints
- `workflow_campaign_pipeline.md` -- brief is F1 CONSTRAIN input
- `action_prompt_n02_copy.md` -- brief fields injected as copy parameters
- `ab_test_config_n02.md` -- `a_b_testing` flag activates variant generation

## Error Responses

| Error Code | Condition | Recovery |
|-----------|-----------|---------|
| `BRIEF_001` | Missing required field | Return field name + expected type |
| `BRIEF_002` | Date inversion | Prompt for corrected end_date |
| `BRIEF_003` | No paid channel for budget | Warn user or zero out budget |
| `BRIEF_004` | Conflicting brand_voice | Load brand_config.yaml and suggest |
| `BRIEF_005` | CTA missing for conversion goal | Force CTA entry before proceeding |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_schema_brand_config]] | related | 0.46 |
| [[p06_is_marketing_data_model]] | sibling | 0.44 |
| [[bld_schema_model_registry]] | related | 0.38 |
| [[bld_schema_multimodal_prompt]] | related | 0.35 |
| [[bld_schema_training_method]] | related | 0.34 |
| [[bld_schema_tagline]] | related | 0.33 |
| [[bld_schema_experiment_tracker]] | related | 0.33 |
| [[bld_schema_validation_schema]] | related | 0.33 |
| [[bld_schema_input_schema]] | related | 0.33 |
| [[p06_is_brand_data_model]] | sibling | 0.32 |
