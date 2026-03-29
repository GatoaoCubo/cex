---
kind: architecture
id: bld_architecture_output_validator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of output_validator — inventory, dependencies, and architectural position
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
