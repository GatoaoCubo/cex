---
kind: architecture
id: bld_architecture_formatter
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of formatter — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Formatter"
version: "1.0.0"
author: n03_builder
tags: [formatter, builder, examples]
tldr: "Golden and anti-examples for formatter construction, demonstrating ideal structure and common pitfalls."
domain: "formatter construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - formatter-builder
  - bld_collaboration_formatter
  - p01_kc_formatter
  - p05_fmt_artifact_creation_report
  - p03_sp_formatter_builder
  - bld_instruction_formatter
  - p10_lr_formatter_builder
  - bld_schema_formatter
  - p11_qg_formatter
  - bld_tools_formatter
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| input_type | Structured data type received by the formatter (dict, list, object, etc.) | formatter | required |
| output_format | Target representation: JSON, YAML, Markdown, HTML, table, CSV, plain text | formatter | required |
| transform_rules | Ordered set of transformation operations applied to input data | formatter | required |
| template | String template or schema used to render the output structure | formatter | optional |
| serializer | Format-specific serialization logic (json.dumps, yaml.dump, tabulate, etc.) | formatter | conditional |
| escaping_strategy | Rules for escaping special characters in the target format | formatter | conditional |
| locale_config | Locale-aware settings for number, date, and currency formatting | formatter | optional |
| null_handling | Rule for rendering missing or null values (empty string, "N/A", omit key) | formatter | required |
| truncation_rule | Maximum length per field; prevents output bloat | formatter | optional |
## Dependency Graph
```
parser (P05)        --produces--> formatter
agent (P02)         --produces--> formatter
knowledge_card (P01) --produces--> formatter
formatter           --produces--> display_ui
formatter           --produces--> api_response
formatter           --produces--> file_export
validator (P06)     --depends-->  formatter
```
| From | To | Type | Data |
|------|----|------|------|
| parser (P05) | formatter | produces | structured data extracted from raw input |
| agent (P02) | formatter | produces | typed output requiring presentation |
| knowledge_card (P01) | formatter | produces | domain facts to render as table or list |
| formatter | display_ui | data_flow | rendered string for user-facing display |
| formatter | api_response | data_flow | serialized payload for API consumption |
| formatter | file_export | data_flow | formatted file content (Markdown, CSV, JSON) |
| validator (P06) | formatter | depends | output schema the formatter must conform to |
## Boundary Table
| formatter IS | formatter IS NOT |
|--------------|------------------|
| A presentation transformer — converts structured data to display format | A data extractor from raw text (that is parser) |
| Applied after data is already structured | A validator that checks content correctness |
| Stateless per invocation — no side effects | A prompt template that instructs an LLM |
| Owner of escaping, locale, and null-handling rules | A response_format definition telling an LLM what to produce |
| Responsible for serialization (JSON, YAML, table) | A naming convention rule for identifiers |
| Capable of multiple output targets (UI, API, file) | An output schema that validates format correctness |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| Input | parser (P05), agent (P02), knowledge_card (P01) | Supply structured data to be formatted |
| Transform | transform_rules, template, serializer | Apply ordered operations to convert data to target format |
| Locale & Safety | escaping_strategy, locale_config, null_handling, truncation_rule | Handle edge cases: encoding, locale, missing values, length |
| Validation | validator (P06) | Confirm output conforms to expected format schema |
| Output | display_ui, api_response, file_export | Deliver formatted result to its consumer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[formatter-builder]] | upstream | 0.68 |
| [[bld_collaboration_formatter]] | downstream | 0.65 |
| [[p01_kc_formatter]] | upstream | 0.55 |
| [[p05_fmt_artifact_creation_report]] | upstream | 0.52 |
| [[p03_sp_formatter_builder]] | upstream | 0.52 |
| [[bld_instruction_formatter]] | upstream | 0.49 |
| [[p10_lr_formatter_builder]] | downstream | 0.46 |
| [[bld_schema_formatter]] | upstream | 0.44 |
| [[p11_qg_formatter]] | downstream | 0.42 |
| [[bld_tools_formatter]] | upstream | 0.40 |
