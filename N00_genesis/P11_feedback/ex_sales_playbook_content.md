---
id: ex_sales_playbook_content
kind: sales_playbook
pillar: P11
version: 1.0.0
title: "Sales Playbook -- Content-Driven Product Integration"
description: "Sales playbook for integrating products into content-first ecommerce. Covers product mention rules by content type, WhatsApp/email sales scripts, AI-assisted message generation, and B2B pitch flows."
domain: sales
nucleus: N06
quality: 9.0
tags: [sales-playbook, content-integration, whatsapp, email, b2b, d2c, ai-sales]
brand_placeholders:
  - BRAND_NAME
  - BRAND_DOMAIN
  - BRAND_VERTICAL
  - BRAND_PRODUCT_CATALOG
  - BRAND_VOICE_TONE
  - BRAND_PERSONA_NAME
  - BRAND_WHATSAPP_B2B
  - BRAND_PARTNER_EMAIL
density_score: 1.0
---

# Sales Playbook -- Content-Driven Product Integration

> Tactical guide for turning content into sales without losing brand voice.
> Replace `{{BRAND_*}}` vars. Voice guidelines defined by `{{BRAND_VOICE_TONE}}`.

---

## 1. Playbook Purpose

Content-first brands face a conversion dilemma: educational/entertainment content
builds audience, but product pitches break trust. This playbook resolves the tension
by defining exact rules for when, where, and how to introduce product mentions.

---

## 2. Product Mention Rules by Content Type

| Content Type | Mention Style | Frequency | CTA Style |
|--------------|--------------|-----------|-----------|
| Educational (blog) | Contextual (problem -> solution) | 1-2x per post | "Veja nossa solucao: [product link]" |
| Social awareness | None (brand only) | 0x | Follow / save |
| Social consideration | Category mention | 1x | "Link na bio" |
| Social conversion | Direct SKU + price | 1-2x | Direct product link |
| AI persona chat | Problem-fit recommendation | As needed | Product card with link |
| WhatsApp sales | Personalized + benefit-led | 1-2x per message | Checkout link + payment method |
| Email sequence | Value-first, product second | 1x per email | Single CTA per email |

---

## 3. Sales Message Scripts

### 3.1 WhatsApp -- Initial Contact (D2C)

```
Oi [nome]!

Aqui eh {{BRAND_PERSONA_NAME}} da {{BRAND_NAME}}. 😊

Você perguntou sobre [produto/problema]. Tenho aqui exatamente o que você precisa:

👉 [nome do produto] -- [beneficio principal em 1 frase]
💰 [preco] | Frete grátis acima de [valor]
🔗 [link direto]

Qualquer dúvida é só falar! 🐾
```

**Customize:**
- Persona name: `{{BRAND_PERSONA_NAME}}`
- Voice: `{{BRAND_VOICE_TONE}}`
- Frete threshold: replace with your policy

### 3.2 WhatsApp -- B2B Initial Pitch

```
Ola [nome do contato], tudo bem?

Sou [nome] da {{BRAND_NAME}}. Vi que você tem [tipo de negocio] e imagino
que os nossos produtos de {{BRAND_VERTICAL}} podem complementar seu catalogo.

Trabalhamos com parceiros em [regiao] com:
- Tabela exclusiva com [desconto %]
- Suporte dedicado via WhatsApp
- Catalogo completo de [X SKUs]

Posso te enviar mais detalhes? Leva 2 minutos. 🙂
```

### 3.3 WhatsApp -- Follow-Up (No Response)

```
Oi [nome], tudo certo?

So passando para ver se recebeu minha mensagem anterior sobre a parceria
{{BRAND_NAME}}.

Se quiser, posso mandar o catalogo completo no melhor momento pra voce.

Abracos! 🐾
```

### 3.4 Email -- Welcome (Post-Purchase D2C)

```
Subject: Seu pedido {{BRAND_NAME}} esta a caminho! 🎁

Ola [nome],

Seu pedido foi confirmado e ja esta sendo preparado com carinho.

Enquanto espera, aqui vai uma dica rapida sobre {{BRAND_VERTICAL}}: [dica educacional 2-3 linhas]

Tambem separamos para voce: [produto complementar] -- voce tem [desconto %] de desconto na proxima compra com o cupom: [cupom]

Qualquer duvida: {{BRAND_PARTNER_EMAIL}} ou WhatsApp

[Assinatura {{BRAND_PERSONA_NAME}}]
```

---

## 4. AI Sales Assistant Integration

The AI sales assistant ({{BRAND_PERSONA_NAME}}) integrates product recommendations into conversational flows:

### 4.1 Recommendation Trigger Patterns

| User signal | AI action |
|-------------|-----------|
| "meu [animal] nao dorme bem" | Product rec: [sleep/comfort product from catalog] |
| "orcamento limitado" | Budget-filtered recommendation (<= X) |
| "qual o melhor presente para..." | Gift-fit recommendation from {{BRAND_PRODUCT_CATALOG}} |
| "quero comprar varios" | B2B channel suggestion |

### 4.2 Recommendation Format

```
Problem detected: [user issue]
Budget: [if stated]
Recommendation: [product name]
  - Why it fits: [1-2 sentences]
  - Price: [range or exact]
  - CTA: [link or next step]
```

---

## 5. B2B Sales Flow

```
PROSPECT                   PITCH                      CLOSE                  ONBOARD
--------                   -----                      -----                  -------
Identify (CNPJ validation) -> WhatsApp intro message -> Catalog + pricing ->  Portal + first order
Social DM / referral       -> Follow-up x2 (D3, D7)  -> Objection handling ->  Tier assignment
Inbound (b2b form)         -> Video call (optional)   -> Contract / terms  ->  Support introduction
```

### 5.1 Objection Handling

| Objection | Response |
|-----------|---------|
| "Ja tenho fornecedor" | "Entendo. Muitos parceiros nos usam como complemento. Posso te mostrar o que diferencia {{BRAND_NAME}}?" |
| "Margem muito baixa" | "Depende do volume. Com X unidades/mes, voce fica em [margem %]. Qual seu volume atual?" |
| "Preciso ver o produto primeiro" | "Mandamos amostra. Qual seu endereco?" |
| "Nao tenho budget agora" | "Nosso plano starter eh gratuito. Voce so paga no primeiro pedido." |

---

## 6. Sales Metrics

| Metric | Example benchmark | Your target |
|--------|-----------------|-------------|
| WhatsApp response rate | 40-60% | (your data) |
| D2C email open rate | 25-40% | (your data) |
| B2B conversion rate (lead -> active) | 15-25% | (your data) |
| Average B2B first order value | 3-5x AOV | (your data) |
| Time to first B2B order | 3-14 days | (your data) |

---

## New Brand Variables

- `BRAND_VOICE_TONE` -- voice descriptor (e.g. "warm, educational, friendly")
- `BRAND_WHATSAPP_B2B` -- B2B WhatsApp number
- `BRAND_PERSONA_NAME` -- AI/brand persona name for signing messages
