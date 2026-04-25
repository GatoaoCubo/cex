---
id: p01_kc_cex_lp05_output
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP05 Output — Delivery Formats Between LLM and System"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp05, output, response-format, parser, formatter]
tldr: "P05 defines HOW the LLM delivers results via 4 types: response_format, parser, formatter and naming_rule"
when_to_use: "Understand LLM delivery formats and the boundary between generation (P05) and validation (P06)"
keywords: [output, response-format, parser, formatter, naming-rule]
long_tails:
  - "How to define the response format of an LLM agent"
  - "What is the difference between response_format and validation_schema"
axioms:
  - "ALWAYS separate response format (P05) from validation (P06)"
  - "NEVER confuse parser (extracts) with formatter (transforms)"
linked_artifacts:
  primary: p01_kc_cex_lp06_schema
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/structured-output"
related:
  - bld_architecture_response_format
  - p01_kc_lp05_output
  - p01_kc_cex_lp06_schema
  - response-format-builder
  - bld_architecture_parser
  - parser-builder
  - p01_kc_validation_schema
  - p03_sp_response_format_builder
  - bld_knowledge_card_response_format
  - p03_ins_response_format
---

## Quick Reference

topic: P05 Output | scope: delivery formats | criticality: high
types: 4 | function: CONSTRAIN | layer: spec + runtime + governance

## Key Concepts

- P05 defines HOW the agent delivers, not WHAT it delivers
- response_format is injected into the prompt (LLM sees and follows)
- validation_schema P06 is post-generation (LLM does not see)
- parser extracts structured data from raw output
- formatter converts between formats (json, md, yaml)
- naming_rule governs nomenclature of generated artifacts
- Leanest LP in CEX: 4 types, all < 4096 bytes
- Dominant function: CONSTRAIN (format post-generation)
- response_format uses machine_format json (spec layer)
- parser uses machine_format yaml (runtime layer)
- formatter operates at the runtime layer (active conversion)
- naming_rule operates at the governance layer (standardization)
- P05 depends on P06: schemas define what P05 formats
- P05 is evaluated by P07: incorrect formats detected
- P05 is shaped by P02: identity defines tone and style
- Without response_format, LLM generates unpredictable format

## Phases

1. Define response_format in the agent prompt
2. LLM generates output following specified format
3. Parser extracts structured data from raw output
4. Formatter converts to downstream consumption format
5. Naming_rule ensures consistent nomenclature
6. P06 validation_schema validates the final result

## Golden Rules

- ALWAYS define response_format before calling the LLM
- NEVER validate within P05 (validation is P06)
- ALWAYS use parser for semi-structured output
- NEVER assume LLM follows format without instruction
- ALWAYS separate extraction (parser) from conversion (fmt)

## Comparison

| Aspect | P05 Output | P06 Schema |
|--------|-----------|------------|
| When it acts | Pre and post-generation | Post-generation |
| Visibility | LLM sees response_format | System applies, LLM does not see |
| Function | Format delivery | Validate contract |
| Failure mode | Malformed output | Contract violation |
| Type count | 4 (rf, parser, fmt, nr) | 7 (is, td, val, iface, vs, bp, gram) |

## Flow

```
[LLM] --response_format--> [raw output]
  |                            |
  v                            v
[P05: format hint]      [parser: extract]
                               |
                               v
                        [formatter: convert]
                               |
                               v
                        [P06: validate contract]
                               |
                               v
                        [downstream consumer]
```

## References

- source: https://docs.anthropic.com/en/docs/build-with-claude/structured-output
- source: https://platform.openai.com/docs/guides/structured-outputs
- related: p01_kc_cex_lp06_schema
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_response_format]] | downstream | 0.39 |
| [[p01_kc_lp05_output]] | sibling | 0.38 |
| [[p01_kc_cex_lp06_schema]] | sibling | 0.38 |
| [[response-format-builder]] | downstream | 0.34 |
| [[bld_architecture_parser]] | downstream | 0.33 |
| [[parser-builder]] | downstream | 0.32 |
| [[p01_kc_validation_schema]] | sibling | 0.31 |
| [[p03_sp_response_format_builder]] | downstream | 0.30 |
| [[bld_knowledge_card_response_format]] | sibling | 0.30 |
| [[p03_ins_response_format]] | downstream | 0.29 |
