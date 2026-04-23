---
id: output_content_factory_business_model
kind: content_monetization
pillar: P04
mission: MISSION_content_factory_v1
title: "Content Factory as a Service — Business Model & Positioning"
version: 1.0.0
created: 2026-04-06
author: n06_commercial
domain: monetization-strategy
quality: 9.0
tags: [business-model, content-factory, monetization, positioning, pricing, market, gtm, cex]
tldr: "Modelo de negócio completo para Content Factory autônoma: análise de 10 competidores com preços reais, ICP priorizado, modelo híbrido OSS+SaaS, pricing R$197-2997/mês, mapa de posicionamento 2D, GTM para CEX como caso #1."
density_score: 1.0
related:
  - spec_content_factory_v1
  - n06_self_review_20260402
  - n07_output_monetization_consolidated
  - output_content_factory_landscape
  - n04_output_monetization_curriculum
  - agent_card_n02
  - p12_dr_commercial
  - n06_competitive_business
  - p01_kc_brand_voice_systems
  - p01_kc_brand_book_patterns
---

# Content Factory as a Service — Business Model & Positioning

> Pipeline completo: Brief → Research → Script → Slides → Vídeo → Voz → Curso → eBook → Publish
> Produzido por N06 Commercial · MISSION_content_factory_v1 · 2026-04-06

---

## 1. EXECUTIVE SUMMARY

**O Produto**: Uma fábrica de conteúdo digital autônoma alimentada pelo sistema CEX. Recebe um brief ("quero um curso sobre X para devs") e entrega em minutos: script, slides, vídeo, narração, PDF, curso estruturado e landing page — tudo com a voz e identidade da marca do cliente.

**O Gap de Mercado**: Existem ferramentas excelentes para CADA formato (Jasper para copy, HeyGen para vídeo, Coursebox para cursos). Mas nenhuma conecta research → script → video → course → publish em um único pipeline com brand consistency automática. O cliente atual usa 6-8 ferramentas distintas, paga 6-8 assinaturas, e ainda assim precisa costurar tudo manualmente.

**Nossa Proposta**: 1 brief → 7+ outputs prontos para publicar, todos com o mesmo tom, cores, persona. Custo menor que a soma das ferramentas individuais.

**Modelo Recomendado**: Open-source (GitHub MIT) + SaaS tiers + Cursos pagos. Três fluxos de receita que se reforçam: o repo gera comunidade → a comunidade compra cursos → os cursos convertem para SaaS.

**Projeção Ano 1**: R$176K (conservador) → R$441K (base) → R$882K (otimista)

---

## 2. MARKET ANALYSIS — Competidores e Gaps

### 2.1 Mapa de Competidores por Categoria

| Categoria | Ferramenta | Plano Entrada | Plano Pro | Limitação Central |
|-----------|-----------|--------------|-----------|-------------------|
| **Copy AI** | Jasper | $49/mês | $69/mês | Copy only. Não cria vídeo, curso, PDF |
| **Copy AI** | Copy.ai | $29/mês | $249/mês | Copy + brand voice. Sem vídeo/curso |
| **Copy AI** | Writesonic | $49/mês | $249/mês | Copy + SEO. Sem vídeo, sem curso |
| **AI Video** | Synthesia | $29/mês (10min) | $89/mês (30min) | Vídeo apenas. Sem script, sem curso |
| **AI Video** | HeyGen | $29/mês | $99/mês | Vídeo + avatar. Sem conteúdo, sem funil |
| **Repurpose** | Pictory | $25/mês (30 vids) | $49/mês (60 vids) | Texto → vídeo. Sem curso, sem brand |
| **AI Video** | InVideo | $28/mês | $60/mês | Vídeo gerado. Sem research, sem curso |
| **AI Voice** | ElevenLabs | $5/mês | $22/mês (100K chars) | Voz apenas. Não integra pipeline |
| **AI Slides** | Gamma | $10/mês | $20/mês | Apresentações. Sem vídeo, sem curso |
| **AI Courses** | Coursebox | $21/mês | $210/mês | Cursos apenas. Sem vídeo, sem copy |

**Custo se usar todas**: $49 + $29 + $89 + $22 + $10 + $21 = **$220/mês mínimo** para ter as principais categorias. E ainda assim o cliente costura manualmente, perde brand consistency, e não tem pipeline automático.

### 2.2 O Gap Real

