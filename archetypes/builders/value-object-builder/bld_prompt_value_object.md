---
quality: 7.8
id: bld_instruction_value_object
kind: instruction
pillar: P06
title: "Value Object Builder -- Instruction"
version: 1.0.0
quality: 7.3
tags: [builder, value_object, instruction]
llm_function: REASON
author: builder
tldr: "Value Object schema: prompt template with variables, tone, and generation strategy"
density_score: 0.83
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_input_schema
  - bld_instruction_golden_test
  - bld_instruction_action_prompt
  - bld_instruction_instruction
  - bld_instruction_entity_memory
  - bld_instruction_constraint_spec
  - bld_instruction_context_doc
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
---
# Instructions: How to Produce a value_object
## Phase 1: RESEARCH
1. Identify the domain concept -- what real-world attribute needs typed representation?
2. Verify no identity needed: two instances with same attributes should be interchangeable.
3. Enumerate attributes: what fields make up this value? What are their types and constraints?
4. Define validation rules: what makes an instance valid vs invalid?
5. Define allowed transformations: what operations produce a new valid instance?
6. Identify context: which aggregate_root or entity uses this value_object?
## Phase 2: COMPOSE
1. Read bld_schema_value_object.md -- source of truth for required fields
2. Fill frontmatter: id pattern p06_vo_{slug}, kind: value_object, quality: null
3. Write Attributes section: field name, type, constraint for each attribute
4. Write Equality section: structural equality contract (all attributes equal = value equal)
5. Write Validation section: invariants for the value (invalid state examples)
6. Write Transformations section: operations that produce new instances (never mutate)
7. Write Usage section: which aggregates or entities use this value_object
## Phase 3: VALIDATE
1. HARD gates: id matches `p06_vo_[a-z][a-z0-9_]+`, kind == value_object, quality == null
2. Value has >= 1 attribute with type and constraint
3. Equality is structural (not by reference)
4. No mutation methods -- only transformations returning new instances
5. Invalid state examples present


## Prompt Construction Checklist

- Verify prompt follows target kind's instruction template
- Validate variable placeholders use standard naming convention
- Cross-reference with chain dependencies for context completeness
- Test prompt with sample input before publishing

## Prompt Pattern

```yaml
# Prompt validation
template_match: true
variables_valid: true
chain_refs_checked: true
sample_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_prompt_optimizer.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | sibling | 0.33 |
| [[bld_instruction_golden_test]] | sibling | 0.32 |
| [[bld_instruction_action_prompt]] | sibling | 0.31 |
| [[bld_instruction_instruction]] | sibling | 0.31 |
| [[bld_instruction_entity_memory]] | sibling | 0.28 |
| [[bld_instruction_constraint_spec]] | sibling | 0.28 |
| [[bld_instruction_context_doc]] | sibling | 0.28 |
| [[bld_instruction_output_validator]] | sibling | 0.27 |
| [[bld_instruction_memory_scope]] | sibling | 0.27 |
| [[bld_instruction_retriever_config]] | sibling | 0.26 |
