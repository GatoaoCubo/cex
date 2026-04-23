---
id: p10_lr_output_validator_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "output_validator artifacts require concrete parameter values with rationale. Placeholder values cause downstream failures."
pattern: "Define all parameters with concrete values and rationale. Validate against SCHEMA.md. Keep body under 2048 bytes."
evidence: "Pattern extracted from Guardrails Guard, Instructor Validator, LangChain OutputFixingParser, NeMo Guardrails, Pydantic BaseModel documentation and production usage."
confidence: 0.7
outcome: SUCCESS
domain: output_validator
tags: [output-validator, P05, type-builder]
tldr: "Concrete values with rationale. Validate against schema. Stay under 2048 bytes."
impact_score: 7.5
decay_rate: 0.05
agent_group: edison
keywords: [output validator, schema validation, regex check, llm-as-judge, fix-and-retry]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Output Validator"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_output_validator
  - p10_lr_retriever_config_builder
  - p10_lr_constraint_spec_builder
  - p10_lr_chunk_strategy_builder
  - p10_lr_handoff_protocol_builder
  - p03_sp_output_validator_builder
  - p10_lr_prompt_version_builder
  - bld_instruction_output_validator
  - output-validator-builder
  - p10_lr_memory_scope_builder
---
## Summary
Output validator — checks and corrective actions applied to LLM output AFTER generation. The difference between a useful output_validator and a useless one is concrete values
with rationale versus placeholder text.
## Pattern
**Concrete parameters with rationale.**
Every parameter must have: name, value, and why that value was chosen.
Required body sections: Overview, Checks, Failure Actions, Integration.
Body budget: 2048 bytes max.
## Anti-Pattern
1. No on_fail action: Validation detects error but pipeline continues with bad output
2. Infinite retry: Fix-and-retry without max attempts loops forever on unfixable errors
3. Validator too strict: Rejects acceptable outputs, wastes tokens on unnecessary retries
4. No error context in retry: Retry prompt doesn't explain what failed — LLM repeats same mistake
## Context
The 2048-byte body limit keeps output_validator artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.

## Metadata

```yaml
id: p10_lr_output_validator_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-output-validator-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | output_validator |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_output_validator]] | upstream | 0.51 |
| [[p10_lr_retriever_config_builder]] | sibling | 0.41 |
| [[p10_lr_constraint_spec_builder]] | sibling | 0.41 |
| [[p10_lr_chunk_strategy_builder]] | sibling | 0.41 |
| [[p10_lr_handoff_protocol_builder]] | sibling | 0.40 |
| [[p03_sp_output_validator_builder]] | upstream | 0.40 |
| [[p10_lr_prompt_version_builder]] | sibling | 0.38 |
| [[bld_instruction_output_validator]] | upstream | 0.38 |
| [[output-validator-builder]] | upstream | 0.38 |
| [[p10_lr_memory_scope_builder]] | sibling | 0.37 |
