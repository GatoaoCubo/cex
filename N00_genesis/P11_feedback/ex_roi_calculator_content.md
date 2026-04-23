---
id: ex_roi_calculator_content
kind: roi_calculator
pillar: P11
version: 1.0.0
title: "ROI Calculator -- Content Factory / AI Content Platform"
description: "ROI calculator for content-as-a-service customers. Inputs: team size, hourly rate, content volume, current tool spend. Outputs: monthly savings, revenue potential, break-even point."
domain: content_monetization
nucleus: N06
quality: 9.0
tags: [roi-calculator, content-factory, cost-savings, break-even, hours-saved, saas]
brand_placeholders:
  - BRAND_NAME
  - BRAND_CURRENCY
  - BRAND_TEAM_SIZE
  - BRAND_HOURLY_RATE
  - BRAND_SUBSCRIPTION_PRICE_TIER_2
density_score: 1.0
related:
  - n06_roi_content_factory
  - n06_report_intent_resolution_moat
  - n06_content_factory_pricing
  - n06_intent_resolution_depth_spec
  - bld_examples_roi_calculator
  - n06_pricing_content_factory
  - p01_kc_cost_budget
  - bld_examples_lens
  - n06_funnel_content_factory
  - n06_funnel_cex_product
---

# ROI Calculator -- Content Factory / AI Platform

> Primary sales artifact. Customers buy the gap between current spend and platform cost.
> Replace `{{BRAND_*}}` with real values. Example ranges are illustrative.

---

## 1. Calculator Inputs

### 1.1 Customer Profile Variables

| Variable | Description | Example default | Your range |
|----------|-------------|----------------|-----------|
| `hours_per_week` | Hours/week spent creating content | 20 | 5-60 |
| `hourly_rate` | Team hourly cost (salary + overhead) | {{BRAND_CURRENCY}} 75 | 25-300 |
| `content_pieces_per_month` | Content units produced monthly | 12 | 4-100 |
| `team_size` | People involved in content | {{BRAND_TEAM_SIZE}} | 1-20 |
| `tool_subscriptions` | Monthly spend on content tools | {{BRAND_CURRENCY}} 500 | 0-5,000 |
| `agency_spend` | Monthly agency/freelancer fees | {{BRAND_CURRENCY}} 3,000 | 0-50,000 |
| `cex_tier` | Platform subscription tier | Pro | Free/Creator/Pro/Enterprise |

### 1.2 Content Mix Variables

| Variable | Default % | Description |
|----------|----------|-------------|
| `pct_text` | 40% | Blog posts, emails, scripts |
| `pct_visual` | 30% | Social sets, presentations |
| `pct_audio` | 15% | Podcasts, narrations |
| `pct_video` | 15% | Produced videos |

---

## 2. Calculator Formulas

### 2.1 Monthly Savings Formula

```python
# Current cost (before platform)
manual_content_cost = hours_per_week * 4.33 * hourly_rate
total_current_cost = manual_content_cost + tool_subscriptions + agency_spend

# Platform cost
platform_cost = monthly_subscription_price  # from chosen tier

# Monthly savings
monthly_savings = total_current_cost - platform_cost

# Break-even
break_even_days = (platform_cost / (total_current_cost / 30))
```

### 2.2 Hours Saved Formula

```python
# Time per format (manual vs AI-assisted) -- example benchmarks
time_map_manual = {
    "blog_post": 4.0,        # hours
    "social_set": 2.5,
    "video_script": 1.5,
    "video_produced": 8.0,
    "podcast_episode": 3.0,
    "email_sequence": 2.0,
    "landing_page": 6.0
}

time_map_with_platform = {
    "blog_post": 0.5,        # review + approve
    "social_set": 0.3,
    "video_script": 0.3,
    "video_produced": 1.0,   # review + minor edits
    "podcast_episode": 0.5,
    "email_sequence": 0.3,
    "landing_page": 0.5
}

hours_saved_per_piece = time_map_manual[format] - time_map_with_platform[format]
monthly_hours_saved = sum(hours_saved_per_piece * count_per_format)
hours_saved_value = monthly_hours_saved * hourly_rate
```

