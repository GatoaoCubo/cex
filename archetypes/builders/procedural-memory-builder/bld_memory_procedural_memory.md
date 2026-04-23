---
kind: memory
id: p10_mem_procedural_memory_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for procedural_memory construction
quality: 8.9
title: "Memory: procedural_memory-builder patterns"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, memory]
tldr: "Key lessons: cite Voyager/Reflexion/ExpeL, always verify before storing, use hierarchical namespace, add tier matrix, free tier = no procedural memory"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - p03_sp_procedural_memory_builder
  - bld_knowledge_card_procedural_memory
  - procedural-memory-builder
  - bld_instruction_procedural_memory
  - bld_tools_procedural_memory
  - bld_collaboration_procedural_memory
  - bld_output_template_procedural_memory
  - bld_examples_procedural_memory
  - bld_schema_procedural_memory
  - bld_collaboration_skill
---

## Observation

The original procedural_memory knowledge_card had partial domain relevance (skill
acquisition, RL, procedural abstraction) but was grounded in robotics/HCI literature
(Anderson ACT-R, motor schemas, Brooks subsumption architecture) rather than the
LLM-specific systems that are the actual domain. The quality gate tested runtime
metrics (retrieval latency, error rate, recovery time) not artifact structure.

## Pattern

High-quality procedural_memory artifacts share four traits:
1. Cite LLM-specific references: Voyager (Wang 2023) for skill library, Reflexion
   (Shinn 2023) for self-notes, ExpeL (Zhao 2023) for experience extraction.
2. Define skill_format explicitly: code (Python/JS), YAML, natural language, or JSON.
3. Include skill verification: what checks prevent unverified skills from entering the library.
4. Commercial tier matrix: FREE (no skills), PRO (shared library), ENTERPRISE (versioned + team).

## Evidence

Wave 3 generation (qwen3:14b) produced partially relevant knowledge_card and reasonable
system_prompt for procedural_memory, but:
- knowledge_card cited Anderson ACT-R (1993), motor schemas, robotics frameworks -- not Voyager
- quality_gate tested: retrieval latency <=200ms, error rate <=0.1%, recovery time <=5min
  (D03: runtime metrics, not artifact structure)
- quality_gate SOFT table had a broken format (3 columns for GOLDEN/PUBLISH/REVIEW/REJECT)
- bld_memory had kind: learning_record instead of kind: memory (D02)

## Recommendations

- The robotics/cognitive science framing is not wrong (procedural memory IS a cognitive
  concept) but it misses the production-relevant literature. Always cite Voyager first.
- Skill verification is the key differentiator between good and bad procedural memory
  systems. Voyager's verify-before-store pattern prevents skill contamination.
- Reflexion self-notes are a lighter alternative to full skill libraries for agents that
  don't need executable code -- document this as an option in the output_template.
- Free tier: no procedural memory. Agents degrade gracefully by reasoning from scratch.
  Document this explicitly; do not leave it ambiguous.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_procedural_memory_builder]] | upstream | 0.59 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.52 |
| [[procedural-memory-builder]] | related | 0.49 |
| [[bld_instruction_procedural_memory]] | upstream | 0.49 |
| [[bld_tools_procedural_memory]] | upstream | 0.38 |
| [[bld_collaboration_procedural_memory]] | downstream | 0.37 |
| [[bld_output_template_procedural_memory]] | upstream | 0.37 |
| [[bld_examples_procedural_memory]] | upstream | 0.36 |
| [[bld_schema_procedural_memory]] | upstream | 0.35 |
| [[bld_collaboration_skill]] | downstream | 0.30 |
