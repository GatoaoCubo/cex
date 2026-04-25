---
id: p01_kc_bling_erp_field_parametrization
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Bling ERP: Product Field Map V3"
version: 2.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: execution
quality: 9.1
tags: [bling, erp, field-mapping, product, parametrization]
tldr: "44 Bling V3 fields in 4 blocks — minimum payload of 4 mandatory fields, images via public URL, and taxation with safe defaults."
when_to_use: "Map fields before creating payloads, connectors, or Bling registration screens"
keywords: [bling_produto, field_mapping, payload, tributacao, imagens]
long_tails:
  - "Which Bling product fields are mandatory in V3"
  - "How to build the minimum valid payload to create a product in Bling"
axioms:
  - "ALWAYS ensure minimum payload before enriching with extras"
  - "NEVER infer GTIN, NCM, or CEST without a verifiable source"
linked_artifacts:
  primary: p01_kc_bling_erp_automation_boundary
  related: [p01_kc_zero_touch_execution]
density_score: null
data_source: "https://developer.bling.com.br/referencia"
related:
  - p01_kc_bling_erp_automation_boundary
  - output_content_factory_landscape
  - p01_kc_skill_format_universal
  - p01_kc_tag_grading_structured_data
---

## Quick Reference

topic: product field mapping | scope: Bling V3 | fields: 44
minimum payload: nome + tipo + situacao + formato

## Spec

| Block | Fields | Function | Central Rule |
|-------|--------|----------|--------------|
| Main data | 14 | commercial identity | 4 mandatory |
| Images | 2 | visual display | public URL |
| Taxation | 5 | fiscal compliance | safe default |
| API Extras | 6 | enrichment | empty fallback |

| Field | API key | Type | Mandatory | Default |
|-------|---------|------|-----------|---------|
| `nome` | nome | text | yes | — |
| `tipo` | tipo | SELECT | yes | P |
| `situacao` | situacao | TOGGLE | yes | A |
| `formato` | formato | SELECT | yes | S |
| `codigo` | codigo | text | no | auto |
| `preco` | preco | float | no | 0.0 |
| `unidade` | unidade | text | no | UN |
| `condicao` | condicao | SELECT | no | 1 |

## Patterns

| Trigger | Action |
|---------|--------|
| Create new product | Send minimum payload first |
| Add images | POST /produtos/{id}/imagens |
| Main image | PUT with imagemURL field |
| Taxation | Use defaults, override by NCM |
| Field without source | Leave empty, never fabricate |

## Anti-Patterns

- Inferring GTIN/barcode without physical product in hand
- Filling NCM/CEST by guesswork (fiscal risk)
- Sending image as base64 (Bling requires URL)
- Mixing main image and gallery in the same call
- Ignoring minimum payload and sending only optional fields

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_bling_erp_automation_boundary]] | sibling | 0.37 |
| [[output_content_factory_landscape]] | related | 0.20 |
| [[p01_kc_skill_format_universal]] | sibling | 0.15 |
| [[p01_kc_tag_grading_structured_data]] | sibling | 0.15 |
