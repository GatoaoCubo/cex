---
id: p03_fs_product_extraction
kind: few_shot
pillar: P03
title: Few-Shot Product Data Extraction from Marketplace Listings
task: extract_product_data
examples_count: 3
quality: 9.2
updated: "2026-04-07"
domain: "prompt engineering"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.92
tldr: "Defines few shot for few-shot product data extraction from marketplace listings, with validation gates and integration points."
---

# Few-Shot: Product Data Extraction

## Task Description
Dado o texto bruto de um anuncio de marketplace, extrair dados estruturados do produto: nome, preco, categoria e bullet points principais. O modelo deve lidar com formatacao inconsistente, abreviacoes comuns (un., pct., cx.) e precos em BRL com virgula decimal.

## Examples

### Example 1: Mercado Livre (Eletronicos)
**Input:**
```text
Kit 3 Lampada LED Bulbo 9W Bivolt E27 Branco Frio 6500K - Economia de 80% energia
Marca: GALAXY LED | Modelo: GL-9W-BF
De R$ 45,90 por R$ 29,99
Frete gratis para SP capital
1. Equivale a lampada incandescente de 60W
2. Durabilidade de 25.000 horas
3. Certificacao INMETRO
4. Base padrao E27, encaixa em qualquer lustre
```

**Output:**
```json
{
  "nome": "Kit 3 Lampada LED Bulbo 9W Bivolt E27 Branco Frio 6500K",
  "preco": 29.99,
  "moeda": "BRL",
  "preco_original": 45.90,
  "categoria": "Eletronicos > Iluminacao > Lampadas LED",
  "marca": "GALAXY LED",
  "modelo": "GL-9W-BF",
  "bullets": [
    "Equivale a lampada incandescente de 60W",
    "Durabilidade de 25.000 horas",
    "Certificacao INMETRO",
    "Base padrao E27, encaixa em qualquer lustre"
  ]
}
```

### Example 2: Shopee (Casa e Decoracao)
**Input:**
```text
Organizador de Maquiagem Acrilico Transparente 360 Graus Rotativo Grande
⭐ 4.8 (2.3mil vendidos)
R$67,50   12x R$5,63 s/ juros
Cor: Transparente | Material: Acrilico PS cristal
✅ Gira 360 graus para facil acesso
✅ 8 compartimentos + 1 bandeja removivel
✅ Dimensoes: 23x23x30cm
✅ Suporta batom, base, pinceis, paletas
Envio: 2 dias uteis (SP)
```

**Output:**
```json
{
  "nome": "Organizador de Maquiagem Acrilico Transparente 360 Graus Rotativo Grande",
  "preco": 67.50,
  "moeda": "BRL",
  "preco_original": null,
  "categoria": "Casa e Decoracao > Organizacao > Organizadores de Maquiagem",
  "marca": null,
  "modelo": null,
  "bullets": [
    "Gira 360 graus para facil acesso",
    "8 compartimentos + 1 bandeja removivel",
    "Dimensoes: 23x23x30cm",
    "Suporta batom, base, pinceis, paletas"
  ]
}
```

### Example 3: Amazon BR (Esporte e Fitness)
**Input:**
```text
Corda de Pular Profissional com Rolamento Speed Rope Crossfit WOD

FORMIGA FITNESS - Corda ajustavel ate 3m
Avaliacao: 4.6/5 (847 avaliacoes)
Preco: R$ 42,90
Material cabo: Aco revestido PVC 2,5mm
Material manopla: Aluminio anodizado

Sobre este item:
1. Rolamento de esferas duplo para giro livre sem embaracar
2. Cabo de aco com revestimento PVC — duravel e leve (apenas 180g)
3. Manoplas ergonomicas em aluminio — antiderrapante
4. Ajustavel de 1,5m a 3,0m — corte no tamanho ideal
5. Ideal para: CrossFit, Double Unders, HIIT, boxe
Inclui: 1 corda + 1 bag de transporte + manual de ajuste
```

**Output:**
```json
{
  "nome": "Corda de Pular Profissional com Rolamento Speed Rope Crossfit WOD",
  "preco": 42.90,
  "moeda": "BRL",
  "preco_original": null,
  "categoria": "Esporte e Fitness > Acessorios de Treino > Cordas de Pular",
  "marca": "FORMIGA FITNESS",
  "modelo": null,
  "bullets": [
    "Rolamento de esferas duplo para giro livre sem embaracar",
    "Cabo de aco com revestimento PVC — duravel e leve (apenas 180g)",
    "Manoplas ergonomicas em aluminio — antiderrapante",
    "Ajustavel de 1,5m a 3,0m — corte no tamanho ideal",
    "Ideal para: CrossFit, Double Unders, HIIT, boxe"
  ]
}
```

## Selection Criteria
1. **Diversity**: 3 marketplaces brasileiros distintos (Mercado Livre, Shopee, Amazon BR) com formatacoes diferentes
2. **Complexity gradient**: Example 1 tem preco promocional (de/por), Example 2 tem emojis e parcelamento, Example 3 tem especificacoes tecnicas densas
3. **Edge cases cobertos**: preco_original null quando nao ha promocao, marca null quando nao informada, bullets com caracteres especiais (✅, *, -)
4. **Research base**: 2-3 few-shot examples ideal para task adherence (+0.91), conforme arxiv 2504.02052

## Properties

| Property | Value |
|----------|-------|
| Kind | `few_shot` |
| Pillar | P03 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
