---
id: p06_is_marketing_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
owner: "n02_marketing"
scope: "marketing campaign creation and content generation operations"
fields:
  - name: "campaign_name"
    type: "string"
    required: true
    default: null
    description: "Unique campaign identifier; slug-safe, 3-80 chars, pattern ^[a-z0-9_-]+$"
    error_message: "campaign_name is required — provide a slug-safe identifier (3-80 chars, lowercase, underscores/hyphens only)"
  - name: "brand_name"
    type: "string"
    required: true
    default: null
    description: "Brand this campaign belongs to; must match brand_config.yaml brand_name exactly"
    error_message: "brand_name is required — must reference a configured brand in brand_config.yaml"
  - name: "marketing_objective"
    type: "string"
    required: true
    default: null
    description: "Campaign goal enum: awareness | conversion | retention | engagement | lead_gen"
    error_message: "marketing_objective is required — must be one of: awareness, conversion, retention, engagement, lead_gen"
  - name: "target_audience"
    type: "string"
    required: true
    default: null
    description: "Natural language description of ideal customer segment (20-500 chars)"
    error_message: "target_audience is required — describe the ideal customer segment in plain text (20-500 chars)"
  - name: "channels"
    type: "list"
    required: true
    default: null
    description: "Distribution channels (min 1): social_media | email | paid_ads | seo | content | influencer"
    error_message: "channels is required — provide at least one channel from: social_media, email, paid_ads, seo, content, influencer"
  - name: "budget"
    type: "float"
    required: false
    default: null
    description: "Campaign budget in USD; null means unset/unlimited; must be >= 0.0 if provided"
    error_message: null
  - name: "tone"
    type: "string"
    required: false
    default: "professional"
    description: "Brand voice for generated content: professional | casual | technical | friendly | bold"
    error_message: null
  - name: "start_date"
    type: "string"
    required: false
    default: null
    description: "Campaign start date YYYY-MM-DD; null means no fixed start"
    error_message: null
  - name: "end_date"
    type: "string"
    required: false
    default: null
    description: "Campaign end date YYYY-MM-DD; must be >= start_date when both provided"
    error_message: null
  - name: "kpis"
    type: "list"
    required: false
    default: []
    description: "KPI identifiers to track: ctr | cpc | roas | cpl | open_rate | conversion_rate"
    error_message: null
  - name: "content_formats"
    type: "list"
    required: false
    default: ["text"]
    description: "Requested output formats: text | image | video | carousel | email | landing_page"
    error_message: null
  - name: "geo_targets"
    type: "list"
    required: false
    default: []
    description: "Geographic targeting: ISO 3166-1 alpha-2 country codes or region names"
    error_message: null
coercion:
  - from: "string"
    to: "float"
    rule: "Parse budget from numeric string ('5000' → 5000.0); reject with type error if non-numeric"
  - from: "string"
    to: "list"
    rule: "Wrap single-item string into list for channels, kpis, content_formats, geo_targets ('email' → ['email'])"
  - from: "YYYYMMDD|DD-MM-YYYY|DD/MM/YYYY"
    to: "YYYY-MM-DD"
    rule: "Normalize start_date and end_date to ISO 8601; reject if unparseable"
examples:
  - campaign_name: "spring_launch_2026"
    brand_name: "AcmeCorp"
    marketing_objective: "conversion"
    target_audience: "B2B SaaS founders aged 30-50 seeking workflow automation tools"
    channels: ["email", "paid_ads", "social_media"]
    budget: 12000.0
    tone: "professional"
    start_date: "2026-04-15"
    end_date: "2026-05-15"
    kpis: ["cpl", "conversion_rate"]
    content_formats: ["text", "email", "landing_page"]
    geo_targets: ["US", "GB", "CA"]
  - campaign_name: "brand_awareness_q2"
    brand_name: "AcmeCorp"
    marketing_objective: "awareness"
    target_audience: "Tech-forward consumers interested in productivity tools"
    channels: ["social_media"]
    budget: null
    tone: "casual"
    start_date: null
    end_date: null
    kpis: []
    content_formats: ["text"]
    geo_targets: []
domain: "marketing"
quality: 9.1
tags: [input-schema, marketing, campaign, data-model, P06]
tldr: "Input contract for marketing campaign creation: requires name, brand, objective, audience, channels; optional budget, tone, dates, KPIs, formats, geo."
keywords: [marketing, campaign, input_schema, brand, objective, audience, channels, budget, tone, kpis, content_formats, geo_targets, coercion]
density_score: 0.91
related:
  - bld_schema_reranker_config
  - bld_schema_input_schema
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_multimodal_prompt
  - bld_schema_nps_survey
  - bld_schema_audit_log
  - bld_schema_eval_metric
  - bld_schema_app_directory_entry
  - bld_schema_sandbox_spec
---
## Contract Definition

