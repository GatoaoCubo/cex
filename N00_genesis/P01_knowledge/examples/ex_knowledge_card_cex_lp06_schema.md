---
id: p01_kc_cex_lp06_schema
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP06 Schema — Data Contracts That Constrain LLM Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp06, schema, contracts, validation, grammar, blueprint]
tldr: "P06 defines 7 types of contract that constrain output: from input_schema to grammar (constraint on the decoder)"
when_to_use: "Understand data contracts in LLM systems and how soft CONSTRAIN becomes hard CONSTRAIN"
keywords: [schema, contracts, validation, grammar, blueprint, type-def]
long_tails:
  - "How to define data contracts between LLM agents"
  - "What is the difference between grammar and validator in CEX"
axioms:
  - "ALWAYS have input_schema before accepting data"
  - "NEVER confuse grammar (during generation) with validator (post)"
linked_artifacts:
  primary: p01_kc_cex_lp05_output
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://json-schema.org/understanding-json-schema"
related:
  - p01_kc_cex_lp05_output
  - p01_kc_cex_function_constrain
  - p06_gram_json_object
  - p01_kc_validation_schema
  - p01_kc_lp06_schema
  - validation-schema-builder
  - p01_kc_input_schema
  - bld_architecture_validation_schema
  - bld_knowledge_card_constraint_spec
  - bld_architecture_type_def
---

## Quick Reference

topic: P06 Schema | scope: data contracts | criticality: high
types: 7 | function: CONSTRAIN + GOVERN | layer: spec + governance

## Key Concepts

- P06 is where soft CONSTRAIN becomes hard CONSTRAIN
- input_schema defines required data at entry
- validation_schema validates post-generation output (system)
- type_def creates reusable custom types
- interface is a bilateral contract between agents
- artifact_blueprint is a meta-template (artifact shape)
- grammar restricts tokens DURING generation (at the decoder)
- Unifies concepts of BNF, EBNF, FSM and WHERE clauses
- No popular framework has these 7 types together
- Guidance uses BNF/EBNF for character-by-character control
- Outlines uses FSMs and CFGs for formal constraint
- LMQL uses declarative WHERE clauses post-generation
- P06 is consumed by P05: schemas define what to format
- P06 is validated by P07: schema conformance tested
- P06 is informed by P01: schemas reflect the domain
- input_schema max 3072 bytes (spec layer, core: true)
- grammar max 3072 bytes (spec layer, core: false)

## Phases

1. Define input_schema with required fields
2. Create type_defs for domain custom types
3. Establish interfaces between cooperating agents
4. Write artifact_blueprints for recurring artifacts
5. Configure validation_schema for post-generation
6. Apply grammar when precision > 99% is critical

## Golden Rules

- ALWAYS validate input before processing (input_schema)
- NEVER confuse response_format P05 with validation_schema
- ALWAYS use grammar for critical deterministic output
- NEVER self-assign quality in artifact_blueprint
- ALWAYS document the boundary of each type (prevents overlap)

## Comparison

| Mechanism | When It Acts | Who Applies | Precision |
|-----------|-------------|-------------|-----------|
| response_format P05 | Pre-generation | LLM interprets | ~85% |
| validation_schema | Post-generation | System validates | ~99% |
| grammar | During generation | Decoder constrains | ~100% |
| validator | Post-generation | Pipeline pass/fail | ~99% |

## Flow

```
[input] --input_schema--> [validated input]
                              |
                              v
              [LLM + grammar] --> [constrained output]
                              |
                              v
              [validation_schema] --> pass/fail
                              |
                              v
              [interface] --> [next agent receives]
                              |
                              v
              [type_def checks] --> [type-safe system]
```

## References

- source: https://json-schema.org/understanding-json-schema
- source: https://github.com/guidance-ai/guidance
- related: p01_kc_cex_lp05_output
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp05_output]] | sibling | 0.42 |
| [[p01_kc_cex_function_constrain]] | sibling | 0.40 |
| [[p06_gram_json_object]] | downstream | 0.31 |
| [[p01_kc_validation_schema]] | sibling | 0.30 |
| [[p01_kc_lp06_schema]] | sibling | 0.29 |
| [[validation-schema-builder]] | downstream | 0.28 |
| [[p01_kc_input_schema]] | sibling | 0.27 |
| [[bld_architecture_validation_schema]] | downstream | 0.25 |
| [[bld_knowledge_card_constraint_spec]] | sibling | 0.25 |
| [[bld_architecture_type_def]] | downstream | 0.25 |
