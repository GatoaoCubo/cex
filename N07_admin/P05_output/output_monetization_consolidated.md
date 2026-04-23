---
id: n07_output_monetization_consolidated
kind: output_template
pillar: P05
title: "MONETIZE_CEX — Consolidated Report (6 Nucleus Perspectives)"
version: 1.0.0
created: 2026-04-02
author: n07_orchestrator
domain: orchestration
quality: 9.1
tags: [monetization, consolidated, grid, all-nucleus, business, course, model]
tldr: "Synthesis of 6 nucleus perspectives on CEX monetization: convergences, conflicts, unified action plan, risk matrix."
density_score: 0.95
related:
  - bld_sp_collaboration_software_project
  - n03_output_monetization_architecture
  - p12_dr_software_project
  - p12_dr_content_factory
  - p12_sc_admin_orchestrator
  - kc_intent_resolution_map
  - output_content_factory_business_model
  - bld_collaboration_supabase_data_layer
  - n06_output_monetization_business_plan
  - p03_pc_cex_universal
---

# MONETIZE_CEX — Consolidated Report

> 6 nuclei × 6 models × 1 goal = unified strategy

---

## 1. CONVERGÊNCIAS (todos concordam)

| Ponto | N01 | N02 | N03 | N04 | N05 | N06 |
|-------|:---:|:---:|:---:|:---:|:---:|:---:|
| Repo MIT público é o caminho | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| cex-brain é o killer differentiator | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| R$497 Builder está no range certo | ✓ | ✓ | — | — | — | ✓ |
| YouTube unlisted pra MVP de vídeo | — | ✓ | ✓ | — | ✓ | — |
| Lemon Squeezy > Hotmart | — | — | ✓ | — | ✓ | ✓ |
| Qwen3 Apache 2.0 = safe pra venda | — | — | ✓ | — | — | — |
| Curso baseado em outputs práticos | — | ✓ | — | ✓ | — | — |
| Early-bird é essencial pro launch | — | ✓ | — | — | — | ✓ |

**Nenhum núcleo questionou** o modelo Repo+Curso+FT. Validação forte.

---

## 2. CONFLITOS E DIVERGÊNCIAS

### 2.1 Projeções financeiras: otimismo vs realismo

| Métrica | N02 (Marketing) | N06 (Commercial) | Delta |
|---------|:---:|:---:|:---:|
| MRR Mês 1 | R$12K | R$6.5K | 2x |
| MRR Mês 6 | R$120K | R$32K | 3.7x |
| Alunos Mês 1 | 26 | 10 | 2.6x |
| Conversion rate LP | 8% | n/a | N02 otimista (industry: 2-5%) |

**Decisão N07**: Usar cenário CONSERVADOR do N06 (10 alunos/mês) como base de planning. Se superar, ótimo. Projeções do N02 são targets aspiracionais, não baselines.

### 2.2 Astro site vs GitHub private repo

| Proposta | Quem | Prós | Contras |
|----------|------|------|---------|
| Astro SSG + MDX on Vercel | N03 | Custom, gated routes, branded | Precisa construir (8h) |
| GitHub private repo | N05 | Zero build, familiar, free | UX ruim pra alunos, sem gating |

**Decisão N07**: N03 vence. Astro + MDX no Vercel é MVP correto — Markdown-native (mesma linguagem do CEX), gating via middleware, custo zero. Investir 8h que resultam em experiência profissional > gambiarras.

### 2.3 Model hosting

| Proposta | Quem | Custo | UX |
|----------|------|-------|-----|
| HuggingFace gated | N03 + N05 | Free | Manual approval |
| S3 + presigned URL | N03 | ~$5/mês | Automated |
| HF primary + S3 backup | N05 | Free+$5 | Best of both |

**Decisão N07**: HuggingFace gated como primary (free, CDN). Lemon Squeezy webhook → auto-approve no HF via API. S3 como fallback se HF tiver downtime.

### 2.4 N04 curriculum vs N02 curriculum

N04 detalhou 14 módulos com tempos e checkpoints.
N02 focou em 3 tracks com métricas de conversão.

**Decisão N07**: Merge — N04 é a estrutura pedagógica (o quê/quanto tempo), N02 é o wrapper de conversão (como vender cada track). Não conflitam, complementam.

