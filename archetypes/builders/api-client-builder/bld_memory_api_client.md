---
id: p10_lr_client_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: builder_agent
observation: "API clients without explicit retry and pagetion specs caused 3 categories of production failure: silent data truncation on pageted responses, retry storms on rate-limited endpoints, and credential leaks via unredacted error logs. Each was preventable at spec time."
pattern: "Declare retry strategy (max attempts, backoff, retryable status codes) and pagetion strategy (cursor vs offset, page size, terminal condition) explicitly in the spec. Redact auth fields in error logs by default."
evidence: "9 client integrations reviewed: 3 had silent pagetion truncation (missing terminal condition), 2 h..."
confidence: 0.7
outcome: SUCCESS
domain: client
tags: [client, retry-strategy, pagetion, rate-limiting, auth-redaction]
tldr: "Retry and pagetion specs prevent the three most common production client failures: data truncation, retry storms, and credential leaks."
impact_score: 8.0
decay_rate: 0.05
agent_group: edison
keywords: [api client, retry, backoff, pagetion, rate limiting, auth, error handling, timeout, serialization]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Api Client"
density_score: 0.90
llm_function: INJECT
---
## Summary
An API client spec that omits retry and pagetion strategy is a spec for a demo, not a production integration. Both are invisible in happy-path testing and catastrophic at scale. Silent pagetion truncation is the most insidious: the client appears to work, returns data, but silently drops records after the first page.
The second most common failure is the retry storm: a client that retries 429 (rate limited) responses immediately and aggressively, converting a temporary rate limit into a permanent ban.
## Pattern
**Explicit retry, pagetion, and auth redaction at spec time.**
Retry strategy declaration:
1. max_attempts: 3 (default; reduce to 2 for user-facing latency-sensitive endpoints)
2. backoff: exponential with jitter (base 1s, max 30s)
3. retryable status codes: [429, 500, 502, 503, 504]
4. non-retryable: [400, 401, 403, 404, 422] — these are caller errors, retrying is pointless
5. respect Retry-After header when present on 429 responses
Pagination strategy declaration:
1. Type: cursor (preferred for large datasets) or offset (acceptable for small, stable datasets)
2. Page size: explicit default + max (e.g., default 100, max 1000)
3. Terminal condition: explicit (null next_cursor, empty data array, total_count reached)
4. Never assume the first response is the complete response
Auth redaction:
1. All auth fields (api_key, token, bearer) must be masked in error logs and traces
2. Log the request shape and response status; never log the Authorization header value
3. Timeout default: 30s per request; configurable via environment variable
Endpoint naming: verb_noun snake_case (`create_charge`, `get_user`, `list_orders`). Methods mirror HTTP conventions: GET = read, POST = create, PUT/PATCH = update, DELETE = remove.
## Anti-Pattern
1. Omitting pagetion handling for endpoints that can return more than one page (guarantees data truncation at scale).
2. Retrying 4xx responses (400, 401, 403 are caller errors; retrying them wastes quota and can trigger abuse detection).
3. No backoff on retries (linear or no backoff on 429s converts temporary rate limits into bans).
4. Hardcoding base_url (environment-specific; must be a config or environment variable).
5. Setting auth: none for SaaS APIs that require keys without checking the API documentation.
6. Logging the full request including Authorization header (credential leak in log aggregation systems).
7. Confusing client with connector: a client is unidirectional (outbound only); a connector is bidirectional with inbound webhook handling.
## Context
The 1024-byte body limit for client is the tightest in P04. Write the endpoint list in frontmatter first, then expand each entry within the remaining budget.

## Metadata

```yaml
id: p10_lr_client_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-client-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | client |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
