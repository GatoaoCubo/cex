---
id: n00_api_reference_manifest
kind: knowledge_card
8f: F3_inject
pillar: P06
nucleus: n00
title: "Api Reference -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, api_reference, p06, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_api_reference
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_tts_provider
  - bld_schema_benchmark_suite
  - bld_schema_client
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
API reference produces a machine-readable and human-readable documentation artifact covering all endpoints, parameters, request/response schemas, authentication requirements, error codes, and usage examples for an API surface. It follows OpenAPI 3.1 conventions and serves as the authoritative contract between API producers and consumers. It constrains how downstream integrations are built.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `api_reference` |
| pillar | string | yes | Always `P06` |
| title | string | yes | API name + version |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| api_version | string | yes | API version (e.g., v1, v2) |
| base_url | string | yes | API base URL |
| auth_schemes | list | yes | Supported auth methods (oauth2, api_key, jwt) |
| endpoints | list | yes | Endpoint definitions with method, path, params, responses |
| error_codes | list | yes | All possible error codes with descriptions |
| openapi_version | string | yes | OpenAPI spec version (3.0.x or 3.1.x) |

## When to use
- Documenting a new or updated API for developer consumption
- Providing the authoritative contract that backs an integration guide
- Generating SDK documentation from a canonical source of truth

## Builder
`archetypes/builders/api_reference-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind api_reference --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations writes; N04 knowledge publishes
- `{{SIN_LENS}}` -- Inventive Pride: precise, complete, no undocumented behavior
- `{{TARGET_AUDIENCE}}` -- developers integrating with the API
- `{{DOMAIN_CONTEXT}}` -- API domain, auth model, versioning strategy, SLA

## Example (minimal)
```yaml
---
id: api_reference_cex_sdk_v1
kind: api_reference
pillar: P06
nucleus: n05
title: "CEX SDK API Reference v1"
version: 1.0
quality: null
---
api_version: v1
base_url: "https://api.cex.example.com/v1"
auth_schemes: [api_key, oauth2]
openapi_version: "3.1.0"
```

## Related kinds
- `integration_guide` (P05) -- human-friendly narrative backed by this reference
- `input_schema` (P06) -- request body schemas referenced in each endpoint definition
- `interface` (P06) -- agent-to-agent contracts that may expose an API surface

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_api_reference]] | related | 0.58 |
| [[bld_schema_integration_guide]] | related | 0.52 |
| [[bld_schema_reranker_config]] | related | 0.47 |
| [[bld_schema_tts_provider]] | related | 0.46 |
| [[bld_schema_benchmark_suite]] | related | 0.46 |
| [[bld_schema_client]] | related | 0.45 |
| [[bld_schema_usage_report]] | related | 0.45 |
| [[bld_schema_dataset_card]] | related | 0.45 |
| [[bld_schema_search_strategy]] | related | 0.45 |
| [[bld_schema_quickstart_guide]] | related | 0.44 |
