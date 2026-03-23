# Amazon Analytics Agent — Output Template

## Campaign Analysis Output

```yaml
analysis_type: campaign
diagnosis: "{{ACOS_TIER_VERDICT}} — {{PLAIN_LANGUAGE_ASSESSMENT}}"
score: {{0_TO_10}}
traffic_light: "{{green|yellow|red}}"

metrics_summary:
  acos:
    current: {{CURRENT_ACOS}}
    target: {{HALF_MARGIN}}
    maximum: {{FULL_MARGIN}}
    verdict: "{{within_target|above_target|above_maximum}}"
  roas:
    current: {{CURRENT_ROAS}}
    minimum_viable: {{MIN_ROAS}}
  tacos:
    current: {{CURRENT_TACOS}}
    target: {{TARGET_TACOS}}
  mpa:
    current: {{MARGIN_MINUS_ACOS}}
    healthy: {{true|false}}
  organic_share:
    current: {{ORGANIC_PCT}}
    target: {{EXPECTED_FOR_AGE}}
    trend: "{{growing|stable|declining}}"

recommendations:
  - priority: 1
    action: "{{SPECIFIC_ACTION}}"
    expected_impact: "{{MEASURABLE_RESULT}}"
    timeline: "{{TIMEFRAME}}"

risks:
  - description: "{{RISK_DESCRIPTION}}"
    probability: "{{high|medium|low}}"
    mitigation: "{{MITIGATION_ACTION}}"

projected_improvement: "{{SPECIFIC_TIME_BOUND_PROJECTION}}"
```

## Product Validation (PPD) Output

```yaml
analysis_type: product_validation
diagnosis: "{{VIABILITY_ASSESSMENT}}"
score: {{0_TO_10}}
traffic_light: "{{green|yellow|red}}"

ppd_scorecard:
  vendas_30d:
    value: {{SALES_COUNT}}
    weight: 0.30
    rating: "{{green|yellow|red}}"
    score: {{WEIGHTED_SCORE}}
  vendedores_ativos:
    value: {{SELLER_COUNT}}
    weight: 0.20
    rating: "{{green|yellow|red}}"
    score: {{WEIGHTED_SCORE}}
  avaliacoes:
    value: {{REVIEW_COUNT}}
    weight: 0.15
    rating: "{{green|yellow|red}}"
    score: {{WEIGHTED_SCORE}}
  rating_medio:
    value: {{AVG_RATING}}
    weight: 0.10
    rating: "{{green|yellow|red}}"
    score: {{WEIGHTED_SCORE}}
  margem_preco:
    value: {{MARGIN_PCT}}
    weight: 0.25
    rating: "{{green|yellow|red}}"
    score: {{WEIGHTED_SCORE}}

weighted_score: {{SUM_OF_WEIGHTED}}
recommendation: "{{Entrar|Entrar com cautela|Evitar}}"

risks:
  - description: "{{RISK}}"
    mitigation: "{{ACTION}}"
```

## Listing Analysis Output

```yaml
analysis_type: listing
diagnosis: "{{CONVERSION_TIER_VERDICT}}"
score: {{0_TO_10}}
traffic_light: "{{green|yellow|red}}"

metrics:
  conversion_rate:
    current: {{CVR}}
    benchmark: "{{excelente|bom|medio|baixo|critico}}"
    target: {{TARGET_CVR}}
  sessions:
    current: {{SESSION_COUNT}}
    trend: "{{growing|stable|declining}}"
  buy_box_percentage:
    current: {{BUY_BOX_PCT}}
    healthy: {{true|false}}

optimization_actions:
  - area: "{{titulo|imagens|bullets|preco|backend_keywords}}"
    current_issue: "{{PROBLEM}}"
    recommended_change: "{{ACTION}}"
    expected_impact: "{{PCT_IMPROVEMENT}}"
```

## Business Intelligence Output

```yaml
analysis_type: business
diagnosis: "{{BUSINESS_HEALTH_ASSESSMENT}}"
score: {{0_TO_10}}

revenue_split:
  organic:
    amount: {{ORGANIC_REVENUE}}
    percentage: {{ORGANIC_PCT}}
    trend: "{{growing|stable|declining}}"
  paid:
    amount: {{PAID_REVENUE}}
    percentage: {{PAID_PCT}}
    trend: "{{growing|stable|declining}}"

maturity_assessment:
  current_phase: "{{launch|growth|maturation|stable}}"
  expected_split: "Month {{N}}: {{X}}% Ads / {{Y}}% Org"
  on_track: {{true|false}}

seasonality:
  current_period: "{{normal|event_name}}"
  impact_on_data: "{{DESCRIPTION}}"
  recommendation: "{{ACTION}}"
```

## Universal Metadata

All outputs include:

```yaml
metadata:
  agent: amazon-analytics-agent
  version: 1.0.0
  analysis_date: "{{ISO_DATE}}"
  data_period_days: {{DAYS}}
  confidence: {{0_TO_1}}
  warnings: ["{{CAVEAT_1}}", "{{CAVEAT_2}}"]
```
