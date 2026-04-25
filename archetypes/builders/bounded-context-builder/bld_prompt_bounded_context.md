---
quality: 7.8
id: bld_instruction_bounded_context
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for bounded_context
version: 1.0.0
quality: 7.3
tags: [bounded_context, builder, instruction]
title: "Instruction Bounded Context Builder"
author: builder
tldr: "Step-by-step production process for bounded_context"
density_score: 0.84
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_context_doc
  - bld_instruction_kind
  - bld_instruction_golden_test
  - bld_instruction_instruction
  - bld_knowledge_card_context_doc
  - bld_instruction_retriever_config
  - bld_instruction_output_validator
  - bld_instruction_chunk_strategy
  - bld_instruction_memory_scope
  - bld_instruction_input_schema
---
# Instructions: How to Produce a bounded_context
## Phase 1: SCOPE
1. Name the bounded context (noun phrase from domain language, not tech terms)
2. Write the scope statement: what domain model applies HERE (not in other BCs)
3. Identify the team/squad that owns this context
4. List the key aggregates and their relationships within this BC
5. Identify neighboring BCs and their integration patterns
## Phase 2: COMPOSE
1. Read bld_schema_bounded_context.md for required fields
2. Set id: bc_{context_name} (snake_case, domain language)
3. Set domain_vocabulary reference (dv_{context}_vocabulary.md)
4. Document integration patterns with neighboring contexts:
   - ACL (Anti-Corruption Layer): protecting this BC from upstream model
   - OHS (Open Host Service): publishing a public API for consumers
   - CF (Conformist): adopting upstream model as-is
5. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates:
   - id follows pattern bc_{context}
   - kind == bounded_context
   - quality == null
   - scope_statement present (what model applies here)
   - team_owner present
   - >= 1 aggregate listed
2. SOFT gates:
   - domain_vocabulary reference present
   - integration patterns documented with rationale
   - upstream_contexts and downstream_contexts listed
   - key invariants stated (business rules that hold within this BC)


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
| [[bld_instruction_context_doc]] | sibling | 0.27 |
| [[bld_instruction_kind]] | sibling | 0.24 |
| [[bld_instruction_golden_test]] | sibling | 0.23 |
| [[bld_instruction_instruction]] | sibling | 0.21 |
| [[bld_knowledge_card_context_doc]] | upstream | 0.21 |
| [[bld_instruction_retriever_config]] | sibling | 0.20 |
| [[bld_instruction_output_validator]] | sibling | 0.20 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.20 |
| [[bld_instruction_memory_scope]] | sibling | 0.20 |
| [[bld_instruction_input_schema]] | sibling | 0.19 |
