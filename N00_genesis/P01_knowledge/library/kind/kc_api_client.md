---
id: p01_kc_api_client
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P04
title: "API Client — Deep Knowledge for api_client"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: operations_agent
domain: api_client
quality: 9.1
tags: [api_client, P04, CALL, kind-kc]
tldr: "Typed client wrapping a REST/GraphQL/gRPC endpoint for deterministic external service calls"
when_to_use: "Building, reviewing, or reasoning about api_client artifacts"
keywords: [api, rest-client, typed-wrapper]
feeds_kinds: [api_client]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
aliases: ["REST client", "API wrapper", "HTTP client", "service connector", "API integration"]
user_says: ["connect to an API", "cliente de API", "integrate with a service", "call an external endpoint", "wrap this REST API"]
long_tails: ["I need to call an external REST API from my agent", "integrate with a third-party service via HTTP", "build a typed wrapper around this API endpoint", "connect my agent to an external data source via API"]
cross_provider:
  langchain: "BaseTool wrapping requests / API SDK"
  llamaindex: "LlamaHub tool spec / FunctionTool"
  crewai: "BaseTool with API call in _run()"
  dspy: "Python function in Module.forward()"
  openai: "function tool with developer-side execution"
  anthropic: "tool definition with developer-side execution"
  haystack: "Custom @component making HTTP calls"
related:
  - api-client-builder
  - bld_collaboration_client
  - n06_api_access_pricing
  - bld_knowledge_card_client
  - p03_sp_client_builder
  - bld_instruction_client
  - kc_api_reference
  - p11_qg_client
  - bld_tools_client
  - bld_output_template_sdk_example
---

# API Client

## Spec
```yaml
kind: api_client
pillar: P04
llm_function: CALL
max_bytes: 1024
naming: p04_api_{{service}}.md + .yaml
core: false
```

## What It Is
An API client is a typed wrapper around an external REST, GraphQL, or gRPC endpoint that an agent can invoke. It provides a deterministic, schema-validated interface for making outbound calls. It is NOT a db_connector (which targets databases specifically) nor an mcp_server (which exposes tools inward to the LLM). An API client is unidirectional: agent calls out to an external service.

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | `BaseTool` wrapping `requests` / API SDK | Custom tool that calls external API with typed input |
| LlamaIndex | LlamaHub tool specs / custom `FunctionTool` | Tool wrappers around external API calls |
| CrewAI | `BaseTool` with API call in `_run()` | Custom tool making HTTP requests to external services |
| DSPy | Python function called inside `Module.forward()` | Direct API calls within module execution flow |
| Haystack | Custom `@component` making HTTP calls | Component wrapping external service interaction |
| OpenAI | `function` tool with developer-side execution | Model requests function call; developer executes API call |
| Anthropic | `tool` definition with developer-side execution | `tool_use` block triggers developer to call external API |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| base_url | string | required | Hardcoded = simple but inflexible across environments |
| auth_method | enum | "bearer" | API key = simple; OAuth = secure but complex setup |
| timeout_ms | int | 5000 | Higher = tolerant of slow APIs but blocks agent longer |
| retry_count | int | 1 | More retries = resilient but higher latency on failures |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| SDK wrapper | Official SDK available | `BlingConnector(api_key=...)` wrapping Bling V3 REST API |
| Generic HTTP client | No SDK, simple REST endpoints | `requests.get(url, headers=auth)` with typed response |
| Rate-limited client | API has usage quotas | Client with built-in rate limiter and quota tracking |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Raw HTTP calls without typing | No validation, silent failures on schema changes | Wrap in typed client with response validation |
| Hardcoding auth credentials | Security risk, breaks across environments | Use env vars or secret manager for credentials |

## Integration Graph
```
[action_prompt] --> [api_client] --> [output_template]
                        |
                  [constraint_spec]
```

## Decision Tree
- IF external service has official SDK THEN wrap SDK in api_client
- IF no SDK and simple REST THEN use generic HTTP client pattern
- IF API has rate limits THEN add rate-limited client pattern
- DEFAULT: Typed wrapper with auth from env vars and 5s timeout

## Quality Criteria
- GOOD: Has base_url, auth method, typed request/response, under 1024 bytes
- GREAT: Includes retry logic, rate limiting, error mapping, and health check
- FAIL: Raw untyped HTTP calls; hardcoded credentials; no error handling

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[api-client-builder]] | related | 0.42 |
| [[bld_collaboration_client]] | downstream | 0.42 |
| [[n06_api_access_pricing]] | downstream | 0.37 |
| [[bld_knowledge_card_client]] | sibling | 0.32 |
| [[p03_sp_client_builder]] | related | 0.31 |
| [[bld_instruction_client]] | upstream | 0.29 |
| [[kc_api_reference]] | sibling | 0.29 |
| [[p11_qg_client]] | downstream | 0.28 |
| [[bld_tools_client]] | related | 0.27 |
| [[bld_output_template_sdk_example]] | downstream | 0.27 |
