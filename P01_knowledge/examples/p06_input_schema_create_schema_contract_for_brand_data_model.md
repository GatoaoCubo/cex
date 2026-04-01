---
id: p06_is_brand_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "input-schema-builder"
scope: "brand configuration and identity data capture for CEX system initialization"
fields:
  - name: "brand_name"
    type: "string"
    required: true
    default: null
    description: "Official company or brand name"
    error_message: "brand_name is required — provide your company/brand name"
  - name: "description"
    type: "string"
    required: true
    default: null
    description: "One sentence describing what the brand does"
    error_message: "description is required — describe what your brand does in one sentence"
  - name: "core_values"
    type: "list"
    required: true
    default: null
    description: "List of 3 core brand values"
    error_message: "core_values is required — provide exactly 3 core brand values"
  - name: "personality_formal"
    type: "boolean"
    required: false
    default: false
    description: "Whether brand personality is formal (true) or casual (false)"
    error_message: null
  - name: "personality_technical"
    type: "boolean"
    required: false
    default: false
    description: "Whether brand personality is technical (true) or friendly (false)"
    error_message: null
  - name: "target_audience"
    type: "string"
    required: true
    default: null
    description: "Description of ideal customer or target audience"
    error_message: "target_audience is required — describe your ideal customer"
  - name: "revenue_model"
    type: "string"
    required: false
    default: "subscription"
    description: "How the brand makes money: subscription, one-time, courses, consulting"
    error_message: null
  - name: "industry"
    type: "string"
    required: false
    default: "technology"
    description: "Primary industry or sector"
    error_message: null
  - name: "primary_color"
    type: "string"
    required: false
    default: "#2563eb"
    description: "Primary brand color in hex format"
    error_message: null
  - name: "secondary_color"
    type: "string"
    required: false
    default: "#64748b"
    description: "Secondary brand color in hex format"
    error_message: null
  - name: "website"
    type: "string"
    required: false
    default: null
    description: "Brand website URL"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Split comma-separated core_values string into list if provided as single string"
  - from: "string"
    to: "boolean"
    rule: "Parse 'true', 'yes', '1' as true; 'false', 'no', '0' as false for personality fields"
examples:
  - brand_name: "TechCorp"
    description: "We build AI-powered productivity tools for remote teams"
    core_values: ["innovation", "transparency", "customer-first"]
    personality_formal: false
    personality_technical: true
    target_audience: "Remote team managers and productivity enthusiasts"
    revenue_model: "subscription"
    industry: "technology"
    primary_color: "#2563eb"
    website: "https://techcorp.com"
  - brand_name: "Design Studio"
    description: "Creative agency specializing in brand identity and web design"
    core_values: ["creativity", "collaboration", "excellence"]
    target_audience: "Small business owners who value premium design"
    revenue_model: "one-time"
    industry: "design"
domain: "brand-configuration"
quality: 8.9
tags: [input-schema, brand-data, configuration, identity, cex-bootstrap]
tldr: "Input contract for brand data model: requires brand_name, description, core_values, target_audience with optional personality and visual settings."
density_score: 0.92
---
## Contract Definition
Brand data model input schema serves the CEX bootstrap process and brand configuration system. Callers (typically the initialization process or brand setup wizard) provide essential brand identity information including name, description, values, personality traits, and target audience. This schema ensures consistent brand data capture across all CEX nuclei and enables automatic brand context injection into prompts and outputs.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | brand_name | string | YES | - | Official company or brand name |
| 2 | description | string | YES | - | One sentence describing what the brand does |
| 3 | core_values | list | YES | - | List of 3 core brand values |
| 4 | personality_formal | boolean | NO | false | Whether brand personality is formal (true) or casual (false) |
| 5 | personality_technical | boolean | NO | false | Whether brand personality is technical (true) or friendly (false) |
| 6 | target_audience | string | YES | - | Description of ideal customer or target audience |
| 7 | revenue_model | string | NO | "subscription" | How the brand makes money: subscription, one-time, courses, consulting |
| 8 | industry | string | NO | "technology" | Primary industry or sector |
| 9 | primary_color | string | NO | "#2563eb" | Primary brand color in hex format |
| 10 | secondary_color | string | NO | "#64748b" | Secondary brand color in hex format |
| 11 | website | string | NO | null | Brand website URL |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Split comma-separated core_values string into list if provided as single string |
| string | boolean | Parse 'true', 'yes', '1' as true; 'false', 'no', '0' as false for personality fields |

## Examples
```json
{
  "brand_name": "TechCorp",
  "description": "We build AI-powered productivity tools for remote teams",
  "core_values": ["innovation", "transparency", "customer-first"],
  "personality_formal": false,
  "personality_technical": true,
  "target_audience": "Remote team managers and productivity enthusiasts",
  "revenue_model": "subscription",
  "industry": "technology",
  "primary_color": "#2563eb",
  "website": "https://techcorp.com"
}
```

## Constraints
- core_values must contain exactly 3 values when provided as list
- color fields must be valid hex color codes when provided
- website must be valid URL format when provided
- revenue_model must be one of: subscription, one-time, courses, consulting, licensing
- Maximum payload size: 2KB
- String fields have maximum length of 500 characters each

## References
- CEX Bootstrap Protocol: `.claude/rules/brand-bootstrap.md`
- Brand Configuration: `.cex/brand/brand_config.yaml`
- Brand Injection System: `brand_inject.py`