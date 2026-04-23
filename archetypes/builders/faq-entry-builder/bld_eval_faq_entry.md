---
kind: quality_gate
id: p01_qg_faq_entry
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for faq_entry
quality: 9.0
title: "Quality Gate Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for faq_entry"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_faq_entry
  - bld_examples_integration_guide
  - p11_qg_audit_log
  - p05_qg_github_issue_template
  - bld_instruction_faq_entry
  - p11_qg_white_label_config
  - p09_qg_marketplace_app_manifest
  - p07_qg_benchmark_suite
  - p08_qg_capability_registry
  - p01_qg_agentic_rag
---

## Quality Gate

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| support_deflection_metric | 20% | > | per entry |
| canonical answer length | <=150 words | <= | answer field |
| required field completeness | 100% | == | all frontmatter fields |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches ^p01_faq_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field = faq_entry | Kind field incorrect or missing |
| H04 | question field exists and is non-empty | Missing or empty question |
| H05 | answer field exists and is non-empty | Missing or empty canonical answer |
| H06 | related_topics array present and non-empty | Missing related topics list |
| H07 | support_deflection_metric is numeric | Non-numeric value or absent |
| H08 | Schema.org FAQPage snippet present in output | Missing structured data |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Question clarity (imperative verb, user language, specific) | 0.20 | All 3 criteria met = 1.0, 2 = 0.6, <2 = 0 |
| D02 | Answer completeness (resolves root cause, no follow-up needed) | 0.20 | Full resolution = 1.0, partial = 0.5, vague = 0 |
| D03 | Schema.org FAQPage compliance (correct type, acceptedAnswer) | 0.20 | Fully compliant = 1.0, partial = 0.5, absent = 0 |
| D04 | Support deflection metric present and quantified | 0.15 | Numeric with % = 1.0, present unquantified = 0.5, absent = 0 |
| D05 | Related topics coverage (>=2 valid links) | 0.15 | >=2 = 1.0, 1 = 0.5, 0 = 0 |
| D06 | Accessibility (no jargon, plain language, WCAG compliant) | 0.10 | All criteria met = 1.0, partial = 0.5 |

## Actions
| Label | Score | Action |
|-------|-------|--------|
| GOLDEN | >=9.5 | Auto-publish, no review |
| PUBLISH | >=8.0 | Publish after editorial approval |
| REVIEW | >=7.0 | Require editorial review |
| REJECT | <7.0 | Reject, rework required |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Urgent support fix (<2h deadline) | Senior Editor | Incident ticket ID |
| Legacy entry critical update | Product Manager | Change log entry |

## Examples

## Golden Example
```yaml
kind: faq_entry
title: How do I update my payment method on Stripe?
body: |
  To update your payment method on Stripe, log in to your account, navigate to the **Payment Methods** section under **Account Settings**, and select **Edit** next to the method you wish to update. Follow the prompts to enter new card details or update existing information. Changes are saved automatically.
related_links:
  - https://stripe.com/docs/payments/accept-a-payment
  - https://stripe.com/docs/faq
support_deflection_metric: 85%
```

## Anti-Example 1: Missing Support Deflection Metric
```yaml
kind: faq_entry
title: How do I update my payment method on Stripe?
body: |
  To update your payment method on Stripe, log in to your account, navigate to the **Payment Methods** section under **Account Settings**, and select **Edit** next to the method you wish to update. Follow the prompts to enter new card details or update existing information. Changes are saved automatically.
related_links:
  - https://stripe.com/docs/payments/accept-a-payment
  - https://stripe.com/docs/faq
```
## Why it fails explanation
The entry lacks a **support_deflection_metric**, making it impossible to measure how effectively the FAQ resolves user issues without contacting support. This metric is critical for evaluating the FAQ's impact on customer service load.

## Anti-Example 2: Using Knowledge Card Structure
```yaml
kind: faq_entry
title: How do I update my payment method on Stripe?
body: |
  **Overview**: Updating payment methods on Stripe is essential for maintaining accurate billing information.  
  **Steps**:  
  1. Log in to your Stripe account.  
  2. Go to **Account Settings** > **Payment Methods**.  
  3. Click **Edit** next to the method you want to update.  
  4. Save changes.  
  **Related**: [Stripe Docs](https://stripe.com/docs)
```
## Why it fails explanation
The entry mimics a **knowledge_card** structure with bullet points and sections, which is broader and less focused than a **faq_entry**. This makes it unsuitable for direct user queries and conflates purposes, violating the boundary requirement.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
