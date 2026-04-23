---
id: enum_def_pricing_tiers
kind: enum_def
pillar: P06
nucleus: n06
title: "Enum Definition -- Pricing Tier Taxonomy"
version: 1.0.0
quality: 9.0
tags: [pricing, tiers, enum, commercial, saas, packaging]
density_score: 1.0
related:
  - n06_intent_resolution_depth_spec
  - commercial_readiness_20260413
  - kc_subscription_tier
  - commercial_readiness_20260414
  - p08_pat_pricing_framework
  - bld_examples_pricing_page
  - pricing_optimization_memory
  - bld_instruction_subscription_tier
  - p06_schema_env_contract
  - instance_supabase_config_template
---

# Enum Definition: Pricing Tier Taxonomy

## Purpose

Canonical enumeration of all pricing tiers, their feature gates, limits, and Stripe Price ID mapping. Every part of the commercial system references this enum -- pricing pages, checkout flow, entity_memory, churn logic, expansion plays.

## Tier Enum

```typescript
enum PlanTier {
  FREE       = "free",
  STARTER    = "starter",
  PRO        = "pro",
  ENTERPRISE = "enterprise",
  CUSTOM     = "custom"
}
```

## Tier Definitions

### FREE

```yaml
tier: free
stripe_price_id: null
monthly_usd: 0
annual_usd: 0
seats: 1
feature_flags:
  ai_builds_per_month: 10
  nuclei_access: [n04]
  brand_config: false
  api_access: false
  priority_support: false
  sso: false
  audit_log: false
  custom_integrations: false
upgrade_path: starter
conversion_trigger: "builds exhausted OR brand_config requested"
churn_risk: N/A
```

### STARTER

```yaml
tier: starter
stripe_price_id_monthly: price_starter_monthly
stripe_price_id_annual: price_starter_annual
monthly_usd: 49
annual_usd: 470          # ~20% discount = 2 months free
annual_discount_pct: 20
seats: 1
feature_flags:
  ai_builds_per_month: 100
  nuclei_access: [n01, n02, n04, n06]
  brand_config: true
  api_access: false
  priority_support: false
  sso: false
  audit_log: false
  custom_integrations: false
upgrade_trigger: "100 builds exhausted OR api_access needed OR seats > 1"
churn_risk_signals: ["<5 builds/month used", "no brand_config set", "login <2x/month"]
```

### PRO

```yaml
tier: pro
stripe_price_id_monthly: price_pro_monthly
stripe_price_id_annual: price_pro_annual
monthly_usd: 149
annual_usd: 1430         # ~20% discount
annual_discount_pct: 20
seats: 5
feature_flags:
  ai_builds_per_month: unlimited
  nuclei_access: [n01, n02, n03, n04, n05, n06]
  brand_config: true
  api_access: true
  api_rate_limit_rpm: 60
  priority_support: true
  sso: false
  audit_log: true
  custom_integrations: false
upgrade_trigger: "seats > 5 OR SSO required OR custom SLA needed"
churn_risk_signals: ["api_calls < 100/month", "only 1 nucleus used"]
expansion_target: enterprise
```

### ENTERPRISE

```yaml
tier: enterprise
stripe_price_id: negotiated
monthly_usd_base: 500          # floor, actual varies
seats: unlimited
feature_flags:
  ai_builds_per_month: unlimited
  nuclei_access: [n01, n02, n03, n04, n05, n06, n07]
  brand_config: true
  api_access: true
  api_rate_limit_rpm: 600
  priority_support: true
  dedicated_success_manager: true
  sso: true
  audit_log: true
  custom_integrations: true
  sla_uptime_pct: 99.9
  data_residency: true
qualification: "requires sales touch, >25 seats OR compliance requirements OR custom SLA"
```

### CUSTOM

```yaml
tier: custom
stripe_price_id: bespoke
description: "White-label, OEM, reseller, or usage-based pricing arrangements"
qualification: "legal review required"
```

## Feature Gate Logic

```python
def is_feature_enabled(customer_tier: str, feature: str) -> bool:
    tier_order = ["free", "starter", "pro", "enterprise", "custom"]
    feature_min_tier = {
        "brand_config": "starter",
        "api_access": "pro",
        "n03_access": "pro",
        "n05_access": "pro",
        "n07_access": "enterprise",
        "sso": "enterprise",
        "audit_log": "pro",
        "dedicated_csm": "enterprise",
        "custom_integrations": "enterprise",
    }
    min_tier = feature_min_tier.get(feature, "free")
    return tier_order.index(customer_tier) >= tier_order.index(min_tier)
```

## Upgrade Path Matrix

```
FREE -> STARTER -> PRO -> ENTERPRISE
          ^                   |
          |                   v
          +--- downgrade ------+
                (retention play)
```

## Pricing Psychology Notes

| Principle | Application |
|-----------|-------------|
| Good/Better/Best | FREE anchors value; PRO is hero; ENTERPRISE is ceiling |
| Annual discount | 20% off = 2 months free framing (psychologically stronger than "20% off") |
| Seat-based expansion | PRO 5 seats triggers natural expansion to Enterprise as team grows |
| Feature gating | Gate API (dev workflow must-have) at PRO to drive conversions |
| Trial-to-paid | FREE has hard limits (10 builds) to create urgency without free-rider problem |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_intent_resolution_depth_spec]] | downstream | 0.35 |
| [[commercial_readiness_20260413]] | downstream | 0.33 |
| [[kc_subscription_tier]] | upstream | 0.31 |
| [[commercial_readiness_20260414]] | downstream | 0.31 |
| [[p08_pat_pricing_framework]] | downstream | 0.27 |
| [[bld_examples_pricing_page]] | downstream | 0.25 |
| [[pricing_optimization_memory]] | downstream | 0.25 |
| [[bld_instruction_subscription_tier]] | upstream | 0.24 |
| [[p06_schema_env_contract]] | related | 0.24 |
| [[instance_supabase_config_template]] | upstream | 0.24 |