---

## 3. INSIGHTS ÚNICOS POR NÚCLEO

### N01 (Research) — Dados de mercado
- **SOM**: 860-1.720 clientes potenciais (BR+PT devs interessados em AI agents)
- **Moat real**: CEX é "sistema", não "framework" → pricing de PKM courses (R$2.500-7.500)
- **Risk**: Conteúdo commoditiza, mas SISTEMA e MODELO são defensáveis

### N02 (Marketing) — Posicionamento killer
- **Headline**: "Organize Your AI Knowledge Like Code"
- **Analogia**: "CEX é o TypeScript para Prompt Engineering"
- **Funil calculado**: GitHub 10K/mês → Newsletter 2K → Foundation 500 → Builder 80/mês

### N03 (Engineering) — Blueprint técnico completo
- **Esforço MVP**: 96.5 horas (~5 semanas a 4h/dia)
- **Repo clean**: Já está 90% pronto (sem secrets vazados, .gitignore sólido)
- **License verification**: FastAPI + S3 presigned URLs (Option A)
- **Qwen3 Apache 2.0**: Confirmed safe para venda de derivativo

### N04 (Knowledge) — Design instrucional
- **Persona primária**: Dev Jr/Pl que quer estruturar LLM workflows
- **Checkpoint pedagógico**: Cada módulo termina com artefato verificável
- **Badges**: "The Initer", "Grid Master", "Flywheel Pilot"
- **Gap**: Faltam scripts de conversão de dataset e guia de troubleshooting

### N05 (Operations) — Infra automation
- **Breakeven**: 4 Builder students/ano (trivial)
- **Custo fixo mensal**: ~$33 (domínio + HF Pro + GitHub Pro + email + monitoring)
- **Scripts P0**: cex_license.py, cex_setup.py, webhook handler, GitHub Actions CI
- **LGPD**: Dados mínimos (email + key + tier), retention 2 anos

### N06 (Commercial) — Business plan
- **Ano 1 conservador**: R$176K líquido
- **Ano 1 base**: R$441K líquido
- **CAC médio**: R$89, LTV Builder: R$572, payback imediato
- **Tagline winner**: "Knowledge that builds itself"
- **NÃO fazer**: Lifetime deal (mata receita recorrente)
- **SIM fazer**: Early-bird R$297 (30 dias), afiliados 25%

---

## 4. PLANO UNIFICADO — 12 SEMANAS

### Semana 1-2: REPO PREP (N03 + N05)
- [ ] .gitignore additions (0.5h)
- [ ] git filter-repo audit (1h)
- [ ] README.md público (3h)
- [ ] cex_setup.py installer (2h)
- [ ] CONTRIBUTING.md (1h)
- [ ] GitHub Actions CI: lint + doctor + test (2h)

### Semana 3-4: PLATAFORMA (N05 + N03)
- [ ] Lemon Squeezy account + products (Builder R$297 EB, Master R$697 EB) (4h)
- [ ] Webhook handler FastAPI (6h)
- [ ] cex_license.py (8h)
- [ ] Astro course site scaffold + license middleware (11h)
- [ ] Privacy Policy + ToS (2h)

### Semana 5-6: CONTEÚDO TRACK 1 — FREE (N04 + N02)
- [ ] M01 texto + vídeo: O que é CEX (3h)
- [ ] M02 texto + vídeo: Instalação + /init (3h)
- [ ] M03 texto + vídeo: Primeiro /build (3h)
- [ ] Landing page copy (N02 output já tem) (4h)
- [ ] YouTube channel setup + upload (2h)

### Semana 7-9: CONTEÚDO TRACK 2 — BUILDER R$297 EB (N04)
- [ ] M04-M10 texto detalhado (20h)
- [ ] M04-M10 vídeos (10-15min cada) (21h)
- [ ] cex_checkpoint.py exercise verification (3h)
- [ ] Beta test com 5-10 early adopters (1 semana)

### Semana 10: LAUNCH (N02 + N06)
- [ ] Hacker News post
- [ ] Twitter/X thread
- [ ] Dev.to article "Why I Built CEX"
- [ ] Newsletter blast
- [ ] YouTube announcement
- [ ] Afiliados outreach

