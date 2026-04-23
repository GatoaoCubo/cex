---
kind: architecture
id: bld_architecture_client
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of client — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Api Client"
version: "1.0.0"
author: n03_builder
tags: [api_client, builder, examples]
tldr: "Golden and anti-examples for api client construction, demonstrating ideal structure and common pitfalls."
domain: "api client construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - api-client-builder
  - p11_qg_client
  - bld_instruction_client
  - bld_architecture_connector
  - bld_collaboration_client
  - p03_sp_client_builder
  - p01_kc_api_client
  - bld_knowledge_card_client
  - bld_schema_client
  - bld_architecture_cli_tool
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| endpoint | Single API operation — method + path + parameters + return type | client | required |
| auth_strategy | Authentication mechanism (API key, OAuth2, Bearer, mTLS) | client | required |
| base_url | Root URL for all endpoint paths | client | required |
| rate_limit | Request throttle policy (requests/sec, burst cap) | client | required |
| retry_policy | Backoff + max_attempts for transient failures | client | required |
| timeout | Per-request time ceiling | client | required |
| pagetion | Cursor or page-based result iteration pattern | client | optional |
| serialization | Wire format for request/response bodies (json, xml, protobuf) | client | required |
| env_config | API keys, base URLs, secrets from environment | P09 | external |
| guardrail | Rate limit constraints and auth enforcement policy | P11 | external |
| agent | Runtime caller that issues API requests via this client | P02 | consumer |
| skill | Wraps one or more client calls into a reusable phased capability | P04 | consumer |
## Dependency Graph
```
env_config     --produces--> base_url
env_config     --produces--> auth_strategy
guardrail      --produces--> rate_limit
endpoint       --depends-->  base_url
endpoint       --depends-->  auth_strategy
endpoint       --depends-->  serialization
retry_policy   --depends-->  endpoint
timeout        --depends-->  endpoint
pagetion     --depends-->  endpoint
agent          --depends-->  endpoint
skill          --depends-->  endpoint
```
| From | To | Type | Data |
|------|----|------|------|
| env_config | base_url | produces | root URL injected at runtime |
| env_config | auth_strategy | produces | credentials (keys, tokens) |
| guardrail | rate_limit | produces | throttle policy from constraint config |
| endpoint | base_url | depends | root URL to construct full request URL |
| endpoint | auth_strategy | depends | auth headers or token attached to request |
| endpoint | serialization | depends | body encoding/decoding format |
| retry_policy | endpoint | depends | retry wraps individual endpoint calls |
| timeout | endpoint | depends | timeout applied per endpoint call |
| pagetion | endpoint | depends | iterates endpoint across result pages |
| agent | endpoint | depends | agent issues API call through endpoint |
| skill | endpoint | depends | skill phase wraps endpoint call |
## Boundary Table
| client IS | client IS NOT |
|-----------|--------------|
| Unidirectional API consumer — sends requests, receives responses | A bidirectional integration that also receives webhooks (that is connector) |
| Consumes structured APIs (REST, GraphQL, gRPC) | Extracts data from HTML/DOM (that is scraper) |
| Programmatic call from agent or skill code | A terminal command invoked via shell (that is cli_tool) |
| One client per external API surface | A tool protocol server exposing capabilities (that is mcp_server) |
| Defines auth, rate limits, retries, and serialization | A reusable capability with defined trigger phases (that is skill) |
| Stateless per call — no persistent connection | A long-lived background process (that is daemon) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | env_config, base_url, auth_strategy | Supply credentials and root URL at runtime |
| interface | endpoint, serialization, pagetion | Define the API surface and data encoding |
| resilience | retry_policy, timeout, rate_limit | Handle failures, throttling, and time bounds |
| governance | guardrail | Enforce rate and auth constraints from policy |
| callers | agent, skill | Runtime consumers that invoke API operations |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[api-client-builder]] | upstream | 0.44 |
| [[p11_qg_client]] | downstream | 0.42 |
| [[bld_instruction_client]] | upstream | 0.38 |
| [[bld_architecture_connector]] | sibling | 0.37 |
| [[bld_collaboration_client]] | downstream | 0.35 |
| [[p03_sp_client_builder]] | upstream | 0.30 |
| [[p01_kc_api_client]] | upstream | 0.30 |
| [[bld_knowledge_card_client]] | upstream | 0.29 |
| [[bld_schema_client]] | upstream | 0.29 |
| [[bld_architecture_cli_tool]] | sibling | 0.28 |
