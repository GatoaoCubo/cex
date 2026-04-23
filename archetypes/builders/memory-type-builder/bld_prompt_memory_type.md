---
kind: instruction
id: bld_instruction_memory_type
pillar: P03
llm_function: REASON
quality: 9.0
title: "Instruction Memory Type"
version: "1.0.0"
author: n03_builder
tags: [memory_type, builder, examples]
tldr: "Golden and anti-examples for memory type construction, demonstrating ideal structure and common pitfalls."
domain: "memory type construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_memory_type
  - bld_manifest_memory_type
  - bld_output_template_memory_type
  - bld_instruction_memory_scope
  - bld_tools_memory_type
  - bld_instruction_golden_test
  - bld_instruction_builder
  - bld_config_memory_type
  - bld_instruction_retriever_config
  - bld_collaboration_memory_scope
---
# Instruction: Build a memory_type artifact

## Phase 1: Classify
1. Identify which of the 4 memory types this artifact defines
2. Determine the correct decay rate (0.0 for corrections, up to 0.05 for context)
3. Decide if this type survives context compression

## Phase 2: Define
4. Write a clear definition of what observations belong to this type
5. Provide the decay formula and rationale
6. Specify storage location and format rules

## Phase 3: Exemplify
7. Provide 3+ concrete examples of observations that match this type
8. Provide 2+ anti-examples (observations that seem like this type but are not)

## Phase 4: Integrate
9. Document how cex_memory_types.py should classify this type
10. Specify interaction with cex_memory_age.py freshness tags

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify memory
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | memory type construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_type]] | downstream | 0.35 |
| [[bld_manifest_memory_type]] | upstream | 0.33 |
| [[bld_output_template_memory_type]] | downstream | 0.31 |
| [[bld_instruction_memory_scope]] | sibling | 0.30 |
| [[bld_tools_memory_type]] | downstream | 0.28 |
| [[bld_instruction_golden_test]] | sibling | 0.27 |
| [[bld_instruction_builder]] | sibling | 0.27 |
| [[bld_config_memory_type]] | downstream | 0.27 |
| [[bld_instruction_retriever_config]] | sibling | 0.26 |
| [[bld_collaboration_memory_scope]] | downstream | 0.25 |