Nenhum player atual oferece:
1. **End-to-end pipeline**: research → script → slides → vídeo → voz → curso → PDF → publish
2. **Brand config system**: 1 YAML define voz, cores, persona — propagada em TODOS os outputs
3. **Multi-formato de 1 brief**: 1 input → 7+ outputs prontos
4. **Open-source core**: framework público, extensível, auditável
5. **Qualidade controlada**: 8F pipeline com gates de qualidade em cada etapa

### 2.3 Adjacentes (não diretos)

| Empresa | Modelo | Por que não compete diretamente |
|---------|--------|--------------------------------|
| **Descript** | Vídeo + transcrição | Edição manual, não pipeline automático |
| **Opus Clip** | Repurpose vídeos longos | Reprocessa existentes, não cria do zero |
| **Repurpose.io** | Distribuição multi-canal | Distribuição, não criação |
| **ContentFries** | Corte automático | Post-production apenas |
| **Missinglettr** | Social scheduling | Distribuição de posts, não factory completo |

---

## 3. ICP — IDEAL CUSTOMER PROFILE

### 3.1 Segmentos Rankeados por Prioridade

**PRIORIDADE 1 — Infoprodutor Técnico**
- **Quem é**: Dev, engenheiro, consultor que quer empacotar conhecimento como curso
- **Dor**: "Sei muito sobre X mas não sei gravar vídeo, montar slides, estruturar módulos"
- **Trigger**: Quer lançar em 30 dias, não em 6 meses
- **Willingness to pay**: R$497-997 one-shot OU R$197/mês SaaS
- **CAC estimado**: R$45-89 (YouTube + LinkedIn orgânico)
- **Por que primeiro**: Dor imediata + fácil de encontrar (GitHub, Twitter/X, devs communities) + valida produto rápido

**PRIORIDADE 2 — Agência de Marketing Digital**
- **Quem é**: Agência com 5-50 clientes que produz conteúdo recorrente
- **Dor**: "Preciso escalar produção sem contratar mais pessoas"
- **Trigger**: Perder cliente por demora na entrega / custo por post muito alto
- **Willingness to pay**: R$997-2997/mês (dilui em N clientes)
- **CAC estimado**: R$200-500 (LinkedIn Ads + referral)
- **Por que segundo**: LTV alto, MRR, mas ciclo de venda mais longo (2-4 semanas)

**PRIORIDADE 3 — Empresa SaaS / Startup**
- **Quem é**: SaaS early-stage que precisa de onboarding, demos, docs, tutoriais
- **Dor**: "Produto pronto mas sem conteúdo educacional para reduzir churn"
- **Trigger**: Alto churn por falta de educação do cliente
- **Willingness to pay**: $99-499/mês USD
- **CAC estimado**: $300-800 USD (Product Hunt, HackerNews, cold outreach)
- **Por que terceiro**: Paga em USD (maior margem), mas ciclo de venda maior e critério de compra mais exigente

**PRIORIDADE 4 — Criador de Conteúdo**
- **Quem é**: YouTuber, podcaster que quer replicar conteúdo em múltiplos formatos
- **Dor**: "Gravo 1 vídeo e quero ter posts, PDF, curso, newsletter automaticamente"
- **Willingness to pay**: R$47-197/mês
- **Nota**: Paga menos, churna mais. Bom para volume, ruim para LTV. **Secundário**.

### 3.2 Early Adopter Ideal (mês 1-3)

**Perfil**: Dev brasileiro, 28-40 anos, já usa LLMs no trabalho, ativo no GitHub, quer monetizar conhecimento mas não tem tempo para produção de conteúdo. Viu o repo do CEX, entendeu o pipeline, quer o mesmo para seu nicho específico.

**Canal**: GitHub stars → README com link para curso → Hotmart ou Kiwify checkout

---

## 4. MONETIZATION MODEL — Recomendação

### 4.1 Modelo Recomendado: Híbrido OSS + SaaS + Curso

