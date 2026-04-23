---
kind: knowledge_card
id: bld_knowledge_card_api_reference
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for api_reference production
quality: 9.1
title: "Knowledge Card Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, knowledge_card]
tldr: "Domain knowledge for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_knowledge_card_quickstart_guide
  - kc_api_reference
  - bld_knowledge_card_sdk_example
  - bld_instruction_api_reference
  - p03_sp_api_reference_builder
  - api-reference-builder
  - bld_knowledge_card_oauth_app_config
  - hybrid_review7_n03
  - bld_knowledge_card_marketplace_app_manifest
  - bld_knowledge_card_transport_config
---

## Domain Overview
API reference documentation serves as a critical interface between API providers and consumers, enabling developers to understand and integrate with an API effectively. It standardizes communication by detailing endpoints, request/response formats, authentication mechanisms, and usage examples. In modern software ecosystems, especially in SaaS, microservices, and platform economies, comprehensive API references are essential for onboarding developers, ensuring interoperability, and reducing integration friction. They also act as a contract, defining expected behavior and constraints for both producers and consumers of an API.

## Key Concepts
| Concept               | Definition                                                                 | Source                          |
|-----------------------|----------------------------------------------------------------------------|---------------------------------|
| REST                  | Architectural style emphasizing statelessness, uniform interfaces, and resource-based URLs | RFC 7231                        |
| OpenAPI Specification | Standard for describing RESTful APIs using declarative YAML or JSON formats | OpenAPI Initiative              |
| OAuth 2.0             | Authorization framework enabling secure delegated access without sharing credentials | RFC 6749                        |
| HTTP Methods          | Verbs (GET, POST, PUT, DELETE) defining resource operations                  | RFC 7231                        |
| Status Codes          | Numeric responses (200, 404, 500) indicating request outcomes               | RFC 7231                        |
| Query Parameters      | Key-value pairs in URLs for filtering, sorting, or pagination               | RFC 3986                        |
| Path Parameters       | URL segments representing resource identifiers                              | RFC 7231                        |
| Headers               | Metadata for requests/responses (e.g., authentication tokens, content type) | RFC 7230                        |
| JSON Schema           | Structural definition for validating request/response payloads              | JSON Schema (IETF)              |
| HAL                   | Hypertext Application Language for linking resources within API responses   | RFC 5843                        |

## Industry Standards
- OpenAPI Specification (OAS)
- OAuth 2.0 (RFC 6749)
- RFC 7231 (HTTP/1.1 Semantics)
- JSON:API (Standard for RESTful JSON APIs)
- RAML (RESTful API Modeling Language)
- gRPC (High-performance RPC framework)

## Common Patterns
1. Versioning endpoints via URL paths (e.g., `/api/v1/resource`).
2. Using consistent status codes (e.g., 400 for client errors, 500 for server errors).
3. Including example requests/responses for each endpoint.
4. Documenting authentication mechanisms (e.g., API keys, OAuth tokens).
5. Grouping related endpoints into logical sections (e.g., "User Management").

## Pitfalls
- Omitting required authentication details (e.g., token scopes or headers).
- Inconsistent parameter naming (e.g., `user_id` vs. `userId`).
- Vague error messages without actionable resolution guidance.
- Failing to document rate limits or usage quotas.
- Overlooking edge cases (e.g., empty responses, optional parameters).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_quickstart_guide]] | sibling | 0.45 |
| [[kc_api_reference]] | sibling | 0.38 |
| [[bld_knowledge_card_sdk_example]] | sibling | 0.38 |
| [[bld_instruction_api_reference]] | downstream | 0.36 |
| [[p03_sp_api_reference_builder]] | downstream | 0.34 |
| [[api-reference-builder]] | downstream | 0.33 |
| [[bld_knowledge_card_oauth_app_config]] | sibling | 0.32 |
| [[hybrid_review7_n03]] | downstream | 0.31 |
| [[bld_knowledge_card_marketplace_app_manifest]] | sibling | 0.30 |
| [[bld_knowledge_card_transport_config]] | sibling | 0.28 |
