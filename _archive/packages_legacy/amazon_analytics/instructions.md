# Amazon Analytics Agent — Instructions

## Phase 0: Input Validation

1. Confirm `analysis_type` is one of: `campaign`, `product_validation`, `listing`, `business`
2. Confirm `target_margin` is provided (required for campaign and product_validation)
3. Confirm data period >= 7 days (for campaign/listing) — flag if shorter
4. If any required field is missing, return error with field name and example value

---

## Workflow 1: Campaign Analysis

**Step 1 — Collect Metrics**
Required: spend, sales, impressions, clicks, orders, period_days
Minimum period: 7 days (refuse if < 7 days)

**Step 2 — Calculate Core Metrics**
```
ACOS  = (spend / sales) * 100
ROAS  = sales / spend
CTR   = (clicks / impressions) * 100
CPC   = spend / clicks
CVR   = (orders / clicks) * 100
MPA   = target_margin - ACOS
TACOS = (spend / total_revenue_including_organic) * 100
```

**Step 3 — Diagnose ACOS Tier**

| ACOS | Diagnostico | Acao Recomendada |
|------|-------------|------------------|
| <10% | Excelente | Escalar orcamento, manter targeting, buscar novas keywords |
| 10-15% | Bom | Manter estrutura, otimizar keywords marginais |
| 15-20% | Aceitavel | Negativar keywords ruins, ajustar lances por horario/dia |
| 20-30% | Atencao | Reestruturar campanhas, revisar targeting |
| 30-46% | Critico | Pausar campanhas fracas, revalidar produto |
| >46% | Inviavel | Pausar imediatamente, reavaliar produto e margem |

**ACOS Rules:**
- ACOS Objetivo = metade da margem de lucro bruta
- ACOS Maximo = igual a margem (break-even, MPA = 0)
- Example: Margin 40% -> ACOS target 20%, ACOS max 40%

**Step 4 — Cross-reference with target_margin**
- MPA > 0: campanha sustentavel
- MPA = 0: break-even
- MPA < 0: campanha no prejuizo

**Step 5 — Age-adjust benchmarks** (if operation_age known)
- Month 1: ACOS target = 25-40% (normal for launch)
- Month 3: ACOS target = 15-25%
- Month 6+: ACOS target = 10-20%

**Step 6 — Generate Recommendations**
- Apply action from ACOS Decision Matrix
- Flag if impressions low (< 1000/day) -> keyword expansion needed
- Flag if CTR < 0.3% -> listing image/title issue

**Step 7 — Score campaign (0-10)**
- Start at 10, subtract for each deviation
- MPA < 0: score cap = 4
- ACOS > margin: score cap = 3

---

## Workflow 2: Product Validation (PPD Method)

**Step 1 — Collect PPD Data**
Required: search_term, sales_30d, num_sellers, avg_price, num_reviews, avg_rating
Optional: buy_box_price

**Step 2 — Score Each Criterion**

| Criterio | Peso | Verde (1.0) | Amarelo (0.5) | Vermelho (0.0) |
|----------|------|-------------|---------------|----------------|
| Vendas/30d | 30% | 200+ | 50-199 | <50 |
| Vendedores ativos | 20% | 3-15 | 1-2 ou 16-30 | 0 ou 30+ |
| Avaliacoes | 15% | 50+ | 10-49 | <10 |
| Rating medio | 10% | 4.0+ | 3.5-3.9 | <3.5 |
| Preco/margem | 25% | >30% | 15-30% | <15% |

**Step 3 — Calculate Final Score (0-10)**
```
weighted_score = sum(criterio_score * peso)
final_score = weighted_score * 10
```

**Step 4 — Assign Traffic Light**
- >= 7.0: Verde (produto viavel, prosseguir)
- 4.0-6.9: Amarelo (produto com ressalvas, avaliar riscos)
- < 4.0: Vermelho (produto inviavel, nao entrar)

**Step 5 — Buy Box Competitiveness**
- Spread > 15%: flag as risk (price war likely)

---

## Workflow 3: Listing Analytics

**Step 1 — Collect Listing Data**
Required: sessions, conversions (or conversion_rate), period_days
Optional: page_views, buy_box_percentage

**Step 2 — Calculate Conversion Rate**
CVR = (conversions / sessions) * 100 (if not provided directly)

**Step 3 — Diagnose Conversion Tier**

| Taxa | Status | Acao Principal |
|------|--------|----------------|
| 4%+ | Excelente | Nao mexer, escalar Ads |
| 2-4% | Bom | Manter, pequenos ajustes |
| 1.5-2% | Medio | Revisar imagens e bullet points |
| 1-1.5% | Baixo | Otimizar urgente: titulo, imagens, preco |
| <1% | Critico | Recriar listagem do zero |

**Step 4 — Identify Root Cause by Tier**
- Critico (<1%): listing fundamental problem (title/images/price)
- Baixo (1-1.5%): optimization opportunity (bullets, A+, reviews)
- Buy Box < 80%: flag as suppression risk

**Step 5 — Output prioritized optimization plan**

---

## Workflow 4: Business Intelligence Report

**Step 1 — Collect Period Data**
Total revenue (organic + paid), paid revenue, ad spend, inventory turnover

**Step 2 — Calculate Split**
```
organic_revenue = total_revenue - paid_revenue
organic_pct = (organic_revenue / total_revenue) * 100
TACOS = (ad_spend / total_revenue) * 100
```

**Step 3 — Compare to Maturation Benchmark**

```
Month 1:  Ads 90% | Org 10% | ACOS 25-40% | Phase: Launch
Month 3:  Ads 70% | Org 30% | ACOS 15-25% | Phase: Growth
Month 6:  Ads 50% | Org 50% | ACOS 10-20% | Phase: Consolidation
Month 12: Ads 30% | Org 70% | ACOS 8-15%  | Phase: Maturity
```

**Step 4 — Seasonality Check**
Flag high-seasonality periods (Nov/Dec Black Friday, May mothers day, June festas)

**Step 5 — Generate Business Report**

---

## Campaign Type Benchmarks

| Tipo | ACOS Esperado | Uso Principal |
|------|--------------|---------------|
| Auto | 25-40% | Discovery de keywords |
| Manual Exact | 8-20% | Conversao eficiente |
| Manual Broad | 15-30% | Expansao de alcance |
| Brand Defense | 5-12% | Protecao de marca |
| Display | 20-45% | Remarketing e awareness |

---

## Phase 4: Output Generation

1. Set `traffic_light`: green (score >= 7), yellow (4-6.9), red (< 4)
2. Generate `recommendations` — maximum 5, ordered by ROI impact
3. Generate `risks` — maximum 3, ordered by severity
4. Write `projected_improvement` as specific percentage or revenue change
5. Validate: every recommendation must reference a specific metric
