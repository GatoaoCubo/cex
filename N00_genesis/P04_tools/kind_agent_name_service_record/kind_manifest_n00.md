---
id: n00_agent_name_service_record_manifest
kind: knowledge_card
pillar: P04
nucleus: n00
title: "Agent Name Service Record -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, agent_name_service_record, p04, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_agent_name_service_record
  - bld_schema_capability_registry
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_collaboration_agent
  - bld_schema_integration_guide
  - bld_schema_agent_profile
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_kind
---

<!-- 8F: F1=knowledge_card P04 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An agent_name_service_record is an IETF ANS (Agent Name Service) registry record that enables agent discovery in multi-agent networks. It declares an agent's canonical ID, capabilities, endpoint, authentication requirements, and supported protocols so other agents can find and invoke it without manual configuration. The output is a machine-readable registry entry compatible with emerging agent-to-agent (A2A) standards.

## Pillar
P04 -- tools

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent_name_service_record` |
| pillar | string | yes | Always `P04` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| agent_id | string | yes | Canonical agent identifier (e.g., urn:cex:n03:engineering) |
| capabilities | list | yes | List of capability tags the agent exposes |
| endpoint | string | yes | URL or local path where the agent can be invoked |
| auth_scheme | string | yes | none, api_key, oauth2, mtls |

## When to use
- When registering a nucleus or custom agent in a multi-agent discovery network
- When building A2A (agent-to-agent) communication infrastructure that requires dynamic routing
- When the capability_registry needs a machine-readable entry for a new agent

## Builder
`archetypes/builders/agent_name_service_record-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent_name_service_record --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: ans_n03_engineering
kind: agent_name_service_record
pillar: P04
nucleus: n03
title: "N03 Engineering ANS Record"
version: 1.0
quality: null
---
agent_id: "urn:cex:n03:engineering"
capabilities: [build, scaffold, architect, compile, review]
endpoint: "local://boot/n03.ps1"
auth_scheme: none
```

## Related kinds
- `agent_card` (P08) -- human-readable capability card that complements the ANS record
- `capability_registry` (P08) -- index that stores all agent_name_service_records
- `mcp_server` (P04) -- protocol layer through which the agent exposes its endpoint
- `nucleus_def` (P08) -- machine-readable nucleus identity that ANS record references

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_agent_name_service_record]] | downstream | 0.39 |
| [[bld_schema_capability_registry]] | downstream | 0.38 |
| [[bld_schema_benchmark_suite]] | downstream | 0.38 |
| [[bld_schema_reranker_config]] | downstream | 0.38 |
| [[bld_collaboration_agent]] | downstream | 0.38 |
| [[bld_schema_integration_guide]] | downstream | 0.37 |
| [[bld_schema_agent_profile]] | downstream | 0.37 |
| [[bld_schema_search_strategy]] | downstream | 0.37 |
| [[bld_schema_usage_report]] | downstream | 0.37 |
| [[bld_schema_kind]] | downstream | 0.36 |
