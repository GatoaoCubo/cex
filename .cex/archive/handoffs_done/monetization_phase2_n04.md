# Phase 2: Knowledge Cards — Content Monetization
**Nucleus**: N04 (Knowledge) | **Superintendent**: N06 (Commercial)
**REGRA: Commit e signal ANTES de qualquer pausa.**

## CONTEXTO
Mission content-monetization. Você cria 8 platform KCs distilados de codexa-core.

Source patterns extraídos (N07 scrape):
- **billing_executor.py** (745L): BillingExecutor class. Stripe/MercadoPago checkout, webhooks, subscriptions. 3 modes: LIVE/TEST/MOCK. create_checkout_session, handle_webhook_event (5 event types), get_subscription.
- **credit_system.py** (711L): CreditSystem class. BRL centavos wallet. PIPELINE_COSTS dict (PESQUISA=75, ANUNCIO=50, FOTO=100, FULL=200). DEFAULT_PACKS (5/20/60 BRL). add_credits, consume, refund, check_sufficient, purchase_pack_pix.
- **cursos_executor.py** (562L): CursosExecutor class. 4 Pydantic models (OutlineOutput, ModuleOutput, SalesPageOutput, EmailSequenceOutput). Sequential LLM chain: outline→module→sales_page→email_sequence.
- **erp_connector.py** (1316L): ERPConnector base + BlingConnector + BaseLinkerConnector. OAuth2 token refresh, rate limiting, 3 data models (ERPProduct, ERPOrder, ERPStockItem).
- **anuncio_validator.py** (619L): AnuncioValidator. Confidence scoring, fabrication detection, factual accuracy checks, retry logic.
- **email_templates.py** (456L): TEMPLATES dict. Transactional + marketing templates with BRL formatting.
- **mercadopago_executor.py** (715L): MercadoPagoExecutor. PIX/boleto/credit card. Preferences API, IPN webhooks, Preapproval for subscriptions.

## CRIAR (8 KCs em P01_knowledge/library/platform/)

1. **kc_stripe_patterns.md** — Checkout sessions, webhooks (5 event types), idempotency, mode detection (LIVE/TEST/MOCK), subscription lifecycle
2. **kc_credit_system_design.md** — Prepaid wallet pattern, centavos model, pipeline costs, packs with discount tiers, idempotency_key, consume+refund
3. **kc_course_generation.md** — LLM sequential chain: outline→module→sales_page→email. Pydantic output models. Mock fallback pattern.
4. **kc_ad_validation.md** — Fabrication detection (FABRICATION_PATTERNS), confidence scoring, factual accuracy, retry-with-sections
5. **kc_email_automation.md** — Template dict pattern, BRL currency formatting, transactional vs marketing, personalization
6. **kc_mercadopago_pix.md** — Preferences API, IPN webhooks, x-signature HMAC-SHA256, PIX/boleto/credit card, Preapproval subscriptions
7. **kc_pricing_strategy.md** — Cost-plus margins (PESQUISA 44%, ANUNCIO 55%, FOTO 47%), pack discounts, tier architecture (free/pro/enterprise)
8. **kc_erp_integration.md** — Connector pattern (base+impl), OAuth2 refresh, rate limiting, BaseLinker sync, Bling v3, stock/order/product models

## REGRAS
- Cada KC: ≤5120B, frontmatter completo (id, kind:knowledge_card, pillar:P01, quality:null, tldr, tags)
- Conteúdo: patterns abstratos, não código codexa-specific
- Use `[PLACEHOLDER]` para valores hardcoded
- Compile após salvar: `python _tools/cex_compile.py --all`

## COMMIT
```bash
git add -A && git commit -m "[N04] monetization phase2: 8 platform KCs for content monetization"
```
