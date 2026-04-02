# Mission: MONETIZE_CEX — N06 Commercial Perspective
**Nucleus**: N06 Commercial | **Model**: claude/sonnet-4 | **Priority**: HIGH
**Output**: `N06_commercial/output/output_monetization_business_plan.md`
**Signal on complete**: `python _tools/signal_writer.py n06 MONETIZE_CEX_COMPLETE 9.0`
**REGRA**: Leia TUDO abaixo. Commit e signal ANTES de qualquer pausa.

---

## CONTEXTO — Estratégia Aprovada pelo User

O CEX (Typed Knowledge System for LLM Agents) será monetizado assim:

| Decisão | Escolha |
|---------|---------|
| Modelo de acesso | Repo público (MIT no GitHub) + Curso pago |
| Formato do curso | Híbrido: vídeo curto + texto + exercícios práticos |
| Currículo | 3 tracks: Foundations (free) → Builder (R$497) → Master (R$997) |
| Plataforma | Lemon Squeezy (5% fee, license keys, internacional) |
| Modelo FT | cex-brain:14b = download exclusivo tier pago |

O user rejeitou: Open-core (precisa community), Model-as-product (commodity), SaaS (caro pro user), Dual-license (não se aplica).

## SUA MISSÃO (N06 — Commercial)

Produza um **business plan e estratégia comercial** cobrindo:

### 1. Projeção financeira (12 meses)

| Mês | Alunos Builder | Alunos Master | Receita bruta | Fee (5%) | Receita líquida |
|-----|---------------|---------------|---------------|----------|-----------------|

- Cenário conservador: 10 alunos/mês crescendo 15%
- Cenário base: 25 alunos/mês crescendo 20%
- Cenário otimista: 50 alunos/mês crescendo 25%
- Mix estimado: 70% Builder / 30% Master

### 2. Unit economics
- CAC (Customer Acquisition Cost) por canal
- LTV (Lifetime Value) — compra única vs upsell
- Payback period
- Margem por tier (receita - fee - custos variáveis)

### 3. Pricing psychology
- Por que R$497 e não R$500? (odd pricing + perceived value)
- Ancoragem: Master R$997 faz Builder R$497 parecer barato
- Decoy effect: vale criar um tier intermediário (R$697)?
- Early-bird pricing: R$297 Builder nos primeiros 30 dias?
- Lifetime deal: faz sentido vender acesso vitalício por R$997?

### 4. Revenue streams além do curso
- Consulting/setup pra empresas (R$5-15K one-time)
- White-label CEX pra agências
- cex-brain fine-tuning personalizado (treinar no corpus do cliente)
- Community premium (membership mensal?)
- Afiliados: 20-30% comissão via Lemon Squeezy

### 5. Brand positioning
- CEX no mercado: onde se posiciona? (dev tool? framework? knowledge OS?)
- Tagline candidatas (3-5 opções)
- Tone of voice pro produto público (técnico? provocador? didático?)
- Diferencial vs concorrentes free (LangChain, CrewAI, AutoGen)

### 6. Riscos comerciais
- E se OpenAI/Google lança product similar? (moat analysis)
- E se Qwen muda licença? (supply chain risk pro FT model)
- E se conversão é menor que esperado? (plano B)
- Sazonalidade: quando dev BR compra curso?

### 7. Roadmap de receita (3 fases)
- Fase 1 (mês 1-3): Launch Builder tier, early-bird
- Fase 2 (mês 4-6): Add Master tier, launch cex-brain
- Fase 3 (mês 7-12): Agency tier, consulting, afiliados

## Formato do output

```yaml
---
id: n06_output_monetization_business_plan
kind: output_template
pillar: P05
domain: commercial
quality: null
tags: [monetization, business-plan, pricing, revenue, brand, projections]
---
```

Tabelas financeiras com números reais (BRL). Cenários claros. Não otimismo cego — inclua riscos.

## Ao finalizar

1. Salve em `N06_commercial/output/output_monetization_business_plan.md`
2. `git add N06_commercial/ && git commit -m "[N06] Monetization business plan"`
3. `python _tools/signal_writer.py n06 MONETIZE_CEX_COMPLETE 9.0`
