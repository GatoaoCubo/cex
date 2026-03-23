# PESQUISA Agent - Examples

**Version**: 1.0.0 | **Quality**: >= 8.0

---

## Example 1: Complete Product Research (Deep)

### Input (via Task tool)
```python
Task(
    subagent_type="pesquisa-agent",
    prompt="""
    product_query: "whey protein isolado 1kg chocolate"
    target_marketplaces: ["mercado_livre", "shopee", "amazon_br"]
    research_depth: "deep"
    competitor_count: 7
    price_range: {"min": 100, "max": 250, "currency": "BRL"}
    category_filter: "Suplementos > Proteinas > Whey Protein"
    analysis_focus: ["pricing_strategy", "title_patterns", "review_sentiment"]
    """,
    description="Deep whey protein market research"
)
```

### Output (Abbreviated)
```json
{
  "productName": "Whey Protein Isolado 1kg Chocolate",
  "report": "## Resumo Executivo\n\nMercado brasileiro de whey protein isolado altamente competitivo com 50+ marcas ativas. Ticket medio R$ 175 (faixa R$ 100-250). Categoria dominada por Growth Supplements (22% share), Integralmedica (18%), Max Titanium (15%).\n\n## Brief Validado\n\n- **Categoria**: Suplementos > Proteinas > Whey Protein Isolado\n- **Publico**: Praticantes musculacao 18-45 anos, classe B/C\n- **Preco**: R$ 150-180 (mid-range competitivo)\n\n## Head Terms (15)\n\n1. whey protein isolado\n2. whey isolado 1kg\n3. proteina isolada\n4. whey protein chocolate\n5. suplemento proteico\n[...10 more]\n\n## Top 5 Concorrentes\n\n### 1. Growth Supplements - Iso Whey 1kg Chocolate\n- **Preco**: R$ 169,90\n- **Rating**: 4.7/5.0 (8.234 reviews)\n- **Forca**: Marca consolidada, melhor custo-beneficio\n- **Fraqueza**: Sabor menos premium, embalagem simples\n\n## Gaps & Oportunidades\n\n### Gaps Identificados\n- **Gap 1**: Sabor chocolate premium ausente no mid-range\n- **Gap 2**: Embalagens sustentaveis - nenhum concorrente\n\n### Acoes Recomendadas\n1. Posicionar como \"Chocolate Premium\"\n2. Oferecer refil eco\n3. Bundle inicial com creatina\n\n---\n\n**CONFIDENCE**: 0.87/1.00\n- Fontes: 15 URLs\n- Queries: 47 executadas\n- Concorrentes: 7 analisados"
}
```

### Quality Score: 8.8/10
- All 16 sections present
- 7 competitors analyzed (exceeds minimum 3)
- 47 queries logged (exceeds minimum 15)
- Compliance checks completed
- Actionable recommendations clear

---

## Example 2: Quick Marketplace Scan (Standard)

### Input
```python
Task(
    subagent_type="pesquisa-agent",
    prompt="""
    product_query: "fone bluetooth esportivo"
    target_marketplaces: ["mercado_livre", "shopee"]
    research_depth: "quick"
    competitor_count: 5
    """,
    description="Quick bluetooth headphones scan"
)
```

### Output (Abbreviated)
```json
{
  "productName": "Fone Bluetooth Esportivo",
  "report": "## Resumo Executivo\n\nMercado saturado com 200+ modelos ativos em ML e Shopee. Ticket medio R$ 85 (faixa R$ 30-300). Categoria dominada por marcas chinesas (Xiaomi, QCY, Haylou) com 60% share.\n\n## Brief Validado\n\n- **Categoria**: Eletronicos > Audio > Fones Bluetooth\n- **Publico**: Praticantes corrida/academia 18-40 anos\n- **Preco**: R$ 70-120 (sweet spot competitivo)\n\n## Head Terms (15)\n\n1. fone bluetooth esportivo\n2. fone sem fio corrida\n3. fone bluetooth prova dagua\n4. fone de ouvido academia\n5. fone bluetooth xiaomi\n[...10 more]\n\n## Top 5 Concorrentes\n\n### 1. Xiaomi Redmi Buds 4 Active\n- **Preco**: R$ 89,90\n- **Rating**: 4.6/5.0\n- **Forca**: Marca forte, autonomia 12h, IPX4\n- **Fraqueza**: Nao tem cancelamento ruido ativo\n\n---\n\n**CONFIDENCE**: 0.72/1.00\n- Fontes: 8 URLs\n- Queries: 18 executadas\n- Concorrentes: 5 analisados"
}
```

