---
kind: knowledge_card
id: bld_knowledge_card_client
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for client production — unidirectional API consumer specification
sources: REST conventions, HTTP standards (RFC 7231), Stripe/GitHub API patterns
---

# Domain Knowledge: client
## Executive Summary
Clients are unidirectional API consumers that send requests and receive responses from external services via REST, GraphQL, or gRPC. They define endpoints, authentication, error handling, pagination, and retry policies. Clients differ from connectors (bidirectional), MCP servers (protocol providers), and scrapers (HTML extraction).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Direction | Unidirectional (request → response) |
| Protocols | REST, GraphQL, gRPC |
| Auth strategies | none, api_key, oauth, bearer |
| Endpoint naming | verb_noun snake_case (create_charge, list_orders) |
## Patterns
- **Auth strategy selection**: match API requirements exactly — api_key for SaaS, oauth for delegated, bearer for JWT
| Strategy | Header | Use case |
|----------|--------|----------|
| none | — | Internal APIs with network trust |
| api_key | `X-API-Key: {key}` | SaaS APIs (most common) |
| oauth | `Authorization: Bearer {access_token}` | User-delegated access |
| bearer | `Authorization: Bearer {token}` | JWT or static token |
- **Error handling by HTTP code**: retry 429 (rate limit) and 5xx (server error); do not retry 400/403/404
| Code | Meaning | Retry? |
|------|---------|--------|
| 400 | Bad request | No (fix input) |
| 401 | Auth failed | Refresh token, retry once |
| 429 | Rate limited | Yes (backoff per Retry-After) |
| 5xx | Server error | Yes (exponential backoff) |
- **Pagination**: cursor-based (Stripe, Shopify) for reliability; offset-based for simple APIs
- **Rate limiting**: respect API limits; implement exponential backoff with jitter
- **Serialization**: JSON default; XML for legacy SOAP; protobuf for gRPC
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Guessing auth strategy | Wrong header = 401 on every request |
| No retry on 429/5xx | Transient failures become permanent errors |
| Retrying 400 errors | Bad input stays bad; retries waste quota |
| Missing pagination | Only first page of results returned |
| No timeout configured | Requests hang indefinitely on slow APIs |
| Mixing client with connector | Client is read-only; bidirectional needs connector |
## Application
1. Identify API: base_url, protocol (REST/GraphQL/gRPC), auth strategy
2. Map endpoints: verb_noun naming, HTTP method, path, parameters, return types
3. Configure auth: strategy, token refresh, credential storage
4. Set resilience: timeout, retry policy (exponential backoff), rate limit handling
5. Define pagination: cursor or offset, page size
6. Validate: test each endpoint with expected and error responses
## References
- RFC 7231: HTTP/1.1 Semantics and Content
- Stripe API: client design patterns (pagination, idempotency, versioning)
- GitHub API: rate limiting and auth best practices
- Enterprise Integration Patterns: messaging and request-reply