```
┌─────────────────────────────────────────────────────────┐
│  TIER 0: OPEN-SOURCE (gratuito, MIT)                    │
│  → Repo GitHub público                                  │
│  → Cria comunidade + credibilidade + inbound            │
│  → Converte: 2-5% de stars em pagantes                  │
├─────────────────────────────────────────────────────────┤
│  TIER 1: CURSO (one-shot, R$497-997)                    │
│  → "CEX na Prática" — curso completo                    │
│  → Revenue imediato sem infra de SaaS                   │
│  → Financia desenvolvimento do SaaS                     │
├─────────────────────────────────────────────────────────┤
│  TIER 2: SaaS HOSTED (recorrente, R$197-2997/mês)       │
│  → Pipeline hospedado + brand config gerenciado         │
│  → Sem setup técnico para o cliente                     │
│  → MRR previsível, escalável                            │
├─────────────────────────────────────────────────────────┤
│  TIER 3: ENTERPRISE / SERVICE BUREAU                    │
│  → "Manda o brief, entregamos pronto"                   │
│  → R$5.000-15.000/projeto                               │
│  → Para validar casos de uso B2B antes de automatizar   │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Sequência de Lançamento

| Fase | Modelo Ativo | Objetivo | Timeline |
|------|-------------|----------|----------|
| **M1-M3** | OSS + Curso | Validar produto, gerar MRR inicial | Hoje |
| **M4-M6** | + SaaS Beta | Converter early adopters em MRR | 3 meses |
| **M7-M12** | + Agências | Escalar B2B, aumentar ARPU | 6 meses |
| **Ano 2** | + Enterprise | Service bureau → SaaS enterprise | 12 meses |

### 4.3 Avaliação de Modelos Alternativos

| Modelo | Pros | Cons | Veredicto |
|--------|------|------|-----------|
| Credit-based | Flexível, paga pelo uso | Complexo de precificar, imprevisível | **Futuro** (fase 2) |
| One-shot por projeto | Simples, alto ticket | Sem recorrência, não escala | **Validação** (fase 1 agências) |
| Template marketplace | Passive income | Ticket baixo, comoditiza | **Não prioritário** |
| Subscription | Recorrência, previsível | Precisa de infra, suporte | **Modelo principal** (fase 2) |

---

## 5. PRICING STRATEGY — Baseado em Pesquisa Real

### 5.1 Benchmark de Pricing dos Competidores (Preços Reais, Abril 2026)

| Ferramenta | Starter | Mid | Pro | Nota |
|-----------|---------|-----|-----|------|
| Jasper | $49/mês | $69/mês | Custom | Copy only |
| Copy.ai | $29/mês | $249/mês | — | Copy + agents |
| Writesonic | $49/mês | $99/mês | $249/mês | Copy + SEO |
| HeyGen | $29/mês | $99/mês | $149/mês | Vídeo |
| Synthesia | $29/mês | $89/mês | Custom | Vídeo |
| Pictory | $25/mês | $49/mês | $119/mês | Text→vídeo |
| InVideo | $28/mês | $60/mês | $899/mês (team) | Vídeo |
| ElevenLabs | $5/mês | $22/mês | $99/mês | Voz |
| Gamma | $10/mês | $20/mês | $100/mês | Slides |
| Coursebox | $21/mês | — | $210/mês | Cursos |

**Insights de pricing**:
- Stack completa (5 ferramentas básicas): ~$130-200/mês
- Nenhum player cobra mais de $249/mês para usuário individual
- B2B/enterprise: custom pricing começa em ~$500/mês
- Cursos one-shot: $97-497 USD no mercado internacional

### 5.2 Pricing CEX — Content Factory

**BRL (mercado BR)**:
| Tier | Nome | Preço | Inclui |
|------|------|-------|--------|
| **Free** | Starter | R$0 | Repo + docs + 3 briefs/mês |
| **Solo** | Builder | R$197/mês | 20 briefs, todos os formatos, 1 brand config |
| **Agência** | Studio | R$997/mês | 100 briefs, N clientes, 10 brand configs, priority support |
| **Empresa** | Factory | R$2.997/mês | Ilimitado, self-hosted, API, SLA, onboarding dedicado |
| **Curso** | CEX na Prática | R$497 (1x) | Módulos 1-8, certificado, acesso vitalício |
| **Curso Master** | CEX Master | R$997 (1x) | Módulo completo + templates + suporte 90 dias |

**USD (mercado INT)**:
| Tier | Nome | Preço | Inclui |
|------|------|-------|--------|
| **Solo** | Builder | $39/mês | 20 briefs, todos formatos |
| **Agência** | Studio | $197/mês | 100 briefs, N clients, priority |
| **Empresa** | Factory | $599/mês | Unlimited, API, SLA |
| **Curso** | CEX Course | $97 (1x) | Full course, certificate |

**Ancoragem Psicológica**:
- "Você já paga $130/mês em 5 ferramentas separadas. O CEX Factory faz tudo por $39/mês."
- "1 curso entregue = R$5.000 de hora de freelancer poupada. O Studio custa R$997/mês."

### 5.3 Custo de Produção por Output (Nossa Stack)

| Output | LLM Tokens | API Calls | Custo Estimado | Margem (Studio R$997) |
|--------|-----------|-----------|---------------|----------------------|
| Script 5min | ~8K tokens | 2-3 | ~R$0,80 | 99,9% |
| Slides (15 cards) | ~6K tokens | Gamma API | ~R$1,20 | 99,9% |
| Narração 5min | ElevenLabs | 45K chars | ~R$2,50 | 99,7% |
| Vídeo 5min | HeyGen API | $0,15/min | ~R$3,75 | 99,6% |
| eBook 30 pags | ~20K tokens | — | ~R$2,00 | 99,8% |
| **Brief completo (todos)** | — | — | **~R$10-15** | **98,5%+** |

Com 100 briefs/mês no plano Studio (R$997), custo direto: R$1.000-1.500 → **margem ~0%** no pior caso.
**Necessário**: cobrar R$997/mês para 50 briefs, ou R$1.997 para 100 briefs para garantir margem >30%.
**Decisão ajustada**: Studio R$997/mês = 30 briefs completos. Acima disso: créditos adicionais.

---

## 6. POSITIONING MAP — 10+ Players

```
Escopo do Output
(Full Pipeline)
     ▲
     │
 CEX │ ●━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━●
     │ (brief → all formats)           (futuro SaaS full-auto)
     │
     │
     │                 ● Copy.ai Agents ($249)
     │           ● Writesonic Pro ($249)
     │
     │
     │        ● Coursebox ($210)         ● Descript
     │
     │    ● Synthesia Enterprise
     │    ● HeyGen Business ($149)
     │
     │  ● Pictory Pro ($49)   ● InVideo Max ($60)
     │  ● Jasper Pro ($69)
     │  ● ElevenLabs ($22)
     │  ● Gamma Pro ($20)
     │
