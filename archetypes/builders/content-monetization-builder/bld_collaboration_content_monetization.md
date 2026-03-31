---
kind: collaboration
id: bld_collaboration_content_monetization
pillar: P12
llm_function: COLLABORATE
purpose: How content-monetization-builder works in crews with other builders
pattern: each builder must know its ROLE, what it RECEIVES and PRODUCES
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
5. api-client-builder          → "Stripe/Hotmart/email provider clients"
6. spawn-config-builder        → "cron: credit refresh, email scheduler, ad sync"
```

### Crew: "Infoproduct Launch"
```
1. content-monetization-builder → "pricing + checkout + course structure"
2. social-publisher-builder     → "launch campaign posts"
3. prompt-template-builder      → "sales page copy + email sequences"
4. formatter-builder            → "landing page template"
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
| knowledge-card-builder | Platform KCs (Stripe, Hotmart) | KC artifact |

| I send to | Data | Format |
|----------|------|--------|
| N02_marketing | Pricing for copy (tier names, features, prices) | Config YAML + signal |
| N04_knowledge | Credit system docs for knowledge base | Architecture .md |
| cli-tool-builder | Checkout + credit pipeline spec | Architecture .md |
| api-client-builder | Provider API specs for client code | Tools .md |
| prompt-template-builder | Email sequence briefs + course outlines | Config YAML |
| spawn-config-builder | Cron schedules (credit refresh, email) | Config .md |

## Nucleus Routing
| Phase | Nucleus | Why |
|-------|---------|-----|
| Monetization design | N03 (engineering) | Architecture + schema work |
| Pricing strategy | N06 (commercial) | Business model expertise |
| Marketing copy | N02 (marketing) | Ad copy, email templates, sales pages |
| Implementation | N05 (operations) | Checkout code, credit API, deploy |
| Knowledge docs | N04 (knowledge) | Platform KCs, credit system docs |

## Relationship to Social Publisher
```
Content Monetization (PRICING)      Social Publisher (AWARENESS)
  price → checkout → deliver  →→→    generate → schedule → publish
  N06_commercial                     N02_marketing
  Billing + Credits + Courses        Calendar + API + Rotation
```
Together: MONETIZE content → PROMOTE via social → CONVERT via checkout → RETAIN via email.
