---
id: n00_formatter_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Formatter -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, formatter, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_formatter
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - p05_fmt_artifact_creation_report
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_schema_multimodal_prompt
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
  - bld_schema_app_directory_entry
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Formatter defines an output transformation rule that converts LLM-generated content into a specific serialization format (JSON, YAML, Markdown, CSV, XML). It specifies the target schema, field mapping, type coercions, and error handling behavior. Formatters are applied post-generation in the 8F pipeline at F7 GOVERN to enforce output contracts.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `formatter` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Human-readable formatter name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_format | enum | yes | json / yaml / markdown / csv / xml / plain |
| input_type | string | yes | Expected input structure description |
| field_mappings | list | no | Source-to-target field rename/transform rules |
| null_handling | string | yes | skip / empty_string / error |
| on_error | enum | yes | raise / warn / passthrough |

## When to use
- Enforcing a downstream API contract on LLM output
- Normalizing varied LLM response formats to a canonical schema
- Post-processing structured extraction results before persistence

## Builder
`archetypes/builders/formatter-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind formatter --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements formatters in pipelines
- `{{SIN_LENS}}` -- Gating Wrath: strict enforcement, no malformed output passes
- `{{TARGET_AUDIENCE}}` -- downstream systems consuming formatted output
- `{{DOMAIN_CONTEXT}}` -- target API schema, format specification, error tolerance

## Example (minimal)
```yaml
---
id: formatter_json_knowledge_card
kind: formatter
pillar: P05
nucleus: n05
title: "JSON Formatter for Knowledge Cards"
version: 1.0
quality: null
---
target_format: json
null_handling: skip
on_error: raise
```

## Related kinds
- `parser` (P05) -- extracts fields from raw LLM output before formatting
- `output_validator` (P05) -- validates formatted output against a contract
- `response_format` (P05) -- defines HOW the agent responds; formatter transforms WHAT

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_formatter]] | downstream | 0.44 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_integration_guide]] | downstream | 0.42 |
| [[p05_fmt_artifact_creation_report]] | related | 0.41 |
| [[bld_schema_pitch_deck]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_voice_pipeline]] | downstream | 0.40 |
| [[bld_schema_app_directory_entry]] | downstream | 0.40 |
