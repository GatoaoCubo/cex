---
# TEMPLATE: Scraper (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.scraper)
# Max 1024 bytes

id: p04_scraper_{{TARGET_SLUG}}
type: scraper
lp: P04
title: "Scraper: {{TARGET_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Scraper: {{TARGET_NAME}}

## Target
- Source: {{URL_OR_SITE}}
- Data wanted: {{PRIMARY_FIELDS}}
- Cadence: {{ONE_SHOT|DAILY|ON_DEMAND}}

## Extraction Plan
1. {{LOAD_PAGE_OR_ENDPOINT}}
2. {{SELECT_RELEVANT_NODES}}
3. {{NORMALIZE_FIELDS}}

## Output
```yaml
items:
  - {{FIELD_1}}: {{EXAMPLE_VALUE}}
    {{FIELD_2}}: {{EXAMPLE_VALUE}}
```
