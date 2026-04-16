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
