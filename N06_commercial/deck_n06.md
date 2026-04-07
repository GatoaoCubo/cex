---
id: deck_n06
kind: context_doc
title: "N06 Deck -- Available Capabilities"
pillar: P01
nucleus: N06
sin: Avareza Estrategica
version: 1.0.0
quality: null
created: 2026-04-07
---

## Identity

| Field | Value |
|-------|-------|
| Sin | Avareza Estrategica (Strategic Greed) |
| Role | Commercial & Monetization Nucleus |
| Domain | Pricing strategy, online courses, sales funnels, conversion, revenue models |
| Optimize for | Conversion and customer lifetime value |
| CLI | Claude (Opus 4.6, 1M context) |
| Route TO N06 | Pricing, courses, sales funnels, monetization, conversion, revenue, brand strategy |
| Route AWAY | Research (N01), marketing copy (N02), build artifacts (N03), deploy/test (N05) |

## My Artifacts

| Subdir | Count | Purpose |
|--------|-------|---------|
| knowledge | 12 | Brand archetypes, naming, voice, monetization models, competitive positioning, ICP frameworks |
| output | 15 | Brand book, pricing page, business plans, competitive maps, discovery reports, visual identity |
| prompts | 6 | Brand discovery interview, audit, config extractor, commercial system/template prompts |
| orchestration | 4 | Dispatch rules + workflows for commercial and content monetization |
| schemas | 4 | Brand audit, brand book, brand config, brand voice contract |
| compiled | 19 | YAML compiled versions of all source artifacts |
| agents | 1 | agent_commercial.md |
| architecture | 1 | agent_card_commercial.md |
| feedback | 1 | quality_gate_commercial.md |
| quality | 1 | scoring_rubric_commercial.md |
| tools | 1 | content_monetization_tool.md (full pipeline: pricing > credits > checkout > courses > ads > email) |
| memory | 0 | **EMPTY** -- no commercial memory persisted yet |
| **Total** | **67** | **48 .md source + 19 .yaml compiled** |

## Kinds I Build

### Core Domain (N06 primary)

| Kind | Pillar | Naming Pattern | Description |
|------|--------|----------------|-------------|
| content_monetization | P04 | p04_cm_{{name}}.md | Config-driven monetization pipeline (parse > pricing > credits > checkout > courses) |
| reward_signal | P11 | p11_reward_{{metric}}.md | Continuous quality/revenue signals |
| tagline | P03 | p03_tl_{{topic}}.md | Brand taglines, slogans, headlines |
| model_card | P02 | p02_mc_{{model}}.md + .yaml | LLM specs with pricing and capabilities |

### P11 Governance (N06 builds for commercial contexts)

| Kind | Pillar | Naming Pattern | Description |
|------|--------|----------------|-------------|
| bugloop | P11 | p11_bl_{{scope}}.md + .yaml | Correction cycles for commercial pipeline bugs |
| guardrail | P11 | p11_gr_{{scope}}.yaml | Safety boundaries for pricing/checkout flows |
| lifecycle_rule | P11 | p11_lc_{{rule}}.yaml | Freshness, archive, promote rules for commercial content |
| optimizer | P11 | p11_opt_{{target}}.md + .yaml | Revenue/conversion optimizers |
| quality_gate | P11 | p11_qg_{{gate}}.yaml | Commercial quality barriers (pricing accuracy, compliance) |

### P06 Validation (N06 builds for commercial schemas)

| Kind | Pillar | Naming Pattern | Description |
|------|--------|----------------|-------------|
| enum_def | P06 | p06_enum_{{name}}.md | Enumerations for pricing tiers, plan types, statuses |
| input_schema | P06 | p06_is_{{scope}}.yaml | Input validation for checkout, pricing API calls |
| interface | P06 | p06_iface_{{contract}}.yaml | Contracts for payment/monetization integrations |
| type_def | P06 | p06_td_{{type}}.yaml | Type definitions for commerce data models |
| validation_schema | P06 | p06_vs_{{scope}}.yaml | Schema validation for pricing configs, product catalogs |
| validator | P06 | p06_val_{{rule}}.yaml | Business rule validators (margin checks, tier logic) |

**Total: 15 kinds (4 core + 5 P11 + 6 P06)**

## Tools I Use

| Tool | Purpose |
|------|---------|
| cex_8f_runner.py | Full 8F pipeline execution for commercial artifacts |
| cex_compile.py | .md to .yaml compilation after every save |
| cex_crew_runner.py | Prompt composer: load ISOs + memory + brand context |
| cex_score.py | Peer review scoring (quality assignment) |
| cex_feedback.py | Quality tracking + archive + metrics |
| cex_retriever.py | TF-IDF similarity search across 2184 docs |
| cex_query.py | Builder discovery for commercial intents |
| cex_gdp.py | Guided Decision Protocol -- manifest I/O for pricing/brand decisions |
| cex_evolve.py | Autonomous artifact improvement loop |
| cex_prompt_layers.py | Load 15+ pillar artifacts into prompts |
| cex_bootstrap.py | Brand setup (first-run brand_config.yaml) |
| cex_notebooklm.py | Content pipeline to NotebookLM (9 content types) |
| brand_inject.py | Replace {{BRAND_*}} placeholders in templates |
| brand_validate.py | Validate brand_config.yaml (13 required fields) |
| brand_propagate.py | Push brand context to all nuclei |
| brand_audit.py | Score brand consistency (6 dimensions) |
| brand_ingest.py | Scan user folders to extract brand signals |
| signal_writer.py | Signal completion to N07 orchestrator |

