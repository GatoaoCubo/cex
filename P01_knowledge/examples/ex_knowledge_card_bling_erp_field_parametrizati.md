---
id: p01_kc_bling_erp_field_parametrization
kind: knowledge_card
pillar: P01
title: "Bling ERP: Mapa de Campos do Produto V3"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: execution
quality: 9.1
tags: [bling, erp, field-mapping, product, parametrization]
tldr: "44 campos Bling V3 em 4 blocos — payload minimo de 4 campos obrigatorios, imagens via URL publica e tributacao com defaults seguros."
when_to_use: "Mapear campos antes de criar payloads, conectores ou telas de cadastro Bling"
keywords: [bling_produto, field_mapping, payload, tributacao, imagens]
long_tails:
  - "Quais campos do produto Bling sao obrigatorios no V3"
  - "Como montar payload minimo valido para criar produto no Bling"
axioms:
  - "SEMPRE garantir payload minimo antes de enriquecer extras"
  - "NUNCA inferir GTIN, NCM ou CEST sem fonte verificavel"
linked_artifacts:
  primary: p01_kc_bling_erp_automation_boundary
  related: [p01_kc_zero_touch_execution]
density_score: null
data_source: "https://developer.bling.com.br/referencia"
---

## Quick Reference

topic: product field mapping | scope: Bling V3 | fields: 44
payload minimo: nome + tipo + situacao + formato

## Spec

| Bloco | Campos | Funcao | Regra central |
|-------|--------|--------|---------------|
| Dados principais | 14 | identidade comercial | 4 obrigatorios |
| Imagens | 2 | exposicao visual | URL publica |
| Tributacao | 5 | fiscalidade | default seguro |
| Extras API | 6 | enriquecimento | fallback vazio |

| Campo | API key | Tipo | Obrigatorio | Default |
|-------|---------|------|-------------|---------|
| `nome` | nome | text | sim | — |
| `tipo` | tipo | SELECT | sim | P |
| `situacao` | situacao | TOGGLE | sim | A |
| `formato` | formato | SELECT | sim | S |
| `codigo` | codigo | text | nao | auto |
| `preco` | preco | float | nao | 0.0 |
| `unidade` | unidade | text | nao | UN |
| `condicao` | condicao | SELECT | nao | 1 |

## Patterns

| Trigger | Action |
|---------|--------|
| Criar produto novo | Enviar payload minimo primeiro |
| Adicionar imagens | POST /produtos/{id}/imagens |
| Imagem principal | PUT com campo imagemURL |
| Tributacao | Usar defaults, override por NCM |
| Campo sem fonte | Deixar vazio, nunca inventar |

## Anti-Patterns

- Inferir GTIN/barcode sem produto fisico em maos
- Preencher NCM/CEST por chute (risco fiscal)
- Enviar imagem como base64 (Bling exige URL)
- Misturar imagem principal e galeria no mesmo call
- Ignorar payload minimo e enviar so campos opcionais

## Code

<!-- lang: json | purpose: minimal valid product payload -->
```json
{
  "nome": "Copo Termico Inox 473ml",
  "tipo": "P",
  "situacao": "A",
  "formato": "S"
}
```

<!-- lang: json | purpose: image enrichment after creation -->
```json
{
  "imagemURL": "https://cdn.exemplo.com/main.jpg",
  "imagens": [
    {"link": "https://cdn.exemplo.com/g1.jpg"},
    {"link": "https://cdn.exemplo.com/g2.jpg"}
  ]
}
```

<!-- lang: json | purpose: tax defaults -->
```json
{
  "tributacao": {
    "origem": 0,
    "tipoItem": "00",
    "percentualTributos": 0
  }
}
```

## References

- external: https://developer.bling.com.br/referencia
- external: https://www.bling.com.br/api-bling
- external: https://ajuda.bling.com.br/hc/pt-br/articles/360047475233
- deepens: p01_kc_bling_erp_automation_boundary
- deepens: p01_kc_zero_touch_execution
