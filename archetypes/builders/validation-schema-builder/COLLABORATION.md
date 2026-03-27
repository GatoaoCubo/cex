---
pillar: P12
llm_function: COLLABORATE
purpose: How validation-schema-builder works in crews
---

# Collaboration: validation-schema-builder

## My Role
I define STRUCTURAL CONTRACTS that the system enforces after generation.
I do not tell the LLM how to format output (response-format-builder).
I do not define individual pass/fail rules (validator-builder).

## Crew: "Output Quality Pipeline"
```
  1. response-format-builder    -> tells LLM how to structure output
  2. validation-schema-builder  -> system validates generated output
  3. quality-gate-builder       -> enforces quality score threshold
```

## Crew: "New Kind Onboarding"
```
  1. input-schema-builder [PLANNED] -> defines what the kind accepts
  2. response-format-builder        -> defines LLM output format
  3. validation-schema-builder      -> defines post-generation checks
  4. validator-builder              -> defines individual field rules
```

## Handoff Protocol
### I Receive
- seeds: target_kind, critical fields, failure strategy
- optional: existing _schema.yaml of target kind, validator references

### I Produce
- validation_schema artifact in P06_schema/examples/
- committed to: cex/P06_schema/examples/p06_vs_{scope}.yaml

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- input-schema-builder [PLANNED]: provides field definitions for target kind (optional)

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validator-builder | May derive individual rules from schema fields |
| quality-gate-builder | Uses schema pass as prerequisite for quality scoring |