### 2.3 ROI Formula

```python
roi_pct = ((monthly_savings + hours_saved_value) / platform_cost) * 100
payback_months = platform_cost / monthly_savings
```

---

## 3. ICP Scenario Examples (Illustrative)

> The following are EXAMPLE calculations only. Replace with your validated data.

### Scenario A: Solo Creator

| Input | Value |
|-------|-------|
| hours_per_week | 10 |
| hourly_rate | {{BRAND_CURRENCY}} 50 |
| content_pieces_per_month | 8 |
| tool_subscriptions | {{BRAND_CURRENCY}} 200 |
| Chosen tier | Creator |

| Output | Example value |
|--------|--------------|
| Current cost/month | {{BRAND_CURRENCY}} 2,165 + 200 = 2,365 |
| Platform cost | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_2}} (Creator example) |
| Monthly savings | {{BRAND_CURRENCY}} ~2,200+ |
| Break-even | Day 1-3 |
| Annual saving | {{BRAND_CURRENCY}} ~26,000 |

### Scenario B: Small Marketing Team

| Input | Value |
|-------|-------|
| team_size | {{BRAND_TEAM_SIZE}} |
| hours_per_week | 30 |
| hourly_rate | {{BRAND_CURRENCY}} {{BRAND_HOURLY_RATE}} |
| agency_spend | {{BRAND_CURRENCY}} 5,000 |
| Chosen tier | Pro |

| Output | Example value |
|--------|--------------|
| Current cost/month | {{BRAND_CURRENCY}} 12,000+ |
| Monthly savings | {{BRAND_CURRENCY}} 8,000-11,000 |
| Break-even | Day 2-4 |
| Annual saving | {{BRAND_CURRENCY}} 96,000-132,000 |

---

## 4. Value Comparison Table

| Deliverable | Manual cost (freelancer market) | Platform cost | Cost reduction |
|-------------|--------------------------------|---------------|----------------|
| Blog post | {{BRAND_CURRENCY}} 150-600 | <1 credit | ~99% |
| Social media set | {{BRAND_CURRENCY}} 300-1,200 | ~12 credits | ~95% |
| Video produced 90s | {{BRAND_CURRENCY}} 800-3,000 | ~25 credits | ~90% |
| Full campaign package | {{BRAND_CURRENCY}} 5,000-20,000 | ~100 credits | ~90% |

> Freelancer market prices are example benchmarks for Brazilian market (2026).
> Adjust for your market.

---

## 5. Sales Usage

This calculator is used at:
- B2B sales calls: run live with prospect data
- Website pricing page: interactive widget (planned)
- Email sequences: personalized ROI in outreach
- Onboarding: show new customer their projected savings

---

## New Brand Variables

- `BRAND_TEAM_SIZE` -- default team size for calculator pre-fill (e.g. 2)
- `BRAND_HOURLY_RATE` -- default hourly rate for calculator pre-fill
- `BRAND_CURRENCY` -- currency code

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_roi_content_factory]] | related | 0.50 |
| [[n06_report_intent_resolution_moat]] | related | 0.26 |
| [[n06_content_factory_pricing]] | related | 0.23 |
| [[n06_intent_resolution_depth_spec]] | related | 0.21 |
| [[bld_examples_roi_calculator]] | upstream | 0.21 |
| [[n06_pricing_content_factory]] | related | 0.20 |
| [[p01_kc_cost_budget]] | upstream | 0.19 |
| [[bld_examples_lens]] | upstream | 0.17 |
| [[n06_funnel_content_factory]] | related | 0.17 |
| [[n06_funnel_cex_product]] | related | 0.17 |
