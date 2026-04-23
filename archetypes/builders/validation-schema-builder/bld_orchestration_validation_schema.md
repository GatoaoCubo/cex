---
kind: collaboration
id: bld_collaboration_validation_schema
pillar: P06
llm_function: COLLABORATE
purpose: How validation-schema-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_validator
  - bld_collaboration_response_format
  - bld_collaboration_type_def
  - bld_collaboration_output_validator
  - validation-schema-builder
  - bld_collaboration_builder
  - bld_collaboration_quality_gate
  - bld_collaboration_golden_test
  - bld_collaboration_input_schema
  - bld_architecture_kind
---

# Collaboration: validation-schema-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what formal contract must the system enforce on generated output?"
I produce post-generation validation contracts applied automatically by the system — the LLM never sees them. I do NOT write format instructions for the LLM (response-format-builder), individual pass/fail rules (validator-builder), or input contracts (input-schema-builder).
## Crew Compositions
### Crew: "Output Quality Pipeline"
```
  1. response-format-builder -> "tells the LLM how to structure its output"
  2. validation-schema-builder -> "system validates the generated output against field contracts"
  3. quality-gate-builder -> "enforces quality score threshold after schema validation passes"
```
### Crew: "New Kind Onboarding"
```
  1. type-def-builder -> "defines domain types and constraints for each output field"
  2. validation-schema-builder -> "builds the post-generation contract: fields, types, on_failure"
  3. validator-builder -> "adds individual pass/fail rules that complement schema-level enforcement"
```
## Handoff Protocol
### I Receive
- seeds: target artifact kind, required fields list, failure strategy (reject/warn/auto_fix)
- optional: type_def references, regex patterns, enum values, existing _schema.yaml of target kind
### I Produce
- validation_schema artifact (YAML, frontmatter 20 fields, max 120 lines)
- committed to: `cex/P06_schema/examples/p06_vs_{scope}.yaml`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- type-def-builder: field type vocabulary must exist before writing typed field constraints in the schema
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| validator-builder | may derive individual rules from fields declared in the validation_schema |
| quality-gate-builder | uses schema pass as a prerequisite before applying quality scoring |
| unit-eval-builder | test assertions verify that generated outputs satisfy the validation_schema contract |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_validator]] | sibling | 0.48 |
| [[bld_collaboration_response_format]] | sibling | 0.46 |
| [[bld_collaboration_type_def]] | sibling | 0.44 |
| [[bld_collaboration_output_validator]] | sibling | 0.42 |
| [[validation-schema-builder]] | related | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_quality_gate]] | sibling | 0.39 |
| [[bld_collaboration_golden_test]] | sibling | 0.38 |
| [[bld_collaboration_input_schema]] | sibling | 0.37 |
| [[bld_architecture_kind]] | downstream | 0.37 |
