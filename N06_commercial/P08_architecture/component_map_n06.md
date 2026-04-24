---
id: component_map_n06
kind: component_map
8f: F4_reason
pillar: P08
nucleus: n06
title: "N06 Commercial -- Component Map"
version: 1.0.0
created: 2026-04-18
author: n07_admin
domain: commercial-revenue-architecture
quality: 8.7
tags: [component_map, n06, commercial, revenue, pricing, architecture]
tldr: "Internal component map of N06 Commercial nucleus: pricing engine, brand pipeline, funnel architecture, content monetization, and inter-nucleus revenue data flows."
density_score: null
related:
  - agent_card_n06
  - p02_agent_commercial_nucleus
  - spec_n06_brand_verticalization
  - p02_mm_commercial_nucleus
  - p08_ac_brand_nucleus
  - p02_agent_brand_nucleus
  - p03_sp_brand_nucleus
  - p12_wf_commercial
  - n06_self_audit_20260408
  - p12_dr_commercial
---

# N06 Commercial -- Component Map

## System Overview

N06 is the revenue, brand, and commercial strategy nucleus. Its primary function
is maximizing revenue opportunity at every touchpoint: pricing, monetization,
customer segmentation, funnels, and brand consistency.
All output flows through 8F: CONSTRAIN kind/pillar -> BECOME revenue optimizer
-> INJECT market KCs + brand config -> REASON on monetization vectors
-> CALL pricing tools -> PRODUCE pricing_page/content_monetization
-> GOVERN for revenue correctness -> COLLABORATE.

**Sin Lens**: Strategic Greed -- extracts every revenue opportunity the product
allows. Never leaves money on the table; always asks "what else can we charge for?"

---

## Artifact Inventory

| Pillar | Count | Primary Kinds |
|--------|------:|---------------|
| P01 Knowledge | 23 | knowledge_card, competitive_matrix, customer_segment |
| P02 Model | 5 | agent, boot_config, nucleus_def |
| P03 Prompt | 11 | system_prompt, prompt_template, action_prompt, sales_playbook |
| P04 Tools | 5 | api_client, webhook, social_publisher |
| P05 Output | 34 | landing_page, pricing_page, pitch_deck, case_study |
| P06 Schema | 12 | input_schema, validation_schema, data_contract |
| P07 Evals | 16 | quality_gate, scoring_rubric, cohort_analysis |
| P08 Architecture | 7 | component_map, decision_record, pattern |
| P09 Config | 6 | env_config, rate_limit_config, feature_flag |
| P10 Memory | 10 | entity_memory, user_model, knowledge_index |
| P11 Feedback | 12 | content_monetization, subscription_tier, renewal_workflow |
| P12 Orchestration | 9 | workflow, schedule, expansion_play, churn_prevention_playbook |

**Total: 153 artifacts**

---

## Internal Components

### C1 -- Pricing Engine
```
Customer segment analysis
  |
  v
[C1.1] Competitive matrix   -- knowledge_card: competitor pricing
  |
  v
[C1.2] Subscription tiers   -- subscription_tier: Free/Pro/Enterprise
  |
  v
[C1.3] Content monetization -- content_monetization: feature gating
  |
  v
[C1.4] Pricing page         -- pricing_page: HTML + copy
  |
  v
ROI calculator              -- roi_calculator: conversion proof
```

### C2 -- Brand Pipeline
```
.cex/brand/brand_config.yaml
  |
  v
brand_inject.py             -- {{BRAND_*}} placeholder resolution
  |
  v
brand_propagate.py          -- push brand context to all nuclei
  |
  v
brand_audit.py              -- 6-dimension consistency score
  |
  v
brand_validate.py           -- 13 required fields check
```

### C3 -- Funnel Architecture
```
pattern_funnel_architecture.md (N06/P08)
  |
  +-- Acquisition: landing_page + press_release
  +-- Activation: onboarding_flow + product_tour
  +-- Retention: renewal_workflow + curation_nudge
  +-- Revenue: pricing_page + subscription_tier
  +-- Referral: referral_program + partner_listing
```

### C4 -- Revenue Intelligence
```
N01 competitive research -> N06 market analysis
  |
  v
customer_segment (P01)
  |
  v
cohort_analysis (P07)
  |
  v
expansion_play + churn_prevention_playbook (P12)
  |
  v
Revenue projection artifacts
```

---

## Data Flows

| Source | -> | N06 | -> | Destination |
|--------|----|----|-----|-------------|
| N01 market research | -> | competitive_matrix | -> | N06/P01 |
| N02 brand assets | -> | brand injection | -> | N06 output templates |
| N07 handoff | -> | commercial task | -> | N06 8F run |
| N06 pricing_page | -> | compile | -> | CLAUDE.md / cursorrules |
| N06 signal | -> | F8 COLLABORATE | -> | N07 consolidation |

---

## Key Tools

| Tool | Function |
|------|----------|
| `brand_inject.py` | Template placeholder resolution |
| `brand_propagate.py` | Brand config push to all nuclei |
| `brand_audit.py` | Brand consistency scoring (6D) |
| `brand_ingest.py` | Extract brand signals from raw files |
| `cex_compile.py --target customgpt` | CEX -> CustomGPT commercial deploy |
| `cex_crew.py run product_launch` | Multi-role launch crew |

---

## Gaps (from SELF_AUDIT)

| Gap | Severity | Status |
|-----|----------|--------|
| component_map missing until this file | MEDIUM | RESOLVED |
| No canary_config builder | MEDIUM | Builder exists now |
| No deployment_manifest builder | MEDIUM | Registered |
| ROI calculator not wired to brand_config | LOW | Manual only |
| expansion_play builder | MEDIUM | Registered |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n06]] | upstream | 0.56 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.51 |
| [[spec_n06_brand_verticalization]] | upstream | 0.51 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.50 |
| [[p08_ac_brand_nucleus]] | related | 0.45 |
| [[p02_agent_brand_nucleus]] | upstream | 0.43 |
| [[p03_sp_brand_nucleus]] | upstream | 0.40 |
| [[p12_wf_commercial]] | downstream | 0.40 |
| [[n06_self_audit_20260408]] | upstream | 0.39 |
| [[p12_dr_commercial]] | downstream | 0.39 |
