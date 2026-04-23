---
kind: architecture
id: bld_architecture_product_tour
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of product_tour -- inventory, dependencies
quality: 9.0
title: "Architecture Product Tour"
version: "1.0.1"
author: n02_marketing
tags: [product_tour, builder, architecture]
tldr: "Component map of product_tour -- inventory, dependencies"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_pitch_deck
  - bld_architecture_interactive_demo
  - bld_architecture_legal_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
  - bld_architecture_github_issue_template
  - bld_architecture_benchmark_suite
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_memory_benchmark
---

## Component Inventory
| ISO Name | Role | Pillar | llm_function | Status |
|---|---|---|---|---|
| bld_manifest_product_tour | Builder identity, capabilities, routing | P05 | BECOME | Active |
| bld_instruction_product_tour | Step-by-step production process (Research/Compose/Validate) | P03 | REASON | Active |
| bld_system_prompt_product_tour | Agent persona, scope rules, quality constraints | P03 | BECOME | Active |
| bld_schema_product_tour | YAML frontmatter spec and field validation rules | P06 | CONSTRAIN | Active |
| bld_quality_gate_product_tour | HARD gates + SOFT 5D scoring rubric | P11 | GOVERN | Active |
| bld_output_template_product_tour | Tour step template with (template variables), trigger and tooltip fields | P05 | PRODUCE | Active |
| bld_examples_product_tour | Reference tour specs for few-shot guidance | P05 | INJECT | Active |
| bld_knowledge_card_product_tour | Domain knowledge: Pendo/Appcues/WalkMe patterns, TTV metrics | P01 | INJECT | Active |
| bld_architecture_product_tour | This file: component map and dependency graph | P08 | CONSTRAIN | Active |
| bld_collaboration_product_tour | Crew roles: receives-from / produces-for boundaries | P12 | COLLABORATE | Active |
| bld_config_product_tour | Runtime parameters: defaults, limits, toggles | P09 | CONSTRAIN | Active |
| bld_memory_product_tour | Learned patterns and pitfalls for product_tour | P10 | INJECT | Active |
| bld_tools_product_tour | CEX tools and external references | P04 | CALL | Active |

## Dependencies
| From | To | Type |
|---|---|---|
| bld_instruction_product_tour | bld_schema_product_tour | reference (COMPOSE step 1) |
| bld_instruction_product_tour | bld_output_template_product_tour | reference (COMPOSE step 5, 7) |
| bld_quality_gate_product_tour | bld_schema_product_tour | validation (H02 ID pattern) |
| bld_quality_gate_product_tour | bld_examples_product_tour | calibration (SOFT scoring) |
| bld_output_template_product_tour | bld_schema_product_tour | structural alignment |
| bld_system_prompt_product_tour | bld_knowledge_card_product_tour | domain injection |
| bld_memory_product_tour | bld_knowledge_card_product_tour | pattern reinforcement |

## Architectural Position
product_tour is a P05 output builder producing in-app tour specifications (tooltip sequences, step triggers, ARIA annotations). It occupies the post-purchase activation layer: after a user signs up, product_tour drives time-to-value by surfacing critical features at contextually relevant moments. Primary platforms: Pendo, Appcues, WalkMe, Intercom Product Tours.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_pitch_deck]] | sibling | 0.59 |
| [[bld_architecture_interactive_demo]] | sibling | 0.55 |
| [[bld_architecture_legal_vertical]] | sibling | 0.52 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.52 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.51 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.50 |
| [[bld_architecture_github_issue_template]] | sibling | 0.50 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.49 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.47 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.47 |
