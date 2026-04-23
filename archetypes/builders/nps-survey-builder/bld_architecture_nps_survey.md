---
kind: architecture
id: bld_architecture_nps_survey
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of nps_survey -- inventory, dependencies
quality: 9.0
title: "Architecture Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, architecture]
tldr: "Component map of nps_survey -- inventory, dependencies"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_app_directory_entry
  - bld_architecture_legal_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_sales_playbook
  - bld_architecture_ai_rmf_profile
  - bld_architecture_fintech_vertical
  - bld_architecture_github_issue_template
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Builder identity, routing     | P11    | Active  |
| bld_instruction       | Step-by-step production       | P03    | Active  |
| bld_system_prompt     | LLM persona and rules         | P03    | Active  |
| bld_schema            | Data structure definition     | P06    | Active  |
| bld_quality_gate      | Bain NPS validation rules     | P11    | Active  |
| bld_output_template   | YAML survey scaffold          | P05    | Active  |
| bld_examples          | Golden + anti-examples        | P07    | Active  |
| bld_knowledge_card    | NPS domain knowledge          | P01    | Active  |
| bld_architecture      | System blueprint              | P08    | Active  |
| bld_collaboration     | Workflow coordination         | P12    | Active  |
| bld_config            | Naming, paths, limits         | P09    | Active  |
| bld_memory            | Learned patterns, pitfalls    | P10    | Active  |
| bld_tools             | Production + validation tools | P04    | Active  |

## Dependencies
| From                | To                    | Type          |
|---------------------|-----------------------|---------------|
| bld_manifest        | bld_config            | configuration |
| bld_instruction     | bld_system_prompt     | dependency    |
| bld_output_template | bld_schema            | dependency    |
| bld_quality_gate    | bld_examples          | validation    |
| bld_collaboration   | bld_memory            | coordination  |
| bld_tools           | CRM / survey platform | integration   |

## Architectural Position
nps_survey sits in P11/GOVERN: it is a governance artifact that configures how NPS
data is collected, segmented, and routed. It feeds into retention workflows (P12),
customer-health dashboards (N06), and churn-prevention playbooks (P03). It does NOT
define customer segments (customer_segment kind) nor analyse cohorts (cohort_analysis).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.79 |
| [[bld_architecture_roi_calculator]] | sibling | 0.73 |
| [[bld_architecture_api_reference]] | sibling | 0.72 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.72 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.71 |
| [[bld_architecture_sales_playbook]] | sibling | 0.71 |
| [[bld_architecture_ai_rmf_profile]] | sibling | 0.70 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.69 |
| [[bld_architecture_github_issue_template]] | sibling | 0.69 |
