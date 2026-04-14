---
kind: schema
id: bld_schema_ab_test_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for ab_test_config
quality: null
title: "Schema Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for ab_test_config"
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                              |  
|------------|--------|----------|---------|------------------------------------|  
| id         | string | yes      | null    | Must match ID pattern              |  
| kind       | string | yes      | null    | Always "ab_test_config"            |  
| pillar     | string | yes      | null    | Always "P11"                       |  
| title      | string | yes      | null    | Concise experiment name            |  
| version    | int    | yes      | null    | Incremental version number         |  
| created    | date   | yes      | null    | ISO 8601 format                    |  
| updated    | date   | yes      | null    | ISO 8601 format                    |  
| author     | string | yes      | null    | Owner email                        |  
| domain     | string | yes      | null    | "ab_test"                          |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | list   | yes      | []      | Keywords for search                |  
| tldr       | string | yes      | null    | Summary of experiment purpose      |  
| experiment_name | string | yes | null | Human-readable test name         |  
| variant_groups | list | yes | [] | List of variant group definitions  |  

### Recommended  
| Field         | Type   | Notes                          |  
|---------------|--------|--------------------------------|  
| description   | string | Detailed experiment objective  |  
| notes         | string | Internal comments or context   |  

## ID Pattern  
^p11_abt_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Experiment Overview**  
   - Purpose, hypothesis, and expected impact.  
2. **Variant Groups**  
   - Definitions, control/variant splits, and user targeting.  
3. **Metrics**  
   - Primary and secondary success metrics with thresholds.  
4. **Schedule**  
   - Start/end dates, rollout phases, and duration.  
5. **Review**  
   - Peer reviewer, approval status, and QA checks.  

## Constraints  
- File size must not exceed 4096 bytes.  
- ID must match exact regex: ^p11_abt_[a-z][a-z0-9_]+.yaml$.  
- All required fields must be present and valid.  
- Quality field must be assigned by peer review, not self-scored.  
- Metrics must include at least one primary success metric.  
- Start/end dates must be within 30 days of each other.
