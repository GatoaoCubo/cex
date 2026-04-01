---
id: p03_pt_brand_tasks
kind: prompt_template
pillar: P03
title: "Brand Task Execution Template"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: prompt-template-builder
variables:
  - name: brand_name
    type: string
    required: true
    default: null
    description: The official name of the brand or company
  - name: brand_personality
    type: string
    required: true
    default: null
    description: Core personality traits and tone (e.g., professional, friendly, innovative, trustworthy)
  - name: brand_values
    type: list
    required: true
    default: null
    description: List of 3-5 core brand values that guide all communications
  - name: target_audience
    type: string
    required: true
    default: null
    description: Primary target demographic or customer segment
  - name: task_type
    type: string
    required: true
    default: null
    description: Specific brand task (messaging, positioning, voice guide, tagline, etc.)
  - name: context
    type: string
    required: false
    default: "general business context"
    description: Additional context or background information relevant to the task
  - name: output_format
    type: string
    required: false
    default: "structured document"
    description: Desired format for the output (bullet points, paragraph, guidelines, etc.)
  - name: constraints
    type: list
    required: false
    default: []
    description: Any specific constraints or requirements to consider
variable_syntax: "mustache"
composable: false
domain: brand
quality: 9.0
tags: [prompt-template, brand, marketing, identity, reusable]
tldr: "Generates brand-consistent content for various brand development and management tasks."
keywords: [brand, identity, messaging, positioning, voice, values, personality, marketing]
density_score: 0.89
---
# Brand Task Execution Template

## Purpose
Produces brand-consistent content for various brand development and management tasks. Reuse scope: any brand-related deliverable requiring alignment with established brand identity, values, and personality. Invoke once per brand task; vary `task_type`, `context`, and `output_format` to produce distinct brand assets from the same strategic foundation.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| brand_name | string | true | null | The official name of the brand or company |
| brand_personality | string | true | null | Core personality traits and tone (e.g., professional, friendly, innovative) |
| brand_values | list | true | null | List of 3-5 core brand values that guide all communications |
| target_audience | string | true | null | Primary target demographic or customer segment |
| task_type | string | true | null | Specific brand task (messaging, positioning, voice guide, tagline, etc.) |
| context | string | false | "general business context" | Additional context or background information relevant to the task |
| output_format | string | false | "structured document" | Desired format for the output (bullet points, paragraph, guidelines, etc.) |
| constraints | list | false | [] | Any specific constraints or requirements to consider |

## Template Body
```
You are a brand strategist working on {{task_type}} for {{brand_name}}.

BRAND FOUNDATION:
- Brand Name: {{brand_name}}
- Brand Personality: {{brand_personality}}
- Core Values: {{#brand_values}}{{.}}{{#unless @last}}, {{/unless}}{{/brand_values}}
- Target Audience: {{target_audience}}

TASK CONTEXT:
- Specific Task: {{task_type}}
- Context: {{context}}
- Output Format: {{output_format}}
{{#constraints}}
- Constraint: {{.}}
{{/constraints}}

INSTRUCTIONS:
Create {{task_type}} content that:
1. Authentically reflects {{brand_name}}'s {{brand_personality}} personality
2. Aligns with all stated brand values: {{#brand_values}}{{.}}{{#unless @last}}, {{/unless}}{{/brand_values}}
3. Resonates with the {{target_audience}} demographic
4. Maintains consistency with existing brand communications
5. Addresses the specific context: {{context}}

Deliver the output in {{output_format}} format. Ensure every element reinforces {{brand_name}}'s brand identity and speaks directly to {{target_audience}}.

Focus on creating content that is both strategically sound and practically implementable across {{brand_name}}'s communications channels.
```

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 | PASS | Frontmatter parses as valid YAML |
| H02 | PASS | ID `p03_pt_brand_tasks` matches pattern `^p03_pt_[a-z][a-z0-9_]+$` |
| H03 | PASS | ID equals filename stem |
| H04 | PASS | Kind equals literal `prompt_template` |
| H05 | PASS | Quality field is null |
| H06 | PASS | All required frontmatter fields present |
| H07 | PASS | Body contains 8 `{{variable}}` placeholders |
| H08 | PASS | All body variables declared in Variables section |

## Examples
### Variables
```yaml
brand_name: "TechFlow Solutions"
brand_personality: "innovative, reliable, customer-focused"
brand_values: ["Innovation", "Reliability", "Customer Success", "Transparency", "Excellence"]
target_audience: "mid-market technology companies and their decision-makers"
task_type: "brand positioning statement"
context: "launching new AI-powered workflow automation platform"
output_format: "concise positioning statement with supporting rationale"
constraints: ["must differentiate from competitors", "emphasize enterprise security"]
```

### Rendered Output
```
You are a brand strategist working on brand positioning statement for TechFlow Solutions.

BRAND FOUNDATION:
- Brand Name: TechFlow Solutions
- Brand Personality: innovative, reliable, customer-focused
- Core Values: Innovation, Reliability, Customer Success, Transparency, Excellence
- Target Audience: mid-market technology companies and their decision-makers

TASK CONTEXT:
- Specific Task: brand positioning statement
- Context: launching new AI-powered workflow automation platform
- Output Format: concise positioning statement with supporting rationale
- Constraint: must differentiate from competitors
- Constraint: emphasize enterprise security

INSTRUCTIONS:
Create brand positioning statement content that:
1. Authentically reflects TechFlow Solutions's innovative, reliable, customer-focused personality
2. Aligns with all stated brand values: Innovation, Reliability, Customer Success, Transparency, Excellence
3. Resonates with the mid-market technology companies and their decision-makers demographic
4. Maintains consistency with existing brand communications
5. Addresses the specific context: launching new AI-powered workflow automation platform

Deliver the output in concise positioning statement with supporting rationale format. Ensure every element reinforces TechFlow Solutions's brand identity and speaks directly to mid-market technology companies and their decision-makers.

Focus on creating content that is both strategically sound and practically implementable across TechFlow Solutions's communications channels.
```