(Point Tool)
     └──────────────────────────────────────────► Automação
          Manual/Setup            Full-Auto
```

**Leitura do mapa**:
- Todos os competidores estão na metade inferior (point tools)
- Ninguém ocupa o quadrante superior direito (full pipeline + full auto) — **esse é o nosso espaço**
- O quadrante superior esquerdo seria uma agência humana ($10K+/projeto) — nós automatizamos isso

**Players no nosso quadrante**: Apenas agências de conteúdo tradicionais (~R$5-20K/projeto, manual).
**Diferencial de preço**: R$997/mês vs R$5.000+/projeto manual. ROI claro.

---

## 7. GTM PLAN — CEX como Caso #1

### 7.1 Overview dos Assets a Produzir

| Asset | Formato | Canal | CTA | Funil |
|-------|---------|-------|-----|-------|
| Repo público | GitHub | Organic / HN / Reddit | "Star → Docs → Curso" | TOFU |
| Vídeo demo 90s | YouTube Shorts / Reels | Paid + Organic | "Link na bio → curso" | TOFU |
| Vídeo tutorial 15min | YouTube | SEO orgânico | "Acessa o repo / compra curso" | MOFU |
| Pitch deck | SlideShare / LinkedIn | LinkedIn orgânico | "DM para demo" | MOFU |
| eBook "CEX em 30 páginas" | PDF gated | Landing page | "Entra para email list" | MOFU |
| Curso "CEX na Prática" | Hotmart (BR) + Digistore24 (INT) | Afiliados + email | "R$497 / $97" | BOFU |
| Newsletter semanal | Substack | Orgânico | "Subscribe free → upgrade" | MOFU |

### 7.2 Sequência de Lançamento (8 semanas)

```
Semana 1-2: FUNDAÇÃO
  ✅ README reescrito (já feito — C764F30)
  ✅ QUICKSTART + requirements
  □ Landing page simples (GitHub Pages)
  □ eBook gerado pela própria Content Factory

Semana 3-4: CONTEÚDO
  □ Vídeo demo 90s (HeyGen ou gravação própria)
  □ Pitch deck (Gamma)
  □ Post "I built a content factory in 30 days" (HN + Reddit)
  □ 5 posts LinkedIn sobre o pipeline 8F

