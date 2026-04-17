---
kind: architecture
id: bld_architecture_gpai_technical_doc
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of gpai_technical_doc -- inventory, dependencies
quality: 9.0
title: "Architecture GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, architecture, GPAI, EU-AI-Act, Annex-IV]
tldr: "Component map of gpai_technical_doc -- inventory, dependencies"
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name | Role | Pillar | Status |
|----------|------|--------|--------|
| bld_manifest | Builder identity and routing | P11 | Active |
| bld_instruction | Annex IV production process | P03 | Active |
| bld_system_prompt | LLM persona for EU compliance | P03 | Active |
| bld_schema | Annex IV field schema | P06 | Active |
| bld_quality_gate | EU AI Office submission gates | P11 | Active |
| bld_output_template | Annex IV structured template | P05 | Active |
| bld_examples | Golden GPAI doc + anti-examples | P07 | Active |
| bld_knowledge_card | EU AI Act domain knowledge | P01 | Active |
| bld_architecture | Component map and dependencies | P08 | Active |
| bld_collaboration | Cross-builder workflow | P12 | Active |
| bld_config | Naming, paths, limits | P09 | Active |
| bld_memory | Session persistence and patterns | P10 | Active |
| bld_tools | Production and validation tools | P04 | Active |

## Dependencies
| From | To | Type |
|------|----|------|
| bld_manifest | bld_config | configuration |
| bld_instruction | bld_schema | dependency |
| bld_output_template | bld_schema | dependency |
| bld_quality_gate | bld_examples | validation reference |
| bld_tools | bld_quality_gate | validation |

## Architectural Position
gpai_technical_doc is the EU AI Act compliance artifact within CEX P11. It bridges EU legal requirements (Article 53 / Annex IV) and structured model documentation. Distinct from: model_card (informal), compliance_framework (policy mapping), conformity_assessment (high-risk systems). Upstream inputs: training metadata from ML engineering, evaluation results from N05, energy data from infrastructure. Downstream: EU AI Office submission, downstream provider agreements.
