---
kind: instruction
id: bld_instruction_procedural_memory
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for procedural_memory
quality: 8.9
title: "Instruction: procedural_memory-builder"
version: "2.0.0"
author: n06_commercial
tags: [procedural_memory, builder, instruction]
tldr: "8F production process for LLM agent procedural memory: load schema, define skill namespace, format, storage backend, verification strategy, reflexion notes, tier matrix"
domain: "LLM agent procedural memory"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
related:
  - procedural-memory-builder
  - bld_knowledge_card_procedural_memory
  - p03_sp_procedural_memory_builder
  - bld_schema_procedural_memory
  - bld_instruction_memory_architecture
  - bld_output_template_procedural_memory
  - bld_tools_procedural_memory
  - p10_mem_procedural_memory_builder
  - p10_qg_procedural_memory
  - bld_instruction_consolidation_policy
---

## Phase 1: RESEARCH

1. Identify the parent memory_architecture artifact (which tier is active, what backends).
2. Determine skill format needed: code (Voyager/Code-as-policies), YAML (workflow SOPs),
   natural language (Reflexion notes), or structured JSON.
3. Map the target commercial tier (free/pro/enterprise) against the tier matrix
   in bld_knowledge_card_procedural_memory.md.
4. Review reference systems: Voyager (Wang 2023) for skill library design, Reflexion
   (Shinn 2023) for self-note patterns, ExpeL (Zhao 2023) for experience extraction.
5. Design the skill namespace: `domain.task.subtask` hierarchy for scalable lookup.
6. Check bld_schema_procedural_memory.md for required frontmatter and body structure.

## Phase 2: COMPOSE

1. Write frontmatter per bld_schema_procedural_memory.md (all required fields, quality: null).
2. Write Overview: agent type, tier, what skill domain this covers.
3. Write Skill Definitions table:
   - Columns: Skill ID | Name | Format | Storage Key | Verification | Tier Required
   - Row per skill or skill category
4. Write Skill Namespace section: hierarchy, key pattern, example lookups.
5. Write Storage Backend section: KV store config, encoding format, retrieval method.
6. Write Verification Strategy: how skills are tested before storage (Voyager pattern).
7. Write Reflexion Notes section: how failure-derived self-notes are stored and retrieved.
8. Write Commercial Tier Matrix: FREE/PRO/ENTERPRISE capability comparison.

## Phase 3: VALIDATE

- [ ] Schema compliance: all required frontmatter fields present, ID matches pattern.
- [ ] LLM-domain grounding: content references Voyager/Reflexion/ExpeL, not robotics motors.
- [ ] skill_format field present and valid.
- [ ] Verification strategy defined (or explicitly excluded with reason for non-code formats).
- [ ] Tier matrix present: FREE/PRO/ENTERPRISE differentiation explicit.
- [ ] Free tier: states "no procedural memory" or graceful degradation.
- [ ] quality: null in frontmatter (never self-score).
- [ ] No Unicode characters (ASCII only per ascii-code-rule.md).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[procedural-memory-builder]] | downstream | 0.48 |
| [[bld_knowledge_card_procedural_memory]] | upstream | 0.47 |
| [[p03_sp_procedural_memory_builder]] | related | 0.46 |
| [[bld_schema_procedural_memory]] | downstream | 0.45 |
| [[bld_instruction_memory_architecture]] | sibling | 0.43 |
| [[bld_output_template_procedural_memory]] | downstream | 0.43 |
| [[bld_tools_procedural_memory]] | downstream | 0.38 |
| [[p10_mem_procedural_memory_builder]] | downstream | 0.38 |
| [[p10_qg_procedural_memory]] | downstream | 0.37 |
| [[bld_instruction_consolidation_policy]] | sibling | 0.37 |