Marketing campaign creation and content generation operations receive structured input defining brand context, campaign strategy, and execution parameters. Callers supply five required fields (campaign identity, brand reference, strategic objective, target audience, and distribution channels) plus up to seven optional fields governing budget, voice, timing, measurement, output formats, and geography. The receiver — N02 marketing nucleus or any campaign builder — produces campaign briefs, copy variants, and content artifacts aligned strictly with caller-provided parameters. This schema is unilateral: it defines only what goes in; output shape is defined by the corresponding formatter or interface artifact.

## Fields

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | campaign_name | string | YES | — | Slug-safe campaign identifier (3-80 chars, ^[a-z0-9_-]+$) |
| 2 | brand_name | string | YES | — | Brand reference matching brand_config.yaml brand_name |
| 3 | marketing_objective | string | YES | — | Enum: awareness, conversion, retention, engagement, lead_gen |
| 4 | target_audience | string | YES | — | Ideal customer segment description (20-500 chars) |
| 5 | channels | list | YES | — | Distribution channels, min 1 entry |
| 6 | budget | float | NO | null | Campaign budget USD; null = unset; must be >= 0.0 |
| 7 | tone | string | NO | "professional" | Brand voice: professional, casual, technical, friendly, bold |
| 8 | start_date | string | NO | null | Campaign start YYYY-MM-DD |
| 9 | end_date | string | NO | null | Campaign end YYYY-MM-DD; must be >= start_date |
| 10 | kpis | list | NO | [] | KPI identifiers: ctr, cpc, roas, cpl, open_rate, conversion_rate |
| 11 | content_formats | list | NO | ["text"] | Output formats: text, image, video, carousel, email, landing_page |
| 12 | geo_targets | list | NO | [] | ISO 3166-1 alpha-2 codes or region names |

## Validation Constraints

| Field | Constraint |
|-------|-----------|
| campaign_name | 3-80 chars; pattern `^[a-z0-9_-]+$` |
| marketing_objective | Enum: awareness \| conversion \| retention \| engagement \| lead_gen |
| target_audience | 20-500 chars |
| channels | min 1 item; each in: social_media, email, paid_ads, seo, content, influencer |
| budget | float >= 0.0 if not null |
| tone | Enum: professional \| casual \| technical \| friendly \| bold |
| start_date / end_date | ISO 8601 `\d{4}-\d{2}-\d{2}`; end_date >= start_date when both set |
| content_formats | Each in: text, image, video, carousel, email, landing_page |
| geo_targets | ISO 3166-1 alpha-2 or recognized region name |

## Coercion Rules

| From | To | Field(s) | Rule |
|------|----|----------|------|
| string | float | budget | Parse numeric string ("5000" → 5000.0); reject with type error if non-numeric |
| string | list | channels, kpis, content_formats, geo_targets | Wrap single-item string in list ("email" → ["email"]) |
| YYYYMMDD / DD-MM-YYYY / DD/MM/YYYY | YYYY-MM-DD | start_date, end_date | Normalize to ISO 8601; reject if unparseable |

## Examples

```json
{
  "campaign_name": "spring_launch_2026",
  "brand_name": "AcmeCorp",
  "marketing_objective": "conversion",
  "target_audience": "B2B SaaS founders aged 30-50 seeking workflow automation tools",
  "channels": ["email", "paid_ads", "social_media"],
  "budget": 12000.0,
  "tone": "professional",
  "start_date": "2026-04-15",
  "end_date": "2026-05-15",
  "kpis": ["cpl", "conversion_rate"],
  "content_formats": ["text", "email", "landing_page"],
  "geo_targets": ["US", "GB", "CA"]
}
```

```json
{
  "campaign_name": "brand_awareness_q2",
  "brand_name": "AcmeCorp",
  "marketing_objective": "awareness",
  "target_audience": "Tech-forward consumers interested in productivity tools",
  "channels": ["social_media"],
  "budget": null,
  "tone": "casual",
  "start_date": null,
  "end_date": null,
  "kpis": [],
  "content_formats": ["text"],
  "geo_targets": []
}
```

## References
- OpenAPI requestBody specification (spec.openapis.org)
- IAB Content Taxonomy 3.0 — channel and format classification
- ISO 3166-1 alpha-2 country code registry (iso.org)
- Pydantic BaseModel field validation patterns (docs.pydantic.dev)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | related | 0.35 |
| [[bld_schema_input_schema]] | related | 0.35 |
| [[bld_schema_integration_guide]] | related | 0.34 |
| [[bld_schema_benchmark_suite]] | related | 0.34 |
| [[bld_schema_multimodal_prompt]] | related | 0.34 |
| [[bld_schema_nps_survey]] | related | 0.34 |
| [[bld_schema_audit_log]] | related | 0.33 |
| [[bld_schema_eval_metric]] | related | 0.33 |
| [[bld_schema_app_directory_entry]] | related | 0.33 |
| [[bld_schema_sandbox_spec]] | related | 0.32 |
