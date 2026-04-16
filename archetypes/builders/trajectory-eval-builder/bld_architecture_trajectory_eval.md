---
kind: architecture
id: bld_architecture_trajectory_eval
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of trajectory_eval -- inventory, dependencies
quality: 9.0
title: "Architecture Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, architecture]
tldr: "13-ISO component map for trajectory_eval-builder: correct pillars and dependencies."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
---

## Component Inventory
| ISO Name | Role | Pillar | Status |
|---|---|---|---|
| bld_manifest_trajectory_eval | Builder identity, capabilities, routing | P07 | Active |
| bld_instruction_trajectory_eval | Step-by-step production process | P03 | Active |
| bld_system_prompt_trajectory_eval | LLM persona + rules for builder | P03 | Active |
| bld_schema_trajectory_eval | Formal schema (agent_id, task_id, step_count) | P06 | Active |
| bld_quality_gate_trajectory_eval | HARD gates H01-H07 + SOFT 5D scoring | P11 | Active |
| bld_output_template_trajectory_eval | Template: step log, metrics, failure analysis | P05 | Active |
| bld_examples_trajectory_eval | Worked examples with real benchmark tasks | P01 | Active |
| bld_knowledge_card_trajectory_eval | Domain KC: AgentBench, WebArena, SWE-bench | P01 | Active |
| bld_architecture_trajectory_eval | This file -- component inventory | P08 | Active |
| bld_collaboration_trajectory_eval | Multi-builder coordination patterns | P12 | Active |
| bld_config_trajectory_eval | Naming, paths, limits | P09 | Active |
| bld_memory_trajectory_eval | Learned patterns for trajectory_eval construction | P10 | Active |
| bld_tools_trajectory_eval | Real CEX tools + benchmark references | P04 | Active |

## Dependencies
| From | To | Type |
|---|---|---|
| bld_instruction | bld_schema | Reads field definitions |
| bld_output_template | bld_schema | Inherits frontmatter shape |
| bld_quality_gate | bld_schema | Validates against ID pattern |
| bld_instruction | bld_output_template | Uses as structural guide |
| bld_system_prompt | bld_knowledge_card | Persona informed by domain KC |
| bld_tools | cex_compile.py | Compiles artifacts post-save |

## Architectural Position
trajectory_eval operates in P07 (Evaluation), producing step-level evaluation records for
LLM agent decision trajectories. It bridges agent benchmarking (AgentBench, WebArena, SWE-bench)
with CEX artifact quality standards by converting raw trajectory logs into structured,
diagnosable evaluation artifacts.
