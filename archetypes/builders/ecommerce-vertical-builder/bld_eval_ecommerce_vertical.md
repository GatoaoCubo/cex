---
kind: quality_gate
id: p01_qg_ecommerce_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for ecommerce_vertical
quality: 9.0
title: "Quality Gate Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for ecommerce_vertical"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_ecommerce_vertical
  - p03_sp_ecommerce_vertical_builder
  - bld_knowledge_card_ecommerce_vertical
  - ecommerce-vertical-builder
  - p10_mem_ecommerce_vertical_builder
  - kc_ecommerce_vertical
  - p01_qg_fintech_vertical
  - bld_instruction_ecommerce_vertical
  - bld_instruction_fintech_vertical
  - bld_examples_fintech_vertical
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| required field completeness | 100% | == | all frontmatter fields |
| domain section coverage | 100% | == | all body sections present |
| industry standard citations | >=2 | >= | PCI-DSS, OWASP, or equivalent |
| use case specificity | >=3 | >= | named ecommerce use cases |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p01_ev_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field = ecommerce_vertical | Kind field incorrect or missing |
| H04 | product_category field present and non-empty | Missing product category |
| H05 | PCI-DSS section present in body | No compliance section found |
| H06 | At least one recommendation engine pattern documented | Missing ML/recommendation content |
| H07 | At least one fraud detection mechanism described | Missing fraud prevention content |
| H08 | At least 3 ecommerce-domain use cases named | Fewer than 3 use cases or generic placeholders |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | PCI-DSS depth (tokenization, scope reduction, v4.0 specifics) | 0.20 | Full v4.0 coverage = 1.0, partial = 0.5, absent = 0 |
| D02 | Recommendation engine technical depth (algorithm, data signals) | 0.20 | Named algorithm + data signals = 1.0, generic = 0.5, absent = 0 |
| D03 | Fraud detection specificity (behavioral biometrics, velocity, ML model) | 0.20 | 3+ techniques named = 1.0, 1-2 = 0.5, absent = 0 |
| D04 | Checkout UX coverage (abandonment recovery, A/B, multi-currency) | 0.20 | All 3 = 1.0, 2 = 0.7, <2 = 0 |
| D05 | Industry citation quality (PCI-DSS, OWASP, Baymard, ACM RecSys) | 0.20 | >=3 citations = 1.0, 1-2 = 0.5, 0 = 0 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN | >=9.5 | Auto-publish to ecommerce vertical library |
| PUBLISH | >=8.0 | Publish after technical review |
| REVIEW | >=7.0 | Require domain expert review |
| REJECT | <7.0 | Reject and rebuild with missing sections |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Emergency platform migration content | Principal Engineer | documented in incident log |
| Regulatory compliance override | Security Lead | signed waiver + post-mortem |

## Examples

## Golden Example  
```yaml  
title: "Personalized Product Recommendations for Fashion E-Commerce"  
kind: ecommerce_vertical  
tools:  
  - recommendation_engine: "Adobe Sensei"  
  - cart_checkout: "Shopify Plus"  
  - pci_compliance: "Stripe (PCI-DSS Level 1)"  
  - fraud_detection: "Sift"  
use_case: "Dynamic product recommendations on checkout page to reduce cart abandonment"  
description: "A fashion retailer integrates Adobe Sensei's AI-driven recommendations with Shopify Plus, ensuring PCI-DSS compliance via Stripe and fraud prevention via Sift. Recommendations are displayed during checkout, increasing average order value by 18%."  
```  

## Anti-Example 1: Overlooking PCI-DSS Compliance  
```yaml  
title: "Basic Payment Integration Without Compliance"  
kind: ecommerce_vertical  
tools:  
  - payment_gateway: "PayPal (non-PCI-DSS compliant)"  
  - cart_checkout: "WooCommerce"  
use_case: "Checkout process using PayPal without encryption"  
description: "A small retailer uses WooCommerce with PayPal, ignoring PCI-DSS requirements. Data breaches occur due to unencrypted payment fields, leading to legal penalties and loss of customer trust."  
```  
## Why it fails: Failing to use PCI-compliant tools exposes sensitive data, violating industry standards and risking legal action.  

## Anti-Example 2: Neglecting Fraud Detection  
```yaml  
title: "No Fraud Tools in High-Risk Market"  
kind: ecommerce_vertical  
tools:  
  - cart_checkout: "BigCommerce"  
  - recommendation_engine: "Algolia"  
use_case: "No fraud checks during checkout"  
description: "An electronics retailer uses BigCommerce and Algolia but lacks fraud detection. Chargeback rates spike at 25% due to bot-driven fake orders, eroding profit margins."  
```  
## Why it fails: Absence of fraud prevention tools leads to financial losses and compromised user experience from account takeovers.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
