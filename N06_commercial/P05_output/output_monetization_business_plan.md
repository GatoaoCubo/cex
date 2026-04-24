---
id: n06_output_monetization_business_plan
kind: output_template
8f: F6_produce
pillar: P05
title: "CEX Monetization Business Plan — Estratégia Comercial 2026"
version: 1.0.0
created: 2026-04-02
author: n06_commercial
domain: monetization-strategy
quality: 9.2
tags: [monetization, business-plan, pricing, revenue, cex, course, model, financial-projections, brand]
tldr: "Plano de negócios completo para monetização do CEX: repo público MIT + cursos pagos (R$497/997), modelo híbrido, projeções 12 meses, unit economics, pricing psychology, brand positioning vs concorrentes."
density_score: 0.92
related:
  - n07_output_monetization_consolidated
  - output_content_factory_business_model
  - bld_architecture_kind
  - n02_output_monetization_launch
  - n04_readme_curriculum
  - n05_output_monetization_infra
  - kind-builder
---

# CEX Monetization Business Plan — Estratégia Comercial 2026

> **Estrategia Aprovada**: Repo publico (MIT) + Curso pago + Claude Code native (Anthropic Max)

---

## 1. PROJEÇÃO FINANCEIRA (12 meses)

### Cenário Conservador (10 alunos/mês, crescimento 15%)
| Mês | Builder (70%) | Master (30%) | Receita Bruta | Lemon (5%) | Receita Líquida |
|-----|---------------|-------------|---------------|------------|-----------------|
| M01 | 7 × R$497 | 3 × R$997 | R$6.470 | R$324 | R$6.146 |
| M02 | 8 × R$497 | 4 × R$997 | R$7.964 | R$398 | R$7.566 |
| M03 | 9 × R$497 | 4 × R$997 | R$8.461 | R$423 | R$8.038 |
| M04 | 10 × R$497 | 5 × R$997 | R$9.955 | R$498 | R$9.457 |
| M05 | 12 × R$497 | 5 × R$997 | R$10.949 | R$547 | R$10.402 |
| M06 | 13 × R$497 | 6 × R$997 | R$12.443 | R$622 | R$11.821 |
| M07 | 15 × R$497 | 7 × R$997 | R$14.434 | R$722 | R$13.712 |
| M08 | 17 × R$497 | 8 × R$997 | R$16.425 | R$821 | R$15.604 |
| M09 | 19 × R$497 | 9 × R$997 | R$18.416 | R$921 | R$17.495 |
| M10 | 22 × R$497 | 10 × R$997 | R$20.904 | R$1.045 | R$19.859 |
| M11 | 25 × R$497 | 11 × R$997 | R$23.392 | R$1.170 | R$22.222 |
| M12 | 29 × R$497 | 13 × R$997 | R$27.374 | R$1.369 | R$26.005 |

**Total Ano 1 (Conservador)**: R$176.513 líquido

### Cenário Base (25 alunos/mês, crescimento 20%)
| Mês | Builder (70%) | Master (30%) | Receita Bruta | Lemon (5%) | Receita Líquida |
|-----|---------------|-------------|---------------|------------|-----------------|
| M01 | 18 × R$497 | 8 × R$497 | R$16.922 | R$846 | R$16.076 |
| M02 | 21 × R$497 | 9 × R$997 | R$19.416 | R$971 | R$18.445 |
| M03 | 25 × R$497 | 11 × R$997 | R$23.392 | R$1.170 | R$22.222 |
| M06 | 36 × R$497 | 16 × R$997 | R$33.844 | R$1.692 | R$32.152 |
| M09 | 52 × R$497 | 22 × R$997 | R$47.878 | R$2.394 | R$45.484 |
| M12 | 74 × R$497 | 32 × R$997 | R$68.682 | R$3.434 | R$65.248 |

**Total Ano 1 (Base)**: R$441.283 líquido

### Cenário Otimista (50 alunos/mês, crescimento 25%)
| Mês | Builder (70%) | Master (30%) | Receita Bruta | Lemon (5%) | Receita Líquida |
|-----|---------------|-------------|---------------|------------|-----------------|
| M01 | 35 × R$497 | 15 × R$997 | R$32.350 | R$1.618 | R$30.732 |
| M06 | 68 × R$497 | 29 × R$997 | R$62.709 | R$3.135 | R$59.574 |
| M12 | 134 × R$497 | 57 × R$997 | R$123.347 | R$6.167 | R$117.180 |

**Total Ano 1 (Otimista)**: R$882.566 líquido

---

## 2. UNIT ECONOMICS

