---
id: customer_segment_n02
kind: customer_segment
8f: F4_reason
pillar: P02
nucleus: n02
title: "ICP-Typed Audience Segment Definitions"
version: 1.0.0
quality: 8.9
tags: [customer_segment, ICP, audience_segments, message_market_fit, P02, n02_marketing]
domain: audience-intelligence
status: active
density_score: 0.99
related:
  - n06_schema_brand_config
  - bld_schema_model_registry
  - bld_schema_tagline
  - bld_schema_training_method
  - bld_schema_customer_segment
  - bld_schema_experiment_tracker
  - bld_schema_multimodal_prompt
  - bld_schema_model_architecture
  - bld_schema_webinar_script
  - n06_kc_icp_frameworks
---

# ICP-Typed Audience Segment Definitions

## Purpose

Generic copy performs generically. Segment-aware copy converts.
These ICP-typed segment definitions are the lens through which N02
views every brief -- not "who is this for?" but "which segment has
the highest message-market fit for this copy approach?"

## Segment Taxonomy

### Segment Structure

```yaml
segment:
  id: string
  label: string                        # short human label
  icp_descriptor: string               # detailed ICP profile
  demographics:
    age_range: [min, max]
    role_seniority: c_suite|vp|director|manager|individual_contributor
    company_size: startup|smb|mid_market|enterprise
    industry: array[string]
  psychographics:
    primary_motivation: string         # jobs-to-be-done framing
    primary_fear: string               # loss aversion anchor
    aspirational_identity: string      # who they want to become
    content_consumption: string        # how they consume content
  platform_behavior:
    primary_platforms: array[string]
    peak_engagement_hours: array[string]
    content_format_preference: string
  message_market_fit:
    hook_type: pain|curiosity|authority|social_proof|data
    preferred_tone: string
    cta_style: string
    urgency_response: low|medium|high
  funnel_entry:
    typical_stage: TOFU|MOFU|BOFU
    avg_sales_cycle_days: integer
    nurture_touches_avg: integer
```

## Core ICP Segments

### SEG_01 -- Founder/CEO (Startup, 1-50 employees)

```yaml
id: SEG_01
label: "Bootstrapped Founder"
icp_descriptor: "Solo founder or early-stage CEO, 28-42, wearing all hats"
demographics:
  age_range: [26, 45]
  role_seniority: c_suite
  company_size: startup
  industry: [saas, consulting, ecommerce, creator_economy]
psychographics:
  primary_motivation: "Build something that lasts without burning out"
  primary_fear: "Wasting time on the wrong thing while competitors move faster"
  aspirational_identity: "Respected founder who built an efficient, profitable company"
  content_consumption: "Podcasts at 1.5x, Twitter/X threads, LinkedIn Sunday evenings"
platform_behavior:
  primary_platforms: [linkedin, x]
  peak_engagement_hours: ["06:30-08:00", "20:00-22:00"]
  content_format_preference: "Thread, short-form insight, data-backed post"
message_market_fit:
  hook_type: pain
  preferred_tone: conversational
  cta_style: "low-friction -- 'See how' beats 'Buy now'"
  urgency_response: medium
funnel_entry:
  typical_stage: TOFU
  avg_sales_cycle_days: 14
  nurture_touches_avg: 5
```

### SEG_02 -- Marketing Director/VP (Mid-Market, 50-500 employees)

```yaml
id: SEG_02
label: "Marketing Director, Mid-Market"
icp_descriptor: "Director or VP of Marketing, accountable to CEO and sales"
demographics:
  age_range: [32, 50]
  role_seniority: director
  company_size: mid_market
  industry: [b2b_saas, professional_services, fintech, healthtech]
psychographics:
  primary_motivation: "Prove marketing drives revenue, not just brand metrics"
  primary_fear: "Budget cut when CMO asks for ROI data and I don't have it"
  aspirational_identity: "Strategic CMO who built a growth machine"
  content_consumption: "LinkedIn feed daily, industry newsletters, case studies"
platform_behavior:
  primary_platforms: [linkedin]
  peak_engagement_hours: ["07:30-09:00", "12:00-13:00", "17:00-18:30"]
  content_format_preference: "Long-form post, carousel, case study, webinar"
message_market_fit:
  hook_type: data
  preferred_tone: professional
  cta_style: "Resource-first -- 'Get the playbook', 'Download the report'"
  urgency_response: low
funnel_entry:
  typical_stage: MOFU
  avg_sales_cycle_days: 45
  nurture_touches_avg: 12
```

