---
id: n07_crm_pipeline_evidence
kind: research
pillar: P12
title: "CRM_FULL_HARVEST — Pipeline Evidence & Batch Status"
version: 1.0.0
created: 2026-04-04
author: n07_orchestrator
quality: 9.1
density_score: 1.0
---

# CRM_FULL_HARVEST — Pipeline Evidence

## 1. Mission Status (04/Abr/2026 13:30) — ✅ COMPLETE

```
BASE FINAL: 509 contatos reais | 0 fakes
Meta:       500+ contatos ✅ ATINGIDA
```

| Wave | Batch | Status | +Novos | Fontes | Output |
|:----:|:-----:|:------:|:------:|--------|--------|
| 2 | **C** Social | ✅ DONE + MERGED | +53 | Instagram hashtags, Facebook Pages | `crm_batch_c_social.json` |
| 2 | **D** Marketplaces | ✅ DONE + MERGED | +12 | iFood, Rappi, ML, Shopee | `crm_batch_d_marketplaces.json` |
| 3 | **E** Reputação | ✅ DONE + MERGED | +15 | Econodata, CRMV-SP, Petlove | `crm_batch_e_reputation.json` |
| 1 | **A** Diretórios Pet | ✅ DONE + MERGED | +159 | Petlove, DogHero, PetAnjo, TeleListas, GuiaMais | `crm_batch_a_diretorios.json` |
| 1 | **B** Google Maps | ✅ DONE + MERGED | +59 | Serper Google Maps, 9 categorias × 7 cidades | `crm_batch_b_gmaps.json` |
| 3 | **F** CNAE Deep | ✅ DONE + MERGED | +55 | Casa dos Dados, CNPJ.biz, ReceitaWS, CNPJá | `crm_batch_f_cnae.json` |

---

## 2. Final CRM Stats

```
Total:          509
Com telefone:   133 (26%)   → meta 60% (gap: enrichment needed)
Com endereço:   284 (55%)   → meta 85% (gap: enrichment needed)
Com web/IG:     179 (35%)   → meta 65% (gap: enrichment needed)
Com CNPJ:       103 (20%)   → meta 40% (gap: enrichment needed)
Fakes:            0         → meta 0 ✅
```

### Distribuição por Cidade
| Cidade | Qtd | Meta | Status |
|--------|:---:|:----:|:------:|
| São Bernardo do Campo | 111 | — | ✅ |
| São Caetano do Sul | 97 | 60+ | ✅ |
| Santo André | 86 | — | ✅ |
| Mauá | 72 | 30+ | ✅ |
| Diadema | 69 | 40+ | ✅ |
| Ribeirão Pires | 46 | 10+ | ✅ |
| Rio Grande da Serra | 13 | 5+ | ✅ |

---

## 3. Pipeline Architecture (Lições da Retrospectiva)

### Pipeline Correta (5 fases)

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────┐     ┌────────────┐
│ FASE 1      │     │ FASE 2       │     │ FASE 3       │     │ FASE 4   │     │ FASE 5     │
│ Discovery   │────▶│ Enrichment   │────▶│ Validation   │────▶│ Storage  │────▶│ Dashboard  │
│ (N01)       │     │ (N01)        │     │ (N07/script) │     │ (JSON)   │     │ (HTML)     │
└─────────────┘     └──────────────┘     └──────────────┘     └──────────┘     └────────────┘
   Serper              Firecrawl           merge_batches.py    crm_pet_abc     gato3_crm_
   Exa                 Fetch site          dedup + recalc      .json + .csv    dashboard.html
   Firecrawl           Instagram           quality gate        
                       Google Maps         
```

### Anti-Fake Rules (enforced)
1. ❌ NUNCA dar meta numérica ao N01 → "pesquise em Rudge Ramos", não "+30 SBC"
2. ✅ Validar ANTES de commitar → merge_batches.py faz dedup automático
3. ✅ Separar discovery de integração → N01 gera batch, N07 merge
4. ✅ JSON como formato de troca → nunca markdown para dados
5. ✅ Fonte obrigatória em cada registro → campo fonte_descoberta

---

## 4. Scraping Pipeline por Batch

### Batch A — Diretórios Pet (ALTO ROI estimado: +40-80 contatos)

```
PIPELINE A:
  ┌─ Petlove Rede Credenciada ──────────────────────┐
  │  Método: FIRECRAWL saude.petlove.com.br/rede     │
  │  7 cidades × clínicas credenciadas                │
  │  ROI: ALTO — dados já validados pela Petlove     │
  └───────────────────────────────────────────────────┘
  ┌─ DogHero + PetAnjo ─────────────────────────────┐
  │  Método: SERPER site:doghero.com.br "cidade"     │
  │  Hospedagem, walker, sitter, creche               │
  │  ROI: MÉDIO — muitos informais, poucos dados     │
  └───────────────────────────────────────────────────┘
  ┌─ TeleListas / GuiaMais / Apontador / ListaMais ──┐
  │  Método: FIRECRAWL URL direta por cidade/segmento│
  │  Pet shop, vet, banho/tosa, hotel — 4 seg × 7 cid│
  │  ROI: ALTO — TeleListas tem telefone validado!   │
  └───────────────────────────────────────────────────┘

  Output: crm_batch_a_diretorios.json
  Dedup: contra 244 existentes (nome + cidade)
  Estimativa: +40-80 novos (diretórios são redundantes entre si)
