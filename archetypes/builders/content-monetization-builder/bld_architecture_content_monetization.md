---
kind: architecture
id: bld_architecture_content_monetization
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of content monetization — 9 stages, billing→credits→courses→ads→email
---

# Architecture: content_monetization in the CEX

## 9-Stage Pipeline
```
CONTENT → S1 PARSE (inventory assets)
  → S2 PRICING (tiers + margins)
  → S3 CREDITS (pipeline cost mapping)
  → S4 CHECKOUT (provider + webhook)
  → S5 COURSES (modules + certification)
  → S6 ADS (campaigns + ROI)
  → S7 EMAILS (sequences + triggers)
  → S8 VALIDATE (margin check + webhook test)
  → S9 DEPLOY (mock → production)
```

## Data Flow
```
config ──► parser ──► pricing_engine
                          │
                    ┌─────┼──────┐
                    ▼     ▼      ▼
              credits  checkout  courses
                    │     │      │
                    └──┬──┘──────┘
                       ▼
                 ┌─────┴─────┐
                 ▼           ▼
            ad_campaign  email_seq
                 │           │
                 └─────┬─────┘
                       ▼
                  validation ──► deploy
```

## Component Inventory
| Component | Stage | Dependencies | External |
|-----------|-------|-------------|----------|
| asset_parser | S1 | config.yaml | none |
| pricing_engine | S2 | asset catalog, market data | none |
| credit_mapper | S3 | pricing tiers, pipeline costs | LLM cost API |
| pack_generator | S3 | credit map, margin floor | none |
| checkout_integrator | S4 | provider SDK | Stripe/Hotmart/Kiwify API |
| webhook_handler | S4 | checkout events | HTTP endpoint |
| course_builder | S5 | content assets | LMS platform |
| module_renderer | S5 | course structure | template engine |
| ad_campaign | S6 | budget, audience | Meta/Google Ads API |
| email_sequencer | S7 | triggers, templates | Resend/SendGrid API |
| validation_engine | S8 | full config | all providers (mock) |
| deploy_cutover | S9 | validated config | production env |

## Dependency Graph
```
knowledge_card ──produces──► content_monetization ──consumed_by──► checkout_flow
research_pipeline ──feeds──► content_monetization ──consumed_by──► email_automation
social_publisher ──feeds──► content_monetization ──consumed_by──► ad_campaign
prompt_template ──produces──► content_monetization ──consumed_by──► course_platform
```

## Position in CEX
| Layer | Location |
|-------|----------|
| Template + Examples | P04_tools/{templates,examples}/ |
| Nucleus instance | N06_commercial/{tools,knowledge,orchestration}/ |
| Company config | _instances/{co}/N06_commercial/ |

## Boundary Table
| This Builder | Other Builder |
|-------------|---------------|
| Pricing strategy + config schema | Python checkout code → cli-tool-builder |
| Credit system design | Credit API implementation → api-client-builder |
| Course structure + modules | Course platform deployment → spawn-config-builder |
| Ad campaign architecture | Ad copy + creatives → social-publisher-builder |
| Email sequence triggers | Email template copy → prompt-template-builder |
| Margin validation logic | Accounting/ERP integration → db-connector-builder |
