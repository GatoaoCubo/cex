---
id: p01_kc_bling_erp_field_parametrization
type: knowledge_card
lp: P01
title: "Bling ERP: Parametrizacao de Campos para Cadastro de Produto"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: PYTHA
domain: execution
quality: null
tags: [bling, erp, produto, field-mapping, catalogo, parametrization]
tldr: "Cadastro robusto em Bling combina payload minimo valido, defaults seguros e separacao clara entre dados principais, imagens e tributacao."
when_to_use: "Mapear campos do produto Bling antes de criar payloads, conectores ou telas de cadastro"
keywords: [bling_produto, field_mapping, product_payload, tributacao, imagens]
long_tails:
  - "Quais campos do produto Bling precisam estar parametrizados no conector"
  - "Como estruturar payload minimo e campos opcionais no Bling ERP"
axioms:
  - "SEMPRE garantir payload minimo valido antes de enriquecer campos extras"
  - "NUNCA misturar imagem principal, galeria e tributacao no mesmo fallback mental"
linked_artifacts:
  primary: null
  related: [p01_kc_zero_touch_execution]
density_score: null
data_source: "https://www.bling.com.br/api-bling"
---

## Quick Reference

topic: product field mapping | scope: Bling ERP V3 | criticality: high
payload minimo: nome + tipo + situacao + formato

## Conceitos Chave

- Dados principais carregam identidade comercial e operacao basica
- Imagens podem entrar no create e tambem por upload posterior
- Tributacao exige defaults seguros e override por categoria
- Campo opcional sem fonte confiavel deve nascer vazio, nao inventado

## Comparativo

| Bloco | Funcao | Campos tipicos | Regra |
|-------|--------|----------------|-------|
| Dados principais | vender e listar | nome, codigo, preco | validar antes |
| Imagens | exposicao visual | imagemURL, imagens[] | URL publica |
| Tributacao | fiscalidade | origem, NCM, CEST | revisar por categoria |
| Extras | enrich | descricao, observacoes | usar fallback seguro |

| Campo | Obrigatorio | Default seguro | Observacao |
|-------|-------------|----------------|------------|
| `nome` | sim | nao ha | max 120 chars |
| `tipo` | sim | `P` | produto padrao |
| `situacao` | sim | `A` | ativo |
| `formato` | sim | `S` | simples |
| `unidade` | nao | `UN` | evita vazio operacional |
| `gtin` | nao | vazio | nao inferir barcode |

## Regras de Ouro

- SEMPRE subir com payload minimo antes de preencher campos long tail
- SEMPRE padronizar defaults de `tipo`, `situacao`, `formato` e `unidade`
- NUNCA preencher GTIN, NCM ou CEST sem fonte verificavel
- SEMPRE tratar imagens como URLs publicas acessiveis pelo Bling

## Code

<!-- lang: json | purpose: minimal valid product payload for Bling -->
```json
{
  "nome": "Copo Termico Inox 473ml",
  "tipo": "P",
  "situacao": "A",
  "formato": "S",
  "unidade": "UN",
  "preco": 79.9,
  "descricaoCurta": "Copo termico inox para uso diario"
}
```

<!-- lang: json | purpose: image enrichment after product creation -->
```json
{
  "imagemURL": "https://cdn.exemplo.com/produto-main.jpg",
  "imagens": [
    {"link": "https://cdn.exemplo.com/produto-1.jpg"},
    {"link": "https://cdn.exemplo.com/produto-2.jpg"}
  ]
}
```

## References

- external: https://www.bling.com.br/api-bling
- external: https://developer.bling.com.br/como-testar
- external: https://ajuda.bling.com.br/hc/pt-br/articles/360047475233-Entendendo-o-m%C3%B3dulo-de-Produtos
- deepens: p01_kc_zero_touch_execution
