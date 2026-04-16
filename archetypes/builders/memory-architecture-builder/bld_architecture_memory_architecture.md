---
kind: architecture
id: bld_architecture_memory_architecture
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of the memory_architecture-builder -- 13 ISOs, dependencies, position
quality: 9.0
title: "Architecture: memory_architecture-builder"
version: "2.0.0"
author: n06_commercial
tags: [memory_architecture, builder, architecture]
tldr: "13-ISO builder for LLM agent memory architecture artifacts: knowledge (P01), instructions (P03), schema (P06), quality gate (P11), output template (P05), examples (P07), architecture (P08), collaboration (P12), config (P09), memory (P10), tools (P04), manifest (P02), system_prompt (P03)"
domain: "LLM agent memory systems"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Component Inventory

| ISO File | Kind | Pillar | Role |
|----------|------|--------|------|
| bld_manifest_memory_architecture.md | manifest | P02 | Builder registry entry + meta |
| bld_instruction_memory_architecture.md | instruction | P03 | 3-phase production process (F4 REASON) |
| bld_system_prompt_memory_architecture.md | system_prompt | P03 | Builder persona (F2 BECOME) |
| bld_schema_memory_architecture.md | schema | P06 | Frontmatter contract + body structure (F1 CONSTRAIN) |
| bld_quality_gate_memory_architecture.md | quality_gate | P11 | HARD gates + SOFT scoring (F7 GOVERN) |
| bld_output_template_memory_architecture.md | output_template | P05 | Annotated template with vars (F6 PRODUCE) |
| bld_examples_memory_architecture.md | examples | P07 | Golden + anti-examples (F3 INJECT) |
| bld_knowledge_card_memory_architecture.md | knowledge_card | P01 | Domain knowledge: MemGPT, Zep, mem0, tier matrix (F3 INJECT) |
| bld_architecture_memory_architecture.md | architecture | P08 | This file -- component map |
| bld_collaboration_memory_architecture.md | collaboration_pattern | P12 | Multi-nucleus handoff protocol |
| bld_config_memory_architecture.md | env_config | P09 | Builder runtime parameters |
| bld_memory_memory_architecture.md | memory | P10 | Learned patterns + pitfalls |
| bld_tools_memory_architecture.md | toolkit | P04 | Tools used during construction |

## Dependencies

| Consumer ISO | Depends On | Dependency Type |
|---|---|---|
| bld_instruction | bld_schema | Must reference correct frontmatter fields |
| bld_system_prompt | bld_knowledge_card | Persona grounded in domain knowledge |
| bld_quality_gate | bld_schema | H02 ID pattern comes from schema |
| bld_output_template | bld_schema | Template vars match schema required fields |
| bld_examples | bld_quality_gate | Golden examples must pass all HARD gates |
| bld_memory | bld_knowledge_card | Patterns grounded in domain evidence |

## Architectural Position

memory_architecture is a P10 (Memory) kind. It defines the structural blueprint for
how an LLM agent manages context across sessions. It is the parent artifact that
consolidation_policy (eviction rules) and procedural_memory (skill storage schema)
operate within. An agent system typically has one memory_architecture artifact per
agent type, with consolidation_policy and procedural_memory artifacts as children.

## 8F Stage Map

| 8F Stage | Primary ISOs Used |
|---|---|
| F1 CONSTRAIN | bld_schema, bld_manifest |
| F2 BECOME | bld_system_prompt |
| F3 INJECT | bld_knowledge_card, bld_examples, bld_memory |
| F4 REASON | bld_instruction |
| F5 CALL | bld_tools, bld_config |
| F6 PRODUCE | bld_output_template |
| F7 GOVERN | bld_quality_gate |
| F8 COLLABORATE | bld_collaboration |
