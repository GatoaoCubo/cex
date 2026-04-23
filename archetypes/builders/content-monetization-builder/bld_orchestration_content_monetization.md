---
kind: collaboration
id: bld_collaboration_content_monetization
pillar: P12
llm_function: COLLABORATE
purpose: How content-monetization-builder works in crews with other builders
pattern: each builder must know its ROLE, what it RECEIVES and PRODUCES
quality: 9.2
title: "Collaboration Content Monetization"
version: "1.0.0"
author: n03_builder
tags: [content_monetization, builder, examples]
tldr: "Golden and anti-examples for content monetization construction, demonstrating ideal structure and common pitfalls."
domain: "content monetization construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_architecture_content_monetization
  - bld_collaboration_research_pipeline
  - bld_collaboration_social_publisher
  - content-monetization-builder
  - p03_sp_content_monetization_builder
  - bld_architecture_kind
  - bld_knowledge_card_content_monetization
  - bld_collaboration_builder
  - bld_instruction_content_monetization
  - kc_intent_resolution_map
---

# Collaboration: content-monetization-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how do we price, bill, package credits, sell
courses, run ads, and send emails for this content business end-to-end?"
I do not write marketing copy. I do not implement payment APIs. I do not deploy services.
I produce monetization architecture + config schema so downstream builders implement and deploy.

## Crew Compositions

### Crew: "Content Monetization End-to-End"
```
1. research-pipeline-builder  → "market intelligence on pricing + competitors"
2. content-monetization-builder → "9-stage monetization config (pricing→deploy)"
3. prompt-template-builder     → "email templates, course descriptions, ad copy briefs"
4. cli-tool-builder            → "checkout orchestrator + credit tracker CLI"
5. api-client-builder          → "Stripe/Hotmart/DS24/email provider clients"
6. spawn-config-builder        → "cron: credit refresh, email scheduler, ad sync"
```

### Crew: "Multi-Platform Launch" (Hotmart BR + DS24 INT)
```
1. research-pipeline-builder    → "platform research: Hotmart+DS24 API, compliance"
2. content-monetization-builder → "dual-platform config: Hotmart(BR) + DS24(INT)"
3. api-client-builder           → "Hotmart webhook (JSON/sha256) + DS24 IPN (form/sha512)"
4. prompt-template-builder      → "copy (PT-BR + EN/DE), email sequences"
5. cli-tool-builder             → "checkout router (geo-detect → provider)"
```

### Crew: "Infoproduct Launch"
```
1. content-monetization-builder → "pricing + checkout + course structure"
2. social-publisher-builder     → "launch campaign posts"
3. prompt-template-builder      → "sales page copy + email sequences"
```

### Crew: "SaaS Credit System"
```
1. content-monetization-builder → "credit economics + tier pricing"
2. api-client-builder           → "usage metering API"
3. db-connector-builder         → "credit ledger schema"
4. notifier-builder             → "low-credit alerts"
```

## Handoff Protocol
| I receive from | Data | Format |
|---------------|------|--------|
| User / N07 | Monetization requirements | Mission handoff .md |
| research-pipeline-builder | Competitor pricing data | JSON + signal |
| knowledge-card-builder | Platform KCs (Hotmart API, DS24 API, compliance) | KC artifact |
| N01_intelligence | Platform research (kc_hotmart_*, kc_digistore24_*, kc_content_platform_*) | 8 KCs |

| I send to | Data | Format |
|----------|------|--------|
| N02_marketing | Pricing for copy (tier names, features, prices, both currencies) | Config YAML + signal |
| N04_knowledge | Credit system + multi-platform docs for knowledge base | Architecture .md |
| cli-tool-builder | Dual checkout pipeline spec (Hotmart JSON + DS24 form-encoded) | Architecture .md |
| api-client-builder | Provider API specs: Hotmart REST + DS24 REST + IPN handler | Tools .md |
| prompt-template-builder | Email sequence briefs + course outlines (PT-BR + EN/DE) | Config YAML |
| spawn-config-builder | Cron schedules (credit refresh, email, webhook health check) | Config .md |

## Nucleus Routing
| Phase | Nucleus | Why |
|-------|---------|-----|
| Monetization design | N03 (engineering) | Architecture + schema work |
| Pricing strategy | N06 (commercial) | Business model expertise |
| Marketing copy | N02 (marketing) | Ad copy, email templates, sales pages |
| Implementation | N05 (operations) | Checkout code, credit API, deploy |
| Knowledge docs | N04 (knowledge) | Platform KCs, credit system docs |

## Relationship to Social Publisher
MONETIZE (this) → PROMOTE (social-publisher) → CONVERT (checkout) → RETAIN (email).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_content_monetization]] | upstream | 0.46 |
| [[bld_collaboration_research_pipeline]] | sibling | 0.45 |
| [[bld_collaboration_social_publisher]] | sibling | 0.43 |
| [[content-monetization-builder]] | upstream | 0.39 |
| [[p03_sp_content_monetization_builder]] | upstream | 0.38 |
| [[bld_architecture_kind]] | upstream | 0.32 |
| [[bld_knowledge_card_content_monetization]] | upstream | 0.32 |
| [[bld_collaboration_builder]] | sibling | 0.31 |
| [[bld_instruction_content_monetization]] | upstream | 0.30 |
| [[kc_intent_resolution_map]] | upstream | 0.29 |
