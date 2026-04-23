---
kind: knowledge_card
id: bld_knowledge_card_integration_guide
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for integration_guide production
quality: 9.2
title: "Knowledge Card Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, knowledge_card]
tldr: "Domain knowledge for integration_guide production"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_tools_integration_guide
  - webhook-builder
  - bld_instruction_integration_guide
  - bld_memory_webhook
  - p03_sp_webhook_builder
  - integration-guide-builder
  - bld_collaboration_webhook
  - bld_examples_integration_guide
  - partner-listing-builder
  - hybrid_review6_n03
---

## Domain Overview
Integration_guide artifacts sit in the Diataxis How-To quadrant: goal-oriented, task-driven, assumes competence. They are the top lever for partner ecosystem adoption and paid-tier onboarding. Reference canon includes Auth0 quickstarts (10-minute first-token paths), Stripe integration guides (code in five languages, copy-paste-run), Salesforce AppExchange certification deliverables, and Slack app directory submission checklists.

A good integration_guide answers four questions in order: (1) which auth flow? (2) which transport -- webhook vs polling vs streaming? (3) which SDK or raw HTTP? (4) how do I verify the integration works end-to-end? Guides that bury these under marketing prose lose developers at first scroll.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| Diataxis How-To | Task-oriented doc quadrant (vs tutorial/reference/explanation) | Daniele Procida, diataxis.fr |
| Quickstart | <10 min first-successful-call path | Auth0, Stripe, Twilio |
| Deep-dive | Full-surface-area reference integration | Auth0, Okta |
| OAuth 2.1 | Consolidated IETF auth framework | IETF draft-ietf-oauth-v2-1 |
| OIDC | Identity layer over OAuth 2.0 | OpenID Foundation |
| SAML 2.0 | Enterprise SSO XML assertion standard | OASIS |
| Webhook | Server-push event delivery | GitHub, Stripe, Shopify patterns |
| Polling | Client-pull state reconciliation | REST sync loops |
| Idempotency key | Dedupe retry-safe operations | Stripe-Idempotency-Key header |
| Partner certification | Platform-gated quality review | AppExchange, Slack directory |

## Industry Standards
- Diataxis framework (How-To quadrant for task-oriented guides)
- OAuth 2.1 (IETF draft-ietf-oauth-v2-1) and OIDC (OpenID Foundation)
- SAML 2.0 (OASIS) for enterprise SSO
- OpenAPI 3.1 (contract reference and code generation)
- AsyncAPI 2.6 (event-driven API contracts)
- Webhook Events specification (webhooks.fyi canonical patterns)
- Salesforce AppExchange Partner Security Review
- Slack app directory review requirements
- Microsoft Partner Center certification
- Stripe integration style guide (dual-code blocks, language tabs)

## Common Patterns
1. Open with the 10-line quickstart; defer theory.
2. Show both webhook and polling paths with trade-off table (latency vs reliability vs cost).
3. Provide a language-tabbed code block (Node / Python / Go / Ruby minimum).
4. Include idempotency-key example for retry-safe mutations.
5. Close with an end-to-end verification checklist and observability tips.
6. Link to partner certification checklist for ecosystem submissions.

## Pitfalls
- Explanation-first prose (violates Diataxis How-To contract; belongs in reference doc).
- Only one auth flow documented -- blocks enterprise SSO deals.
- No webhook-vs-polling trade-off -- developers pick wrong transport for workload.
- Missing idempotency guidance -- duplicate charges or double-writes in production.
- No E2E verification step -- silent integrations look fine until prod traffic hits.
- Quickstart buried below marketing -- developers bounce before first token.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_integration_guide]] | downstream | 0.37 |
| [[webhook-builder]] | downstream | 0.24 |
| [[bld_instruction_integration_guide]] | downstream | 0.22 |
| [[bld_memory_webhook]] | downstream | 0.22 |
| [[p03_sp_webhook_builder]] | downstream | 0.21 |
| [[integration-guide-builder]] | downstream | 0.20 |
| [[bld_collaboration_webhook]] | downstream | 0.20 |
| [[bld_examples_integration_guide]] | downstream | 0.20 |
| [[partner-listing-builder]] | downstream | 0.19 |
| [[hybrid_review6_n03]] | sibling | 0.19 |
