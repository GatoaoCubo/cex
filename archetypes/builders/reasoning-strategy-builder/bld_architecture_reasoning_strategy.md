---
kind: architecture
id: bld_architecture_reasoning_strategy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of reasoning_strategy -- inventory, dependencies
quality: 9.0
title: "Architecture Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, architecture]
tldr: "Component map of reasoning_strategy -- inventory, dependencies"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Component Inventory  

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
| ISO | llm_function | Purpose | Status |  
|-----|-------------|---------|--------|  
| bld_manifest_reasoning_strategy | BECOME | Builder identity, capabilities, routing | Production |  
| bld_system_prompt_reasoning_strategy | BECOME | Persona injected at F2 — reasoning specialist | Production |  
| bld_instruction_reasoning_strategy | REASON | 3-phase production process (Research/Compose/Validate) | Production |  
| bld_schema_reasoning_strategy | CONSTRAIN | Formal field schema, ID pattern, body structure | Production |  
| bld_quality_gate_reasoning_strategy | GOVERN | HARD gates (H01-H10) + SOFT scoring (D01-D08) | Production |  
| bld_output_template_reasoning_strategy | PRODUCE | Frontmatter template + section stubs | Production |  
| bld_examples_reasoning_strategy | INJECT | Golden example + 2 anti-examples with boundary notes | Production |  
| bld_knowledge_card_reasoning_strategy | INJECT | Domain KC: reasoning paradigms, industry standards | Production |  
| bld_tools_reasoning_strategy | CALL | Validation tools, external refs (PyTorch, LangChain) | Production |  
| bld_collaboration_reasoning_strategy | COLLABORATE | Crew roles: upstream/downstream builders | Production |  
| bld_config_reasoning_strategy | CONSTRAIN | Naming convention, paths, size limits | Production |  
| bld_memory_reasoning_strategy | INJECT | Learning record: lessons from past builds | Production |  
| bld_architecture_reasoning_strategy | CONSTRAIN | This file -- component map and dependencies | Production |  

## Dependencies  
| From | To | Type |  
|------|----|------|  
| bld_instruction | bld_schema | Reads schema before compose phase |  
| bld_instruction | bld_output_template | Fills template at F6 PRODUCE |  
| bld_system_prompt | bld_manifest | Derives persona from identity section |  
| bld_quality_gate | bld_schema | H02 pattern enforces schema ID rule |  
| bld_examples | bld_knowledge_card | Examples demonstrate KC domain concepts |  
| bld_tools | bld_config | Tools must respect path/size config limits |  

## Architectural Position  
reasoning_strategy-builder occupies P03 (Prompt pillar) in the CEX taxonomy. It produces structured reasoning blueprints (deductive, inductive, abductive) consumed by agent prompts and chain orchestration. Upstream: knowledge_card (domain input). Downstream: prompt_template, chain, system_prompt (consumers of the strategy).
