---
kind: architecture
id: bld_architecture_ai_rmf_profile
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of ai_rmf_profile -- inventory, dependencies
quality: 9.0
title: "Architecture AI RMF Profile"
version: "1.0.0"
author: n01_wave7
tags: [ai_rmf_profile, builder, architecture, NIST, AI-RMF, GOVERN, MAP, MEASURE, MANAGE]
tldr: "Component map of ai_rmf_profile -- inventory, dependencies"
domain: "ai_rmf_profile construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name | Role | Pillar | Status |
|----------|------|--------|--------|
| bld_manifest | Builder identity and routing | P11 | Active |
| bld_instruction | Step-by-step production process | P03 | Active |
| bld_system_prompt | LLM persona and rules | P03 | Active |
| bld_schema | YAML schema and ID pattern | P06 | Active |
| bld_quality_gate | HARD gates + SOFT scoring | P11 | Active |
| bld_output_template | Annex IV-style output template with vars | P05 | Active |
| bld_examples | Golden and anti-examples | P07 | Active |
| bld_knowledge_card | NIST AI-RMF domain knowledge | P01 | Active |
| bld_architecture | Component map and dependencies | P08 | Active |
| bld_collaboration | Cross-builder workflow coordination | P12 | Active |
| bld_config | Naming, paths, limits | P09 | Active |
| bld_memory | Session persistence and learned patterns | P10 | Active |
| bld_tools | Production and validation tools | P04 | Active |

## Dependencies
| From | To | Type |
|------|----|------|
| bld_manifest | bld_config | configuration |
| bld_instruction | bld_system_prompt | dependency |
| bld_output_template | bld_schema | dependency |
| bld_quality_gate | bld_examples | validation reference |
| bld_collaboration | bld_memory | coordination |
| bld_tools | bld_quality_gate | validation |

## Architectural Position
ai_rmf_profile occupies the governance compliance intersection within CEX P11 (Feedback/Governance). It bridges NIST AI-RMF policy requirements and CEX artifact production, enabling structured profile artifacts that map AI system risks to AI-RMF actions. Upstream: compliance_framework (broader regulatory mapping). Downstream: threat_model (risk analysis), safety_policy (org-level enforcement). Crosswalk: iso_42001 controls, EU AI Act obligations.