```

### Batch B — Google Maps (MAIOR ROI estimado: +60-120 contatos)

```
PIPELINE B:
  ┌─ Serper Google Maps Mode ────────────────────────┐
  │  Query: "{categoria}" near "{cidade}" SP          │
  │  9 categorias × 7 cidades = 63 queries            │
  │                                                    │
  │  CATEGORIAS:                                       │
  │    pet shop | clínica veterinária | banho e tosa  │
  │    hotel pet | creche pet | adestrador            │
  │    farmácia veterinária | funerária pet           │
  │    táxi pet                                        │
  │                                                    │
  │  CIDADES (prioridade):                             │
  │    1. SCS (56→60+)                                │
  │    2. Diadema (13→40+)                            │
  │    3. Mauá (11→30+)                               │
  │    4. Rib. Pires + RGS (3→15+)                   │
  │    5. SBC + SA (focar segmentos fracos)            │
  └───────────────────────────────────────────────────┘
  ┌─ Enrichment de cada resultado ───────────────────┐
  │  Se tem website → FETCH para email/whats/IG       │
  │  Extrair: tel, rating, reviews, horário, coords  │
  └───────────────────────────────────────────────────┘

  Output: crm_batch_b_gmaps.json
  Dedup: contra 244 existentes (nome + cidade + CNPJ)
  Estimativa: +60-120 novos (Google Maps é a fonte mais completa)
```

### Batch F — CNAE Deep (MÉDIO ROI estimado: +30-50 contatos)

```
PIPELINE F:
  ┌─ Casa dos Dados ─────────────────────────────────┐
  │  Para cada CNAE × cidade:                         │
  │  8 CNAEs × 7 cidades = 56 queries                │
  │                                                    │
  │  CNAEs:                                            │
  │    4789-0/04 (pet shop)                           │
  │    7500-1/00 (veterinário)                        │
  │    9609-2/08 (banho/tosa)                         │
  │    4771-7/04 (farmácia vet)                       │
  │    0159-8/02 (criador)                            │
  │    5590-6/99 (hotel pet)                          │
  │    9609-2/99 (serviços pet)                       │
  │    4789-0/01 (ração/suprimentos)                  │
  │                                                    │
  │  Método: SERPER site:casadosdados.com.br          │
  │  + CNPJ.biz + validação ReceitaWS (3/min limit)  │
  └───────────────────────────────────────────────────┘
  ┌─ Validação CNPJ ────────────────────────────────┐
  │  publica.cnpj.ws/cnpj/{14dig}                    │
  │  SÓ situação ATIVA                               │
  │  Rate limit: 3 requests/min                       │
  └───────────────────────────────────────────────────┘

  Output: crm_batch_f_cnae.json
  Dedup: contra 244 existentes (CNPJ primário, nome secundário)
  Estimativa: +30-50 novos (muitos overlap com pet shops já encontrados)
  BÔNUS: sobe cobertura CNPJ de 22% → 35-40%
```

---

## 5. Grid Execution Plan

### Dispatch Strategy
```
WAVE FINAL (3 slots paralelos N01):
  Slot 1: BATCH_A — Diretórios Pet
  Slot 2: BATCH_B — Google Maps
  Slot 3: BATCH_F — CNAE Deep

Todos usam: N01 (Research Analyst)
Provider: gemini/2.5-pro (primary) → claude (fallback)
Cada batch é autônomo — handoff já escrito em:
  .cex/runtime/handoffs/crm_mission/batch_{a,b,f}_*.md
```

### Post-Grid (N07)
```
1. Poll signals: signal_n01_*_BATCH_{A,B,F}
2. Validate: python merge_batches.py --all --dry-run
3. Merge: python merge_batches.py --all
4. Re-export CSV
5. Update dashboard HTML
6. Commit consolidado
7. Stats vs meta 500+
```

---

## 6. Risk Assessment

| Risk | Mitigation |
|------|------------|
| N01 fabrica dados (like before) | Handoffs say "NUNCA inventar", dedup + quality gate |
| Rate limit Serper/ReceitaWS | 3 batches paralelos spread load across APIs |
| Batch B (63 queries) é grande | Priorizar cidades com gap (Diadema, Mauá, Rib.Pires) |
| Overlap entre batches | merge_batches.py faz dedup por nome+cidade+CNPJ |
| Completeness ainda baixa | Batch B (Google Maps) traz tel+rating nativo |

---

## 7. Projeção Pós-Grid

```
                  Atual    +A      +B       +F     TOTAL
Contatos:          244    +50     +80      +40      414
Com telefone:       34%    38%     48%      50%      50%
Com endereço:       56%    62%     72%      75%      72%
Com CNPJ:           22%    24%     25%      38%      32%
Meta 500+:                                         ❌ (84%)
```

Se 414 < 500: próximo passo seria Wave 4 com re-scrape por bairro
(varrer SBC por bairro: Rudge Ramos, Planalto, Centro, Assunção, etc.)

---

*Generated by N07 Orchestrator — 2026-04-04T12:50:00-03:00*
