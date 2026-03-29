---
kind: architecture
id: bld_architecture_constraint_spec
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of constraint_spec — inventory, dependencies, and architectural position
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
