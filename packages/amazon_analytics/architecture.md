# Amazon Analytics Agent — Architecture

## System Components

### 1. Campaign Analytics Engine

**Purpose**: Process advertising campaign metrics and produce actionable ACOS/ROAS diagnosis.

```
Inputs:  spend, sales, impressions, clicks, orders, period_days, target_margin
Process: Calculate ACOS, ROAS, CTR, CPC, CVR, MPA, TACOS
         Apply ACOS Decision Matrix (6-tier)
         Cross-reference margin for MPA calculation
         Detect anomalies (low impressions, poor CTR, high CPC)
Outputs: ACOS tier diagnosis, MPA, campaign health score, action plan
```

Key formulas:
```
ACOS  = (spend / sales) * 100
ROAS  = sales / spend
CTR   = (clicks / impressions) * 100
CPC   = spend / clicks
CVR   = (orders / clicks) * 100
MPA   = target_margin - ACOS
TACOS = (spend / total_revenue) * 100
```

### 2. Product Validation Engine (PPD)

**Purpose**: Score product viability using the PPD (Produto Por Demanda) method.

```
Inputs:  search_term, sales_30d, num_sellers, avg_price, num_reviews, avg_rating, target_margin
Process: Score each of 5 criteria (Verde=1.0, Amarelo=0.5, Vermelho=0.0)
         Apply weights (vendas 30%, preco 25%, vendedores 20%, avaliacoes 15%, rating 10%)
         Calculate weighted score 0-10
         Assign traffic light signal
Outputs: PPD scorecard, weighted score, traffic light, per-criterion breakdown
```

Scoring formula:
```
weighted_score = (
  score_vendas * 0.30 +
  score_preco  * 0.25 +
  score_vendedores * 0.20 +
  score_avaliacoes * 0.15 +
  score_rating * 0.10
)
final_score = weighted_score * 10
```

### 3. Listing Analytics Engine

**Purpose**: Diagnose listing conversion performance and prescribe optimization actions.

```
Inputs:  sessions, conversions, conversion_rate, page_views, buy_box_percentage, period_days
Process: Calculate or validate conversion_rate
         Apply 5-tier conversion benchmark
         Identify root cause by tier
         Match symptoms to listing elements (title, images, bullets, price, reviews)
Outputs: Conversion tier, diagnosis, prioritized listing optimization plan
```

### 4. Business Intelligence Engine

**Purpose**: Macro-level business health — organic/paid split, seasonality, maturation.

```
Inputs:  total_revenue, paid_revenue, ad_spend, product_age_months, period_data
Process: Calculate organic vs paid split
         Calculate TACOS
         Compare to maturation curve benchmarks
         Detect seasonality patterns (Nov/Dec, May, June)
Outputs: Business health report, maturation phase, TACOS, split analysis
```

## Data Flow Diagram

```
                    +-------------------------------+
                    |   amazon-analytics-agent       |
                    +-------------------------------+
                                  |
          +-----------------------+------------------------+
          |                       |                        |
   +------v------+        +------v-------+        +-------v------+
   |  Campaign   |        |   Product    |        |   Listing    |
   |  Analytics  |        |  Validation  |        |  Analytics   |
   |  Engine     |        |  Engine(PPD) |        |  Engine      |
   +------+------+        +------+-------+        +-------+------+
          |                       |                        |
          +-----------------------+------------------------+
                                  |
                    +-------------v--------------+
                    |   Business Intelligence     |
                    |   Engine                    |
                    |   (Aggregates all signals)  |
                    +-------------+--------------+
                                  |
                    +-------------v--------------+
                    |   Structured Output         |
                    |   diagnosis + score +       |
                    |   traffic_light +           |
                    |   recommendations + risks   |
                    +----------------------------+
```

## External Integrations

| System | Direction | Data |
|--------|-----------|------|
| amazon-ads-agent | Upstream | Live campaign metrics (ACOS, spend, sales) |
| pesquisa-agent | Upstream | Market research, competitor data |
| SP-API | Upstream | Raw data retrieval (reports, catalog, sales) |
| Seller Central | Upstream | Manual data input (sessions, CVR, Buy Box %) |
| Pricing strategy | Downstream | Margin-aware pricing recommendations |
| Product sourcing | Downstream | PPD validation results |
| Listing optimization | Downstream | Conversion analysis + action plan |

## State Management

The agent is stateless per invocation. It does not persist state between calls.
Historical comparison requires caller to provide previous period data explicitly.
Maturation tracking requires `product_age_months` as explicit input.

## Performance Characteristics

| Metric | Value |
|--------|-------|
| Analysis time (manual data) | < 5 seconds |
| Analysis time (SP-API fetch) | 30-120 seconds (report latency) |
| Minimum data required | 7 days, 20 clicks |
| Max recommendations generated | 5 |
| Output size (typical) | 800-1500 tokens |
