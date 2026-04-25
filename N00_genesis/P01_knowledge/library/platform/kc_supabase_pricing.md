---
id: p01_kc_supabase_pricing
kind: knowledge_card
8f: F3_inject
type: platform
pillar: P01
title: "Supabase Pricing — Tiers, Limits, Cost Optimization"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n04_knowledge
domain: data_platform
quality: 9.1
tags: [supabase, pricing, tiers, free, pro, team, enterprise, cost, platform]
tldr: "4 tiers: Free (USD 0, 500MB DB, 2 projects), Pro (USD 25/mo, 8GB DB), Team (USD 599/mo, SOC2+SSO), Enterprise (custom). Overage billing on Pro+."
when_to_use: "When deciding Supabase tier or optimizing costs of existing project"
keywords: [supabase-pricing, free-tier, pro-tier, cost-optimization]
long_tails:
  - How much does Supabase Pro cost per month with overages
  - Supabase free tier limits in 2025
  - How to optimize costs on Supabase Pro tier
axioms:
  - ALWAYS start on Free tier to validate — upgrade when necessary
  - NEVER ignore overage pricing — DB storage can scale fast
  - ALWAYS monitor the usage dashboard to avoid billing surprises
linked_artifacts:
  primary: null
  related: [p01_kc_supabase_database, p01_kc_supabase_storage]
density_score: 0.93
data_source: "https://supabase.com/pricing"
related:
  - p04_ex_content_monetization_saas
  - bld_config_supabase_data_layer
  - commercial_readiness_20260413
  - n06_intent_resolution_depth_spec
  - p01_kc_supabase_database
  - bld_schema_supabase_data_layer
  - bld_knowledge_card_supabase_data_layer
  - bld_output_template_pricing_page
  - commercial_readiness_20260414
  - p01_kc_cost_budget
---

# Supabase Pricing

## Quick Reference
```yaml
topic: supabase_pricing
scope: Free, Pro, Team, Enterprise tiers + overage costs
owner: n04_knowledge
criticality: high
url: https://supabase.com/pricing
```

## Tier Comparison
| Resource | Free (USD 0) | Pro (USD 25/mo) | Team (USD 599/mo) | Enterprise |
|----------|-------------|-----------------|---------------------|------------|
| Projects | 2 active | Unlimited | Unlimited | Unlimited |
| Database | 500 MB | 8 GB | 8 GB | Custom |
| Bandwidth | 5 GB | 250 GB | 250 GB | Custom |
| Storage | 1 GB | 100 GB | 100 GB | Custom |
| Edge Functions | 500K/mo | 2M/mo | 2M/mo | Custom |
| Auth MAU | 50.000 | 100.000 | 100.000 | Custom |
| Realtime msgs | 2M/mo | 5M/mo | Unlimited | Custom |
| Concurrent RT | 200 | 500 | 1000+ | Custom |
| Daily backups | No | 7 days | 14 days | Custom |
| PITR | No | Addon | Addon | Included |
| SOC2 | No | No | Yes | Yes |
| SSO SAML | No | Addon | Included | Included |
| Support | Community | Email | Priority | Dedicated |

## Overage Pricing (Pro+)
| Resource | Included (Pro) | Overage |
|---------|---------------|---------|
| Database | 8 GB | USD 0.125/GB |
| Bandwidth | 250 GB | USD 0.09/GB |
| Storage | 100 GB | USD 0.021/GB |
| Auth MAU | 100K | USD 0.00325/MAU |
| Edge invocations | 2M | USD 0.002/1K |
| Realtime msgs | 5M | USD 0.0025/1K |

## Addons (Pro+)
| Addon | Price | What It Does |
|-------|-------|--------------|
| PITR | USD 100/mo | Point-in-time recovery |
| Custom domain | USD 10/mo | Your domain on API URL |
| Compute (Small) | Included Pro | 2 CPU, 1 GB RAM |
| Compute (Medium) | USD 100/mo | 2 CPU, 2 GB RAM |
| Compute (Large) | USD 200/mo | 2 CPU, 4 GB RAM |
| Compute (XL) | USD 400/mo | 4 CPU, 8 GB RAM |
| Compute (2XL) | USD 950/mo | 8 CPU, 16 GB RAM |
| IPv4 | USD 4/mo | Dedicated IPv4 address |

## Decision Tree
```text
New project / MVP / testing?
  → FREE (validate, iterate, no cost)

Production with <100K MAU, <8GB DB?
  → PRO (USD 25/mo, sufficient for most)

Production with SOC2, SSO, priority support?
  → TEAM (USD 599/mo, compliance ready)

>100K MAU, SLA 99.99%, dedicated support?
  → ENTERPRISE (negotiate custom)
```

## Cost Optimization Tips
| Tip | Estimated Savings |
|-----|-------------------|
| `pg_stat_statements` → optimize slow queries | 20-40% CPU/RAM |
| Index on filter/RLS columns | 50-90% query time |
| Storage: serve webp via transforms | 40-60% bandwidth |
| CDN (Pro) for static assets | 50-70% bandwidth |
| Connection pooler (Supavisor) | Less compute addon |
| Edge Functions: cache results | 30-50% invocations |
| Realtime: filter by table/event | Fewer messages |
| Cleanup: pg_cron to delete expired data | DB storage |

## Costs per Vertical
| Vertical | Tier | Cost/month |
|----------|------|-----------| 
| MVP / Side project | Free | USD 0 |
| Small e-commerce | Pro | USD 25-35 |
| SaaS B2B (500 users) | Pro | USD 30-60 |
| Marketplace (10K listings) | Pro+Compute | USD 130-200 |
| Content platform (50K posts) | Team | USD 620-700 |

## Anti-Patterns
| Anti-Pattern | Extra Cost | Fix |
|-------------|------------|-----|
| No spend cap on Pro | Unexpected overage | Enable spend cap |
| Data never deleted | DB grows infinitely | pg_cron cleanup |
| Original images served | Bandwidth 5-10x | Transforms + CDN |
| Inactive Free project | Paused after 7 days | Move to Pro or delete |

## Golden Rules
- START Free, upgrade to Pro when you validate product-market fit
- ENABLE spend cap on Pro to avoid surprises
- MONITOR Dashboard > Usage weekly
- DESIGN for the tier — do not assume Enterprise features on Free

## References
- Pricing: https://supabase.com/pricing
- Spend cap: https://supabase.com/docs/guides/platform/spend-cap
- Compute addons: https://supabase.com/docs/guides/platform/compute-add-ons

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_ex_content_monetization_saas]] | downstream | 0.31 |
| [[bld_config_supabase_data_layer]] | downstream | 0.28 |
| [[commercial_readiness_20260413]] | downstream | 0.26 |
| [[n06_intent_resolution_depth_spec]] | downstream | 0.26 |
| [[p01_kc_supabase_database]] | sibling | 0.24 |
| [[bld_schema_supabase_data_layer]] | downstream | 0.24 |
| [[bld_knowledge_card_supabase_data_layer]] | sibling | 0.24 |
| [[bld_output_template_pricing_page]] | downstream | 0.21 |
| [[commercial_readiness_20260414]] | downstream | 0.21 |
| [[p01_kc_cost_budget]] | sibling | 0.20 |
