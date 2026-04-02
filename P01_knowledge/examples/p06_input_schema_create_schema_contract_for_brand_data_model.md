---
id: p06_is_brand_data_model
kind: input_schema
pillar: P06
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "input-schema-builder"
scope: "brand configuration data model for CEX system initialization"
fields:
  - name: "brand_name"
    type: "string"
    required: true
    default: null
    description: "Official company or brand name"
    error_message: "brand_name is required - provide your company or brand name"
  - name: "description"
    type: "string" 
    required: true
    default: null
    description: "One-sentence description of what the brand does"
    error_message: "description is required - provide what your brand does in one sentence"
  - name: "core_values"
    type: "list"
    required: true
    default: null
    description: "List of 3-5 core brand values"
    error_message: "core_values is required - provide 3-5 core values as a list"
  - name: "personality"
    type: "string"
    required: false
    default: "professional"
    description: "Brand personality descriptor (formal, casual, technical, friendly)"
    error_message: null
  - name: "target_audience"
    type: "string"
    required: false
    default: "professionals"
    description: "Primary target customer segment"
    error_message: null
  - name: "revenue_model"
    type: "string"
    required: false
    default: "services"
    description: "How the brand makes money (subscription, one-time, courses, services)"
    error_message: null
  - name: "industry"
    type: "string"
    required: false
    default: null
    description: "Primary industry or sector"
    error_message: null
  - name: "brand_colors"
    type: "object"
    required: false
    default: null
    description: "Brand color palette with primary and secondary colors"
    error_message: null
  - name: "tone_keywords"
    type: "list"
    required: false
    default: ["clear", "professional", "helpful"]
    description: "Keywords that describe desired communication tone"
    error_message: null
  - name: "differentiation"
    type: "string"
    required: false
    default: null
    description: "What makes this brand unique from competitors"
    error_message: null
coercion:
  - from: "string"
    to: "list"
    rule: "Split comma-separated values into list for core_values and tone_keywords"
  - from: "object"
    to: "string"
    rule: "Serialize brand_colors object to JSON string for storage"
examples:
  - brand_name: "TechFlow Solutions"
    description: "We help startups build scalable software platforms"
    core_values: ["innovation", "reliability", "customer-first", "transparency"]
    personality: "technical but approachable"
    target_audience: "B2B startup founders"
    revenue_model: "subscription"
    industry: "SaaS"
    tone_keywords: ["clear", "confident", "technical"]
  - brand_name: "Creative Studio X"
    description: "Design agency specializing in brand identity for emerging companies"
    core_values: ["creativity", "collaboration", "excellence"]
    personality: "creative and energetic"
    target_audience: "emerging companies needing brand design"
    revenue_model: "project-based"
    industry: "design"
    brand_colors: {"primary": "#FF6B35", "secondary": "#004E89"}
domain: "brand-configuration"
quality: 9.1
tags: [input-schema, brand-data, configuration, identity, CEX]
tldr: "Input contract for brand data model: requires name, description, values; optional personality, audience, revenue model, and brand assets."
density_score: 0.92
---
## Contract Definition
The brand data model input schema defines the required and optional data fields needed to configure a CEX system for a specific brand identity. This schema serves the brand bootstrap process and ongoing brand configuration updates throughout the system.

## Fields
| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | brand_name | string | YES | - | Official company or brand name |
| 2 | description | string | YES | - | One-sentence description of what the brand does |
| 3 | core_values | list | YES | - | List of 3-5 core brand values |
| 4 | personality | string | NO | "professional" | Brand personality descriptor |
| 5 | target_audience | string | NO | "professionals" | Primary target customer segment |
| 6 | revenue_model | string | NO | "services" | How the brand makes money |
| 7 | industry | string | NO | null | Primary industry or sector |
| 8 | brand_colors | object | NO | null | Brand color palette with primary/secondary |
| 9 | tone_keywords | list | NO | ["clear", "professional", "helpful"] | Communication tone descriptors |
| 10 | differentiation | string | NO | null | What makes this brand unique |

## Coercion Rules
| From | To | Rule |
|------|----|------|
| string | list | Split comma-separated values for core_values and tone_keywords |
| object | string | Serialize brand_colors object to JSON for storage |

## Examples
```json
{
  "brand_name": "TechFlow Solutions",
  "description": "We help startups build scalable software platforms",
  "core_values": ["innovation", "reliability", "customer-first", "transparency"],
  "personality": "technical but approachable",
  "target_audience": "B2B startup founders",
  "revenue_model": "subscription",
  "industry": "SaaS",
  "tone_keywords": ["clear", "confident", "technical"]
}
```

## References
- CEX Brand Bootstrap Protocol (.claude/rules/brand-bootstrap.md)
- Brand Configuration System (_tools/cex_bootstrap.py)
- Brand Identity Propagation (brand_inject.py, brand_propagate.py)