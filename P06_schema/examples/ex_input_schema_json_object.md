---
id: p06_gram_json_object
kind: grammar
pillar: P06
description: "BNF grammar constraint for generating valid JSON objects during LLM decoding"
version: 1.0.0
created: 2026-03-25
author: edison
quality: 9.0
tags: [grammar, constraint, json, BNF, structured-generation]
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
- **Guidance** (Microsoft): grammar-based constrained generation
- **Outlines** (dottxt): FSM-compiled regex/JSON schemas
- **llama.cpp**: GBNF grammars for local models
- **LMQL**: `where` clauses compile to token masks

## Difference from response_format (P05)
| | response_format (P05) | grammar (P06) |
|---|---|---|
| Mechanism | Text instruction in prompt | Token mask during decoding |
| Guarantee | LLM may ignore | Physically enforced |
| Flexibility | Works with any API | Requires grammar-aware runtime |
| Function | CONSTRAIN (soft) | CONSTRAIN (hard) |
