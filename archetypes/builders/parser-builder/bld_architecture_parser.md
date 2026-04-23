---
kind: architecture
id: bld_architecture_parser
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of parser — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Parser"
version: "1.0.0"
author: n03_builder
tags: [parser, builder, examples]
tldr: "Golden and anti-examples for parser construction, demonstrating ideal structure and common pitfalls."
domain: "parser construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - parser-builder
  - p11_qg_parser
  - bld_collaboration_parser
  - p01_kc_parser
  - p03_sp_parser_builder
  - bld_architecture_response_format
  - bld_schema_parser
  - bld_memory_parser
  - p03_ins_parser
  - bld_examples_parser
---

# Architecture: parser in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 14-field metadata header (id, kind, pillar, domain, input_format, etc.) | parser-builder | active |
| input_format_spec | Description of the raw input format (JSON, HTML, log, text) | author | active |
| extraction_rules | Ordered list of regex, JSON path, or CSS selector rules | author | active |
| normalization_pipeline | Steps to clean, transform, and standardize extracted values | author | active |
| error_handling | Fallback strategies when extraction rules fail to match | author | active |
| output_schema | Typed structure of the parsed result | author | active |
| test_vectors | Sample inputs with expected parsed outputs for validation | author | active |
## Dependency Graph
```
raw_output      --consumed_by-->  parser  --produces-->     structured_data
response_format --depends-->      parser  --consumed_by-->  agent
parser          --signals-->      parse_error
```
| From | To | Type | Data |
|------|----|------|------|
| raw_output (LLM/API) | parser | data_flow | unstructured text, JSON, HTML, or log input |
| parser | structured_data | produces | typed, normalized data ready for downstream use |
| parser | agent (P02) | consumes | agent uses parser to extract data from tool results |
| response_format (P05) | parser | dependency | expected output format guides extraction rules |
| parser | parse_error (P12) | signals | emitted when extraction fails after fallback attempts |
| validation_schema (P06) | parser | dependency | validates parsed output matches expected contract |
## Boundary Table
| parser IS | parser IS NOT |
|-----------|---------------|
| An extractor of structured data from raw output | A format converter between structured formats (formatter P05) |
| Defined by regex, JSON path, or CSS selector rules | A pass/fail content check (validator P06) |
| Includes normalization and error handling | A naming convention enforcer (naming_rule P05) |
| Produces typed structured data from untyped input | A response format injected into LLM prompts (response_format P05) |
| Operates post-generation on actual output | A pre-generation instruction to the LLM |
| Handles malformed input with fallback extraction | A hard failure on unexpected input |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | raw_output, input_format_spec | Define what raw data the parser receives |
| Extraction | extraction_rules | Apply patterns to extract target values |
| Normalization | normalization_pipeline | Clean, transform, and standardize extracted data |
| Validation | output_schema, test_vectors | Verify parsed result matches expected structure |
| Error | error_handling, parse_error | Handle extraction failures with fallbacks |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[parser-builder]] | upstream | 0.63 |
| [[p11_qg_parser]] | downstream | 0.53 |
| [[bld_collaboration_parser]] | upstream | 0.51 |
| [[p01_kc_parser]] | upstream | 0.49 |
| [[p03_sp_parser_builder]] | upstream | 0.47 |
| [[bld_architecture_response_format]] | sibling | 0.43 |
| [[bld_schema_parser]] | upstream | 0.42 |
| [[bld_memory_parser]] | downstream | 0.41 |
| [[p03_ins_parser]] | upstream | 0.38 |
| [[bld_examples_parser]] | upstream | 0.37 |
