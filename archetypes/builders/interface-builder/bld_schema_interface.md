---
kind: schema
id: bld_schema_interface
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for interface
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_input_schema
  - bld_schema_unit_eval
  - bld_schema_handoff_protocol
  - bld_schema_reranker_config
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_chunk_strategy
  - bld_schema_golden_test
  - bld_schema_constraint_spec
  - bld_schema_action_prompt
---

# Schema: interface
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_iface_{contract}) | YES | - | Namespace compliance |
| kind | literal "interface" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| contract | string | YES | - | Human-readable contract name |
| provider | string | YES | - | Provider agent/system |
| consumer | string | YES | - | Consumer agent/system |
| methods | list[object] | YES | - | Method definitions (min 1) |
| backward_compatible | boolean | YES | true | Breaking change flag |
| deprecation | object {deprecated_methods, sunset_date, migration} | REC | null | Deprecation plan |
| mock | object {enabled, example_payloads} | REC | null | Test specification |
| domain | string | YES | - | Integration domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "interface" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string] | REC | - | Brain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |
## Methods Object
```yaml
methods:
  - name: "{{method_name}}"
    input: {{type_or_object}}
    output: {{type_or_object}}
    description: "{{what_it_does}}"
```
Each method MUST have: name, input, output, description.
Input/output can be primitives (string, integer, boolean) or structured objects.
## Deprecation Object
```yaml
deprecation:
  deprecated_methods: ["method_a", "method_b"]
  sunset_date: "2026-06-01"
  migration: "Use method_c instead of method_a"
```
All fields optional. If no deprecation planned: deprecation: null.
## Mock Object
```yaml
mock:
  enabled: true
  example_payloads:
    - method: "get_status"
      input: {"agent_id": "shaka"}
      output: {"status": "active", "uptime": 3600}
```
## ID Pattern
Regex: `^p06_iface_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Contract Definition` — what this interface enables, in plain language
2. `## Methods` — table with name/input/output/description for each method
3. `## Versioning` — version, backward_compatible, changelog, migration
4. `## Mock Specification` — example payloads for testing
## Constraints
- max_bytes: 3072 (body only)
- naming: p06_iface_{contract}.yaml
- machine_format: json (compiled form)
- id == filename stem
- methods MUST have at least 1 entry
- backward_compatible MUST be boolean
- quality: null always
- interface is bilateral — provider AND consumer must be specified

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | sibling | 0.63 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
| [[bld_schema_handoff_protocol]] | sibling | 0.59 |
| [[bld_schema_reranker_config]] | sibling | 0.59 |
| [[bld_schema_retriever_config]] | sibling | 0.58 |
| [[bld_schema_output_validator]] | sibling | 0.58 |
| [[bld_schema_chunk_strategy]] | sibling | 0.58 |
| [[bld_schema_golden_test]] | sibling | 0.58 |
| [[bld_schema_constraint_spec]] | sibling | 0.57 |
| [[bld_schema_action_prompt]] | sibling | 0.57 |
