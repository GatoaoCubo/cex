---
id: n00_integration_guide_manifest
kind: knowledge_card
8f: F3_inject
pillar: P05
nucleus: n00
title: "Integration Guide -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, integration_guide, p05, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_contributor_guide
  - bld_schema_api_reference
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_tts_provider
  - bld_schema_search_strategy
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Integration guide produces a deep technical integration document for platform partners covering authentication, endpoint catalog, request/response formats, error handling, rate limits, webhook configuration, and end-to-end working examples. Unlike a quickstart guide, it targets engineers building production integrations and covers edge cases, versioning, and deprecation policies.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `integration_guide` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Platform name + "Integration Guide" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| partner_platform | string | yes | Target integration platform name |
| auth_method | enum | yes | oauth2 / api_key / jwt / mtls |
| base_url | string | yes | API base URL |
| endpoint_count | int | yes | Number of endpoints documented |
| rate_limits | object | yes | Requests per minute/hour/day limits |
| sdk_languages | list | no | Languages with official SDK examples |

## When to use
- Building a partner ecosystem that requires deep technical integrations
- Enabling a platform integration partner to complete their implementation independently
- Replacing informal Slack-based integration support with self-serve documentation

## Builder
`archetypes/builders/integration_guide-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind integration_guide --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations + N04 knowledge co-produce integration docs
- `{{SIN_LENS}}` -- Knowledge Gluttony: exhaustive coverage, no undocumented behavior
- `{{TARGET_AUDIENCE}}` -- partner engineers building production integrations
- `{{DOMAIN_CONTEXT}}` -- API protocol, auth model, payload structures, SLA expectations

## Example (minimal)
```yaml
---
id: integration_guide_cex_zapier
kind: integration_guide
pillar: P05
nucleus: n05
title: "CEX -- Zapier Integration Guide"
version: 1.0
quality: null
---
partner_platform: Zapier
auth_method: api_key
endpoint_count: 12
rate_limits: {rpm: 60, rph: 1000}
```

## Related kinds
- `api_reference` (P06) -- machine-readable contract that backs the integration guide
- `quickstart_guide` (P05) -- abbreviated first-contact doc; integration guide is the deep-dive
- `mcp_server` (P04) -- tool integration that may need an accompanying integration guide

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | downstream | 0.56 |
| [[bld_schema_quickstart_guide]] | downstream | 0.42 |
| [[bld_schema_contributor_guide]] | downstream | 0.42 |
| [[bld_schema_api_reference]] | downstream | 0.41 |
| [[bld_schema_reranker_config]] | downstream | 0.41 |
| [[bld_schema_usage_report]] | downstream | 0.40 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_dataset_card]] | downstream | 0.40 |
| [[bld_schema_tts_provider]] | downstream | 0.40 |
| [[bld_schema_search_strategy]] | downstream | 0.39 |
