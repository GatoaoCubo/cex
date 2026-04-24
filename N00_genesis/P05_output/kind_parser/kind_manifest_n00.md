---
id: n00_parser_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Parser -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, parser, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_parser
  - parser-builder
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_collaboration_parser
  - p01_kc_parser
  - bld_architecture_parser
  - bld_schema_dataset_card
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Parser defines an output data extraction rule that pulls structured fields from raw LLM-generated text using pattern matching, regex, JSON extraction, or structured parsing strategies. Parsers operate between LLM generation and downstream formatting or validation, converting unstructured or semi-structured output into typed key-value data.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `parser` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Parser name describing what it extracts |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| input_format | enum | yes | raw_text / markdown / json / xml / yaml |
| extraction_method | enum | yes | regex / json_path / xml_xpath / llm_extract |
| output_fields | list | yes | Field definitions with name, type, required, pattern |
| on_missing | enum | yes | null / default / error |
| confidence_threshold | float | no | Minimum extraction confidence (0.0-1.0) |

## When to use
- Extracting structured data from narrative LLM output (e.g., parsing a score from a paragraph)
- Converting markdown-formatted LLM responses to typed JSON for downstream APIs
- Building a structured extraction layer on top of an LLM that does not support JSON mode

## Builder
`archetypes/builders/parser-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind parser --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements parsers in pipeline steps
- `{{SIN_LENS}}` -- Gating Wrath: extract only verified, typed data
- `{{TARGET_AUDIENCE}}` -- downstream formatters, validators, or storage layers
- `{{DOMAIN_CONTEXT}}` -- LLM output format, required fields, type constraints

## Example (minimal)
```yaml
---
id: parser_quality_score_extractor
kind: parser
pillar: P05
nucleus: n05
title: "Quality Score Parser from LLM Evaluation Output"
version: 1.0
quality: null
---
input_format: raw_text
extraction_method: regex
on_missing: error
output_fields:
  - {name: score, type: float, required: true, pattern: "Score: (\\d+\\.?\\d*)"}
```

## Related kinds
- `formatter` (P05) -- formats parsed fields into target serialization
- `output_validator` (P05) -- validates parsed output against business rules
- `input_schema` (P06) -- defines the contract for what the parser should extract

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_parser]] | downstream | 0.46 |
| [[parser-builder]] | related | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.40 |
| [[bld_schema_integration_guide]] | downstream | 0.40 |
| [[bld_collaboration_parser]] | related | 0.39 |
| [[p01_kc_parser]] | sibling | 0.39 |
| [[bld_architecture_parser]] | downstream | 0.38 |
| [[bld_schema_dataset_card]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_sandbox_spec]] | downstream | 0.36 |
