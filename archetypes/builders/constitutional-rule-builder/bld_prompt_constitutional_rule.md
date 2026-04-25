---
quality: 7.8
id: bld_instruction_constitutional_rule
kind: instruction
pillar: P11
title: "Constitutional Rule Builder -- Instruction"
version: 1.0.0
quality: 7.3
tags: [builder, constitutional_rule, instruction]
llm_function: REASON
author: builder
tldr: "Constitutional Rule feedback: prompt template with variables, tone, and generation strategy"
density_score: 0.76
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_instruction_golden_test
  - bld_instruction_guardrail
  - bld_instruction_input_schema
  - bld_instruction_output_validator
  - bld_instruction_memory_scope
  - bld_instruction_retriever_config
  - p03_ins_law
  - bld_instruction_chunk_strategy
  - bld_instruction_instruction
  - bld_instruction_prompt_version
---
# Instructions: How to Produce a constitutional_rule
## Phase 1: RESEARCH
1. Identify the absolute prohibition: what behavior must NEVER occur under ANY circumstances?
2. Classify the constitutional basis: harm_prevention, honesty, autonomy_preservation, legality
3. Verify it is truly absolute: is there ANY legitimate scenario where this should be bypassed? If yes -> it is a guardrail, not a constitutional rule.
4. Define the violation test: how would a reviewer recognize that this rule was broken?
5. Write the rationale: why can this never have an exception?
6. Check existing constitutional_rules for overlap -- each rule should cover a distinct prohibition.
## Phase 2: COMPOSE
1. Read bld_schema_constitutional_rule.md -- source of truth for required fields
2. Fill frontmatter: id pattern p11_cr_{slug}, kind: constitutional_rule, quality: null
3. Write Principle section: one clear, concrete statement of the absolute prohibition
4. Write Basis section: which constitutional value this protects (harm/honesty/autonomy/legality)
5. Write Rationale section: why this has zero exceptions
6. Write Violation section: concrete examples of what breaking this rule looks like
7. Write Detection section: how a violation is identified
8. CONFIRM: bypass_policy must be "none" -- if you find yourself writing any bypass, downgrade to guardrail
## Phase 3: VALIDATE
1. HARD gates: id matches `p11_cr_[a-z][a-z0-9_]+`, kind == constitutional_rule, quality == null
2. bypass_policy == "none" (absolute)
3. Principle is a single clear prohibition, not a collection
4. At least 2 concrete violation examples
5. constitutional_basis is one of the valid enum values


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
| [[bld_instruction_golden_test]] | sibling | 0.32 |
| [[bld_instruction_guardrail]] | sibling | 0.32 |
| [[bld_instruction_input_schema]] | sibling | 0.31 |
| [[bld_instruction_output_validator]] | sibling | 0.29 |
| [[bld_instruction_memory_scope]] | sibling | 0.29 |
| [[bld_instruction_retriever_config]] | sibling | 0.29 |
| [[p03_ins_law]] | sibling | 0.28 |
| [[bld_instruction_chunk_strategy]] | sibling | 0.28 |
| [[bld_instruction_instruction]] | sibling | 0.28 |
| [[bld_instruction_prompt_version]] | sibling | 0.28 |
