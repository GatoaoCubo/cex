---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: client-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_client_stripe not p04_client_stripe-api)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. endpoints list not matching ## Endpoints section names exactly (S03 drift)
4. Missing base_url field (required — cannot connect without it)
5. Setting auth: none for public SaaS APIs that require keys (check API docs)
6. Including implementation code in body (this is a spec, not source)
7. Writing endpoint entries without method or path (S04 incomplete)
8. Exceeding 1024 bytes body limit (client is compact — tightest P04 limit)
9. Confusing client with connector (client is unidirectional, connector is bidirectional)
10. Omitting error_codes and retry strategy (## Error Handling section required)

### Effective Patterns
- Endpoint naming: verb_noun snake_case — `create_charge`, `get_user`, `list_orders`
- Auth selection: check API docs first; most SaaS = api_key, user-delegated = oauth
- endpoints mirror: write the list in frontmatter FIRST, then expand each in body
- Overview pattern: "Consumes {api} REST API for {capability}. Used by {consumer}."
- Body budget: Overview(80B) + Endpoints(600B) + Auth(150B) + Errors(150B) = ~980B

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | id hyphens, endpoints drift, missing base_url |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a client, update:
- New common mistake (if encountered)
- New effective pattern (if discovered)
- Production counter increment
