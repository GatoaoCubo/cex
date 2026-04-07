---
id: brand_context_n05
kind: config
pillar: P09
title: Brand Context for N05
version: 2.0.0
created: 2026-04-01
updated: 2026-04-07
author: n04_knowledge
quality: 9.1
tags: [brand, context, n05, operations, infrastructure, payments]
tldr: "Brand context for N05 Operations — infrastructure endpoints, payment integrations, deployment standards, monitoring, and operational constraints for GATO³ hybrid commerce."
density_score: 0.95
---

# Brand Context — N05 Operations

> Source: `.cex/brand/brand_config.yaml`
> Nucleus: N05 (Operations/Code/Test/Deploy)
> Domain: Infrastructure, CI/CD, monitoring, payments, deployment

## Core Brand Identity

| Field | Value |
|-------|-------|
| **Brand** | GATO³ (Gato ao Cubo) |
| **Model** | Hybrid (B2C direto + B2B revenda + marketplaces) |
| **Currency** | BRL |
| **Language** | pt-BR |
| **HQ** | São Caetano do Sul - SP, 09581-030 |

## Infrastructure Endpoints

| Service | URL | Purpose |
|---------|-----|---------|
| E-commerce | `https://gato3.com.br` | Shopify storefront |
| Logo | `https://gato3.com.br/logo.svg` | Brand mark (SVG) |
| Favicon | `https://gato3.com.br/favicon.ico` | Browser tab icon |
| API (future) | `https://api.gato3.com.br` | Backend services |

## Payment & Commerce

### Payment Providers

| Provider | Channel | Use Case |
|----------|---------|----------|
| Shopify Payments | gato3.com.br | Primary checkout (credit/debit) |
| MercadoPago | ML + Shopee | Marketplace escrow |
| PIX | All channels | Instant payment (preferred by ICP) |

### Pricing Model
- **Type**: Hybrid — multiple tiers
- **Price anchor**: R$ 30-80 (camas, tapetes gelados, brinquedos interativos)
- **Tiers**: b2c-direto, b2c-local, b2b-revenda, marketplace-ml, marketplace-shopee

### Revenue Channels

| Tier | Channel | Margin Profile |
|------|---------|----------------|
| b2c-direto | gato3.com.br | Highest (no commission) |
| b2c-local | Entrega ABC | High (local logistics) |
| b2b-revenda | Pet shops, clínicas | Medium (volume discount) |
| marketplace-ml | Mercado Livre | Lower (16-19% commission) |
| marketplace-shopee | Shopee | Lower (12-18% commission) |

## N05 Operations Guidelines

### Deployment Standards
1. **Environment parity**: Staging must mirror production (Shopify theme structure)
2. **Feature flags**: Use Shopify metafields for A/B tests, not code branches
3. **Rollback**: Every deploy must have 1-click rollback capability
4. **Monitoring**: Uptime checks on `gato3.com.br` every 5 minutes

### Testing Requirements

| Type | Coverage | Tools |
|------|----------|-------|
| Unit tests | ≥80% business logic | pytest, jest |
| Integration | Payment flows (PIX, card, ML) | Sandbox environments |
| E2E | Critical user paths (browse → cart → checkout) | Playwright |
| Accessibility | WCAG 2.1 AA | axe-core, Lighthouse |
| Performance | LCP < 2.5s, FID < 100ms, CLS < 0.1 | Web Vitals |

### Operational Constraints
- **Data residency**: All PII stays in Brazil (LGPD compliance)
- **Backup cadence**: Daily Shopify export + weekly full backup
- **Incident response**: < 15 min acknowledgment for payment failures
- **Encoding**: UTF-8 strict (no cp1252 — critical for pt-BR diacritics)
- **Timezone**: America/Sao_Paulo (UTC-3)

### Security Baseline
- HTTPS everywhere (no mixed content)
- API keys in environment variables, never in code
- Shopify webhook verification (HMAC)
- MercadoPago IPN signature validation
- PIX QR code generation server-side only

### Expansion Geography

| Ring | Region | Infrastructure Impact |
|------|--------|-----------------------|
| 1 | ABC Paulista | Local delivery, same-day |
| 2 | Grande São Paulo | Next-day delivery, regional warehouse |
| 3 | Estado de SP | 2-3 day shipping, Correios + transportadoras |
| 4 | Brasil (capitals) | E-commerce only, 5-7 day shipping |

## Cross-References
- Payment schemas → `P06_schema/`
- CRM pipeline → `P12_orchestration/p12_wf_crm_research_pipeline.md`
- Brand validation → `python _tools/brand_validate.py`
- Contact validator → `P06_schema/p06_val_business_contact_quality.md`
