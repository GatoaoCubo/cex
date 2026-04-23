---
id: ex_landing_page_b2b_generic
kind: landing_page
pillar: P05
version: 1.0.0
title: "B2B Landing Page Template -- Partner/Wholesale Channel"
description: "B2B landing page with channel value props, FAQ accordion, and partner registration CTA. For brands with a wholesale or reseller program."
domain: ecommerce
nucleus: N06
quality: 9.0
tags: [landing-page, b2b, partner, wholesale, cta, faq]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_B2B_TAGLINE
  - BRAND_WHATSAPP_B2B
  - BRAND_PARTNER_EMAIL
  - BRAND_VERTICAL
  - BRAND_AFFILIATE_COMMISSION
  - BRAND_PRIMARY_COLOR
density_score: 1.0
related:
  - bld_system_prompt_landing_page
  - bld_instruction_landing_page
  - landing_page_template
  - kc_landing_page
  - bld_quality_gate_landing_page
  - landing-page-builder
  - bld_architecture_landing_page
  - bld_knowledge_card_landing_page
  - bld_schema_landing_page
  - ad_copy_template
---

# B2B Landing Page Template

> Sections are ordered by conversion priority. Keep above-the-fold lean.
> Replace all `{{BRAND_*}}` from `brand_config.yaml`.

---

## Page Meta

```yaml
title: "Parceiros {{BRAND_NAME}} -- Revenda com Margem Real"
description: "Seja revendedor {{BRAND_NAME}}. Acesso a catálogo completo, preços exclusivos e suporte dedicado. Cadastre-se em 2 minutos."
og_image: /images/og_b2b.jpg
canonical: https://{{BRAND_DOMAIN}}/b2b
```

---

## Section 1: Hero

```
Headline: "Venda {{BRAND_VERTICAL}} premium com a margem que você merece"
Subheadline: "{{BRAND_B2B_TAGLINE}}"

CTA primary: [Quero ser parceiro] -> /b2b/cadastro
CTA secondary: [Falar com consultor] -> wa.me/{{BRAND_WHATSAPP_B2B}}
```

**Trust badges (3 items):**
- Cadastro gratuito em 2 minutos
- Suporte via WhatsApp
- Tabela de preços exclusiva

---

## Section 2: Channel Value Props (3 columns)

| Canal | Descricao | CTA |
|-------|-----------|-----|
| Revendedor | Acesso a tabela com descontos por volume | Cadastrar como revendedor |
| Afiliado | {{BRAND_AFFILIATE_COMMISSION}} de comissao por venda | Ver programa de afiliados |
| ONG/Institucional | Condições especiais para organizações sem fins lucrativos | Contato institucional |

---

## Section 3: How It Works (steps)

```
1. Cadastro  ->  2. Aprovação  ->  3. Acesso ao catálogo  ->  4. Pedido  ->  5. Entrega
   (2 min)        (até 24h)        (portal B2B)              (mínimo: X unidades)
```

---

## Section 4: FAQ Accordion

| Pergunta | Resposta |
|----------|---------|
| Qual o pedido mínimo? | A partir de (X unidades por SKU -- configure conforme sua política) |
| Tem exclusividade territorial? | (Defina sua política de exclusividade) |
| Como é feito o pagamento? | PIX, boleto, ou cartão. Prazo de pagamento negociado por perfil. |
| Posso vender online? | Sim, com uso das nossas diretrizes de marca. |
| Tem suporte para montar minha loja? | Sim, via {{BRAND_PARTNER_EMAIL}} ou WhatsApp {{BRAND_WHATSAPP_B2B}} |

---

## Section 5: Social Proof

> Testimonial block -- 3 partner quotes. Use real quotes or illustrative format:

```
"[Nome do parceiro], [cidade]: '[Resultado quantificado -- ex: dobrei meu ticket médio
em 2 meses com o catálogo {{BRAND_NAME}}]'"
```

---

## Section 6: CTA Footer

```
Headline: "Pronto para começar?"
CTA: [Criar minha conta parceiro] -> /b2b/cadastro
Secondary: [Dúvidas? Fale conosco] -> mailto:{{BRAND_PARTNER_EMAIL}}
```

---

## Component Dependencies

| Component | Purpose |
|-----------|---------|
| Header | Navigation with partner login link |
| FAQ Accordion | Interactive collapse/expand |
| WhatsApp Float | Sticky WhatsApp button |
| SEO Head | Meta + OG tags |

---

## Design Tokens

```css
--primary: {{BRAND_PRIMARY_COLOR}};
--b2b-accent: #1a1a2e;   /* professional dark tone for B2B */
--cta-radius: 8px;
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_system_prompt_landing_page]] | upstream | 0.25 |
| [[bld_instruction_landing_page]] | upstream | 0.22 |
| [[landing_page_template]] | related | 0.21 |
| [[kc_landing_page]] | upstream | 0.17 |
| [[bld_quality_gate_landing_page]] | downstream | 0.17 |
| [[landing-page-builder]] | related | 0.16 |
| [[bld_architecture_landing_page]] | downstream | 0.16 |
| [[bld_knowledge_card_landing_page]] | upstream | 0.16 |
| [[bld_schema_landing_page]] | downstream | 0.16 |
| [[ad_copy_template]] | related | 0.16 |