### SEG_03 -- Content Creator / Personal Brand (Solopreneur)

```yaml
id: SEG_03
label: "Creator / Personal Brand"
icp_descriptor: "Solopreneur monetizing expertise via content, coaching, or courses"
demographics:
  age_range: [24, 40]
  role_seniority: individual_contributor
  company_size: startup
  industry: [creator_economy, education, consulting, coaching]
psychographics:
  primary_motivation: "Turn knowledge into income without a corporate job"
  primary_fear: "Invisible in a crowded feed; followers who don't convert"
  aspirational_identity: "Recognized authority in niche with a paid community"
  content_consumption: "Instagram Reels, TikTok, YouTube long-form"
platform_behavior:
  primary_platforms: [instagram, tiktok, youtube]
  peak_engagement_hours: ["09:00-11:00", "19:00-21:00"]
  content_format_preference: "Reel, carousel, educational series"
message_market_fit:
  hook_type: social_proof
  preferred_tone: conversational
  cta_style: "Social -- 'Join 2,000 creators who...', 'See what others built'"
  urgency_response: high
funnel_entry:
  typical_stage: TOFU
  avg_sales_cycle_days: 7
  nurture_touches_avg: 3
```

### SEG_04 -- Enterprise Buyer (Large Corp, 500+ employees)

```yaml
id: SEG_04
label: "Enterprise Decision Maker"
icp_descriptor: "Senior leader or economic buyer in enterprise, risk-averse"
demographics:
  age_range: [38, 60]
  role_seniority: vp
  company_size: enterprise
  industry: [finance, healthcare, manufacturing, enterprise_tech]
psychographics:
  primary_motivation: "Scale without introducing new risk; protect existing systems"
  primary_fear: "Failed implementation that puts career on the line"
  aspirational_identity: "Executive who makes the smart, safe, ROI-proven call"
  content_consumption: "LinkedIn, Gartner, Harvard Business Review, analyst reports"
platform_behavior:
  primary_platforms: [linkedin, email]
  peak_engagement_hours: ["08:00-09:30", "12:00-13:00"]
  content_format_preference: "Long-form article, ROI report, executive brief"
message_market_fit:
  hook_type: authority
  preferred_tone: authoritative
  cta_style: "High-trust -- 'Request a demo', 'Read the Gartner report'"
  urgency_response: low
funnel_entry:
  typical_stage: BOFU
  avg_sales_cycle_days: 180
  nurture_touches_avg: 30
```

## Segment Selection Logic

```yaml
auto_segment_from_brief:
  if company_size == startup AND role_seniority == c_suite:
    primary_segment: SEG_01
  if company_size in [mid_market] AND role_seniority in [director, vp]:
    primary_segment: SEG_02
  if industry in [creator_economy, education, coaching]:
    primary_segment: SEG_03
  if company_size == enterprise AND role_seniority in [vp, c_suite]:
    primary_segment: SEG_04
  default:
    action: request explicit ICP from brief; GDP if insufficient
```

## Integration

- Read by: `action_prompt_n02_copy.md` (ICP injection)
- Read by: `workflow_campaign_pipeline.md` (F2 STRATEGIZE)
- Referenced by: `cohort_analysis_n02.md` (segment performance tracking)
- Updated by: `self_improvement_loop_n02.md` (segment performance learnings)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_schema_brand_config]] | downstream | 0.34 |
| [[bld_schema_model_registry]] | downstream | 0.32 |
| [[bld_schema_tagline]] | downstream | 0.30 |
| [[bld_schema_training_method]] | downstream | 0.28 |
| [[bld_schema_customer_segment]] | downstream | 0.28 |
| [[bld_schema_experiment_tracker]] | downstream | 0.27 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.25 |
| [[bld_schema_model_architecture]] | downstream | 0.25 |
| [[bld_schema_webinar_script]] | downstream | 0.24 |
| [[n06_kc_icp_frameworks]] | upstream | 0.24 |
