---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for connector production
sources: Integration patterns, EAI standards, real connector examples
---

# Domain Knowledge: connector

## Foundational Concept
A connector artifact defines a BIDIRECTIONAL INTEGRATION CONTRACT with an external
service. Unlike a client (request/response only), a connector can both SEND and RECEIVE
data — handling webhooks, event streams, two-way sync, and push/pull patterns. Connectors
are the bridge layer between the CEX runtime and external services that require mutual
data exchange.

## Protocol Patterns

| Protocol | Direction | Use Case |
|----------|-----------|----------|
| rest | request + webhook | Most SaaS APIs with webhook callbacks |
| websocket | full-duplex | Real-time data (chat, prices, events) |
| grpc | bidirectional stream | Microservice-to-microservice, high throughput |
| mqtt | pub/sub | IoT, event-driven, lightweight messaging |

Rule: protocol must match the service's integration model — never force REST on a streaming API.

## Integration Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| Request-Webhook | Outbound REST + inbound webhook callback | Stripe payments |
| Event Stream | Subscribe to events, push commands | Slack events API |
| Two-Way Sync | Bidirectional data mirroring | CRM <-> ERP sync |
| Pub-Sub | Publish and subscribe to topics | MQTT IoT devices |

## Data Mapping Concepts
- Transform: field renaming, type coercion, format conversion between systems
- Mapping direction: inbound (external->CEX), outbound (CEX->external)
- Schema alignment: ensure field types match between source and destination
- Idempotency: inbound events must be deduplicated by event_id

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT connector |
|------|------------|------------------------|
| client | Unidirectional API consumer | Client only sends requests; connector also receives |
| mcp_server | Exposes tools via MCP protocol | MCP is agent protocol; connector is service integration |
| scraper | Extracts from HTML/DOM | Scraper reads web pages; connector uses structured APIs |
| hook | Pre/post event trigger | Hook is a code callback; connector is a service bridge |
| daemon | Background persistent process | Daemon runs code; connector defines integration spec |

## References
- Enterprise Integration Patterns (Hohpe, Woolf 2003)
- Webhook best practices (stripe.com/docs/webhooks)
- gRPC bidirectional streaming (grpc.io/docs)
