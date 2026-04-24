---
id: p01_kc_external_integrations
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "External Integrations — API Clients, Webhooks, Notifications, DB Connectors, Browser Automation"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: integrations
origin: manual
quality: 9.1
tags: [api, webhook, notification, database, browser, rest, graphql, playwright, connector]
tldr: "External integrations bridge agent systems to the outside world via API clients, webhooks, notification channels, database connectors, and browser automation tools"
when_to_use: "Building or classifying any component that communicates with external services, databases, or browsers"
keywords: [api_client, webhook, notifier, db_connector, browser_tool, rest, graphql, playwright]
long_tails:
  - "How to map API client wrappers to CEX api_client kind"
  - "Which webhook event models map to CEX webhook kind"
  - "How browser automation tools like Playwright map to browser_tool kind"
axioms:
  - "Every external call must have timeout, retry, and error propagation — never fire-and-forget"
  - "Webhooks are event-driven inbound triggers; API clients are request-driven outbound calls"
  - "Database connectors abstract connection pooling, migrations, and query building behind a uniform interface"
linked_artifacts:
  primary: null
  related: [p01_kc_mcp_protocol, p01_kc_langchain_patterns, p01_kc_routing_resilience]
feeds_kinds:
  - api_client       # REST/GraphQL wrappers, SDK clients, HTTP adapters
  - webhook          # Inbound event receivers, signature verification, payload routing
  - notifier         # Slack, email, SMS, push notification dispatchers
  - db_connector     # PostgreSQL, Redis, SQLite adapters, connection pools, ORMs
  - browser_tool     # Playwright, Puppeteer, Selenium automation, screenshot capture
density_score: 0.87
related:
  - bld_collaboration_webhook
  - webhook-builder
  - p03_sp_webhook_builder
  - p01_kc_webhook
  - bld_architecture_notifier
  - bld_architecture_webhook
  - p01_kc_api_client
  - notifier-builder
  - p01_kc_notifier
  - p01_kc_browser_tool
---

# External Integrations

## Quick Reference
```yaml
topic: External Integration Patterns
scope: API clients, webhooks, notifications, DB connectors, browser automation
source: cross-domain (REST/GraphQL specs, DB driver docs, Playwright docs)
criticality: high
```

## Key Concepts

| Concept | Category | CEX Kind | Role |
|---------|----------|----------|------|
| REST Client | API | api_client | HTTP request/response with JSON serialization |
| GraphQL Client | API | api_client | Query-based API with schema introspection |
| SDK Wrapper | API | api_client | Vendor-specific client (Stripe, Bling, Railway) |
| Webhook Receiver | Event | webhook | Inbound HTTP POST with signature verification |
| Webhook Dispatcher | Event | webhook | Outbound event delivery with retry queue |
| Event Schema | Event | webhook | Typed payload models (Pydantic/Zod) for events |
| Slack Notifier | Notification | notifier | Channel/DM message dispatch via Slack API |
| Email Sender | Notification | notifier | SMTP/API-based email (SendGrid, SES) |
| SMS Gateway | Notification | notifier | Twilio/SNS text message dispatch |
| PG Connector | Database | db_connector | asyncpg/psycopg pool with migration support |
| Redis Adapter | Database | db_connector | Cache/pubsub via redis-py or ioredis |
| ORM Layer | Database | db_connector | SQLAlchemy/Prisma model-to-table mapping |
| Playwright Page | Browser | browser_tool | Headless browser page with navigation/interaction |
| Screenshot Tool | Browser | browser_tool | Visual capture for testing and monitoring |
| Form Filler | Browser | browser_tool | Automated input, selection, and submission |

## Patterns

| Trigger | Action |
|---------|--------|
| Call external REST API | Build `api_client` with base_url, auth header, timeout, retry decorator |
| Receive webhook event | Validate signature -> parse typed payload -> route to handler |
| Send notification | Select channel (slack/email/sms) -> render template -> dispatch with delivery tracking |
| Connect to database | Create connection pool -> run migrations -> expose query interface |
| Automate browser task | Launch headless browser -> navigate -> interact -> capture result/screenshot |
| Handle API rate limits | Implement exponential backoff with jitter, respect Retry-After headers |

## Anti-Patterns

- Making external calls without timeouts — risks hanging the entire pipeline
- Trusting webhook payloads without signature verification (HMAC/SHA256)
- Hardcoding connection strings instead of using environment variables
- Opening new DB connections per request instead of using a pool
- Running browser automation in headed mode in CI/production
- Swallowing HTTP errors silently instead of propagating typed exceptions

## CEX Mapping

```text
[api_client -> webhook] -> [notifier] -> delivery
[db_connector] -> query/mutation -> [api_client] -> external service
[browser_tool] -> navigate -> interact -> [api_client] -> report results
```

## References

- source: REST (RFC 7231), GraphQL (graphql.org/spec), Playwright (playwright.dev)
- related: p01_kc_mcp_protocol, p01_kc_a2a_protocol

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_webhook]] | downstream | 0.47 |
| [[webhook-builder]] | downstream | 0.43 |
| [[p03_sp_webhook_builder]] | downstream | 0.39 |
| [[p01_kc_webhook]] | sibling | 0.39 |
| [[bld_architecture_notifier]] | downstream | 0.35 |
| [[bld_architecture_webhook]] | downstream | 0.35 |
| [[p01_kc_api_client]] | sibling | 0.35 |
| [[notifier-builder]] | downstream | 0.33 |
| [[p01_kc_notifier]] | sibling | 0.33 |
| [[p01_kc_browser_tool]] | sibling | 0.32 |
