---
kind: knowledge_card
id: bld_knowledge_card_output_validator
pillar: P05
llm_function: INJECT
purpose: Domain knowledge for output_validator production
sources: Guardrails AI validators, Instructor retry/validation, LangChain output parsers, output fixing patterns, retry-with-feedback loops
quality: 9.0
title: "Knowledge Card Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p10_lr_output_validator_builder
  - output-validator-builder
  - p01_kc_output_validator
  - p01_kc_validation_schema
  - bld_knowledge_card_constraint_spec
  - bld_instruction_output_validator
  - p01_kc_llm_output_parsing_validation
  - p01_kc_self_healing
  - bld_examples_output_validator
  - p03_sp_output_validator_builder
---

# Domain Knowledge: output_validator
## Executive Summary
Output validator — checks and corrective actions applied to LLM output AFTER generation. Produced as P05 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P05 |
| llm_function | GOVERN |
| Max bytes | 2048 |
| Density min | 0.85 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Schema validation | Validate output matches JSON/Pydantic schema | Structured data extraction, API responses |
| Regex check | Verify output matches expected pattern | IDs, codes, formatted strings |
| LLM-as-judge | Second LLM call evaluates output quality | Creative content, nuanced validation |
| Fix-and-retry | On failure, inject error into prompt and regenerate | Self-healing pipelines, auto-correction |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No on_fail action | Validation detects error but pipeline continues with bad output |
| Infinite retry | Fix-and-retry without max attempts loops forever on unfixable errors |
| Validator too strict | Rejects acceptable outputs, wastes tokens on unnecessary retries |
| No error context in retry | Retry prompt doesn't explain what failed — LLM repeats same mistake |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p05_oval_[a-z][a-z0-9_]+$`
## References
- Guardrails Guard, Instructor Validator, LangChain OutputFixingParser, NeMo Guardrails, Pydantic BaseModel
- Guardrails AI validators, Instructor retry/validation, LangChain output parsers, output fixing patterns, retry-with-feedback loops

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_output_validator_builder]] | downstream | 0.50 |
| [[output-validator-builder]] | related | 0.34 |
| [[p01_kc_output_validator]] | sibling | 0.32 |
| [[p01_kc_validation_schema]] | sibling | 0.32 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.30 |
| [[bld_instruction_output_validator]] | upstream | 0.30 |
| [[p01_kc_llm_output_parsing_validation]] | sibling | 0.30 |
| [[p01_kc_self_healing]] | sibling | 0.30 |
| [[bld_examples_output_validator]] | downstream | 0.30 |
| [[p03_sp_output_validator_builder]] | related | 0.29 |