### Quality Score: 7.5/10
- All sections present
- 5 competitors (meets minimum)
- 18 queries (above minimum 10, but below recommended 30+)
- Quick research mode appropriate

---

## Example 3: Competitor URL Analysis (Deep)

### Input
```python
Task(
    subagent_type="pesquisa-agent",
    prompt="""
    source_type: "competitor_url"
    product_query: "https://www.mercadolivre.com.br/garrafa-termica-gato-500ml-MLB2934567890"
    target_marketplaces: ["mercado_livre", "shopee", "amazon_br"]
    research_depth: "deep"
    competitor_count: 10
    analysis_focus: ["pricing_strategy", "title_patterns", "image_quality", "review_sentiment"]
    """,
    description="Reverse-engineer competitor product"
)
```

### Output (Abbreviated)
```json
{
  "productName": "Garrafa Termica Inox Gato 500ml",
  "report": "## Resumo Executivo\n\nProduto URL-alvo: Garrafa Termica com Design de Gato (orelhas 3D na tampa). Nicho: garrafas termicas personalizadas para publico feminino jovem. Preco R$ 79,90 (premium vs genericas R$ 45). Rating 4.8/5.0 (2.345 reviews).\n\n## Top 10 Concorrentes\n\n### 1. Garrafa Termica Gato 500ml (URL-alvo)\n- **Preco**: R$ 79,90\n- **Rating**: 4.8/5.0 (2.345 reviews)\n- **Forca**: Design unico (orelhas 3D), fotos lifestyle alta qualidade\n- **Fraqueza**: Apenas 1 cor (rosa)\n\n## Gaps & Oportunidades\n\n- **Gap 1**: Apenas 1 cor disponivel - audiencia masculina ignorada\n- **Gap 2**: Sem variante 750ml\n\n### Acoes Recomendadas\n1. Lancar 3 cores: rosa, cinza, azul\n2. Oferecer versao 750ml\n3. Bundle garrafa + caneca matching\n\n---\n\n**CONFIDENCE**: 0.91/1.00\n- Fontes: 23 URLs\n- Queries: 52 executadas\n- Concorrentes: 10 analisados"
}
```

### Quality Score: 9.2/10
- Deep competitor reverse-engineering
- 10 competitors analyzed
- Visual analysis (image quality focus)
- Sentiment analysis from reviews
- Highly actionable recommendations

---

## Integration Examples

### Example 4: Chain to ANUNCIO Agent

```python
# Step 1: PESQUISA research
pesquisa_result = Task(
    subagent_type="pesquisa-agent",
    prompt="product_query: garrafa termica gato 500ml",
    description="Market research for cat-themed water bottle"
)

# Step 2: Extract handoff data from research_notes.md (Block 22)
handoff_data = {
    "product_name": "Garrafa Termica Inox Gato 500ml",
    "head_terms": ["garrafa termica gato", "squeeze termico"],
    "longtails": ["garrafa termica 500ml parede dupla"],
    "pain_points": ["bebida esfria rapido", "vazamentos"],
    "competitor_avg_rating": "4.6/5.0",
    "unique_selling_points": ["Tampa com orelhas de gato 3D"]
}

# Step 3: ANUNCIO uses research to generate listings
anuncio_result = Task(
    subagent_type="anuncio-agent",
    prompt=f"Using research data: {handoff_data}\nGenerate 5 marketplace listings",
    description="Generate listings from research"
)
```

---

## Quality Validation Examples

### Example 5: Failed Quality Gate (< 7.0)

**Input**: "pesquise chocolate"
**Issue**: Too vague - no category, no target audience
**Confidence**: 0.35 (below 0.60 threshold)
**Action**: Request clarification

```
AGENT RESPONSE:
"Sua pesquisa e muito ampla. Para gerar um relatorio util, preciso de:
- Tipo especifico: chocolate em barra? bombom? achocolatado?
- Publico: consumidor final? revenda? presente?
- Faixa de preco estimada?"
```

### Example 6: Passed Quality Gate (>= 8.0)

**Input**: Complete deep research with all filters
**Sections**: All 16 present
**Competitors**: 7 analyzed
**Queries**: 47 logged
**Confidence**: 0.87
**Result**: Pool-ready, exported to research_notes.md

---

**Version**: 1.0.0 | **Created**: 2026-02-06 | **Quality**: 8.5/10
