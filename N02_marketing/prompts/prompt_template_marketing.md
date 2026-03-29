---
id: p03_pt_marketing_message
kind: prompt_template
pillar: P03
title: "Marketing Message Template"
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "marketing-team"
variables:
  - name: "product_name"
    type: "string"
    required: true
    default: null
    description: "The name of the product being marketed"
  - name: "customer_segment"
    type: "string"
    required: true
    default: null
    description: "The target customer segment for the message"
  - name: "key_features"
    type: "list"
    required: true
    default: []
    description: "A list of key features of the product"
  - name: "unique_selling_proposition"
    type: "string"
    required: true
    default: null
    description: "The unique selling proposition of the product"
  - name: "benefits"
    type: "list"
    required: false
    default: []
    description: "The main benefits of the product"
  - name: "cta_action"
    type: "string"
    required: false
    default: "Explore now"
    description: "The call-to-action phrase to be used"
variable_syntax: "mustache"
composable: false
domain: "marketing"
quality: null
tags: [marketing, advertisement, product_promotion, template]
tldr: "Creates a marketing message with product details tailored to a specific customer segment."
keywords: [marketing, product, features, benefits, customer, call to action]
density_score: 0.85
---

# Marketing Message Template
## Purpose
This template produces a marketing message by highlighting product features, targeting a specific customer segment, and including a call to action. It's reusable across various marketing campaigns for different products.

## Variables Table
| Name | Type | Required | Default | Description |
|---|---|---|---|---|
| product_name | string | true | null | The name of the product being marketed |
| customer_segment | string | true | null | The target customer segment for the message |
| key_features | list | true | [] | A list of key features of the product |
| unique_selling_proposition | string | true | null | The unique selling proposition of the product |
| benefits | list | false | [] | The main benefits of the product |
| cta_action | string | false | "Explore now" | The call-to-action phrase to be used |

## Template Body
You are crafting a marketing message for {{product_name}}. This message is intended for the {{customer_segment}}. Below are the key elements that we want to emphasize:

1. **Product Name**: {{product_name}}
2. **Customer Segment**: {{customer_segment}}
3. **Key Features**:
   {{#key_features}}
   - {{.}}
   {{/key_features}}
4. **Unique Selling Proposition**: {{unique_selling_proposition}}
5. **Benefits**:
   {{#benefits}}
   - {{.}}
   {{/benefits}}
6. **Call to Action**: {{cta_action}}

Encourage potential customers within the {{customer_segment}} to discover the benefits and unique offerings of {{product_name}} today!

## Quality Gates
| Gate | Status | Notes |
|---|---|---|
| H01 id pattern | PASS | `p03_pt_marketing_message` matches `^p03_pt_[a-z][a-z0-9_]+$` |
| H02 required fields | PASS | id, kind, title, variables, quality all present |
| H03 no undeclared vars | PASS | All `{{vars}}` in body declared in variables list |
| H04 no unused vars | PASS | All 6 declared variables appear in template body |
| H05 size <= 8192 bytes | PASS | ~1.5KB |
| H06 valid syntax tier | PASS | variable_syntax: mustache |

## Examples
### Filled Example
**Variables:**
---
yaml
product_name: "EcoSmart Light Bulb"
customer_segment: "Eco-conscious Consumers"
key_features: ["Energy efficient", "Long-lasting", "Cost-effective"]
unique_selling_proposition: "The green choice for a brighter future"
benefits: ["Reduce energy bills", "Less frequent replacements"]
cta_action: "Buy now"
```
**Rendered Output:**
You are crafting a marketing message for EcoSmart Light Bulb. This message is intended for the Eco-conscious Consumers. Below are the key elements that we want to emphasize:

1. **Product Name**: EcoSmart Light Bulb
2. **Customer Segment**: Eco-conscious Consumers
3. **Key Features**:
   - Energy efficient
   - Long-lasting
   - Cost-effective
4. **Unique Selling Proposition**: The green choice for a brighter future
5. **Benefits**:
   - Reduce energy bills
   - Less frequent replacements
6. **Call to Action**: Buy now

Encourage potential customers within the Eco-conscious Consumers to discover the benefits and unique offerings of EcoSmart Light Bulb today!
```