---
kind: architecture
id: bld_architecture_renewal_workflow
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of renewal_workflow -- inventory, dependencies
quality: 9.0
title: "Architecture Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, architecture, renewal, GRR, Gainsight]
tldr: "Component map of renewal_workflow -- inventory, dependencies"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_api_reference
  - bld_architecture_roi_calculator
  - bld_architecture_legal_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_benchmark_suite
  - bld_architecture_sales_playbook
  - bld_architecture_quickstart_guide
  - bld_architecture_ai_rmf_profile
  - bld_architecture_expansion_play
---

## Component Inventory
| ISO Name              | Role                               | Pillar | Status  |
|-----------------------|------------------------------------|--------|---------|
| bld_manifest          | Builder identity and routing       | P11    | Active  |
| bld_instruction       | Production process (3 phases)      | P03    | Active  |
| bld_system_prompt     | LLM persona and rules              | P03    | Active  |
| bld_schema            | Renewal workflow data structure    | P06    | Active  |
| bld_quality_gate      | GRR/stage completion validation    | P11    | Active  |
| bld_output_template   | Renewal stage document formatting  | P05    | Active  |
| bld_examples          | Golden and anti-examples           | P07    | Active  |
| bld_knowledge_card    | Renewal operations domain knowledge| P01    | Active  |
| bld_architecture      | System blueprint (this file)       | P08    | Active  |
| bld_collaboration     | CSM/RevOps/Legal crew coordination | P12    | Active  |
| bld_config            | Naming, paths, runtime limits      | P09    | Active  |
| bld_memory            | Learned renewal patterns           | P10    | Active  |
| bld_tools             | Salesforce/Gainsight integrations  | P04    | Active  |

## Dependencies
| From                  | To                       | Type          |
|-----------------------|--------------------------|---------------|
| bld_manifest          | bld_config               | configuration |
| bld_instruction       | bld_schema               | dependency    |
| bld_output_template   | bld_schema               | dependency    |
| bld_quality_gate      | bld_examples             | validation    |
| bld_collaboration     | bld_memory               | coordination  |
| bld_tools             | Salesforce/Gainsight APIs| integration   |
| bld_system_prompt     | bld_instruction          | dependency    |

## Architectural Position
renewal_workflow serves as the GRR protection engine within CEX P12 orchestration layer, automating the contract lifecycle from 90-day pre-renewal through close. It bridges Salesforce (opportunity management), Gainsight (health scoring and CTA automation), and Legal (contract amendment governance), enforcing stage-gated accountability and price-increase compliance across the renewal motion used by Salesforce, HubSpot, and Gainsight-native CS organizations.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.68 |
| [[bld_architecture_api_reference]] | sibling | 0.68 |
| [[bld_architecture_roi_calculator]] | sibling | 0.68 |
| [[bld_architecture_legal_vertical]] | sibling | 0.67 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.67 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.66 |
| [[bld_architecture_sales_playbook]] | sibling | 0.65 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.65 |
| [[bld_architecture_ai_rmf_profile]] | sibling | 0.64 |
| [[bld_architecture_expansion_play]] | sibling | 0.64 |
