---
kind: architecture
id: bld_architecture_team_charter
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of team_charter -- inventory, dependencies
quality: 9.1
title: "Architecture Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, architecture, governance]
tldr: "Component map of team_charter -- inventory, dependencies"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_legal_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_benchmark_suite
  - bld_architecture_code_of_conduct
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_healthcare_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_ai_rmf_profile
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Builder identity + routing    | P12    | Active  |
| bld_instruction       | Step-by-step production       | P03    | Active  |
| bld_system_prompt     | LLM persona + rules           | P03    | Active  |
| bld_schema            | SSOT field definitions        | P06    | Active  |
| bld_quality_gate      | 8F scoring thresholds         | P11    | Active  |
| bld_output_template   | Var-substitution template     | P05    | Active  |
| bld_examples          | Golden + anti-examples        | P07    | Active  |
| bld_knowledge_card    | PMI/OKR/SLA domain knowledge  | P01    | Active  |
| bld_architecture      | This component map            | P08    | Active  |
| bld_collaboration     | Crew coordination protocol    | P12    | Active  |
| bld_config            | Naming, paths, runtime limits | P09    | Active  |
| bld_memory            | Learned patterns + pitfalls   | P10    | Active  |
| bld_tools             | Production + validation tools | P04    | Active  |

## Dependencies
| From                | To                        | Type          |
|---------------------|---------------------------|---------------|
| bld_manifest        | bld_config                | configuration |
| bld_instruction     | bld_schema                | dependency    |
| bld_instruction     | bld_system_prompt         | dependency    |
| bld_output_template | bld_schema                | dependency    |
| bld_quality_gate    | bld_examples              | validation    |
| bld_collaboration   | bld_memory                | coordination  |
| bld_tools           | cex_score.py              | integration   |
| bld_schema          | crew_template_ref (P12)   | reference     |
| bld_schema          | decision_manifest.yaml    | reference     |

## Architectural Position
team_charter occupies the governance layer of P12 (Orchestration). It sits ABOVE dispatch_rule and handoff (implementation layer) and BELOW the N07 orchestrator (meta-governance layer). The charter is the bridge between the GDP co-pilot phase (user decisions) and the autonomous execution phase (nucleus dispatch). Without a charter, nuclei have no authorized scope boundary; with a charter, N07 can enforce budget, quality, and termination constraints without user re-engagement.

## Data Flow
```
GDP Decision Manifest  -->  team_charter_builder  -->  team_charter artifact
crew_template_ref      -->  (validates capability fit)  |
                                                         v
                                             N07 dispatch (handoffs reference charter)
                                                         |
                                             Nuclei execute within charter constraints
                                                         |
                                             Termination criteria evaluated by N07
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_legal_vertical]] | sibling | 0.67 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.66 |
| [[bld_architecture_roi_calculator]] | sibling | 0.66 |
| [[bld_architecture_api_reference]] | sibling | 0.65 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.65 |
| [[bld_architecture_code_of_conduct]] | sibling | 0.65 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.64 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.64 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.64 |
| [[bld_architecture_ai_rmf_profile]] | sibling | 0.63 |
