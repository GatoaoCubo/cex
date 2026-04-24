---
id: con_rate_limit_config_n06
kind: rate_limit_config
8f: F1_constrain
pillar: P09
nucleus: n06
title: Commercial Rate Limits
version: 1.0
quality: 9.0
tags: [config, rate-limit, budget, pricing, ops]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_collaboration_cost_budget
  - p01_kc_rate_limit_config
  - cost-budget-builder
  - bld_instruction_rate_limit_config
  - bld_knowledge_card_model_provider
  - p01_kc_cost_budget
  - bld_knowledge_card_rate_limit_config
  - p11_qg_rate_limit_config
  - bld_architecture_cost_budget
  - p03_sp_rate_limit_config_builder
---

<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate-limit-config-builder F3 inject=nucleus_def_n06.md,n06-commercial.md,bld_manifest_rate_limit_config.md,kc_rate_limit_config.md,P09_config/_schema.yaml F4 reason=rate_budget_policy_that_favors_high_value_revenue_actions F5 call=apply_patch;python _tools/cex_compile.py F6 produce=4864_bytes F7 govern=frontmatter_sections_ascii_density_review F8 collaborate=N06_commercial/P09_config/con_rate_limit_config_n06.md -->

# Commercial Rate Limits

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define RPM, TPM, concurrency, and spend limits for N06 commercial execution |
| Business Lens | Strategic Greed spends aggressively where revenue is near, and throttles hard where curiosity burns budget without cash return |
| Primary Use | govern research, pricing generation, renewal defense, and premium proposal flows |
| Failure Prevented | runaway token spend, provider throttling, and low-value work starving high-value customer actions |
| Provider Stance | provider-neutral policy with premium-path prioritization |
| Budget Rule | money follows monetization probability |

## Values

| Profile | RPM | TPM | Concurrency | Daily Budget USD | Priority Use |
|---------|-----|-----|-------------|------------------|--------------|
| premium_close | 40 | 240000 | 6 | 45 | active checkout, enterprise proposal, renewal rescue |
| expansion_push | 30 | 180000 | 5 | 30 | upsell targeting and annual conversion |
| pricing_ops | 20 | 120000 | 4 | 18 | pricing pages, offer refresh, margin analysis |
| experiment_loop | 12 | 80000 | 3 | 10 | controlled A/B offer testing |
| low_value_research | 6 | 40000 | 2 | 4 | broad exploratory work with weak monetization signal |

## Model Overrides

| Model Class | RPM Cap | TPM Cap | Reason |
|-------------|---------|---------|--------|
| premium_reasoning | 15 | 120000 | reserved for high-value commercial decisions |
| standard_generation | 30 | 180000 | default offer and documentation work |
| low_cost_batch | 50 | 100000 | cheap bulk transformations under budget guard |

## Backoff Policy

| Field | Value | Why |
|-------|-------|-----|
| strategy | exponential_jitter | avoids burst retries during provider pressure |
| first_delay_ms | 1500 | fast enough for customer-facing rescue flows |
| max_delay_ms | 45000 | caps frustration while preserving spend |
| retry_limit | 5 | enough recovery attempts without budget bleed |
| degrade_to | lower_cost_profile | protect premium actions when budget tightens |

## Conservation Rules

| Trigger | Action | Commercial Reason |
|---------|--------|-------------------|
| daily spend >= 80 percent | cut experiment_loop by 50 percent | preserve budget for near-cash work |
| daily spend >= 90 percent | disable low_value_research | low-intent work should be first sacrificed |
| provider 429 on premium_close | backoff, keep queue priority | do not demote near-revenue tasks |
| provider 429 on research | defer to off-peak | cheap patience beats costly contention |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| Distinct premium_close profile | checkout and enterprise saves are highest value | directs capacity to imminent revenue |
| Research kept intentionally thin | curiosity often burns spend without return | protects unit economics |
| Daily budget per profile | one runaway loop should not steal the whole day | preserves optionality for later high-yield work |
| Degrade by profile, not total shutdown | some work should continue under pressure | sustains revenue defense even in constraint |
| Model overrides | expensive reasoning should be scarce | keeps premium cognition for premium moments |

## Example

| Scenario | Result |
|----------|--------|
| Daily spend hits 82 percent before evening renewal run | experiments slow down, rescue workflows keep priority |

```yaml
provider: commercial_default
profiles:
  premium_close:
    rpm: 40
    tpm: 240000
    concurrency: 6
    daily_budget_usd: 45
  low_value_research:
    rpm: 6
    tpm: 40000
    concurrency: 2
    daily_budget_usd: 4
backoff:
  strategy: exponential_jitter
  retry_limit: 5
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Profile Count | 5 |
| Override Count | 3 |
| Backoff Strategy | exponential_jitter |
| Budget Bias | premium-first |
| Cost Guard | conservation triggers at 80 and 90 percent |
| Throughput Guard | concurrency bounded per profile |
| Failure Mode | degrade low-value work first |
| Commercial Bias | spend where cash is closest |
| Related Pillars | P09, P06, P11 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_cost_budget]] | downstream | 0.35 |
| [[p01_kc_rate_limit_config]] | related | 0.32 |
| [[cost-budget-builder]] | related | 0.30 |
| [[bld_instruction_rate_limit_config]] | upstream | 0.26 |
| [[bld_knowledge_card_model_provider]] | upstream | 0.25 |
| [[p01_kc_cost_budget]] | related | 0.25 |
| [[bld_knowledge_card_rate_limit_config]] | upstream | 0.25 |
| [[p11_qg_rate_limit_config]] | downstream | 0.24 |
| [[bld_architecture_cost_budget]] | upstream | 0.23 |
| [[p03_sp_rate_limit_config_builder]] | related | 0.23 |
