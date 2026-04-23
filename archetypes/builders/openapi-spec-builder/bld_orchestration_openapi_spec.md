---
quality: 8.4
quality: 8.0
kind: collaboration
id: bld_collaboration_openapi_spec
pillar: P12
llm_function: COLLABORATE
purpose: How openapi-spec-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
title: "Collaboration OpenAPI Spec"
version: "1.0.0"
author: n03_builder
tags: [openapi_spec, builder, collaboration]
tldr: "API contract specialist. Upstream of api_client and api_reference. Downstream of domain model design."
domain: "openapi spec construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
related:
  - bld_collaboration_client
  - bld_collaboration_builder
  - bld_collaboration_input_schema
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_streaming_config
  - bld_collaboration_agent
  - bld_collaboration_retriever
  - bld_collaboration_kind
  - bld_collaboration_validation_schema
---
# Collaboration: openapi-spec-builder
## My Role in Crews
| Responsibility | What I Answer | What I DON'T Do |
|----------------|---------------|-----------------|
| API CONTRACT SPECIALIST | "What is the machine-readable surface of this REST API?" | Write SDK code |
| OAS 3.x specification | Paths, operations, schemas, security | Write human documentation |
| Contract layer | Machine-readable for tooling | Handle async event APIs |
## Crew Compositions
### Crew: "API First Development"
```
  1. openapi-spec-builder    -> "OAS 3.x contract (machine-readable)"
  2. api-reference-builder   -> "human-readable docs from spec"
  3. api-client-builder      -> "SDK implementation from spec"
  4. event-schema-builder    -> "async event schemas alongside REST"
```
### Crew: "Integration Package"
```
  1. data-contract-builder   -> "producer-consumer SLA and data model"
  2. openapi-spec-builder    -> "REST API surface (paths, schemas, security)"
  3. event-schema-builder    -> "event payload schemas"
  4. agent-builder           -> "agent that consumes the API"
```
### Crew: "API Gateway Configuration"
```
  1. openapi-spec-builder    -> "API contract for gateway import"
  2. rate-limit-config-builder -> "inbound throttle per endpoint"
  3. env-config-builder      -> "API keys, base URLs, timeouts"
```
## Handoff Protocol
### I Receive
| Input | Type | Notes |
|-------|------|-------|
| API name and base URL | string | Production + staging servers |
| Endpoint list | table | Path + method + purpose |
| Data models | table | Entity names and key fields |
| Auth requirement | enum | JWT, API key, OAuth2, or public |
### I Produce
| Output | Format | Destination |
|--------|--------|-------------|
| openapi_spec artifact | .md with YAML frontmatter + OAS document | N0X_{domain}/P06_schema/ |
| Compilation signal | complete with quality score | .cex/runtime/signals/ |
## Builders I Depend On
| Builder | Why | Dependency Type |
|---------|-----|----------------|
| None | Independent builder (layer 0) | -- |
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| api-client-builder | Generates SDK code from OAS spec |
| api-reference-builder | Renders human docs from OAS spec |
| agent-builder | Agents reference spec for tool configuration |
| env-config-builder | API base URLs defined in servers section |
## Quality Checklist Before Signal
| Check | Pass Condition |
|-------|---------------|
| id pattern | ^p06_oas_[a-z][a-z0-9_]+$ |
| servers | non-empty array |
| paths | at least one operation |
| security | scheme declared + global security set |
| error responses | 400/401/404/500 defined |
| operationId | all operations have camelCase id |
| $ref usage | schemas used 2+ times in components.schemas |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_client]] | sibling | 0.38 |
| [[bld_collaboration_builder]] | sibling | 0.33 |
| [[bld_collaboration_input_schema]] | sibling | 0.31 |
| [[bld_architecture_kind]] | upstream | 0.31 |
| [[kind-builder]] | upstream | 0.28 |
| [[bld_collaboration_streaming_config]] | sibling | 0.28 |
| [[bld_collaboration_agent]] | sibling | 0.28 |
| [[bld_collaboration_retriever]] | sibling | 0.28 |
| [[bld_collaboration_kind]] | sibling | 0.28 |
| [[bld_collaboration_validation_schema]] | sibling | 0.28 |
