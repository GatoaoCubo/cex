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
