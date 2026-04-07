---
id: p05_rf_crm_output_standard
kind: response_format
pillar: P05
title: "CRM Output Standard v2 — JSON-First"
version: 2.0.0
created: 2026-04-03
updated: 2026-04-03
author: n07_orchestrator
domain: crm-research
format_type: json
quality: 9.1
tags: [response_format, crm, output, json, quality-first]
tldr: "Formato padrão de output CRM: JSON (não markdown), fonte obrigatória, completeness calculado, anti-fake."
density_score: 1.0
---

# CRM Output Standard v2 — JSON-First

## Regra Principal

**Output é JSON. Não markdown. Não YAML. Não tabela.**

O pesquisador (N01) grava direto em `N01_research/output/data/crm_batch_{scope}.json`.

---

## Schema por Registro

```json
{
  "nome_fantasia": "string — OBRIGATÓRIO",
  "razao_social": "string — opcional",
  "cnpj": "string — XX.XXX.XXX/XXXX-XX ou vazio",
  "segmento": "enum — OBRIGATÓRIO",
  "sub_segmento": "string — opcional",
  "endereco": "string — com número se possível",
  "bairro": "string — extraído do endereço",
  "cidade": "string — OBRIGATÓRIO",
  "ring": "string — 1_abc | 2_grande_sp | 3_sp | 4_brasil",
  "telefone": "string — (XX) XXXX-XXXX ou (XX) XXXXX-XXXX",
  "whatsapp": "string — mesmo formato",
  "email": "string — email comercial",
  "instagram": "string — @handle",
  "website": "string — URL com protocolo",
  "google_maps_url": "string — URL Google Maps",
  "google_rating": "string — 1.0 a 5.0",
  "google_reviews": "string — número",
  "porte": "string — mei | me | epp | medio | grande",
  "foco_felino": "string — true | false",
  "potencial_b2b": "string — alto | medio | baixo",
  "notas": "string — observações do pesquisador",
  "fonte_descoberta": "string — OBRIGATÓRIO — query ou URL de origem",
  "fonte_enriquecimento": "string — como os dados extras foram obtidos",
  "completeness_score": "int — 0-5, calculado automaticamente",
  "data_discovery": "string — YYYY-MM-DD",
  "lat": "float — latitude",
  "lng": "float — longitude"
}
```

## Segmentos Válidos

```
pet_shop | clinica_vet | banho_tosa | hospital_24h | hotel_pet | creche_pet | 
distribuidor | agropecuaria | ong | cat_cafe | arquiteto_pet | adestramento
```

## Campos Obrigatórios (gate mínimo)

| Campo | Obrigatório | Motivo |
|-------|:-----------:|--------|
| nome_fantasia | ✅ | Sem nome = sem contato |
| cidade | ✅ | Sem cidade = sem localização |
| segmento | ✅ | Sem segmento = sem classificação |
| fonte_descoberta | ✅ | Sem fonte = possivelmente fabricado |
| pelo menos 1 de: telefone, whatsapp, email, website | ✅ | Sem canal = não acionável |

**Registro sem os 5 campos = REJEITADO antes de entrar no CRM.**

---

## Exemplo Completo

```json
{
  "nome_fantasia": "Pets House",
  "razao_social": "Pets House Centro Veterinário e Pet Shop Ltda.",
  "cnpj": "48.807.594/0001-73",
  "segmento": "clinica_vet",
  "sub_segmento": "24h",
  "endereco": "Av. Goiás, 269 - Santo Antônio",
  "bairro": "Santo Antônio",
  "cidade": "São Caetano do Sul",
  "ring": "1_abc",
  "telefone": "(11) 4234-2384",
  "whatsapp": "(11) 97727-0001",
  "email": "",
  "instagram": "@_petshouse",
  "website": "",
  "google_maps_url": "https://www.google.com/maps/search/?api=1&query=Pets+House+São+Caetano",
  "google_rating": "4.9",
  "google_reviews": "130",
  "porte": "epp",
  "foco_felino": "true",
  "potencial_b2b": "alto",
  "notas": "Clínica 24h com bom foco em gatos, Dra. Larissa é especialista.",
  "fonte_descoberta": "serper:query='clinica veterinaria santo antonio são caetano'",
  "fonte_enriquecimento": "fetch:google_maps+serper:telefone",
  "completeness_score": 4,
  "data_discovery": "2026-04-03",
  "lat": -23.627,
  "lng": -46.567
}
```

## Exemplo Mínimo Aceitável (score 2)

```json
{
  "nome_fantasia": "Dog's Day",
  "segmento": "pet_shop",
  "cidade": "São Caetano do Sul",
  "endereco": "R. Visc. de Inhaúma, 65 - Oswaldo Cruz",
  "fonte_descoberta": "serper:query='pet shop oswaldo cruz são caetano'",
  "completeness_score": 2
}
```