**Total: 18 tools**

## MCP Servers

Source: `.mcp-n06.json`

| Server | Purpose | Auth |
|--------|---------|------|
| stripe | Payment processing -- subscriptions, checkout, invoices | STRIPE_SECRET_KEY |
| hotmart | Course platform -- products, sales, commissions, club | HOTMART_CLIENT_ID + SECRET + BASIC_AUTH |
| canva | Design -- brand assets, visual identity, social graphics | CANVA_CLIENT_ID + SECRET |
| notebooklm | Content generation -- 9 content types from KCs | None |
| fetch | Web fetching -- competitor research, pricing pages | None |
| markitdown | Document conversion -- ingest PDFs, docs for analysis | None |

**Total: 6 MCP servers**

## Platform Knowledge Cards Available

17 commerce-relevant KCs in `P01_knowledge/library/platform/`:

| KC | Domain |
|----|--------|
| kc_pricing_strategy.md | Pricing models, tiers, psychology |
| kc_stripe_patterns.md | Stripe API, checkout, subscriptions |
| kc_hotmart_marketplace.md | Hotmart products, affiliates |
| kc_hotmart_club.md | Hotmart member areas, courses |
| kc_hotmart_api.md | Hotmart API integration patterns |
| kc_digistore24_marketplace.md | Digistore24 products, EU market |
| kc_digistore24_api.md | Digistore24 API integration |
| kc_digistore24_ipn.md | Digistore24 IPN webhooks, payment notifications |
| kc_mercadopago_pix.md | MercadoPago PIX payments (BR) |
| kc_credit_system_design.md | Credit-based monetization |
| kc_content_platform_comparison.md | Platform feature matrix |
| kc_content_platform_compliance.md | Legal/compliance per platform |
| kc_course_generation.md | Course structure, curriculum |
| kc_email_automation.md | Email sequences, drip campaigns |
| kc_ad_validation.md | Ad compliance, creative validation |
| kc_erp_integration.md | ERP/accounting integration |
| kc_supabase_pricing.md | Supabase cost modeling |

## Agent Definitions

8 agents in `.claude/agents/` relevant to N06:

| Agent | File | Domain |
|-------|------|--------|
| content-monetization-builder | content-monetization-builder.md | Monetization pipelines |
| tagline-builder | tagline-builder.md | Brand taglines, slogans |
| landing-page-builder | landing-page-builder.md | Conversion-optimized pages |
| model-card-builder | model-card-builder.md | LLM pricing/capability specs |
| supabase-data-layer-builder | supabase-data-layer-builder.md | Commerce data infrastructure |
| guardrail-builder | guardrail-builder.md | Pricing/checkout safety boundaries |
| quality-gate-builder | quality-gate-builder.md | Commercial quality barriers |
| reward-signal-builder | reward-signal-builder.md | Revenue/conversion signals |

18 builder archetypes in `archetypes/builders/` (13 ISOs each):

**Core commerce** (5): content-monetization, tagline, landing-page, model-card, supabase-data-layer
**P11 governance** (7): bugloop, guardrail, lifecycle-rule, optimizer, quality-gate, reward-signal, output-validator
**P06 validation** (6): enum-def, input-schema, interface, type-def, validation-schema, validator

## My Strengths

1. **Brand intelligence depth** -- 12 KCs covering archetypes, naming, voice, monetization models, competitive positioning, ICP frameworks
2. **Rich output portfolio** -- 15 deliverables spanning brand books, pricing pages, business plans, competitive maps, visual identity
3. **Full monetization pipeline** -- content_monetization_tool.md covers parse > pricing > credits > checkout > courses > ads > email
4. **Multi-payment integration** -- Stripe (global), Hotmart (BR/LATAM), MercadoPago PIX (BR), Digistore24 (EU)
5. **Brand lifecycle** -- Discovery interview > config extraction > audit > propagation > visual identity
6. **Platform intelligence** -- 17 platform KCs with deep integration knowledge
7. **Design tooling** -- Canva MCP for brand asset generation
8. **Content amplification** -- NotebookLM MCP for 9 content types from any KC

## My Gaps

| Gap | Severity | What's Missing |
|-----|----------|----------------|
| memory/ | HIGH | 0 artifacts -- no commercial memory persisted across sessions |
| tools/ | MEDIUM | Only 1 tool definition -- need pricing calculator, ROI estimator, funnel validator |
| Course artifacts | MEDIUM | KC exists (kc_course_generation) but no built course_structure outputs |
| Funnel artifacts | MEDIUM | No sales funnel templates, sequences, or conversion tracking configs |
| Pricing model kind | LOW | No dedicated pricing_model kind in kinds_meta.json -- using output_ files instead |
| P06 schemas | LOW | Only 4 brand-focused schemas in schemas/ -- P06 kinds (enum, input_schema, validator) can fill this |

## Cards in My Deck

| Category | Count |
|----------|-------|
| Source artifacts (.md) | 48 |
| Compiled artifacts (.yaml) | 19 |
| Kinds I build | 15 |
| CEX tools I use | 18 |
| MCP servers | 6 |
| Platform KCs (commerce-relevant) | 17 |
| Agent definitions | 8 |
| Builder archetypes (core commerce) | 5 |
| Builder archetypes (P11 governance) | 7 |
| Builder archetypes (P06 validation) | 6 |
| Brand KCs (in-nucleus) | 12 |
| **Total cards in deck** | **161** |
