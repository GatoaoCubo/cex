---
id: p10_lr_constraint_spec_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "constraint_spec artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from Outlines Guide, LMQL where-clause, Guidance select/gen, Instructor response_model, LangChain StructuredOutputParser documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: constraint_spec
tags: [constraint-spec, P03, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [constraint spec, regex, enum/choice, json schema, grammar (cfg)]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Constraint Spec"
density_score: 0.90
llm_function: INJECT
related:
  - constraint-spec-builder
  - bld_collaboration_constraint_spec
  - bld_knowledge_card_constraint_spec
  - p03_sp_constraint_spec_builder
  - bld_examples_constraint_spec
  - bld_instruction_constraint_spec
  - bld_architecture_constraint_spec
  - p10_lr_output_validator_builder
  - p10_lr_retriever_config_builder
  - p10_lr_handoff_protocol_builder
---
## Summary
Constraint spec — rules that govern the LLM decoder during generation (grammar, regex, enum, schema). The difference between a useful constraint_spec and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Constraint Definition, Provider Compatibility, Integration.
Body budget: 2048 bytes max.
## Anti-Pattern
1. Constraint too strict: Rejects valid outputs, LLM loops or fails to generate
2. No fallback: Hard constraint failure crashes pipeline instead of graceful degrade
3. Provider-specific syntax: Constraint only works on one provider, not portable
4. Constraint in prompt only: Natural language constraints are soft — LLM may ignore them
## Context
The 2048-byte body limit keeps constraint_spec artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_constraint_spec_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-constraint-spec-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | constraint_spec |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[constraint-spec-builder]] | upstream | 0.52 |
| [[bld_collaboration_constraint_spec]] | downstream | 0.48 |
| [[bld_knowledge_card_constraint_spec]] | upstream | 0.48 |
| [[p03_sp_constraint_spec_builder]] | upstream | 0.46 |
| [[bld_examples_constraint_spec]] | upstream | 0.46 |
| [[bld_instruction_constraint_spec]] | upstream | 0.45 |
| [[bld_architecture_constraint_spec]] | upstream | 0.43 |
| [[p10_lr_output_validator_builder]] | sibling | 0.42 |
| [[p10_lr_retriever_config_builder]] | sibling | 0.41 |
| [[p10_lr_handoff_protocol_builder]] | sibling | 0.38 |
