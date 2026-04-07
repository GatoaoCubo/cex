# Mission: Content Monetization v2 — Research + Template + DS24 Enrichment
**Prioridade**: Media | **Estimativa**: 3-4h | **Nuclei**: N01 (research) + N03 (engineering)
**REGRA: Commit e signal ANTES de qualquer pausa.**

---

## OBJETIVO

Completar o content-monetization-builder com o que FALTA:
1. Knowledge Cards de pesquisa (Hotmart API, Digistore24 API, webhooks, compliance)
2. Template generico em _instances/_template/N06/ (qualquer empresa usa)
3. Enriquecer builder ISOs com Digistore24 (hoje so tem Hotmart raso)

## O QUE JA EXISTE (Nao Refazer)

| Artefato | Status | Detalhe |
|----------|--------|---------|
| content-monetization-builder | DONE | 14 ISOs, 48.6KB, Hotmart refs em 11 files |
| N06 nucleus artifacts | DONE | 22 files (dispatch, workflow, KC, agent, prompts) |
| _instances/codexa/N06 | DONE | 8 files (agent york, pricing, workflow) |
| knowledge_card_content_monetization.md | DONE | 206 ln, mas codexa-specific (BRL, MercadoPago) |
| knowledge_card_commercial.md | DONE | 164 ln, nucleus-level KC |

## O QUE FALTA (Escopo desta mission)

| Gap | Detalhe | Impacto |
|-----|---------|---------|
| Research KCs Hotmart | Zero KCs sobre Hotmart API, webhooks, Club, Marketplace | Builder nao sabe como integrar |
| Research KCs Digistore24 | Zero refs a DS24 no repo inteiro | Plataforma internacional ignorada |
| Research KCs compliance | Zero KCs sobre EU VAT, GDPR, Widerrufsrecht | Risco legal para clientes EU |
| Template generico N06 | _instances/_template/N06 nao existe | Empresas novas nao tem ponto de partida |
| Builder ISOs DS24 | 0 refs DS24 nos 14 ISOs | Builder so sabe Hotmart, nao multi-plataforma |
---

## FASE 0: Research KCs (N01 solo — 1.5-2h)

Criar 8 Knowledge Cards em P01_knowledge/library/platform/:

| # | KC ID | Titulo | Fonte Oficial | Prioridade |
|---|-------|--------|---------------|------------|
| 1 | kc_hotmart_api | Hotmart REST API & Webhooks | developers.hotmart.com | P0 |
| 2 | kc_hotmart_club | Hotmart Club (Member Area) | hotmart.com/club | P1 |
| 3 | kc_hotmart_marketplace | Hotmart Marketplace & Afiliados | hotmart.com/marketplace | P1 |
| 4 | kc_digistore24_api | Digistore24 REST API | developer.digistore24.com | P0 |
| 5 | kc_digistore24_ipn | Digistore24 IPN (Webhooks) | developer.digistore24.com/ipn | P0 |
| 6 | kc_digistore24_marketplace | DS24 Marketplace & Affiliates | digistore24.com/vendor | P1 |
| 7 | kc_content_platform_compliance | EU VAT/GDPR/Widerrufsrecht para Infoprodutos | europa.eu, gdpr.eu | P0 |
| 8 | kc_content_platform_comparison | Hotmart vs DS24 vs Teachable vs Kiwify | Comparativo cross-platform | P1 |

Cada KC deve conter:
- Frontmatter completo (id, kind, pillar, domain, keywords, axioms, linked_artifacts)
- Endpoints principais (REST paths, metodos, payloads)
- Webhook/IPN events (nomes, formato, assinatura)
- Rate limits e quotas
- Modo sandbox/test
- Gotchas e armadilhas reais

**Detalhes criticos por KC:**

KC 1 (kc_hotmart_api):
- Base URL: https://developers.hotmart.com/docs/en/
- Auth: OAuth2 Bearer token (client_credentials)
- Endpoints: /payments/api/v1/sales, /club/api/v1/modules, /affiliation
- Webhook events: PURCHASE_COMPLETE, PURCHASE_CANCELED, PURCHASE_REFUNDED,
  PURCHASE_CHARGEBACK, SUBSCRIPTION_CANCELLATION, SWITCH_PLAN
