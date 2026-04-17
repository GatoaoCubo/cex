---
kind: knowledge_card
id: bld_knowledge_card_white_label_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for white_label_config production
quality: 9.2
title: "Knowledge Card White Label Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [white_label_config, builder, knowledge_card]
tldr: "Domain knowledge for white_label_config production"
domain: "white_label_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview  
White-label configurations enable SaaS providers to deliver customizable, rebrandable deployments for resellers or enterprise clients. These configurations typically isolate branding, UI/UX, and API integrations from core product logic, allowing resellers to embed the service into their own ecosystems without exposing underlying infrastructure. Key focus areas include dynamic theming, API endpoint customization, and secure credential management. Unlike brand_config (identity-related settings) or env_config (runtime parameters), white_label_config prioritizes reseller-specific overrides while maintaining product integrity.  

The domain intersects with multi-tenancy, API management, and software composition, requiring robust abstractions to balance flexibility with security. Industry adoption spans platforms like CRM, e-commerce, and analytics tools, where resellers demand tailored deployments without compromising upstream functionality.  

## Key Concepts  
| Concept                        | Definition                                                                 | Source                              |  
|------------------------------|----------------------------------------------------------------------------|-------------------------------------|  
| Customizable UI Components   | Modular UI elements allowing reseller branding overrides                   | W3C UI Accessibility Guidelines     |  
| Branding Assets              | Logos, color schemes, and typography managed externally                   | ISO 20252:2019 (Brand Management)   |  
| API Keys                     | Reseller-specific credentials for external system integration             | OAuth 2.0 (RFC 6749)                |  
| Configuration Templates      | Predefined YAML/JSON structures for reseller overrides                    | OpenAPI Specification (RFC 7807)    |  
| Runtime Environment Isolation| Isolation of reseller-specific settings from core application logic       | RFC 7231 (HTTP/1.1)                 |  
| Brand-Specific Routing       | Custom URL paths or subdomains for reseller deployments                   | RFC 7285 (HTTP/2)                   |  
| Secure Configuration Storage | Encrypted storage of reseller secrets and overrides                       | NIST SP 800-57 (Key Management)     |  
| Configuration Validation     | Schema-based checks for reseller input integrity                          | JSON Schema (RFC 7396)              |  
| Multi-Tenant Configuration   | Shared infrastructure with reseller-specific configuration layers         | ISO/IEC 2382-1:2011 (Software Terms)|  
| Brand-Specific Analytics     | Reseller-specific tracking IDs and data export rules                      | GA4 (Google Analytics 4)            |  
| Legal Compliance Flags       | Toggleable settings for GDPR, CCPA, or regional regulations               | IETF RFC 7991 (Data Privacy)        |  
| Reseller-Specific Quotas     | Custom rate limits or resource allocations per reseller                   | RFC 7523 (OAuth 2.0 Token Introspection)|  

## Industry Standards  
- OAuth 2.0 (RFC 6749)  
- OpenAPI Specification (RFC 7807)  
- ISO/IEC 2382-1:2011 (Software Terminology)  
- NIST SP 800-57 (Key Management)  
- GDPR (EU Regulation 2016/679)  
- RFC 7231 (HTTP/1.1)  
- JSON Schema (RFC 7396)  
- ISO 20252:2019 (Brand Management)  

## Common Patterns  
1. **Configuration as Code** – Store white-label settings in versioned files (e.g., YAML).  
2. **Modular UI Frameworks** – Use component-based systems for dynamic theming.  
3. **Abstraction Layers** – Isolate reseller-specific logic from core application code.  
4. **Runtime Injection** – Load reseller configs at deployment via environment variables.  
5. **Policy-Driven Validation** – Enforce schema rules for reseller input consistency.  

## Stripe Connect Sub-Account Model  
White-label platforms commonly use Stripe Connect to manage reseller billing:  
- **Platform account**: owns product, sets pricing floors, collects platform fees (1-3% typical).  
- **Connected (sub) account**: reseller's Stripe account, receives payouts minus platform fee.  
- **Charge types**: Direct charges (reseller controls UX), Destination charges (platform controls UX), Separate charges + transfers (split billing).  
- **OEM licensing model**: platform licenses product to reseller at wholesale price; reseller sets retail price. Margin = retail - wholesale - platform fee.  
- Config artifact must specify: `stripe_connect_type`, `platform_fee_percent`, `reseller_margin_floor`, `payout_schedule`.  

## Branding Components (MUST configure in every white_label_config)  
| Component | Config Key | Notes |  
|-----------|------------|-------|  
| Custom domain | `custom_domain` | e.g., app.reseller.com -- requires DNS CNAME |  
| Branded email sender | `email_from_domain` | e.g., noreply@reseller.com -- requires SPF/DKIM |  
| Logo (header) | `logo_url` | PNG/SVG, min 200x50px |  
| Favicon | `favicon_url` | ICO/PNG 32x32 |  
| Primary color | `brand_color_primary` | HEX, used in buttons/links |  
| Co-branded footer | `cobrand_text` | "Powered by [Platform]" or fully white-labeled |  
| Theming API | `theme_api_enabled` | Exposes CSS variable overrides to reseller |  

## Common Patterns  
1. **Configuration as Code** -- Store white-label settings in versioned YAML files.  
2. **Modular UI Frameworks** -- CSS variable injection via theming API for runtime branding.  
3. **Abstraction Layers** -- Isolate reseller logic from core application code.  
4. **Stripe Connect sub-accounts** -- Platform fee model with connected account payouts.  
5. **Policy-Driven Validation** -- Enforce schema rules for reseller input consistency.  
6. **Custom domain provisioning** -- Automated CNAME + SSL cert issuance per reseller.  
7. **OEM licensing tiers** -- Wholesale price + margin floor + retail pricing freedom for reseller.  

## Pitfalls  
- **Hardcoding Branding** -- Embedding reseller-specific data directly into core code.  
- **Insecure Credential Handling** -- Storing Stripe Connect keys or API tokens in plaintext config.  
- **Missing reseller margin floor** -- Allowing resellers to price below cost, eroding platform revenue.  
- **Single custom domain** -- Not supporting multiple domains per reseller (multi-brand accounts).  
- **No theming API versioning** -- CSS variable changes breaking existing reseller themes on deploy.
