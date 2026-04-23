---
kind: knowledge_card
id: bld_knowledge_card_constraint_spec
pillar: P03
llm_function: INJECT
purpose: Domain knowledge for constraint_spec production
sources: Outlines structured generation, LMQL constrained decoding, Guidance grammar-based generation, Instructor Pydantic validation, JSON mode (OpenAI/Anthropic)
quality: 9.0
title: "Knowledge Card Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_constraint_spec_builder
  - constraint-spec-builder
  - p03_sp_constraint_spec_builder
  - bld_examples_constraint_spec
  - bld_knowledge_card_output_validator
  - bld_instruction_constraint_spec
  - bld_architecture_constraint_spec
  - p01_kc_constraint_spec
  - bld_collaboration_constraint_spec
  - p06_gram_json_object
---

# Domain Knowledge: constraint_spec
## Executive Summary
Constraint spec — rules that govern the LLM decoder during generation (grammar, regex, enum, schema). Produced as P03 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P03 |
| llm_function | CONSTRAIN |
| Max bytes | 2048 |
| Density min | 0.85 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Regex | Constrain output to match regex pattern | IDs, codes, formatted strings |
| Enum/choice | Force selection from predefined values | Categories, status fields, yes/no |
| JSON schema | Constrain output to valid JSON matching schema | Structured data extraction |
| Grammar (CFG) | Context-free grammar constraining token sequence | Complex structured formats, DSLs |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Constraint too strict | Rejects valid outputs, LLM loops or fails to generate |
| No fallback | Hard constraint failure crashes pipeline instead of graceful degrade |
| Provider-specific syntax | Constraint only works on one provider, not portable |
| Constraint in prompt only | Natural language constraints are soft — LLM may ignore them |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p03_constraint_[a-z][a-z0-9_]+$`
## References
- Outlines Guide, LMQL where-clause, Guidance select/gen, Instructor response_model, LangChain StructuredOutputParser
- Outlines structured generation, LMQL constrained decoding, Guidance grammar-based generation, Instructor Pydantic validation, JSON mode (OpenAI/Anthropic)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_constraint_spec_builder]] | downstream | 0.52 |
| [[constraint-spec-builder]] | related | 0.39 |
| [[p03_sp_constraint_spec_builder]] | related | 0.39 |
| [[bld_examples_constraint_spec]] | downstream | 0.37 |
| [[bld_knowledge_card_output_validator]] | sibling | 0.36 |
| [[bld_instruction_constraint_spec]] | related | 0.35 |
| [[bld_architecture_constraint_spec]] | downstream | 0.33 |
| [[p01_kc_constraint_spec]] | sibling | 0.33 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.32 |
| [[p06_gram_json_object]] | downstream | 0.29 |
