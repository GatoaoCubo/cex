---
id: p10_lr_output_validator_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
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
satellite: edison
keywords: [output validator, schema validation, regex check, llm-as-judge, fix-and-retry]
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
- No on_fail action: Validation detects error but pipeline continues with bad output
- Infinite retry: Fix-and-retry without max attempts loops forever on unfixable errors
- Validator too strict: Rejects acceptable outputs, wastes tokens on unnecessary retries
- No error context in retry: Retry prompt doesn't explain what failed — LLM repeats same mistake
## Context
The 2048-byte body limit keeps output_validator artifacts focused. Fill required fields first,
then add recommended fields if space permits. Always set quality: null.
