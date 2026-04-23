---
kind: architecture
id: bld_architecture_constraint_spec
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of constraint_spec — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - constraint-spec-builder
  - bld_examples_constraint_spec
  - p03_sp_constraint_spec_builder
  - p10_lr_constraint_spec_builder
  - bld_collaboration_constraint_spec
  - bld_instruction_constraint_spec
  - bld_architecture_output_validator
  - bld_output_template_constraint_spec
  - bld_tools_constraint_spec
  - bld_knowledge_card_constraint_spec
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| constraint_type | Type of constraint (regex, enum, json_schema, grammar) | constraint_spec | required |
| pattern | The constraint definition (regex string, enum list, JSON schema, CFG) | constraint_spec | required |
| provider_compat | Which providers support this constraint natively | constraint_spec | optional |
| fallback | Behavior when provider doesn't support native constraint | constraint_spec | optional |
| prompt_template | Prompt that uses this constraint | P03 | consumer |
| output_validator | Post-generation validator as safety net | P05 | downstream |
## Dependency Graph
| From | To | Type | Data |
|------|----|------|------|
| constraint_type | constraint_spec | produces | Type of constraint (regex, enum, json_schema, grammar) |
| pattern | constraint_spec | produces | The constraint definition (regex string, enum list, JSON schema, CFG) |
| provider_compat | constraint_spec | produces | Which providers support this constraint natively |
| fallback | constraint_spec | produces | Behavior when provider doesn't support native constraint |
| prompt_template | P03 | depends | Prompt that uses this constraint |
| output_validator | P05 | depends | Post-generation validator as safety net |
## Boundary Table
| constraint_spec IS | constraint_spec IS NOT |
|-------------|----------------|
| Constraint spec — rules that govern the LLM decoder during generation (grammar, regex, enum, schema) | validation_schema (P06 |
| Not validation_schema | validation_schema (P06 |
| Not post-generation validation) | post-generation validation) |
| Not quality_gate | quality_gate (P11 |
| Not scoring) | scoring) |
| Not guardrail | guardrail (P11 |
| Not safety filter) | safety filter) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| spec | constraint_type, pattern | Define the artifact's core parameters |
| optional | provider_compat, fallback | Extend with recommended fields |
| external | prompt_template, output_validator | Upstream/downstream connections |

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_architecture_constraint_spec
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-architecture-constraint-spec.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[constraint-spec-builder]] | upstream | 0.61 |
| [[bld_examples_constraint_spec]] | upstream | 0.60 |
| [[p03_sp_constraint_spec_builder]] | upstream | 0.59 |
| [[p10_lr_constraint_spec_builder]] | downstream | 0.53 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.48 |
| [[bld_instruction_constraint_spec]] | upstream | 0.47 |
| [[bld_architecture_output_validator]] | sibling | 0.47 |
| [[bld_output_template_constraint_spec]] | upstream | 0.46 |
| [[bld_tools_constraint_spec]] | upstream | 0.42 |
| [[bld_knowledge_card_constraint_spec]] | upstream | 0.40 |
