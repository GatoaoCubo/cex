---
kind: schema
id: bld_schema_ecommerce_vertical
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for ecommerce_vertical
quality: 9.1
title: "Schema Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for ecommerce_vertical"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "ecommerce_vertical" | Fixed value |
| pillar | string | yes | "P01" | Fixed value |
| title | string | yes | null | Descriptive name |
| version | string | yes | "1.0" | Schema version |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Owner/creator |
| domain | string | yes | "ecommerce" | Fixed value |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | array | yes | [] | Keywords for categorization |
| tldr | string | yes | null | Summary of core purpose |
| product_category | string | yes | null | E.g., "apparel", "electronics" |
| sales_volume | number | yes | null | Monthly revenue in USD |

### Recommended
| Field | Type | Notes |
|---|---|---|
| average_order_value | number | Optional metric |
| customer_segment | string | E.g., "B2C", "B2B" |

## ID Pattern
^p01_ev_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Product Catalog Structure**
   Define hierarchical categorization and metadata standards.

2. **Sales Performance Metrics**
   Include KPIs like conversion rate, CAC, and CLV.

3. **Customer Behavior Analysis**
   Segment users by purchase frequency, basket size, and preferences.

4. **Marketing Channel Effectiveness**
   Track ROI for ads, email campaigns, and referral programs.

5. **Inventory Management Protocols**
   Specify restocking thresholds and supplier SLAs.

6. **Compliance and Data Privacy**
   Align with GDPR, CCPA, and regional e-commerce laws.

## Constraints
- All numeric fields must use ISO 4217 currency codes.
- Product categories must adhere to a predefined taxonomy.
- Sales_volume updates must occur at least monthly.
- Tags must be lowercase, alphanumeric, and underscore-separated.
- Author must be a registered contributor in the CEX system.
- Version increments require peer review approval.