Semana 5-6: CURSO
  □ Script do curso (8 módulos)
  □ Slides de cada módulo (Gamma)
  □ Gravação / narração
  □ Upload Hotmart (BR) + Digistore24 (INT)
  □ Email sequence 5 dias (pré-lançamento)

Semana 7-8: LANÇAMENTO
  □ Product Hunt submission
  □ HackerNews: "Show HN: CEX — typed knowledge system"
  □ Afiliados recrutados (5-10 devs/consultores)
  □ Launch email para lista
```

### 7.3 Métricas de Sucesso (Mês 1-3)

| Métrica | Target M1 | Target M3 | Canal |
|---------|-----------|-----------|-------|
| GitHub Stars | 200 | 1.000 | HN + Reddit + LinkedIn |
| Email subscribers | 150 | 500 | eBook gated + newsletter |
| Alunos (curso) | 20 | 100 | Hotmart + afiliados |
| MRR (SaaS beta) | R$0 | R$2.000 | Direct outreach |
| Receita total | R$9.940 | R$65.000 | Cursos |

### 7.4 Canal por Segmento ICP

| ICP | Canal Principal | Mensagem | CTA |
|-----|----------------|---------|-----|
| Infoprodutor técnico | YouTube + GitHub | "De repo para curso em 1 brief" | Compra curso R$497 |
| Agência BR | LinkedIn + indicação | "Escale sem contratar" | Demo gratuita → Studio R$997/mês |
| SaaS startup | HN + Twitter/X | "Reduce time-to-content by 10x" | Free trial → Builder $39/mês |

---

## 8. BRAND CONFIG SEED — CEX

```yaml
# .cex/brand/brand_config.yaml — Seed para CEX
# Validar: python _tools/brand_validate.py
# Propagar: python _tools/brand_propagate.py

identity:
  BRAND_NAME: "CEX"
  BRAND_TAGLINE: "The typed knowledge system that builds itself"
  BRAND_SLOGAN: "Brief in. Everything out."
  BRAND_MISSION: "Transformar conhecimento especializado em produtos de conteúdo completos, sem atrito de produção — para devs, agências e infoprodutores."
  BRAND_VISION: "Todo especialista com um brief consegue lançar um produto de conteúdo profissional em menos de 1 hora."
  BRAND_VALUES:
    - "Qualidade como gate, não como aspiração"
    - "Transparência: código aberto, pipeline auditável"
    - "Velocidade sem trade-off de identidade"
  BRAND_STORY: "CEX nasceu da frustração de usar 8 ferramentas diferentes para produzir 1 curso. O X é uma variável — qualquer marca, mesmo pipeline, zero compromisso com identidade."

archetype:
  BRAND_ARCHETYPE: "magician"
  BRAND_ARCHETYPE_SHADOW: "trickster"
  BRAND_PERSONALITY:
    - "técnico-confiante"
    - "direto-sem-enrolação"
    - "builder-minded"
    - "obsessivamente-sistemático"

voice:
  BRAND_VOICE_TONE: "técnico, confiante, direto. Fala como um senior engineer, não como um vendedor."
  BRAND_VOICE_FORMALITY: 2
  BRAND_VOICE_DO:
    - "Use termos técnicos precisos (pipeline, artifact, nucleus, kind)"
    - "Mostre o sistema por trás, não só o resultado"
    - "Seja específico: números reais, nomes reais, paths reais"
  BRAND_VOICE_DONT:
    - "Evite superlatives vazios (revolucionário, incrível, game-changer)"
    - "Não esconda a complexidade — celebre-a"
    - "Não use o ! como substituto de substância"

visual:
  PRIMARY_HEX: "#0D1117"
  SECONDARY_HEX: "#161B22"
  ACCENT_HEX: "#58A6FF"
  SUCCESS_HEX: "#3FB950"
  WARNING_HEX: "#D29922"
  DANGER_HEX: "#F85149"
  BG_HEX: "#010409"
  FG_HEX: "#C9D1D9"
  HEADING_FONT: "JetBrains Mono"
  BODY_FONT: "Inter"
  BRAND_STYLE: "dark-terminal-minimal"
  BRAND_AESTHETIC: "GitHub dark + terminal green — código como arte"

