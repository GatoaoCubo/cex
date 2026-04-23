---
id: n00_response_format_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Response Format -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, response_format, p05, n00, archetype, template]
density_score: 0.99
related:
  - response-format-builder
  - bld_collaboration_response_format
  - bld_schema_response_format
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_examples_response_format
  - bld_schema_benchmark_suite
  - bld_memory_response_format
  - bld_schema_pitch_deck
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Response format defines how an LLM agent structures and delivers its output to the caller. It constrains tone, length, structure (prose vs. list vs. table), citation style, code block conventions, and termination signals. Applied at F1 CONSTRAIN in the 8F pipeline, it ensures all output from a given agent or pipeline step is consistent and machine-parseable by downstream consumers.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `response_format` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Agent name + "Response Format" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| structure | enum | yes | prose / bullet_list / table / json / markdown_sections |
| max_length | string | no | Token or character limit for the response |
| citation_style | enum | no | inline / footnote / none |
| code_blocks | bool | yes | Whether to use fenced code blocks for code |
| termination_signal | string | no | Explicit signal when response is complete |

## When to use
- Defining how a custom agent responds to users or downstream systems
- Enforcing consistent output structure across all nuclei in a pipeline
- Configuring an LLM to return machine-parseable output in a specific format

## Builder
`archetypes/builders/response_format-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind response_format --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N03 engineering defines; all nuclei consume their own format
- `{{SIN_LENS}}` -- Inventive Pride: precise, elegant, unambiguous specification
- `{{TARGET_AUDIENCE}}` -- downstream parser, user interface, or human reviewer
- `{{DOMAIN_CONTEXT}}` -- agent type, caller system, output consumption method

## Example (minimal)
```yaml
---
id: response_format_n05_operations
kind: response_format
pillar: P05
nucleus: n05
title: "N05 Operations Agent Response Format"
version: 1.0
quality: null
---
structure: markdown_sections
max_length: "4096 tokens"
citation_style: inline
code_blocks: true
termination_signal: "=== END N05 RESPONSE ==="
```

## Related kinds
- `system_prompt` (P03) -- injects the response format as a constraint in the system prompt
- `formatter` (P05) -- transforms output after generation; response format constrains before
- `output_validator` (P05) -- validates that the response conforms to the declared format

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[response-format-builder]] | related | 0.48 |
| [[bld_collaboration_response_format]] | related | 0.39 |
| [[bld_schema_response_format]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.37 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_examples_response_format]] | downstream | 0.36 |
| [[bld_schema_benchmark_suite]] | downstream | 0.35 |
| [[bld_memory_response_format]] | downstream | 0.35 |
| [[bld_schema_pitch_deck]] | downstream | 0.34 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.34 |