- Webhook signature: sha256 HMAC (header X-Hotmart-Hottok)
- Sandbox: hotmart.com/developer (test environment)

KC 4-5 (kc_digistore24_api + ipn):
- API Base: https://www.digistore24.com/api/v1/
- Auth: API key via header X-DS-API-KEY
- IPN: POST form-encoded (NAO JSON!), sha512 signature verification
- IPN response: body must be exact string "OK" (nao JSON, nao HTML)
- IPN events: on_payment, on_refund, on_chargeback, on_rebill_resumed,
  on_rebill_cancelled, on_affiliatelink, on_invoice_created, on_payment_missed
- Merchant of Record: DS24 coleta/remete EU VAT automaticamente
- 7 idiomas nativos: DE, EN, ES, FR, IT, NL, PL
- Payment methods por pais: DE(SEPA+Sofort), NL(iDEAL), US/UK(cards+PayPal)

KC 7 (compliance):
- EU VAT: DS24 como Merchant of Record = vendedor nao precisa registro VAT por pais
- GDPR: double opt-in obrigatorio, data processing agreement, right to erasure
- Widerrufsrecht: 14-day cooling-off period (Alemanha), exceto digital com consent
- Impressum: obrigatorio para vendedores na DACH region
- Cookie consent: ePrivacy directive, opt-in antes de analytics

KC 8 (comparison):
- Hotmart: BR/LATAM dominante, real(BRL), marketplace com 500K+ afiliados
- Digistore24: EU dominante, EUR, marketplace com afiliados, auto VAT
- Teachable: self-hosted, USD, sem marketplace, sem afiliados nativos
- Kiwify: BR emergente, BRL, clone hotmart mais simples, fees menores
- Tier strategy: T1=Hotmart(BR)+DS24(INT), T2=+Udemy+ClickBank se mass niche

**Fontes oficiais (URLs para pesquisa):**
- https://developers.hotmart.com/docs/en/
- https://developers.hotmart.com/docs/en/1.0.0/webhook/
- https://hotmart.com/en/club
- https://developer.digistore24.com/
- https://developer.digistore24.com/ipn-interface/
- https://help.digistore24.com/en/
- https://gdpr.eu/

Commit: "research: 8 platform KCs (Hotmart API, DS24 API+IPN, compliance, comparison)"
---

## FASE 1: Template Generico N06 (N03 solo — 30min)

Criar _instances/_template/N06_commercial/ com 3 files:

#### 1. content_monetization_config.md

Template com [PLACEHOLDERS] para qualquer empresa:

    # Content Monetization Config — Instance Template
    > Copy to _instances/{empresa}/N06_commercial/, fill [PLACEHOLDERS]

    identidade:
      empresa: "[EMPRESA_NOME]"
      vertical: "[educacao|saas|consultoria|coaching|comunidade]"
      moeda_principal: "[BRL|EUR|USD]"
      regiao_principal: "[BR|LATAM|EU|US|GLOBAL]"

    plataformas:
      tier_1:
        brasil: "[hotmart|kiwify|eduzz|none]"
        internacional: "[digistore24|teachable|thinkific|none]"
      tier_2: "[udemy|clickbank|gumroad|none]"

    produtos:
      - tipo: "[curso|ebook|mentoria|comunidade|template|saas]"
        nome: "[PRODUTO_NOME]"
        preco_brl: [PRECO]
        preco_eur: [PRECO]
        preco_usd: [PRECO]
        checkout: "[hotmart|ds24|stripe|mercadopago]"
        entrega: "[hotmart_club|ds24_member|teachable|custom]"

    webhooks:
      hotmart:
        hottok: "[HOTMART_HOTTOK]"
        endpoint: "[URL_WEBHOOK_HOTMART]"
      digistore24:
        api_key: "[DS24_API_KEY]"
        ipn_passphrase: "[DS24_IPN_PASSPHRASE]"
        endpoint: "[URL_WEBHOOK_DS24]"

    afiliados:
      hotmart_programa: "[LINK_PROGRAMA_AFILIADOS]"
      comissao_percentual: [PERCENTUAL]
      ds24_affiliate_enabled: [true|false]

    compliance:
      gdpr_dpa_signed: [true|false]
      impressum_url: "[URL_IMPRESSUM]"
      widerrufsrecht_text: "[URL_CANCELLATION_POLICY]"
      cookie_consent: "[PROVIDER]"

