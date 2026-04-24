---
id: con_env_config_n06
kind: env_config
8f: F1_constrain
pillar: P09
nucleus: n06
title: Commercial Env Config
version: 1.0
quality: 9.0
tags: [config, env, pricing, funnel, revenue]
density_score: 1.0
related:
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_reranker_config
  - bld_schema_bugloop
  - bld_schema_quickstart_guide
  - bld_schema_dataset_card
  - bld_schema_env_config
  - bld_schema_pitch_deck
  - bld_examples_kind
  - bld_schema_pricing_page
---

<!-- 8F: F1 constrain=P09/env_config F2 become=env-config-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_env_config.md,kc_env_config.md,P09_config/_schema.yaml F4 reason=env_catalog_for_monetization_controls_and_funnel_defaults F5 call=apply_patch;python _tools/cex_compile.py F6 produce=5508_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/P09_config/con_env_config_n06.md -->

# Commercial Env Config

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define the environment variable contract for N06 pricing, funnel, monetization, and renewal systems |
| Business Lens | Strategic Greed uses env vars to make revenue experiments fast while keeping premium defaults protected |
| Primary Use | Configure pricing engines, checkout routing, offer cadence, budget thresholds, and retention alerts |
| Failure Prevented | hidden defaults, unsafe free-tier leakage, and environment drift across commercial surfaces |
| Scope | local, staging, production |
| Precedence | runtime env -> managed secret injection -> safe default |

## Values

| Variable | Type | Default | Required | Validation | Commercial Intent |
|----------|------|---------|----------|------------|-------------------|
| N06_ENV | string | `local` | yes | `local|staging|prod` | environment-specific greed level |
| N06_DEFAULT_CURRENCY | string | `BRL` | yes | ISO 4217 | normalize monetization reports |
| N06_DEFAULT_REVENUE_STATE | string | `lead_captured` | yes | must match enum | safe first funnel state |
| N06_MIN_CHECKOUT_VALUE | decimal | `49.00` | yes | `>= 0` | blocks low-value custom work |
| N06_ANNUAL_DISCOUNT_CAP_PCT | integer | `20` | yes | `0-40` | prevents margin-eroding discounts |
| N06_FREE_TIER_LIMIT_EVENTS | integer | `100` | yes | `>= 0` | keeps free usage from cannibalizing paid |
| N06_UPSELL_TRIGGER_USAGE_PCT | integer | `80` | yes | `50-100` | prompt expansion before churn |
| N06_RENEWAL_RISK_WINDOW_DAYS | integer | `14` | yes | `1-45` | start save motions before renewal fails |
| N06_DUNNING_MAX_ATTEMPTS | integer | `4` | yes | `1-10` | balance recovery with customer fatigue |
| N06_MARGIN_FLOOR_PCT | integer | `65` | yes | `1-95` | defend profitability |
| N06_PRIORITY_SEGMENTS | string | `scale,enterprise,growth` | yes | comma list | premium demand gets first attention |
| N06_EXPERIMENTS_ENABLED | boolean | `true` | yes | `true|false` | pricing compounding stays on by default |
| N06_PRICE_ANCHOR_MODE | string | `premium_first` | yes | `premium_first|mid_first|off` | anchors buyers toward higher tiers |
| N06_ALERT_WEBHOOK | secret_ref | none | no | secret pointer only | notify revenue-risk systems |
| N06_PAYMENT_PROVIDER | string | `stripe` | yes | `stripe|mercadopago|hybrid` | select monetization rail |

## Profiles

| Environment | Override | Why |
|-------------|----------|-----|
| local | experiments enabled, low alert noise | fast commercial iteration |
| staging | production-like values, sandbox provider | validates pricing logic safely |
| prod | strict floors and premium-first anchor | protect margin and realized cash |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Currency default is explicit | revenue reports fail when currency is implicit | keeps commercial data comparable |
| Margin floor env var | margin policy changes faster than code | allows rapid profit defense |
| Annual discount cap | discounting is the fastest way to destroy value | forces deliberate concessions |
| Priority segment list | not all customers deserve equal latency | shifts attention to highest LTV |
| Upsell trigger threshold | expansion must happen before plateau | captures more ARPU from usage peaks |
| Renewal risk window | retention is cheaper than reacquisition | activates save tactics earlier |

## Example

| Scenario | Result |
|----------|--------|
| Production rollout for a premium-first pricing page | paid tiers stay anchored, free leakage capped, renewal alerts enabled |

```env
N06_ENV=prod
N06_DEFAULT_CURRENCY=BRL
N06_DEFAULT_REVENUE_STATE=lead_captured
N06_MIN_CHECKOUT_VALUE=49.00
N06_ANNUAL_DISCOUNT_CAP_PCT=20
N06_FREE_TIER_LIMIT_EVENTS=100
N06_UPSELL_TRIGGER_USAGE_PCT=80
N06_RENEWAL_RISK_WINDOW_DAYS=14
N06_DUNNING_MAX_ATTEMPTS=4
N06_MARGIN_FLOOR_PCT=65
N06_PRIORITY_SEGMENTS=scale,enterprise,growth
N06_EXPERIMENTS_ENABLED=true
N06_PRICE_ANCHOR_MODE=premium_first
N06_PAYMENT_PROVIDER=stripe
```

## Notes

| Topic | Rule |
|-------|------|
| Secrets | values such as webhooks and provider keys must come from `con_secret_config_n06` references, never inline |
| Validation | enum-backed values must match N06 schemas |
| Logging | sensitive values masked, commercial thresholds visible |
| Drift | staging should mirror prod except for payment settlement and alert routing |

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Scope | runtime |
| Variable Count | 15 |
| Secret Strategy | reference only |
| Default Bias | premium-first monetization |
| Risk Guard | margin floor plus discount cap |
| Growth Lever | upsell trigger and experiments toggle |
| Retention Lever | renewal window and dunning count |
| Compatibility | additive vars only |
| Related Pillars | P06, P09, P11 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_sandbox_config]] | upstream | 0.43 |
| [[bld_schema_reranker_config]] | upstream | 0.43 |
| [[bld_schema_bugloop]] | downstream | 0.43 |
| [[bld_schema_quickstart_guide]] | upstream | 0.42 |
| [[bld_schema_dataset_card]] | upstream | 0.42 |
| [[bld_schema_env_config]] | upstream | 0.41 |
| [[bld_schema_pitch_deck]] | upstream | 0.41 |
| [[bld_examples_kind]] | upstream | 0.41 |
| [[bld_schema_pricing_page]] | upstream | 0.41 |
