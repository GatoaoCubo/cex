---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: connector-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p04_conn_stripe not p04_conn_stripe-api)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. endpoints list not matching ## Endpoints section names exactly (S03 drift)
4. Missing direction annotation on endpoints (inbound/outbound required per S04)
5. Confusing connector with client (connector is bidirectional, client is unidirectional)
6. Including implementation code in body (this is a spec, not source)
7. Missing ## Data Mapping section (required — H07 checks all 4 sections)
8. No health_check defined (connectors must be monitorable)
9. Using protocol: rest for a pure streaming service (should be websocket or grpc)
10. Missing idempotency strategy for inbound webhooks (critical for dedup)

### Integration Patterns
| Pattern | Protocol | Direction | Example |
|---------|----------|-----------|---------|
| Request-Webhook | rest | outbound + inbound | Stripe, Shopify |
| Event Stream | websocket | full-duplex | Slack, Discord |
| Two-Way Sync | rest | outbound + inbound | CRM <-> ERP |
| Pub-Sub | mqtt | publish + subscribe | IoT devices |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | direction annotation, mapping rules, idempotency |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a connector, update:
- New common mistake (if encountered)
- New integration pattern (if discovered)
- Production counter increment
