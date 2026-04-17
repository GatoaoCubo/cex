---
kind: architecture
id: bld_architecture_rl_algorithm
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of rl_algorithm -- inventory, dependencies
quality: 9.0
title: "Architecture Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, architecture]
tldr: "Component map of rl_algorithm -- inventory, dependencies"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory
| ISO | llm_function | Purpose | Status |
|-----|-------------|---------|--------|
| bld_manifest_rl_algorithm | BECOME | Builder identity: RL algorithm specialist | Production |
| bld_system_prompt_rl_algorithm | BECOME | Persona: mathematically rigorous algorithm designer | Production |
| bld_instruction_rl_algorithm | REASON | 3-phase production (Research/Compose/Validate) | Production |
| bld_schema_rl_algorithm | CONSTRAIN | Schema: id pattern ^p02_rla_*, required fields | Production |
| bld_quality_gate_rl_algorithm | GOVERN | HARD gates (H01-H07) + SOFT scoring (D01-D08) | Production |
| bld_output_template_rl_algorithm | PRODUCE | Frontmatter + body structure for rl_algorithm artifact | Production |
| bld_examples_rl_algorithm | INJECT | Golden (PPO) + 2 anti-examples with boundary notes | Production |
| bld_knowledge_card_rl_algorithm | INJECT | Domain KC: RL paradigms, Sutton & Barto references | Production |
| bld_tools_rl_algorithm | CALL | Stable Baselines3, Ray Tune, TensorBoard | Production |
| bld_collaboration_rl_algorithm | COLLABORATE | Crew: upstream reward_model, downstream training pipeline | Production |
| bld_config_rl_algorithm | CONSTRAIN | Naming, paths, max_bytes=5120, max_turns=100 | Production |
| bld_memory_rl_algorithm | INJECT | Learning record: modular pseudocode patterns | Production |
| bld_architecture_rl_algorithm | CONSTRAIN | This file -- component map and ISO dependencies | Production |

## Dependencies
| From | To | Type |
|------|----|------|
| bld_instruction | bld_schema | Reads schema before compose phase |
| bld_instruction | bld_output_template | Fills template at F6 PRODUCE |
| bld_system_prompt | bld_manifest | Derives persona from identity section |
| bld_quality_gate | bld_schema | H02 enforces schema ID pattern ^p02_rla_* |
| bld_examples | bld_knowledge_card | Examples reference KC RL paradigm concepts |
| reward_model-builder | rl_algorithm-builder | reward_model defines reward signal rl_algorithm consumes |

## Architectural Position
rl_algorithm-builder occupies P02 (Model pillar) in the CEX taxonomy. It produces training algorithm definitions (policy optimization, exploration-exploitation rules, convergence guarantees) consumed by training pipelines and agent configurations. Upstream: reward_model (reward signal definitions). Downstream: boot_config, agent (consume trained policies).
