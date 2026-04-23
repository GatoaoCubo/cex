---
kind: architecture
id: bld_architecture_reward_model
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of reward_model -- inventory, dependencies
quality: 9.0
title: "Architecture Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, architecture]
tldr: "Component map of reward_model -- inventory, dependencies"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_architecture_rl_algorithm
  - bld_architecture_reasoning_strategy
  - bld_architecture_search_strategy
  - bld_architecture_tts_provider
  - bld_instruction_reward_model
  - bld_architecture_vad_config
  - bld_architecture_contributor_guide
  - bld_architecture_webinar_script
  - p03_sp_reward_model_builder
  - bld_architecture_memory_architecture
---

## Component Inventory
| ISO | llm_function | Purpose | Status |
|-----|-------------|---------|--------|
| bld_manifest_reward_model | BECOME | Builder identity: process/outcome reward specialist | Production |
| bld_system_prompt_reward_model | BECOME | Persona: governance-aligned reward designer | Production |
| bld_instruction_reward_model | REASON | 3-phase production (Research/Compose/Validate) | Production |
| bld_schema_reward_model | CONSTRAIN | Schema: id pattern ^p07_rwm_*, reward_type enum | Production |
| bld_quality_gate_reward_model | GOVERN | HARD gates (H01-H09) + SOFT scoring (D01-D09) | Production |
| bld_output_template_reward_model | PRODUCE | Frontmatter + body structure for reward_model artifact | Production |
| bld_examples_reward_model | INJECT | Golden (Dialogue Quality RM) + 2 anti-examples | Production |
| bld_knowledge_card_reward_model | INJECT | Domain KC: RLHF, Stiennon et al., ISO 23894 | Production |
| bld_tools_reward_model | CALL | Hugging Face evaluate, Ray, OpenAI eval API | Production |
| bld_collaboration_reward_model | COLLABORATE | Crew: upstream rl_algorithm, downstream scoring_rubric | Production |
| bld_config_reward_model | CONSTRAIN | Naming: p07_rwm_<name>_<ts>.md, max_turns=20 | Production |
| bld_memory_reward_model | INJECT | Learning record: 20-30% alignment improvement patterns | Production |
| bld_architecture_reward_model | CONSTRAIN | This file -- component map and ISO dependencies | Production |

## Dependencies
| From | To | Type |
|------|----|------|
| bld_instruction | bld_schema | Reads schema before compose phase |
| bld_instruction | bld_output_template | Fills template at F6 PRODUCE |
| bld_system_prompt | bld_manifest | Derives governance persona from identity section |
| bld_quality_gate | bld_schema | H02 enforces schema ID pattern ^p07_rwm_* |
| bld_examples | bld_knowledge_card | Examples demonstrate RLHF domain concepts |
| rl_algorithm-builder | reward_model-builder | rl_algorithm consumes reward_model's signal definitions |

## Architectural Position
reward_model-builder occupies P07 (Evaluation pillar) in the CEX taxonomy. It produces process/outcome reward specifications that encode governance objectives as measurable metrics. Upstream: scoring_rubric (rubric inputs), human evaluation (RLHF data). Downstream: rl_algorithm (consumes reward signal), guardrail (uses outcome metrics).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_rl_algorithm]] | sibling | 0.62 |
| [[bld_architecture_reasoning_strategy]] | sibling | 0.56 |
| [[bld_architecture_search_strategy]] | sibling | 0.40 |
| [[bld_architecture_tts_provider]] | sibling | 0.28 |
| [[bld_instruction_reward_model]] | upstream | 0.28 |
| [[bld_architecture_vad_config]] | sibling | 0.27 |
| [[bld_architecture_contributor_guide]] | sibling | 0.26 |
| [[bld_architecture_webinar_script]] | sibling | 0.26 |
| [[p03_sp_reward_model_builder]] | upstream | 0.26 |
| [[bld_architecture_memory_architecture]] | sibling | 0.26 |
