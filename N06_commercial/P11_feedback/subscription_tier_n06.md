---
id: subscription_tier_n06
kind: subscription_tier
pillar: P11
nucleus: n06
title: "Subscription Tier Architecture -- Revenue Model and Upgrade Logic"
version: 1.0.0
quality: null
tags: [subscription, tier, pricing, revenue, saas, upgrade, expansion]
---

# Subscription Tier Architecture

## Revenue Model Philosophy

Strategic Greed principle: every tier must earn its keep AND create conditions for the next upgrade. Tiers are not just price buckets -- they are upgrade funnels. FREE creates desire, STARTER creates dependency, PRO creates team adoption, ENTERPRISE creates contracts.

## Tier Revenue Architecture

| Tier | Monthly Price | Annual Price | Target MRR/Customer | LTV Target |
|------|:---:|:---:|:---:|:---:|
| FREE | $0 | $0 | $0 | $0 (convert target) |
| STARTER | $49 | $470 | $49 (monthly) / $39 (annual) | $500-$1,200 |
| PRO | $149 | $1,430 | $149 (monthly) / $119 (annual) | $2,500-$6,000 |
| ENTERPRISE | $500+ | custom | $500-$5,000 | $15,000-$100,000+ |

## Feature Matrix

| Feature | FREE | STARTER | PRO | ENTERPRISE |
|---------|:----:|:-------:|:---:|:----------:|
| AI builds/month | 10 | 100 | Unlimited | Unlimited |
| Nuclei access | N04 only | N01,N02,N04,N06 | All N01-N06 | All N01-N07 |
| Brand config | No | Yes | Yes | Yes |
| API access | No | No | Yes (60 RPM) | Yes (600 RPM) |
| Seats | 1 | 1 | 5 | Unlimited |
| Priority support | No | No | Yes | Yes + CSM |
| SSO | No | No | No | Yes |
| Audit log | No | No | Yes | Yes |
| Custom integrations | No | No | No | Yes |
| SLA uptime | No | No | No | 99.9% |
| Data residency | No | No | No | Yes |

## Upgrade Triggers (Automated)

```yaml
upgrade_triggers:
  free_to_starter:
    - event: builds_quota_exhausted
      action: show_upgrade_modal
    - event: brand_config_attempted
      action: gate_with_upgrade_prompt
    - event: login_streak_7_days
      action: send_upgrade_email
    
  starter_to_pro:
    - event: api_access_requested
      action: show_upgrade_modal
    - event: builds_quota_exhausted
      action: show_upgrade_modal
    - event: second_seat_invited
      action: show_upgrade_modal
    - event: n03_feature_requested
      action: gate_with_upgrade_prompt
    
  pro_to_enterprise:
    - event: seats_at_capacity_5
      action: trigger_sales_touchpoint
    - event: sso_requested
      action: trigger_sales_touchpoint
    - event: compliance_document_requested
      action: trigger_sales_touchpoint
    - event: api_rate_limit_hit_3x
      action: trigger_expansion_play
```

## Revenue Metrics per Tier

### Conversion Rates (Benchmarks)

| Conversion | Industry Avg | N06 Target |
|-----------|:---:|:---:|
| FREE -> STARTER | 2-5% | 8% |
| STARTER -> PRO | 15-25% | 30% |
| PRO -> ENTERPRISE | 5-10% | 15% |
| Monthly -> Annual | 20-40% | 45% |

### Payback Period

| Tier | CAC Target | Payback Period |
|------|:---:|:---:|
| STARTER | <$50 | <2 months |
| PRO | <$300 | <3 months |
| ENTERPRISE | <$3,000 | <9 months |

## Annual vs Monthly Pricing Strategy

Annual discount: 20% (presented as "2 months free").

Annual customer benefits:
- Predictable revenue: reduces churn 35-60% vs monthly
- Cash flow: upfront collection improves runway
- Commitment signal: annual customers 3x less likely to churn

Levers to push annual:
1. Annual discount on checkout default selection
2. "Most popular" badge on annual
3. Annual-only features (data residency for ENTERPRISE)
4. Annual invoicing for Enterprise (vs credit card)

## Cannibalization Guard

```
PRO ($149) must NOT compete with ENTERPRISE floor ($500):
  - PRO caps seats at 5 (Enterprise = unlimited)
  - PRO lacks SSO (Enterprise blocker)
  - PRO lacks SLA (Enterprise requirement)

STARTER ($49) must NOT feel "good enough" for power users:
  - No API access (developer workflow blocker)
  - N03 locked (no artifact construction)
  - 1 seat (no team use)
```

## Related Artifacts

- `enum_def_pricing_tiers.md` -- canonical tier definitions and feature flags
- `expansion_play_n06.md` -- automated upgrade trigger mechanics
- `churn_prevention_playbook_n06.md` -- retention by tier
- `roi_calculator_n06.md` -- value proof per tier for sales
