---
id: p10_lr_client_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "API clients without explicit retry and pagination specs caused 3 categories of production failure: silent data truncation on paginated responses, retry storms on rate-limited endpoints, and credential leaks via unredacted error logs. Each was preventable at spec time."
pattern: "Declare retry strategy (max attempts, backoff, retryable status codes) and pagination strategy (cursor vs offset, page size, terminal condition) explicitly in the spec. Redact auth fields in error logs by default."
evidence: "9 client integrations reviewed: 3 had silent pagination truncation (missing terminal condition), 2 h..."
confidence: 0.7
outcome: SUCCESS
domain: client
tags: [client, retry-strategy, pagination, rate-limiting, auth-redaction]
tldr: "Retry and pagination specs prevent the three most common production client failures: data truncation, retry storms, and credential leaks."
impact_score: 8.0
decay_rate: 0.05
agent_node: edison
keywords: [api client, retry, backoff, pagination, rate limiting, auth, error handling, timeout, serialization]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
An API client spec that omits retry and pagination strategy is a spec for a demo, not a production integration. Both are invisible in happy-path testing and catastrophic at scale. Silent pagination truncation is the most insidious: the client appears to work, returns data, but silently drops records after the first page.
The second most common failure is the retry storm: a client that retries 429 (rate limited) responses immediately and aggressively, converting a temporary rate limit into a permanent ban.
## Pattern
**Explicit retry, pagination, and auth redaction at spec time.**
Retry strategy declaration:
- max_attempts: 3 (default; reduce to 2 for user-facing latency-sensitive endpoints)
- backoff: exponential with jitter (base 1s, max 30s)
- retryable status codes: [429, 500, 502, 503, 504]
- non-retryable: [400, 401, 403, 404, 422] — these are caller errors, retrying is pointless
- respect Retry-After header when present on 429 responses
Pagination strategy declaration:
- Type: cursor (preferred for large datasets) or offset (acceptable for small, stable datasets)
- Page size: explicit default + max (e.g., default 100, max 1000)
- Terminal condition: explicit (null next_cursor, empty data array, total_count reached)
- Never assume the first response is the complete response
Auth redaction:
- All auth fields (api_key, token, bearer) must be masked in error logs and traces
- Log the request shape and response status; never log the Authorization header value
- Timeout default: 30s per request; configurable via environment variable
Endpoint naming: verb_noun snake_case (`create_charge`, `get_user`, `list_orders`). Methods mirror HTTP conventions: GET = read, POST = create, PUT/PATCH = update, DELETE = remove.
## Anti-Pattern
- Omitting pagination handling for endpoints that can return more than one page (guarantees data truncation at scale).
- Retrying 4xx responses (400, 401, 403 are caller errors; retrying them wastes quota and can trigger abuse detection).
- No backoff on retries (linear or no backoff on 429s converts temporary rate limits into bans).
- Hardcoding base_url (environment-specific; must be a config or environment variable).
- Setting auth: none for SaaS APIs that require keys without checking the API documentation.
- Logging the full request including Authorization header (credential leak in log aggregation systems).
- Confusing client with connector: a client is unidirectional (outbound only); a connector is bidirectional with inbound webhook handling.
## Context
The 1024-byte body limit for client is the tightest in P04. Write the endpoint list in frontmatter first, then expand each entry within the remaining budget.
