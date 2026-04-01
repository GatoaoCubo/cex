# N01 Task — Content Monetization v2: Research 8 Platform KCs
**Autonomia Total** | **Quality 9.0+**
**REGRA: Commit e signal ANTES de qualquer pausa.**

---

## CONTEXTO
Leia `.cex/runtime/handoffs/mission_content_monetization_v2.md` para detalhes completos.

## TAREFA: FASE 0 — Criar 8 Knowledge Cards

Diretório: `P01_knowledge/library/platform/`

### KCs a criar (use MCPs fetch/brave-search para pesquisar fontes oficiais):

| # | Arquivo | Fonte Oficial | Prioridade |
|---|---------|---------------|------------|
| 1 | kc_hotmart_api.md | developers.hotmart.com/docs/en/ | P0 |
| 2 | kc_hotmart_club.md | hotmart.com/club | P1 |
| 3 | kc_hotmart_marketplace.md | hotmart.com/marketplace | P1 |
| 4 | kc_digistore24_api.md | developer.digistore24.com | P0 |
| 5 | kc_digistore24_ipn.md | developer.digistore24.com/ipn-interface/ | P0 |
| 6 | kc_digistore24_marketplace.md | digistore24.com/vendor | P1 |
| 7 | kc_content_platform_compliance.md | gdpr.eu, europa.eu | P0 |
| 8 | kc_content_platform_comparison.md | Comparativo cross-platform | P1 |

### Formato de cada KC (OBRIGATÓRIO):
```yaml
---
id: kc_{name}
kind: knowledge_card
pillar: P01
quality: null
tldr: "..."
tags: [...]
---
```

### Requisitos por KC:
- **≥ 80 linhas** de conteúdo (não raso)
- Endpoints REST (paths, métodos, payloads)
- Webhook/IPN events (nomes, formato, assinatura)
- Rate limits e quotas
- Modo sandbox/test
- Gotchas e armadilhas reais
- Código de exemplo quando relevante

### Detalhes críticos:
- **Hotmart**: OAuth2 Bearer, X-Hotmart-Hottok SHA256 HMAC, events: PURCHASE_COMPLETE/CANCELED/REFUNDED/CHARGEBACK
- **DS24**: API key via X-DS-API-KEY, IPN é form-encoded (NÃO JSON!), sha512 signature, resposta MUST be exata string "OK"
- **DS24 é Merchant of Record**: coleta EU VAT automaticamente
- **Compliance**: GDPR double opt-in, Widerrufsrecht 14 dias, Impressum obrigatório DACH

### Referência de formato:
Veja KCs existentes como modelo:
- `P01_knowledge/library/platform/kc_stripe_patterns.md`
- `P01_knowledge/library/platform/kc_mercadopago_pix.md`

## COMMIT
```bash
git add P01_knowledge/library/platform/kc_hotmart_*.md P01_knowledge/library/platform/kc_digistore24_*.md P01_knowledge/library/platform/kc_content_platform_*.md
git commit -m "[N01] research: 8 platform KCs (Hotmart API/Club/Marketplace, DS24 API/IPN/Marketplace, compliance, comparison)"
```

## SIGNAL
```python
python -c "from _tools.signal_writer import write_signal; write_signal('n01', 'cmv2_research_complete', 9.0)"
```