market:
  BRAND_ICP_PRIMARY: "Engenheiros e devs que querem monetizar conhecimento como infoproduto"
  BRAND_ICP_SECONDARY: "Agências digitais BR que precisam escalar produção de conteúdo"
  BRAND_ICP_TERTIARY: "Startups SaaS que precisam de conteúdo educacional"
  BRAND_LANGUAGE: "pt-BR"
  BRAND_LANGUAGE_SECONDARY: "en"
  BRAND_REGION: "BR/LATAM primary, global secondary"
  BRAND_COMPETITION: "Jasper, HeyGen, Coursebox — mas nenhum tem o pipeline completo"

pricing:
  BRAND_PRICING_MODEL: "hybrid"
  BRAND_PRICING_TIERS:
    - name: "Free"
      price_brl: 0
      price_usd: 0
      description: "Repo + docs + 3 briefs/mês"
    - name: "Builder"
      price_brl: 19700
      price_usd: 3900
      description: "20 briefs/mês, todos os formatos, 1 brand config"
    - name: "Studio"
      price_brl: 99700
      price_usd: 19700
      description: "30 briefs completos/mês, 10 brand configs, priority"
    - name: "Factory"
      price_brl: 299700
      price_usd: 59900
      description: "Ilimitado, API, SLA, onboarding, self-hosted option"
  BRAND_CHECKOUT_PRIMARY: "kiwify"
  BRAND_CHECKOUT_SECONDARY: "digistore24"
  BRAND_CURRENCY_PRIMARY: "BRL"
  BRAND_CURRENCY_SECONDARY: "USD"

distribution:
  BRAND_COURSE_PLATFORM_BR: "hotmart"
  BRAND_COURSE_PLATFORM_INT: "digistore24"
  BRAND_COMMUNITY: "GitHub Discussions + Discord"
  BRAND_CONTENT_CHANNELS:
    - "github"
    - "youtube"
    - "linkedin"
    - "hackernews"
    - "twitter-x"
  BRAND_EMAIL_PROVIDER: "resend"
