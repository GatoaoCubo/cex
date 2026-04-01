---
id: p06_is_brand_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "brand configuration and identity data model setup"
fields:
  - name: "brand_name"
    type: "string"
    required: true
    default: null
    description: "Official brand or company name"
    error_message: "brand_name is required — provide your company or brand name"
  - name: "brand_description"
    type: "string"
    required: false
    default: ""
    description: "One-sentence description of what the brand does"
    error_message: null
  - name: "core_values"
    type: "list"
    required: true
    default: null
    description: "List of 3-5 core brand values or principles"
    error_message: "core_values is required — provide at least 3 brand values"
  - name: "brand_personality"
    type: "string"
    required: false
    default: "professional"
    description: "Brand personality: formal, casual, technical, friendly, authoritative"
    error_message: null
  - name: "target_customer"
    type: "string"
    required: false
    default: "business professionals"
    description: "Primary target customer or audience description"
    error_message: null
  - name: "revenue_model"
    type: "string"
    required: false
    default: "services"
    description: "How the brand makes money: subscription, one-time, courses, services, products"
    error_message: null
  - name: "brand_colors"
    type: "object"
    required: false
    default: {"primary": "#000000", "secondary": "#FFFFFF"}
    description: "Brand color palette with primary and secondary colors"
    error_message: null
  - name: "logo_url"
    type: "string"
    required: false
    default: null
    description: "URL or path to brand logo image"
    error_message: null
  - name: "website_url"
    type: "string"
    required: false
    default: null
    description: "Official brand website URL"
    error_message: null
  - name: "industry"
    type: "string"
    required: false
    default: "technology"
    description: "Primary industry or business sector"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Split comma-separated core_values string into list"
  - from: "string"
    to: "object"
    rule: "Parse JSON string for brand_colors if provided as string"
examples:
  - brand_name: "TechFlow Solutions"
    brand_description: "AI-powered workflow automation for enterprises"
    core_values: ["innovation", "reliability", "customer-first", "transparency"]
    brand_personality: "technical"
    target_customer: "enterprise software teams"
    revenue_model: "subscription"
  - brand_name: "Creative Studio Plus"
    core_values: ["creativity", "quality", "collaboration"]
    brand_colors: {"primary": "#FF6B35", "secondary": "#F7F7F7"}
    website_url: "https://creativestudioplus.com"
domain: "brand-configuration"
quality: 8.9
tags: [input-schema, brand-data-model, configuration, identity]
tldr: "Input contract for brand data model configuration: requires brand_name and core_values, optional personality, colors, and business details."
density_score: 0.87
---
## Contract Definition
Brand data model input schema defines the required and optional data for configuring brand identity within the CEX system. Used by brand configuration tools, bootstrap processes, and brand validation systems to ensure consistent brand data structure.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | brand_name | string | YES | - | Official brand or company name |
| 2 | brand_description | string | NO | "" | One-sentence description of what the brand does |
| 3 | core_values | list | YES | - | List of 3-5 core brand values or principles |
| 4 | brand_personality | string | NO | "professional" | Brand personality: formal, casual, technical, friendly, authoritative |
| 5 | target_customer | string | NO | "business professionals" | Primary target customer or audience description |
| 6 | revenue_model | string | NO | "services" | How the brand makes money: subscription, one-time, courses, services, products |
| 7 | brand_colors | object | NO | {"primary": "#000000", "secondary": "#FFFFFF"} | Brand color palette with primary and secondary colors |
| 8 | logo_url | string | NO | null | URL or path to brand logo image |
| 9 | website_url | string | NO | null | Official brand website URL |
| 10 | industry | string | NO | "technology" | Primary industry or business sector |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Split comma-separated core_values string into list |
| string | object | Parse JSON string for brand_colors if provided as string |

## Examples
```json
{
  "brand_name": "TechFlow Solutions",
  "brand_description": "AI-powered workflow automation for enterprises",
  "core_values": ["innovation", "reliability", "customer-first", "transparency"],
  "brand_personality": "technical",
  "target_customer": "enterprise software teams",
  "revenue_model": "subscription"
}
```

```json
{
  "brand_name": "Creative Studio Plus",
  "core_values": ["creativity", "quality", "collaboration"],
  "brand_colors": {"primary": "#FF6B35", "secondary": "#F7F7F7"},
  "website_url": "https://creativestudioplus.com"
}
```

## References
- CEX brand_config.yaml specification
- Brand bootstrap protocol (.claude/rules/brand-bootstrap.md)
- Brand validation requirements (brand_validate.py)