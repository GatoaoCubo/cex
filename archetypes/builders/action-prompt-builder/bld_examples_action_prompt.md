---
kind: examples
id: bld_examples_action_prompt
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of action_prompt artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: action-prompt-builder
## Golden Example
INPUT: "Create action prompt for extracting product metrics from marketplace scrape data"
OUTPUT:
```yaml
id: p03_ap_extract_product_metrics
kind: action_prompt
pillar: P03
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder_agent"
title: "Extract Product Metrics from Marketplace Scrape"
action: "Extract and normalize product metrics from raw marketplace scrape data"
input_required:
  - "scrape_data: JSON object with raw marketplace response"
  - "marketplace: enum (mercado_livre, shopee, amazon_br)"
output_expected: "Normalized JSON with price, rating, reviews_count, seller_score, availability"
purpose: "Enables cross-marketplace comparison by normalizing heterogeneous scrape formats"
steps_count: 4
timeout: "30s"
edge_cases:
  - "Missing price field (some listings show 'Sob consulta')"
  - "Rating format varies (4.5 vs 4,5 vs 45/50)"
  - "Seller score absent on new sellers"
constraints:
  - "Do NOT infer missing data — use null"
  - "Do NOT convert currencies"
domain: "research"
quality: null
tags: [action_prompt, marketplace, metrics, extraction, research]
tldr: "Extract and normalize product metrics from raw marketplace scrape into structured JSON for comparison"
density_score: 0.92
```
## Context
Marketplace scrapes return heterogeneous formats per platform. This prompt normalizes
raw scrape data into a consistent schema for cross-marketplace product comparison.
Purpose: enable pricing and competitive analysis across ML, Shopee, Amazon BR.
## Input
| Item | Type | Format | Required |
|------|------|--------|----------|
| scrape_data | JSON object | Raw marketplace API/scrape response | YES |
| marketplace | enum string | mercado_livre, shopee, amazon_br | YES |
## Execution
1. Identify marketplace-specific field mappings for price, rating, reviews, seller
2. Extract each metric, applying format normalization (comma->dot, percentage->decimal)
3. Set missing fields to null (never infer)
4. Return normalized JSON object
## Output
Format: JSON
Structure:
```json
{
  "price_brl": 149.90,
  "rating": 4.5,
  "reviews_count": 1247,
  "seller_score": 0.95,
  "availability": true
}
```
## Validation
- All 5 output fields present (null OK for missing)
- price_brl is float or null (never string)
- rating normalized to 0.0-5.0 scale
- Edge case: "Sob consulta" -> price_brl: null
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_ap_ pattern (H02 pass)
- kind: action_prompt (H04 pass)
- 21 required fields present (H06 pass)
- edge_cases: 3 entries >= 2 (H07 pass)
- body has all 5 sections (H08 pass)
- action is verb phrase "Extract and normalize..." (S03 pass)
- input_required lists specific types (S04 pass)
- output_expected is verifiable JSON structure (S05 pass)
- No identity/persona content (S07 pass)
## Anti-Example
INPUT: "Create action prompt for analyzing data"
BAD OUTPUT:
```yaml
id: analyze-data
kind: prompt
pillar: prompt
action: data analysis
input_required: some data
output_expected: analysis results
quality: 9.0
tags: [analysis]
edge_cases: []
```
You are a data analysis expert. Analyze the provided data thoroughly and
provide comprehensive insights. Make sure your analysis is detailed and helpful.
FAILURES:
1. id: no `p03_ap_` prefix, uses hyphens -> H02 FAIL
2. kind: "prompt" not "action_prompt" -> H04 FAIL
3. pillar: "prompt" not "P03" -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. edge_cases: empty list (need >= 2) -> H07 FAIL
6. Missing fields: version, created, updated, author, title, purpose, domain -> H06 FAIL
7. action: "data analysis" is noun phrase, not verb phrase -> S03 FAIL
8. input_required: "some data" is vague string, not typed list -> S04 FAIL
9. Contains persona ("You are a data analysis expert") -> S07 FAIL
10. No ## Context, ## Input, ## Execution, ## Output, ## Validation sections -> H08 FAIL
