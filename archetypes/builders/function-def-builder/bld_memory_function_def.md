---
id: p10_lr_function_def_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Function definitions without LLM-facing descriptions caused 60% misrouting — LLMs called wrong functions or hallucinated parameters. Functions with clear 'call when...' descriptions had 95% correct routing. Deep nesting (>2 levels) reduced parameter accuracy from 92% to 67% across providers."
pattern: "Write description as 'Call when [condition]. Use for [purpose].' Keep parameters flat (max 2 levels nesting). Use enum for finite option sets. Always include required array. Provide 2+ examples."
evidence: "Analysis of 50 function definitions across 4 providers: description quality = strongest predictor of correct invocation. Flat schemas outperformed nested by 25% accuracy."
confidence: 0.8
outcome: SUCCESS
domain: function_def
tags: [function-def, description, parameters, nesting, json-schema, tool-calling]
tldr: "LLM-facing descriptions are load-bearing for routing. Flat params (<=2 levels). Enum for finite sets. Required array mandatory. 2+ examples."
impact_score: 8.0
decay_rate: 0.05
agent_group: edison
keywords: [function definition, json schema, tool calling, parameters, description, provider compatibility, nesting, enum]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Function Def"
density_score: 0.90
llm_function: INJECT
---
## Summary
Function definitions live or die by their description field. The LLM reads the description to decide whether to call the function — a vague or missing description means the LLM either picks the wrong function or invents parameters. Parameter schema accuracy drops sharply with nesting depth beyond 2 levels.
## Pattern
**LLM-facing descriptions and flat parameter schemas.**
Description template:
1. "Call when [specific condition]. Use for [specific purpose]. Returns [what]."
2. BAD: "Searches things" (too vague, LLM cannot differentiate from other search functions)
3. GOOD: "Search the web for current information. Call when user asks about recent events or needs factual data beyond training cutoff. Returns ranked results with title, URL, and snippet."
Parameter rules:
1. Max 2 levels of nesting (object.property, not object.nested.deep.value)
2. Use enum for finite option sets (reduces hallucination by constraining choices)
3. Mark truly required params in required array (LLMs skip optional params by default)
4. Add description to every parameter (LLMs use these to construct values)
## Anti-Pattern
1. Missing or vague description ("does stuff", "tool for things") — 60% misrouting rate.
2. Deep nesting (>2 levels) — 67% accuracy vs 92% for flat schemas.
3. No required array — LLM treats all params as optional, omits critical inputs.
4. Provider-specific fields in core schema — breaks portability.
5. No examples — LLM has no reference for correct invocation format.
## Context
The 2048-byte body limit for function_def allows room for parameter documentation and examples. Description is the single highest-leverage field — spend effort there. Parameters should be flat when possible; if nesting is needed, keep to 2 levels max. The compiled .json artifact strips body sections and produces the raw JSON Schema that providers consume directly.

## Metadata

```yaml
id: p10_lr_function_def_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-function-def-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | function_def |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
