---
id: p06_gram_json_object
kind: grammar
8f: F1_constrain
pillar: P06
description: "BNF grammar constraint for generating valid JSON objects during LLM decoding"
version: 1.0.0
created: 2026-03-25
author: builder_agent
quality: 9.0
tags: [grammar, constraint, json, BNF, structured-generation]
updated: "2026-04-07"
domain: "schema"
title: "Input Schema Json Object"
density_score: 0.92
tldr: "Defines grammar for input schema json object, with validation gates and integration points."
related:
  - p01_kc_cex_function_constrain
  - bld_knowledge_card_constraint_spec
  - p01_kc_cex_lp06_schema
  - bld_output_template_function_def
  - p01_kc_response_format
  - bld_architecture_response_format
  - response-format-builder
  - p01_kc_validation_schema
  - p10_lr_constraint_spec_builder
  - bld_schema_type_def
---

# Grammar: JSON Object

## Purpose
Constrains LLM token generation at the DECODER level to produce only valid JSON. Unlike response_format (P05) which is a text instruction the LLM may ignore, a grammar physically prevents invalid tokens from being sampled.

## BNF Definition
```bnf
root   ::= object
object ::= "{" ws members ws "}"
members::= pair ("," ws pair)*
pair   ::= string ws ":" ws value
value  ::= string | number | object | array | "true" | "false" | "null"
array  ::= "[" ws (value ("," ws value)*)? ws "]"
string ::= '"' [^"\]* '"'
number ::= "-"? [0-9]+ ("." [0-9]+)?
ws     ::= [ \t\n]*
```

## Frameworks that use this
1. **Guidance** (Microsoft): grammar-based constrained generation
2. **Outlines** (dottxt): FSM-compiled regex/JSON schemas
3. **llama.cpp**: GBNF grammars for local models
4. **LMQL**: `where` clauses compile to token masks

## Difference from response_format (P05)
| | response_format (P05) | grammar (P06) |
|---|---|---|
| Mechanism | Text instruction in prompt | Token mask during decoding |
| Guarantee | LLM may ignore | Physically enforced |
| Flexibility | Works with any API | Requires grammar-aware runtime |
| Function | CONSTRAIN (soft) | CONSTRAIN (hard) |

## Properties

| Property | Value |
|----------|-------|
| Kind | `grammar` |
| Pillar | P06 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_constrain]] | upstream | 0.34 |
| [[bld_knowledge_card_constraint_spec]] | upstream | 0.32 |
| [[p01_kc_cex_lp06_schema]] | upstream | 0.26 |
| [[bld_output_template_function_def]] | upstream | 0.25 |
| [[p01_kc_response_format]] | upstream | 0.23 |
| [[bld_architecture_response_format]] | downstream | 0.22 |
| [[response-format-builder]] | upstream | 0.22 |
| [[p01_kc_validation_schema]] | related | 0.20 |
| [[p10_lr_constraint_spec_builder]] | downstream | 0.20 |
| [[bld_schema_type_def]] | related | 0.20 |
