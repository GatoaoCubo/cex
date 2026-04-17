---
kind: architecture
id: bld_architecture_pitch_deck
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of pitch_deck -- inventory, dependencies
quality: 9.0
title: "Architecture Pitch Deck"
version: "1.0.1"
author: n02_marketing
tags: [pitch_deck, builder, architecture]
tldr: "Component map of pitch_deck -- inventory, dependencies"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name | Role | Pillar | llm_function | Status |
|---|---|---|---|---|
| bld_manifest_pitch_deck | Builder identity, capabilities, routing | P05 | BECOME | Active |
| bld_instruction_pitch_deck | Step-by-step production process (Research/Compose/Validate) | P03 | REASON | Active |
| bld_system_prompt_pitch_deck | Agent persona, scope rules, quality constraints | P03 | BECOME | Active |
| bld_schema_pitch_deck | YAML frontmatter spec and field validation rules | P06 | CONSTRAIN | Active |
| bld_quality_gate_pitch_deck | HARD gates + SOFT 5D scoring rubric | P11 | GOVERN | Active |
| bld_output_template_pitch_deck | Slide structure template with (template variables) | P05 | PRODUCE | Active |
| bld_examples_pitch_deck | Reference pitch deck instances for few-shot | P05 | INJECT | Active |
| bld_knowledge_card_pitch_deck | Domain knowledge: frameworks, concepts, pitfalls | P01 | INJECT | Active |
| bld_architecture_pitch_deck | This file: component map and dependency graph | P08 | CONSTRAIN | Active |
| bld_collaboration_pitch_deck | Crew roles: receives-from / produces-for boundaries | P12 | COLLABORATE | Active |
| bld_config_pitch_deck | Runtime parameters: defaults, limits, toggles | P09 | CONSTRAIN | Active |
| bld_memory_pitch_deck | Learned patterns and pitfalls for pitch_deck | P10 | INJECT | Active |
| bld_tools_pitch_deck | CEX tools and external references | P04 | CALL | Active |

## Dependencies
| From | To | Type |
|---|---|---|
| bld_instruction_pitch_deck | bld_schema_pitch_deck | reference (COMPOSE step 1) |
| bld_instruction_pitch_deck | bld_output_template_pitch_deck | reference (COMPOSE step 6) |
| bld_quality_gate_pitch_deck | bld_schema_pitch_deck | validation (H02 ID pattern) |
| bld_quality_gate_pitch_deck | bld_examples_pitch_deck | calibration (SOFT scoring) |
| bld_output_template_pitch_deck | bld_schema_pitch_deck | structural alignment |
| bld_system_prompt_pitch_deck | bld_knowledge_card_pitch_deck | domain injection |
| bld_memory_pitch_deck | bld_knowledge_card_pitch_deck | pattern reinforcement |

## Architectural Position
pitch_deck is a P05 output builder producing investor-facing slide narratives. It occupies the conversion-narrative layer alongside interactive_demo (self-serve evaluation) and product_tour (in-app activation). The narrative arc -- problem -> solution -> proof -> ask -- runs as a through-line across all three kinds.
