# Mission: MONETIZE_CEX — N02 Marketing Perspective
**Nucleus**: N02 Marketing | **Model**: claude/sonnet-4 | **Priority**: HIGH
**Output**: `N02_marketing/output/output_monetization_launch.md`
**Signal on complete**: `python _tools/signal_writer.py n02 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto (10-15min) + texto detalhado + exercícios práticos no CEX |
| Currículo | 3 tracks: Foundations (free, M01-M03) → Builder (pago, M04-M10) → Master (premium, M11-M14) |
| Pricing | Explorer R$0 / Builder R$497 / Master R$997. 12x sem juros, PIX -10% |
| Plataforma | Lemon Squeezy (5% fee, license keys, internacional) |
| Modelo FT | cex-brain:14b = download exclusivo tier pago. Gap: qwen3 genérico ~7.0 vs cex-brain ~9.0 |

## SUA MISSÃO (N02 — Marketing)

Produza um **plano de lançamento + estratégia de marketing** cobrindo:

### 1. Posicionamento
- Headline principal (1 frase que vende CEX)
- Subheadline (quem é pra, o que ganha)
- Comparação: "CEX é o X para Y" (analogia de mercado)
- 3 propostas de valor únicas (USPs)

### 2. Funil de conversão
- TOFU: como atrair (GitHub, Twitter/X, YouTube, LinkedIn, comunidades)
- MOFU: como nutrir (conteúdo free, preview modules, newsletter)
- BOFU: como converter (landing page, urgência, prova social)
- Diagrama do funil com métricas esperadas por etapa

### 3. Copy da landing page
- Hero section (headline + subheadline + CTA)
- Seção "O que você vai construir" (outcomes, não features)
- Seção de prova social (badges, stars, metrics do repo)
- Seção de pricing (3 tiers com copy persuasiva)
- FAQ section (objeções comuns respondidas)

### 4. Plano de lançamento (90 dias)
- Pré-launch (semana 1-4): o que fazer antes de abrir vendas
- Launch (semana 5-6): como gerar pico de conversão
- Post-launch (semana 7-12): como manter tração
- Canais, frequência de posts, tipos de conteúdo

### 5. Métricas de sucesso
- KPIs por fase (views, signups, conversão, receita)
- Meta de lançamento (mês 1, mês 3, mês 6)

## Tom e estilo

Tom: técnico mas acessível. Fala com devs que sabem código mas querem organizar conhecimento.
NÃO: marketing genérico, buzzwords vazios, hype sem substância.
SIM: dados, outcomes concretos, analogias tech, honestidade sobre limitações.

## Formato do output

```yaml
---
id: n02_output_monetization_launch
kind: output_template
pillar: P05
domain: marketing
quality: null
tags: [monetization, marketing, launch, funnel, copy, landing-page]
---
```

## Ao finalizar

1. Salve em `N02_marketing/output/output_monetization_launch.md`
2. `git add N02_marketing/ && git commit -m "[N02] Monetization launch plan + copy"`
3. `python _tools/signal_writer.py n02 MONETIZE_CEX_COMPLETE 9.0`
