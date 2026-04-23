---
kind: architecture
id: bld_architecture_output_validator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of output_validator — inventory, dependencies, and architectural position
quality: 9.2
title: "Architecture Output Validator"
version: "1.0.0"
author: n03_builder
tags: [output_validator, builder, examples]
tldr: "Golden and anti-examples for output validator construction, demonstrating ideal structure and common pitfalls."
domain: "output validator construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_output_validator_builder
  - bld_architecture_constraint_spec
  - output-validator-builder
  - bld_output_template_output_validator
  - p01_kc_output_validator
  - p10_lr_output_validator_builder
  - bld_instruction_output_validator
  - bld_examples_output_validator
  - constraint-spec-builder
  - p03_sp_constraint_spec_builder
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| checks | List of validation checks to apply | output_validator | required |
| on_fail | Action on validation failure (retry, fix, reject, warn) | output_validator | required |
| retry_count | Max retry attempts before hard fail | output_validator | optional |
| fix_prompt | Prompt template for fix-and-retry correction | output_validator | optional |
| constraint_spec | Decode-time constraint (first line of defense) | P03 | upstream |
| validation_schema | Schema definition referenced by checks | P06 | external |
| quality_gate | Scoring rubric applied after validation passes | P11 | downstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| checks | output_validator | produces | List of validation checks to apply |
| on_fail | output_validator | produces | Action on validation failure (retry, fix, reject, warn) |
| retry_count | output_validator | produces | Max retry attempts before hard fail |
| fix_prompt | output_validator | produces | Prompt template for fix-and-retry correction |
| constraint_spec | P03 | depends | Decode-time constraint (first line of defense) |
| validation_schema | P06 | depends | Schema definition referenced by checks |
| quality_gate | P11 | depends | Scoring rubric applied after validation passes |
## Boundary Table
| output_validator IS | output_validator IS NOT |
|-------------|----------------|
| Output validator — checks and corrective actions applied to LLM output AFTER generation | validation_schema (P06 |
| Not validation_schema | validation_schema (P06 |
| Not type/schema definition) | type/schema definition) |
| Not quality_gate | quality_gate (P11 |
| Not scoring rubric) | scoring rubric) |
| Not constraint_spec | constraint_spec (P03 |
| Not decode-time constraint) | decode-time constraint) |
| Not guardrail | guardrail (P11 |
| Not safety filter) | safety filter) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | checks, on_fail | Define the artifact's core parameters |
| optional | retry_count, fix_prompt | Extend with recommended fields |
| external | constraint_spec, validation_schema, quality_gate | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_output_validator
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-output-validator.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_output_validator_builder]] | upstream | 0.55 |
| [[bld_architecture_constraint_spec]] | sibling | 0.45 |
| [[output-validator-builder]] | upstream | 0.43 |
| [[bld_output_template_output_validator]] | upstream | 0.40 |
| [[p01_kc_output_validator]] | upstream | 0.38 |
| [[p10_lr_output_validator_builder]] | downstream | 0.37 |
| [[bld_instruction_output_validator]] | upstream | 0.36 |
| [[bld_examples_output_validator]] | upstream | 0.33 |
| [[constraint-spec-builder]] | upstream | 0.32 |
| [[p03_sp_constraint_spec_builder]] | upstream | 0.31 |
