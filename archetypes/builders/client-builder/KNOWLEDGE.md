---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for client production
sources: REST API conventions, HTTP standards, real client examples
---

# Domain Knowledge: client

## Foundational Concept
A client artifact defines the CONSUMPTION CONTRACT for an external API.
It specifies which endpoints to call, how to authenticate, what to expect in
responses, and how to handle errors. Clients are UNIDIRECTIONAL: they send
requests and receive responses. They never expose capabilities to other systems.

## Auth Patterns

| Strategy | Header | Use Case |
|----------|--------|----------|
| none | - | Internal APIs with network trust |
| api_key | `X-API-Key: {key}` or `Authorization: ApiKey {key}` | SaaS APIs (most common) |
| oauth | `Authorization: Bearer {access_token}` | User-delegated access (Google, GitHub) |
| bearer | `Authorization: Bearer {token}` | JWT or static token auth |

Rule: auth strategy must match API requirements — never guess.

## Endpoint Naming Pattern
- Convention: verb_noun in snake_case
- Examples: `create_charge`, `get_user`, `list_orders`, `delete_subscription`
- Method mapping: create=POST, get=GET, list=GET, update=PUT/PATCH, delete=DELETE

## Error Handling Patterns

| Code Range | Meaning | Retry? |
|-----------|---------|--------|
| 400 | Bad request — invalid params | No (fix input) |
| 401 | Auth failed | Refresh token, retry once |
| 403 | Forbidden — insufficient permissions | No |
| 404 | Not found | No |
| 429 | Rate limited | Yes (backoff per Retry-After) |
| 5xx | Server error | Yes (exponential backoff) |

## Pagination Patterns

| Strategy | How it works | Example APIs |
|----------|-------------|--------------|
| cursor | Token-based, pass `cursor` param | Stripe, Shopify, Slack |
| offset | `offset` + `limit` params | SQL-style, simpler APIs |
| none | All results in one response | Small datasets |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT client |
|------|------------|---------------------|
| connector | Bidirectional service integration | Client is unidirectional only |
| mcp_server | Exposes tools via MCP protocol | Client consumes, never exposes |
| scraper | Extracts from HTML/DOM | Client uses structured API (JSON/XML) |
| cli_tool | Command-line execution | Client is programmatic HTTP calls |
