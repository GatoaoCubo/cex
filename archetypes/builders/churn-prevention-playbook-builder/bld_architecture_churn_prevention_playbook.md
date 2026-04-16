---
kind: architecture
id: bld_architecture_churn_prevention_playbook
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of churn_prevention_playbook -- inventory, dependencies
quality: 9.0
title: "Architecture Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, architecture]
tldr: "Component map of churn_prevention_playbook -- inventory, dependencies"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name              | Role                                  | Pillar | Status  |
|-----------------------|---------------------------------------|--------|---------|
| bld_manifest          | Builder identity, routing             | P03    | Active  |
| bld_instruction       | Step-by-step production               | P03    | Active  |
| bld_system_prompt     | LLM persona and rules                 | P03    | Active  |
| bld_schema            | Data structure definition             | P06    | Active  |
| bld_quality_gate      | Retention intervention validation     | P11    | Active  |
| bld_output_template   | Playbook scaffold                     | P05    | Active  |
| bld_examples          | Golden + anti-examples                | P07    | Active  |
| bld_knowledge_card    | CS ops domain knowledge               | P01    | Active  |
| bld_architecture      | System blueprint                      | P08    | Active  |
| bld_collaboration     | Workflow coordination                 | P12    | Active  |
| bld_config            | Naming, paths, limits                 | P09    | Active  |
| bld_memory            | Learned patterns, pitfalls            | P10    | Active  |
| bld_tools             | CS platform integrations              | P04    | Active  |

## Dependencies
| From                | To                       | Type          |
|---------------------|--------------------------|---------------|
| bld_manifest        | bld_config               | configuration |
| bld_instruction     | bld_system_prompt        | dependency    |
| bld_output_template | bld_schema               | dependency    |
| bld_quality_gate    | bld_examples             | validation    |
| bld_collaboration   | nps_survey kind          | signal-in     |
| bld_tools           | Gainsight / ChurnZero    | integration   |

## Architectural Position
churn_prevention_playbook sits in P03/PRODUCE: it is a strategy artifact that produces
actionable intervention scripts. It receives NPS detractor signals from nps_survey (P11)
and health score data from CS platforms. It feeds escalation workflows (P12) and win-back
sequences. It is upstream of renewal_workflow but downstream of cohort_analysis.