```

---

## 9. REVENUE PROJECTIONS

### 9.1 Premissas

| Premissa | Valor |
|----------|-------|
| Ticket médio curso BR | R$697 (mix Builder R$497 + Master R$997) |
| ARPU SaaS Solo | R$197/mês |
| ARPU SaaS Studio | R$997/mês |
| Churn mensal SaaS | 8% |
| Conversão GitHub Star → curso | 0,5% |
| Conversão curso → SaaS | 12% |
| Comissão Hotmart/DS24 | 5% |

### 9.2 Cenário Conservador (Meses 1-12)

**Base**: 10 alunos/mês (cursos) + crescimento orgânico SaaS

| Mês | Alunos (R$697) | SaaS Solo | SaaS Studio | Receita Bruta | Receita Líquida |
|-----|----------------|-----------|-------------|---------------|-----------------|
| M01 | 10 × R$697 | 0 | 0 | R$6.970 | R$6.622 |
| M02 | 12 × R$697 | 2 × R$197 | 0 | R$8.758 | R$8.320 |
| M03 | 14 × R$697 | 4 × R$197 | 0 | R$10.546 | R$10.019 |
| M06 | 20 × R$697 | 10 × R$197 | 2 × R$997 | R$17.906 | R$17.011 |
| M09 | 28 × R$697 | 18 × R$197 | 4 × R$997 | R$27.478 | R$26.104 |
| M12 | 38 × R$697 | 28 × R$197 | 7 × R$997 | R$37.382 | R$35.513 |

**Total Ano 1 (Conservador)**: ~R$220K líquido

### 9.3 Cenário Base (Meses 1-12)

**Base**: 25 alunos/mês + aquisição ativa SaaS

| Mês | Alunos | SaaS Solo | SaaS Studio | Receita Bruta |
|-----|--------|-----------|-------------|---------------|
| M01 | 25 × R$697 | 0 | 0 | R$17.425 |
| M03 | 30 × R$697 | 8 × R$197 | 2 × R$997 | R$23.500 |
| M06 | 40 × R$697 | 20 × R$197 | 6 × R$997 | R$37.722 |
| M09 | 55 × R$697 | 35 × R$197 | 12 × R$997 | R$57.221 |
| M12 | 75 × R$697 | 50 × R$197 | 20 × R$997 | R$82.115 |

**Total Ano 1 (Base)**: ~R$550K líquido

### 9.4 Cenário Otimista (Product-Led Growth)

**Base**: Viral GitHub traction + 50+ alunos/mês + SaaS escala

| Mês | Alunos | SaaS Solo | SaaS Studio | Receita Bruta |
|-----|--------|-----------|-------------|---------------|
| M01 | 50 × R$697 | 0 | 0 | R$34.850 |
| M03 | 80 × R$697 | 20 × R$197 | 5 × R$997 | R$64.625 |
| M06 | 120 × R$697 | 50 × R$197 | 15 × R$997 | R$109.425 |
| M12 | 200 × R$697 | 100 × R$197 | 40 × R$997 | R$198.680 |

**Total Ano 1 (Otimista)**: ~R$1,1M líquido

### 9.5 Unit Economics por Tier

| Tier | Preço | CAC | LTV (12 meses) | Payback |
|------|-------|-----|----------------|---------|
| Curso Builder (1x) | R$497 | R$45 | R$497 | 1,1 meses |
| Curso Master (1x) | R$997 | R$89 | R$997 | 1,1 meses |
| SaaS Solo | R$197/mês | R$89 | R$2.161 (11×) | 0,5 meses |
| SaaS Studio | R$997/mês | R$450 | R$10.966 (11×) | 0,5 meses |

---

## 10. RISKS & MITIGATIONS

| Risco | Probabilidade | Impacto | Mitigação |
|-------|--------------|---------|-----------|
| **Competidor lança pipeline completo** (OpenAI, Anthropic) | Alta | Alto | Diferencial: open-source + brand system + BR-first + 8F quality gates |
| **Custo de API sobe 3x** | Média | Médio | Créditos pré-pagos + caching de outputs + modelos menores onde possível |
| **Churn SaaS > 15%** | Média | Alto | Onboarding estruturado + certificação + community lock-in |
| **Produto difícil demais para infoprodutor** | Alta | Alto | Hosted version com UI no-code + templates prontos |
| **Margem zerada por custo de API** | Baixa | Alto | Floor margin calculado: R$997/30 briefs = R$33/brief, custo direto R$12 → margem 64% |
| **GitHub repo não gera leads** | Média | Médio | Newsletter gated + eBook + landing page independente |
| **Regulação AI no Brasil** | Baixa | Médio | Pipeline auditável (8F) + conteúdo gerado marcado como AI-assisted |
| **Hotmart/DS24 bane conta** | Baixa | Alto | Multi-plataforma: Kiwify + Hotmart + DS24 + Stripe como fallback |

---

## APÊNDICE: Stack de Produção Estimada

Para um brief completo gerando todos os 7 outputs:

| Etapa | Ferramenta | Custo/Brief | Alternativa OSS |
|-------|-----------|-------------|-----------------|
| Research | Claude Opus 4.6 | ~R$1,20 (8K tokens) | — |
| Script | Claude Sonnet 4.6 | ~R$0,40 (6K tokens) | Llama 3.3 (grátis) |
| Slides | Gamma API | ~R$0,80 (10 slides) | reveal.js template |
| Narração | ElevenLabs Creator | ~R$2,50 (45K chars) | Coqui TTS (grátis) |
| Vídeo | HeyGen Creator | ~R$3,75 (1min) | Auto-editor local |
| PDF/eBook | LaTeX/WeasyPrint | ~R$0,00 | Markdown → PDF |
| Publicação | API Hotmart/DS24 | ~R$0,00 | Manual webhook |
| **TOTAL** | | **~R$8-12/brief** | **R$1-2/brief (OSS)** |

Margem no plano Studio (R$997 / 30 briefs = R$33,23/brief): **64-76%**
Margem no plano Builder (R$197 / 20 briefs = R$9,85/brief): **15-20%** (breakeven — necessário ajuste)

**Ajuste recomendado Builder**: R$197/mês para **10 briefs** (não 20). Ou elevar para R$297/mês para 20 briefs.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_content_factory_v1]] | downstream | 0.26 |
| [[n06_self_review_20260402]] | downstream | 0.20 |
| [[n07_output_monetization_consolidated]] | downstream | 0.20 |
| [[output_content_factory_landscape]] | upstream | 0.20 |
| [[n04_output_monetization_curriculum]] | downstream | 0.19 |
| [[agent_card_n02]] | downstream | 0.19 |
| [[p12_dr_commercial]] | downstream | 0.19 |
| [[n06_competitive_business]] | downstream | 0.18 |
| [[p01_kc_brand_voice_systems]] | upstream | 0.18 |
| [[p01_kc_brand_book_patterns]] | upstream | 0.18 |
