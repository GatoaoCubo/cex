---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of connector — inventory, dependencies, and architectural position
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| outbound_endpoint | Sends data to external service — method, path, payload schema | connector | required |
| inbound_endpoint | Receives data from external service — webhook path, event schema | connector | required |
| protocol | Wire protocol for the integration (REST, WebSocket, gRPC, MQTT) | connector | required |
| auth_strategy | Authentication for both directions (API key, OAuth2, mTLS, HMAC) | connector | required |
| data_mapping | Transform rules converting internal schema to external format and back | connector | required |
| health_check | Periodic probe confirming the external service is reachable | connector | required |
| retry_policy | Backoff + max_attempts for failed outbound requests | connector | required |
| rate_limit | Throttle policy applied to outbound calls | connector | optional |
| env_config | Secrets, service URLs, and credentials from environment | P09 | external |
| guardrail | Auth and rate enforcement constraints | P11 | external |
| agent | Caller that triggers outbound operations or handles inbound events | P02 | consumer |
| workflow | Orchestrator that sequences connector calls in a pipeline | P12 | consumer |

## Dependency Graph

```
env_config         --produces-->  auth_strategy
env_config         --produces-->  outbound_endpoint
guardrail          --produces-->  rate_limit
outbound_endpoint  --depends-->   protocol
outbound_endpoint  --depends-->   auth_strategy
outbound_endpoint  --depends-->   data_mapping
inbound_endpoint   --depends-->   protocol
inbound_endpoint   --depends-->   auth_strategy
inbound_endpoint   --depends-->   data_mapping
health_check       --depends-->   outbound_endpoint
retry_policy       --depends-->   outbound_endpoint
outbound_endpoint  <-->           inbound_endpoint
agent              --depends-->   outbound_endpoint
agent              --depends-->   inbound_endpoint
workflow           --depends-->   outbound_endpoint
```

| From | To | Type | Data |
|------|----|------|------|
| env_config | auth_strategy | produces | credentials and secrets injected at runtime |
| env_config | outbound_endpoint | produces | service base URL and path configuration |
| guardrail | rate_limit | produces | throttle policy from constraint config |
| outbound_endpoint | protocol | depends | wire protocol for sending requests |
| outbound_endpoint | auth_strategy | depends | auth applied to outgoing calls |
| outbound_endpoint | data_mapping | depends | internal-to-external schema transform |
| inbound_endpoint | protocol | depends | wire protocol for receiving events |
| inbound_endpoint | auth_strategy | depends | signature verification for inbound calls |
| inbound_endpoint | data_mapping | depends | external-to-internal schema transform |
| health_check | outbound_endpoint | depends | probes the outbound path for liveness |
| retry_policy | outbound_endpoint | depends | retry wraps outbound call on failure |
| outbound_endpoint | inbound_endpoint | bidirectional | paired send/receive on same service |
| agent | outbound_endpoint | depends | agent triggers outbound calls |
| agent | inbound_endpoint | depends | agent handles inbound webhook events |
| workflow | outbound_endpoint | depends | workflow sequences connector operations |

## Boundary Table

| connector IS | connector IS NOT |
|-------------|-----------------|
| Bidirectional integration — sends outbound AND receives inbound | A unidirectional API consumer (that is client) |
| Defines data mapping and transform rules between schemas | An HTML/DOM data extractor (that is scraper) |
| Handles webhooks, streams, pub/sub event reception | A tool exposed via MCP protocol (that is mcp_server) |
| Includes health check and liveness monitoring | A reusable phased capability (that is skill) |
| One connector per external service integration | A background process with no external service (that is daemon) |
| Protocol-aware (REST, WebSocket, gRPC, MQTT) | A one-shot command executed from terminal (that is cli_tool) |

## Layer Map

| Layer | Components | Purpose |
|-------|-----------|---------|
| configuration | env_config, auth_strategy, protocol | Supply credentials, secrets, and wire protocol |
| outbound | outbound_endpoint, data_mapping, retry_policy, rate_limit | Define outgoing data path and resilience |
| inbound | inbound_endpoint, data_mapping | Define incoming event reception and transform |
| operations | health_check | Monitor external service liveness |
| governance | guardrail | Enforce rate and auth constraint policy |
| callers | agent, workflow | Runtime consumers that drive integration |