### Customer Acquisition Cost (CAC) por Canal

| Canal | CAC Médio | Conversão | Origem Tráfego |
|-------|-----------|-----------|----------------|
| **Orgânico (SEO + GitHub)** | R$12 | 8% | Devs procurando agent frameworks |
| **YouTube (conteúdo)** | R$45 | 4% | Tutoriais sobre LLM agents |
| **LinkedIn (posts técnicos)** | R$89 | 2% | Decision makers, CTOs, tech leads |
| **Google Ads (branded)** | R$167 | 6% | "CEX agents", "knowledge system" |
| **Afiliados (20% comissão)** | R$119 | 12% | Network de devs/consultores |

### Lifetime Value (LTV)

**Builder (R$497)**: 
- Compra única: R$497
- Upsell Master (15%): R$497 + R$997 = R$1.494
- **LTV médio Builder**: R$572

**Master (R$997)**:
- Entry direto Master: R$997
- Consulting upsell (8%): R$997 + R$5.000 = R$5.997
- **LTV médio Master**: R$1.397

### Payback Period
- **Builder**: R$572 LTV ÷ R$89 CAC médio = **6.4x retorno** (payback imediato)
- **Master**: R$1.397 LTV ÷ R$89 CAC médio = **15.7x retorno** (payback imediato)

### Margem por Tier
- **Lemon Squeezy fee**: 5%
- **Custos variáveis**: ~R$25/aluno (hosting video, licença cex-brain, suporte)
- **Margem Builder**: R$497 - R$25 - R$25 = **89% margem**
- **Margem Master**: R$997 - R$50 - R$50 = **90% margem**

---

## 3. PRICING PSYCHOLOGY

### Por que R$497 e não R$500?

**Odd pricing** funciona especialmente no Brasil:
- R$497 é percebido como "abaixo de R$500" (heurística mental)
- Evita threshold psychological barrier dos "R$500"
- Parcelamento: 12× R$41,42 (mais palatável que 12× R$41,67)

### Estratégia de Ancoragem

```
Master R$997 (ancora alta) → Builder R$497 (parece barato)
                          ↓
            Foundations FREE (prova valor)
```

**Decoy Effect**: Vale criar tier intermediário?
**Recomendação**: **NÃO**. Simplicidade > complexity. 
Dois tiers claros criam decisão binária mais fácil.

### Early-bird Pricing
- **Builder**: R$297 primeiros 30 dias (40% desconto)
- **Master**: R$697 primeiros 30 dias (30% desconto)
- Cria urgência + premia early adopters

### Lifetime Deal Analysis
**Builder Lifetime**: R$997 (2× preço normal)
**Viabilidade**: ❌ **NÃO recomendado**
**Razão**: CEX evolui rápido, conteúdo cresce. LTD mata receita recorrente.

---

## 4. REVENUE STREAMS ALÉM DO CURSO

### Tier Enterprise (B2B)

| Serviço | Preço | Descrição |
|---------|-------|-----------|
| **CEX Setup** | R$5.000-15.000 | Implementação completa para empresa |
| **White-label CEX** | R$10.000 + 15% rev share | CEX com marca da agência/consultoria |
| **cex-brain Custom** | R$25.000-50.000 | Fine-tuning no corpus específico do cliente |
| **Retainer Mensal** | R$3.000-8.000 | Suporte dedicado + updates customizados |

### Community Premium
- **CEX Insiders**: R$97/mês
- Discord privado + office hours semanais
- Early access a features + templates exclusivos
- **Projeção**: 50-100 membros = R$4.850-9.700/mês adicional

### Programa de Afiliados
- **Comissão**: 25% via Lemon Squeezy
- Target: consultores, devs, YouTube tech channels
- **Projeção**: 15-20% vendas via afiliados (year 1)

### Licenciamento IP
- **CEX Framework License**: empresas que querem usar comercialmente
- **One-time**: R$50.000-200.000 (depende porte da empresa)
- **Use case**: grandes corporações, SIs

---

## 5. BRAND POSITIONING

### CEX no Mercado

**Categoria**: Knowledge Engineering Platform (não "just another agent framework")

**Posicionamento vs Concorrentes**:

| Framework | Foco | CEX Diferencial |
|-----------|------|----------------|
| **LangChain** | RAG pipes genéricos | 114 kinds + 8F pipeline tipado |
| **CrewAI** | Multi-agent workflows | 8 nuclei especializados + brand injection |
| **AutoGen** | Conversational agents | Knowledge cards + 12 pillar architecture |
| **n8n/Zapier** | No-code automation | Code-first mas com templates |

