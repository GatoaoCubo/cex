---
kind: collaboration
id: bld_collaboration_dataset_card
pillar: P12
llm_function: COLLABORATE
purpose: How dataset_card-builder works in crews with other builders
quality: 8.9
title: "Collaboration Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, collaboration]
tldr: "How dataset_card-builder works in crews with other builders"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - dataset-card-builder
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_llm_evaluation_scenario
  - bld_collaboration_capability_registry
  - bld_collaboration_eval_framework
  - p03_sp_dataset_card_builder
  - bld_collaboration_prompt_technique
  - bld_collaboration_agent_profile
  - bld_collaboration_action_paradigm
  - bld_collaboration_eval_dataset
---

## Crew Role
Standardizes and automates the creation of dataset documentation, transforming raw metadata, schema definitions, and legal constraints into structured, human-readable dataset cards.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| data_auditor | Data statistics and distributions | JSON |
| legal_agent | Licensing and usage restrictions | Text |
| data_engineer | Schema and structural metadata | YAML |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| data_scientist | Finalized Dataset Card | Markdown |
| compliance_officer | Privacy and usage summary | Markdown |
| model_trainer | Data provenance and lineage info | JSON |

## Boundary
- Does NOT generate evaluation benchmarks or metrics (handled by eval_dataset-builder).
- Does NOT define general domain knowledge or facts (handled by knowledge_card-builder).
- Does NOT perform data cleaning or preprocessing (handled by data_pipeline-agent).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[dataset-card-builder]] | upstream | 0.36 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.33 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.30 |
| [[bld_collaboration_capability_registry]] | sibling | 0.29 |
| [[bld_collaboration_eval_framework]] | sibling | 0.28 |
| [[p03_sp_dataset_card_builder]] | upstream | 0.27 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.27 |
| [[bld_collaboration_agent_profile]] | sibling | 0.27 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.26 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.26 |
