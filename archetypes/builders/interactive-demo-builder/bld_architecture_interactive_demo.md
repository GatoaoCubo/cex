---
kind: architecture
id: bld_architecture_interactive_demo
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of interactive_demo -- inventory, dependencies
quality: 9.0
title: "Architecture Interactive Demo"
version: "1.0.1"
author: n02_marketing
tags: [interactive_demo, builder, architecture]
tldr: "Component map of interactive_demo -- inventory, dependencies"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_pitch_deck
  - bld_architecture_product_tour
  - bld_architecture_legal_vertical
  - bld_architecture_app_directory_entry
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
  - bld_architecture_github_issue_template
  - bld_architecture_benchmark_suite
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_api_reference
---

## Component Inventory
| ISO Name | Role | Pillar | llm_function | Status |
|---|---|---|---|---|
| bld_manifest_interactive_demo | Builder identity, capabilities, routing | P05 | BECOME | Active |
| bld_instruction_interactive_demo | Step-by-step production process (Research/Compose/Validate) | P03 | REASON | Active |
| bld_system_prompt_interactive_demo | Agent persona, scope rules, quality constraints | P03 | BECOME | Active |
| bld_schema_interactive_demo | YAML frontmatter spec and field validation rules | P06 | CONSTRAIN | Active |
| bld_quality_gate_interactive_demo | HARD gates + SOFT 5D scoring rubric | P11 | GOVERN | Active |
| bld_output_template_interactive_demo | Demo script template with (template variables) and step structure | P05 | PRODUCE | Active |
| bld_examples_interactive_demo | Reference demo scripts for few-shot guidance | P05 | INJECT | Active |
| bld_knowledge_card_interactive_demo | Domain knowledge: platforms, talk tracks, presales patterns | P01 | INJECT | Active |
| bld_architecture_interactive_demo | This file: component map and dependency graph | P08 | CONSTRAIN | Active |
| bld_collaboration_interactive_demo | Crew roles: receives-from / produces-for boundaries | P12 | COLLABORATE | Active |
| bld_config_interactive_demo | Runtime parameters: defaults, limits, toggles | P09 | CONSTRAIN | Active |
| bld_memory_interactive_demo | Learned patterns and pitfalls for interactive_demo | P10 | INJECT | Active |
| bld_tools_interactive_demo | CEX tools and external references | P04 | CALL | Active |

## Dependencies
| From | To | Type |
|---|---|---|
| bld_instruction_interactive_demo | bld_schema_interactive_demo | reference (COMPOSE step 1) |
| bld_instruction_interactive_demo | bld_output_template_interactive_demo | reference (COMPOSE step 4) |
| bld_quality_gate_interactive_demo | bld_schema_interactive_demo | validation (H02 ID pattern) |
| bld_quality_gate_interactive_demo | bld_examples_interactive_demo | calibration (SOFT scoring) |
| bld_output_template_interactive_demo | bld_schema_interactive_demo | structural alignment |
| bld_system_prompt_interactive_demo | bld_knowledge_card_interactive_demo | domain injection |
| bld_memory_interactive_demo | bld_knowledge_card_interactive_demo | pattern reinforcement |

## Architectural Position
interactive_demo is a P05 output builder producing self-serve guided-tour scripts and talk tracks. It occupies the self-serve evaluation layer: after pitch_deck closes the deal conceptually, interactive_demo lets buyers explore the product independently. The presales SE playbook (talk track + objection map) is the primary structural reference.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_pitch_deck]] | sibling | 0.61 |
| [[bld_architecture_product_tour]] | sibling | 0.53 |
| [[bld_architecture_legal_vertical]] | sibling | 0.52 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.51 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.51 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.50 |
| [[bld_architecture_github_issue_template]] | sibling | 0.50 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.50 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.48 |
| [[bld_architecture_api_reference]] | sibling | 0.47 |
