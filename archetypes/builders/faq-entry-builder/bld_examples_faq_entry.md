---
kind: examples
id: bld_examples_faq_entry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of faq_entry artifacts
quality: 8.9
title: "Examples Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, examples]
tldr: "Golden and anti-examples of faq_entry artifacts"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