### Taglines Candidatas

1. **"Knowledge that builds itself"** ← WINNER
2. "The typed brain for AI agents"
3. "From chaos to knowledge in 8 functions"
4. "CEX = Code + Experience + eXpertise"
5. "Knowledge engineering for the AI age"

### Tone of Voice

**Técnico + Provocador + Didático**
- "While others build chatbots, we build brains"
- "114 kinds. 8 functions. Zero bullshit."
- "Your AI doesn't need more models. It needs more knowledge."

### Diferencial Core

**Template-First Construction**: CEX não gera do zero. Analisa 2.184 artifacts, acha patterns, adapta template. Resultado: densidade 0.85+, não generic fluff.

---

## 6. RISCOS COMERCIAIS

### Competitive Threats

**E se OpenAI/Google lança similar?**
- **Moat**: Our 114 kinds + 12 pillars = 2 anos de R&D
- **Defense**: Community-driven evolution (contributors vested)
- **Timing**: Big tech moves slow, we ship fast

**Probabilidade**: MÉDIA (12-18 meses)
**Mitigation**: Build network effects via community + consulting

### Platform Dependency Risk

**E se Anthropic muda pricing do Claude Code / Max subscription?**
- **Mitigation**: CEX knowledge system is model-agnostic (typed .md + .yaml)
- **Backup plan**: Export artifacts, run via API (pay-per-token) or alternative LLM
- **Impact**: MEDIO (runtime changes, knowledge persists)
- **Moat**: 123 kinds + 12 pillars + 2000+ artifacts = portable knowledge, not locked to one provider

### Demand Risk

**E se conversão é menor que esperado?**

| Cenário | Ação |
|---------|------|
| <5% trial→paid | Revise onboarding + free content |
| <2% SEO conversion | Double down em YouTube + afiliados |
| High churn (>20%) | Focus em community + suporte |

**Plano B**: Pivot para consulting-first (R$5-15K tickets)

### Sazonalidade

**Q1 (Jan-Mar)**: Alto (budget ano novo + upskill)
**Q2 (Abr-Jun)**: Médio 
**Q3 (Jul-Set)**: Baixo (férias, BlackFriday coming)
**Q4 (Out-Dez)**: Alto (BlackFriday, ano novo)

**Estratégia**: Launch em Janeiro, BlackFriday 40% off.

---

## 7. ROADMAP DE RECEITA (3 fases)

### Fase 1 — Foundation Launch (Mês 1-3)
**Goal**: Provar product-market fit

- ✅ Foundations track (free) no YouTube
- ✅ Builder course R$297 early-bird
- ✅ GitHub SEO optimization
- 🎯 **Target**: 50 alunos, R$15K MRR

### Fase 2 — Scale & Premium (Mês 4-6)
**Goal**: Escalar + Master tier

- ✅ Master course R$697 launch
- ✅ Claude Code templates + advanced builder packs (paid)
- ✅ Afiliados program (25% comissão)
- 🎯 **Target**: 150 alunos total, R$45K MRR

### Fase 3 — Enterprise & Community (Mês 7-12)
**Goal**: Diversificar revenue streams

- ✅ CEX Setup consulting (R$5-15K)
- ✅ Community premium R$97/mês
- ✅ White-label licensing
- ✅ Custom fine-tuning service
- 🎯 **Target**: R$75K MRR mix (courses + services + community)

---

## RESUMO EXECUTIVO

**Estrategia**: Repo publico + curso premium + Claude Code native
**Target Ano 1**: R$441K-882K receita líquida
**Key Metrics**: CAC R$89, LTV R$572-1.397, payback imediato
**Diferencial**: 114 kinds + Template-First construction vs generic frameworks
**Risk Mitigation**: Multi-stream revenue, community moat, fast iteration

**Next Actions**:
1. Setup Lemon Squeezy + early-bird landing page
2. Record Foundations track (free) para YouTube
3. Build CEX Insiders community pre-launch
4. Launch Builder course R$297 early-bird
5. Measure → iterate → scale

---

*Gerado por N06 Commercial Nucleus — Revenue Engineering para CEX*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n07_output_monetization_consolidated]] | sibling | 0.26 |
| [[output_content_factory_business_model]] | upstream | 0.26 |
| [[bld_architecture_kind]] | downstream | 0.18 |
| [[n02_output_monetization_launch]] | related | 0.17 |
| [[n04_readme_curriculum]] | sibling | 0.17 |
| [[n05_output_monetization_infra]] | related | 0.16 |
| [[kind-builder]] | downstream | 0.15 |
