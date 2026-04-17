---
kind: examples
id: bld_examples_subscription_tier
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of subscription_tier artifacts
quality: 8.8
title: "Examples Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, examples]
tldr: "Golden and anti-examples of subscription_tier artifacts"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
---
kind: subscription_tier
name: Notion Team Plan
provider: Notion
pricing: "$15/user/month"
features:
  - Unlimited pages
  - Collaborative editing
  - Priority support
  - 5GB storage
billing_cycle: monthly
limitations:
  - No advanced analytics
  - Limited integrations

Notion's Team Plan offers scalable collaboration tools for small teams. Pricing is transparent with a monthly billing cycle. Features include real-time editing and storage, but lacks advanced analytics for data-driven teams.

## Anti-Example 1: Missing Pricing
---
kind: subscription_tier
name: Slack Premium
provider: Slack
features:
  - Unlimited messages
  - Custom emojis
  - Advanced security
billing_cycle: annual

## Why it fails: No pricing details make the tier definition incomplete. Users cannot evaluate cost-benefit without knowing the price.

## Anti-Example 2: Content Monetization Mix
---
kind: subscription_tier
name: Substack Creator Tier
provider: Substack
pricing: "$10/reader/month"
features:
  - Custom domain
  - Email analytics
  - Affiliate program access
billing_cycle: yearly

## Why it fails: Focuses on content monetization (affiliate programs) rather than SaaS subscription features. Violates boundary conditions by conflating pricing models.
