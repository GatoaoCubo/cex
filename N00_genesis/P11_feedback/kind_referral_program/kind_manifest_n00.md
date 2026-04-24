---
id: n00_referral_program_manifest
kind: knowledge_card
8f: F3_inject
pillar: P11
nucleus: n00
title: "Referral Program -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, referral_program, p11, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_referral_program
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_roi_calculator
  - bld_schema_sandbox_spec
  - bld_schema_optimizer
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_nps_survey
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A referral_program designs a viral growth mechanism with defined incentive structures, viral coefficient targets, and reward distribution rules. It constrains how CEX-powered products leverage existing customers to acquire new ones, specifying the referral loop mechanics that make word-of-mouth growth computable and optimizable.

## Pillar
P11 -- feedback

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `referral_program` |
| pillar | string | yes | Always `P11` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| referrer_reward | object | yes | Reward for the referrer (cash, credit, feature access) |
| referee_reward | object | yes | Reward for the referred user |
| viral_coefficient_target | float | yes | Target K-factor (>1.0 = viral growth) |
| eligibility_criteria | array | yes | Conditions a user must meet to participate |
| reward_trigger | enum | yes | on_signup \| on_first_payment \| on_30d_retention |
| max_referrals_per_user | integer | no | Cap on referrals per user per period |
| expiry_days | integer | no | Days after which referral links expire |

## When to use
- When designing viral growth mechanics for a CEX-powered product launch
- When configuring referral rewards for a subscription tier upgrade campaign
- When modeling K-factor to project growth curve from word-of-mouth

## Builder
`archetypes/builders/referral_program-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind referral_program --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rp_cex_saas_referral_v1
kind: referral_program
pillar: P11
nucleus: n06
title: "Example Referral Program"
version: 1.0
quality: null
---
# Referral Program: CEX SaaS
referrer_reward: {type: credit, value: 30, currency: USD}
referee_reward: {type: discount, value: 20, unit: percent, duration: 3_months}
viral_coefficient_target: 1.2
reward_trigger: on_first_payment
```

## Related kinds
- `content_monetization` (P11) -- monetization pipeline this referral program amplifies
- `subscription_tier` (P11) -- tier that referral rewards grant access to
- `roi_calculator` (P11) -- ROI model incorporating referral LTV calculations

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_referral_program]] | upstream | 0.56 |
| [[bld_schema_reranker_config]] | upstream | 0.42 |
| [[bld_schema_usage_report]] | upstream | 0.41 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_roi_calculator]] | upstream | 0.40 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
| [[bld_schema_optimizer]] | upstream | 0.39 |
| [[bld_schema_dataset_card]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.39 |
| [[bld_schema_nps_survey]] | upstream | 0.39 |