### Semana 11-12: POST-LAUNCH + MASTER PREP
- [ ] Collect feedback, fix issues
- [ ] Start Track 3 content (M11-M14)
- [ ] cex_finetune_export.py + train cex-brain (12h)
- [ ] HuggingFace gated model upload
- [ ] Master tier launch (R$697 early-bird → R$997 after 30d)

---

## 5. RISK MATRIX

| Risk | Probability | Impact | Mitigation | Owner |
|------|:-----------:|:------:|------------|:-----:|
| Codex/o3 not available on ChatGPT sub | **HAPPENED** | LOW | claude/sonnet fallback | N07 |
| Gemini CLI Node.js crash | MEDIUM | LOW | claude fallback boot scripts | N07 |
| <5 alunos/mês | MEDIUM | HIGH | Double YouTube + afiliados | N02 |
| Qwen license change | LOW | MEDIUM | Retrain on Llama 3.3 (2-4 weeks) | N03 |
| OpenAI/Google launches similar | MEDIUM | MEDIUM | Community moat + speed | ALL |
| Piracy of cex-brain GGUF | MEDIUM | LOW | Model is commodity, course is value | N06 |
| Content outdates fast | HIGH | MEDIUM | Text > video (easy update), modular | N04 |

---

## 6. MÉTRICAS DE SUCESSO

| KPI | Mês 1 | Mês 3 | Mês 6 | Mês 12 |
|-----|:-----:|:-----:|:-----:|:------:|
| GitHub Stars | 500 | 1.5K | 3K | 5K |
| Newsletter subs | 200 | 1K | 2.5K | 5K |
| Foundation completions | 50 | 250 | 500 | 1K |
| Builder sales (cumulative) | 10 | 40 | 100 | 250 |
| Master sales (cumulative) | 2 | 12 | 35 | 80 |
| MRR | R$6K | R$12K | R$32K | R$65K |
| Community members | 30 | 100 | 300 | 600 |

---

## 7. DECISÕES LOCKED

| # | Decision | Value | Source |
|---|----------|-------|--------|
| D01 | Modelo de acesso | Repo MIT público + curso pago | /guide |
| D02 | Formato do curso | Híbrido (vídeo + texto + exercícios) | /guide |
| D03 | Currículo | 3 tracks, 14 módulos (N04 design) | N04 |
| D04 | Pricing | EB: R$297/R$697 → Full: R$497/R$997 | N06 |
| D05 | Plataforma | Lemon Squeezy | /guide + N03 + N05 |
| D06 | Model hosting | HuggingFace gated (primary) + S3 (backup) | N03 + N05 |
| D07 | Video | YouTube unlisted (MVP) → Vimeo (V2) | N03 + N05 |
| D08 | Course site | Astro + MDX on Vercel | N03 |
| D09 | License verification | FastAPI + presigned URLs | N03 |
| D10 | Headline | "Knowledge that builds itself" / "Organize Your AI Knowledge Like Code" | N06 / N02 |
| D11 | Early-bird | R$297 Builder / R$697 Master (30 dias) | N06 |
| D12 | Lifetime deal | NÃO | N06 |
| D13 | Afiliados | 25% comissão via Lemon Squeezy | N06 |
| D14 | FT model | cex-brain:14b Qwen3 QLoRA → GGUF Q5_K_M | N03 + /guide |
| D15 | Ollama fallback | qwen3:32b (heavy) / qwen3:14b (light) | /guide |

---

*Consolidation by N07 Orchestrator — 6/6 nuclei complete, 0 conflicts unresolved.*

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_sp_collaboration_software_project]] | downstream | 0.32 |
| [[n03_output_monetization_architecture]] | related | 0.30 |
| [[p12_dr_software_project]] | downstream | 0.27 |
| [[p12_dr_content_factory]] | downstream | 0.27 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.26 |
| [[kc_intent_resolution_map]] | upstream | 0.25 |
| [[output_content_factory_business_model]] | upstream | 0.24 |
| [[bld_collaboration_supabase_data_layer]] | downstream | 0.23 |
| [[n06_output_monetization_business_plan]] | sibling | 0.23 |
| [[p03_pc_cex_universal]] | upstream | 0.22 |