#### 2. pricing_model.md

Template de pricing strategy com [PLACEHOLDERS]:
- Ladder: freebie -> low-ticket -> mid -> high-ticket -> recorrencia
- Pricing por regiao (PPP - Purchasing Power Parity)
- Cupons e datas de lancamento
- Metricas: CAC, LTV, churn, conversion rate targets

#### 3. launch_checklist.md

Checklist generico de lancamento:
- [ ] Produto criado na plataforma (Hotmart/DS24)
- [ ] Checkout testado (sandbox)
- [ ] Webhook configurado e testado
- [ ] Pagina de vendas publicada
- [ ] Email sequences configuradas
- [ ] Programa de afiliados ativado
- [ ] Compliance verificado (GDPR/VAT se EU)
- [ ] Analytics tracking (UTMs, pixel)

Commit: "template: create _instances/_template/N06_commercial/ (config + pricing + checklist)"
---

## FASE 2: Enriquecer Builder ISOs com DS24 (N03 solo — 1h)

Atualizar 8 dos 14 ISOs do content-monetization-builder para cobrir Digistore24:

| ISO | O Que Adicionar |
|-----|----------------|
| bld_architecture | DS24 IPN flow (form-encoded, sha512, respond "OK") ao lado do Hotmart webhook flow |
| bld_instruction | Steps para DS24: create product, configure IPN, test sandbox, go live |
| bld_examples | Exemplo DS24: produto em EUR, IPN handler, affiliate setup |
| bld_schema | Campos DS24: ds24_product_id, ds24_api_key, ipn_passphrase, eu_vat_included |
| bld_config | Config vars DS24: DS24_API_KEY, DS24_IPN_URL, DS24_SANDBOX_MODE |
| bld_tools | DS24 API endpoints: /products, /purchases, /affiliates |
| bld_knowledge_card | Refs aos 8 novos KCs de Fase 0 |
| bld_collaboration | Crew: "Multi-Platform Launch" (research->build->validate->deploy) |

NAO alterar: bld_manifest (frontmatter sera atualizado pela mission_builder_autodiscovery),
bld_quality_gate, bld_system_prompt, bld_output_template, bld_memory (sera ativado pela autodiscovery).

Regra: cada ISO deve tratar Hotmart e DS24 como PARES equivalentes,
nao Hotmart como principal e DS24 como secundario.
Usar pattern: "Platform A (Hotmart/BR) ... Platform B (Digistore24/INT) ..."

Commit: "enrich: content-monetization-builder ISOs with Digistore24 parity"

---

## FASE 3: Reindex + Validate (N03 — 15min)

1. Rodar cex_compile.py para recompilar N06 artifacts
2. Rodar cex_index.py para reindexar (novos KCs aparecerao no index)
3. Validar: 8 novos KCs no index.db com keywords
4. Validar: builder ISOs mencionam DS24 em >= 8 files
5. Validar: _instances/_template/N06 existe com 3 files

Commit: "validate: recompile + reindex after content monetization v2"

---

## PLANO DE EXECUCAO

Deps: F0 --> F1 + F2 (paralelos) --> F3

F0 (research) NAO depende de nada — pesquisa pura.
F1 (template) NAO depende de F0 — eh placeholder generico.
F2 (enrich) DEPENDE de F0 — precisa dos KCs como referencia.
F3 (validate) DEPENDE de F1 e F2.

### Opcao 1: 2 spawns (recomendado, ~2.5h)

Spawn 1 (N01 research):
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n01 -task "Leia .cex/runtime/handoffs/mission_content_monetization_v2.md. Execute Fase 0: criar 8 KCs de pesquisa em P01_knowledge/library/platform/. Use as fontes oficiais listadas. Commit ao final." -interactive

Spawn 2 (N03 template, roda junto):
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_content_monetization_v2.md. Execute Fase 1: criar _instances/_template/N06_commercial/ com 3 files (config, pricing, checklist). Commit ao final." -interactive

Depois que Spawn 1 terminar:

