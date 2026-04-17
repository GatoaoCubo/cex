---
kind: output_template
id: bld_output_template_ecommerce_vertical
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for ecommerce_vertical production
quality: 9.1
title: "Output Template Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, output_template]
tldr: "Template with vars for ecommerce_vertical production"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

```markdown
---
id: p01_ev_{{vertical_slug}}_{{use_case_slug}}.md
kind: ecommerce_vertical
pillar: P01
product_category: {{product_category}}   <!-- apparel | electronics | marketplace | grocery | beauty -->
sales_volume: {{sales_volume}}           <!-- Monthly GMV in USD -->
average_order_value: {{aov}}             <!-- Optional: avg order value USD -->
customer_segment: {{customer_segment}}  <!-- B2C | B2B | D2C -->
quality: null
title: "Ecommerce Vertical: {{title}}"
version: "1.0.0"
created: {{created_date}}
updated: {{updated_date}}
author: {{author}}
domain: ecommerce
tags: [{{tag_1}}, {{tag_2}}, ecommerce_vertical]
tldr: "{{one_sentence_summary}}"
---

## Checkout Flow
1. Cart review
2. Address + delivery selection ({{delivery_options}})
3. Payment: {{payment_methods}}   <!-- Stripe | Klarna | Affirm | PayPal -->
4. Order confirmation + receipt

### PCI-DSS Compliance
Scope reduction method: {{pci_scope_method}}   <!-- tokenization | P2PE | hosted fields -->
PCI-DSS level: {{pci_level}}                   <!-- Level 1 | Level 2 | Level 3 | Level 4 -->
Encryption: {{encryption_spec}}               <!-- TLS 1.3, AES-256 -->

## Recommendation Engine
Algorithm: {{rec_algorithm}}   <!-- collaborative filtering | content-based | hybrid | session-based -->
Data signals: {{data_signals}} <!-- purchase history, browse behavior, real-time session -->
Lift metric: {{lift_metric}}   <!-- CTR, AOV uplift, conversion rate improvement -->

## Fraud Detection
| Layer | Technique | Threshold | Action |
|-------|-----------|-----------|--------|
| {{layer_1}} | {{technique_1}} | {{threshold_1}} | {{action_1}} |
| {{layer_2}} | {{technique_2}} | {{threshold_2}} | {{action_2}} |

3DS2 / CNP prevention: {{threeds_config}}

## Abandoned Cart Recovery
Trigger: {{trigger_delay}}     <!-- e.g., 1h after last cart activity -->
Channel: {{recovery_channel}}  <!-- email | SMS | push -->
Discount offer: {{discount_pct}}%

## Performance Targets
| Metric | Target | Method |
|--------|--------|--------|
| Checkout load time | <=2s | Lighthouse p95 |
| Cart abandonment rate | <{{target_abandonment}}% | GA4 funnel |
| Recommendation CTR | >{{target_ctr}}% | A/B test |
| Fraud false positive rate | <{{target_fp}}% | Fraud platform |
```
