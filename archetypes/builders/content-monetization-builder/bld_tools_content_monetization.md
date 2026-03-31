---
kind: tools
id: bld_tools_content_monetization
pillar: P04
llm_function: CALL
purpose: Tools, APIs, and data sources for content monetization pipeline
---

# Tools: content-monetization-builder

## Payment Providers

### Platform A — Hotmart (BR)
| Aspect | Detail |
|--------|--------|
| API Base | https://developers.hotmart.com/docs/en/ |
| Auth | OAuth2 Bearer token (client_credentials) → HOTMART_TOKEN |
| Endpoints | /payments/api/v1/sales, /club/api/v1/modules, /affiliation |
| Webhook | JSON, sha256 HMAC via X-Hotmart-Hottok header |
| Events | PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED, PURCHASE_CHARGEBACK, SUBSCRIPTION_CANCELLATION, SWITCH_PLAN |
| Sandbox | hotmart.com/developer (test environment) |
| Cost | varies by product category |
| Market | BR/LATAM infoproducts, 500K+ affiliates |
| Member area | Hotmart Club (native course delivery) |

### Platform B — Digistore24 (International)
| Aspect | Detail |
|--------|--------|
| API Base | https://www.digistore24.com/api/v1/ |
| Auth | API key via X-DS-API-KEY header → DS24_API_KEY |
| Endpoints | /products, /purchases, /affiliates, /transactions |
| IPN | form-encoded (NOT JSON), sha512 signature (DS24_IPN_PASSPHRASE) |
| IPN Response | body must be exact string "OK" (not JSON, not HTML) |
| Events | on_payment, on_refund, on_chargeback, on_rebill_resumed, on_rebill_cancelled, on_affiliatelink, on_invoice_created, on_payment_missed |
| Sandbox | DS24 test product mode |
| Cost | varies, DS24 is Merchant of Record |
| Market | EU/DACH dominant, EUR, auto EU VAT |
| Languages | 7 native: DE, EN, ES, FR, IT, NL, PL |
| Payment methods | SEPA+Sofort (DE), iDEAL (NL), cards+PayPal (global) |
| Member area | DS24 member area or external redirect |

### Other Providers
| Provider | API | Auth | Cost | Market |
|----------|-----|------|------|--------|
| Stripe | REST + webhooks | STRIPE_SECRET_KEY | 2.9% + $0.30/tx | Global |
| Kiwify | REST | KIWIFY_API_KEY | 8.99% per sale | BR infoproducts |
| Monetizze | REST | MONETIZZE_TOKEN | varies | BR health/finance |
| Eduzz | REST | EDUZZ_API_KEY | varies | BR digital+physical |

## Email Providers
| Provider | API | Auth | Cost | Specialty |
|----------|-----|------|------|-----------|
| Resend | REST | RESEND_API_KEY | Free 3K/mo, $20/50K | Dev-friendly, React Email |
| SendGrid | REST | SENDGRID_API_KEY | Free 100/day, $19.95/50K | Scale, templates |
| AWS SES | REST/SMTP | AWS_ACCESS_KEY_ID | $0.10/1K emails | Cost-effective at scale |
| Mailchimp | REST | MAILCHIMP_API_KEY | Free 500 contacts | No-code, automations |

## Ad Platforms
| Platform | API | Auth | Min Budget | Best For |
|----------|-----|------|-----------|----------|
| Meta Ads | Marketing API | META_ACCESS_TOKEN | R$20/day | B2C awareness, retargeting |
| Google Ads | REST | GOOGLE_ADS_TOKEN | R$10/day | Intent capture, search |
| TikTok Ads | Marketing API | TIKTOK_ACCESS_TOKEN | R$50/day | Gen-Z, viral content |
| LinkedIn Ads | Marketing API | LINKEDIN_TOKEN | $10/day | B2B, professional |

## Course Platforms
Hotmart Club (native), Teachable, Thinkific, DS24 member area, Custom LMS.

## CEX Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | .md → .yaml compilation | After save |
| cex_hooks.py | Pre/post validation | Before commit |
| cex_doctor.py | Builder health check | After build |
| cex_score.py | 5D quality scoring | Peer review |
| signal_writer.py | Inter-nucleus signals | After complete |

## Data Sources
| Source | Path | Data |
|--------|------|------|
| Schema | P06/_schema.yaml | Field definitions |
| Kind KC | P01_knowledge/library/kind/ | Domain knowledge |
| Examples | P04_tools/examples/ | Reference configs |
| SEED_BANK | archetypes/SEED_BANK.yaml | Builder seeds |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |
