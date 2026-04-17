---
kind: examples
id: bld_examples_integration_guide
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of integration_guide artifacts
quality: 9.1
title: "Examples Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, examples]
tldr: "Golden and anti-examples of integration_guide artifacts"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
---
title: "Stripe + AWS Integration Guide for SaaS Platforms"
description: "End-to-end integration guide for connecting Stripe payments with AWS infrastructure for enterprise SaaS onboarding"
audience: "Platform partners, enterprise account managers"
tags: ["payment-processing", "cloud-integration", "onboarding"]

# Stripe & AWS Integration Guide

## Overview
This guide enables seamless integration between Stripe's payment processing and AWS infrastructure for enterprise SaaS onboarding. Targeting organizations requiring PCI-DSS compliance and automated scaling.

## Prerequisites
- Stripe account with API keys (live/test)
- AWS account with IAM roles configured
- Node.js 16+ environment

## Integration Steps
1. **API Setup**
   Configure Stripe Webhook endpoints in AWS API Gateway with Lambda triggers for real-time payment events.

2. **Data Pipeline**
   Use AWS Glue to transform Stripe's JSON events into Parquet format for storage in S3.

3. **Security**
   Implement AWS KMS encryption for payment data at rest, with IAM policies restricting access to payment data.

4. **Monitoring**
   Set up CloudWatch metrics for payment processing latency and error rates.

## Best Practices
- Use Stripe's Radar for fraud detection before AWS processing
- Implement automated scaling in EC2 for high-volume payment periods
- Maintain audit logs in CloudTrail for compliance

## Support
Contact Stripe's enterprise team at enterprise-support@stripe.com and AWS support via AWS Premium Support.

---
## Anti-Example 1: Vague Implementation
---
title: "Generic Payment Integration Guide"
description: "Basic integration steps for payment systems"
audience: "Developers"
tags: ["payments"]

# Payment Integration Guide

## Overview
This guide helps integrate payment systems with your platform.

## Steps
1. Get API keys from your provider
2. Make API calls to process payments
3. Handle webhooks for payment confirmation

## Notes
- Use HTTPS
- Store secrets securely

---
## Why it fails
Lacks specificity about vendors, implementation details, and enterprise requirements. No concrete examples or technical depth for platform partners.

## Anti-Example 2: API Reference Contamination
---
title: "Stripe Integration Guide"
description: "How to use Stripe API"
audience: "Developers"
tags: ["stripe"]

# Stripe Integration Guide

## API Endpoints
- POST /v1/charges (Create charge)
- GET /v1/customers (List customers)

## Parameters
- amount (integer, required)
- currency (string, 3-letter ISO code)
- description (string, max 255 chars)

## Example
```json
{
  "amount": 1000,
  "currency": "usd",
  "description": "Monthly subscription"
}
```

---
## Why it fails
Focuses on API reference content (endpoints, parameters, schema examples) rather than integration workflow, security considerations, or enterprise onboarding processes.
