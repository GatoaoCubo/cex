---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: connector Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_conn_{service_slug}.md` + `.yaml` | `p04_conn_stripe.md` |
| Builder directory | kebab-case | `connector-builder/` |
| Frontmatter fields | snake_case | `health_check`, `rate_limit` |
| Service slug | snake_case, lowercase, no hyphens | `stripe`, `slack`, `bling_erp` |
| Endpoint names | snake_case, verb_noun or receive_noun | `push_order`, `receive_webhook` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P04_tools/examples/p04_conn_{service_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_conn_{service_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80 (no filler)

## Protocol Enum

| Value | When to use |
|-------|-------------|
| rest | HTTP request/response + webhook callbacks (most common) |
| websocket | Full-duplex real-time data exchange |
| grpc | High-throughput bidirectional streaming between services |
| mqtt | Lightweight pub/sub (IoT, event-driven) |

## Auth Enum

| Value | When to use |
|-------|-------------|
| none | Internal services with network-level trust only |
| api_key | Static key in header (most common for SaaS) |
| oauth | OAuth 2.0 flow for user-delegated access |
| bearer | JWT or static token in Authorization header |
| hmac | Webhook signature verification (inbound auth) |

## Logging Enum

| Value | When to use |
|-------|-------------|
| structured | JSON logs with fields (default, recommended) |
| plaintext | Simple text logs (legacy systems) |
| none | No logging (sensitive data, minimal footprint) |