Spawn 3 (N03 enrich + validate):
    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_content_monetization_v2.md. Execute Fase 2 (enrich 8 ISOs com DS24) e Fase 3 (recompile + reindex + validate). Commit cada fase." -interactive

### Opcao 2: Sequencial (1 spawn N03, ~3h)

    powershell -NoProfile -ExecutionPolicy Bypass -File _spawn/spawn_solo.ps1 -nucleus n03 -task "Leia .cex/runtime/handoffs/mission_content_monetization_v2.md. Execute F0, F1, F2, F3 sequencialmente. Commit cada fase. Signal ao final." -interactive
---

## CRITERIOS DE ACEITE

| Criterio | Validacao |
|----------|----------|
| 8 KCs criados | P01_knowledge/library/platform/kc_{hotmart_api,hotmart_club,hotmart_marketplace,digistore24_api,digistore24_ipn,digistore24_marketplace,content_platform_compliance,content_platform_comparison}.md |
| KCs com profundidade | Cada KC >= 100 linhas, com endpoints, events, gotchas |
| Template N06 | _instances/_template/N06_commercial/ com 3 files |
| Template com placeholders | Zero valores hardcoded, tudo [PLACEHOLDER] |
| Builder ISOs enriquecidos | DS24 refs em >= 8 dos 14 ISOs |
| DS24 como par do Hotmart | Ambos tratados equivalentemente nos ISOs |
| Recompilado | cex_compile.py roda sem erro |
| Reindexado | 8 novos KCs aparecem no index.db com keywords |

## ANTI-PATTERNS

- NAO refazer o builder (14 ISOs ja existem, so enriquecer)
- NAO refazer N06 nucleus (22 files ja existem)
- NAO refazer _instances/codexa/ (8 files ja existem)
- NAO hardcodar dados de nenhuma empresa nos KCs (usar dados publicos das APIs)
- NAO tratar DS24 como secundario ao Hotmart (sao PARES)
- NAO ignorar compliance EU (GDPR/VAT eh obrigatorio para DS24)
- NAO criar KCs rasos (<50 linhas) — pesquisa precisa de profundidade
- NAO confundir esta mission com mission_builder_autodiscovery (sao independentes)

## CONEXAO COM OUTRAS MISSIONS

| Mission | Conexao |
|---------|---------|
| mission_builder_autodiscovery | Track A hydrata frontmatter do builder (keywords/triggers/capability_summary). Independente. |
| mission_builder_autodiscovery | Track B ativa bld_memory. Independente. |
| mission_research_pipeline | Usa mesmo padrao de KCs em P01_knowledge/library/platform/. Consistente. |
| mission_supabase_data_layer | KCs de supabase sao modelo para os KCs de Hotmart/DS24. Mesmo padrao. |

## ARTEFATOS CRIADOS

| # | Artefato | Fase | Tipo |
|---|----------|------|------|
| 1 | P01_knowledge/library/platform/kc_hotmart_api.md | F0 | KC novo |
| 2 | P01_knowledge/library/platform/kc_hotmart_club.md | F0 | KC novo |
| 3 | P01_knowledge/library/platform/kc_hotmart_marketplace.md | F0 | KC novo |
| 4 | P01_knowledge/library/platform/kc_digistore24_api.md | F0 | KC novo |
| 5 | P01_knowledge/library/platform/kc_digistore24_ipn.md | F0 | KC novo |
| 6 | P01_knowledge/library/platform/kc_digistore24_marketplace.md | F0 | KC novo |
| 7 | P01_knowledge/library/platform/kc_content_platform_compliance.md | F0 | KC novo |
| 8 | P01_knowledge/library/platform/kc_content_platform_comparison.md | F0 | KC novo |
| 9 | _instances/_template/N06_commercial/content_monetization_config.md | F1 | Template novo |
| 10 | _instances/_template/N06_commercial/pricing_model.md | F1 | Template novo |
| 11 | _instances/_template/N06_commercial/launch_checklist.md | F1 | Template novo |
| 12-19 | archetypes/builders/content-monetization-builder/bld_{8 ISOs}.md | F2 | Enrich |

---
**Total: 19 artefatos (8 KCs + 3 templates + 8 ISO enrichments)**
**Estimativa: 3-4h sequencial | 2.5h paralelo (2-3 spawns)**