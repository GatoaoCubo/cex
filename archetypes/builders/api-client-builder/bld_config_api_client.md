---
kind: config
id: bld_config_client
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: client Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_client_{api_slug}.md` + `.yaml` | `p04_client_stripe.md` |
| Builder directory | kebab-case | `api-client-builder/` |
| Frontmatter fields | snake_case | `base_url`, `rate_limit` |
| API slug | snake_case, lowercase, no hyphens | `stripe`, `openai`, `railway` |
| Endpoint names | snake_case, verb_noun pattern | `create_charge`, `list_users` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_client_{api_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_client_{api_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Auth Enum
| Value | When to use |
|-------|-------------|
| none | Internal APIs with network-level trust only |
| api_key | Static key in header (most common for SaaS APIs) |
| oauth | OAuth 2.0 flow for user-delegated access |
| bearer | JWT or token in Authorization: Bearer header |
## Serialization Enum
| Value | When to use |
|-------|-------------|
| json | REST APIs (default, most common) |
| xml | Legacy SOAP or XML-based APIs |
| protobuf | gRPC services |
## Pagination Enum
| Value | When to use |
|-------|-------------|
| cursor | Token-based pagination (Stripe, Shopify style) |
| offset | Numeric offset/limit (SQL-style) |
| none | API returns all results or no list endpoints |
