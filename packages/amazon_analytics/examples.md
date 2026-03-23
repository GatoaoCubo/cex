# Amazon Analytics Agent — Examples

## Example 1: Campaign Analysis — New Product (Month 2)

### Input

```yaml
analysis_type: campaign
campaign_data:
  acos: 38.2
  roas: 2.62
  spend: 2800.00
  sales: 7333.00
  impressions: 95000
  clicks: 1140
  orders: 48
  period_days: 30
target_margin: 42.0
operation_age_months: 2
```

### Output

```yaml
diagnosis: >
  ACOS de 38.2% esta dentro do range esperado para mes 2 (25-40%).
  MPA positivo em 3.8pp indica operacao viavel mas apertada.
  CVR de 4.21% e excelente — diferencial forte.

score: 6.5
traffic_light: yellow

metrics_summary:
  - key_metric: ACOS
    current_value: 38.2
    target_value: 21.0
    gap: 17.2
    status: yellow
  - key_metric: MPA
    current_value: 3.8
    target_value: 21.0
    gap: -17.2
    status: yellow
  - key_metric: CVR
    current_value: 4.21
    target_value: 2.0
    gap: 2.21
    status: green

recommendations:
  - "Manter campanhas — ACOS normal para maturacao. Nao pausar."
  - "Isolar keywords com ACOS > 60% e negativar (15-20 termos estimados)"
  - "Aumento de budget em 20% em keywords de CVR > 5%"

risks:
  - "MPA de 3.8% deixa operacao vulneravel a aumentos de CPC"

projected_improvement: "ACOS 28-32% no mes 3 com maturacao organica normal"

maturation_context:
  operation_age_months: 2
  expected_acos_range: "25-40%"
  comment: "Dentro do esperado. CVR excelente e diferencial forte."
```

---

## Example 2: Product Validation (PPD) — Green Signal

### Input

```yaml
analysis_type: product_validation
product_data:
  search_term: "suplemento whey protein 1kg"
  sales_30d: 480
  num_sellers: 9
  avg_price: 129.90
  num_reviews: 203
  avg_rating: 4.5
  buy_box_price: 127.50
target_margin: 35.0
```

### Output

```yaml
diagnosis: >
  Produto com forte sinal verde: 480 vendas/30d, 9 vendedores (saudavel),
  rating 4.5. Margem estimada de 35% atinge ACOS objetivo de 17.5%.

score: 8.4
traffic_light: green

ppd_scorecard:
  vendas_30d:
    value: 480
    status: green
    weight: 0.30
  num_sellers:
    value: 9
    status: green
    weight: 0.20
  avaliacoes:
    value: 203
    status: green
    weight: 0.15
  rating:
    value: 4.5
    status: green
    weight: 0.10
  preco_margem:
    value: 35.0
    status: green
    weight: 0.25

recommendations:
  - "Iniciar com 1 ASIN, testar com budget Ads de R$50/dia por 14 dias"
  - "ACOS objetivo: 17.5% | ACOS maximo: 35%"
  - "Monitorar spread Buy Box — atualmente 1.8% (saudavel)"

risks:
  - "Categoria de suplementos tende a sazonalidade em Jan-Fev"

projected_improvement: "Break-even Ads em 45 dias com operacao bem executada"
```

---

## Example 3: Listing Analysis — Critical Conversion

### Input

```yaml
analysis_type: listing
listing_data:
  sessions: 2840
  conversions: 34
  conversion_rate: 1.2
  page_views: 3100
  buy_box_percentage: 78.0
campaign_data:
  period_days: 14
```

### Output

```yaml
diagnosis: >
  CONVERSAO BAIXA — 1.2% na faixa Baixo (1-1.5%). Buy Box 78% aceitavel,
  problema nao e preco. Com 2840 sessoes/14d, volume suficiente para diagnostico.
  Root cause provavel: imagens principais fracas ou titulo mal otimizado.

score: 4.0
traffic_light: yellow

metrics_summary:
  - key_metric: Conversion Rate
    current_value: 1.2
    target_value: 2.5
    gap: -1.3
    status: red
  - key_metric: Sessions/day
    current_value: 202.9
    status: green
  - key_metric: Buy Box %
    current_value: 78.0
    target_value: 85.0
    gap: -7
    status: yellow

recommendations:
  - "PRIORITARIO: Substituir imagem principal — fotografo ou modelo 3D profissional"
  - "PRIORITARIO: Revisar titulo — incluir top 3 keywords com maior volume"
  - "Adicionar video de produto (listings com video convertem 3-5x melhor)"
  - "Revisar bullet points: primeiro bullet = beneficio principal, nao feature"
  - "Nao escalar Ads com conversao < 1.5% — dinheiro desperdicado"

risks:
  - "Escalar Ads agora com CVR 1.2% vai piorar ACOS sem aumentar vendas"
  - "Concorrentes com imagens profissionais capturam sessoes da busca"

projected_improvement: >
  Com nova imagem + titulo otimizado (7-14 dias):
  CVR esperado 2.0-2.8% em 30 dias. ~90 pedidos extras/mes sem mais Ads.
```
