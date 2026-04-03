---
id: p12_wf_crm_research_pipeline
kind: workflow
pillar: P12
version: "2.0.0"
created: "2026-04-03"
updated: "2026-04-03"
author: "n07_orchestrator"
title: "CRM Research Pipeline — Quality-First"
steps_count: 6
execution: sequential
agent_nodes: [n01, n07]
timeout: 7200
retry_policy: per_step
signals: [research_batch_complete, enrichment_complete, validation_complete, pipeline_complete]
domain: "crm-research"
quality: null
tags: [workflow, crm, research, pipeline, quality-first, anti-fake]
tldr: "Pipeline de pesquisa CRM quality-first: buscar por bairro → enriquecer → validar → exportar JSON. Anti-fabricação em cada step."
---

# CRM Research Pipeline v2 — Quality-First

## Princípio

**10 contatos completos > 100 contatos vazios.**

Pipeline anterior (v1) priorizava quantidade e gerou 336 contatos fabricados.
Esta versão prioriza dados acionáveis: nome + endereço + pelo menos 1 canal de contato.

---

## Regras Anti-Fabricação (APLICAM A TODOS OS STEPS)

```
1. NUNCA inventar dados. Campo não encontrado = campo vazio.
2. NUNCA gerar nomes numerados ("Pet Shop 1", "Clínica 2").
3. NUNCA gerar CNPJs sequenciais (N+1 do anterior).
4. NUNCA usar endereços genéricos ("Avenida Pet Shop, 200").
5. CADA contato DEVE ter fonte_descoberta (URL ou query que originou).
6. NUNCA dar meta numérica ao pesquisador. Meta = cobertura de bairros.
7. Completeness mínimo para entrar no CRM: nome + cidade + 1 contato.
```

---

## Steps

### Step 1: Pesquisa por Bairro [N01] — Descoberta

**Input**: Cidade + lista de bairros + segmentos
**Método**: 1 query Serper por bairro×segmento. Máx 5-10 resultados por query.
**Output**: JSON parcial em `N01_research/output/data/crm_batch_{cidade}_{date}.json`

**Queries modelo**:
```
"pet shop" "{bairro}" "{cidade}"
"veterinário" "{bairro}" "{cidade}"
"banho e tosa" "{bairro}" "{cidade}"
"hotel pet" "{cidade}"
```

**Para cada resultado**:
```json
{
  "nome_fantasia": "Nome do Google/Serper",
  "segmento": "pet_shop|clinica_vet|banho_tosa|hotel_pet|creche_pet",
  "endereco": "Endereço do Google",
  "bairro": "Bairro",
  "cidade": "Cidade",
  "fonte_descoberta": "serper:query='pet shop rudge ramos são bernardo'",
  "url_fonte": "https://google.com/...",
  "completeness_score": 1
}
```

**Gate**: Só avança se tem pelo menos nome + cidade + endereço OU telefone.
**Signal**: `research_batch_complete`

---

### Step 2: Enriquecimento [N01] — Buscar contatos

**Input**: JSON do Step 1
**Método**: Para CADA contato, buscar dados adicionais:

1. Se tem website → `fetch(website)` → extrair telefone/email do rodapé
2. Se não tem telefone → Serper: `"{nome}" "{cidade}" telefone OR whatsapp`
3. Se tem Google Maps URL → extrair rating e reviews
4. Se tem Instagram → anotar handle

**Atualizar campos**:
```json
{
  "telefone": "(11) XXXX-XXXX",
  "whatsapp": "(11) 9XXXX-XXXX",
  "email": "contato@empresa.com.br",
  "website": "https://...",
  "instagram": "@handle",
  "google_rating": "4.6",
  "google_reviews": "130",
  "fonte_enriquecimento": "fetch:website+serper:telefone",
  "completeness_score": 4
}
```

**Gate**: Recalcular completeness_score (0-5):
- +1 nome_fantasia
- +1 endereço
- +1 telefone OU whatsapp
- +1 email OU website
- +1 instagram OU google_maps_url

**Signal**: `enrichment_complete`

---

### Step 3: Validação [N07] — Quality Gate

**Input**: JSON enriquecido
**Método**: Script Python automatizado:

```python
# Validações automáticas:
1. Nome não termina em número sequencial → REJECT
2. CNPJ não é sequencial do anterior → REJECT
3. Endereço não começa com nome de segmento → REJECT
4. Telefone tem 10-11 dígitos (se preenchido) → WARN
5. completeness_score >= 2 → PASS, < 2 → QUARANTINE
6. Deduplicação por nome_fantasia (case insensitive)
```

**Output**: 
- `crm_pet_abc.json` — contatos validados (score >= 2)
- `crm_quarantine.json` — contatos incompletos (score < 2, para enriquecer depois)

**Signal**: `validation_complete`

---

### Step 4: Geocoding [N07] — Coordenadas

**Input**: JSON validado
**Método**: Para cada contato, atribuir lat/lng baseado em:
1. Endereço específico → Nominatim API (grátis) ou coords do bairro
2. Bairro conhecido → coords do centroide do bairro
3. Só cidade → coords do centro da cidade + offset aleatório

**Output**: JSON atualizado com lat/lng

---

### Step 5: Export [N07] — Formatos finais

**Input**: JSON com coords
**Output**:
- `crm_pet_abc.json` — fonte de verdade (dashboards consomem)
- `crm_pet_abc.csv` — UTF-8 BOM pra Excel/Google Sheets
- `crm_dashboard.html` — atualizar HTML com novo JSON inline

---

### Step 6: Commit + Report [N07]

**Commit**: Todos os arquivos de data + artefatos
**Report**: Atualizar `output_crm_pet_abc.md` com resumo executivo atualizado
**Signal**: `pipeline_complete`

---

## Wave Plan

| Wave | Step | Quem | Gate |
|------|------|------|------|
| 0 | Pesquisa por bairro | N01 | research_batch_complete |
| 1 | Enriquecimento | N01 | enrichment_complete |
| 2 | Validação + Geocoding + Export | N07 | validation_complete |
| 3 | Commit + Report | N07 | pipeline_complete |

**N01 faz pesquisa + enriquecimento. N07 faz validação + export.**
Isso garante que os dados passam por quality gate externo antes de entrar no CRM.

---

## Métricas de Sucesso

| Métrica | Threshold | v1 (real) | Meta v2 |
|---------|-----------|-----------|---------|
| Contatos com telefone | > 50% | 17% | > 60% |
| Contatos com endereço | > 70% | 40% | > 80% |
| Contatos com email | > 20% | 2% | > 25% |
| Completeness médio | > 3.0 | 1.7 | > 3.5 |
| Taxa de fakes | 0% | 62% | 0% |
| Contatos acionáveis | > 70% | 19% | > 70% |
