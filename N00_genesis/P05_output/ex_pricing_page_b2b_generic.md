---
id: ex_pricing_page_b2b_generic
kind: pricing_page
pillar: P05
version: 1.0.0
title: "B2B Pricing Page Template -- Subscription Tiers + Volume Discounts"
description: "Pricing page for B2B/partner channel. Three subscription tiers, volume discount table, feature comparison matrix, and annual discount CTA."
domain: ecommerce
nucleus: N06
quality: 9.0
tags: [pricing-page, b2b, subscription, tiers, feature-matrix, volume-discount]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_CURRENCY
  - BRAND_SUBSCRIPTION_PRICE_TIER_1
  - BRAND_SUBSCRIPTION_PRICE_TIER_2
  - BRAND_SUBSCRIPTION_PRICE_TIER_3
  - BRAND_PARTNER_EMAIL
  - BRAND_WHATSAPP_B2B
density_score: 1.0
---

# B2B Pricing Page Template

> Replace `{{BRAND_*}}` vars. Prices shown as `{{BRAND_SUBSCRIPTION_PRICE_TIER_X}}` --
> example values use illustrative ranges only.

---

## Page Meta

```yaml
title: "Planos {{BRAND_NAME}} para Parceiros"
description: "Compare os planos de parceria {{BRAND_NAME}}. De revendedor iniciante a grande atacadista -- encontre o plano certo para o seu negocio."
canonical: https://{{BRAND_DOMAIN}}/b2b/planos
```

---

## Section 1: Plan Toggle

```
[Mensal]  [Anual -20%]   <- toggle
```

---

## Section 2: Tier Cards (3 columns)

### Tier 1 -- Starter

| Field | Value |
|-------|-------|
| Name | Parceiro Starter |
| Price | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_1}}/mes (example range: 0-49) |
| Tagline | Para revendedores iniciando |
| CTA | [Cadastrar gratis] |

**Features:**
- Acesso ao catálogo completo
- Desconto de (5-10%) em pedidos
- Suporte via email
- Pedido mínimo: (X unidades)
- Portal B2B basico

### Tier 2 -- Pro (RECOMMENDED badge)

| Field | Value |
|-------|-------|
| Name | Parceiro Pro |
| Price | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_2}}/mes (example range: 89-149) |
| Tagline | Para revendedores estabelecidos |
| CTA | [Assinar Pro] |

**Features (includes Starter +):**
- Desconto de (15-20%) em pedidos
- Prioridade em lotes limitados
- Suporte WhatsApp dedicado
- Acesso antecipado a lancamentos
- Dashboard analytics de vendas
- Materiais de marketing exclusivos

### Tier 3 -- Enterprise

| Field | Value |
|-------|-------|
| Name | Parceiro Enterprise |
| Price | {{BRAND_CURRENCY}} {{BRAND_SUBSCRIPTION_PRICE_TIER_3}}/mes (example range: 299+) |
| Tagline | Para grandes distribuidores |
| CTA | [Falar com equipe] -> {{BRAND_WHATSAPP_B2B}} |

**Features (includes Pro +):**
- Desconto de (25-35%) em pedidos
- Gerente de conta dedicado
- Exclusividade territorial (negocio)
- API access para integracao de sistemas
- Co-branding disponivel
- SLA de entrega prioritario

---

## Section 3: Feature Comparison Matrix

| Feature | Starter | Pro | Enterprise |
|---------|---------|-----|------------|
| Catalogo completo | [OK] | [OK] | [OK] |
| Portal B2B | basico | avancado | full |
| Desconto volume | 5-10% | 15-20% | 25-35% |
| Suporte | email | WhatsApp | gerente dedicado |
| Analytics | -- | [OK] | [OK] + API |
| Lancamentos early access | -- | [OK] | [OK] |
| Exclusividade territorial | -- | -- | negocio |
| Co-branding | -- | -- | [OK] |

---

## Section 4: Volume Discount Table

> Stacks on top of tier discount. Example ranges -- configure per your margins.

| Pedido (unidades) | Desconto adicional |
|-------------------|--------------------|
| 10-49 | +0% |
| 50-99 | +3% |
| 100-249 | +5% |
| 250-499 | +8% |
| 500+ | negocie com equipe |

---

## Section 5: Annual Discount CTA

```
Anual = 2 meses gratis (economize 20%)
[Ver planos anuais]
```

---

## Section 6: FAQ Pricing

| Pergunta | Resposta |
|----------|---------|
| Posso mudar de plano? | Sim, a qualquer momento. |
| Ha taxa de cancelamento? | Nao. Cancele quando quiser. |
| Como e feito o pagamento? | PIX, boleto ou cartao. |
| Preciso de CNPJ? | Sim, CNPJ ativo obrigatorio. |

---

## Section 7: Enterprise Contact

```
Precisa de algo personalizado?
Nossa equipe monta um plano sob medida para o seu volume.
[Falar com equipe] -> {{BRAND_PARTNER_EMAIL}} | {{BRAND_WHATSAPP_B2B}}
```
