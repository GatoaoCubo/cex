---
id: e2e_gold_petshop_marketing
kind: golden_test
type: marketing
pillar: P01
title: "Gold Standard — Pet Shop CRM Marketing Artifacts"
version: 1.0.0
created: 2026-04-06
author: n02_marketing
scenario: S1
input: "faz um CRM pra pet shop"
quality: 9.0
tags: [e2e, gold-standard, petshop, crm, marketing, stress-test]
density_score: 1.0
---

# Pet Shop CRM — Marketing Gold Standard

> Scenario S1: "faz um CRM pra pet shop" — 5 words of vague pt-BR input.
> This is what 8F should produce when N02 handles the marketing layer.

---

## 1. Landing Page Copy

### Headline

**Seu pet shop no piloto automatico.**

### Subheadline

Agendamentos, fichas de clientes e lembretes de vacina — tudo em um so lugar.
Menos planilha. Mais banho-e-tosa.

### Benefit 1: Agenda Inteligente

Chega de WhatsApp perdido. Seus clientes agendam online, recebem confirmacao automatica,
e voce ve tudo num calendario visual. Cancelamento de ultima hora? O sistema ja oferece
o horario pra lista de espera.

### Benefit 2: Ficha Pet Completa

Raca, porte, alergias, vacinas, historico de servicos — tudo na ficha do pet.
Quando o cliente liga perguntando "quando foi a ultima vermifugacao do Thor?",
voce responde em 2 segundos. Profissionalismo que fideliza.

### Benefit 3: Lembretes que Vendem

Vacina vencendo? Banho mensal? O CRM manda lembrete automatico por WhatsApp.
Cada lembrete e uma venda que volta sozinha. Sem voce levantar o dedo.

### CTA (Primary)

**Teste gratis por 14 dias — sem cartao, sem contrato.**

### CTA (Secondary)

Ja atende mais de 50 pets por mes? Fale com nosso time e ganhe setup gratis.

---

## 2. Pricing Table

| | Starter | Pro | Premium |
|---|---------|-----|---------|
| **Preco/mes** | R$ 49 | R$ 129 | R$ 299 |
| **Pets cadastrados** | ate 100 | ate 500 | ilimitado |
| **Agendamento online** | sim | sim | sim |
| **Lembretes WhatsApp** | 50/mes | 300/mes | ilimitado |
| **Ficha pet completa** | sim | sim | sim |
| **Multi-unidade** | -- | ate 3 lojas | ilimitado |
| **Relatorios** | basico | avancado | avancado + BI |
| **Integracoes** | -- | iFood Pet, PagSeguro | todas + API |
| **Suporte** | email | chat prioritario | gerente dedicado |
| **Ideal para** | pet shop solo | rede pequena | franquias |

### Ancora de preco

> "Por menos de R$ 2 por dia, voce para de perder cliente por esquecimento."

### Gatilho de urgencia

> "Primeiros 100 assinantes: 3 meses pelo preco de 2."

---

## 3. Tagline Variations

| # | Tagline | Angulo |
|---|---------|--------|
| 1 | "Seu pet shop no piloto automatico." | Automacao / tempo livre |
| 2 | "Quem cuida dos pets merece um CRM que cuida de voce." | Empatia / reciprocidade |
| 3 | "Menos planilha. Mais banho-e-tosa." | Dor → solucao concreta |
| 4 | "O CRM que fala a lingua do pet shop." | Especializacao / nicho |
| 5 | "Cada lembrete e uma venda que volta sozinha." | Revenue / resultado |

### Recomendacao

Tagline #1 para hero da landing page (clareza + beneficio imediato).
Tagline #3 para ads (contraste dor/solucao em poucas palavras).
Tagline #5 para email marketing (resultado financeiro direto).

---

## Validation Criteria

These elements MUST be present for the gold standard to pass:

- **LP-01**: Headline exists and is under 60 characters
- **LP-02**: Subheadline expands on headline (not repeats it)
- **LP-03**: Exactly 3 benefit blocks, each with title + body
- **LP-04**: Primary CTA uses action verb + removes friction ("gratis", "sem cartao")
- **LP-05**: Pricing has exactly 3 tiers with clear differentiation
- **TG-01**: Exactly 5 tagline variations
- **TG-02**: Each tagline targets a different psychological angle
- **BR-01**: All copy in pt-BR (matching input language)
- **BR-02**: Tone is professional but warm (pet shop audience = small business owners)
- **BR-03**: No English jargon without explanation
